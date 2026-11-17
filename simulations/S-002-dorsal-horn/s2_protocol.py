"""S-2 protocol: input generators, conditions, scoring, control criteria and verdict
helpers.  No NEURON import: everything here is pure numpy so it can be tested and
imported by the aggregator.

All definitions are those of PREDICTION.md (commit 007f633); where this file needs a
number that file fixes, the constant is named and annotated with the section.
"""

import math
import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

# --- run and scoring (PREDICTION.md, "Operational definitions") -------------------
T_RUN = 7500.0            # ms
T_SCORE0, T_SCORE1 = 1500.0, 7500.0
DT_MAIN = 0.025
DT_PUB = 0.0125
SHIFTS = (0, 5, 10, 15, 20, 25, 30, 40)
SEEDS = (1, 2, 3)
RC_SET = (2.5, 5.0, 10.0, 20.0)       # Hz per C fibre
RC_BAND = (2.0, 15.0)                 # Hz, WDR rate with C only
RT_SET = (10.0, 20.0, 40.0, 80.0)     # Hz per Abeta fibre
RT_MIN_RATE = 0.5                     # Hz, touch only, C off
CONTROL_FREQS = (5, 10, 20, 30, 40, 60, 100, 150, 200)
SWEEP_FREQS = (5, 10, 20, 40, 80, 160)
SWEEP_SHIFTS = (0, 10, 15, 20, 25, 40)
DELTA_REF = 15
DELTA_PROG = 25
SCS_PRIMARY_HZ = 20
ONSET_RISE = 1.0                      # Hz above R_T(0)
RED_THRESHOLD = 0.20
MIN_DEFINED_RATE = 0.5                # Hz, mean rate needed for a reduction to be defined
ONSET_NONE_VALUE = 45.0               # mV, "none" counted as above the grid
N_ENSEMBLE = 200
MAX_CANDIDATES = 1500
N_SUBSAMPLE = 40
N_CONVERGE = 10
BOOT_N = 10000
BASE_SEED = 20261118

CONDITIONS = {   # name: (touch, C level, scs)
    "C1": (False, 1.0, False),
    "Ch": (False, 0.5, False),
    "CS": (False, 1.0, True),
    "T": (True, 0.0, False),
    "S": (False, 0.0, True),
    "TS": (True, 0.0, True),
    "TC": (True, 1.0, False),
    "TCh": (True, 0.5, False),
    "TCS": (True, 1.0, True),
}
VARIANTS = ("norm", "H", "D1", "D2")
H_PASS_PROB = 0.5
D1_FIBRES = 5

ABETA = tuple(range(0, 15))
ADELTA = tuple(range(15, 30))
CFIB = tuple(range(45, 75))

if os.environ.get("S2_PILOT"):
    # PILOT ONLY (set by `simulate_s002.py --pilot`): a much smaller grid so the whole pipeline can be
    # exercised in minutes.  Nothing from a pilot is a result; pilots write results/pilot/ only.
    T_RUN, T_SCORE0, T_SCORE1 = 3500.0, 1000.0, 3500.0
    SHIFTS = (0, 15, 25)
    SEEDS = (1,)
    SWEEP_SHIFTS = (0, 15, 25)
    SWEEP_FREQS = (10, 20, 40)
    RT_SET = (20.0, 80.0)

# control criteria (PREDICTION.md, "The positive control")
W_RATIO = 1.5
W_DIFF = 1.0
A_MIN_WITHOUT = 1.0
A_RATIO = 0.80
F_INHIB = 0.80
F_EXCITE = 1.10


# --- input generators ---------------------------------------------------------------

def rng_for(net, seed, stream, fibre=0):
    """Deterministic generator: the same (net, seed, stream, fibre) gives the same numbers in
    every condition and at every shift, so comparisons are paired."""
    return np.random.default_rng([BASE_SEED, int(net), int(seed), int(stream), int(fibre)])


def poisson_train(rng, rate_hz, t_end=T_RUN):
    """Poisson spike times (ms) on [0, t_end)."""
    if rate_hz <= 0:
        return np.array([])
    n = rng.poisson(rate_hz * t_end / 1000.0)
    return np.sort(rng.uniform(0.0, t_end, n))


def c_trains(net, seed, rate_hz, level):
    """30 C fibres.  `level` 1: the full trains; 0.5: the same trains thinned by independent
    probability 0.5; 0: none."""
    out = {}
    if level <= 0:
        return out
    for f in CFIB:
        t = poisson_train(rng_for(net, seed, 0, f), rate_hz)
        if level < 1.0:
            keep = rng_for(net, seed, 1, f).uniform(size=len(t)) < level
            t = t[keep]
        out[f] = t
    return out


def touch_trains(net, seed, rate_hz):
    return {f: poisson_train(rng_for(net, seed, 2, f), rate_hz) for f in ABETA}


def scs_times(freq_hz, t_end=T_RUN):
    """Regular pulses, first at 1/f."""
    step = 1000.0 / freq_hz
    return np.arange(1, int(t_end // step) + 1) * step


def scs_trains(freq_hz, variant, net, seed):
    """Fibre -> pulse times for the stimulus, by variant (PREDICTION.md, P3)."""
    base = scs_times(freq_hz)
    out = {}
    if variant == "norm":
        for f in ABETA:
            out[f] = base
    elif variant == "H":
        for f in ABETA:
            keep = rng_for(net, seed, 3, f).uniform(size=len(base)) < H_PASS_PROB
            out[f] = base[keep]
    elif variant == "D1":
        for f in ABETA[:D1_FIBRES]:
            out[f] = base
    elif variant == "D2":
        for f in ABETA + ADELTA:
            out[f] = base
    else:
        raise ValueError(variant)
    return out


def merge_trains(*trainsets):
    """Union of the trains of each fibre (no collision, no refractoriness; declared)."""
    out = {}
    for ts in trainsets:
        for f, t in ts.items():
            out[f] = t if f not in out else np.union1d(out[f], t)
    return out


def build_fibre_trains(cond, net, seed, rC, rT, freq=SCS_PRIMARY_HZ, variant="norm"):
    touch, clevel, scs = CONDITIONS[cond]
    sets = []
    if clevel > 0:
        sets.append(c_trains(net, seed, rC, clevel))
    if touch:
        sets.append(touch_trains(net, seed, rT))
    if scs:
        sets.append(scs_trains(freq, variant, net, seed))
    return merge_trains(*sets)


def rate_in_window(spikes, t0=T_SCORE0, t1=T_SCORE1):
    spikes = np.asarray(spikes)
    return float(np.sum((spikes >= t0) & (spikes < t1))) / ((t1 - t0) / 1000.0)


# --- shipped input files (read as data) --------------------------------------------

def read_shipped_inputs(prefix):
    """(per-row spike times dict for rows 0..224, tstop_ms) from the shipped files.  Format:
    SpikeStatsVector.txt = n, n counts, tstop; SpikeTimesVector.txt = each vector's times
    followed by a -1e15 sentinel (the `scantil` format)."""
    with open(os.path.join(DATA, f"{prefix}_SpikeStatsVector.txt")) as fh:
        stats = [float(x) for x in fh.read().split()]
    n = int(stats[0])
    counts = [int(c) for c in stats[1:1 + n]]
    tstop = stats[1 + n]
    with open(os.path.join(DATA, f"{prefix}_SpikeTimesVector.txt")) as fh:
        times = [float(x) for x in fh.read().split()]
    vecs, cur = [], []
    for x in times:
        if x <= -1e14:
            vecs.append(np.array(cur))
            cur = []
        else:
            cur.append(x)
    if cur:
        vecs.append(np.array(cur))
    assert len(vecs) == n and all(len(v) == c for v, c in zip(vecs, counts)), "shipped spike file does not parse"
    return {k: vecs[k] for k in range(n)}, tstop


# --- control criteria ---------------------------------------------------------------

def windup_counts(wdr_spikes, n_stim=20):
    """WDR spikes in [1000k, 1000k + 1000) ms, k = 1..n_stim."""
    s = np.asarray(wdr_spikes)
    return np.array([np.sum((s >= 1000.0 * k) & (s < 1000.0 * k + 1000.0)) for k in range(1, n_stim + 1)], float)


def judge_windup(counts):
    early = float(np.mean(counts[0:5]))
    late = float(np.mean(counts[15:20]))
    ok = bool(late >= W_RATIO * early and (late - early) >= W_DIFF)
    return dict(early=early, late=late, ok=ok)


def afib_counts(wdr_spikes, n_cycles=10):
    """WDR spikes per cycle in [1000 + 2000k, 3000 + 2000k) ms, k = 0..n_cycles-1."""
    s = np.asarray(wdr_spikes)
    return np.array([np.sum((s >= 1000.0 + 2000.0 * k) & (s < 3000.0 + 2000.0 * k)) for k in range(n_cycles)], float)


def judge_afib(with_a, without_a):
    m_with, m_without = float(np.mean(with_a)), float(np.mean(without_a))
    ok = bool(m_without >= A_MIN_WITHOUT and m_with <= A_RATIO * m_without)
    return dict(with_A=m_with, without_A=m_without, ok=ok)


def judge_frequency(base_rate, rates_by_freq):
    """`rates_by_freq`: {freq: mean rate}.  rho = rate / base_rate.  (PREDICTION.md, F)."""
    if not (RC_BAND[0] <= base_rate <= RC_BAND[1]):
        return dict(ok=False, base=base_rate, rho={}, reason="baseline outside band")
    rho = {int(f): r / base_rate for f, r in rates_by_freq.items()}
    band = [rho[f] for f in (30, 40, 60, 100)]
    out_inh = [rho[f] for f in (5, 10, 20, 150, 200)]
    i = min(band) <= F_INHIB and min(band) < min(out_inh)
    ii = max(rho[f] for f in (5, 10, 20)) >= F_EXCITE
    iii = max(rho[f] for f in (150, 200)) >= F_EXCITE
    return dict(ok=bool(i and ii and iii), base=base_rate, rho=rho, inhibited_in_band=bool(i),
                excited_below_30=bool(ii), excited_above_100=bool(iii))


# --- ensemble sampling -----------------------------------------------------------------

def sample_factors(idx, group_names, weight_range, cond_ranges):
    """Independent log-uniform factors for candidate idx (candidate 0: all 1)."""
    if idx == 0:
        return {g: 1.0 for g in group_names}, {c: 1.0 for c in cond_ranges}
    rng = np.random.default_rng(20261118 + idx)
    w = {g: float(math.exp(rng.uniform(math.log(weight_range[0]), math.log(weight_range[1])))) for g in group_names}
    c = {k: float(math.exp(rng.uniform(math.log(lo), math.log(hi)))) for k, (lo, hi) in cond_ranges.items()}
    return w, c


# --- statistics ---------------------------------------------------------------------------

def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return (0.0, 1.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def boot_indices(n, nboot=BOOT_N, seed=0):
    return np.random.default_rng(seed).integers(0, n, size=(nboot, n))


def ratio_reduction_ci(num, den, idx):
    """1 - mean(num)/mean(den) over networks, point and bootstrap percentile 95% CI using the
    shared resample indices `idx`.  `den` mean must be > 0 in each resample or that resample is
    dropped."""
    num, den = np.asarray(num, float), np.asarray(den, float)
    pt = 1.0 - num.mean() / den.mean() if den.mean() > 0 else float("nan")
    dm = den[idx].mean(axis=1)
    nm = num[idx].mean(axis=1)
    ok = dm > 0
    r = 1.0 - nm[ok] / dm[ok]
    if len(r) < 0.9 * len(idx):
        return pt, float("nan"), float("nan")
    return pt, float(np.percentile(r, 2.5)), float(np.percentile(r, 97.5))


def median_ci(values, idx):
    v = np.asarray(values, float)
    meds = np.median(v[idx], axis=1)
    return float(np.median(v)), float(np.percentile(meds, 2.5)), float(np.percentile(meds, 97.5))


def onset_shift(r_t_by_shift, shifts=SHIFTS):
    """First grid shift with R_T >= R_T(0) + ONSET_RISE, else None.  `r_t_by_shift`: list aligned
    with `shifts`."""
    base = r_t_by_shift[0]
    for s, r in zip(shifts, r_t_by_shift):
        if s > 0 and r >= base + ONSET_RISE:
            return s
    return None
