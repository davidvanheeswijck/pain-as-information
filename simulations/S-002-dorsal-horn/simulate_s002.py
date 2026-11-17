#!/usr/bin/env python3
"""S-2 driver: dorsal-horn model of touch-evoked pain.

Pre-registration: PREDICTION.md (commit 007f633, alone, before any code or run).
The network is the Python re-implementation of ModelDB 168414 in dh_model.py; the
protocol, criteria and constants are in s2_protocol.py.

Stages (resumable: a per-model file that exists is never recomputed):
  control    candidate 0 at dt 0.025 and 0.0125 (gate G1), then candidates in index
             order in chunks until 200 are accepted (max 1500 considered)
  measure    9 conditions x 8 shifts x 3 seeds on every accepted network
  sweep      frequency sweeps and the P3 variants on the first 40 accepted networks
  converge   dt halving on the first 10 accepted networks
  visual     visual-traces.json
  aggregate  results.json / results.md / PNGs (aggregate_s002.py)

  python simulate_s002.py --pilot             # smoke test, writes results/pilot/ only
  python simulate_s002.py                     # full run, results/main/
  (resume: the same command; cached per-model files are reused)
"""

import argparse
import gc
import json
import os
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

if "--pilot" in sys.argv:
    os.environ["S2_PILOT"] = "1"   # read by s2_protocol at import (also in spawned workers)

import s2_protocol as P  # noqa: E402

_MODEL = None


def log(msg, fh=None):
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    if fh:
        fh.write(line + "\n")
        fh.flush()


def new_model(wf, cf, dt):
    """Build a fresh network, dropping the previous one first (two live networks in one
    process can crash NEURON)."""
    global _MODEL
    import dh_model as dm
    _MODEL = None
    gc.collect()
    _MODEL = dm.DorsalHorn(weight_factors=wf, cond_factors=cf, dt=dt)
    return _MODEL


def save(path, obj):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as fh:
        json.dump(obj, fh)
    os.replace(tmp, path)


def load(path):
    with open(path) as fh:
        return json.load(fh)


def factors_for(idx):
    import dh_model as dm
    return P.sample_factors(idx, list(dm.GROUP_ROWS), dm.WEIGHT_RANGE, dm.CONDUCTANCE_FACTORS)


# --- single runs ---------------------------------------------------------------------

def rate_run(model, net, cond, shift, seed, rC, rT, freq=P.SCS_PRIMARY_HZ, variant="norm", dt=P.DT_MAIN):
    model.set_shift(shift)
    ft = P.build_fibre_trains(cond, net, seed, rC, rT, freq, variant)
    out = model.run(model.expand_fibres(ft), P.T_RUN, dt)
    return P.rate_in_window(out["WDR"])


def mean_rate(model, net, cond, shift, rC, rT, freq=P.SCS_PRIMARY_HZ, variant="norm", dt=P.DT_MAIN, seeds=P.SEEDS):
    rs = [rate_run(model, net, cond, shift, s, rC, rT, freq, variant, dt) for s in seeds]
    return float(np.mean(rs)), [float(r) for r in rs]


# --- control (PREDICTION.md, "The positive control") --------------------------------------

def shipped_run(model, prefix, drop_afferent_below=None, n_cycles=None, dt=P.DT_MAIN):
    rows, tstop = P.read_shipped_inputs(prefix)
    ev = {k: v for k, v in rows.items() if k in set(int(r) for r in model.afferent_rows)}
    if drop_afferent_below is not None:
        ev = {k: v for k, v in ev.items() if int(model.table.frm[k]) >= drop_afferent_below}
    model.set_shift(0)
    out = model.run(ev, tstop, dt)
    return out["WDR"]


def control_record(idx, dt=P.DT_MAIN, stop_early=True):
    """The three-feature control for candidate idx.  Early exit in the order W, A, rC, F."""
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    rec = dict(idx=idx, dt=dt, weight_factors=wf, cond_factors=cf, stage="start", accepted=False)
    w = shipped_run(model, "windup", dt=dt)
    rec["W"] = P.judge_windup(P.windup_counts(w))
    rec["W"]["counts"] = P.windup_counts(w).tolist()
    if not rec["W"]["ok"] and stop_early:
        rec["stage"] = "W"
        rec["seconds"] = time.time() - t0
        return rec
    with_a = P.afib_counts(shipped_run(model, "afib", dt=dt))
    without_a = P.afib_counts(shipped_run(model, "afib", drop_afferent_below=30, dt=dt))
    rec["A"] = P.judge_afib(with_a, without_a)
    rec["A"]["with_counts"] = with_a.tolist()
    rec["A"]["without_counts"] = without_a.tolist()
    if not rec["A"]["ok"] and stop_early:
        rec["stage"] = "A"
        rec["seconds"] = time.time() - t0
        return rec
    rC, base, base_by_seed = None, None, None
    tried = {}
    for r in P.RC_SET:
        m, by = mean_rate(model, idx, "C1", 0, r, 0.0, dt=dt)
        tried[str(r)] = m
        if P.RC_BAND[0] <= m <= P.RC_BAND[1]:
            rC, base, base_by_seed = r, m, by
            break
    rec["rC_tried"] = tried
    rec["rC"] = rC
    if rC is None:
        rec["stage"] = "rC"
        rec["seconds"] = time.time() - t0
        return rec
    rates = {}
    for f in P.CONTROL_FREQS:
        rates[f], _ = mean_rate(model, idx, "CS", 0, rC, 0.0, freq=f, dt=dt)
    rec["F"] = P.judge_frequency(base, rates)
    rec["F"]["rates"] = {str(k): v for k, v in rates.items()}
    rec["F"]["rho"] = {str(k): v for k, v in rec["F"]["rho"].items()}
    rec["stage"] = "done"
    rec["accepted"] = bool(rec["W"]["ok"] and rec["A"]["ok"] and rec["F"]["ok"])
    rec["seconds"] = time.time() - t0
    return rec


def task_control(args):
    path, idx, dt = args
    if os.path.exists(path):
        return load(path)
    rec = control_record(idx, dt)
    save(path, rec)
    return rec


# --- measure ---------------------------------------------------------------------------------

def match_touch(model, idx, rC, dt):
    tried = {}
    for r in P.RT_SET:
        m, _ = mean_rate(model, idx, "T", 0, rC, r, dt=dt)
        tried[str(r)] = m
        if m >= P.RT_MIN_RATE:
            return r, tried, True
    return P.RT_SET[-1], tried, False


def task_measure(args):
    path, idx, rC, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    rT, tried, reached = match_touch(model, idx, rC, dt)
    R = {c: {} for c in P.CONDITIONS}
    for cond in P.CONDITIONS:
        for s in P.SHIFTS:
            R[cond][str(s)] = [rate_run(model, idx, cond, s, sd, rC, rT, dt=dt) for sd in P.SEEDS]
    rec = dict(idx=idx, rC=rC, rT=rT, rT_tried=tried, rT_reached=reached, R=R, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_sweep(args):
    path, idx, rC, rT, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    S = {}   # "TCS|norm|shift|freq" -> per-seed rates
    for s in P.SWEEP_SHIFTS:
        for f in P.SWEEP_FREQS:
            S[f"TCS|norm|{s}|{f}"] = [rate_run(model, idx, "TCS", s, sd, rC, rT, f, "norm", dt) for sd in P.SEEDS]
    for v in ("H", "D1", "D2"):
        for f in P.SWEEP_FREQS:
            S[f"TCS|{v}|{P.DELTA_REF}|{f}"] = [rate_run(model, idx, "TCS", P.DELTA_REF, sd, rC, rT, f, v, dt)
                                              for sd in P.SEEDS]
        for cond in ("TS", "CS"):
            S[f"{cond}|{v}|{P.DELTA_REF}|{P.SCS_PRIMARY_HZ}"] = [
                rate_run(model, idx, cond, P.DELTA_REF, sd, rC, rT, P.SCS_PRIMARY_HZ, v, dt) for sd in P.SEEDS]
    rec = dict(idx=idx, rC=rC, rT=rT, S=S, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_converge(args):
    path, idx, rC, rT = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    out = {}
    t0 = time.time()
    for dt in (P.DT_MAIN, P.DT_PUB):
        model = new_model(wf, cf, dt)
        for cond in ("C1", "T", "TS", "TCS"):
            for s in (0, 20):
                out[f"{cond}|{s}|{dt}"] = rate_run(model, idx, cond, s, 1, rC, rT, dt=dt)
    rec = dict(idx=idx, rC=rC, rT=rT, R=out, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_visual(args):
    path, idx, rC, rT, collapsed, dt, control_passed = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    out = dict(network_index=idx, label="model units; not a stimulation setting", dt_ms=dt,
               control_passed=control_passed,
               window_ms=[P.T_SCORE0, P.T_SCORE1], rC_hz_per_fibre=rC, rT_hz_per_fibre=rT,
               scs_hz=P.SCS_PRIMARY_HZ, C_input="off", panels=[])
    step = max(1, int(round(0.5 / dt)))   # 0.5 ms
    for shift in (0, collapsed):
        for cond in ("T", "TS"):
            model.set_shift(shift)
            ft = P.build_fibre_trains(cond, idx, 1, rC or 0.0, rT, P.SCS_PRIMARY_HZ, "norm")
            res = model.run(model.expand_fibres(ft), P.T_RUN, dt, traces=True)
            panel = dict(shift_mV=shift, E_anion_mV=-70 + shift, condition=cond,
                         t_ms=[round(float(x), 2) for x in res["t"][::step]],
                         wdr_v=[round(float(x), 2) for x in res["v"]["WDR"][::step]],
                         inhibitory_interneuron_v=[round(float(x), 2) for x in res["v"]["SG75"][::step]],
                         wdr_spikes_ms=[round(float(x), 2) for x in res["WDR"]],
                         inhibitory_interneuron_spikes_ms=[round(float(x), 2) for x in res["SG75"]],
                         abeta_touch_events_ms=[round(float(x), 2) for x in ft.get(0, [])],
                         n_abeta_fibres=len([f for f in ft if f in P.ABETA]))
            out["panels"].append(panel)
    save(path, out)
    return out


# --- driver ------------------------------------------------------------------------------------------

def run_stage_control(pool, out, fh, args):
    cdir = os.path.join(out, "cand")
    if args.pilot and args.force_rc:
        # PILOT ONLY: skip the control, accept the first n candidates with a forced C rate, to exercise
        # the later stages and the aggregator.  Never used for results/main.
        acc = list(range(args.n_ensemble))
        for i in acc:
            save(os.path.join(out, "cand0-dt0.025.json") if i == 0 else os.path.join(cdir, f"{i}.json"),
                 dict(idx=i, dt=P.DT_MAIN, stage="forced", accepted=True, rC=args.force_rc))
        save(os.path.join(out, "forced.json"), dict(force_rc=args.force_rc))
        save(os.path.join(out, "gate_g1.json"), dict(passed=True, forced=True))
        save(os.path.join(out, "accepted.json"), dict(accepted=acc, considered=len(acc), target=args.n_ensemble,
                                                      n_sub=args.n_sub, n_conv=args.n_conv, ok=True))
        return acc
    # gate G1: candidate 0 at both dt
    recs0 = []
    for dt in (P.DT_MAIN, P.DT_PUB):
        path = os.path.join(out, "cand0-dt{}.json".format(dt))
        r = task_control((path, 0, dt))
        recs0.append(r)
        log(f"candidate 0 at dt {dt}: stage {r['stage']} accepted {r['accepted']} "
            f"W {r.get('W', {}).get('ok')} A {r.get('A', {}).get('ok')} F {r.get('F', {}).get('ok')}", fh)
    g1 = all(r["accepted"] for r in recs0)
    save(os.path.join(out, "gate_g1.json"), dict(passed=g1, records=[os.path.basename(os.path.join(out, f"cand0-dt{d}.json")) for d in (P.DT_MAIN, P.DT_PUB)]))
    if not g1:
        log("G1 FAILED: candidate 0 does not pass the control; NO VERDICT, stopping", fh)
        return None
    accepted, n_done, chunk = [], 0, args.workers * 2
    max_cand = args.max_candidates
    # candidate 0 is accepted by construction of G1 (its record at dt main is cand0-dt0.025.json)
    accepted.append(0)
    idx = 1
    while len(accepted) < args.n_ensemble and idx < max_cand:
        batch = list(range(idx, min(idx + chunk, max_cand)))
        tasks = [(os.path.join(cdir, f"{i}.json"), i, P.DT_MAIN) for i in batch]
        recs = pool.map(task_control, tasks, chunksize=1)
        for r in recs:
            if r["accepted"] and len(accepted) < args.n_ensemble:
                accepted.append(r["idx"])
        idx = batch[-1] + 1
        log(f"control: considered {idx}, accepted {len(accepted)}", fh)
    save(os.path.join(out, "accepted.json"), dict(accepted=accepted, considered=idx, target=args.n_ensemble,
                                                  n_sub=args.n_sub, n_conv=args.n_conv,
                                                  ok=len(accepted) >= args.n_ensemble))
    return accepted


def accepted_rc(out, i):
    path = os.path.join(out, "cand0-dt0.025.json") if i == 0 else os.path.join(out, "cand", f"{i}.json")
    return load(path)["rC"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pilot", action="store_true", help="small run; writes results/pilot/ only")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--stages", default="control,measure,sweep,converge,visual,aggregate")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--n-ensemble", type=int, default=P.N_ENSEMBLE)
    ap.add_argument("--max-candidates", type=int, default=P.MAX_CANDIDATES)
    ap.add_argument("--n-sub", type=int, default=P.N_SUBSAMPLE)
    ap.add_argument("--n-conv", type=int, default=P.N_CONVERGE)
    ap.add_argument("--force-rc", type=float, default=None, help="PILOT ONLY: skip the control and use this C rate")
    args = ap.parse_args()
    if args.pilot:
        args.n_ensemble = min(args.n_ensemble, 4)
        args.max_candidates = min(args.max_candidates, 24)
        args.n_sub = min(args.n_sub, 2)
        args.n_conv = min(args.n_conv, 2)
    out = args.outdir or os.path.join(HERE, "results", "pilot" if args.pilot else "main")
    os.makedirs(out, exist_ok=True)
    fh = open(os.path.join(out, "run.log"), "a")
    stages = args.stages.split(",")
    log(f"start; workers {args.workers}; stages {stages}; out {os.path.relpath(out, HERE)}", fh)
    # G4: the wiring test must pass before anything else
    import subprocess
    py = sys.executable
    r = subprocess.run([py, "-B", "-m", "unittest", "test_sites"], cwd=HERE, capture_output=True, text=True)
    g4 = r.returncode == 0
    save(os.path.join(out, "gate_g4.json"), dict(passed=g4, tail=r.stderr.strip().splitlines()[-3:]))
    log(f"G4 wiring test passed: {g4}", fh)
    if not g4:
        log("G4 FAILED; stopping", fh)
        return 1
    with Pool(args.workers, maxtasksperchild=16) as pool:
        accepted = None
        if "control" in stages:
            accepted = run_stage_control(pool, out, fh, args)
            if accepted is None:
                stages = [s for s in stages if s in ("visual", "aggregate")]
        if accepted is None and os.path.exists(os.path.join(out, "accepted.json")):
            accepted = load(os.path.join(out, "accepted.json"))["accepted"]
        if accepted:
            if "measure" in stages:
                tasks = []
                for i in accepted:
                    tasks.append((os.path.join(out, "model", f"{i}.json"), i, accepted_rc(out, i), P.DT_MAIN))
                for k, _ in enumerate(pool.imap_unordered(task_measure, tasks, chunksize=1)):
                    if (k + 1) % 10 == 0:
                        log(f"measure: {k + 1}/{len(tasks)}", fh)
            models = {i: load(os.path.join(out, "model", f"{i}.json")) for i in accepted
                      if os.path.exists(os.path.join(out, "model", f"{i}.json"))}
            if "sweep" in stages:
                tasks = [(os.path.join(out, "sweep", f"{i}.json"), i, models[i]["rC"], models[i]["rT"], P.DT_MAIN)
                         for i in accepted[:args.n_sub] if i in models]
                for k, _ in enumerate(pool.imap_unordered(task_sweep, tasks, chunksize=1)):
                    log(f"sweep: {k + 1}/{len(tasks)}", fh)
            if "converge" in stages:
                tasks = [(os.path.join(out, "converge", f"{i}.json"), i, models[i]["rC"], models[i]["rT"])
                         for i in accepted[:args.n_conv] if i in models]
                for k, _ in enumerate(pool.imap_unordered(task_converge, tasks, chunksize=1)):
                    log(f"converge: {k + 1}/{len(tasks)}", fh)
            if "visual" in stages and accepted[0] in models:
                i = accepted[0]
                task_visual((os.path.join(out, "visual-traces.json"), i, models[i]["rC"], models[i]["rT"], 30, P.DT_MAIN, True))
                log("visual traces written", fh)
        elif "visual" in stages:
            # control not passed: candidate 0 only, labelled as such (touch conditions need no rC)
            vpath = os.path.join(out, "visual-traces.json")
            if not os.path.exists(vpath):
                m = new_model(*factors_for(0), P.DT_MAIN)
                rT, _, _ = match_touch(m, 0, 0.0, P.DT_MAIN)
                task_visual((vpath, 0, None, rT, 30, P.DT_MAIN, False))
                log("visual traces written for candidate 0 (control NOT passed)", fh)
    if "aggregate" in stages:
        import aggregate_s002
        aggregate_s002.main(out)
    log("done", fh)
    return 0


if __name__ == "__main__":
    sys.exit(main())
