#!/usr/bin/env python3
"""What sensor sensitivity does C-fibre detection need, WITH gradiometric
rejection applied?

C-008 claimed sensitivity below ~1 fT/rtHz "buys nothing" because interference,
not sensor noise, is the obstacle. The main C-008 run shows the reverse:
gradiometry removes interference almost entirely and the C band is still
undetectable. This sweep turns that refutation into a specification.
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
AMPS = {"cardiac": 5e-12, "mains": 2e-12, "drift": 3e-12, "muscle": 2e-13}


def run(asd, seed, n_null, use_grad):
    cfg = s4.SimConfig(n_trials=2000, noise_asd_fT_rtHz=asd)
    v_grid = s4.default_v_grid(); sx = cfg.sensor_positions()
    t_axis = s4.make_time_axis(cfg, min(s4.C_FIBRE.v_min, s4.AB_FIBRE.v_min))
    dt = 1.0 / cfg.fs_hz
    gains = gain_mismatch(np.random.default_rng(seed + 500_000), sx.size, 0.003)
    r0 = np.random.default_rng(seed)
    ab_i, c_i = s4.calibrate_i_ref(r0, cfg)
    r0 = np.random.default_rng(seed)
    pc = s4.build_population(r0, cfg.n_c, s4.C_FIBRE, c_i)
    pa = s4.build_population(r0, cfg.n_ab, s4.AB_FIBRE, ab_i)

    def build(sig, r):
        tr = np.zeros((sx.size, t_axis.size))
        if sig:
            tr += s4.population_signal(pc, cfg.n_trials, sx, cfg.r_standoff_m, dt,
                                       t_axis.size, cfg.n_velocity_bins_c, r)
            tr += s4.population_signal(pa, cfg.n_trials, sx, cfg.r_standoff_m, dt,
                                       t_axis.size, cfg.n_velocity_bins_ab, r)
        w = {"cardiac": s4.cardiac_interference_trace(r, t_axis, dt, cfg.n_trials, AMPS["cardiac"]),
             "mains": s4.mains_interference_trace(r, t_axis, cfg.n_trials, AMPS["mains"]),
             "drift": s4.drift_interference_trace(r, t_axis, dt, AMPS["drift"]),
             "muscle": muscle_interference_trace(r, t_axis, dt, cfg.n_trials, AMPS["muscle"])}
        for k, v in w.items():
            tr += (ITF[k].sensor_weights(sx) * gains)[:, None] * v[None, :]
        tr = s4.apply_low_pass_filter(tr, dt, 350.0, 4)
        tr = tr + s4.averaged_noise(r, sx.size, t_axis.size, asd, cfg.fs_hz, cfg.n_trials)
        if use_grad:
            return first_order_gradiometer(tr, sx)
        return tr, sx

    tr, xs = build(True, np.random.default_rng(seed))
    e = s4.beamform_sweep(tr, xs, t_axis, v_grid)
    peak = {b: s4.ridge_stats(v_grid, e, bd)["peak_energy"] for b, bd in BANDS.items()}
    nr = np.random.default_rng(seed + 10_000)
    nulls = {b: [] for b in BANDS}
    for _ in range(n_null):
        ntr, nxs = build(False, nr)
        ne = s4.beamform_sweep(ntr, nxs, t_axis, v_grid)
        for b, bd in BANDS.items():
            nulls[b].append(s4.ridge_stats(v_grid, ne, bd)["peak_energy"])
    return {b: peak[b] / float(np.percentile(nulls[b], 95)) for b in BANDS}


if __name__ == "__main__":
    seeds, n_null = 8, 20
    print("C-band detectability with first-order gradiometry, by sensor ASD.")
    print("A ratio above 1.0 means detectable above the matched null.\n")
    print(f"{'ASD fT/rtHz':>12} | {'no rejection':>13} | {'gradiometer':>12}")
    out = {}
    for asd in (1.0, 0.5, 0.3, 0.2, 0.1, 0.05):
        g = np.array([run(asd, s, n_null, True)["C"] for s in range(seeds)])
        n = np.array([run(asd, s, n_null, False)["C"] for s in range(seeds)])
        out[asd] = {"grad_mean": float(g.mean()), "none_mean": float(n.mean()),
                    "grad_ci": [float(g.mean()-1.96*g.std(ddof=1)/np.sqrt(seeds)),
                                float(g.mean()+1.96*g.std(ddof=1)/np.sqrt(seeds))]}
        print(f"{asd:>12.2f} | {n.mean():>13.3f} | {g.mean():>12.3f}")
    Path("results").mkdir(exist_ok=True)
    Path("results/sensitivity-spec.json").write_text(json.dumps(out, indent=2))
    print("\nwrote results/sensitivity-spec.json")
