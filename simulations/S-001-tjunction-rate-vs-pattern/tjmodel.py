"""Pseudounipolar sensory-neuron models and stimulation protocols for S-1.

C-neuron: after Sundt, Gamper & Jaffe 2015 (ModelDB 187473), geometry and
channel densities from its Figure5d.hoc / Figure8c.hoc, rebuilt in Python with
the ModelDB mechanisms (copied into mod/, see mod/PROVENANCE.md). The pump and
extracellular-K mechanisms of Fig. 8c are not used: the paper reports that
they do not change the following frequency.

Aβ comparator: generic node-and-internode pseudounipolar neuron, built here.

This module is imported by simulate_s001.py and is import-safe: NEURON is
loaded lazily by load_neuron() so worker processes each get their own.
"""

import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

h = None  # set by load_neuron()


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
    h = _h
    return h


def clear_all():
    """Delete every section so one process can build many cells in turn."""
    load_neuron()
    for sec in list(h.allsec()):
        h.delete_section(sec=sec)


# --- C-neuron ---------------------------------------------------------------

# Sundt 2015 Fig5d / Fig8c values.  Lengths are shortened (the axons are 5 mm
# in the paper; conduction delay is irrelevant to following-frequency).
C_BASE = dict(
    diam_peri=0.8, diam_central=0.4, diam_stem=1.4,
    L_axon=1500.0, L_tj=100.0, L_stem=75.0, diam_soma=25.0,
    nav=0.0385, nav_soma=0.02, kv=0.04,
    kcnq=0.0, ek=-90.0,
    gsk=0.0, gcal=0.00025, sk_tau=500.0, sk_stem=False,
    celsius=35.0, dx=50.0, dx_tj=10.0,
)

# The three Sundt configurations used as the positive control.
CONFIG_NA_K = dict(kcnq=0.0, gsk=0.0)
CONFIG_KCNQ = dict(kcnq=0.0004, gsk=0.0)


def _seg(L, dx):
    n = max(3, int(round(L / dx)))
    return n if n % 2 else n + 1  # odd


class CNeuron:
    v_rest = -60.0
    """Soma, stem, tj (peripheral and central stubs), peripheral and central axons."""

    def __init__(self, **kw):
        clear_all()
        p = dict(C_BASE)
        p.update(kw)
        self.p = p
        h.celsius = p["celsius"]
        mk = lambda name: h.Section(name=name, cell=self)
        self.peri, self.tjperi, self.tjcentral = mk("peri"), mk("tjperi"), mk("tjcentral")
        self.central, self.stem, self.soma = mk("central"), mk("stem"), mk("soma")
        self.sections = [self.peri, self.tjperi, self.tjcentral, self.central, self.stem, self.soma]
        self.peri.L, self.peri.diam = p["L_axon"], p["diam_peri"]
        self.tjperi.L, self.tjperi.diam = p["L_tj"], p["diam_peri"]
        self.tjcentral.L, self.tjcentral.diam = p["L_tj"], p["diam_central"]
        self.central.L, self.central.diam = p["L_axon"], p["diam_central"]
        self.stem.L, self.stem.diam = p["L_stem"], p["diam_stem"]
        self.soma.L, self.soma.diam = 25.0, p["diam_soma"]
        dx = p["dx"]
        dxj = p["dx_tj"]
        self.peri.nseg = self.central.nseg = _seg(p["L_axon"], dx)
        self.tjperi.nseg = self.tjcentral.nseg = _seg(p["L_tj"], dxj)
        self.stem.nseg = _seg(p["L_stem"], dxj)
        self.soma.nseg = 1
        # same topology as the hoc: peri->tjperi, tjperi->stem, stem->soma,
        # tjperi->tjcentral, tjcentral->central
        self.tjperi.connect(self.peri(1), 0)
        self.stem.connect(self.tjperi(1), 0)
        self.soma.connect(self.stem(1), 0)
        self.tjcentral.connect(self.tjperi(1), 0)
        self.central.connect(self.tjcentral(1), 0)
        self._insert()

    def _insert(self):
        p = self.p
        for sec in self.sections:
            sec.Ra = 100.0
            sec.insert("nahh")
            sec.gnabar_nahh = p["nav"]
            sec.mshift_nahh = -6.0
            sec.hshift_nahh = 6.0
            sec.insert("borgkdr")
            sec.gkdrbar_borgkdr = p["kv"]
            sec.ek = p["ek"]
            sec.insert("pas")
            sec.g_pas = 1.0 / 10000.0
        self.soma.gnabar_nahh = p["nav_soma"]
        for sec in (self.tjperi, self.tjcentral, self.stem, self.soma):
            if p["kcnq"] > 0:
                sec.insert("iM")
                sec.vshift_iM = -5.0
                sec.gkbar_iM = p["kcnq"]
        if p["gsk"] > 0:
            targets = [self.soma] + ([self.stem] if p["sk_stem"] else [])
            for sec in targets:
                sec.insert("cal")
                sec.gcalbar_cal = p["gcal"]
                sec.insert("SK")
                sec.gskbar_SK = p["gsk"]
                sec.sstau_SK = p["sk_tau"]
        self.init_rest()

    def init_rest(self):
        """As the hoc: set v=-60 everywhere and choose e_pas so that -60 is a fixed point."""
        for sec in self.sections:
            sec.v = -60.0
        h.finitialize(-60.0)
        h.fcurrent()
        for sec in self.sections:
            for seg in sec:
                ica = seg.ica if hasattr(seg, "ica") else 0.0
                seg.e_pas = seg.v + (seg.ina + seg.ik + ica) / seg.g_pas
        h.finitialize(-60.0)
        h.fcurrent()

    # recording sites -----------------------------------------------------
    def sites(self):
        return dict(
            peri_dist=self.peri(0.05), peri_pre=self.peri(0.95),
            stem_mid=self.stem(0.5), stem_pre=self.stem(0.9), soma=self.soma(0.5),
            central=self.central(0.04), tj=self.tjperi(0.5),
        )


# --- Aβ comparator ------------------------------------------------------------

AB_BASE = dict(
    diam_axon=5.0, diam_stem=3.0, L_int=400.0, n_int=4, L_node=2.0,
    nav_node=0.5, nav_stem=0.12, nav_soma=0.05, kv=0.04, cm_int=0.01,
    rm_int=1e5, diam_soma=40.0, L_stem=60.0, celsius=35.0,
)


V_REST_A = -65.0  # unshifted Traub-Miles Na kinetics rest near -65 mV; -60 is above threshold


class ANeuron:
    v_rest = V_REST_A
    """Myelinated pseudounipolar neuron: soma, short stem, T-junction node, then
    alternating internode/node peripheral and central axons.  Unshifted Na
    kinetics (nahh default), Kdr at nodes and stem."""

    def __init__(self, **kw):
        clear_all()
        p = dict(AB_BASE)
        p.update(kw)
        self.p = p
        h.celsius = p["celsius"]
        self.soma = h.Section(name="soma", cell=self)
        self.stem = h.Section(name="stem", cell=self)
        self.tj = h.Section(name="tj", cell=self)  # T-junction node
        self.sections = [self.soma, self.stem, self.tj]
        self.soma.L = 40.0
        self.soma.diam = p["diam_soma"]
        self.soma.nseg = 1
        self.stem.L, self.stem.diam, self.stem.nseg = p["L_stem"], p["diam_stem"], 7
        self.tj.L, self.tj.diam, self.tj.nseg = p["L_node"], p["diam_axon"], 1
        self.stem.connect(self.soma(1), 0)
        self.tj.connect(self.stem(1), 0)

        def chain(prev, tag):
            secs = []
            for k in range(p["n_int"]):
                inter = h.Section(name=f"{tag}_int{k}", cell=self)
                node = h.Section(name=f"{tag}_node{k}", cell=self)
                inter.L, inter.diam, inter.nseg = p["L_int"], p["diam_axon"], 9
                node.L, node.diam, node.nseg = p["L_node"], p["diam_axon"], 1
                inter.connect(prev(1), 0)
                node.connect(inter(1), 0)
                prev = node
                secs += [inter, node]
            return secs

        self.peri_secs = chain(self.tj, "peri")
        self.central_secs = chain(self.tj, "cent")
        self.sections += self.peri_secs + self.central_secs
        # distal and proximal recording nodes
        self.peri_last = self.peri_secs[-1]
        self.peri_pre = self.peri_secs[1]       # first node peripheral of the T-junction
        self.central_first = self.central_secs[1]
        self.central_last = self.central_secs[-1]
        for sec in self.sections:
            sec.Ra = 100.0
            sec.insert("pas")
            sec.insert("nahh")
            sec.insert("borgkdr")
            sec.ek = -90.0
            internode = "_int" in sec.name()
            if internode:
                sec.cm = p["cm_int"]
                sec.g_pas = 1.0 / p["rm_int"]
                sec.gnabar_nahh = 0.0
                sec.gkdrbar_borgkdr = 0.0
            else:
                sec.cm = 1.0
                sec.g_pas = 1.0 / 10000.0
                sec.gnabar_nahh = p["nav_node"]
                sec.gkdrbar_borgkdr = p["kv"]
        self.stem.gnabar_nahh = p["nav_stem"]
        self.soma.gnabar_nahh = p["nav_soma"]
        for sec in self.sections:
            sec.v = V_REST_A
        h.finitialize(V_REST_A)
        h.fcurrent()
        for sec in self.sections:
            for seg in sec:
                seg.e_pas = seg.v + (seg.ina + seg.ik) / seg.g_pas
        h.finitialize(V_REST_A)
        h.fcurrent()

    def sites(self):
        return dict(
            peri_dist=self.peri_last(0.5), peri_pre=self.peri_pre(0.5),
            stem_mid=self.stem(0.5), stem_pre=self.stem(0.9), soma=self.soma(0.5),
            central=self.central_first(0.5), tj=self.tj(0.5),
        )
