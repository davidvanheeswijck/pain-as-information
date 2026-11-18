#!/usr/bin/env python3
"""Diagnostic (a pilot, never a result): how the unmodified network (candidate 0) responds to
the pre-registered input generators.  Writes results/pilot/diag_candidate0.json only.
It exists to explain a control outcome and to size a follow-up; nothing pre-registered is
changed by it.

  python diag_candidate0.py [--workers 10]
"""

import argparse
import json
import os
import sys
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import s2_protocol as P  # noqa: E402

RC_GRID = (0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 5.0, 10.0)
RT_GRID = (10.0, 20.0, 40.0, 80.0)
SHIFT_GRID = (0, 10, 20, 30, 40)


F_RC = (1.0, 1.5)


def one(task):
    import simulate_s002 as S
    kind, a, b = task
    m = S.new_model({}, {}, P.DT_MAIN)
    if kind == "C":
        return task, S.rate_run(m, 0, "C1", 0, 1, a, 0.0)
    if kind == "F":   # SCS at b Hz with C background at a Hz per fibre (no touch), seed 1
        return task, S.rate_run(m, 0, "CS", 0, 1, a, 0.0, freq=b)
    return task, S.rate_run(m, 0, "T", int(b), 1, 0.0, a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--parts", default="C,T,F", help="which of C, T, F to run; results are cached per task")
    args = ap.parse_args()
    parts = args.parts.split(",")
    tasks = ([("C", r, 0) for r in RC_GRID] if "C" in parts else []) + \
        ([("T", r, s) for r in RT_GRID for s in SHIFT_GRID] if "T" in parts else []) + \
        ([("F", r, f) for r in F_RC for f in P.CONTROL_FREQS] if "F" in parts else [])
    cache = os.path.join(HERE, "results", "pilot", "diag_candidate0_cache.json")
    done = {}
    if os.path.exists(cache):
        with open(cache) as fh:
            done = {tuple([v[0][0], v[0][1], v[0][2]]): v[1] for v in json.load(fh)}
    todo = [t for t in tasks if t not in done]
    # ProcessPoolExecutor raises BrokenProcessPool if a worker dies; multiprocessing.Pool would hang
    with ProcessPoolExecutor(args.workers, max_tasks_per_child=1) as ex:
        for t, r in ex.map(one, todo):
            done[t] = r
            os.makedirs(os.path.dirname(cache), exist_ok=True)
            with open(cache, "w") as fh:
                json.dump([[list(k), v] for k, v in done.items()], fh)
    res = done
    out = dict(C_only_rate_hz={str(r): res[("C", r, 0)] for r in RC_GRID if ("C", r, 0) in res},
               touch_only_rate_hz={f"{r}|{s}": res[("T", r, s)] for r in RT_GRID for s in SHIFT_GRID if ("T", r, s) in res},
               scs_with_C_background_rate_hz={f"{r}|{f}": res[("F", r, f)] for r in F_RC for f in P.CONTROL_FREQS if ("F", r, f) in res},
               note="candidate 0, seed 1, one 6 s scored window; a pilot, not a result")
    path = os.path.join(HERE, "results", "pilot", "diag_candidate0.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("C only (Hz per fibre -> WDR Hz):", out["C_only_rate_hz"])
    for r in F_RC:
        if ("F", r, P.CONTROL_FREQS[0]) not in res:
            continue
        base = res[("C", r, 0)]
        print(f"SCS frequency effect, C background {r} Hz per fibre (no-SCS rate {base:.2f}): " +
              str({f: round(res[("F", r, f)], 2) for f in P.CONTROL_FREQS}))
    for r in RT_GRID:
        if ("T", r, SHIFT_GRID[0]) in res:
            print(f"touch only at {r} Hz per fibre, WDR Hz by shift:", {s: round(res[('T', r, s)], 2) for s in SHIFT_GRID})


if __name__ == "__main__":
    main()
