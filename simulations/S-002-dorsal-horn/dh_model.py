"""Python re-implementation of the Zhang, Janik & Grill 2014 dorsal-horn network.

Source: ModelDB 168414 (PROVENANCE.md).  The shipped hoc scripts are NOT run and
not loaded.  The four cell templates in `CellTemplates.hoc` are re-created here
from their geometry and parameters as read, and the 291-connection table is read
as plain numbers from `data/`.

Cells (shipped names): `MelnickSG` x2 (cell 75 local, cell 76 surround; the
inhibitory interneurons), `AguiarIN` (cell 77, the excitatory interneuron),
`AguiarWDR` (cell 78, the projection neuron).  Afferent "fibres" 0 to 74: 0-14
A-beta, 15-29 A-delta, 30-44 surround input, 45-74 C.

Every recording site and every synapse target is resolved from the built topology
(see test_sites.py); nothing here hard-codes a synapse index for a role except the
shipped table itself.
"""

import os

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")

h = None

N_FIBRES = 75
ABETA = tuple(range(0, 15))
ADELTA = tuple(range(15, 30))
SURROUND = tuple(range(30, 45))
CFIB = tuple(range(45, 75))

# Shipped cell indices of the four neurons
CELL_INDEX = {"SG75": 75, "SG76": 76, "EX": 77, "WDR": 78}

# Weight groups for the ensemble (PREDICTION.md, Ensemble): rows of the shipped table
GROUP_ROWS = {
    "abeta_wdr": list(range(15, 45)),
    "abeta_sg": list(range(0, 15)),
    "sg_wdr": [286, 287],
    "sg_ex": [225],
    "c_ex": list(range(105, 165)),
    "nk1": list(range(165, 225)),
    "ex_wdr": list(range(226, 286)),
    "adelta_wdr": list(range(60, 90)),
    "surround_out": [288, 289, 290],
}
WEIGHT_RANGE = (0.5, 2.0)
CONDUCTANCE_FACTORS = {  # name: (low, high)
    "wdr_cal": (0.5, 2.0),
    "wdr_kca": (0.5, 2.0),
    "wdr_nap": (0.5, 2.0),
    "sg_na": (0.8, 1.25),
    "wdr_na": (0.8, 1.25),
}


def load_neuron():
    """Import NEURON and load the compiled mechanisms in mod/arm64 (or similar)."""
    global h
    if h is not None:
        return h
    from neuron import h as _h

    for arch in ("arm64", "x86_64", "aarch64"):
        lib = os.path.join(HERE, "mod", arch, "libnrnmech.dylib")
        if not os.path.exists(lib):
            lib = os.path.join(HERE, "mod", arch, "libnrnmech.so")
        if os.path.exists(lib):
            _h.nrn_load_dll(lib)
            break
    else:
        raise RuntimeError("compiled mechanisms not found; run nrnivmodl in mod/")
    _h.load_file("stdrun.hoc")
    _h.cvode_active(0)
    h = _h
    return h


def read_table(name, dtype=float):
    with open(os.path.join(DATA, name)) as fh:
        return np.array([dtype(x) for x in fh.read().split()])


class Table:
    """The shipped connection table (Foreman SCS weights)."""

    def __init__(self):
        self.frm = read_table("FromVector.txt", int)
        self.to = read_table("ToVector.txt", int)
        self.syn = read_table("SynapseVector.txt", int)
        self.weight = read_table("WeightVector_foreman.txt", float)
        self.delay = read_table("DelayVector.txt", float)
        n = len(self.frm)
        assert n == 291 and all(len(a) == n for a in (self.to, self.syn, self.weight, self.delay))


class Cell:
    """A cell with sections created under it, named so that `sec.cell()` returns it."""

    kind = "?"

    def __init__(self, label):
        self.label = label
        self.synlist = []

    def __repr__(self):
        return self.label

    def sec(self, name):
        s = h.Section(name=name, cell=self)
        setattr(self, name, s)
        return s

    def sections(self):
        return [getattr(self, n) for n in ("soma", "hillock", "axon", "dend") if hasattr(self, n)]

    def add_syn(self, typ, tau_rise, tau_decay, e=None, sec=None):
        sec = sec if sec is not None else self.dend
        syn = getattr(h, typ)(sec(0.5))
        syn.tau_rise = tau_rise
        syn.tau_decay = tau_decay
        if e is not None:
            syn.e = e
        self.synlist.append(syn)
        return syn


class MelnickSG(Cell):
    """`MelnickSG` of CellTemplates.hoc (Melnick et al. 2004), as read."""

    kind = "MelnickSG"

    def __init__(self, label):
        super().__init__(label)
        soma, hil, axon, dend = (self.sec(n) for n in ("soma", "hillock", "axon", "dend"))
        soma.diam = 10
        soma.L = 10
        soma.nseg = 10
        for m in ("B_Na", "B_A", "B_DR", "KDR", "KDRI", "pas"):
            soma.insert(m)
        soma.gnabar_B_Na = 0.008
        soma.ena = 60
        soma.g_pas = 1.1e-05
        soma.e_pas = -70
        soma.gkbar_KDRI = 0.0043
        soma.ek = -84

        hil.L = 30
        hil.nseg = 30
        hil.diam = 1.0   # diam(0:1) = 1 : 0.5
        for m in ("B_Na", "B_A", "B_DR", "KDR", "KDRI", "pas"):
            hil.insert(m)
        hil.gnabar_B_Na = 3.45
        hil.ena = 60
        hil.g_pas = 1.1e-05
        hil.e_pas = -70
        hil.gkbar_KDRI = 0.076
        hil.ek = -84
        for i, seg in enumerate(hil):
            seg.diam = 1.0 + (0.5 - 1.0) * seg.x

        axon.diam = 0.001
        axon.L = 0.001
        axon.nseg = 50
        for m in ("B_Na", "B_A", "B_DR", "KDR", "KDRI", "pas"):
            axon.insert(m)
        axon.ena = 60
        axon.g_pas = 0
        axon.e_pas = -70
        axon.gkbar_KDRI = 0
        axon.ek = -84

        dend.nseg = 50
        dend.diam = 1.4
        dend.L = 1371
        for m in ("SS", "B_DR", "KDR", "KDRI", "pas"):
            dend.insert(m)
        dend.gnabar_SS = 0
        dend.ena = 60
        dend.g_pas = 1.1e-05
        dend.e_pas = -70
        dend.gkbar_KDRI = 0.034
        dend.ek = -84

        hil.connect(soma(1), 0)
        axon.connect(hil(1), 0)
        dend.connect(soma(0), 0)
        for s in self.sections():
            s.Ra = 80
        # Two groups of 15 AMPA synapses (local A-beta input; A-delta input), tau 0.1/5
        for _ in range(30):
            self.add_syn("AMPA_DynSyn", 0.1, 5)


class AguiarIN(Cell):
    """`AguiarIN` ("EX cell") of CellTemplates.hoc, as read."""

    kind = "AguiarIN"

    def __init__(self, label):
        super().__init__(label)
        soma, dend, hil, axon = (self.sec(n) for n in ("soma", "dend", "hillock", "axon"))
        soma.nseg = 3
        soma.L = 20.0
        soma.diam = 20.0
        soma.insert("HH2")
        soma.gnabar_HH2 = 0.0
        soma.gkbar_HH2 = 0.0043 * 1 / 4
        soma.vtraub_HH2 = -55.0
        soma.insert("CaIntraCellDyn")
        soma.depth_CaIntraCellDyn = 0.1
        soma.cai_tau_CaIntraCellDyn = 1.0
        soma.cai_inf_CaIntraCellDyn = 50.0e-6
        soma.insert("iKCa")
        soma.gbar_iKCa = 0.002
        soma.insert("pas")
        soma.g_pas = 4.2e-5
        soma.e_pas = -65.0
        soma.ek = -70.0
        soma.Ra = 150.0

        dend.nseg = 5
        dend.L = 400.0
        dend.diam = 3.0
        dend.insert("HH2")
        dend.gnabar_HH2 = 0.0
        dend.gkbar_HH2 = 0.036
        dend.insert("CaIntraCellDyn")
        dend.depth_CaIntraCellDyn = 0.1
        dend.cai_tau_CaIntraCellDyn = 2.0
        dend.cai_inf_CaIntraCellDyn = 50.0e-6
        dend.insert("iKCa")
        dend.gbar_iKCa = 0.002
        dend.insert("pas")
        dend.g_pas = 4.2e-5
        dend.e_pas = -65.0
        dend.ek = -70.0
        dend.Ra = 150.0

        hil.nseg = 3
        hil.L = 9.0
        hil.insert("HH2")
        hil.gnabar_HH2 = 3.45
        hil.gkbar_HH2 = 0.076
        hil.vtraub_HH2 = -55.0
        hil.insert("pas")
        hil.g_pas = 4.2e-5
        hil.e_pas = -65.0
        hil.Ra = 150.0
        for seg in hil:
            seg.diam = 2.0 + (1.0 - 2.0) * seg.x

        axon.nseg = 5
        axon.L = 1000.0
        axon.diam = 1.0
        axon.insert("HH2")
        axon.gnabar_HH2 = 0.0
        axon.gkbar_HH2 = 0.0
        axon.vtraub_HH2 = -55
        axon.insert("pas")
        axon.g_pas = 4.2e-5
        axon.e_pas = -65.0
        axon.Ra = 150.0

        hil.connect(soma(1), 0)
        axon.connect(hil(1), 0)
        dend.connect(soma(0), 0)

        for _ in range(30):
            self.add_syn("AMPA_DynSyn", 0.1, 5)
        for _ in range(30):
            self.add_syn("NMDA_DynSyn", 2, 100)
        for _ in range(30):
            self.add_syn("NK1_DynSyn", 100, 3000)
        for _ in range(2):
            self.add_syn("GABAa_DynSyn", 0.1, 20, e=-70)
        for _ in range(2):
            self.add_syn("GABAa_DynSyn", 0.1, 20, e=-70)


class AguiarWDR(Cell):
    """`AguiarWDR` ("T cell", the projection neuron) of CellTemplates.hoc, as read."""

    kind = "AguiarWDR"

    def __init__(self, label):
        super().__init__(label)
        cascale = 1.0
        soma, dend, hil, axon = (self.sec(n) for n in ("soma", "dend", "hillock", "axon"))
        soma.nseg = 3
        soma.L = 20.0
        soma.diam = 20.0
        soma.insert("HH2")
        soma.gnabar_HH2 = 0.000
        soma.gkbar_HH2 = 0.0043 * 6 / 24
        soma.vtraub_HH2 = -55.0
        soma.insert("CaIntraCellDyn")
        soma.depth_CaIntraCellDyn = 0.1
        soma.cai_tau_CaIntraCellDyn = 1.0
        soma.cai_inf_CaIntraCellDyn = 50.0e-6
        soma.insert("iCaL")
        soma.pcabar_iCaL = 0.0001 * cascale
        soma.insert("iCaAN")
        soma.gbar_iCaAN = 0.0000
        soma.insert("iKCa")
        soma.gbar_iKCa = 0.0001 * cascale
        soma.insert("iNaP")
        soma.gnabar_iNaP = 0.0001 * cascale
        soma.insert("pas")
        soma.g_pas = 4.2e-5
        soma.e_pas = -65.0
        soma.ek = -70.0
        soma.Ra = 150.0

        dend.nseg = 5
        dend.L = 350.0
        dend.diam = 2.5
        dend.insert("CaIntraCellDyn")
        dend.depth_CaIntraCellDyn = 0.1
        dend.cai_tau_CaIntraCellDyn = 2.0
        dend.cai_inf_CaIntraCellDyn = 50.0e-6
        dend.insert("iCaL")
        dend.pcabar_iCaL = 3e-5 * cascale
        dend.insert("iCaAN")
        dend.gbar_iCaAN = 0.00007 * cascale * 1.3
        dend.insert("iKCa")
        dend.gbar_iKCa = 0.001 * cascale
        dend.insert("HH2")
        dend.gnabar_HH2 = 0.000
        dend.gkbar_HH2 = 0.036
        dend.insert("pas")
        dend.g_pas = 4.2e-5
        dend.e_pas = -65.0
        dend.ek = -70.0
        dend.Ra = 150.0

        hil.nseg = 3
        hil.L = 9
        hil.insert("HH2")
        hil.gnabar_HH2 = 3.45
        hil.gkbar_HH2 = 0.076
        hil.vtraub_HH2 = -55.0
        hil.insert("B_A")
        hil.gkbar_B_A = 0.0
        hil.insert("pas")
        hil.g_pas = 4.2e-5
        hil.e_pas = -65.0
        hil.Ra = 150.0
        for seg in hil:
            seg.diam = 2.0 + (1.0 - 2.0) * seg.x

        axon.nseg = 5
        axon.L = 1000
        axon.diam = 1.0
        axon.insert("HH2")
        axon.gnabar_HH2 = 0
        axon.gkbar_HH2 = 0
        axon.vtraub_HH2 = -55
        axon.insert("pas")
        axon.g_pas = 0
        axon.e_pas = -65.0
        axon.Ra = 150.0

        hil.connect(soma(1), 0)
        axon.connect(hil(1), 0)
        dend.connect(soma(0), 0)

        # synapse list order as in the template: 15 AMPA, 15 NMDA, 15 AMPA, 15 NMDA,
        # 30 NK1, 30 AMPA, 30 NMDA, 1 glycine, 3 GABA-A
        for _ in range(15):
            self.add_syn("AMPA_DynSyn", 0.1, 5)
        for _ in range(15):
            self.add_syn("NMDA_DynSyn", 2, 100)
        for _ in range(15):
            self.add_syn("AMPA_DynSyn", 0.1, 5)
        for _ in range(15):
            self.add_syn("NMDA_DynSyn", 2, 100)
        for _ in range(30):
            self.add_syn("NK1_DynSyn", 200, 3000)
        for _ in range(30):
            self.add_syn("AMPA_DynSyn", 0.1, 5)
        for _ in range(30):
            self.add_syn("NMDA_DynSyn", 2, 100)
        self.add_syn("Glycine_DynSyn", 0.1, 10)
        for _ in range(3):
            self.add_syn("GABAa_DynSyn", 0.1, 20, e=-70)


class DorsalHorn:
    """The four-cell network with the shipped connection table.

    `weight_factors`: group name -> multiplier on the shipped weights of that group's rows.
    `cond_factors`: name -> multiplier on the shipped conductances (CONDUCTANCE_FACTORS).
    """

    def __init__(self, weight_factors=None, cond_factors=None, dt=0.025):
        load_neuron()
        for sec in list(h.allsec()):
            h.delete_section(sec=sec)
        self.table = Table()
        self.sg75 = MelnickSG("SG75")
        self.sg76 = MelnickSG("SG76")
        self.ex = AguiarIN("EX")
        self.wdr = AguiarWDR("WDR")
        self.cells = {"SG75": self.sg75, "SG76": self.sg76, "EX": self.ex, "WDR": self.wdr}
        by_index = {75: self.sg75, 76: self.sg76, 77: self.ex, 78: self.wdr}
        self.row_group = {}
        for g, rows in GROUP_ROWS.items():
            for r in rows:
                assert r not in self.row_group, (g, r)
                self.row_group[r] = g
        wf = dict(weight_factors or {})
        self.ncs = []
        self.afferent_rows = []
        T = self.table
        for k in range(len(T.frm)):
            tgt = by_index[int(T.to[k])]
            syn = tgt.synlist[int(T.syn[k])]
            src = int(T.frm[k])
            if src < N_FIBRES:
                nc = h.NetCon(None, syn)
                self.afferent_rows.append(k)
            else:
                scell = by_index[src]
                nc = h.NetCon(scell.soma(1)._ref_v, syn, sec=scell.soma)
                nc.threshold = -30
            nc.delay = float(T.delay[k])
            nc.weight[0] = float(T.weight[k]) * float(wf.get(self.row_group.get(k), 1.0))
            self.ncs.append(nc)
        self.afferent_rows = np.array(self.afferent_rows)
        cf = dict(cond_factors or {})
        self.apply_conductance_factors(cf)
        self.dt = dt
        self._shift = 0.0
        self.set_shift(0.0)
        # recorders
        self.rec = {}
        self._pending = {}
        self._fih = h.FInitializeHandler(1, self._load_events)

    # -- topology-derived roles ------------------------------------------------

    def wdr_inhibitory_synapses(self):
        """Inhibitory (glycine / GABA-A) synapses whose post-synaptic cell is the WDR neuron,
        resolved from the NetCon targets, not from indices."""
        out = []
        for nc in self.ncs:
            syn = nc.syn()
            if syn.get_segment().sec.cell() is self.wdr and syn.hname().startswith(("GABAa_DynSyn", "Glycine_DynSyn")):
                if not any(syn == o for o in out):
                    out.append(syn)
        return out

    def apply_conductance_factors(self, cf):
        f = {k: float(cf.get(k, 1.0)) for k in CONDUCTANCE_FACTORS}
        w = self.wdr
        for s in (w.soma, w.dend):
            for seg in s:
                seg.pcabar_iCaL = seg.pcabar_iCaL * f["wdr_cal"]
                seg.gbar_iKCa = seg.gbar_iKCa * f["wdr_kca"]
        for seg in w.soma:
            seg.gnabar_iNaP = seg.gnabar_iNaP * f["wdr_nap"]
        for c in (self.sg75, self.sg76):
            for seg in c.hillock:
                seg.gnabar_B_Na = seg.gnabar_B_Na * f["sg_na"]
        for seg in w.hillock:
            seg.gnabar_HH2 = seg.gnabar_HH2 * f["wdr_na"]

    def set_shift(self, shift_mv, base=-70.0):
        """Shift the anion reversal potential of the WDR's inhibitory synapses to base + shift."""
        self._shift = float(shift_mv)
        for syn in self.wdr_inhibitory_synapses():
            syn.e = base + self._shift

    # -- recording --------------------------------------------------------------

    def setup_recorders(self, traces=False):
        """Spike recorders (WDR, SG75, EX soma, upward crossing of -30 mV at x = 0.5, as the
        shipped `OutputData`) are made once; trace recorders on request, once."""
        if not self.rec:
            for name, cell in (("WDR", self.wdr), ("SG75", self.sg75), ("EX", self.ex)):
                vec = h.Vector()
                nc = h.NetCon(cell.soma(0.5)._ref_v, None, sec=cell.soma)
                nc.threshold = -30
                nc.record(vec)
                self.rec[name] = {"nc": nc, "spikes": vec, "section": cell.soma, "x": 0.5}
        if traces and "v" not in self.rec["WDR"]:
            for name, cell in (("WDR", self.wdr), ("SG75", self.sg75), ("EX", self.ex)):
                v = h.Vector()
                v.record(cell.soma(0.5)._ref_v, sec=cell.soma)
                self.rec[name]["v"] = v
            self.rec_t = h.Vector()
            self.rec_t.record(h._ref_t)

    # -- running ----------------------------------------------------------------

    def _load_events(self):
        for k, times in self._pending.items():
            nc = self.ncs[k]
            for t in times:
                nc.event(float(t))

    def run(self, events_by_row, tstop, dt=None, traces=False, v_init=-65.0):
        """Run once from rest.  `events_by_row`: connection row -> array of event times (ms),
        for afferent rows only.  Returns dict(WDR=spike times, SG75=..., EX=...)."""
        dt = self.dt if dt is None else dt
        h.celsius = 36
        h.dt = dt
        h.tstop = tstop
        self.setup_recorders(traces=traces)
        for r in self.rec.values():
            r["spikes"].resize(0)
            if "v" in r:
                r["v"].resize(0)
        rows = set(int(k) for k in self.afferent_rows)
        pend = {}
        for k, times in events_by_row.items():
            assert int(k) in rows, f"row {k} is not afferent"
            if self.ncs[int(k)].weight[0] == 0:
                continue
            t = np.asarray(times, dtype=float)
            t = t[(t >= 0) & (t < tstop)]
            if len(t):
                pend[int(k)] = np.sort(t)
        self._pending = pend
        h.finitialize(v_init)
        h.continuerun(tstop)
        out = {n: np.array(r["spikes"]) for n, r in self.rec.items()}
        if traces and "v" in self.rec["WDR"]:
            out["t"] = np.array(self.rec_t)
            out["v"] = {n: np.array(r["v"]) for n, r in self.rec.items()}
        return out

    # -- afferent helpers ----------------------------------------------------------

    def rows_of_fibre(self, fibre):
        return [int(k) for k in self.afferent_rows if int(self.table.frm[k]) == fibre]

    def expand_fibres(self, fibre_trains):
        """fibre -> times  ==>  row -> times (same train on every connection of a fibre)."""
        ev = {}
        for f, t in fibre_trains.items():
            if len(t) == 0:
                continue
            for k in self.rows_of_fibre(int(f)):
                ev[k] = t
        return ev
