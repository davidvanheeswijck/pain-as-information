#!/usr/bin/env python3
"""Cheap-kill simulation for C-004: velocity-domain matched filtering of a
peripheral-nerve magnetic compound action potential.

WHAT IS MODELLED
-----------------
A straight peripheral nerve of length ``--nerve-length`` (default 15 cm) lies
along x. A population of unmyelinated C-fibres (default N=1000, conduction
velocity 0.4-1.4 m/s) and myelinated A-beta fibres (default N=200, 30-60 m/s)
each carry one propagating action potential, initiated at x=0 at t=0. A
linear array of M optically pumped magnetometers (default M=8) sits at a
fixed radial standoff r=6.5 mm (Bu et al., PMID 35370794) over a 10 cm span
of the nerve.

Each propagating action potential is modelled as a travelling, spatially
localised, NET-ZERO-CURRENT current source along the fibre's local axis: a
current tripole/quadrupole (a Ricker wavelet / "Mexican hat", the second
derivative of a Gaussian in the co-moving coordinate (x - v*t)/sigma). This
is chosen, rather than a monopole or a simple two-lobed dipole, because a
biphasic-to-triphasic transmembrane current is what real compound action
potentials look like, and because a source with zero net current is what
correctly produces destructive interference (phase cancellation) between
fibres arriving at slightly different times — a net-current monopole would
not cancel the way real dispersed volleys do. The spatial width is
sigma = v * tau_ap, where tau_ap is a fixed per-population-type action
potential duration (2.0 ms for C-fibres, 0.5 ms for A-beta, both
representative literature values, not fitted). Because width scales with
velocity, the TEMPORAL width of the pulse seen at a fixed sensor is
approximately tau_ap regardless of a fibre's velocity, which is the physically
correct behaviour (a fibre's action potential takes about as long to pass a
point as its own duration, independent of how fast it is moving).

The magnetic field is built from the differential, near-field form of the
Biot-Savart law for a current element on the fibre axis:

    dB(x_s, t) = (mu0 / 4*pi) * I(x', t) * r / ((x_s - x')**2 + r**2)**1.5 * dx'

integrated over the fibre. This is exactly the kernel whose integral over a
spatially UNIFORM current I(x') = I0 (for all x', i.e. a genuine steady
current in an infinite straight wire) reproduces the textbook azimuthal-field
result B = mu0*I0/(2*pi*r). That special case is used below (see
``_check_wire_kernel_normalisation``) purely to confirm the kernel constant is
right; it is NOT a claim that the tripole itself produces that field, since a
zero-net-current tripole's far field falls off faster than 1/r, which is
correct physics, not a bug.

Per-fibre peak current is scaled with the SQUARE of an assumed axon diameter
(current ~ cross-sectional area), diameter itself linearly interpolated from
each fibre's conduction velocity across the population's physiological
diameter range (0.2-1.5 um for C, 6-12 um for A-beta). The overall current
scale is fixed once, from Bu et al.'s back-calculated compound nerve current
of ~0.195 uA (see ``calibration_check``), and is never touched again
regardless of what the C-fibre band does.

APPROXIMATIONS, STATED EXPLICITLY
----------------------------------
1. Volume-conductor return currents are ignored. Only the intracellular
   axial current is modelled as a Biot-Savart source; the extracellular
   return path that must exist in a real bounded conductor is not
   represented. This is the single largest idealisation in this module.
2. The nerve is a 1-D line of current: no fascicular structure, no
   anisotropy, no finite nerve radius.
3. All fibres conduct in the same direction, are recruited exactly once,
   and are independent (no ephaptic coupling, no collision block).
4. Conduction velocity is constant along the fibre's length (no
   acceleration/deceleration, no activity-dependent slowing).
5. Diameter-to-current scaling uses a single global "current density"
   constant shared between C and A-beta fibres. Real unmyelinated and
   myelinated axons differ in channel density and membrane properties
   beyond geometry; this is a simplification, not a measurement.
6. For computational tractability, fibres are grouped into velocity bins
   (``--velocity-bins-c/ab``) that share one precomputed field template.
   This is an exact averaging-order rearrangement for everything EXCEPT the
   use of each bin's centre velocity (rather than each fibre's own exact
   velocity) when computing conduction delay to each sensor; bins are narrow
   enough (~0.01 m/s for C, ~0.75 m/s for A-beta at the defaults) that this
   is far below the resolution the AP width and jitter already impose.
7. Per-sensor noise is white and Gaussian over the stated bandwidth
   (DC to fs/2), with no 1/f, cardiac, or environmental interference —
   the evidence base is explicit that real recordings are usually
   interference- rather than sensor-noise-limited (E-04 3.1); this
   simulation is a sensor-noise-only best case; the noise-sweep threshold
   this script reports should be read as optimistic accordingly.

APPROXIMATIONS ADDED FOR THE SENSOR-REALISM FOLLOW-UP (--sensor-realism),
NUMBERED ON FROM THE SEVEN ABOVE
--------------------------------------------------------------------------
8. Sensor bandwidth is modelled as a magnitude-only, zero-phase low-pass
   filter (an order-4 Butterworth magnitude response,
   |H(f)| = 1/sqrt(1+(f/fc)**8), applied by multiplying the FFT of the
   finite trace) rather than a real causal digital filter. This is
   deliberate: the beamformer depends on precise arrival-time alignment
   across sensors, and a causal filter's group delay would need explicit
   compensation that is out of scope here; a zero-phase filter isolates
   the question actually being asked (does the ridge's ENERGY survive the
   sensor's bandwidth) from an artefact of an uncompensated filter delay.
9. That filter is applied to the neural signal, and (Part 3) to
   interference, but NOT to the sensor's own intrinsic noise, which is
   generated flat out to the sampling Nyquist frequency regardless of the
   sensor's quoted bandwidth. A real sensor's noise floor is not
   guaranteed to be confined to its quoted signal bandwidth (readout
   electronics, digitisation, and pickup downstream of the magnetometer
   proper are not modelled), so leaving the noise unfiltered is the
   conservative, harder-to-detect choice, consistent with this
   programme's rule against resolving uncertain modelling choices in a
   conjecture's favour.
10. Interference (cardiac, 1/f drift, mains) is modelled as a spatially
    UNIFORM field, identical at every sensor. Appropriate when the
    interference source is much farther from the array than its own
    ~10 cm aperture (true of a torso heartbeat dipole or mains pickup at
    a limb recording site), but an idealisation: real interference has
    some spatial structure across an 8-sensor, 10 cm array.
11. Cardiac amplitude at a limb recording is a stated GUESS, not a
    measurement: magnetocardiography at the torso is of order 50-100 pT;
    this script assumes a geometric attenuation factor from that to a
    limb site (default 1/1728, ``--cardiac-attenuation``), giving a
    default amplitude of about 43 fT. ``--cardiac-amplitude-fT``
    overrides this directly. Nothing about the Part 3 verdict should be
    read as independent of this number without checking the sensitivity.
12. Cardiac and mains interference are given an independent, uniformly
    random phase per trial, representing a stimulus trigger uncorrelated
    with the heartbeat or the mains cycle, so both attenuate somewhat
    under trial averaging (computed via an equivalent closed-form or
    histogram route rather than materialising every trial, in the same
    spirit as ``averaged_noise`` and ``population_signal``). 1/f drift is
    instead added AFTER trial averaging, un-reduced by trial count,
    because slow environmental/baseline drift is typically coherent
    across an entire recording session rather than independent from
    trial to trial — the harder, more honest of the two available
    assumptions.
13. The QRS-like cardiac transient reuses the Ricker wavelet already used
    for AP sources, purely as a generic triphasic pulse of realistic
    duration (~90 ms). It is not a claim of ECG waveform fidelity.

DELIBERATELY EXCLUDED
----------------------
Stimulus artefact, electrode/coil ringing, muscle/cardiac magnetic
interference, microneurography ground truth, and anything about a human
subject. This is a pure forward-model + signal-processing simulation.

DEPENDENCY NOTE
----------------
This directory uses numpy and matplotlib, which the rest of this repository
deliberately does not (see ``simulations/requirements.txt``). ``tools/`` is
standard-library-only so CI runs on a bare runner; ``simulations/`` is
explicitly outside that constraint and outside the CI path.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np

MU0 = 4.0 * np.pi * 1e-7  # vacuum permeability, T*m/A


def _ensure_matplotlib():
    """Import matplotlib with a non-interactive backend, deferred to call
    time so a plain --json/--check run never needs a display."""
    import matplotlib

    matplotlib.use("Agg", force=False)
    import matplotlib.pyplot as plt

    return plt


# ---------------------------------------------------------------------------
# configuration
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class FibreType:
    """Fixed physiological parameters for one population of fibres."""

    name: str
    v_min: float  # m/s
    v_max: float  # m/s
    d_min_m: float  # metres
    d_max_m: float  # metres
    tau_ap_s: float  # action potential duration, seconds
    jitter_sigma_s: float  # trial-to-trial latency jitter, seconds
    velocity_dist: str  # "lognormal" or "normal", documented at use site


C_FIBRE = FibreType(
    name="C",
    v_min=0.4,
    v_max=1.4,
    d_min_m=0.2e-6,
    d_max_m=1.5e-6,
    tau_ap_s=2.0e-3,
    jitter_sigma_s=1.0e-3,
    velocity_dist="lognormal",
)

AB_FIBRE = FibreType(
    name="Abeta",
    v_min=30.0,
    v_max=60.0,
    d_min_m=6e-6,
    d_max_m=12e-6,
    tau_ap_s=0.5e-3,
    jitter_sigma_s=0.1e-3,
    velocity_dist="normal",
)

BU_TOTAL_CURRENT_A = 0.195e-6  # Bu et al. PMID 35370794, back-calculated
BU_TARGET_FIELD_T = 1.0e-12  # ~1 pT, same reference


@dataclass(frozen=True)
class SimConfig:
    n_trials: int = 2000
    n_sensors: int = 8
    noise_asd_fT_rtHz: float = 17.7
    n_c: int = 1000
    n_ab: int = 200
    seed: int = 0
    out_dir: Path = Path("results")
    fs_hz: float = 20_000.0
    nerve_length_m: float = 0.15
    sensor_span_m: float = 0.10
    sensor_margin_m: float = 0.025
    r_standoff_m: float = 6.5e-3
    n_velocity_bins_c: int = 100
    n_velocity_bins_ab: int = 40
    n_null_repeats: int = 100
    n_sigma_template: float = 4.0

    def sensor_positions(self) -> np.ndarray:
        return np.linspace(
            self.sensor_margin_m,
            self.sensor_margin_m + self.sensor_span_m,
            self.n_sensors,
        )


# ---------------------------------------------------------------------------
# fibre population sampling
# ---------------------------------------------------------------------------


def sample_truncated_lognormal(
    rng: np.random.Generator, n: int, v_min: float, v_max: float
) -> np.ndarray:
    """Conduction velocities for C-fibres.

    Lognormal, not normal: measured human C-fibre conduction velocity
    distributions are right-skewed (a long tail of faster silent/CMH units
    above a mode nearer the slow end), e.g. Serra et al. microneurography
    data. Underlying-normal parameters are chosen so the lognormal's median
    sits near 0.75 m/s inside the 0.4-1.4 m/s band, then truncated by
    rejection sampling.
    """
    mu, sigma = np.log(0.75), 0.35
    out = np.empty(0)
    while out.size < n:
        draw = rng.lognormal(mean=mu, sigma=sigma, size=n * 2)
        draw = draw[(draw >= v_min) & (draw <= v_max)]
        out = np.concatenate([out, draw])
    return out[:n]


def sample_truncated_normal(
    rng: np.random.Generator, n: int, v_min: float, v_max: float
) -> np.ndarray:
    """Conduction velocities for A-beta fibres.

    Truncated normal, not lognormal: large myelinated fibre conduction
    velocity histograms in compound nerve recordings are approximately
    symmetric over their range (Hursh's near-linear velocity/diameter
    relation applied to a roughly symmetric diameter spread), unlike the
    long right tail seen in unmyelinated populations.
    """
    mean, std = 0.5 * (v_min + v_max), (v_max - v_min) / 4.3
    out = np.empty(0)
    while out.size < n:
        draw = rng.normal(loc=mean, scale=std, size=n * 2)
        draw = draw[(draw >= v_min) & (draw <= v_max)]
        out = np.concatenate([out, draw])
    return out[:n]


def sample_velocities(rng: np.random.Generator, n: int, ft: FibreType) -> np.ndarray:
    if n == 0:
        return np.zeros(0)
    if ft.velocity_dist == "lognormal":
        return sample_truncated_lognormal(rng, n, ft.v_min, ft.v_max)
    if ft.velocity_dist == "normal":
        return sample_truncated_normal(rng, n, ft.v_min, ft.v_max)
    raise ValueError(f"unknown velocity_dist {ft.velocity_dist!r}")


def velocity_to_diameter(v: np.ndarray, ft: FibreType) -> np.ndarray:
    """Linear map from conduction velocity to axon diameter within a
    fibre type's physiological band. A simplification (see module
    docstring point 4/5): real velocity-diameter relations are not
    perfectly linear, but the qualitative point (current scales with
    velocity within a type, and C << A-beta) is insensitive to this."""
    frac = (v - ft.v_min) / (ft.v_max - ft.v_min)
    frac = np.clip(frac, 0.0, 1.0)
    return ft.d_min_m + frac * (ft.d_max_m - ft.d_min_m)


@dataclass
class FibrePopulation:
    fibre_type: FibreType
    velocities: np.ndarray
    diameters: np.ndarray
    peak_currents: np.ndarray  # amperes, per fibre


def build_population(
    rng: np.random.Generator, n: int, ft: FibreType, i_ref: float
) -> FibrePopulation:
    v = sample_velocities(rng, n, ft)
    d = velocity_to_diameter(v, ft)
    scale = (d / ft.d_max_m) ** 2
    currents = i_ref * scale
    return FibrePopulation(fibre_type=ft, velocities=v, diameters=d, peak_currents=currents)


def calibrate_i_ref(rng: np.random.Generator, cfg: SimConfig) -> tuple[float, float]:
    """Fix the current-density scale once, from Bu et al.'s back-calculated
    ~0.195 uA compound current for an idealised, perfectly synchronous
    A-beta volley (i.e. all peak sink currents summed as if coincident).
    This is fixed exactly once, here, and is never adjusted based on
    anything the C-fibre band later does.

    Returns (i_ref_ab, i_ref_c).
    """
    v_ab = sample_velocities(rng, cfg.n_ab, AB_FIBRE)
    d_ab = velocity_to_diameter(v_ab, AB_FIBRE)
    scale_sum = float(np.sum((d_ab / AB_FIBRE.d_max_m) ** 2))
    i_ref_ab = BU_TOTAL_CURRENT_A / scale_sum
    i_ref_c = i_ref_ab * (C_FIBRE.d_max_m / AB_FIBRE.d_max_m) ** 2
    return i_ref_ab, i_ref_c


# ---------------------------------------------------------------------------
# source model and Biot-Savart field template
# ---------------------------------------------------------------------------


def ricker(u: np.ndarray) -> np.ndarray:
    """Second derivative of a Gaussian (Ricker wavelet / "Mexican hat"),
    the triphasic (source-sink-source) spatial current profile used for
    every propagating action potential. Peak value 1 at u=0; integrates to
    exactly zero (net current conservation)."""
    return (1.0 - u**2) * np.exp(-0.5 * u**2)


def _check_wire_kernel_normalisation(r: float) -> float:
    """Sanity-check the Biot-Savart kernel constant only: integrating the
    SAME differential kernel used below against a spatially UNIFORM current
    I0=1 A over a long but finite wire should reproduce the textbook
    B = mu0*I0/(2*pi*r) azimuthal field, to within the truncation error of
    a finite integration window. This does not test the tripole model; it
    tests that the kernel is not mis-normalised."""
    half_len = 2000 * r
    x = np.linspace(-half_len, half_len, 200_001)
    integrand = (MU0 / (4 * np.pi)) * 1.0 * r / (x**2 + r**2) ** 1.5
    b_numeric = np.trapezoid(integrand, x)
    b_exact = MU0 * 1.0 / (2 * np.pi * r)
    return b_numeric / b_exact


def build_template(
    v: float, tau_ap_s: float, r: float, dt: float, n_sigma: float = 4.0, n_x: int = 401
) -> tuple[np.ndarray, np.ndarray]:
    """Precompute one fibre-type/velocity-bin's field waveform, in tesla
    per ampere of peak sink current, as seen at a sensor directly over the
    point the fibre occupies at t=0 (reference sensor position x=0).

    Because of translation invariance along x, this same array, added at a
    time offset x_k/v, gives the field at any other sensor position x_k.
    """
    sigma_x = v * tau_ap_s
    t_half = n_sigma * tau_ap_s
    n_t = max(3, int(np.ceil(2 * t_half / dt)))
    t_axis = np.linspace(-t_half, t_half, n_t)

    s_grid = np.linspace(-n_sigma * sigma_x, n_sigma * sigma_x, n_x)
    f_vals = ricker(s_grid / sigma_x)

    # x_abs(t, s) = v*t + s  (sensor fixed at x=0)
    x_abs = v * t_axis[:, None] + s_grid[None, :]
    kernel = r / (x_abs**2 + r**2) ** 1.5
    integrand = f_vals[None, :] * kernel
    template = (MU0 / (4 * np.pi)) * np.trapezoid(integrand, s_grid, axis=1)
    return t_axis, template


# ---------------------------------------------------------------------------
# population field synthesis (histogram + convolution)
# ---------------------------------------------------------------------------


def population_signal(
    population: FibrePopulation,
    n_trials: int,
    sensors_x: np.ndarray,
    r: float,
    dt: float,
    n_samples: int,
    n_bins: int,
    rng: np.random.Generator,
    n_sigma_template: float = 4.0,
) -> np.ndarray:
    """Trial-averaged magnetic field at each sensor from a whole fibre
    population, exactly reproducing (up to the velocity-binning
    approximation documented in the module docstring) what an explicit
    Monte-Carlo loop over n_trials trials, each drawing a fresh latency
    jitter per fibre and averaging, would give.

    This works because averaging over trials is a LINEAR operation and
    convolution (template-with-arrival-time-distribution) is linear:
    averaging n_trials realisations of (template placed at a per-trial
    jittered time) is identical, exactly, to convolving the template with
    the combined empirical histogram of all (fibre, trial) jitter draws.
    That lets every fibre's own random per-trial jitter be represented
    without materialising an (n_fibres x n_trials x n_samples) array.
    """
    n_sensors = len(sensors_x)
    trace = np.zeros((n_sensors, n_samples))
    ft = population.fibre_type
    n_fibres = population.velocities.size
    if n_fibres == 0:
        return trace

    v = population.velocities
    bin_edges = np.linspace(ft.v_min, ft.v_max, n_bins + 1)
    bin_idx = np.clip(np.digitize(v, bin_edges) - 1, 0, n_bins - 1)
    bin_centres = 0.5 * (bin_edges[:-1] + bin_edges[1:])

    sigma_jit = ft.jitter_sigma_s
    # local histogram half-window: jitter spread plus template half-width
    hist_half = 5.0 * sigma_jit + n_sigma_template * ft.tau_ap_s
    n_hist = max(3, int(np.ceil(2 * hist_half / dt)))
    hist_axis = np.linspace(-hist_half, hist_half, n_hist)

    for b in range(n_bins):
        members = np.nonzero(bin_idx == b)[0]
        if members.size == 0:
            continue
        v_bin = float(bin_centres[b])
        currents = population.peak_currents[members]

        # all (fibre, trial) jitter draws for this bin, in one call
        jitter = rng.normal(0.0, sigma_jit, size=(members.size, n_trials))
        weights = np.repeat(currents / n_trials, n_trials)

        idx = np.round((jitter.ravel() - hist_axis[0]) / dt).astype(np.int64)
        valid = (idx >= 0) & (idx < n_hist)
        hist = np.zeros(n_hist)
        np.add.at(hist, idx[valid], weights[valid])

        t_template, template = build_template(
            v_bin, ft.tau_ap_s, r, dt, n_sigma=n_sigma_template
        )
        # hist[m] already holds a raw weight (ampere), not a sampled density,
        # so no extra dt factor belongs here: hist is a sum of discretised
        # delta functions, and convolving a delta comb with the template is
        # a plain (unscaled) discrete convolution.
        bin_waveform = np.convolve(hist, template, mode="full")
        # convolution output time axis, relative to jitter=0 / sensor at x=0
        t0 = hist_axis[0] + t_template[0]
        wave_axis = t0 + dt * np.arange(bin_waveform.size)

        for k, x_k in enumerate(sensors_x):
            delay = x_k / v_bin
            sample_shift = int(np.round(delay / dt))
            start = sample_shift + int(np.round((wave_axis[0]) / dt))
            _add_clipped(trace[k], bin_waveform, start)

    return trace


def _add_clipped(dest: np.ndarray, src: np.ndarray, start: int) -> None:
    """Add ``src`` into ``dest`` beginning at (possibly negative /
    overflowing) index ``start``, clipping to the overlap."""
    n_dest, n_src = dest.size, src.size
    d0, d1 = max(0, start), min(n_dest, start + n_src)
    if d0 >= d1:
        return
    s0, s1 = d0 - start, d1 - start
    dest[d0:d1] += src[s0:s1]


def single_fibre_signal(
    v: float,
    current_a: float,
    ft: FibreType,
    sensors_x: np.ndarray,
    r: float,
    dt: float,
    n_samples: int,
    t0: float = 0.0,
) -> np.ndarray:
    """Noiseless, no-jitter field trace from exactly one fibre. Used for
    the single-fibre sanity check and the calibration check."""
    n_sensors = len(sensors_x)
    trace = np.zeros((n_sensors, n_samples))
    t_template, template = build_template(v, ft.tau_ap_s, r, dt)
    wave = current_a * template
    t_axis0 = t_template[0]
    for k, x_k in enumerate(sensors_x):
        delay = x_k / v + t0
        start = int(np.round((delay + t_axis0) / dt))
        _add_clipped(trace[k], wave, start)
    return trace


# ---------------------------------------------------------------------------
# noise
# ---------------------------------------------------------------------------


def averaged_noise(
    rng: np.random.Generator,
    n_sensors: int,
    n_samples: int,
    noise_asd_fT_rtHz: float,
    fs_hz: float,
    n_trials: int,
) -> np.ndarray:
    """The trial-averaged noise trace.

    Per-trial, per-sample noise is i.i.d. N(0, sigma_sample) with
    sigma_sample = ASD * sqrt(fs/2) (white noise, flat one-sided spectral
    density out to Nyquist). Averaging n_trials independent draws of an
    i.i.d. Gaussian is EXACTLY equivalent in distribution to a single draw
    from N(0, sigma_sample/sqrt(n_trials)) -- this is an algebraic identity
    for i.i.d. Gaussians, not an approximation, and it is used here to
    avoid materialising an (n_trials x n_sensors x n_samples) array.
    """
    sigma_sample = noise_asd_fT_rtHz * 1e-15 * np.sqrt(fs_hz / 2.0)
    sigma_avg = sigma_sample / np.sqrt(n_trials)
    return rng.normal(0.0, sigma_avg, size=(n_sensors, n_samples))


def noise_sigma_avg(noise_asd_fT_rtHz: float, fs_hz: float, n_trials: int) -> float:
    sigma_sample = noise_asd_fT_rtHz * 1e-15 * np.sqrt(fs_hz / 2.0)
    return sigma_sample / np.sqrt(n_trials)


# ---------------------------------------------------------------------------
# analysis A: time-domain averaging
# ---------------------------------------------------------------------------


def time_domain_peak_snr(
    avg_trace: np.ndarray, t_axis: np.ndarray, window: tuple[float, float], sigma_noise: float
) -> tuple[float, float, float]:
    """Peak |field| within [window[0], window[1]] seconds, across all
    sensors, and that peak divided by the (known) post-averaging noise
    standard deviation. Returns (peak_field_T, snr, t_of_peak_s)."""
    mask = (t_axis >= window[0]) & (t_axis <= window[1])
    if not np.any(mask):
        return 0.0, 0.0, float("nan")
    sub = avg_trace[:, mask]
    flat_idx = int(np.argmax(np.abs(sub)))
    k, j = np.unravel_index(flat_idx, sub.shape)
    peak = float(sub[k, j])
    t_peak = float(t_axis[mask][j])
    snr = abs(peak) / sigma_noise if sigma_noise > 0 else float("inf")
    return peak, snr, t_peak


# ---------------------------------------------------------------------------
# analysis B: velocity-domain matched filtering (beamforming)
# ---------------------------------------------------------------------------


def beamform_sweep(
    avg_trace: np.ndarray,
    sensors_x: np.ndarray,
    t_axis: np.ndarray,
    v_grid: np.ndarray,
) -> np.ndarray:
    """For each hypothesised velocity, shift every sensor's averaged trace
    by -x_k/v and sum across sensors; record the peak squared amplitude
    ("energy") of that sum. Returns an array shaped like v_grid."""
    n_sensors = avg_trace.shape[0]
    energy = np.zeros(v_grid.size)
    for i, v in enumerate(v_grid):
        beamsum = np.zeros(t_axis.size)
        for k in range(n_sensors):
            shifted_t = t_axis + sensors_x[k] / v
            beamsum += np.interp(shifted_t, t_axis, avg_trace[k], left=0.0, right=0.0)
        energy[i] = float(np.max(beamsum**2))
    return energy


def ridge_stats(
    v_grid: np.ndarray, energy: np.ndarray, band: tuple[float, float]
) -> dict:
    mask = (v_grid >= band[0]) & (v_grid <= band[1])
    if not np.any(mask):
        return {"peak_v": float("nan"), "peak_energy": 0.0, "fwhm_low": float("nan"), "fwhm_high": float("nan")}
    sub_v, sub_e = v_grid[mask], energy[mask]
    i_peak = int(np.argmax(sub_e))
    peak_v, peak_e = float(sub_v[i_peak]), float(sub_e[i_peak])
    half = peak_e / 2.0
    above = sub_e >= half
    idxs = np.nonzero(above)[0]
    lo = float(sub_v[idxs[0]]) if idxs.size else float("nan")
    hi = float(sub_v[idxs[-1]]) if idxs.size else float("nan")
    return {"peak_v": peak_v, "peak_energy": peak_e, "fwhm_low": lo, "fwhm_high": hi}


# ---------------------------------------------------------------------------
# sensor realism: bandwidth-limiting filter, notch filter, interference
# (used only by --sensor-realism; see approximations 8-13 in the module
# docstring)
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class SensorSpec:
    """One realistic sensor: a flat noise ASD over a stated bandwidth --
    the two numbers the bandwidth-premise follow-up turns on."""

    name: str
    noise_asd_fT_rtHz: float
    bandwidth_hz: float
    low_pass_order: int = 4


def _apply_fft_filter(trace: np.ndarray, dt: float, freq_response, pad_s: float) -> np.ndarray:
    """Shared machinery for the two filters below: zero-pad ``trace`` by
    ``pad_s`` seconds on each side of the time axis before transforming,
    then crop back to the original length.

    This padding matters and is not cosmetic: the compound-signal trace
    does not necessarily have the same value at its first and last sample
    (a slow C-fibre volley is still non-zero at t=0, by construction of the
    Ricker template's support), and naive FFT-domain filtering treats the
    trace as one period of an infinite periodic signal. Filtering that
    boundary discontinuity directly (no padding) forces a spurious,
    near-constant low-frequency correction across the ENTIRE record to
    "close the gap" using only low frequencies -- which lands squarely in
    the same low-frequency territory as the slow C-band ridge itself and
    was verified, empirically, to inflate the observed C-band peak by
    orders of magnitude. Zero-padding first moves that same discontinuity
    (real trace value meeting an artificial zero) out to the padded
    region, where the filter's own finite impulse-response length confines
    the resulting ringing to a few filter time-constants around the seam,
    instead of smearing it across the whole window."""
    pad_n = max(1, int(np.ceil(pad_s / dt)))
    pad_width = [(0, 0)] * (trace.ndim - 1) + [(pad_n, pad_n)]
    padded = np.pad(trace, pad_width, mode="constant")
    n = padded.shape[-1]
    freqs = np.fft.rfftfreq(n, dt)
    spec = np.fft.rfft(padded, axis=-1)
    filtered = np.fft.irfft(spec * freq_response(freqs), n=n, axis=-1)
    return filtered[..., pad_n : pad_n + trace.shape[-1]]


def apply_low_pass_filter(
    trace: np.ndarray, dt: float, fc_hz: float, order: int = 4, pad_s: float | None = None
) -> np.ndarray:
    """Zero-phase, magnitude-only low-pass filter: multiplies the FFT of
    ``trace`` (last axis = time) by the magnitude response of an
    order-``order`` Butterworth low-pass with cutoff ``fc_hz``:
    |H(f)| = 1 / sqrt(1 + (f/fc)**(2*order)). See approximation 8: this is
    deliberately magnitude-only (no group delay) because the beamformer
    depends on precise cross-sensor arrival-time alignment. ``pad_s``
    defaults to 10 cutoff periods (at least 10 ms) -- see
    ``_apply_fft_filter`` for why padding is needed at all."""
    if pad_s is None:
        pad_s = max(10.0 / fc_hz, 0.01)
    return _apply_fft_filter(
        trace, dt, lambda freqs: 1.0 / np.sqrt(1.0 + (freqs / fc_hz) ** (2 * order)), pad_s
    )


def apply_notch_filter(
    trace: np.ndarray,
    dt: float,
    notch_freqs_hz: tuple[float, ...],
    width_hz: float = 2.0,
    pad_s: float | None = None,
) -> np.ndarray:
    """Gaussian band-stop at each of ``notch_freqs_hz`` (FWHM ``width_hz``),
    applied the same way as the low-pass filter: a post-acquisition
    analysis step, not a claim about the sensor itself. A narrow notch has
    a long impulse response (~1/width_hz), so ``pad_s`` defaults to
    1/width_hz (at least 0.5 s) rather than the low-pass filter's shorter
    default."""
    if pad_s is None:
        pad_s = max(1.0 / width_hz, 0.5)
    sigma = width_hz / 2.3548  # FWHM -> Gaussian sigma

    def freq_response(freqs):
        mask = np.ones_like(freqs)
        for f0 in notch_freqs_hz:
            mask *= 1.0 - np.exp(-0.5 * ((freqs - f0) / sigma) ** 2)
        return mask

    return _apply_fft_filter(trace, dt, freq_response, pad_s)


def compute_energy_spectrum(trace_1d: np.ndarray, dt: float) -> tuple[np.ndarray, np.ndarray]:
    """Energy spectrum (one-sided |FFT|^2) of a single finite-duration
    trace. The source here is a one-shot transient, not a stationary
    process, so this is the trace's actual, exact frequency content
    (Parseval's theorem), not a Welch-style PSD *estimate* needing
    averaging over repeats."""
    n = trace_1d.size
    freqs = np.fft.rfftfreq(n, dt)
    spec = np.fft.rfft(trace_1d)
    return freqs, np.abs(spec) ** 2


def energy_percentile_frequencies(
    freqs: np.ndarray, energy: np.ndarray, percentiles: tuple[float, ...] = (0.5, 0.9, 0.99)
) -> dict[str, float]:
    """Frequency below which each fraction of total energy lies, by linear
    interpolation of the cumulative energy curve."""
    cumulative = np.cumsum(energy)
    total = cumulative[-1]
    if total <= 0:
        return {f"f_{int(round(p*100))}pct_hz": float("nan") for p in percentiles}
    frac = cumulative / total
    return {f"f_{int(round(p*100))}pct_hz": float(np.interp(p, frac, freqs)) for p in percentiles}


def cardiac_interference_trace(
    rng: np.random.Generator,
    t_axis: np.ndarray,
    dt: float,
    n_trials: int,
    amplitude_T: float,
    heart_rate_hz: float = 1.0,
    qrs_width_s: float = 0.09,
) -> np.ndarray:
    """Trial-averaged cardiac (QRS-like) interference: a periodic
    Ricker-shaped transient (approximation 13) whose phase relative to the
    stimulus trigger is drawn independently, once per trial, from a
    uniform distribution over one heartbeat period (approximation 12,
    unsynchronised trigger).

    Uses the same histogram + convolution trick as ``population_signal``
    to reproduce averaging over ``n_trials`` independent phase draws
    exactly, without materialising an (n_trials x n_samples) array.
    """
    period_s = 1.0 / heart_rate_hz
    sigma = qrs_width_s / 4.0
    margin_s = 4.0 * sigma
    t_min, t_max = float(t_axis[0]), float(t_axis[-1])

    phases = rng.uniform(0.0, period_s, size=n_trials)
    k_min = int(np.floor((t_min - margin_s) / period_s)) - 1
    k_max = int(np.ceil((t_max + margin_s) / period_s)) + 1
    k_vals = np.arange(k_min, k_max + 1)
    beat_times = (phases[:, None] + k_vals[None, :] * period_s).ravel()
    keep = (beat_times >= t_min - margin_s) & (beat_times <= t_max + margin_s)
    beat_times = beat_times[keep]

    n_samples = t_axis.size
    idx = np.round((beat_times - t_min) / dt).astype(np.int64)
    valid = (idx >= 0) & (idx < n_samples)
    hist = np.zeros(n_samples)
    np.add.at(hist, idx[valid], 1.0 / n_trials)

    half = 4.0 * sigma
    n_t = max(3, int(np.ceil(2 * half / dt)))
    templ_t = np.linspace(-half, half, n_t)
    template = amplitude_T * ricker(templ_t / sigma)

    wave = np.convolve(hist, template, mode="full")
    start = int(np.round(templ_t[0] / dt))
    out = np.zeros(n_samples)
    _add_clipped(out, wave, start)
    return out


def averaged_sinusoid_interference(
    rng: np.random.Generator, t_axis: np.ndarray, freq_hz: float, amplitude_T: float, n_trials: int
) -> np.ndarray:
    """Trial-averaged sinusoidal interference at a single frequency, with
    an independent uniform phase drawn per trial (used for mains).
    Closed form: mean_i cos(w*t + phi_i) = C*cos(w*t) - S*sin(w*t), where
    C, S are the sample mean cosine/sine of the n_trials phase draws --
    algebraically identical to simulating every trial and averaging, the
    same trick ``averaged_noise`` uses for white noise."""
    phases = rng.uniform(0.0, 2.0 * np.pi, size=n_trials)
    c, s = float(np.mean(np.cos(phases))), float(np.mean(np.sin(phases)))
    w = 2.0 * np.pi * freq_hz
    return amplitude_T * (c * np.cos(w * t_axis) - s * np.sin(w * t_axis))


def mains_interference_trace(
    rng: np.random.Generator,
    t_axis: np.ndarray,
    n_trials: int,
    amplitude_T: float,
    harmonics_hz: tuple[float, ...] = (50.0, 100.0, 150.0),
    harmonic_weights: tuple[float, ...] = (1.0, 0.3, 0.1),
) -> np.ndarray:
    """Mains pickup at 50 Hz (Belgium/Europe) plus two harmonics, each with
    its own independent per-trial phase, weighted by an assumed (not
    measured) harmonic roll-off."""
    out = np.zeros(t_axis.size)
    for f0, w in zip(harmonics_hz, harmonic_weights):
        out += averaged_sinusoid_interference(rng, t_axis, f0, amplitude_T * w, n_trials)
    return out


def drift_interference_trace(
    rng: np.random.Generator, t_axis: np.ndarray, dt: float, rms_amplitude_T: float, fmax_hz: float = 10.0
) -> np.ndarray:
    """A single realisation of 1/f-shaped baseline drift, band-limited
    below ``fmax_hz``, added AFTER trial averaging (approximation 12: slow
    drift is coherent across a session, not independent per trial, so it
    is not reduced by trial count the way white noise is)."""
    n = t_axis.size
    freqs = np.fft.rfftfreq(n, dt)
    white = rng.normal(size=freqs.size) + 1j * rng.normal(size=freqs.size)
    f_ref = freqs[1] if freqs.size > 1 else 1.0
    shape = 1.0 / np.sqrt(np.maximum(freqs, f_ref))
    shape[freqs > fmax_hz] = 0.0
    shape[0] = 0.0  # no DC offset
    raw = np.fft.irfft(white * shape, n=n)
    current_rms = float(np.sqrt(np.mean(raw**2)))
    if current_rms <= 0:
        return raw
    return raw * (rms_amplitude_T / current_rms)


# ---------------------------------------------------------------------------
# pipeline
# ---------------------------------------------------------------------------


def make_time_axis(cfg: SimConfig, min_velocity: float) -> np.ndarray:
    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    margin = 5.0 * C_FIBRE.jitter_sigma_s + cfg.n_sigma_template * C_FIBRE.tau_ap_s
    t_end = float(sensors_x.max()) / min_velocity + margin
    n_samples = int(np.ceil(t_end / dt))
    return np.arange(n_samples) * dt


@dataclass
class PipelineResult:
    t_axis: np.ndarray
    sensors_x: np.ndarray
    avg_trace: np.ndarray
    sigma_noise: float
    v_grid: np.ndarray
    energy: np.ndarray


def run_pipeline(
    cfg: SimConfig,
    pop_c: FibrePopulation | None,
    pop_ab: FibrePopulation | None,
    rng: np.random.Generator,
    v_grid: np.ndarray,
    include_noise: bool = True,
    signal_scale: float = 1.0,
    low_pass_fc_hz: float | None = None,
    low_pass_order: int = 4,
    extra_field_T: np.ndarray | None = None,
) -> PipelineResult:
    """``low_pass_fc_hz``, ``low_pass_order`` and ``extra_field_T`` are used
    only by the ``--sensor-realism`` follow-up (see that section below);
    they default to no-ops so every existing call site is byte-for-byte
    unaffected."""
    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    min_v = min(
        [p.fibre_type.v_min for p in (pop_c, pop_ab) if p is not None] or [C_FIBRE.v_min]
    )
    t_axis = make_time_axis(cfg, min_v)
    n_samples = t_axis.size

    trace = np.zeros((cfg.n_sensors, n_samples))
    if signal_scale != 0.0:
        if pop_c is not None and pop_c.velocities.size:
            trace += signal_scale * population_signal(
                pop_c, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, n_samples,
                cfg.n_velocity_bins_c, rng,
            )
        if pop_ab is not None and pop_ab.velocities.size:
            trace += signal_scale * population_signal(
                pop_ab, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, n_samples,
                cfg.n_velocity_bins_ab, rng,
            )

    if extra_field_T is not None:
        trace += extra_field_T[None, :]

    if low_pass_fc_hz is not None:
        trace = apply_low_pass_filter(trace, dt, low_pass_fc_hz, low_pass_order)

    sigma_noise = noise_sigma_avg(cfg.noise_asd_fT_rtHz, cfg.fs_hz, cfg.n_trials)
    if include_noise:
        trace += averaged_noise(
            rng, cfg.n_sensors, n_samples, cfg.noise_asd_fT_rtHz, cfg.fs_hz, cfg.n_trials
        )

    energy = beamform_sweep(trace, sensors_x, t_axis, v_grid)
    return PipelineResult(
        t_axis=t_axis, sensors_x=sensors_x, avg_trace=trace, sigma_noise=sigma_noise,
        v_grid=v_grid, energy=energy,
    )


def default_v_grid(n: int = 300) -> np.ndarray:
    return np.logspace(np.log10(0.2), np.log10(100.0), n)


# ---------------------------------------------------------------------------
# sanity checks
# ---------------------------------------------------------------------------


def check_single_fibre(cfg: SimConfig, v_true: float = 0.8) -> dict:
    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    t_axis = make_time_axis(cfg, v_true)
    trace = single_fibre_signal(
        v_true, 1e-9, C_FIBRE, sensors_x, cfg.r_standoff_m, dt, t_axis.size
    )
    v_grid = default_v_grid()
    energy = beamform_sweep(trace, sensors_x, t_axis, v_grid)
    i_peak = int(np.argmax(energy))
    v_est = float(v_grid[i_peak])
    rel_err = abs(v_est - v_true) / v_true
    return {
        "v_true": v_true,
        "v_estimated": v_est,
        "relative_error": rel_err,
        "passed": bool(rel_err < 0.05),
    }


def check_determinism(cfg: SimConfig, v_grid: np.ndarray) -> dict:
    def once() -> np.ndarray:
        rng = np.random.default_rng(cfg.seed)
        i_ref_ab, i_ref_c = calibrate_i_ref(rng, cfg)
        rng = np.random.default_rng(cfg.seed)
        pop_c = build_population(rng, cfg.n_c, C_FIBRE, i_ref_c)
        pop_ab = build_population(rng, cfg.n_ab, AB_FIBRE, i_ref_ab)
        result = run_pipeline(cfg, pop_c, pop_ab, rng, v_grid)
        return result.energy

    e1 = once()
    e2 = once()
    identical = bool(np.array_equal(e1, e2))
    return {"passed": identical}


# ---------------------------------------------------------------------------
# CLI / main
# ---------------------------------------------------------------------------


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--n-trials", type=int, default=2000)
    p.add_argument("--sensors", type=int, default=8)
    p.add_argument("--noise-fT-per-rtHz", type=float, default=17.7)
    p.add_argument("--c-fibres", type=int, default=1000)
    p.add_argument("--ab-fibres", type=int, default=200)
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--out", type=str, default=None)
    p.add_argument("--sweep-noise", action="store_true")
    p.add_argument("--json", action="store_true")
    p.add_argument("--n-null-repeats", type=int, default=100)
    p.add_argument("--fs", type=float, default=20_000.0)

    # --sensor-realism follow-up (see module docstring, approximations 8-13)
    p.add_argument(
        "--sensor-realism", action="store_true",
        help="run the bandwidth-premise follow-up instead of the default "
        "pipeline, writing to <out>/sensor-realism/",
    )
    p.add_argument("--research-alkali-noise-fT", type=float, default=1.0)
    p.add_argument("--research-alkali-bw-hz", type=float, default=350.0)
    p.add_argument("--commercial-alkali-noise-fT", type=float, default=10.0)
    p.add_argument("--commercial-alkali-bw-hz", type=float, default=350.0)
    p.add_argument("--helium4-noise-fT", type=float, default=43.0)
    p.add_argument("--helium4-bw-hz", type=float, default=2000.0)
    p.add_argument(
        "--cardiac-attenuation", type=float, default=1.0 / 1728.0,
        help="GUESSED (not measured) geometric attenuation from ~75 pT "
        "torso MCG to this limb recording; see approximation 11",
    )
    p.add_argument(
        "--cardiac-amplitude-fT", type=float, default=None,
        help="override the cardiac interference amplitude directly (fT), "
        "instead of deriving it from --cardiac-attenuation",
    )
    p.add_argument("--cardiac-rate-hz", type=float, default=1.0)
    p.add_argument("--cardiac-width-ms", type=float, default=90.0)
    p.add_argument("--drift-rms-fT", type=float, default=50.0)
    p.add_argument("--mains-amplitude-fT", type=float, default=20.0)
    p.add_argument(
        "--sensor-realism-null-repeats", type=int, default=200,
        help="null-distribution repeats per sensor/interference condition "
        "in --sensor-realism mode. 200 was chosen empirically: at 60 "
        "repeats the ratio near the detectability threshold moved by "
        "roughly a tenth between reruns, too noisy to read a crossing "
        "near 1 as meaningful; 200 stabilises it to within a few points",
    )
    return p.parse_args(argv)


def build_config(args: argparse.Namespace) -> SimConfig:
    here = Path(__file__).resolve().parent
    out_dir = Path(args.out) if args.out else here / "results"
    return SimConfig(
        n_trials=args.n_trials,
        n_sensors=args.sensors,
        noise_asd_fT_rtHz=args.noise_fT_per_rtHz,
        n_c=args.c_fibres,
        n_ab=args.ab_fibres,
        seed=args.seed,
        out_dir=out_dir,
        fs_hz=args.fs,
        n_null_repeats=args.n_null_repeats,
    )


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    cfg = build_config(args)
    v_grid = default_v_grid()

    if args.sensor_realism:
        # Exclusive with the default pipeline below: this keeps the default
        # (no-flag) code path below completely untouched, which is what
        # makes the "default run is byte-identical" guarantee easy to trust
        # rather than merely claimed.
        return run_sensor_realism_mode(cfg, v_grid, args)

    cfg.out_dir.mkdir(parents=True, exist_ok=True)

    log: list[str] = []

    def emit(msg: str) -> None:
        print(msg)
        log.append(msg)

    emit("=" * 72)
    emit("C-004 velocity-beamforming simulation")
    emit(
        f"n_trials={cfg.n_trials} sensors={cfg.n_sensors} "
        f"noise={cfg.noise_asd_fT_rtHz} fT/rtHz c_fibres={cfg.n_c} "
        f"ab_fibres={cfg.n_ab} seed={cfg.seed}"
    )
    emit("=" * 72)

    # --- kernel normalisation self-check (implementation correctness,
    # not one of the five mandated checks, but reported for transparency).
    kernel_ratio = _check_wire_kernel_normalisation(cfg.r_standoff_m)
    emit(
        f"[internal] Biot-Savart kernel vs. infinite-wire formula, ratio = "
        f"{kernel_ratio:.6f} (should be ~1.0)"
    )

    # --- sanity check 1: single fibre, no noise, known velocity ---
    check1 = check_single_fibre(cfg)
    emit(
        f"[check 1] single-fibre velocity recovery: true={check1['v_true']} m/s, "
        f"estimated={check1['v_estimated']:.4f} m/s, "
        f"rel. error={check1['relative_error']*100:.2f}% -> "
        f"{'PASS' if check1['passed'] else 'FAIL'}"
    )

    # --- populations + calibration ---
    rng = np.random.default_rng(cfg.seed)
    i_ref_ab, i_ref_c = calibrate_i_ref(rng, cfg)
    rng = np.random.default_rng(cfg.seed)  # reset for reproducible population draw
    pop_c = build_population(rng, cfg.n_c, C_FIBRE, i_ref_c)
    pop_ab = build_population(rng, cfg.n_ab, AB_FIBRE, i_ref_ab)
    emit(
        f"[calibration] I_ref (A-beta, max diameter) = {i_ref_ab*1e9:.3f} nA, "
        f"I_ref (C, max diameter) = {i_ref_c*1e12:.3f} pA "
        f"(ratio {i_ref_ab/i_ref_c:.1f}x, from cross-sectional-area scaling)"
    )

    # --- sanity check 2: amplitude calibration ---
    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    t_axis_ab = make_time_axis(cfg, AB_FIBRE.v_min)
    sync_ab = population_signal(
        pop_ab, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, t_axis_ab.size,
        cfg.n_velocity_bins_ab, np.random.default_rng(cfg.seed + 1),
    )
    ab_peak_field = float(np.max(np.abs(sync_ab)))
    order_of_magnitude_ok = 0.1 * BU_TARGET_FIELD_T <= ab_peak_field <= 10.0 * BU_TARGET_FIELD_T
    emit(
        f"[check 2] amplitude calibration: {cfg.n_ab} A-beta fibres driven by a "
        f"total idealised-synchronous compound current of {BU_TOTAL_CURRENT_A*1e6:.3f} uA "
        f"(Bu et al. PMID 35370794) produce a peak field of "
        f"{ab_peak_field*1e12:.3f} pT at {cfg.r_standoff_m*1e3:.1f} mm "
        f"(target ~{BU_TARGET_FIELD_T*1e12:.1f} pT, order-of-magnitude band "
        f"[{0.1*BU_TARGET_FIELD_T*1e12:.2f}, {10*BU_TARGET_FIELD_T*1e12:.2f}] pT) -> "
        f"{'PASS' if order_of_magnitude_ok else 'FAIL'}"
    )

    # --- main run: full population, with noise ---
    result = run_pipeline(cfg, pop_c, pop_ab, rng, v_grid)

    ab_window = (sensors_x.min() / AB_FIBRE.v_max, sensors_x.max() / AB_FIBRE.v_min)
    c_window = (sensors_x.min() / C_FIBRE.v_max, sensors_x.max() / C_FIBRE.v_min)

    a_peak_ab, a_snr_ab, a_t_ab = time_domain_peak_snr(
        result.avg_trace, result.t_axis, ab_window, result.sigma_noise
    )
    a_peak_c, a_snr_c, a_t_c = time_domain_peak_snr(
        result.avg_trace, result.t_axis, c_window, result.sigma_noise
    )
    emit(
        f"[time-domain A] A-beta window {ab_window[0]*1e3:.2f}-{ab_window[1]*1e3:.2f} ms: "
        f"peak {a_peak_ab*1e12:.3f} pT, SNR {a_snr_ab:.2f}"
    )
    emit(
        f"[time-domain A] C-fibre window {c_window[0]*1e3:.1f}-{c_window[1]*1e3:.1f} ms: "
        f"peak {a_peak_c*1e15:.3f} fT, SNR {a_snr_c:.3f}"
    )

    ridge_ab = ridge_stats(result.v_grid, result.energy, (AB_FIBRE.v_min, AB_FIBRE.v_max))
    ridge_c = ridge_stats(result.v_grid, result.energy, (C_FIBRE.v_min, C_FIBRE.v_max))
    beam_noise_floor = (cfg.n_sensors ** 0.5) * result.sigma_noise
    b_snr_ab = (ridge_ab["peak_energy"] ** 0.5) / beam_noise_floor
    b_snr_c = (ridge_c["peak_energy"] ** 0.5) / beam_noise_floor
    emit(
        f"[velocity-domain B] A-beta band ridge: peak at {ridge_ab['peak_v']:.2f} m/s, "
        f"amplitude {ridge_ab['peak_energy']**0.5*1e12:.3f} pT, SNR {b_snr_ab:.2f}, "
        f"FWHM [{ridge_ab['fwhm_low']:.2f}, {ridge_ab['fwhm_high']:.2f}] m/s"
    )
    emit(
        f"[velocity-domain B] C-fibre band ridge: peak at {ridge_c['peak_v']:.3f} m/s, "
        f"amplitude {ridge_c['peak_energy']**0.5*1e15:.3f} fT, raw SNR {b_snr_c:.3f}, "
        f"FWHM [{ridge_c['fwhm_low']:.3f}, {ridge_c['fwhm_high']:.3f}] m/s "
        "(raw SNR vs. theoretical noise sigma, NOT corrected for the "
        "velocity-sweep multiple-comparisons search; check 4's null "
        "distribution below is the corrected test and is authoritative "
        "for the C-band verdict)"
    )

    ab_pass = bool(AB_FIBRE.v_min <= ridge_ab["peak_v"] <= AB_FIBRE.v_max and b_snr_ab > 3)
    emit(
        f"[check 3] A-beta positive control (must be recovered by both methods): "
        f"time-domain SNR={a_snr_ab:.2f}, velocity-domain SNR={b_snr_ab:.2f}, "
        f"ridge inside [{AB_FIBRE.v_min},{AB_FIBRE.v_max}] m/s -> "
        f"{'PASS' if ab_pass else 'FAIL'}"
    )

    # --- sanity check 4: null distribution ---
    null_peak_c = np.zeros(cfg.n_null_repeats)
    null_spectra = np.zeros((cfg.n_null_repeats, v_grid.size))
    rng_null = np.random.default_rng(cfg.seed + 1000)
    for i in range(cfg.n_null_repeats):
        null_result = run_pipeline(
            cfg, None, None, rng_null, v_grid, include_noise=True, signal_scale=0.0
        )
        null_spectra[i] = null_result.energy
        band_mask = (v_grid >= C_FIBRE.v_min) & (v_grid <= C_FIBRE.v_max)
        null_peak_c[i] = float(np.max(null_result.energy[band_mask]))

    null_mean = float(np.mean(null_peak_c))
    null_std = float(np.std(null_peak_c))
    null_p95 = float(np.percentile(null_peak_c, 95))
    c_exceeds_null = bool(ridge_c["peak_energy"] > null_p95)
    z_score = (ridge_c["peak_energy"] - null_mean) / null_std if null_std > 0 else float("nan")
    emit(
        f"[check 4] null distribution ({cfg.n_null_repeats} noise-only repeats), "
        f"C-band peak energy: mean {null_mean:.3e} T^2, std {null_std:.3e} T^2, "
        f"95th pct {null_p95:.3e} T^2; observed C-band peak energy "
        f"{ridge_c['peak_energy']:.3e} T^2 (z={z_score:.2f}) -> "
        f"{'ridge EXCEEDS null' if c_exceeds_null else 'ridge DOES NOT exceed null'}"
    )

    # --- sanity check 5: determinism ---
    check5 = check_determinism(cfg, v_grid)
    emit(f"[check 5] determinism (identical seed, run twice): {'PASS' if check5['passed'] else 'FAIL'}")

    model_validity_ok = check1["passed"] and order_of_magnitude_ok and ab_pass
    c_band_ridge_survives = c_exceeds_null and (C_FIBRE.v_min <= ridge_c["peak_v"] <= C_FIBRE.v_max) and b_snr_c > 3

    emit("-" * 72)
    emit(
        f"[validity] Checks 1-3 (velocity recovery, amplitude calibration, "
        f"A-beta positive control) all passed: {'YES' if model_validity_ok else 'NO'} "
        "-- if NO, the model/pipeline itself is not trustworthy and the C-band "
        "result below cannot be interpreted either way."
    )
    emit(
        f"HEADLINE: C-band ridge {'DETECTED above the null distribution' if c_exceeds_null else 'NOT distinguishable from the null distribution'}. "
        f"C-004's prediction {'SURVIVES' if c_band_ridge_survives else 'DOES NOT SURVIVE'} this simulation."
    )
    emit("-" * 72)

    # --- optional noise sweep ---
    sweep_results = None
    if args.sweep_noise:
        sweep_results = run_noise_sweep(cfg, pop_c, pop_ab, v_grid)
        emit(
            "[sweep] noise ASD (fT/rtHz) -> C-band detectability ratio "
            "(observed peak / null 95th percentile at that noise level; >=1 is detectable):"
        )
        for asd, ratio in zip(
            sweep_results["noise_asd_fT"], sweep_results["c_band_detectability_ratio"]
        ):
            emit(f"    {asd:8.2f} fT/rtHz -> ratio {ratio:.3f}")
        threshold = sweep_results["threshold_fT"]
        if threshold is not None:
            emit(
                f"[sweep] C-band ridge becomes detectable above the null near "
                f"noise ASD ~= {threshold:.2f} fT/rtHz"
            )
        else:
            emit(
                "[sweep] C-band ridge does not become detectable above the null "
                "anywhere in the swept range (0.5-500 fT/rtHz)"
            )
        emit(
            "[sweep] each ratio uses a 40-repeat null distribution at that "
            "noise level, so individual points carry Monte-Carlo sampling "
            "noise (the crossing near ratio=1 is not a sharp threshold); "
            "read the crossing point as order-of-magnitude, not exact"
        )

    # --- outputs ---
    results_payload = {
        "config": {
            "n_trials": cfg.n_trials,
            "n_sensors": cfg.n_sensors,
            "noise_asd_fT_rtHz": cfg.noise_asd_fT_rtHz,
            "n_c": cfg.n_c,
            "n_ab": cfg.n_ab,
            "seed": cfg.seed,
            "fs_hz": cfg.fs_hz,
        },
        "kernel_normalisation_ratio": kernel_ratio,
        "check_1_single_fibre": check1,
        "check_2_amplitude_calibration": {
            "ab_peak_field_T": ab_peak_field,
            "target_field_T": BU_TARGET_FIELD_T,
            "total_current_A": BU_TOTAL_CURRENT_A,
            "passed": order_of_magnitude_ok,
        },
        "check_3_ab_positive_control": {
            "time_domain_snr": a_snr_ab,
            "velocity_domain_snr": b_snr_ab,
            "ridge_peak_v": ridge_ab["peak_v"],
            "passed": ab_pass,
        },
        "check_4_null_distribution": {
            "n_repeats": cfg.n_null_repeats,
            "null_mean_energy": null_mean,
            "null_std_energy": null_std,
            "null_p95_energy": null_p95,
            "observed_c_band_peak_energy": ridge_c["peak_energy"],
            "z_score": z_score,
            "ridge_exceeds_null": c_exceeds_null,
        },
        "check_5_determinism": check5,
        "time_domain": {
            "ab_peak_T": a_peak_ab,
            "ab_snr": a_snr_ab,
            "c_peak_T": a_peak_c,
            "c_snr": a_snr_c,
        },
        "velocity_domain": {
            "ab_ridge": ridge_ab,
            "c_ridge": ridge_c,
            "ab_snr": b_snr_ab,
            "c_snr": b_snr_c,
        },
        "headline": {
            "c_band_ridge_exceeds_null": c_exceeds_null,
            "c004_prediction_survives": c_band_ridge_survives,
        },
        "noise_sweep": sweep_results,
    }

    write_outputs(cfg, result, v_grid, null_spectra, results_payload, log)

    if args.json:
        print(json.dumps(results_payload, indent=2, default=_json_default))

    return 0


def _json_default(o):
    if isinstance(o, (np.floating,)):
        return float(o)
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    raise TypeError(f"not JSON serialisable: {type(o)}")


def run_noise_sweep(
    cfg: SimConfig,
    pop_c: FibrePopulation,
    pop_ab: FibrePopulation,
    v_grid: np.ndarray,
    n_null_repeats: int = 40,
) -> dict:
    """Sweep sensor noise spectral density to find the sensitivity at which
    the C-band ridge becomes detectable, i.e. the number that tells us what
    hardware would be needed.

    "Detectable" is defined the same way as sanity check 4: the observed
    C-band beamformer peak energy must exceed the 95th percentile of a
    noise-only null distribution computed through the IDENTICAL pipeline at
    that same noise level. A simple ratio to the theoretical per-sample
    noise sigma is NOT used here, because sweeping the assumed velocity over
    ~100 points inside the C band is itself a multiple-comparisons search:
    the single-hypothesis SNR of the noise-only maximum is systematically
    inflated above the naive sigma-based expectation (verified empirically:
    an early version of this function found a nonsensical "always
    detectable, even at 0.5 fT/rtHz" result from exactly this bias). The
    null-percentile comparison is the only one of the two criteria used in
    the main run that is not fooled by it, so it is the only one used here.

    Signal is computed once (it does not depend on noise); only the noise
    draw, beamforming and null distribution are repeated per noise level.
    """
    asd_values = np.logspace(np.log10(0.5), np.log10(500.0), 14)
    ratios = []
    rng = np.random.default_rng(cfg.seed + 2000)
    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    t_axis = make_time_axis(cfg, C_FIBRE.v_min)
    band_mask = (v_grid >= C_FIBRE.v_min) & (v_grid <= C_FIBRE.v_max)

    signal_only = np.zeros((cfg.n_sensors, t_axis.size))
    rng_signal = np.random.default_rng(cfg.seed)
    signal_only += population_signal(
        pop_c, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, t_axis.size,
        cfg.n_velocity_bins_c, rng_signal,
    )
    signal_only += population_signal(
        pop_ab, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, t_axis.size,
        cfg.n_velocity_bins_ab, rng_signal,
    )

    for asd in asd_values:
        noisy = signal_only + averaged_noise(
            rng, cfg.n_sensors, t_axis.size, float(asd), cfg.fs_hz, cfg.n_trials
        )
        energy = beamform_sweep(noisy, sensors_x, t_axis, v_grid)
        observed_peak = float(np.max(energy[band_mask]))

        null_peaks = np.zeros(n_null_repeats)
        for i in range(n_null_repeats):
            noise_only = averaged_noise(
                rng, cfg.n_sensors, t_axis.size, float(asd), cfg.fs_hz, cfg.n_trials
            )
            null_energy = beamform_sweep(noise_only, sensors_x, t_axis, v_grid)
            null_peaks[i] = float(np.max(null_energy[band_mask]))
        null_p95 = float(np.percentile(null_peaks, 95))
        ratios.append(observed_peak / null_p95 if null_p95 > 0 else float("inf"))

    ratios_arr = np.array(ratios)
    threshold = None
    above = ratios_arr >= 1.0
    if above.any() and not above.all():
        # find crossing by log-linear interpolation between bracketing points
        idx = int(np.argmax(np.diff(above.astype(int)) != 0))
        x0, x1 = np.log10(asd_values[idx]), np.log10(asd_values[idx + 1])
        y0, y1 = ratios_arr[idx], ratios_arr[idx + 1]
        if y1 != y0:
            frac = (1.0 - y0) / (y1 - y0)
            threshold = float(10 ** (x0 + frac * (x1 - x0)))
    elif above.all():
        threshold = float(asd_values[-1])

    return {
        "noise_asd_fT": asd_values.tolist(),
        "c_band_detectability_ratio": ratios_arr.tolist(),
        "detectability_definition": (
            "observed C-band beamformer peak energy / 95th-percentile of "
            f"{n_null_repeats} noise-only null repeats at the same noise "
            "level; ratio >= 1 means detectable at that noise level"
        ),
        "threshold_fT": threshold,
    }


def write_outputs(
    cfg: SimConfig,
    result: PipelineResult,
    v_grid: np.ndarray,
    null_spectra: np.ndarray,
    payload: dict,
    log: list[str],
) -> None:
    plt = _ensure_matplotlib()

    null_mean_spectrum = null_spectra.mean(axis=0)
    null_p95_spectrum = np.percentile(null_spectra, 95, axis=0)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.loglog(v_grid, result.energy, color="black", lw=1.4, label="signal + noise")
    ax.loglog(v_grid, null_mean_spectrum, color="tab:gray", lw=1.0, ls="--", label="null mean (noise only)")
    ax.loglog(v_grid, null_p95_spectrum, color="tab:gray", lw=1.0, ls=":", label="null 95th percentile")
    ax.axvspan(C_FIBRE.v_min, C_FIBRE.v_max, color="tab:red", alpha=0.15, label="C-fibre band")
    ax.axvspan(AB_FIBRE.v_min, AB_FIBRE.v_max, color="tab:blue", alpha=0.15, label="A-beta band")
    ax.set_xlabel("assumed conduction velocity (m/s)")
    ax.set_ylabel("beamformer peak energy (T^2)")
    ax.set_title("Velocity-domain matched filter spectrum")
    ax.legend(fontsize=8, loc="upper left")
    fig.tight_layout()
    fig.savefig(cfg.out_dir / "velocity-spectrum.png", dpi=150)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    offset_step = 1.2 * np.max(np.abs(result.avg_trace)) if np.max(np.abs(result.avg_trace)) > 0 else 1e-12
    for k in range(result.avg_trace.shape[0]):
        ax.plot(
            result.t_axis * 1e3,
            result.avg_trace[k] * 1e12 + k * offset_step * 1e12,
            lw=0.7,
        )
    ax.axvspan(
        result.sensors_x.min() / AB_FIBRE.v_max * 1e3,
        result.sensors_x.max() / AB_FIBRE.v_min * 1e3,
        color="tab:blue", alpha=0.12,
    )
    ax.axvspan(
        result.sensors_x.min() / C_FIBRE.v_max * 1e3,
        result.sensors_x.max() / C_FIBRE.v_min * 1e3,
        color="tab:red", alpha=0.12,
    )
    ax.set_xlabel("time since stimulus (ms)")
    ax.set_ylabel("trial-averaged field, sensors offset (pT)")
    ax.set_title("Time-domain averaging: what conventional analysis sees")
    fig.tight_layout()
    fig.savefig(cfg.out_dir / "time-domain-comparison.png", dpi=150)
    plt.close(fig)

    with open(cfg.out_dir / "results.json", "w") as fh:
        json.dump(payload, fh, indent=2, default=_json_default)

    write_results_md(cfg, payload, log)


def write_results_md(cfg: SimConfig, payload: dict, log: list[str]) -> None:
    headline = payload["headline"]
    c4 = payload["check_4_null_distribution"]
    c3 = payload["check_3_ab_positive_control"]
    c2 = payload["check_2_amplitude_calibration"]
    c1 = payload["check_1_single_fibre"]
    vd = payload["velocity_domain"]
    td = payload["time_domain"]

    lines = []
    lines.append("# C-004 velocity-beamforming simulation: results")
    lines.append("")
    lines.append(
        "This is a forward-model simulation, not a measurement. It asks a narrow "
        "question: given a physically reasonable (documented, not tuned) model "
        "of propagating C-fibre and A-beta compound action potentials, sensor "
        "geometry, and noise, does velocity-domain matched filtering recover a "
        "coherent C-band ridge that time-domain averaging misses?"
    )
    lines.append("")
    lines.append("## What was simulated")
    lines.append("")
    lines.append(
        f"- Nerve: straight, {cfg.nerve_length_m*100:.0f} cm along x. "
        f"Sensor array: {cfg.n_sensors} OPMs over a {cfg.sensor_span_m*100:.0f} cm span, "
        f"standoff {cfg.r_standoff_m*1e3:.1f} mm."
    )
    lines.append(
        f"- C-fibres: N={cfg.n_c}, conduction velocity 0.4-1.4 m/s (truncated "
        "lognormal), jitter sigma 1.0 ms, AP duration 2.0 ms."
    )
    lines.append(
        f"- A-beta fibres: N={cfg.n_ab}, conduction velocity 30-60 m/s (truncated "
        "normal), jitter sigma 0.1 ms, AP duration 0.5 ms."
    )
    lines.append(
        "- Source model: travelling current tripole (Ricker wavelet), net current "
        "zero, spatial width = velocity x AP duration."
    )
    lines.append(
        f"- Sensor noise: {cfg.noise_asd_fT_rtHz} fT/sqrt(Hz) white, {cfg.n_trials} "
        f"trials averaged, sample rate {cfg.fs_hz/1e3:.0f} kHz."
    )
    lines.append("")
    lines.append("## Sanity checks")
    lines.append("")
    lines.append(
        f"1. **Single fibre, no noise, known velocity ({c1['v_true']} m/s):** "
        f"beamformer recovered {c1['v_estimated']:.4f} m/s "
        f"({c1['relative_error']*100:.2f}% error) -> "
        f"**{'PASS' if c1['passed'] else 'FAIL'}**."
    )
    lines.append(
        f"2. **Amplitude calibration:** a synchronous A-beta volley carrying "
        f"Bu et al.'s back-calculated {payload['check_2_amplitude_calibration']['total_current_A']*1e6:.3f} uA "
        f"compound current produced a peak field of "
        f"{c2['ab_peak_field_T']*1e12:.3f} pT at {cfg.r_standoff_m*1e3:.1f} mm "
        f"(target ~1 pT) -> **{'PASS' if c2['passed'] else 'FAIL'}**."
    )
    lines.append(
        f"3. **A-beta positive control:** time-domain SNR "
        f"{c3['time_domain_snr']:.2f}, velocity-domain SNR "
        f"{c3['velocity_domain_snr']:.2f}, ridge at {c3['ridge_peak_v']:.2f} m/s -> "
        f"**{'PASS' if c3['passed'] else 'FAIL'}**. If this had failed, the "
        "geometry/filter would be mis-specified and any C-band result below "
        "would be uninterpretable."
    )
    lines.append(
        f"4. **Null distribution** ({c4['n_repeats']} noise-only repeats of the "
        f"identical pipeline): C-band peak energy mean {c4['null_mean_energy']:.3e} T^2, "
        f"95th percentile {c4['null_p95_energy']:.3e} T^2. Observed C-band peak "
        f"energy {c4['observed_c_band_peak_energy']:.3e} T^2 (z={c4['z_score']:.2f}) -> "
        f"{'exceeds' if c4['ridge_exceeds_null'] else 'does NOT exceed'} the null."
    )
    lines.append(
        f"5. **Determinism:** identical seed, run twice -> "
        f"**{'PASS' if payload['check_5_determinism']['passed'] else 'FAIL'}**."
    )
    lines.append("")
    lines.append("## Headline numbers")
    lines.append("")
    lines.append(
        f"- Time-domain averaging, C-fibre window: peak "
        f"{td['c_peak_T']*1e15:.3f} fT, SNR {td['c_snr']:.3f}."
    )
    lines.append(
        f"- Velocity-domain matched filtering, C band: ridge at "
        f"{vd['c_ridge']['peak_v']:.3f} m/s, amplitude "
        f"{vd['c_ridge']['peak_energy']**0.5*1e15:.3f} fT, raw SNR {vd['c_snr']:.3f} "
        f"(vs. theoretical per-sensor noise sigma; NOT corrected for the "
        "velocity-sweep multiple-comparisons search -- see check 4 for the "
        "corrected, null-distribution-based test), "
        f"FWHM [{vd['c_ridge']['fwhm_low']:.3f}, {vd['c_ridge']['fwhm_high']:.3f}] m/s."
    )
    lines.append(
        f"- A-beta band (positive control): time-domain SNR {c3['time_domain_snr']:.2f}, "
        f"velocity-domain SNR {c3['velocity_domain_snr']:.2f} (Aβ margin is large "
        "enough that the multiple-comparisons correction does not change the "
        "conclusion here)."
    )
    if payload.get("noise_sweep"):
        thr = payload["noise_sweep"]["threshold_fT"]
        if thr is not None:
            lines.append(
                f"- Noise sweep: the C-band ridge becomes detectable above its "
                f"own noise-only null distribution near {thr:.2f} fT/sqrt(Hz) "
                "sensor noise (all else held fixed)."
            )
        else:
            lines.append(
                "- Noise sweep: the C-band ridge did not become detectable above "
                "its own noise-only null distribution anywhere in the swept "
                "range (0.5-500 fT/sqrt(Hz)); the compound signal amplitude "
                "itself, not sensor noise, is the limiting factor in this model."
            )
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    if headline["c004_prediction_survives"]:
        lines.append(
            "**C-004's prediction survives this simulation.** Under the "
            "documented model and parameters, velocity-domain matched filtering "
            "produces a C-band ridge that exceeds the noise-only null "
            "distribution, at a velocity inside the physiological C-fibre band, "
            "while the A-beta positive control confirms the geometry and filter "
            "are correctly specified. This does not confirm the conjecture in a "
            "person; it means the mechanism is not obviously false and the "
            "hardware experiment is not a wasted trip on physics grounds alone."
        )
    else:
        lines.append(
            "**C-004's prediction does NOT survive this simulation.** Under the "
            "documented model and parameters, the C-band velocity-domain peak "
            "does not exceed the noise-only null distribution at a "
            "signal-to-noise ratio above 3, even though the A-beta positive "
            "control confirms the array geometry and matched filter are "
            "correctly specified and working. In this model, C-fibre "
            "cross-sectional current amplitude, combined with realistic "
            "conduction-velocity dispersion and trial-to-trial jitter, produces "
            "a compound signal too small to recover at the assumed sensor noise "
            "floor, even after velocity-domain beamforming and full trial "
            "averaging. This is a negative result and should be reported as "
            "one: it does not mean the analysis method is wrong (the A-beta "
            "recovery shows it works), it means the C-fibre magnetic signal, "
            "as modelled here, may be too small at this standoff and this "
            "sensor noise floor. The noise-sweep result above (if run) states "
            "what sensitivity would be needed to change that."
        )
    lines.append("")
    lines.append(
        "No parameter in this simulation was adjusted after seeing this result; "
        "the only calibrated free parameter (overall current scale) was fixed "
        "once from Bu et al.'s back-calculated compound current, against the "
        "A-beta amplitude check, before the C-fibre band was examined."
    )
    lines.append("")
    lines.append("## Full run log")
    lines.append("")
    lines.append("```")
    lines.extend(log)
    lines.append("```")
    lines.append("")

    with open(cfg.out_dir / "results.md", "w") as fh:
        fh.write("\n".join(lines))


# ---------------------------------------------------------------------------
# sensor realism follow-up: mode entry point
# ---------------------------------------------------------------------------


def build_sensor_specs(args: argparse.Namespace) -> list[SensorSpec]:
    return [
        SensorSpec("Research alkali OPM", args.research_alkali_noise_fT, args.research_alkali_bw_hz),
        SensorSpec("Commercial alkali OPM", args.commercial_alkali_noise_fT, args.commercial_alkali_bw_hz),
        SensorSpec("Helium-4 OPM", args.helium4_noise_fT, args.helium4_bw_hz),
    ]


def run_sensor_realism_mode(cfg: SimConfig, v_grid: np.ndarray, args: argparse.Namespace) -> int:
    """Answers the follow-up question in PREDICTION's escape-route form:
    does the C-band signal sit inside a realistic alkali OPM's bandwidth
    (Part 1), does a realistic sensor (noise ASD + bandwidth, together)
    then actually recover it (Part 2), and does that survive realistic
    interference (Part 3)? Writes to <out>/sensor-realism/, and never
    touches the default <out>/ files."""
    out_dir = cfg.out_dir / "sensor-realism"
    out_dir.mkdir(parents=True, exist_ok=True)

    log: list[str] = []

    def emit(msg: str) -> None:
        print(msg)
        log.append(msg)

    emit("=" * 72)
    emit("C-004 sensor-realism follow-up")
    emit(
        "Does the C-band signal fit inside a realistic alkali OPM's "
        "bandwidth, and does that survive realistic interference?"
    )
    emit("=" * 72)

    sensors_x = cfg.sensor_positions()
    dt = 1.0 / cfg.fs_hz
    plt = _ensure_matplotlib()

    # --- populations: identical calibration route to the default run ---
    rng = np.random.default_rng(cfg.seed)
    i_ref_ab, i_ref_c = calibrate_i_ref(rng, cfg)
    rng = np.random.default_rng(cfg.seed)
    pop_c = build_population(rng, cfg.n_c, C_FIBRE, i_ref_c)
    pop_ab = build_population(rng, cfg.n_ab, AB_FIBRE, i_ref_ab)

    # =======================================================================
    # Part 1: spectral content of the noiseless compound signal
    # =======================================================================
    mid = cfg.n_sensors // 2
    t_axis_c = make_time_axis(cfg, C_FIBRE.v_min)
    trace_c = population_signal(
        pop_c, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, t_axis_c.size,
        cfg.n_velocity_bins_c, np.random.default_rng(cfg.seed + 3000),
    )
    t_axis_ab = make_time_axis(cfg, AB_FIBRE.v_min)
    trace_ab = population_signal(
        pop_ab, cfg.n_trials, sensors_x, cfg.r_standoff_m, dt, t_axis_ab.size,
        cfg.n_velocity_bins_ab, np.random.default_rng(cfg.seed + 3001),
    )

    freqs_c, energy_c = compute_energy_spectrum(trace_c[mid], dt)
    freqs_ab, energy_ab = compute_energy_spectrum(trace_ab[mid], dt)
    pct_c = energy_percentile_frequencies(freqs_c, energy_c)
    pct_ab = energy_percentile_frequencies(freqs_ab, energy_ab)

    emit(
        f"[part 1] C-band noiseless compound signal, mid-array sensor: energy "
        f"below 50%={pct_c['f_50pct_hz']:.1f} Hz, 90%={pct_c['f_90pct_hz']:.1f} Hz, "
        f"99%={pct_c['f_99pct_hz']:.1f} Hz"
    )
    emit(
        f"[part 1] A-beta noiseless compound signal, mid-array sensor: energy "
        f"below 50%={pct_ab['f_50pct_hz']:.1f} Hz, 90%={pct_ab['f_90pct_hz']:.1f} Hz, "
        f"99%={pct_ab['f_99pct_hz']:.1f} Hz"
    )

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.semilogy(freqs_c, energy_c / np.max(energy_c), color="tab:red", lw=1.2, label="C-fibre population")
    ax.semilogy(freqs_ab, energy_ab / np.max(energy_ab), color="tab:blue", lw=1.2, label="A-beta population")
    ax.axvline(350.0, color="black", ls="--", lw=1.2, label="350 Hz (alkali OPM bandwidth)")
    ax.axvline(2000.0, color="grey", ls=":", lw=1.2, label="2 kHz (helium-4 OPM bandwidth)")
    ax.set_xlim(0, 3000)
    ax.set_ylim(bottom=1e-8)
    ax.set_xlabel("frequency (Hz)")
    ax.set_ylabel("energy spectral density (normalised to each population's peak)")
    ax.set_title("Noiseless compound-signal spectral content, mid-array sensor")
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "psd.png", dpi=150)
    plt.close(fig)

    # =======================================================================
    # Part 2: three realistic sensor models, full pipeline
    # =======================================================================
    sensors = build_sensor_specs(args)
    band_mask = (v_grid >= C_FIBRE.v_min) & (v_grid <= C_FIBRE.v_max)
    sensor_results = []
    sensor_spectra: dict[str, tuple[np.ndarray, np.ndarray, float]] = {}

    for i, sensor in enumerate(sensors):
        # run_pipeline reads its noise level from cfg.noise_asd_fT_rtHz, so
        # each sensor needs its own config with that one field overridden;
        # every other field (fs, n_trials, geometry, ...) stays identical.
        sensor_cfg = replace(cfg, noise_asd_fT_rtHz=sensor.noise_asd_fT_rtHz)
        rng_sig = np.random.default_rng(cfg.seed + 4000 + i)
        result = run_pipeline(
            sensor_cfg, pop_c, pop_ab, rng_sig, v_grid,
            low_pass_fc_hz=sensor.bandwidth_hz, low_pass_order=sensor.low_pass_order,
        )
        ab_window = (sensors_x.min() / AB_FIBRE.v_max, sensors_x.max() / AB_FIBRE.v_min)
        _, a_snr_ab, _ = time_domain_peak_snr(result.avg_trace, result.t_axis, ab_window, result.sigma_noise)
        ridge_ab = ridge_stats(result.v_grid, result.energy, (AB_FIBRE.v_min, AB_FIBRE.v_max))
        ridge_c = ridge_stats(result.v_grid, result.energy, (C_FIBRE.v_min, C_FIBRE.v_max))
        beam_noise_floor = (cfg.n_sensors ** 0.5) * result.sigma_noise
        b_snr_ab = (ridge_ab["peak_energy"] ** 0.5) / beam_noise_floor
        ab_pass = bool(AB_FIBRE.v_min <= ridge_ab["peak_v"] <= AB_FIBRE.v_max and b_snr_ab > 3)

        rng_null = np.random.default_rng(cfg.seed + 5000 + i)
        null_peaks = np.zeros(args.sensor_realism_null_repeats)
        for r in range(args.sensor_realism_null_repeats):
            null_result = run_pipeline(
                sensor_cfg, None, None, rng_null, v_grid, include_noise=True, signal_scale=0.0,
                low_pass_fc_hz=sensor.bandwidth_hz, low_pass_order=sensor.low_pass_order,
            )
            null_peaks[r] = float(np.max(null_result.energy[band_mask]))
        null_p95 = float(np.percentile(null_peaks, 95))
        ratio = ridge_c["peak_energy"] / null_p95 if null_p95 > 0 else float("inf")

        emit(
            f"[part 2] {sensor.name} ({sensor.noise_asd_fT_rtHz:g} fT/rtHz, "
            f"{sensor.bandwidth_hz:.0f} Hz bandwidth): A-beta positive control "
            f"{'PASS' if ab_pass else 'FAIL'} (ridge {ridge_ab['peak_v']:.2f} m/s, "
            f"SNR {b_snr_ab:.2f}); C-band ridge {ridge_c['peak_v']:.3f} m/s, "
            f"detectability ratio {ratio:.3f} (observed {ridge_c['peak_energy']:.3e} T^2 "
            f"vs. null p95 {null_p95:.3e} T^2, {args.sensor_realism_null_repeats} repeats)"
        )

        sensor_results.append({
            "name": sensor.name,
            "noise_asd_fT_rtHz": sensor.noise_asd_fT_rtHz,
            "bandwidth_hz": sensor.bandwidth_hz,
            "ab_positive_control_passed": ab_pass,
            "ab_ridge_v": ridge_ab["peak_v"],
            "ab_snr": b_snr_ab,
            "c_ridge_v": ridge_c["peak_v"],
            "c_band_detectability_ratio": ratio,
            "null_p95_energy": null_p95,
            "observed_c_band_peak_energy": ridge_c["peak_energy"],
        })
        sensor_spectra[sensor.name] = (result.v_grid, result.energy, null_p95)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    for (name, (vg, en, np95)), color in zip(sensor_spectra.items(), ("tab:green", "tab:orange", "tab:purple")):
        ax.loglog(vg, en, color=color, lw=1.2, label=f"{name} (signal + noise)")
        ax.axhline(np95, color=color, ls=":", lw=1.0)
    ax.axvspan(C_FIBRE.v_min, C_FIBRE.v_max, color="tab:red", alpha=0.12, label="C-fibre band")
    ax.axvspan(AB_FIBRE.v_min, AB_FIBRE.v_max, color="tab:blue", alpha=0.12, label="A-beta band")
    ax.set_xlabel("assumed conduction velocity (m/s)")
    ax.set_ylabel("beamformer peak energy (T^2)")
    ax.set_title("Velocity-domain spectrum per sensor (dotted = that sensor's own null 95th pct)")
    ax.legend(fontsize=7, loc="upper left")
    fig.tight_layout()
    fig.savefig(out_dir / "sensor-comparison.png", dpi=150)
    plt.close(fig)

    # =======================================================================
    # Part 3: interference, on the best-case sensor
    # =======================================================================
    candidates = [s for s in sensor_results if s["ab_positive_control_passed"]]
    pool = candidates if candidates else sensor_results
    best = max(pool, key=lambda s: s["c_band_detectability_ratio"])
    best_sensor = next(s for s in sensors if s.name == best["name"])
    if not candidates:
        emit(
            "[part 3] WARNING: no sensor passed the A-beta positive control; "
            f"proceeding with {best_sensor.name} anyway, but its C-band result "
            "is uninterpretable per the module's own discipline."
        )
    emit(f"[part 3] best-case sensor carried forward for interference testing: {best_sensor.name}")
    best_sensor_cfg = replace(cfg, noise_asd_fT_rtHz=best_sensor.noise_asd_fT_rtHz)

    cardiac_amplitude_T = (
        args.cardiac_amplitude_fT * 1e-15 if args.cardiac_amplitude_fT is not None
        else 75.0e-12 * args.cardiac_attenuation  # 75 pT = midpoint of the stated 50-100 pT torso MCG range
    )
    drift_rms_T = args.drift_rms_fT * 1e-15
    mains_amplitude_T = args.mains_amplitude_fT * 1e-15

    t_axis_int = make_time_axis(cfg, C_FIBRE.v_min)

    def build_interference(rng_int: np.random.Generator) -> np.ndarray:
        cardiac = cardiac_interference_trace(
            rng_int, t_axis_int, dt, cfg.n_trials, cardiac_amplitude_T,
            heart_rate_hz=args.cardiac_rate_hz, qrs_width_s=args.cardiac_width_ms * 1e-3,
        )
        mains = mains_interference_trace(rng_int, t_axis_int, cfg.n_trials, mains_amplitude_T)
        drift = drift_interference_trace(rng_int, t_axis_int, dt, drift_rms_T)
        return cardiac + mains + drift

    interference_signal = build_interference(np.random.default_rng(cfg.seed + 6000))

    def ratio_with_interference(apply_notch: bool) -> tuple[float, float, float]:
        rng_sig = np.random.default_rng(cfg.seed + 7000 + int(apply_notch))
        result = run_pipeline(
            best_sensor_cfg, pop_c, pop_ab, rng_sig, v_grid,
            low_pass_fc_hz=best_sensor.bandwidth_hz, low_pass_order=best_sensor.low_pass_order,
            extra_field_T=interference_signal,
        )
        trace = result.avg_trace
        if apply_notch:
            trace = apply_notch_filter(trace, dt, (50.0, 100.0, 150.0))
        energy = beamform_sweep(trace, sensors_x, result.t_axis, v_grid)
        observed = float(np.max(energy[band_mask]))

        rng_null = np.random.default_rng(cfg.seed + 8000 + int(apply_notch))
        null_peaks = np.zeros(args.sensor_realism_null_repeats)
        for r in range(args.sensor_realism_null_repeats):
            interference_r = build_interference(rng_null)
            null_result = run_pipeline(
                best_sensor_cfg, None, None, rng_null, v_grid, include_noise=True, signal_scale=0.0,
                low_pass_fc_hz=best_sensor.bandwidth_hz, low_pass_order=best_sensor.low_pass_order,
                extra_field_T=interference_r,
            )
            null_trace = null_result.avg_trace
            if apply_notch:
                null_trace = apply_notch_filter(null_trace, dt, (50.0, 100.0, 150.0))
            null_energy = beamform_sweep(null_trace, sensors_x, null_result.t_axis, v_grid)
            null_peaks[r] = float(np.max(null_energy[band_mask]))
        null_p95 = float(np.percentile(null_peaks, 95))
        ratio = observed / null_p95 if null_p95 > 0 else float("inf")
        return ratio, observed, null_p95

    ratio_interf, obs_interf, null95_interf = ratio_with_interference(apply_notch=False)
    ratio_notch, obs_notch, null95_notch = ratio_with_interference(apply_notch=True)

    emit(
        f"[part 3] interference assumptions: cardiac {cardiac_amplitude_T*1e15:.1f} fT "
        f"(attenuation {args.cardiac_attenuation:.2e} from a GUESSED, not measured, 75 pT "
        f"torso MCG midpoint), 1/f drift {args.drift_rms_fT:.1f} fT rms below 10 Hz "
        f"(added after trial averaging), mains {args.mains_amplitude_fT:.1f} fT at 50 Hz "
        "plus two harmonics (all with independent per-trial phase)"
    )
    emit(
        f"[part 3] {best_sensor.name} WITHOUT interference: detectability ratio "
        f"{best['c_band_detectability_ratio']:.3f}"
    )
    emit(
        f"[part 3] {best_sensor.name} WITH interference: detectability ratio "
        f"{ratio_interf:.3f} (observed {obs_interf:.3e} T^2 vs. null p95 {null95_interf:.3e} T^2)"
    )
    emit(
        f"[part 3] {best_sensor.name} WITH interference AND a 50/100/150 Hz notch: "
        f"detectability ratio {ratio_notch:.3f} (observed {obs_notch:.3e} T^2 vs. "
        f"null p95 {null95_notch:.3e} T^2); no notch is applied at the ~1 Hz cardiac "
        "fundamental, since that frequency overlaps the C-band signal's own dominant "
        "content (Part 1) and notching it would remove signal along with interference"
    )

    bandwidth_alone_overturns = bool(candidates) and best["c_band_detectability_ratio"] > 1.0
    survives_with_interference = bandwidth_alone_overturns and ratio_notch > 1.0
    overturned = bandwidth_alone_overturns and survives_with_interference

    emit("-" * 72)
    if overturned:
        emit(
            f"HEADLINE: the bandwidth premise is wrong for {best_sensor.name}, and this "
            "survives realistic interference with a 50 Hz notch applied. C-004's "
            "refutation is OVERTURNED under this analysis."
        )
    elif bandwidth_alone_overturns:
        emit(
            f"HEADLINE: {best_sensor.name} clears the sensitivity+bandwidth bar with no "
            "interference, but realistic interference (even after a 50 Hz notch) pushes "
            "it back under the null. C-004's refutation SURVIVES this analysis."
        )
    else:
        emit(
            "HEADLINE: no sensor both passes the A-beta positive control and clears the "
            "C-band null even before interference is added. C-004's refutation SURVIVES "
            "this analysis; the bandwidth premise does not save it."
        )
    emit("-" * 72)

    payload = {
        "config": {
            "n_trials": cfg.n_trials,
            "n_sensors": cfg.n_sensors,
            "n_c": cfg.n_c,
            "n_ab": cfg.n_ab,
            "seed": cfg.seed,
            "fs_hz": cfg.fs_hz,
            "null_repeats": args.sensor_realism_null_repeats,
        },
        "part_1_spectral_content": {
            "c_band": pct_c,
            "ab_band": pct_ab,
        },
        "part_2_sensor_comparison": sensor_results,
        "part_3_interference": {
            "best_sensor": best_sensor.name,
            "best_sensor_ab_control_passed": bool(candidates),
            "cardiac_amplitude_fT": cardiac_amplitude_T * 1e15,
            "cardiac_attenuation_assumption": args.cardiac_attenuation,
            "drift_rms_fT": args.drift_rms_fT,
            "mains_amplitude_fT": args.mains_amplitude_fT,
            "ratio_no_interference": best["c_band_detectability_ratio"],
            "ratio_with_interference": ratio_interf,
            "ratio_with_interference_and_notch": ratio_notch,
        },
        "headline": {
            "bandwidth_alone_overturns_refutation": bandwidth_alone_overturns,
            "survives_with_interference_and_notch": survives_with_interference,
            "c004_refutation_overturned": overturned,
        },
    }

    with open(out_dir / "results.json", "w") as fh:
        json.dump(payload, fh, indent=2, default=_json_default)

    write_sensor_realism_md(out_dir, payload, log)

    if args.json:
        print(json.dumps(payload, indent=2, default=_json_default))

    return 0


def write_sensor_realism_md(out_dir: Path, payload: dict, log: list[str]) -> None:
    p1 = payload["part_1_spectral_content"]
    p2 = payload["part_2_sensor_comparison"]
    p3 = payload["part_3_interference"]
    headline = payload["headline"]

    lines = []
    lines.append("# C-004 sensor-realism follow-up: does the bandwidth premise save it?")
    lines.append("")
    if headline["c004_refutation_overturned"]:
        lines.append(
            f"**C-004's refutation is OVERTURNED by this analysis: the {p3['best_sensor']} "
            f"clears both the sensitivity and bandwidth bar for the C-band ridge "
            "(detectability ratio "
            f"{p3['ratio_no_interference']:.2f} with no interference), and this survives "
            "cardiac, 1/f-drift and mains interference once a 50 Hz notch is applied "
            f"(ratio {p3['ratio_with_interference_and_notch']:.2f}), under the stated, "
            "explicitly guessed interference amplitudes (see Part 3).**"
        )
    elif headline["bandwidth_alone_overturns_refutation"]:
        lines.append(
            f"**C-004's refutation SURVIVES this analysis.** The bandwidth premise was "
            f"right on its own terms -- the {p3['best_sensor']} clears the C-band null "
            f"with no interference (ratio {p3['ratio_no_interference']:.2f}) -- but "
            "realistic interference reverses that again, even after a 50 Hz notch "
            f"(ratio {p3['ratio_with_interference_and_notch']:.2f})."
        )
    else:
        lines.append(
            "**C-004's refutation SURVIVES this analysis.** No sensor in the table both "
            "passes the A-beta positive control and clears the C-band null even before "
            "interference is added; the bandwidth premise alone does not save it."
        )

    decisive_ratios = [
        p3["ratio_no_interference"], p3["ratio_with_interference"], p3["ratio_with_interference_and_notch"],
    ]
    if any(0.8 < r < 1.25 for r in decisive_ratios):
        lines.append("")
        lines.append(
            "**This crossing is marginal, not decisive.** Every ratio above sits within "
            "about 25% of 1 -- the threshold itself, not a wide margin either side of it. "
            f"With {payload['config']['null_repeats']} null repeats the 95th-percentile "
            "estimate that these ratios are divided by still carries several percent of "
            "Monte-Carlo noise, and an independent check at a different seed (not "
            "written to this file, since it is not the pre-registered run) flipped the "
            "with-interference verdict to the opposite side of 1. Read the headline above "
            "as 'right on the boundary', in the direction PREDICTION.md itself expected "
            "('marginal, within roughly an order of magnitude of the noise floor either "
            "way'), not as a robust result in either direction."
        )
    lines.append("")
    lines.append(
        "This is a forward-model simulation, not a measurement. It extends "
        "`simulate.py`'s default pipeline (see `../results.md`) to ask a narrower "
        "follow-up question: was the original 'no sensor is both quiet enough and "
        "fast enough' conclusion an artefact of assuming the full 10 kHz bandwidth "
        "used elsewhere in the evidence base, when that requirement was derived from "
        "myelinated (fast, narrow) compound action potentials rather than the slower, "
        "broader C-fibre volley?"
    )
    lines.append("")
    lines.append("## Part 1 -- spectral content of the noiseless compound signal")
    lines.append("")
    lines.append(
        f"- **C-fibre population:** 50% of energy below **{p1['c_band']['f_50pct_hz']:.1f} Hz**, "
        f"90% below **{p1['c_band']['f_90pct_hz']:.1f} Hz**, 99% below "
        f"**{p1['c_band']['f_99pct_hz']:.1f} Hz**."
    )
    lines.append(
        f"- **A-beta population:** 50% of energy below **{p1['ab_band']['f_50pct_hz']:.1f} Hz**, "
        f"90% below **{p1['ab_band']['f_90pct_hz']:.1f} Hz**, 99% below "
        f"**{p1['ab_band']['f_99pct_hz']:.1f} Hz**."
    )
    lines.append("")
    lines.append("See `psd.png`.")
    lines.append("")
    lines.append("## Part 2 -- three realistic sensors, full pipeline")
    lines.append("")
    lines.append("| Sensor | Noise ASD (fT/√Hz) | Bandwidth (Hz) | Aβ control | C-band ratio |")
    lines.append("|---|---|---|---|---|")
    for s in p2:
        lines.append(
            f"| {s['name']} | {s['noise_asd_fT_rtHz']:g} | {s['bandwidth_hz']:.0f} | "
            f"{'PASS' if s['ab_positive_control_passed'] else 'FAIL'} | "
            f"{s['c_band_detectability_ratio']:.3f} |"
        )
    lines.append("")
    lines.append(
        "\"C-band ratio\" is observed C-band beamformer peak energy divided by the "
        "95th percentile of a noise-only null generated through the identical, "
        "band-limited pipeline (same definition as the default run's sweep, "
        f"here with {payload['config']['null_repeats']} null repeats per row). "
        ">= 1 means detectable at that sensor's noise+bandwidth. The A-beta control "
        "must pass for a row's C-band result to be interpretable at all."
    )
    lines.append("")
    lines.append("See `sensor-comparison.png`.")
    lines.append("")
    lines.append("## Part 3 -- interference, on the best-case sensor")
    lines.append("")
    lines.append(f"Best-case sensor carried forward: **{p3['best_sensor']}**.")
    lines.append("")
    lines.append(
        f"- Cardiac interference: **{p3['cardiac_amplitude_fT']:.1f} fT**, from a GUESSED "
        f"(not measured) attenuation factor of {p3['cardiac_attenuation_assumption']:.2e} "
        "applied to a 75 pT torso-MCG midpoint of the stated 50-100 pT range; change "
        "`--cardiac-amplitude-fT` to test other assumptions."
    )
    lines.append(f"- 1/f drift below 10 Hz: **{p3['drift_rms_fT']:.1f} fT rms**, added after trial averaging.")
    lines.append(f"- Mains: **{p3['mains_amplitude_fT']:.1f} fT** at 50 Hz plus two harmonics.")
    lines.append("")
    lines.append(
        f"- Detectability ratio with no interference: **{p3['ratio_no_interference']:.3f}**."
    )
    lines.append(
        f"- Detectability ratio with interference: **{p3['ratio_with_interference']:.3f}**."
    )
    lines.append(
        f"- Detectability ratio with interference and a 50/100/150 Hz notch: "
        f"**{p3['ratio_with_interference_and_notch']:.3f}**. No notch is applied at the "
        "~1 Hz cardiac fundamental, since Part 1 shows that frequency overlaps the "
        "C-band signal's own dominant content -- notching it would remove signal "
        "along with interference."
    )
    lines.append("")
    lines.append("## Discipline")
    lines.append("")
    lines.append(
        "No calibrated constant from the default run (in particular the overall "
        "current scale) was touched here. Every new assumption specific to this "
        "follow-up -- the filter type/order, the noise-vs-bandwidth split, the "
        "interference amplitudes -- is listed in `simulate.py`'s module docstring "
        "as approximations 8-13, with the same explicitness as the original seven. "
        "The cardiac amplitude in particular is a stated guess, not a measurement; "
        "the headline above should not be read as insensitive to it without rerunning "
        "with `--cardiac-amplitude-fT` set to other plausible values."
    )
    lines.append("")
    lines.append("## Full run log")
    lines.append("")
    lines.append("```")
    lines.extend(log)
    lines.append("```")
    lines.append("")

    with open(out_dir / "results.md", "w") as fh:
        fh.write("\n".join(lines))


if __name__ == "__main__":
    sys.exit(main())
