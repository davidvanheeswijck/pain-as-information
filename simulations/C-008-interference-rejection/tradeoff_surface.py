#!/usr/bin/env python3
"""The C-008 trade-off surface: sensor sensitivity against channel matching.

The main C-008 run sampled two corners and found that neither axis alone
reaches detectability, while both together reach 4.7x. That leaves the useful
question unanswered: what is the CHEAPEST combination that works?

This sweeps both axes jointly and reports the frontier. Muscle is held at its
literature-consistent 200 fT (PMID 40542043) rather than zeroed, because a
quiescent limb is an assumption a real experiment has to earn.
"""
import sys, json, numpy as np
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "C-004-velocity-beamforming"))
import simulate as s4
from simulate_c008 import (first_order_gradiometer, default_interferers,
                           muscle_interference_trace, gain_mismatch)

BANDS = {"C": (s4.C_FIBRE.v_min, s4.C_FIBRE.v_max),
         "Ab": (s4.AB_FIBRE.v_min, s4.AB_FIBRE.v_max)}
ITF = default_interferers(2.0)


def run(asd, gsig, seed, n_null, muscle_fT):
    cfg = s4.SimConfig(n_trials=2000, noise_asd_fT_rtHz=asd)
    amps = {"cardiac": 5e-12, "mains": 2e-12, "drift": 3e-12,
            "muscle": muscle_fT * 1e-15}
    v = s4.default_v_grid(); sx = cfg.sensor_positions()
    t = s4.make_time_axis(cfg, min(s4.C_FIBRE.v_min, s4.AB_FIBRE.v_min))
    dt = 1.0 / cfg.fs_hz
    gains = gain_mismatch(np.random.default_rng(seed + 500_000), sx.size, gsig)
    r0 = np.random.default_rng(seed)
    ab_i, c_i = s4.calibrate_i_ref(r0, cfg)
    r0 = np.random.default_rng(seed)
    pc = s4.build_population(r0, cfg.n_c, s4.C_FIBRE, c_i)
    pa = s4.build_population(r0, cfg.n_ab, s4.AB_FIBRE, ab_i)

    def build(sig, r):
        tr = np.zeros((sx.size, t.size))
        if sig:
            tr += s4.population_signal(pc, cfg.n_trials, sx, cfg.r_standoff_m,
                                       dt, t.size, cfg.n_velocity_bins_c, r)
            tr += s4.population_signal(pa, cfg.n_trials, sx, cfg.r_standoff_m,
                                       dt, t.size, cfg.n_velocity_bins_ab, r)
        w = {"cardiac": s4.cardiac_interference_trace(r, t, dt, cfg.n_trials, amps["cardiac"]),
             "mains": s4.mains_interference_trace(r, t, cfg.n_trials, amps["mains"]),
             "drift": s4.drift_interference_trace(r, t, dt, amps["drift"]),
             "muscle": muscle_interference_trace(r, t, dt, cfg.n_trials, amps["muscle"])}
        for k, x in w.items():
            tr += (ITF[k].sensor_weights(sx) * gains)[:, None] * x[None, :]
        tr = s4.apply_low_pass_filter(tr, dt, 350.0, 4)
        tr = tr + s4.averaged_noise(r, sx.size, t.size, asd, cfg.fs_hz, cfg.n_trials)
        return first_order_gradiometer(tr, sx)

    tr, xs = build(True, np.random.default_rng(seed))
    e = s4.beamform_sweep(tr, xs, t, v)
    peak = {b: s4.ridge_stats(v, e, bd)["peak_energy"] for b, bd in BANDS.items()}
    nr = np.random.default_rng(seed + 10_000)
    nulls = {b: [] for b in BANDS}
    for _ in range(n_null):
        ntr, nxs = build(False, nr)
        ne = s4.beamform_sweep(ntr, nxs, t, v)
        for b, bd in BANDS.items():
            nulls[b].append(s4.ridge_stats(v, ne, bd)["peak_energy"])
    return {b: peak[b] / float(np.percentile(nulls[b], 95)) for b in BANDS}


if __name__ == "__main__":
    seeds, n_null, muscle = 6, 15, 200.0
    asds = [1.0, 0.5, 0.2, 0.1]
    gsigs = [3e-3, 1e-3, 3e-4, 1e-4]
    print(f"C-band detectability. gradiometer, muscle={muscle:.0f} fT, "
          f"{seeds} seeds x {n_null} nulls.")
    print("Rows = sensor ASD fT/rtHz. Cols = channel matching 1:N.\n")
    hdr = "  ASD \\ 1:N |" + "".join(f"{int(1/g):>10d}" for g in gsigs)
    print(hdr); print("-" * len(hdr))
    surface = {}
    for asd in asds:
        cells = []
        for g in gsigs:
            vals = np.array([run(asd, g, s, n_null, muscle)["C"] for s in range(seeds)])
            m = float(vals.mean())
            surface[f"{asd}|{g}"] = {
                "mean": m,
                "ci95": [float(m - 1.96*vals.std(ddof=1)/np.sqrt(seeds)),
                         float(m + 1.96*vals.std(ddof=1)/np.sqrt(seeds))],
                "above_1": int((vals > 1.0).sum()), "n": seeds}
            cells.append(m)
        row = f"{asd:>11.2f} |" + "".join(
            f"{c:>9.2f}{'*' if c > 1.0 else ' '}" for c in cells)
        print(row, flush=True)
    print("\n* = mean above the detectability threshold of 1.0")
    Path("results").mkdir(exist_ok=True)
    Path("results/tradeoff-surface.json").write_text(json.dumps(
        {"muscle_fT": muscle, "seeds": seeds, "n_null": n_null,
         "surface": surface}, indent=2))
    print("wrote results/tradeoff-surface.json")
