"""S-2b protocol: input generators, conditions, scoring, control criteria and statistics helpers.
No NEURON import: pure numpy, so it can be tested and imported by the aggregator.

All definitions are those of PREDICTION.md in this directory.  The S-2 port (dh_model.py) and the
S-2 helpers that carry no S-2 design constants are reused by import from ../S-002-dorsal-horn; that
directory is not edited.
"""

import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
S2_DIR = os.path.join(os.path.dirname(HERE), "S-002-dorsal-horn")
if S2_DIR not in sys.path:
    sys.path.append(S2_DIR)   # appended: this directory's modules win any name clash

import s2_protocol as base  # noqa: E402  (reused: rng_for, poisson_train, merge_trains, wilson, ...)

DATA = base.DATA

# --- run and scoring (PREDICTION.md, "Operational definitions") ----------------------
T_RUN = 5500.0            # ms
T_SCORE0, T_SCORE1 = 1500.0, 5500.0
DT_MAIN = 0.025
DT_PUB = 0.0125
SHIFTS = (0, 2.5, 5, 7.5, 10, 15, 20, 30)          # mV
SEEDS = (1, 2)
RC_GRID = tuple(round(0.5 + 0.125 * i, 3) for i in range(17))   # Hz per C fibre, 0.5 .. 2.5
RC_BAND = (2.0, 15.0)     # Hz, WDR rate with C only
TOUCH_HZ = 9.0            # Hz per Abeta fibre; the shipped Foreman SCS file's Abeta background (8.96)
SCS_PRIMARY_HZ = 40
CONTROL_FREQS = (5, 10, 20, 30, 40, 60, 100, 150, 200)
SWEEP_FREQS = (5, 10, 20, 40, 80, 160)
SWEEP_SHIFTS = (0, 5, 10, 15, 30)
DELTA_REF = 5
DELTA_PROG = 15
ONSET_RISE = 2.0          # Hz above R_T(0)
RED_THRESHOLD = 0.20
MIN_DEFINED_RATE = 0.5
ONSET_NONE_VALUE = 45.0
P0_ONSET_LIMIT = 10.0     # mV
N_ENSEMBLE = 200
MAX_CANDIDATES = 1500
N_SUBSAMPLE = 40
N_VALID = 60              # networks (first accepted) that get the held-out frequency feature
F_SEEDS = (1, 2, 3, 4)
N_CONVERGE = 10
BOOT_N = 10000
BASE_SEED = 20261119

if os.environ.get("S2B_PILOT"):
    # PILOT ONLY (set by `simulate_s002b.py --pilot`): a smaller protocol so the whole pipeline can be
    # exercised in minutes.  Nothing from a pilot is a result; pilots write results/pilot/ only.
    T_RUN, T_SCORE0, T_SCORE1 = 3000.0, 1000.0, 3000.0
    SHIFTS = (0, 5, 15, 20)
    SEEDS = (1,)
    F_SEEDS = (1,)
    SWEEP_SHIFTS = (0, 5, 15)
    SWEEP_FREQS = (10, 40, 160)

# control criteria
W_RATIO = 1.5
W_DIFF = 1.0
A_MIN_WITHOUT = 1.0
A_RATIO = 0.80
F_BASE_MIN = 1.0
F_INHIB = 0.80
F_EXCITE = 1.10
A_TSTOP = 21000.0         # first 10 cycles of the shipped A-fibre-inhibition input

ABETA = base.ABETA
ADELTA = base.ADELTA
SURROUND = tuple(range(30, 45))
CFIB = base.CFIB

CONDITIONS = {   # name: (touch, C level, scs)
    "C1": (False, 1.0, False),
    "Ch": (False, 0.5, False),
    "CS": (False, 1.0, True),
    "T": (True, 0.0, False),
    "TS": (True, 0.0, True),
    "TC": (True, 1.0, False),
    "TCh": (True, 0.5, False),
    "TCS": (True, 1.0, True),
}
MAIN_CONDITIONS = ("C1", "Ch", "T", "TC", "TCh", "TS")
VARIANTS = ("norm", "H", "D1", "D2")
H_PASS_PROB = 0.5
D1_FIBRES = 5

# --- input generators ------------------------------------------------------------------------


def rng_for(net, seed, stream, fibre=0):
    """Deterministic generator: the same (net, seed, stream, fibre) gives the same numbers in
    every condition and at every shift, so comparisons are paired.  Own base seed."""
    return np.random.default_rng([BASE_SEED, int(net), int(seed), int(stream), int(fibre)])


def poisson_train(rng, rate_hz, t_end=T_RUN):
    return base.poisson_train(rng, rate_hz, t_end)


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


def touch_trains(net, seed, rate_hz=TOUCH_HZ):
    return {f: poisson_train(rng_for(net, seed, 2, f), rate_hz) for f in ABETA}


def scs_times(freq_hz, t_end=T_RUN):
    """Regular pulses, first at 1/f."""
    step = 1000.0 / freq_hz
    return np.arange(1, int(t_end // step) + 1) * step


def scs_trains(freq_hz, variant, net, seed):
    """Fibre -> pulse times for the stimulus, on the SURROUND input (fibres 30 to 44), by variant."""
    pulses = scs_times(freq_hz)
    out = {}
    if variant == "norm":
        for f in SURROUND:
            out[f] = pulses
    elif variant == "H":
        for f in SURROUND:
            keep = rng_for(net, seed, 3, f).uniform(size=len(pulses)) < H_PASS_PROB
            out[f] = pulses[keep]
    elif variant == "D1":
        for f in SURROUND[:D1_FIBRES]:
            out[f] = pulses
    elif variant == "D2":
        for f in SURROUND + ADELTA:
            out[f] = pulses
    else:
        raise ValueError(variant)
    return out


def merge_trains(*trainsets):
    return base.merge_trains(*trainsets)


def build_fibre_trains(cond, net, seed, rC, freq=SCS_PRIMARY_HZ, variant="norm", touch_hz=TOUCH_HZ):
    touch, clevel, scs = CONDITIONS[cond]
    sets = []
    if clevel > 0:
        sets.append(c_trains(net, seed, rC, clevel))
    if touch:
        sets.append(touch_trains(net, seed, touch_hz))
    if scs:
        sets.append(scs_trains(freq, variant, net, seed))
    return merge_trains(*sets)


def rate_in_window(spikes, t0=T_SCORE0, t1=T_SCORE1):
    s = np.asarray(spikes)
    return float(np.sum((s >= t0) & (s < t1))) / ((t1 - t0) / 1000.0)


# --- shipped inputs, by fibre class (read as data) ----------------------------------------------

def afib_events(model, keep_abeta, keep_adelta):
    """Shipped A-fibre-inhibition events for the first 10 cycles, as row -> times.  Surround and C
    fibres are always kept (the shipped surround events are dummy times at 1e9 ms and are dropped by
    the run window); Abeta (fibres 0-14) and Adelta (15-29) are kept as asked."""
    rows, _ = base.read_shipped_inputs("afib")
    aff = set(int(r) for r in model.afferent_rows)
    ev = {}
    for k, v in rows.items():
        if k not in aff:
            continue
        fibre = int(model.table.frm[k])
        if fibre in ABETA and not keep_abeta:
            continue
        if fibre in ADELTA and not keep_adelta:
            continue
        ev[k] = v
    return ev


A_CONDITIONS = {   # name: (keep Abeta, keep Adelta)
    "C_only": (False, False),
    "C_abeta": (True, False),
    "C_adelta": (False, True),
    "C_all_A": (True, True),
}

windup_counts = base.windup_counts
judge_windup = base.judge_windup


def afib_counts(wdr_spikes, n_cycles=10):
    return base.afib_counts(wdr_spikes, n_cycles)


def judge_afib_beta(c_only, c_abeta, c_adelta=None, c_all=None):
    """Calibration feature A: criterion on the Abeta-only condition.  The Adelta-only and all-A
    conditions are registered next to it and are not part of the criterion."""
    m0, mb = float(np.mean(c_only)), float(np.mean(c_abeta))
    ok = bool(m0 >= A_MIN_WITHOUT and mb <= A_RATIO * m0)
    out = dict(ok=ok, C_only=m0, C_abeta=mb, ratio_abeta=(mb / m0 if m0 > 0 else None))
    if c_adelta is not None:
        md = float(np.mean(c_adelta))
        out.update(C_adelta=md, ratio_adelta=(md / m0 if m0 > 0 else None))
    if c_all is not None:
        ma = float(np.mean(c_all))
        out.update(C_all_A=ma, ratio_all=(ma / m0 if m0 > 0 else None))
    return out


def judge_frequency(base_rate, rates_by_freq):
    """Held-out validation feature F.  `rates_by_freq`: {freq: mean rate}; rho = rate / base_rate
    with base_rate the touch-plus-C rate without stimulation."""
    if base_rate < F_BASE_MIN:
        return dict(ok=False, evaluable=False, base=base_rate, rho={}, reason="baseline below minimum")
    rho = {int(f): r / base_rate for f, r in rates_by_freq.items()}
    band = [rho[f] for f in (30, 40, 60, 100)]
    out_inh = [rho[f] for f in (5, 10, 20, 150, 200)]
    i = min(band) <= F_INHIB and min(band) < min(out_inh)
    ii = max(rho[f] for f in (5, 10, 20)) >= F_EXCITE
    iii = max(rho[f] for f in (150, 200)) >= F_EXCITE
    return dict(ok=bool(i and ii and iii), evaluable=True, base=base_rate, rho=rho,
                inhibited_in_band=bool(i), excited_below_30=bool(ii), excited_above_100=bool(iii))


# --- ensemble sampling ---------------------------------------------------------------------------

def sample_factors(idx, group_names, weight_range, cond_ranges):
    """Independent log-uniform factors for candidate idx (candidate 0: all 1); own seed."""
    if idx == 0:
        return {g: 1.0 for g in group_names}, {c: 1.0 for c in cond_ranges}
    rng = np.random.default_rng(BASE_SEED + idx)
    w = {g: float(math.exp(rng.uniform(math.log(weight_range[0]), math.log(weight_range[1])))) for g in group_names}
    c = {k: float(math.exp(rng.uniform(math.log(lo), math.log(hi)))) for k, (lo, hi) in cond_ranges.items()}
    return w, c


# --- C-drive matching -------------------------------------------------------------------------------

def match_rc(rate_at):
    """Smallest grid index whose mean C-only WDR rate is >= RC_BAND[0], found by bisection (the
    rate is monotone in the drive up to noise); accepted iff that rate is also <= RC_BAND[1].
    `rate_at(i)` -> mean rate at RC_GRID[i].  Returns (rC or None, rate, tried dict, reason)."""
    tried = {}

    def r(i):
        if i not in tried:
            tried[i] = rate_at(i)
        return tried[i]

    lo, hi = 0, len(RC_GRID) - 1
    if r(hi) < RC_BAND[0]:
        return None, None, {RC_GRID[i]: v for i, v in tried.items()}, "unreachable: top of grid below band"
    while lo < hi:
        mid = (lo + hi) // 2
        if r(mid) >= RC_BAND[0]:
            hi = mid
        else:
            lo = mid + 1
    rate = r(lo)
    tr = {RC_GRID[i]: v for i, v in tried.items()}
    if rate > RC_BAND[1]:
        return None, rate, tr, "jumped over the band"
    return RC_GRID[lo], rate, tr, "ok"


# --- statistics (reused) -------------------------------------------------------------------------------

wilson = base.wilson
boot_indices = base.boot_indices
ratio_reduction_ci = base.ratio_reduction_ci
median_ci = base.median_ci


def onset_shift(r_t_by_shift, shifts=SHIFTS):
    """First grid shift > 0 with R_T >= R_T(0) + ONSET_RISE, else None."""
    b = r_t_by_shift[0]
    for s, r in zip(shifts, r_t_by_shift):
        if s > 0 and r >= b + ONSET_RISE:
            return s
    return None
