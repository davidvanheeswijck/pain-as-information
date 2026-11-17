#!/usr/bin/env python3
"""S-1b driver: re-tuned T-junction model, rate versus pattern.

Pre-registration: PREDICTION.md (commit #1).  S-1's code is imported unchanged
(tjmodel, engine, protocol) or reused by import (simulate_s001 tasks); what is
new here is the tuning search, the ensemble built around the selected sets, the
regular 2 Hz condition and two-pulse following frequency for the held-out
validation, and a 30 s visual-traces file.

Stages (resumable: a per-model file that exists is never recomputed):
  tune       Latin-hypercube search (round 1, round 2 if needed), selection
  control    canonical following frequencies of the selected sets (dt, dt/2, mutation)
  accept     variants around the selected sets, accepted on following frequency + drivability
  det        regular 2/4/20/40/60/80 Hz and burst at 1.0x and 1.5x, plus probe-only baseline
  stoch      Poisson and jitter, many seeds, on the subsample
  tests      10 Hz / 5 Hz test trains and the drive-matched diagnostic
  ab         Abeta comparator population
  converge   dt halving on 10 models
  val        held-out validation V2: two-pulse following frequency
  visual     visual-traces.json
  aggregate  results.json / results.md / PNGs

  python simulate_s001b.py --pilot             # smoke test, writes results/pilot/ only
  python simulate_s001b.py                     # full run, results/main/
  (resume: the same command; cached per-model files are reused)
"""

import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
S1 = os.path.join(os.path.dirname(HERE), "S-001-tjunction-rate-vs-pattern")
sys.path.insert(0, S1)
sys.path.insert(0, HERE)

import tjmodel  # noqa: E402  (S-1, unchanged)
import engine  # noqa: E402
import protocol as P  # noqa: E402
import tuning as TU  # noqa: E402
from simulate_s001 import (  # noqa: E402  (S-1 tasks reused by import)
    AMPS, FOLLOW_RANGE, PROBE_HZ, jclean, load, one_run, sample_a, save, task_ab,
    task_converge, task_stoch, task_tests, thresholds,
)

DET_PATTERNS = ("reg2", "reg4", "reg20", "reg40", "reg60", "reg80", "burst")
MAX_CANDIDATES = 600
STAND_IN = dict(nav=0.0385, nav_soma=0.02, kv=0.04, kcnq=0.0015, gsk=0.02, gcal=0.00025,
                sk_tau=1500.0, diam_stem=1.4, sk_stem=False)   # pilot only: S-1's SK configuration


def log(msg, fh):
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    if fh:
        fh.write(line + "\n")
        fh.flush()


def factory(params, **over):
    p = dict(params)
    p.update(over)
    return lambda: tjmodel.CNeuron(**p)


# --- tuning tasks -----------------------------------------------------------

def task_tune(args):
    """One search candidate, as a funnel with early exit (PREDICTION.md, 'Search method')."""
    path, cid, params, dt, T = args
    if os.path.exists(path):
        return load(path)
    t0 = time.time()
    rec = dict(id=cid, params=params, ff={}, stage=None, calibrated=False, meets=False)
    ff = rec["ff"]
    ff["na_k"] = engine.following_frequency(factory(params, kcnq=0.0, gsk=0.0), dt)
    if not TU.in_band("na_k", ff["na_k"]):
        rec["stage"] = "na_k_band"
    else:
        ff["kcnq"] = engine.following_frequency(factory(params, gsk=0.0), dt)
        if not TU.in_band("kcnq", ff["kcnq"]):
            rec["stage"] = "kcnq_band"
        else:
            ff["sk"] = engine.following_frequency(factory(params), dt)
            rec["sk_in_band"] = TU.in_band("sk", ff["sk"])
            lo, hi = TU.SK_ACCEPT_RANGE
            if not (lo <= ff["sk"] <= hi):
                rec["stage"] = "sk_range"
            else:
                f = factory(params)
                lat = engine.measure_latencies(f, dt)
                rest, drive = thresholds(f, dt)
                if lat is None or drive is None:
                    rec["stage"] = "undrivable"
                else:
                    res = one_run(f, lat, "reg20", 1.5 * drive, T, PROBE_HZ, 7000 + cid, dt)
                    flags = TU.block_flags(res)
                    J, d = TU.score_J(ff, flags)
                    rec.update(stage="calibrated", calibrated=True, rest_thr=rest, drive_thr=drive,
                               run=res, flags=flags, J=J, d=d,
                               meets=TU.meets_targets(ff, flags))
    rec["wall_s"] = time.time() - t0
    save(path, rec)
    return rec


def task_check(args):
    """G1 for a candidate: following frequencies at dt/2 and the SK-removed mutation."""
    path, cid, params, dt = args
    if os.path.exists(path):
        return load(path)
    half = dt / 2
    ff = dict(
        na_k=engine.following_frequency(factory(params, kcnq=0.0, gsk=0.0), half),
        kcnq=engine.following_frequency(factory(params, gsk=0.0), half),
        sk=engine.following_frequency(factory(params), half))
    mut = engine.following_frequency(factory(params, gsk=0.0), dt)
    rec = dict(id=cid, params=params, dt_half=half, ff_half=ff, mutation_ff=mut,
               pass_dt_half=bool(all(TU.in_band(n, ff[n]) for n in TU.TARGET_HZ)),
               pass_mutation=bool(not TU.in_band("sk", mut)))
    rec["pass"] = bool(rec["pass_dt_half"] and rec["pass_mutation"])
    save(path, rec)
    return rec


def run_tuning(pool, out, n1, n2_per, T, dt, workers, fh):
    """Round 1; round 2 if fewer than 3 candidates meet the targets; selection.
    Deterministic from the per-candidate files, so a resume recomputes only what is missing."""
    tdir = os.path.join(out, "tuning")
    c1 = TU.round1_candidates(n1)
    log(f"tune: round 1, {len(c1)} candidates", fh)
    jobs = [(os.path.join(tdir, "r1", f"c{i:04d}.json"), i, p, dt, T) for i, p in enumerate(c1)]
    for n, r in enumerate(pool.imap_unordered(task_tune, jobs)):
        if (n + 1) % 10 == 0 or n + 1 == len(jobs):
            log(f"tune r1: {n + 1}/{len(jobs)}", fh)
    r1 = [load(j[0]) for j in jobs]
    meeting = [r for r in r1 if r["meets"]]
    cal = sorted((r for r in r1 if r["calibrated"]), key=lambda r: r["J"])
    centres, r2 = [], []
    round2 = len(meeting) < 3 and len(cal) > 0
    if round2:
        centres = cal[:TU.N_CENTRES]
        c2 = TU.round2_candidates([c["params"] for c in centres], n2_per)
        log(f"tune: round 2, {len(c2)} candidates around {len(centres)} centre(s) (ids {[c['id'] for c in centres]})", fh)
        jobs2 = [(os.path.join(tdir, "r2", f"c{1000 + i:04d}.json"), 1000 + i, p, dt, T) for i, p in enumerate(c2)]
        for n, r in enumerate(pool.imap_unordered(task_tune, jobs2)):
            if (n + 1) % 10 == 0 or n + 1 == len(jobs2):
                log(f"tune r2: {n + 1}/{len(jobs2)}", fh)
        r2 = [load(j[0]) for j in jobs2]
    allr = r1 + r2
    meeting = sorted((r for r in allr if r["meets"]), key=lambda r: (r["J"], r["id"]))
    # selection: lowest J first, must also pass the dt/2 check and the mutation check
    selected, checks, i = [], [], 0
    while len(selected) < TU.N_CENTRES and i < len(meeting):
        chunk = meeting[i:i + TU.N_CENTRES]
        i += len(chunk)
        res = pool.map(task_check, [(os.path.join(tdir, "check", f"c{r['id']:04d}.json"), r["id"], r["params"], dt) for r in chunk])
        for r, c in zip(chunk, res):
            checks.append(c)
            if c["pass"] and len(selected) < TU.N_CENTRES:
                selected.append(dict(id=r["id"], params=r["params"], J=r["J"], ff=r["ff"], flags=r["flags"],
                                     run=r["run"], drive_thr=r["drive_thr"], check=c))
    sel = dict(n_round1=len(r1), n_round2=len(r2), round2_ran=bool(round2), centres=[c["id"] for c in centres],
               n_meeting_targets=len(meeting), checks=checks, sets=selected, T=T, dt=dt)
    save(os.path.join(tdir, "selected.json"), sel)
    log(f"tune: {len(meeting)} candidate(s) meet the targets, {len(selected)} selected", fh)
    return sel


# --- ensemble ---------------------------------------------------------------

def sample_variant(i, sets):
    """Variant i around selected set (i mod K); PREDICTION.md 'Ensemble'."""
    r = np.random.default_rng(30_000 + i)
    s = sets[i % len(sets)]
    u = lambda lo, hi: float(r.uniform(lo, hi))
    lg = lambda: float(np.exp(r.uniform(np.log(0.67), np.log(1.5))))
    return dict(
        nav=s["nav"] * u(0.97, 1.03), nav_soma=s["nav_soma"] * u(0.90, 1.10), kv=s["kv"] * u(0.95, 1.05),
        diam_stem=s["diam_stem"] * u(0.93, 1.07), kcnq=s["kcnq"] * lg(), gsk=s["gsk"] * lg(),
        gcal=s["gcal"] * lg(), sk_tau=s["sk_tau"] * lg(), sk_stem=bool(s["sk_stem"]), L_stem=75.0)


def task_accept(args):
    path, i, params, dt = args
    if os.path.exists(path):
        return load(path)
    t0 = time.time()
    f = factory(params)
    ff = engine.following_frequency(f, dt)
    in_range = bool(FOLLOW_RANGE[0] <= ff <= FOLLOW_RANGE[1])
    rest = drive = None
    if in_range:
        rest, drive = thresholds(f, dt)
    rec = dict(i=i, params=params, ff=ff, in_range=in_range, rest_thr=rest, drive_thr=drive,
               accepted=bool(in_range and drive is not None), wall_s=time.time() - t0)
    save(path, rec)
    return rec


def task_det(args):
    path, k, params, rest, drive, T, dt = args
    if os.path.exists(path):
        return load(path)
    f = factory(params)
    t0 = time.time()
    lat = engine.measure_latencies(f, dt)
    rec = dict(k=k, params=params, lat=lat, rest_thr=rest, drive_thr=drive, T=T, runs={})
    ps = 1000 + k
    rec["runs"]["none"] = one_run(f, lat, None, 0.0, T, PROBE_HZ, ps, dt)
    for amp in AMPS:
        for pat in DET_PATTERNS:
            rec["runs"][f"{pat}@{amp}"] = one_run(f, lat, pat, amp * drive, T, PROBE_HZ, ps, dt)
    rec["wall_s"] = time.time() - t0
    save(path, rec)
    return rec


def task_val(args):
    """V2: two-pulse following frequency (the 21-pulse value is in the candidate file)."""
    path, k, params, ff21, dt = args
    if os.path.exists(path):
        return load(path)
    ff2 = engine.following_frequency(factory(params), dt, npulse=2)
    rec = dict(k=k, ff2=ff2, ff21=ff21)
    save(path, rec)
    return rec


def task_visual(args):
    """30 s voltage traces for one model: none, regular 20 Hz, regular 80 Hz, burst."""
    path, params, drive, label, T, dt = args
    if os.path.exists(path):
        return load(path)
    every = 1.0
    out = dict(
        description=("Voltage traces for one C-neuron model (" + label + "). Time in ms from the start of the run "
                     "(stimulation starts at 200 ms); voltage in mV rounded to 0.1, sampled every 1 ms (a 1 ms "
                     "spike is under-sampled: this file shows slow state, not spike shapes). Model units; "
                     "intracellular current injected at the mid-stem of a simplified model, not a clinical "
                     "amplitude or a stimulation setting. stim_times are the 1 ms pulses at the mid-stem; "
                     "test_times are the peripheral probe pulses (2 Hz mean)."),
        dt_ms=dt, sample_every_ms=every, window_ms=[0.0, T], probe_hz=PROBE_HZ,
        stimulus_amplitude_nA=1.5 * drive, params=params, conditions={})
    f = factory(params)
    lat = engine.measure_latencies(f, dt)
    for name, pat, amp in (("no_stimulation", None, 0.0), ("regular_20Hz", "reg20", 1.5 * drive),
                           ("regular_80Hz", "reg80", 1.5 * drive), ("burst_5x100Hz_per_250ms", "burst", 1.5 * drive)):
        st = P.make_pattern(pat, 1, T) if pat else np.array([])
        tt = P.test_times(1000, PROBE_HZ, T)
        rig = engine.Rig(f(), dt)
        o = rig.run(st, amp, tt, T + 10.0, traces=dict(every=every, sites=["soma", "tj", "central"]))
        sc = P.score(o, tt, lat, T)
        tr = o["traces"]
        out["conditions"][name] = dict(
            stim_times=st.round(2).tolist(), test_times=tt.round(2).tolist(), F_in_window=sc["F"],
            n_scored=sc["n_scored"], soma_mV=np.round(tr["soma"], 1).tolist(),
            tjunction_mV=np.round(tr["tj"], 1).tolist(), central_mV=np.round(tr["central"], 1).tolist())
    save(path, out)
    return out


# --- orchestration -----------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pilot", action="store_true", help="small run; writes results/pilot/ only")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--stages", default="tune,control,accept,det,stoch,tests,ab,converge,val,visual,aggregate")
    ap.add_argument("--outdir", default=None)
    a = ap.parse_args()

    if a.pilot:
        N, T, NSUB, NSEED, NAB, TCONV, NCONV = 12, 8000.0, 4, 3, 4, 3000.0, 3
        N1, N2PER, TTUNE, MAXC = 16, 2, 12000.0, 60
        sub = "pilot"
    else:
        N, T, NSUB, NSEED, NAB, TCONV, NCONV = 200, 30000.0, 30, 20, 30, 10000.0, 10
        N1, N2PER, TTUNE, MAXC = TU.N1, TU.N2 // TU.N_CENTRES, 30000.0, MAX_CANDIDATES
        sub = "main"
    out = a.outdir or os.path.join(HERE, "results", sub)
    base = os.path.basename(os.path.normpath(out))
    if not a.pilot and base != "main":
        raise SystemExit("refusing: non-pilot run must write to results/main")
    if a.pilot and base == "main":
        raise SystemExit("refusing: --pilot must never write to results/main")
    os.makedirs(out, exist_ok=True)
    fh = open(os.path.join(out, "run.log"), "a")
    stages = a.stages.split(",")
    dt = 0.025
    from multiprocessing import Pool
    pool = Pool(a.workers)
    t_start = time.time()
    log(f"start {sub} N={N} T={T} N1={N1} stages={stages} workers={a.workers}", fh)
    tdir = os.path.join(out, "tuning")

    # --- tuning -------------------------------------------------------------
    if "tune" in stages:
        sel = run_tuning(pool, out, N1, N2PER, TTUNE, dt, a.workers, fh)
    else:
        sel = load(os.path.join(tdir, "selected.json"))
    sets = [s["params"] for s in sel["sets"]]
    stand_in = False
    if not sets and a.pilot:
        sets, stand_in = [dict(STAND_IN)], True
        log("PILOT ONLY: no candidate met the targets; using S-1's SK configuration as a stand-in set "
            "so that the later stages are exercised (it is not a selected set)", fh)
    if stand_in:
        save(os.path.join(tdir, "stand_in.json"), dict(stand_in=True, params=sets[0]))
    if not sets:
        log("no set meets the calibration targets: no ensemble, no pattern runs (PREDICTION.md)", fh)
        # visual traces for the best-J calibrated candidate, labelled, so the failure can be inspected
        best = None
        for d in ("r1", "r2"):
            for fn in sorted(os.listdir(os.path.join(tdir, d))) if os.path.isdir(os.path.join(tdir, d)) else []:
                r = load(os.path.join(tdir, d, fn))
                if r.get("calibrated") and (best is None or r["J"] < best["J"]):
                    best = r
        if best is not None and "visual" in stages:
            pool.apply(task_visual, ((os.path.join(out, "visual-traces.json"), best["params"], best["drive_thr"],
                                      f"the best-scoring candidate, id {best['id']}, J = {best['J']:.3f}; it does NOT meet the "
                                      "calibration targets", 30000.0, dt),))
        pool.close()
        pool.join()
        log(f"done in {(time.time() - t_start) / 60:.1f} min", fh)
        if "aggregate" in stages:
            import aggregate_s001b
            aggregate_s001b.main(out, pilot=a.pilot)
            zip_per_model(out, fh)
        return

    # --- control (selected sets) -------------------------------------------
    ctl = dict(sets=[dict(id=s["id"], ff=s["ff"], check=s["check"]) for s in sel["sets"]])
    if stand_in:
        ctl = dict(sets=[], stand_in=True)
    save(os.path.join(out, "control.json"), ctl)

    # --- accept -------------------------------------------------------------
    from collections import deque
    cand_dir = os.path.join(out, "cand")
    accepted = []
    inflight = deque()
    nxt = n_done = 0
    while len(accepted) < N and (nxt < MAXC or inflight):
        while nxt < MAXC and len(inflight) < a.workers * 2:
            inflight.append(pool.apply_async(task_accept, ((os.path.join(cand_dir, f"c{nxt:04d}.json"), nxt,
                                                            sample_variant(nxt, sets), dt),)))
            nxt += 1
        r = inflight.popleft().get()
        n_done += 1
        if r["accepted"]:
            accepted.append(r)
        if n_done % 10 == 0 or len(accepted) == N:
            log(f"accept: {len(accepted)}/{N} accepted after {n_done} candidates", fh)
    n_cand_used = max((r["i"] for r in accepted), default=-1) + 1 if len(accepted) >= N else n_done
    cands = [load(os.path.join(cand_dir, f"c{j:04d}.json")) for j in range(n_cand_used)]
    save(os.path.join(out, "accept_summary.json"), dict(
        n_accepted=len(accepted), n_target=N, n_candidates_considered=n_cand_used, max_candidates=MAXC,
        range_hz=FOLLOW_RANGE, ff=[r["ff"] for r in accepted],
        set_of_accepted=[r["i"] % len(sets) for r in accepted],
        n_in_range=sum(1 for c in cands if c["in_range"]),
        n_in_range_undrivable=sum(1 for c in cands if c["in_range"] and c["drive_thr"] is None),
        ff_all_candidates=[c["ff"] for c in cands]))
    if len(accepted) < N:
        log(f"only {len(accepted)} accepted in {n_cand_used} candidates (< {N}): NO VERDICT by rule", fh)
    accepted = accepted[:N]

    mdir = os.path.join(out, "model")
    if "det" in stages:
        jobs = [(os.path.join(mdir, f"m{k:03d}.json"), k, r["params"], r["rest_thr"], r["drive_thr"], T, dt)
                for k, r in enumerate(accepted)]
        done = 0
        for r in pool.imap_unordered(task_det, jobs):
            done += 1
            if done % 5 == 0 or done == len(jobs):
                log(f"det: {done}/{len(jobs)}", fh)
    det = {}
    for k in range(len(accepted)):
        pth = os.path.join(mdir, f"m{k:03d}.json")
        if os.path.exists(pth):
            det[k] = load(pth)
    sub_idx = [k for k in range(min(NSUB, len(accepted))) if k in det]

    if "stoch" in stages or "tests" in stages:
        jobs_s = [(os.path.join(out, "stoch", f"m{k:03d}.json"), k, det[k]["params"], det[k]["drive_thr"],
                   det[k]["lat"], T, dt, NSEED) for k in sub_idx]
        jobs_t = [(os.path.join(out, "tests", f"m{k:03d}.json"), k, det[k]["params"], det[k]["drive_thr"],
                   det[k]["lat"], T, dt, NSEED) for k in sub_idx]
        pend = []
        if "stoch" in stages:
            pend += [(task_stoch, j) for j in jobs_s]
        if "tests" in stages:
            pend += [(task_tests, j) for j in jobs_t]
        pend.sort(key=lambda x: 0 if x[0] is task_stoch else 1)
        res = [pool.apply_async(fn, (j,)) for fn, j in pend]
        for n, r in enumerate(res):
            r.get()
            log(f"stoch/tests: {n + 1}/{len(res)}", fh)

    if "ab" in stages:
        jobs = [(os.path.join(out, "ab", f"a{j:03d}.json"), j, sample_a(j), T, dt, j) for j in range(NAB)]
        for n, r in enumerate(pool.imap_unordered(task_ab, jobs)):
            if (n + 1) % 5 == 0 or n + 1 == len(jobs):
                log(f"ab: {n + 1}/{len(jobs)}", fh)

    if "converge" in stages:
        jobs = []
        for k in sub_idx[:NCONV]:
            for d in (0.025, 0.0125):
                jobs.append((os.path.join(out, "converge", f"m{k:03d}_dt{d}.json"), k, det[k]["params"],
                             det[k]["drive_thr"], det[k]["lat"], d, TCONV))
        for n, r in enumerate(pool.imap_unordered(task_converge, jobs)):
            log(f"converge: {n + 1}/{len(jobs)}", fh)

    if "val" in stages:
        jobs = [(os.path.join(out, "val", f"m{k:03d}.json"), k, accepted[k]["params"], accepted[k]["ff"], dt)
                for k in sorted(det)]
        for n, r in enumerate(pool.imap_unordered(task_val, jobs)):
            if (n + 1) % 20 == 0 or n + 1 == len(jobs):
                log(f"val: {n + 1}/{len(jobs)}", fh)

    if "visual" in stages and det:
        ks = sorted(det)
        ffs = np.array([accepted[k]["ff"] for k in ks])
        rep = ks[int(np.argmin(np.abs(ffs - np.median(ffs))))]
        pool.apply(task_visual, ((os.path.join(out, "visual-traces.json"), det[rep]["params"], det[rep]["drive_thr"],
                                  f"accepted variant k={rep}, the one closest to the median following frequency", 30000.0, dt),))
        log(f"visual: representative model k={rep} ff={accepted[rep]['ff']:.1f}", fh)

    pool.close()
    pool.join()
    log(f"done in {(time.time() - t_start) / 60:.1f} min", fh)
    if "aggregate" in stages:
        import aggregate_s001b
        aggregate_s001b.main(out, pilot=a.pilot)
        zip_per_model(out, fh)


def zip_per_model(out, fh):
    """One zip of the per-model files (the directories are gitignored: ~1,000 small files hit
    GitHub's diff limit)."""
    import zipfile
    zp = os.path.join(out, "per-model-files.zip")
    with zipfile.ZipFile(zp, "w", zipfile.ZIP_DEFLATED) as z:
        for d in ("tuning", "cand", "model", "stoch", "tests", "ab", "converge", "val"):
            for root, _, files in os.walk(os.path.join(out, d)):
                for fn in sorted(files):
                    full = os.path.join(root, fn)
                    z.write(full, os.path.relpath(full, out))
    log(f"wrote {os.path.relpath(zp, out)}", fh)


if __name__ == "__main__":
    main()
