#!/usr/bin/env python3
"""The ONE unmodified-model response curve allowed before the S-2b pre-registration (PREDICTION.md,
"What was run before this file").  It measures one quantity: the WDR firing rate of the unmodified
shipped network (candidate 0, E_anion shift 0) against the per-fibre rate of Poisson C input, with C
input only (no touch, no stimulation), on the S-2b run protocol.  It is used only to place the C-drive
grid.  Nothing here bears on P0 to P3.

    simulations/.venv/bin/python -B prereg_response_curve.py [--workers 8]

Writes results/pilot/response-curve.json (gitignored); a copy is committed as results/prereg/.
"""

import argparse
import json
import os
import sys
import time
from concurrent.futures import ProcessPoolExecutor

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import s2b_protocol as P  # noqa: E402

GRID = tuple(round(0.5 + 0.125 * i, 3) for i in range(17))   # Hz per C fibre


def one(rc):
    import dh_model as dm
    model = dm.DorsalHorn(dt=P.DT_MAIN)
    model.set_shift(0)
    rates = []
    for seed in P.SEEDS:
        ft = P.build_fibre_trains("C1", 0, seed, rc)
        out = model.run(model.expand_fibres(ft), P.T_RUN, P.DT_MAIN)
        rates.append(P.rate_in_window(out["WDR"]))
    return rc, rates


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    out_dir = os.path.join(HERE, "results", "pilot")
    os.makedirs(out_dir, exist_ok=True)
    t0 = time.time()
    print(time.strftime("%Y-%m-%d %H:%M:%S ") + "start response curve", flush=True)
    with ProcessPoolExecutor(args.workers, max_tasks_per_child=1) as ex:
        res = list(ex.map(one, GRID))
    curve = [dict(rC_hz_per_fibre=rc, wdr_rate_hz_by_seed=r, wdr_rate_hz_mean=float(np.mean(r))) for rc, r in res]
    obj = dict(what="unmodified shipped network (candidate 0), E_anion shift 0, C input only, S-2b run protocol",
               seeds=list(P.SEEDS), t_run_ms=P.T_RUN, window_ms=[P.T_SCORE0, P.T_SCORE1], dt_ms=P.DT_MAIN,
               curve=curve, seconds=time.time() - t0)
    path = os.path.join(out_dir, "response-curve.json")
    with open(path, "w") as fh:
        json.dump(obj, fh, indent=1)
    print(time.strftime("%Y-%m-%d %H:%M:%S ") + "wrote " + os.path.relpath(path, HERE), flush=True)
    for c in curve:
        print(f"{c['rC_hz_per_fibre']:6.3f} Hz/fibre -> WDR {c['wdr_rate_hz_mean']:7.2f} Hz  {c['wdr_rate_hz_by_seed']}")


if __name__ == "__main__":
    main()
