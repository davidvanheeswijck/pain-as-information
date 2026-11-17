"""Simulation engine: drive a cell with soma stimulation and peripheral test
spikes, record threshold crossings, score F.  Import-safe (NEURON lazy)."""

import numpy as np

import tjmodel

PULSE_MS = 1.0
TEST_PULSE_AMP = 0.3  # nA, 1 ms, at the distal peripheral end


class Rig:
    """Wraps a cell with a stem stimulator, a distal test stimulator and spike recorders."""

    def __init__(self, cell, dt=0.025):
        h = tjmodel.load_neuron()
        self.h = h
        self.cell = cell
        self.dt = dt
        s = cell.sites()
        self.stim = h.IClamp(cell.stem(0.5))  # stimulation site: mid-stem
        self.stim.delay, self.stim.dur, self.stim.amp = 0, 1e9, 0
        self.test = h.IClamp(s["peri_dist"])
        self.test.delay, self.test.dur, self.test.amp = 0, 1e9, 0
        self.rec = {}
        self._apc = {}
        for name in ("peri_pre", "stem_pre", "soma", "central"):
            apc = h.APCount(s[name])
            apc.thresh = 0.0
            vec = h.Vector()
            apc.record(vec)
            self._apc[name] = apc
            self.rec[name] = vec
        self._keep = []

    def _play(self, iclamp, times, amp, width=PULSE_MS):
        """Drive iclamp.amp with rectangular pulses at `times` (ms)."""
        h = self.h
        times = np.asarray(times, dtype=float)
        if len(times) == 0:
            return
        tv = np.empty(2 * len(times) + 1)
        yv = np.zeros(2 * len(times) + 1)
        tv[0], yv[0] = 0.0, 0.0
        tv[1::2] = times
        tv[2::2] = times + width
        yv[1::2] = amp
        yv[2::2] = 0.0
        assert np.all(np.diff(tv) >= 0), "overlapping pulses"
        T, Y = h.Vector(tv), h.Vector(yv)
        Y.play(iclamp._ref_amp, T, 0)
        self._keep += [T, Y]

    def run(self, stim_times, stim_amp, test_times, tstop, test_amp=TEST_PULSE_AMP, traces=None):
        h = self.h
        h.dt = self.dt
        h.steps_per_ms = 1.0 / self.dt
        h.tstop = tstop
        self._keep = []
        for v in self.rec.values():
            v.resize(0)
        self._play(self.stim, stim_times, stim_amp)
        self._play(self.test, test_times, test_amp)
        recs = {}
        if traces:
            s = self.cell.sites()
            tv = h.Vector()
            tv.record(h._ref_t, traces["every"])
            recs["t"] = tv
            for name in traces["sites"]:
                v = h.Vector()
                v.record(s[name]._ref_v, traces["every"])
                recs[name] = v
        h.finitialize(self.cell.v_rest)
        h.fcurrent()
        while h.t < tstop:
            h.fadvance()
        out = {k: np.array(v) for k, v in self.rec.items()}
        if traces:
            out["traces"] = {k: np.array(v) for k, v in recs.items()}
        self.stim.amp = 0.0
        return out


def first_in(times, lo, hi):
    """First crossing time within [lo, hi], else nan (times sorted)."""
    i = np.searchsorted(times, lo)
    if i < len(times) and times[i] <= hi:
        return times[i]
    return np.nan


def measure_latencies(cell_factory, dt=0.025):
    """Unstimulated test-spike latencies launch -> peri_pre -> central."""
    rig = Rig(cell_factory(), dt)
    out = rig.run([], 0.0, [20.0], 120.0)
    pp, ce = out["peri_pre"], out["central"]
    if len(pp) == 0 or len(ce) == 0:
        return None
    return dict(l1=pp[0] - 20.0, d0=ce[0] - pp[0])


def train_follows(cell_factory, f, lat, dt=0.025, npulse=21):
    """True if every one of npulse peripheral pulses at f Hz reaches the central axon."""
    per = 1000.0 / f
    times = 20.0 + per * np.arange(npulse)
    rig = Rig(cell_factory(), dt)
    out = rig.run([], 0.0, times, times[-1] + 60.0)
    ce = out["central"]
    total = lat["l1"] + lat["d0"]
    ok = 0
    for tk in times:
        hi = tk + min(1.8 * total + 3.0, total + 0.9 * per)
        if not np.isnan(first_in(ce, tk + 0.6 * total, hi)):
            ok += 1
    return ok == npulse


FOLLOW_GRID = [2.0 * 1.12 ** k for k in range(0, 40)]  # 2 Hz .. ~180 Hz, 12% steps


def following_frequency(cell_factory, dt=0.025, npulse=21, grid=None):
    """Following frequency: the highest grid frequency below the first at which a
    21-pulse peripheral train fails to reach the central axon in full (as in
    Sundt 2015 and Gemes 2013).  Following is not monotone in frequency in
    these models (phase-locked resonances), so the first failure is used, not
    bisection.  Returns 0.0 if the lowest grid frequency already fails and the
    top of the grid if nothing fails."""
    grid = grid or FOLLOW_GRID
    lat = measure_latencies(cell_factory, dt)
    if lat is None:
        return 0.0
    last = 0.0
    for f in grid:
        if not train_follows(cell_factory, f, lat, dt, npulse):
            # refine: one intermediate point (6% resolution)
            mid = (last * f) ** 0.5 if last > 0 else 0.0
            if mid > 0 and train_follows(cell_factory, mid, lat, dt, npulse):
                return mid
            return last
        last = f
    return last
