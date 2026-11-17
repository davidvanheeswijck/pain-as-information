"""Search space, Latin-hypercube sampling, calibration score and target test for S-1b.

Everything here is fixed by PREDICTION.md (commit #1); this module holds no
NEURON code so it can be unit-tested without the simulator.  The score J and the
target test use the calibration targets only (Sundt 2015 following frequencies;
Chao 2020 progressive block at regular 20 Hz, 1.5x).  No P1 or P2 quantity enters.
"""

import math

import numpy as np

# name, low, high, scale  (PREDICTION.md, "Tuning search space")
SPACE = [
    ("nav", 0.034, 0.043, "lin"),
    ("nav_soma", 0.008, 0.040, "lin"),
    ("kv", 0.030, 0.055, "lin"),
    ("kcnq", 0.0003, 0.004, "log"),
    ("gsk", 0.0005, 0.060, "log"),
    ("gcal", 0.00005, 0.0020, "log"),
    ("sk_tau", 300.0, 20000.0, "log"),
    ("diam_stem", 1.2, 1.6, "lin"),
]
N1, N2, N_CENTRES = 240, 96, 3
SEED_LHS, SEED_COIN, SEED_R2 = 20261117, 20261118, 20261119

TARGET_HZ = {"na_k": 110.0, "kcnq": 30.0, "sk": 6.0}
BAND = 0.25                      # +/-25%
B1_MAX_F_EARLY = 0.50            # first 5 s window
B2_MIN_F_LATE = 0.80             # last 10 s window
B3_ONSET_S = (2.0, 20.0)         # block onset after stimulation starts
STIM_START_MS = 200.0            # protocol.T0_MS
SK_ACCEPT_RANGE = (2.0, 40.0)    # run the calibration run when the SK-configuration ff is in here
D_CAP = 10.0


def band(target):
    return (target * (1 - BAND), target * (1 + BAND))


def in_band(name, ff):
    lo, hi = band(TARGET_HZ[name])
    return bool(ff is not None and lo <= ff <= hi)


def lhs_unit(n, d, rng):
    """n x d Latin hypercube on [0,1): one point per stratum in every dimension."""
    perm = rng.permuted(np.tile(np.arange(n), (d, 1)), axis=1).T
    return (perm + rng.random((n, d))) / n


def _to_scale(x, scale):
    return math.log(x) if scale == "log" else x


def _from_scale(y, scale):
    return math.exp(y) if scale == "log" else y


def point(u_row, space=SPACE, box=None):
    """Map a unit-cube row to a parameter dict.  box: {name: (lo, hi)} narrows the range."""
    p = {}
    for u, (name, lo, hi, sc) in zip(u_row, space):
        if box and name in box:
            lo, hi = box[name]
        a, b = _to_scale(lo, sc), _to_scale(hi, sc)
        p[name] = float(_from_scale(a + float(u) * (b - a), sc))
    return p


def round1_candidates(n=N1):
    rng = np.random.default_rng(SEED_LHS)
    u = lhs_unit(n, len(SPACE), rng)
    coin = np.random.default_rng(SEED_COIN).random(n) < 0.5
    out = []
    for i in range(n):
        p = point(u[i])
        p["sk_stem"] = bool(coin[i])
        out.append(p)
    return out


def local_box(centre, frac=0.15, space=SPACE):
    """+/-frac of each parameter's range on its own scale, clipped to the global range."""
    box = {}
    for name, lo, hi, sc in space:
        a, b = _to_scale(lo, sc), _to_scale(hi, sc)
        c = _to_scale(centre[name], sc)
        hw = frac * (b - a)
        box[name] = (_from_scale(max(a, c - hw), sc), _from_scale(min(b, c + hw), sc))
    return box


def round2_candidates(centres, n_per=None):
    """n_per local hypercube points around each centre (sk_stem fixed to the centre's)."""
    n_per = n_per or N2 // N_CENTRES
    out = []
    for ci, c in enumerate(centres):
        rng = np.random.default_rng(SEED_R2 + ci)
        u = lhs_unit(n_per, len(SPACE), rng)
        box = local_box(c)
        for i in range(n_per):
            p = point(u[i], box=box)
            p["sk_stem"] = bool(c["sk_stem"])
            out.append(p)
    return out


def d_term(ff, target):
    """Normalised log deviation: 1.0 at a band edge; capped; ff <= 0 gets the cap."""
    if ff is None or not ff > 0:
        return D_CAP
    return float(max(-D_CAP, min(D_CAP, math.log(ff / target) / math.log(1 + BAND))))


def block_flags(res):
    """B1, B2, B3 from a regular 20 Hz, 1.5x run result (protocol.score output).
    Returns dict(B1, B2, B3, onset_s, e1, e2, e3)."""
    fe, fl, tb = res.get("F_early"), res.get("F_late"), res.get("t_block_ms")
    b1 = bool(fe is not None and fe <= B1_MAX_F_EARLY)
    b2 = bool(fl is not None and fl >= B2_MIN_F_LATE)
    onset = None if tb is None else (tb - STIM_START_MS) / 1000.0
    b3 = bool(onset is not None and B3_ONSET_S[0] <= onset <= B3_ONSET_S[1])
    e1 = 1.0 if fe is None else max(0.0, fe - B1_MAX_F_EARLY) / B1_MAX_F_EARLY
    e2 = 1.0 if fl is None else max(0.0, B2_MIN_F_LATE - fl) / B2_MIN_F_LATE
    e3 = 0.0 if b3 else 1.0
    return dict(B1=b1, B2=b2, B3=b3, onset_s=onset, e1=e1, e2=e2, e3=e3)


def score_J(ffs, flags):
    """Calibration score (lower is better): three Sundt terms plus block shortfall.
    ffs = dict(na_k, kcnq, sk).  Uses calibration targets only."""
    d = {n: d_term(ffs.get(n), TARGET_HZ[n]) for n in TARGET_HZ}
    J = sum(v * v for v in d.values()) + flags["e1"] ** 2 + flags["e2"] ** 2 + flags["e3"] ** 2
    return float(J), d


def meets_targets(ffs, flags):
    return bool(all(in_band(n, ffs.get(n)) for n in TARGET_HZ) and flags["B1"] and flags["B2"] and flags["B3"])
