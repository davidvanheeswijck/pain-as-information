#!/usr/bin/env python3
"""C-008: does gradiometric interference rejection, rather than sensor
sensitivity, unblock magnetic detection of C-fibre traffic?

This extends the C-004 simulation rather than replacing it. The forward model,
beamformer, fibre populations and null-distribution machinery are imported
unchanged from ``simulations/C-004-velocity-beamforming/simulate.py`` so that
any difference in the result is attributable to the rejection stage alone.

WHAT THIS ADDS, AND WHY EACH ADDITION MATTERS
---------------------------------------------

1. **Interference now has spatial structure.** C-004 added interference as
   ``extra_field_T[None, :]``, i.e. numerically identical at every sensor. A
   first-order gradiometer cancels a perfectly uniform field *exactly*, so
   running C-008 against C-004's interference model would have confirmed the
   conjecture by construction and proved nothing. Every interferer here is
   placed at a stated distance and its amplitude falls off across the array
   according to a stated power law.

2. **A local muscular source.** C-008's own second rival says this is the most
   likely way it fails, and notes the simulation "does not currently model
   muscle at all". An EMG source in the limb, tens of millimetres from the
   array, is *not* common-mode and should survive gradiometry. Omitting it
   would be the second way to rig the test.

3. **The falloff exponent is swept, not assumed.** A current dipole in a volume
   conductor gives B ~ 1/r^2; a magnetic dipole gives 1/r^3. Which one applies
   sets the residual gradient across the array, and therefore sets the answer.
   Both are reported.

4. **Three rejection schemes**, each with its own effective sensor geometry:
   first-order gradiometer (adjacent differences, midpoint positions),
   second-order gradiometer, and reference-array regression using sensors
   placed where the nerve contribution is negligible.

5. **The A-beta positive control runs through the identical rejection.** If a
   scheme suppresses the known large fast ridge as well, the configuration is
   wrong rather than the conjecture refuted. This is the mandatory control.

6. **The null distribution is recomputed through each rejection pipeline.**
   Comparing a rejected signal against an unrejected null would manufacture
   detectability, which is the dominant false-pass route C-008 names.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict
from pathlib import Path

import numpy as np

_C004 = Path(__file__).resolve().parents[1] / "C-004-velocity-beamforming"
sys.path.insert(0, str(_C004))

import simulate as s4  # noqa: E402


# ---------------------------------------------------------------------------
# spatial models for the interferers
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Interferer:
    """A source at a stated distance with a stated falloff.

    ``distance_m`` is measured from the centre of the sensor array. ``offset``
    is the along-array component of the source direction: 0.0 means the source
    lies broadside (perpendicular to the array axis), 1.0 means it lies along
    the array axis. Broadside sources produce the smallest gradient across the
    array and are therefore the easiest to reject; axial sources the hardest.
    """

    name: str
    distance_m: float
    falloff_exponent: float
    offset_along_array: float = 0.0

    def sensor_weights(self, sensors_x: np.ndarray) -> np.ndarray:
        """Relative field amplitude at each sensor, normalised to the array
        centre. A perfectly uniform interferer would return all ones."""
        centre = float(np.mean(sensors_x))
        dx = sensors_x - centre
        along = self.offset_along_array * self.distance_m
        broad = np.sqrt(max(self.distance_m**2 - along**2, 0.0))
        r = np.sqrt((along + dx) ** 2 + broad**2)
        return (self.distance_m / r) ** self.falloff_exponent


def gain_mismatch(rng: np.random.Generator, n: int, sigma: float) -> np.ndarray:
    """Per-sensor multiplicative gain and orientation error.

    THIS IS THE MOST IMPORTANT LINE IN THE FILE. Geometry is not what limits
    a real gradiometer. Common-mode rejection is limited by how well two
    channels are matched in gain and axis alignment, and for real arrays that
    is about 1 part in 100 to 1 part in 1000. A simulation that omits it lets
    a first-order gradiometer cancel a distant source to machine precision,
    which no instrument has ever done, and would confirm C-008 by construction.

    The first draft of this file omitted it and produced an A-beta
    detectability ratio of ~8000, which is what a collapsed null looks like.
    """
    return 1.0 + rng.normal(0.0, sigma, size=n)


# Distances chosen for an array on the lower leg over a superficial nerve.
def default_interferers(exponent: float) -> dict[str, Interferer]:
    return {
        # Heart to lower leg. Broadside-ish, far: the classic common-mode case.
        "cardiac": Interferer("cardiac", 0.85, exponent, offset_along_array=0.3),
        # Building wiring: much further, effectively uniform.
        "mains": Interferer("mains", 3.0, exponent, offset_along_array=0.2),
        # Ambient/environmental drift: far field, treated as uniform.
        "drift": Interferer("drift", 10.0, exponent, offset_along_array=0.0),
        # Gastrocnemius under the array. LOCAL. This is the one that hurts.
        "muscle": Interferer("muscle", 0.030, exponent, offset_along_array=0.6),
    }


def muscle_interference_trace(
    rng: np.random.Generator,
    t_axis: np.ndarray,
    dt: float,
    n_trials: int,
    amplitude_T: float,
    burst_rate_hz: float = 8.0,
    burst_width_s: float = 0.015,
) -> np.ndarray:
    """Trial-averaged surface-EMG-like interference: recurrent low-frequency
    motor-unit bursts with trial-independent phase.

    Modelled the same way as the cardiac term -- a Ricker transient at
    Poisson-ish intervals with uniform phase per trial -- because the point
    here is its SPATIAL locality, not its waveform fidelity. Amplitude is
    the free parameter and is swept.
    """
    period_s = 1.0 / burst_rate_hz
    sigma = burst_width_s / 4.0
    margin_s = 4.0 * sigma
    t_min, t_max = float(t_axis[0]), float(t_axis[-1])

    phases = rng.uniform(0.0, period_s, size=n_trials)
    k_min = int(np.floor((t_min - margin_s) / period_s)) - 1
    k_max = int(np.ceil((t_max + margin_s) / period_s)) + 1
    k_vals = np.arange(k_min, k_max + 1)
    times = (phases[:, None] + k_vals[None, :] * period_s).ravel()
    keep = (times >= t_min - margin_s) & (times <= t_max + margin_s)
    times = times[keep]

    n_samples = t_axis.size
    idx = np.round((times - t_min) / dt).astype(np.int64)
    valid = (idx >= 0) & (idx < n_samples)
    hist = np.zeros(n_samples)
    np.add.at(hist, idx[valid], 1.0 / n_trials)

    half = 4.0 * sigma
    n_t = max(3, int(np.ceil(2 * half / dt)))
    templ_t = np.linspace(-half, half, n_t)
    template = amplitude_T * s4.ricker(templ_t / sigma)

    wave = np.convolve(hist, template, mode="full")
    start = int(np.round(templ_t[0] / dt))
    out = np.zeros(n_samples)
    s4._add_clipped(out, wave, start)
    return out


# ---------------------------------------------------------------------------
# rejection schemes
# ---------------------------------------------------------------------------

def first_order_gradiometer(trace: np.ndarray, sensors_x: np.ndarray):
    return np.diff(trace, axis=0), 0.5 * (sensors_x[:-1] + sensors_x[1:])


def second_order_gradiometer(trace: np.ndarray, sensors_x: np.ndarray):
    return np.diff(trace, n=2, axis=0), sensors_x[1:-1]


def reference_regression(
    trace: np.ndarray, sensors_x: np.ndarray, ref_trace: np.ndarray
):
    """Least-squares projection of each primary channel onto the reference
    channels, then subtraction. An intercept is included.

    This is the scheme with the most free parameters and therefore the most
    dangerous: with enough references it will subtract anything, including the
    signal. That is why the A-beta control and the matched null are mandatory.
    """
    n_ref = ref_trace.shape[0]
    design = np.vstack([ref_trace, np.ones((1, ref_trace.shape[1]))]).T
    coef, *_ = np.linalg.lstsq(design, trace.T, rcond=None)
    return trace - (design @ coef).T, sensors_x, n_ref


SCHEMES = ("none", "grad1", "grad2", "refreg")


# ---------------------------------------------------------------------------
# one run
# ---------------------------------------------------------------------------

def build_trace(
    cfg: s4.SimConfig,
    pop_c, pop_ab,
    rng: np.random.Generator,
    sensors_x: np.ndarray,
    t_axis: np.ndarray,
    interferers: dict[str, Interferer],
    amps: dict[str, float],
    include_signal: bool,
    include_noise: bool,
    lp_fc: float | None,
    lp_order: int,
    gains: np.ndarray,
) -> np.ndarray:
    dt = 1.0 / cfg.fs_hz
    n_samples = t_axis.size
    trace = np.zeros((sensors_x.size, n_samples))

    if include_signal:
        for pop, nbins in ((pop_c, cfg.n_velocity_bins_c), (pop_ab, cfg.n_velocity_bins_ab)):
            if pop is not None and pop.velocities.size:
                trace += s4.population_signal(
                    pop, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt,
                    n_samples, nbins, rng,
                )

    # --- interference, each with its own spatial weighting ---
    waves = {
        "cardiac": s4.cardiac_interference_trace(
            rng, t_axis, dt, cfg.n_trials, amps["cardiac"]),
        "mains": s4.mains_interference_trace(
            rng, t_axis, cfg.n_trials, amps["mains"]),
        "drift": s4.drift_interference_trace(
            rng, t_axis, dt, amps["drift"]),
        "muscle": muscle_interference_trace(
            rng, t_axis, dt, cfg.n_trials, amps["muscle"]),
    }
    for key, wave in waves.items():
        w = interferers[key].sensor_weights(sensors_x) * gains
        trace += w[:, None] * wave[None, :]

    if lp_fc is not None:
        trace = s4.apply_low_pass_filter(trace, dt, lp_fc, lp_order)
    if include_noise:
        trace += s4.averaged_noise(
            rng, sensors_x.size, n_samples, cfg.noise_asd_fT_rtHz,
            cfg.fs_hz, cfg.n_trials)
    return trace


def apply_scheme(scheme, trace, sensors_x, ref_trace):
    if scheme == "none":
        return trace, sensors_x
    if scheme == "grad1":
        return first_order_gradiometer(trace, sensors_x)
    if scheme == "grad2":
        return second_order_gradiometer(trace, sensors_x)
    if scheme == "refreg":
        out, xs, _ = reference_regression(trace, sensors_x, ref_trace)
        return out, xs
    raise ValueError(scheme)


def seed_run(
    cfg: s4.SimConfig, seed: int, bands: dict, interferers, amps,
    v_grid: np.ndarray, lp_fc: float | None, lp_order: int,
    n_null: int, ref_offset_m: float, gain_sigma: float,
) -> dict:
    """All four schemes and both bands for one seed, from ONE set of traces.

    Building the trace is the expensive step, so it is done once per seed and
    reused across schemes and bands. This is purely an efficiency change: each
    scheme still sees identical input, and each null is still pushed through
    the same rejection as its signal.
    """
    rng = np.random.default_rng(seed)
    i_ref_ab, i_ref_c = s4.calibrate_i_ref(rng, cfg)
    rng = np.random.default_rng(seed)
    pop_c = s4.build_population(rng, cfg.n_c, s4.C_FIBRE, i_ref_c)
    pop_ab = s4.build_population(rng, cfg.n_ab, s4.AB_FIBRE, i_ref_ab)
    sensors_x = cfg.sensor_positions()
    t_axis = s4.make_time_axis(cfg, min(s4.C_FIBRE.v_min, s4.AB_FIBRE.v_min))
    dt = 1.0 / cfg.fs_hz

    ref_x = sensors_x[[0, -1]] + ref_offset_m
    gain_rng = np.random.default_rng(seed + 500_000)
    gains = gain_mismatch(gain_rng, sensors_x.size, gain_sigma)
    ref_gains = gain_mismatch(gain_rng, ref_x.size, gain_sigma)

    def make(include_signal, r):
        trace = build_trace(cfg, pop_c, pop_ab, r, sensors_x, t_axis,
                            interferers, amps, include_signal, True, lp_fc,
                            lp_order, gains)
        ref = np.zeros((ref_x.size, t_axis.size))
        waves = {
            "cardiac": s4.cardiac_interference_trace(r, t_axis, dt, cfg.n_trials, amps["cardiac"]),
            "mains": s4.mains_interference_trace(r, t_axis, cfg.n_trials, amps["mains"]),
            "drift": s4.drift_interference_trace(r, t_axis, dt, amps["drift"]),
            "muscle": muscle_interference_trace(r, t_axis, dt, cfg.n_trials, amps["muscle"]),
        }
        for key, wave in waves.items():
            ref += (interferers[key].sensor_weights(ref_x) * ref_gains)[:, None] * wave[None, :]
        if lp_fc is not None:
            ref = s4.apply_low_pass_filter(ref, dt, lp_fc, lp_order)
        ref += s4.averaged_noise(r, ref_x.size, t_axis.size,
                                 cfg.noise_asd_fT_rtHz, cfg.fs_hz, cfg.n_trials)
        return trace, ref

    sig_trace, sig_ref = make(True, rng)
    null_rng = np.random.default_rng(seed + 10_000)
    null_traces = [make(False, null_rng) for _ in range(n_null)]

    out = {}
    for scheme in SCHEMES:
        proc, xs = apply_scheme(scheme, sig_trace, sensors_x, sig_ref)
        sig_energy = s4.beamform_sweep(proc, xs, t_axis, v_grid)
        null_energies = []
        for n_trace, n_ref in null_traces:
            n_proc, n_xs = apply_scheme(scheme, n_trace, sensors_x, n_ref)
            null_energies.append(s4.beamform_sweep(n_proc, n_xs, t_axis, v_grid))
        for band_name, band in bands.items():
            peak = s4.ridge_stats(v_grid, sig_energy, band)["peak_energy"]
            nulls = np.array([s4.ridge_stats(v_grid, e, band)["peak_energy"]
                              for e in null_energies])
            thresh = float(np.percentile(nulls, 95))
            out[f"{scheme}:{band_name}"] = (
                float(peak / thresh) if thresh > 0 else float("nan"))
    return out


def ci95(x: np.ndarray) -> tuple[float, float]:
    m, sd, n = float(np.mean(x)), float(np.std(x, ddof=1)), x.size
    h = 1.96 * sd / np.sqrt(n)
    return m - h, m + h


def main(argv=None):
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--seeds", type=int, default=18)
    p.add_argument("--n-null", type=int, default=40)
    p.add_argument("--trials", type=int, default=2000)
    p.add_argument("--noise-asd", type=float, default=1.0,
                   help="fT/rtHz; 1.0 = research alkali OPM, as in C-004")
    p.add_argument("--bandwidth", type=float, default=350.0)
    p.add_argument("--exponent", type=float, default=2.0,
                   help="interference falloff: 2 = current dipole, 3 = magnetic dipole")
    p.add_argument("--muscle-amp-fT", type=float, default=200.0)
    p.add_argument("--cardiac-amp-fT", type=float, default=5000.0)
    p.add_argument("--mains-amp-fT", type=float, default=2000.0)
    p.add_argument("--drift-amp-fT", type=float, default=3000.0)
    p.add_argument("--ref-offset-m", type=float, default=0.15)
    p.add_argument("--gain-sigma", type=float, default=0.003,
                   help="per-sensor gain/orientation mismatch, 1-sigma. "
                        "0.003 = 0.3%%, i.e. ~1:300 common-mode rejection, "
                        "a realistic figure for a matched OPM array.")
    p.add_argument("--out", type=Path, default=Path("results"))
    a = p.parse_args(argv)

    cfg = s4.SimConfig(n_trials=a.trials, noise_asd_fT_rtHz=a.noise_asd)
    v_grid = s4.default_v_grid()
    interferers = default_interferers(a.exponent)
    amps = {"cardiac": a.cardiac_amp_fT * 1e-15, "mains": a.mains_amp_fT * 1e-15,
            "drift": a.drift_amp_fT * 1e-15, "muscle": a.muscle_amp_fT * 1e-15}
    bands = {"C": (s4.C_FIBRE.v_min, s4.C_FIBRE.v_max),
             "Ab": (s4.AB_FIBRE.v_min, s4.AB_FIBRE.v_max)}

    # How non-uniform is each interferer across the array? Report it, because
    # if these are all ~1.0 the gradiometer result is meaningless.
    sx = cfg.sensor_positions()
    print(f"\n[geometry] {cfg.n_sensors} sensors spanning "
          f"{(sx[-1]-sx[0])*100:.1f} cm, nerve standoff {cfg.r_standoff_m*1e3:.1f} mm")
    print(f"[geometry] interference falloff exponent = {a.exponent}")
    print("[geometry] spatial non-uniformity across the array "
          "(max/min sensor weight; 1.000 = perfectly common-mode):")
    for k, it in interferers.items():
        w = it.sensor_weights(sx)
        print(f"           {k:8s} d={it.distance_m:6.3f} m  ratio={w.max()/w.min():.4f}")

    per_seed = []
    for seed in range(a.seeds):
        per_seed.append(seed_run(cfg, seed, bands, interferers, amps, v_grid,
                                 a.bandwidth, 4, a.n_null, a.ref_offset_m,
                                 a.gain_sigma))
        print(f"  seed {seed+1}/{a.seeds} done", flush=True)

    results = {}
    for scheme in SCHEMES:
        for band_name in bands:
            key = f"{scheme}:{band_name}"
            vals = np.array([r[key] for r in per_seed])
            lo, hi = ci95(vals)
            results[key] = {
                "mean": float(np.mean(vals)), "ci95": [lo, hi],
                "above_1": int(np.sum(vals > 1.0)), "n": int(vals.size),
                "min": float(vals.min()), "max": float(vals.max()),
                "values": [float(v) for v in vals],
            }
            print(f"[{scheme:6s}] {band_name:2s}-band  mean={np.mean(vals):.3f}  "
                  f"CI=[{lo:.3f}, {hi:.3f}]  above 1.0: {np.sum(vals>1.0)}/{vals.size}")

    a.out.mkdir(parents=True, exist_ok=True)
    payload = {"config": {**{k: v for k, v in asdict(cfg).items() if k != "out_dir"},
                          "seeds": a.seeds, "n_null": a.n_null,
                          "exponent": a.exponent, "amps_fT": {
                              "cardiac": a.cardiac_amp_fT, "mains": a.mains_amp_fT,
                              "drift": a.drift_amp_fT, "muscle": a.muscle_amp_fT}},
               "results": results}
    (a.out / "results.json").write_text(json.dumps(payload, indent=2))
    print(f"\nwrote {a.out / 'results.json'}")

    # --- the verdict, stated against C-008's own pre-registered threshold ---
    print("\n=== C-008 refutation threshold ===")
    print("Refuted if the mean C-band ratio stays below 1.0 with a 95% CI")
    print("excluding 1.0, WHILE the A-beta positive control still passes.")
    for scheme in ("grad1", "grad2", "refreg"):
        c, ab = results[f"{scheme}:C"], results[f"{scheme}:Ab"]
        ab_ok = ab["ci95"][0] > 1.0
        c_fail = c["ci95"][1] < 1.0
        c_pass = c["ci95"][0] > 1.0
        if not ab_ok:
            verd = "INCONCLUSIVE - positive control lost; configuration wrong"
        elif c_pass:
            verd = "CONJECTURE SURVIVES"
        elif c_fail:
            verd = "CONJECTURE REFUTED"
        else:
            verd = "INCONCLUSIVE - CI spans 1.0"
        print(f"  {scheme:6s}: C mean={c['mean']:.3f} CI=[{c['ci95'][0]:.3f},"
              f"{c['ci95'][1]:.3f}] | Ab mean={ab['mean']:.3f} -> {verd}")


if __name__ == "__main__":
    main()
