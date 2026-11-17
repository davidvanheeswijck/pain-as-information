"""Stimulation patterns, thresholds and the filtering index F for S-1."""

import numpy as np

import engine

T_STIM_MS = 30000.0
T0_MS = 200.0           # stimulation starts here
TEST_T0_MS = 300.0      # test spikes start here (stimulation starts at T0_MS)
DEAD_MS = 2.0
PATTERN_RATE = 20.0


def regular(rate, T=T_STIM_MS):
    n = int(round(rate * T / 1000.0))
    return T0_MS + (1000.0 / rate) * np.arange(n)


def n_matched(T):
    return int(round(PATTERN_RATE * T / 1000.0))


def poisson(rng, T=T_STIM_MS):
    """Dead time + exponential intervals, excess rescaled so n pulses span T exactly."""
    n = n_matched(T)
    mean = T / n
    iv = rng.exponential(mean - DEAD_MS, n)
    iv = iv * ((T - DEAD_MS * n) / iv.sum())
    return T0_MS + np.cumsum(iv + DEAD_MS) - (iv[0] + DEAD_MS)


def burst(T=T_STIM_MS):
    """5 pulses at 100 Hz every 250 ms (20 Hz mean)."""
    nb = n_matched(T) // 5
    t = (250.0 * np.arange(nb))[:, None] + 10.0 * np.arange(5)[None, :]
    return T0_MS + t.ravel()


def jitter(rng, T=T_STIM_MS, lo=2.0, hi=50.0):
    """Instantaneous rate uniform on [lo, hi] Hz per pulse; one common factor so n pulses span T."""
    n = n_matched(T)
    r = rng.uniform(lo, hi, n)
    iv = 1000.0 / r
    iv = iv * (T / iv.sum())
    assert iv.min() >= DEAD_MS + 1.0, "jitter interval too short"
    return T0_MS + np.cumsum(iv) - iv[0]


def test_times(seed, rate, T=T_STIM_MS):
    """Test spikes with mean rate `rate` Hz, each jittered +/-30% of the period around
    its nominal slot so that they sample every phase of the stimulus train.  Same seed
    gives the same test times in every condition for a given model."""
    rng = np.random.default_rng(seed)
    per = 1000.0 / rate
    n = int((T - 500.0) // per)
    return TEST_T0_MS + per * np.arange(n) + rng.uniform(-0.3, 0.3, n) * per + 0.3 * per


def make_pattern(name, seed, T=T_STIM_MS):
    rng = np.random.default_rng(seed)
    if name.startswith("reg"):
        return regular(float(name[3:]), T)
    if name == "poisson":
        return poisson(rng, T)
    if name == "burst":
        return burst(T)
    if name == "jitter":
        return jitter(rng, T)
    raise ValueError(name)


def stim_threshold(cell_factory, dt=0.025, rel=0.01):
    """Smallest 1 ms mid-stem pulse (nA) from rest that fires a spike crossing stem_pre
    (bisection to `rel`)."""
    def fires(a):
        rig = engine.Rig(cell_factory(), dt)
        out = rig.run([20.0], a, [], 80.0)
        return len(out["stem_pre"]) >= 1

    lo, hi = 0.0, 0.05
    while not fires(hi):
        lo, hi = hi, hi * 2
        if hi > 20:
            return None
    while (hi - lo) > rel * hi:
        mid = 0.5 * (lo + hi)
        if fires(mid):
            hi = mid
        else:
            lo = mid
    return hi


def score(out, test_t, lat, T_end):
    """Filtering index F over isolated test spikes.

    For test k launched at tk: arrival te = first peri_pre crossing in
    [tk+0.6*l1, tk+1.6*l1+2]; none => collided or lost en route, excluded.  The spike
    is *ambiguous* if a stimulus-evoked spike crossed stem_pre in the interval that
    could produce a central crossing inside the success window; ambiguous spikes are
    excluded (a stimulus spike entering the central axon would otherwise be
    mistaken for the test spike).  Otherwise success iff a central crossing occurs in
    [te+0.4*d0, te+2.5*d0+2].  F_all ignores the ambiguity exclusion (success if any
    central crossing in the window), a lower bound on F.
    """
    pp, st, ce = out["peri_pre"], out["stem_pre"], out["central"]
    l1, d0 = lat["l1"], lat["d0"]
    rows = []  # (tk, arrived, scored, success, success_any)
    for tk in test_t:
        te = engine.first_in(pp, tk + 0.6 * l1, tk + 1.6 * l1 + 2.0)
        if np.isnan(te):
            rows.append((tk, 0, 0, 0, 0))
            continue
        cw = (te + 0.4 * d0, te + 2.5 * d0 + 2.0)
        any_ok = int(not np.isnan(engine.first_in(ce, *cw)))
        zlo, zhi = te - 0.6 * d0 - 1.0, te + 1.5 * d0 + 3.2
        # A stimulus-evoked stem crossing inside [zlo, zhi] could be mistaken for the
        # test spike at the central site.  A successful test spike also backfires into
        # the stem, crossing stem_pre within ~one conduction step after te; that window
        # (te, te+ign) is ignored so that successes do not mark themselves ambiguous.
        ign = 0.5 * d0 + 0.5
        amb = (not np.isnan(engine.first_in(st, zlo, te))) or (
            not np.isnan(engine.first_in(st, te + ign, zhi)))
        rows.append((tk, 1, 0 if amb else 1, any_ok if not amb else 0, any_ok))
    r = np.array(rows, dtype=float)
    arrived = r[:, 1] == 1
    scored = r[:, 2] == 1
    res = dict(
        n_test=int(len(test_t)), n_arrived=int(arrived.sum()), n_scored=int(scored.sum()),
        n_soma_spikes=int(len(out["soma"])), n_evoked=int(len(out["stem_pre"])),
    )
    if scored.sum() > 0:
        res["F"] = float(1.0 - r[scored, 3].mean())
    else:
        res["F"] = float("nan")
    res["F_all"] = float(1.0 - r[arrived, 4].mean()) if arrived.sum() else float("nan")
    # early / late windows (scored spikes only)
    tk = r[:, 0]
    for name, lo, hi in (("F_early", 0, 5000 + TEST_T0_MS), ("F_late", T_end - 10000, T_end + 1)):
        m = scored & (tk >= lo) & (tk < hi)
        res[name] = float(1.0 - r[m, 3].mean()) if m.sum() >= 3 else float("nan")
    # time-to-block: onset of the first run of 5 consecutive failed scored test spikes
    fails = (r[scored, 3] == 0)
    times = tk[scored]
    tb = None
    run = 0
    for i, f in enumerate(fails):
        run = run + 1 if f else 0
        if run == 5:
            tb = float(times[i - 4])
            break
    res["t_block_ms"] = tb
    return res


THR_MULTS = (1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 12.0)


def drive_threshold(cell_factory, rest_thr, dt=0.025, T=4000.0, frac=0.9):
    """Steady-state threshold (nA): the smallest multiple of the from-rest threshold at
    which at least `frac` of the pulses in the last half of a regular 20 Hz train evoke
    a stem spike.  Defined because a from-rest threshold is not suprathreshold once
    Ca/SK and Na inactivation have built up (n_evoked is also reported for every run).
    Returns None if no multiple up to 12x drives the neuron."""
    st = regular(20.0, T)
    for m in THR_MULTS:
        rig = engine.Rig(cell_factory(), dt)
        out = rig.run(st, m * rest_thr, [], T + 50.0)
        sp = out["stem_pre"]
        late = st[st >= T / 2]
        hit = sum(1 for t0 in late if not np.isnan(engine.first_in(sp, t0, t0 + 5.0)))
        if hit >= frac * len(late):
            return m * rest_thr
    return None
