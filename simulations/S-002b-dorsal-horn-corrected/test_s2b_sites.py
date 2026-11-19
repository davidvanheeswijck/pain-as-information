"""Site and connectivity test for S-2b, from the BUILT topology.

S-2 drove the wrong input (Abeta fibres 0-14 instead of the surround fibres 30-44) and counted Abeta and
Adelta together.  Here every driver fibre set is derived from what NEURON says about the built network (which
cell a NetCon's target synapse sits on, with what weight) and the protocol's constants are asserted equal to
the derived sets.  The Mutation class applies the same assertion helpers to deliberately wrong inputs (S-2's
actual error, a hillock recorder, a shifted set that includes the EX synapses) and they must FAIL.

    simulations/.venv/bin/python -B -m unittest test_s2b_sites    (from this directory)
"""

import os
import sys
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import s2b_protocol as P  # noqa: E402
import dh_model as dm  # noqa: E402


def post_cell(nc):
    return str(nc.syn().get_segment().sec.cell())


def syn_type(nc):
    return nc.syn().hname().split("[")[0]


def fibres_reaching_only(model, cell_label):
    """Fibres (0..74) every one of whose connections targets `cell_label`, derived from the NetCons."""
    out = []
    for f in range(dm.N_FIBRES):
        rows = model.rows_of_fibre(f)
        if rows and {post_cell(model.ncs[k]) for k in rows} == {cell_label}:
            out.append(f)
    return out


def fibres_driving(model, cell_label):
    """Fibres with a NON-ZERO-weight connection onto `cell_label`."""
    return sorted({int(model.table.frm[k]) for k in model.afferent_rows
                   if post_cell(model.ncs[k]) == cell_label and model.ncs[k].weight[0] > 0})


def assert_stimulation_fibres(case, model, fibres):
    """The stimulation must be on exactly the fibres that reach SG76 only (the surround input)."""
    case.assertEqual(sorted(fibres), fibres_reaching_only(model, "SG76"))


def assert_recorder(case, model, name, cell_label):
    r = model.rec[name]
    case.assertEqual(str(r["section"].cell()), cell_label)
    case.assertEqual(r["section"].name().split(".")[-1], "soma")
    case.assertEqual(r["x"], 0.5)
    case.assertEqual(str(r["nc"].precell()), cell_label)


def assert_shifted_set(case, model, shifted):
    names = sorted((str(s.get_segment().sec.cell()), s.hname().split("[")[0]) for s in shifted)
    case.assertEqual(len(shifted), 4, names)
    case.assertTrue(all(c == "WDR" for c, _ in names), names)
    case.assertEqual(sum(1 for _, n in names if n == "Glycine_DynSyn"), 1)
    case.assertEqual(sum(1 for _, n in names if n == "GABAa_DynSyn"), 3)


_MODEL = []


def shared_model():
    if not _MODEL:
        m = dm.DorsalHorn()
        m.setup_recorders()
        _MODEL.append(m)
    return _MODEL[0]


class Topology(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = shared_model()

    def test_surround_fibres_derived_from_topology(self):
        derived = fibres_reaching_only(self.m, "SG76")
        self.assertEqual(derived, list(range(30, 45)))
        self.assertEqual(derived, list(P.SURROUND))
        for f in derived:
            rows = self.m.rows_of_fibre(f)
            self.assertEqual(len(rows), 1)
            self.assertEqual(syn_type(self.m.ncs[rows[0]]), "AMPA_DynSyn")
            self.assertGreater(self.m.ncs[rows[0]].weight[0], 0)

    def test_stimulation_driver_uses_exactly_the_surround_fibres(self):
        for v in ("norm", "H", "D1"):
            fibres = list(P.scs_trains(40, v, 0, 1))
            self.assertTrue(set(fibres) <= set(P.SURROUND), v)
        assert_stimulation_fibres(self, self.m, list(P.scs_trains(40, "norm", 0, 1)))
        # D2 adds the Adelta fibres on purpose
        self.assertEqual(sorted(P.scs_trains(40, "D2", 0, 1)), sorted(list(P.SURROUND) + list(P.ADELTA)))

    def test_sg76_outputs_are_gaba_a_onto_ex_and_wdr(self):
        rows = [k for k, nc in enumerate(self.m.ncs) if nc.precell() is not None and str(nc.precell()) == "SG76"]
        self.assertEqual(rows, [288, 289, 290])
        got = sorted((post_cell(self.m.ncs[k]), syn_type(self.m.ncs[k])) for k in rows)
        self.assertEqual(got, [("EX", "GABAa_DynSyn"), ("WDR", "GABAa_DynSyn"), ("WDR", "GABAa_DynSyn")])
        shifted = self.m.wdr_inhibitory_synapses()
        for k in rows:
            on_wdr = post_cell(self.m.ncs[k]) == "WDR"
            self.assertEqual(any(self.m.ncs[k].syn() == s for s in shifted), on_wdr, f"row {k}")

    def test_abeta_fibres_are_the_ones_driving_sg75_and_adelta_are_not(self):
        self.assertEqual(fibres_driving(self.m, "SG75"), list(P.ABETA))
        for f in P.ADELTA:
            self.assertNotIn(f, fibres_driving(self.m, "SG75"))
            self.assertIn(f, fibres_driving(self.m, "WDR"))
        for f in P.ABETA:
            self.assertIn(f, fibres_driving(self.m, "WDR"))

    def test_afib_decomposition_masks(self):
        m = self.m
        frm = m.table.frm

        def fibres(ev):
            return {int(frm[k]) for k in ev}

        full = fibres(P.afib_events(m, True, True))
        only_b = fibres(P.afib_events(m, True, False))
        only_d = fibres(P.afib_events(m, False, True))
        none = fibres(P.afib_events(m, False, False))
        self.assertTrue(set(P.ABETA) <= full and set(P.ADELTA) <= full)
        self.assertTrue(set(P.ABETA) <= only_b and not (set(P.ADELTA) & only_b))
        self.assertTrue(set(P.ADELTA) <= only_d and not (set(P.ABETA) & only_d))
        self.assertFalse((set(P.ABETA) | set(P.ADELTA)) & none)
        for s in (full, only_b, only_d, none):
            self.assertTrue(set(P.CFIB) <= s)

    def test_c_fibres_reach_only_ex_and_wdr_nk1(self):
        m = self.m
        for f in P.CFIB:
            for k in m.rows_of_fibre(f):
                self.assertIn((post_cell(m.ncs[k]), syn_type(m.ncs[k])),
                              {("EX", "AMPA_DynSyn"), ("EX", "NMDA_DynSyn"), ("EX", "NK1_DynSyn"),
                               ("WDR", "NK1_DynSyn")})

    def test_recorders_on_somas_at_half(self):
        for name in ("WDR", "SG75", "EX"):
            assert_recorder(self, self.m, name, name)

    def test_shift_changes_exactly_the_four_wdr_inhibitory_synapses(self):
        m = self.m
        assert_shifted_set(self, m, m.wdr_inhibitory_synapses())
        before = {(c.label, i): float(s.e) for c in m.cells.values() for i, s in enumerate(c.synlist)}
        m.set_shift(20.0)
        after = {(c.label, i): float(s.e) for c in m.cells.values() for i, s in enumerate(c.synlist)}
        changed = sorted(k for k in before if before[k] != after[k])
        self.assertEqual(len(changed), 4, changed)
        self.assertTrue(all(c == "WDR" for c, _ in changed))
        m.set_shift(0.0)
        self.assertAlmostEqual(float(m.cells[changed[0][0]].synlist[changed[0][1]].e), -70.0)

    def test_scs_pulses_reach_sg76_and_its_gaba_a_synapse_on_the_wdr(self):
        """A short run with synchronous pulses on the surround fibres: SG76 fires, its GABA-A synapse on the
        WDR (row 289) becomes conductive after SG76's first spike, and no other fibre class is driven."""
        m = self.m
        m.set_shift(0.0)
        sg76 = dm.h.Vector()
        nc = dm.h.NetCon(m.sg76.soma(0.5)._ref_v, None, sec=m.sg76.soma)
        nc.threshold = -30
        nc.record(sg76)
        g = dm.h.Vector()
        g.record(m.ncs[289].syn()._ref_g)
        m.run(m.expand_fibres({f: np.arange(10.0, 130.0, 10.0) for f in P.SURROUND}), 160.0, 0.025)
        self.assertGreater(len(sg76), 0, "SG76 did not fire")
        self.assertGreater(max(np.array(g)), 0.0, "row 289 synapse never conducted")
        self.assertEqual(len(m.rec["WDR"]["spikes"]), 0)


class Mutations(unittest.TestCase):
    """The helpers above must FAIL on a wrong site, a wrong driver, a wrong shifted set (python -B)."""

    @classmethod
    def setUpClass(cls):
        cls.m = shared_model()

    def test_pulses_on_abeta_fibres_fail(self):
        """S-2's error: stimulation pulsed Abeta fibres 0-14."""
        wrong = {f: P.scs_times(40) for f in P.ABETA}
        with self.assertRaises(AssertionError):
            assert_stimulation_fibres(self, self.m, list(wrong))

    def test_pulses_on_surround_plus_adelta_fail(self):
        wrong = list(P.SURROUND) + list(P.ADELTA)
        with self.assertRaises(AssertionError):
            assert_stimulation_fibres(self, self.m, wrong)

    def test_mutated_protocol_constant_fails_the_real_driver_test(self):
        saved = P.SURROUND
        try:
            P.SURROUND = P.ABETA
            with self.assertRaises(AssertionError):
                assert_stimulation_fibres(self, self.m, list(P.scs_trains(40, "norm", 0, 1)))
        finally:
            P.SURROUND = saved

    def test_recorder_on_hillock_fails(self):
        m = self.m
        r = m.rec["WDR"]
        saved = dict(r)
        try:
            nc = dm.h.NetCon(m.wdr.hillock(0.5)._ref_v, None, sec=m.wdr.hillock)
            r.update(nc=nc, section=m.wdr.hillock, x=0.5)
            with self.assertRaises(AssertionError):
                assert_recorder(self, m, "WDR", "WDR")
        finally:
            r.update(saved)

    def test_shifted_set_on_ex_fails(self):
        wrong = [s for s in self.m.ex.synlist if s.hname().startswith("GABAa_DynSyn")]
        with self.assertRaises(AssertionError):
            assert_shifted_set(self, self.m, wrong)

    def test_shifted_set_with_ex_synapse_added_fails(self):
        ex_gaba = [s for s in self.m.ex.synlist if s.hname().startswith("GABAa_DynSyn")][0]
        wrong = list(self.m.wdr_inhibitory_synapses())[:3] + [ex_gaba]
        with self.assertRaises(AssertionError):
            assert_shifted_set(self, self.m, wrong)


if __name__ == "__main__":
    unittest.main()
