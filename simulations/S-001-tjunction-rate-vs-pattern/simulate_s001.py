#!/usr/bin/env python3
"""S-1 driver: T-junction filtering, rate versus pattern.

Stages (all resumable: a per-model result file that exists is never recomputed):
  control    positive control: Sundt following frequencies on the canonical sets,
             and the SK-removed mutation
  accept     rejection-sample C-neuron variants until N are accepted (cand/)
  det        regular 4/20/40/60/80 Hz and burst at 1.0x and 1.5x, plus probe-only baseline
  stoch      Poisson and jitter, many seeds, 1.0x and 1.5x, on the subsample
  tests      pre-registered 10 Hz / 5 Hz test trains and the drive-matched diagnostic
  ab         Abeta comparator population
  converge   dt halving on 10 models
  visual     visual-traces.json for one representative accepted model
  aggregate  results.json / results.md / PNGs (aggregate_s001.py)

  python simulate_s001.py --pilot            # smoke test, writes results/pilot/ only
  python simulate_s001.py                    # full run, results/main/
  python simulate_s001.py --stages det,stoch # subset (resume with the same command)
"""

import argparse
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import tjmodel  # noqa: E402
import engine  # noqa: E402
import protocol as P  # noqa: E402

CONFIG_NA_K = dict(kcnq=0.0, gsk=0.0)
CONFIG_KCNQ = dict(kcnq=0.0015, gsk=0.0)
CONFIG_SK = dict(kcnq=0.0015, gsk=0.02, sk_tau=1500.0)
CANON_BANDS = {"na_k": (110, CONFIG_NA_K), "kcnq": (30, CONFIG_KCNQ), "sk": (6, CONFIG_SK)}
FOLLOW_RANGE = (2.0, 40.0)   # accepted unstimulated following frequency, Hz
TIGHT_RANGE = (2.0, 15.0)    # sensitivity cut
AMPS = (1.0, 1.5)
DET_PATTERNS = ("reg4", "reg20", "reg40", "reg60", "reg80", "burst")
PROBE_HZ = 2.0


def jclean(o):
    if isinstance(o, dict):
        return {k: jclean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jclean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        return None if not np.isfinite(o) else float(o)
    if isinstance(o, np.integer):
        return int(o)
    return o


def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(jclean(obj), f)
    os.replace(tmp, path)


def load(path):
    with open(path) as f:
        return json.load(f)


# --- ensembles --------------------------------------------------------------

def sample_c(i):
    r = np.random.default_rng(10_000 + i)
    return dict(
        nav=float(r.uniform(0.0365, 0.0405)),
        diam_stem=float(r.uniform(1.3, 1.5)),
        kcnq=float(np.exp(r.uniform(np.log(0.0008), np.log(0.003)))),
        gsk=float(np.exp(r.uniform(np.log(0.01), np.log(0.04)))),
        sk_tau=float(r.uniform(800.0, 2500.0)),
        L_stem=75.0,
    )


def sample_a(j):
    r = np.random.default_rng(20_000 + j)
    return dict(
        diam_axon=float(r.uniform(4.0, 7.0)), nav_node=float(r.uniform(0.4, 0.7)),
        L_int=float(r.uniform(300.0, 500.0)), diam_stem=float(r.uniform(2.5, 3.5)),
        nav_stem=float(r.uniform(0.08, 0.16)),
    )


# --- per-run helper -----------------------------------------------------------

def one_run(factory, lat, pat, amp_nA, T, probe_hz, probe_seed, dt, pat_seed=1):
    st = P.make_pattern(pat, pat_seed, T) if pat else np.array([])
    tt = P.test_times(probe_seed, probe_hz, T)
    rig = engine.Rig(factory(), dt)
    out = rig.run(st, amp_nA, tt, T + 100.0)
    res = P.score(out, tt, lat, T)
    res["n_pulses"] = int(len(st))
    return res


# --- tasks (top-level for multiprocessing) -------------------------------------

def task_accept(args):
    path, i, dt = args
    if os.path.exists(path):
        return load(path)
    p = sample_c(i)
    t0 = time.time()
    f = lambda: tjmodel.CNeuron(**p)
    ff = engine.following_frequency(f, dt)
    in_range = bool(FOLLOW_RANGE[0] <= ff <= FOLLOW_RANGE[1])
    rest = drive = None
    if in_range:
        rest, drive = thresholds(f, dt)
    rec = dict(i=i, params=p, ff=ff, in_range=in_range, rest_thr=rest, drive_thr=drive,
               accepted=bool(in_range and drive is not None), wall_s=time.time() - t0)
    save(path, rec)
    return rec


def thresholds(f, dt):
    rest = P.stim_threshold(f, dt)
    drive = P.drive_threshold(f, rest, dt) if rest else None
    return rest, drive


def task_det(args):
    path, k, params, rest, drive, T, dt = args
    if os.path.exists(path):
        return load(path)
    f = lambda: tjmodel.CNeuron(**params)
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


def task_stoch(args):
    path, k, params, drive, lat, T, dt, nseed = args
    if os.path.exists(path):
        return load(path)
    f = lambda: tjmodel.CNeuron(**params)
    rec = dict(k=k, T=T, runs={})
    for amp in AMPS:
        for pat in ("poisson", "jitter"):
            for s in range(nseed):
                rec["runs"][f"{pat}@{amp}#{s}"] = one_run(
                    f, lat, pat, amp * drive, T, PROBE_HZ, 1000 + k, dt, pat_seed=1_000_000 + 1000 * k + s)
    save(path, rec)
    return rec


def task_tests(args):
    """Pre-registered 10 Hz / 5 Hz test trains (1.5x only) and the drive-matched diagnostic."""
    path, k, params, drive, lat, T, dt, nseed = args
    if os.path.exists(path):
        return load(path)
    f = lambda: tjmodel.CNeuron(**params)
    rec = dict(k=k, T=T, runs={})
    amp = 1.5
    ps = 1000 + k
    for hz in (10.0, 5.0):
        rec["runs"][f"none@probe{hz:g}"] = one_run(f, lat, None, 0.0, T, hz, ps, dt)
    for pat in ("reg20", "reg80", "burst"):
        rec["runs"][f"{pat}@probe10"] = one_run(f, lat, pat, amp * drive, T, 10.0, ps, dt)
    for pat in ("reg20", "reg80"):
        rec["runs"][f"{pat}@probe5"] = one_run(f, lat, pat, amp * drive, T, 5.0, ps, dt)
    for pat in ("poisson", "jitter"):
        for s in range(min(5, nseed)):
            rec["runs"][f"{pat}@probe10#{s}"] = one_run(
                f, lat, pat, amp * drive, T, 10.0, ps, dt, pat_seed=1_000_000 + 1000 * k + s)
    # drive-matched diagnostic (post hoc, labelled as such): reg80 at 1.5x of its own
    # steady-state drive threshold, 2 Hz probes
    rest = P.stim_threshold(f, dt)
    d80 = None
    st = P.regular(80.0, 4000.0)
    for m in P.THR_MULTS:
        rig = engine.Rig(f(), dt)
        out = rig.run(st, m * rest, [], 4050.0)
        sp = out["stem_pre"]
        late = st[st >= 2000.0]
        hit = sum(1 for t0 in late if not np.isnan(engine.first_in(sp, t0, t0 + 5.0)))
        if hit >= 0.9 * len(late):
            d80 = m * rest
            break
    rec["d80"] = d80
    if d80 is not None:
        rec["runs"]["reg80@drive80"] = one_run(f, lat, "reg80", amp * d80, T, PROBE_HZ, ps, dt)
    save(path, rec)
    return rec


def task_ab(args):
    path, j, params, T, dt, seed = args
    if os.path.exists(path):
        return load(path)
    f = lambda: tjmodel.ANeuron(**params)
    lat = engine.measure_latencies(f, dt)
    rec = dict(j=j, params=params, lat=lat, T=T, runs={})
    rest = P.stim_threshold(f, dt)
    rec["rest_thr"] = rest
    drive = P.drive_threshold(f, rest, dt) if rest else None
    rec["drive_thr"] = drive
    if drive is None or lat is None:
        rec["undrivable"] = True
        save(path, rec)
        return rec
    ps = 5000 + j
    rec["runs"]["none"] = one_run(f, lat, None, 0.0, T, PROBE_HZ, ps, dt)
    for amp in AMPS:
        for pat in DET_PATTERNS + ("poisson", "jitter"):
            rec["runs"][f"{pat}@{amp}"] = one_run(
                f, lat, pat, amp * drive, T, PROBE_HZ, ps, dt, pat_seed=2_000_000 + j)
    save(path, rec)
    return rec


def task_follow(args):
    name, params, dt = args
    f = lambda: tjmodel.CNeuron(**params)
    return dict(name=name, params=params, dt=dt, ff=engine.following_frequency(f, dt))


def task_converge(args):
    path, k, params, drive, lat, dt, T = args
    if os.path.exists(path):
        return load(path)
    f = lambda: tjmodel.CNeuron(**params)
    rec = dict(k=k, dt=dt, T=T, runs={})
    lat_dt = engine.measure_latencies(f, dt)
    for pat in ("reg20", "reg80", "burst"):
        rec["runs"][pat] = one_run(f, lat_dt, pat, 1.5 * drive, T, PROBE_HZ, 1000 + k, dt)
    save(path, rec)
    return rec


def task_visual(args):
    path, params, drive, ab_params, ab_drive, T, dt = args
    if os.path.exists(path):
        return load(path)
    every = 0.4
    window = (0.0, T)
    out = dict(
        description=("Voltage traces for one representative accepted C-neuron variant (and an A-beta "
                     "comparator at 20 Hz). Time in ms from the start of stimulation; voltage in mV "
                     "rounded to 0.1. stim_times are the 1 ms pulses at the mid-stem; test_times are "
                     "the peripheral probe pulses (2 Hz mean)."),
        dt_ms=dt, sample_every_ms=every, window_ms=window, probe_hz=PROBE_HZ,
        stimulus_amplitude_nA=dict(c_neuron=1.5 * drive, a_beta=1.5 * ab_drive),
        c_params=params, ab_params=ab_params, conditions={},
    )
    f = lambda: tjmodel.CNeuron(**params)
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
            stim_times=st.round(2).tolist(), test_times=tt.round(2).tolist(),
            F_in_window=sc["F"], n_scored=sc["n_scored"],
            soma_mV=np.round(tr["soma"], 1).tolist(), tjunction_mV=np.round(tr["tj"], 1).tolist(),
            central_mV=np.round(tr["central"], 1).tolist())
    fa = lambda: tjmodel.ANeuron(**ab_params)
    lat_a = engine.measure_latencies(fa, dt)
    st = P.make_pattern("reg20", 1, T)
    tt = P.test_times(5000, PROBE_HZ, T)
    rig = engine.Rig(fa(), dt)
    o = rig.run(st, 1.5 * ab_drive, tt, T + 10.0, traces=dict(every=every, sites=["soma", "tj", "central"]))
    sc = P.score(o, tt, lat_a, T)
    tr = o["traces"]
    out["conditions"]["abeta_regular_20Hz"] = dict(
        stim_times=st.round(2).tolist(), test_times=tt.round(2).tolist(), F_in_window=sc["F"],
        n_scored=sc["n_scored"], soma_mV=np.round(tr["soma"], 1).tolist(),
        tjunction_mV=np.round(tr["tj"], 1).tolist(), central_mV=np.round(tr["central"], 1).tolist())
    save(path, out)
    return out


# --- orchestration -----------------------------------------------------------

def log(msg, fh):
    line = time.strftime("%H:%M:%S ") + msg
    print(line, flush=True)
    if fh:
        fh.write(line + "\n")
        fh.flush()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pilot", action="store_true", help="20 models, 5 s; writes results/pilot/ only")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--stages", default="control,accept,det,stoch,tests,ab,converge,visual,aggregate")
    ap.add_argument("--models", type=int, default=None)
    ap.add_argument("--outdir", default=None)
    a = ap.parse_args()

    if a.pilot:
        N, T, NSUB, NSEED, NAB, TCONV, NCONV = 20, 5000.0, 5, 3, 6, 3000.0, 4
        sub = "pilot"
    else:
        N, T, NSUB, NSEED, NAB, TCONV, NCONV = 200, 30000.0, 30, 20, 30, 10000.0, 10
        sub = "main"
    if a.models:
        N = a.models
    out = a.outdir or os.path.join(HERE, "results", sub)
    if not a.pilot and os.path.basename(os.path.normpath(out)) != "main" and a.outdir is None:
        raise SystemExit("refusing: non-pilot run must write to results/main")
    if a.pilot and os.path.basename(os.path.normpath(out)) == "main":
        raise SystemExit("refusing: --pilot must never write to results/main")
    os.makedirs(out, exist_ok=True)
    fh = open(os.path.join(out, "run.log"), "a")
    stages = a.stages.split(",")
    dt = 0.025
    from multiprocessing import Pool
    pool = Pool(a.workers)
    t_start = time.time()
    log(f"start {sub} N={N} T={T} stages={stages} workers={a.workers}", fh)

    if "control" in stages:
        jobs = [(n, dict(p), dt) for n, (_, p) in CANON_BANDS.items()]
        jobs += [(n + "_dt0.0125", dict(p), 0.0125) for n, (_, p) in CANON_BANDS.items()]
        jobs += [("sk_removed_mutation", dict(CONFIG_SK, gsk=0.0), dt)]
        res = pool.map(task_follow, jobs)
        ctl = {r["name"]: r for r in res}
        for n, (target, _) in CANON_BANDS.items():
            r = ctl[n]
            r["target_hz"] = target
            r["band"] = [0.75 * target, 1.25 * target]
            r["pass"] = bool(r["band"][0] <= r["ff"] <= r["band"][1])
        m = ctl["sk_removed_mutation"]
        m["pass"] = bool(not (4.5 <= m["ff"] <= 7.5))
        m["note"] = "mutation check: removing SK/Ca-K must take the third configuration OUT of 4.5-7.5 Hz"
        save(os.path.join(out, "control.json"), ctl)
        log("control: " + json.dumps({k: round(v["ff"], 1) for k, v in ctl.items()}), fh)

    # accept
    accepted = []
    if any(s in stages for s in ("accept", "det", "stoch", "tests", "converge", "visual", "aggregate")):
        from collections import deque
        cand_dir = os.path.join(out, "cand")
        inflight = deque()
        nxt = 0
        n_done = 0
        # rolling window keeps every worker busy; results are consumed in candidate
        # order so the population is "the first N accepted by index" regardless of timing
        while len(accepted) < N:
            while len(inflight) < a.workers * 2:
                inflight.append(pool.apply_async(
                    task_accept, ((os.path.join(cand_dir, f"c{nxt:04d}.json"), nxt, dt),)))
                nxt += 1
            r = inflight.popleft().get()
            n_done += 1
            if r["accepted"]:
                accepted.append(r)
            if n_done % 10 == 0 or len(accepted) == N:
                log(f"accept: {len(accepted)}/{N} accepted after {n_done} candidates", fh)
        n_cand_used = max(r["i"] for r in accepted) + 1
        save(os.path.join(out, "accept_summary.json"), dict(
            n_accepted=len(accepted), n_candidates_considered=n_cand_used,
            range_hz=FOLLOW_RANGE, ff=[r["ff"] for r in accepted],
            n_in_range=sum(1 for j in range(n_cand_used) if load(os.path.join(cand_dir, f"c{j:04d}.json"))["in_range"]),
            n_in_range_undrivable=sum(1 for j in range(n_cand_used) if (lambda c: c["in_range"] and c["drive_thr"] is None)(load(os.path.join(cand_dir, f"c{j:04d}.json")))),
            ff_all_candidates=[load(os.path.join(cand_dir, f"c{j:04d}.json"))["ff"] for j in range(n_cand_used)]))

    mdir = os.path.join(out, "model")
    if "det" in stages:
        jobs = [(os.path.join(mdir, f"m{k:03d}.json"), k, r["params"], r["rest_thr"], r["drive_thr"], T, dt) for k, r in enumerate(accepted)]
        done = 0
        for r in pool.imap_unordered(task_det, jobs):
            done += 1
            log(f"det: {done}/{len(jobs)} (model {r['k']}) undrivable={r.get('undrivable', False)}", fh)
    det = {}
    for k in range(len(accepted)):
        pth = os.path.join(mdir, f"m{k:03d}.json")
        if os.path.exists(pth):
            det[k] = load(pth)
    sub_idx = [k for k in range(min(NSUB, len(accepted))) if k in det and not det[k].get("undrivable")]

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
            log(f"ab: {n + 1}/{len(jobs)}", fh)

    if "converge" in stages:
        jobs = []
        for k in sub_idx[:NCONV]:
            for d in (0.025, 0.0125):
                jobs.append((os.path.join(out, "converge", f"m{k:03d}_dt{d}.json"), k, det[k]["params"],
                             det[k]["drive_thr"], det[k]["lat"], d, TCONV))
        for n, r in enumerate(pool.imap_unordered(task_converge, jobs)):
            log(f"converge: {n + 1}/{len(jobs)}", fh)

    if "visual" in stages:
        ffs = np.array([det[k]["params"] and accepted[k]["ff"] for k in sorted(det)])
        ks = sorted(det)
        rep = ks[int(np.argmin(np.abs(ffs - np.median(ffs))))]
        ab_path = os.path.join(out, "ab", "a000.json")
        ab = load(ab_path)
        res = pool.apply(task_visual, ((os.path.join(out, "visual-traces.json"), det[rep]["params"],
                                        det[rep]["drive_thr"], ab["params"], ab["drive_thr"], 6000.0, dt),))
        log(f"visual: representative model k={rep} ff={accepted[rep]['ff']:.1f}", fh)

    pool.close()
    pool.join()
    log(f"done in {(time.time() - t_start) / 60:.1f} min", fh)
    if "aggregate" in stages:
        import aggregate_s001
        aggregate_s001.main(out, pilot=a.pilot)


if __name__ == "__main__":
    main()
