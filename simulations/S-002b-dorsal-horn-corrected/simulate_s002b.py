#!/usr/bin/env python3
"""S-2b driver: corrected dorsal-horn run.

Pre-registration: PREDICTION.md (commit #1 of its branch, alone, before any code or run).  The network is
the S-2 port (../S-002-dorsal-horn/dh_model.py, reused by import); the protocol, criteria and constants are
in s2b_protocol.py.  Execution: ProcessPoolExecutor with max_tasks_per_child=1, so one network per process.

Stages (resumable: a per-network file that exists is never recomputed):
  gates      the oracle equivalence test, the wiring and protocol tests (G6, G4)
  control    candidate 0 at dt 0.025 and 0.0125 (gates G1, G5), then candidates in index order until 200
             are accepted on the calibration features (max 1500 considered)
  measure    main conditions x shifts x seeds, plus the A-delta-only and all-A runs, on every accepted network
  valid      the held-out frequency feature F on the first 60 accepted networks
  sweep      frequency sweeps and the P3 variants on the first 40 accepted networks
  converge   dt halving on the first 10 accepted networks
  visual     visual-traces.json (one accepted network)
  aggregate  results.json / results.md / PNGs / zip (aggregate_s002b.py)

  python simulate_s002b.py --pilot             # smoke test, writes results/pilot/ only
  python simulate_s002b.py                     # full run, results/main/
  (resume: the same command; cached per-network files are reused)
"""

import argparse
import gc
import hashlib
import json
import os
import subprocess
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

if "--pilot" in sys.argv:
    os.environ["S2B_PILOT"] = "1"   # read by s2b_protocol at import (also in spawned workers)

import s2b_protocol as P  # noqa: E402

_MODEL = None
_SHIPPED = {}


def rel(path):
    return os.path.relpath(path, HERE)


def log(msg, fh=None):
    line = time.strftime("%Y-%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    if fh:
        fh.write(line + "\n")
        fh.flush()


def new_model(wf, cf, dt):
    """Build a fresh network (one network per worker process; a second live one can crash NEURON)."""
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


# --- single runs ---------------------------------------------------------------------------

def rate_run(model, net, cond, shift, seed, rC, freq=P.SCS_PRIMARY_HZ, variant="norm", dt=P.DT_MAIN):
    model.set_shift(shift)
    ft = P.build_fibre_trains(cond, net, seed, rC, freq, variant)
    out = model.run(model.expand_fibres(ft), P.T_RUN, dt)
    return P.rate_in_window(out["WDR"])


def seed_rates(model, net, cond, shift, rC, freq=P.SCS_PRIMARY_HZ, variant="norm", dt=P.DT_MAIN, seeds=P.SEEDS):
    return [float(rate_run(model, net, cond, shift, s, rC, freq, variant, dt)) for s in seeds]


def shipped(prefix):
    if prefix not in _SHIPPED:
        _SHIPPED[prefix] = P.base.read_shipped_inputs(prefix)
    return _SHIPPED[prefix]


def windup_run(model, dt):
    rows, tstop = shipped("windup")
    aff = set(int(r) for r in model.afferent_rows)
    model.set_shift(0)
    return model.run({k: v for k, v in rows.items() if k in aff}, tstop, dt)["WDR"]


def afib_run(model, name, dt):
    keep_b, keep_d = P.A_CONDITIONS[name]
    rows, _ = shipped("afib")
    aff = set(int(r) for r in model.afferent_rows)
    ev = {}
    for k, v in rows.items():
        if k not in aff:
            continue
        fibre = int(model.table.frm[k])
        if fibre in P.ABETA and not keep_b:
            continue
        if fibre in P.ADELTA and not keep_d:
            continue
        ev[k] = v
    model.set_shift(0)
    return model.run(ev, P.A_TSTOP, dt)["WDR"]


def frequency_record(model, idx, rC, dt):
    """Held-out feature F at shift 0 (PREDICTION.md): TCS at each control frequency against TC."""
    base = float(np.mean(seed_rates(model, idx, "TC", 0, rC, dt=dt, seeds=P.F_SEEDS)))
    rates = {}
    for f in P.CONTROL_FREQS:
        rates[f] = float(np.mean(seed_rates(model, idx, "TCS", 0, rC, freq=f, dt=dt, seeds=P.F_SEEDS)))
    rec = P.judge_frequency(base, rates)
    rec["rates"] = {str(k): v for k, v in rates.items()}
    rec["rho"] = {str(k): v for k, v in rec.get("rho", {}).items()}
    return rec


# --- control: calibration (and, for candidate 0, the held-out feature) -------------------------

def control_record(idx, dt, extras):
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    rec = dict(idx=idx, dt=dt, weight_factors=wf, cond_factors=cf, stage="start", accepted=False)
    w = P.windup_counts(windup_run(model, dt))
    rec["W"] = P.judge_windup(w)
    rec["W"]["counts"] = w.tolist()
    if not rec["W"]["ok"] and not extras:
        rec["stage"] = "W"
        rec["seconds"] = time.time() - t0
        return rec
    names = ["C_only", "C_abeta"] + (["C_adelta", "C_all_A"] if extras else [])
    cnt = {n: P.afib_counts(afib_run(model, n, dt)) for n in names}
    rec["A"] = P.judge_afib_beta(cnt["C_only"], cnt["C_abeta"], cnt.get("C_adelta"), cnt.get("C_all_A"))
    rec["A"]["counts"] = {n: c.tolist() for n, c in cnt.items()}
    if not rec["A"]["ok"] and not extras:
        rec["stage"] = "A"
        rec["seconds"] = time.time() - t0
        return rec
    cache = {}

    def rate_at(i):
        if i not in cache:
            cache[i] = seed_rates(model, idx, "C1", 0, P.RC_GRID[i], dt=dt)
        return float(np.mean(cache[i]))

    rC, rate, tried, reason = P.match_rc(rate_at)
    rec["rC"], rec["rC_rate"], rec["rC_tried"], rec["rC_reason"] = rC, rate, {str(k): v for k, v in tried.items()}, reason
    if rC is None:
        rec["stage"] = "rC"
        rec["seconds"] = time.time() - t0
        return rec
    rec["stage"] = "done"
    rec["accepted"] = bool(rec["W"]["ok"] and rec["A"]["ok"])
    if extras:
        rec["F"] = frequency_record(model, idx, rC, dt)
    rec["seconds"] = time.time() - t0
    return rec


def task_control(args):
    path, idx, dt, extras = args
    if os.path.exists(path):
        return load(path)
    rec = control_record(idx, dt, extras)
    save(path, rec)
    return rec


# --- measure ----------------------------------------------------------------------------------------

def task_measure(args):
    path, idx, rC, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    R = {c: {} for c in P.MAIN_CONDITIONS}
    for cond in P.MAIN_CONDITIONS:
        for s in P.SHIFTS:
            R[cond][str(s)] = seed_rates(model, idx, cond, s, rC, dt=dt)
    A = {n: P.afib_counts(afib_run(model, n, dt)).tolist() for n in ("C_adelta", "C_all_A")}
    rec = dict(idx=idx, rC=rC, R=R, A=A, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_valid(args):
    path, idx, rC, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    rec = dict(idx=idx, rC=rC, F=frequency_record(model, idx, rC, dt), seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_sweep(args):
    path, idx, rC, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    t0 = time.time()
    S = {}   # "cond|variant|shift|freq" -> per-seed rates
    for s in P.SWEEP_SHIFTS:
        for f in P.SWEEP_FREQS:
            S[f"TCS|norm|{s}|{f}"] = seed_rates(model, idx, "TCS", s, rC, f, "norm", dt)
    for s in (P.DELTA_REF, P.DELTA_PROG):
        S[f"CS|norm|{s}|{P.SCS_PRIMARY_HZ}"] = seed_rates(model, idx, "CS", s, rC, P.SCS_PRIMARY_HZ, "norm", dt)
    for v in ("H", "D1", "D2"):
        for f in P.SWEEP_FREQS:
            S[f"TCS|{v}|{P.DELTA_REF}|{f}"] = seed_rates(model, idx, "TCS", P.DELTA_REF, rC, f, v, dt)
        for cond in ("TS", "CS"):
            S[f"{cond}|{v}|{P.DELTA_REF}|{P.SCS_PRIMARY_HZ}"] = seed_rates(
                model, idx, cond, P.DELTA_REF, rC, P.SCS_PRIMARY_HZ, v, dt)
    rec = dict(idx=idx, rC=rC, S=S, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_converge(args):
    path, idx, rC = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    out = {}
    t0 = time.time()
    model = new_model(wf, cf, P.DT_MAIN)   # one model for both dt (dt is a run argument)
    for dt in (P.DT_MAIN, P.DT_PUB):
        for cond in ("C1", "T", "TS"):
            for s in (0, 20):
                out[f"{cond}|{s}|{dt}"] = rate_run(model, idx, cond, s, 1, rC, dt=dt)
    rec = dict(idx=idx, rC=rC, R=out, seconds=time.time() - t0)
    save(path, rec)
    return rec


def task_visual(args):
    path, idx, rC, collapsed, dt = args
    if os.path.exists(path):
        return load(path)
    wf, cf = factors_for(idx)
    model = new_model(wf, cf, dt)
    out = dict(network_index=idx, label="model units; not a stimulation setting", dt_ms=dt,
               window_ms=[P.T_SCORE0, P.T_SCORE1], rC_hz_per_fibre=rC, touch_hz_per_abeta_fibre=P.TOUCH_HZ,
               scs_hz=P.SCS_PRIMARY_HZ, scs_target_fibres="30-44 (surround input to SG76)", C_input="off", panels=[])
    step = max(1, int(round(0.5 / dt)))   # 0.5 ms
    for shift in (0, collapsed):
        for cond in ("T", "TS"):
            model.set_shift(shift)
            ft = P.build_fibre_trains(cond, idx, 1, rC, P.SCS_PRIMARY_HZ, "norm")
            res = model.run(model.expand_fibres(ft), P.T_RUN, dt, traces=True)
            out["panels"].append(dict(
                shift_mV=shift, E_anion_mV=-70 + shift, condition=cond,
                t_ms=[round(float(x), 2) for x in res["t"][::step]],
                wdr_v=[round(float(x), 2) for x in res["v"]["WDR"][::step]],
                inhibitory_interneuron_v=[round(float(x), 2) for x in res["v"]["SG75"][::step]],
                wdr_spikes_ms=[round(float(x), 2) for x in res["WDR"]],
                inhibitory_interneuron_spikes_ms=[round(float(x), 2) for x in res["SG75"]],
                n_touch_events_total=int(sum(len(ft[f]) for f in P.ABETA if f in ft)),
                n_scs_pulses=int(len(ft.get(30, [])) if cond == "TS" else 0)))
    save(path, out)
    return out


# --- driver ----------------------------------------------------------------------------------------------

def run_tasks(ex, fn, tasks, fh, label):
    futs = [ex.submit(fn, t) for t in tasks]
    done = 0
    results = []
    for fu in as_completed(futs):
        results.append(fu.result())
        done += 1
        if done % 10 == 0 or done == len(futs):
            log(f"{label}: {done}/{len(futs)}", fh)
    return results


def gate_g1(recs0):
    return bool(all(r["accepted"] for r in recs0))


def gate_g5(recs0):
    return bool(all("F" in r and r["F"].get("ok") for r in recs0))


def run_stage_control(ex, out, fh, args):
    cdir = os.path.join(out, "cand")
    if args.pilot and args.force_rc:
        # PILOT ONLY: skip the control, accept the first n candidates with a forced C rate.
        acc = list(range(args.n_ensemble))
        for i in acc:
            save(os.path.join(out, f"cand0-dt{P.DT_MAIN}.json") if i == 0 else os.path.join(cdir, f"{i}.json"),
                 dict(idx=i, dt=P.DT_MAIN, stage="forced", accepted=True, rC=args.force_rc))
        save(os.path.join(out, "forced.json"), dict(force_rc=args.force_rc))
        save(os.path.join(out, "gate_g1.json"), dict(passed=True, forced=True))
        save(os.path.join(out, "accepted.json"), dict(accepted=acc, considered=len(acc), target=args.n_ensemble, ok=True))
        return acc
    tasks = [(os.path.join(out, f"cand0-dt{dt}.json"), 0, dt, True) for dt in (P.DT_MAIN, P.DT_PUB)]
    recs0 = run_tasks(ex, task_control, tasks, fh, "candidate 0")
    recs0 = sorted(recs0, key=lambda r: -r["dt"])
    for r in recs0:
        log(f"candidate 0 at dt {r['dt']}: stage {r['stage']} accepted {r['accepted']} W {r['W']['ok']} "
            f"A-beta {r.get('A', {}).get('ok')} rC {r.get('rC')} F {r.get('F', {}).get('ok')}", fh)
    g1, g5 = gate_g1(recs0), gate_g5(recs0)
    save(os.path.join(out, "gate_g1.json"), dict(passed=g1, files=[f"cand0-dt{d}.json" for d in (P.DT_MAIN, P.DT_PUB)]))
    save(os.path.join(out, "gate_g5.json"), dict(passed=g5, files=[f"cand0-dt{d}.json" for d in (P.DT_MAIN, P.DT_PUB)]))
    log(f"G1 (calibration at candidate 0) passed: {g1}; G5 (held-out F at candidate 0) passed: {g5}", fh)
    if not g1:
        log("G1 FAILED: candidate 0 does not pass the calibration; NO VERDICT, stopping", fh)
        return None
    accepted, idx, chunk = [0], 1, args.workers * 2
    while len(accepted) < args.n_ensemble and idx < args.max_candidates:
        batch = list(range(idx, min(idx + chunk, args.max_candidates)))
        tasks = [(os.path.join(cdir, f"{i}.json"), i, P.DT_MAIN, False) for i in batch]
        recs = run_tasks(ex, task_control, tasks, fh, f"control {batch[0]}-{batch[-1]}")
        for r in sorted(recs, key=lambda r: r["idx"]):
            if r["accepted"] and len(accepted) < args.n_ensemble:
                accepted.append(r["idx"])
        idx = batch[-1] + 1
        log(f"control: considered {idx}, accepted {len(accepted)}", fh)
    stages = {"W": 0, "A": 0, "rC": 0, "accepted": 0}
    for i in range(1, idx):
        p = os.path.join(cdir, f"{i}.json")
        if os.path.exists(p):
            stages[load(p)["stage"] if not load(p)["accepted"] else "accepted"] += 1
    save(os.path.join(out, "accepted.json"), dict(accepted=accepted, considered=idx, target=args.n_ensemble,
                                                  rejected_at_stage=stages, ok=len(accepted) >= args.n_ensemble))
    return accepted


def accepted_rc(out, i):
    path = os.path.join(out, f"cand0-dt{P.DT_MAIN}.json") if i == 0 else os.path.join(out, "cand", f"{i}.json")
    return load(path)["rC"]


def file_sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git_state():
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], cwd=HERE, capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "status", "--porcelain", "--", "."], cwd=HERE, capture_output=True, text=True).stdout.strip()
        return head, bool(dirty)
    except Exception:
        return None, None


def run_gate_tests(out, fh):
    """G4 (wiring + protocol) and G6 (oracle equivalence), run as subprocesses with python -B."""
    res = {}
    env = {k: v for k, v in os.environ.items() if k != "S2B_PILOT"}   # the tests check the registered constants
    for gate, mods in (("g4", ["test_s2b_sites", "test_s2b_protocol"]), ("g6", ["test_s2b_oracle"])):
        r = subprocess.run([sys.executable, "-B", "-m", "unittest", *mods], cwd=HERE, capture_output=True, text=True, env=env)
        res[gate] = dict(passed=r.returncode == 0, modules=mods, tail=r.stderr.strip().splitlines()[-3:],
                         file_sha256={m + ".py": file_sha(os.path.join(HERE, m + ".py")) for m in mods})
        save(os.path.join(out, f"gate_{gate}.json"), res[gate])
        log(f"{gate.upper()} tests {mods} passed: {res[gate]['passed']}", fh)
    return res["g4"]["passed"] and res["g6"]["passed"]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--pilot", action="store_true", help="small run; writes results/pilot/ only")
    ap.add_argument("--workers", type=int, default=12)
    ap.add_argument("--stages", default="control,measure,valid,sweep,converge,visual,aggregate")
    ap.add_argument("--outdir", default=None)
    ap.add_argument("--n-ensemble", type=int, default=P.N_ENSEMBLE)
    ap.add_argument("--max-candidates", type=int, default=P.MAX_CANDIDATES)
    ap.add_argument("--n-sub", type=int, default=P.N_SUBSAMPLE)
    ap.add_argument("--n-valid", type=int, default=P.N_VALID)
    ap.add_argument("--n-conv", type=int, default=P.N_CONVERGE)
    ap.add_argument("--force-rc", type=float, default=None, help="PILOT ONLY: skip the control and use this C rate")
    args = ap.parse_args()
    if args.workers > 12:
        ap.error("12 workers or fewer")
    if args.pilot:
        args.n_ensemble = min(args.n_ensemble, 4)
        args.max_candidates = min(args.max_candidates, 24)
        args.n_sub = min(args.n_sub, 2)
        args.n_valid = min(args.n_valid, 2)
        args.n_conv = min(args.n_conv, 2)
    out = args.outdir or os.path.join(HERE, "results", "pilot" if args.pilot else "main")
    if args.outdir and not args.pilot:
        out = os.path.abspath(out)
    os.makedirs(out, exist_ok=True)
    fh = open(os.path.join(out, "run.log"), "a")
    stages = args.stages.split(",")
    head, dirty = git_state()
    log(f"start; workers {args.workers}; stages {stages}; out {rel(out)}; git HEAD {head}; "
        f"uncommitted changes in this directory: {dirty}", fh)
    if not run_gate_tests(out, fh):
        log("G4 or G6 FAILED; stopping", fh)
        return 1
    with ProcessPoolExecutor(args.workers, max_tasks_per_child=1) as ex:
        accepted = None
        if "control" in stages:
            accepted = run_stage_control(ex, out, fh, args)
        if accepted is None and os.path.exists(os.path.join(out, "accepted.json")):
            accepted = load(os.path.join(out, "accepted.json"))["accepted"]
        if accepted:
            def p(sub, i):
                return os.path.join(out, sub, f"{i}.json")
            if "measure" in stages:
                run_tasks(ex, task_measure, [(p("model", i), i, accepted_rc(out, i), P.DT_MAIN) for i in accepted], fh, "measure")
            if "valid" in stages:
                run_tasks(ex, task_valid, [(p("valid", i), i, accepted_rc(out, i), P.DT_MAIN) for i in accepted[:args.n_valid]], fh, "valid")
            if "sweep" in stages:
                run_tasks(ex, task_sweep, [(p("sweep", i), i, accepted_rc(out, i), P.DT_MAIN) for i in accepted[:args.n_sub]], fh, "sweep")
            if "converge" in stages:
                run_tasks(ex, task_converge, [(p("converge", i), i, accepted_rc(out, i)) for i in accepted[:args.n_conv]], fh, "converge")
            if "visual" in stages:
                i = accepted[0]
                run_tasks(ex, task_visual, [(os.path.join(out, "visual-traces.json"), i, accepted_rc(out, i), 15, P.DT_MAIN)], fh, "visual")
        elif "visual" in stages:
            log("no accepted ensemble: no visual traces (the control record is the result)", fh)
    if "aggregate" in stages:
        import aggregate_s002b
        aggregate_s002b.main(out)
    log("done", fh)
    return 0


if __name__ == "__main__":
    sys.exit(main())
