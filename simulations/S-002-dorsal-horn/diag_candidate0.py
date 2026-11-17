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
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import s2_protocol as P  # noqa: E402

RC_GRID = (0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 5.0, 10.0)
RT_GRID = (10.0, 20.0, 40.0, 80.0)
SHIFT_GRID = (0, 10, 20, 30, 40)


def one(task):
    import simulate_s002 as S
    kind, a, b = task
    m = S.new_model({}, {}, P.DT_MAIN)
    if kind == "C":
        return task, S.rate_run(m, 0, "C1", 0, 1, a, 0.0)
    return task, S.rate_run(m, 0, "T", int(b), 1, 0.0, a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=10)
    args = ap.parse_args()
    tasks = [("C", r, 0) for r in RC_GRID] + [("T", r, s) for r in RT_GRID for s in SHIFT_GRID]
    with Pool(args.workers, maxtasksperchild=1) as pool:
        res = dict(pool.map(one, tasks))
    out = dict(C_only_rate_hz={str(r): res[("C", r, 0)] for r in RC_GRID},
               touch_only_rate_hz={f"{r}|{s}": res[("T", r, s)] for r in RT_GRID for s in SHIFT_GRID},
               note="candidate 0, seed 1, one 6 s scored window; a pilot, not a result")
    path = os.path.join(HERE, "results", "pilot", "diag_candidate0.json")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as fh:
        json.dump(out, fh, indent=1)
    print("C only (Hz per fibre -> WDR Hz):", out["C_only_rate_hz"])
    for r in RT_GRID:
        print(f"touch only at {r} Hz per fibre, WDR Hz by shift:", {s: round(res[('T', r, s)], 2) for s in SHIFT_GRID})


if __name__ == "__main__":
    main()
