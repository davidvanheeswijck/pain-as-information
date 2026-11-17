"""Recording-site and connectivity test for S-2, from the BUILT topology.

S-1 lost a night to a recording-site label that pointed at the wrong end of a
section.  Here every named site and every named synapse is checked against what
NEURON itself says about the built network: which section a recorder sits on and
at which x, which cell a NetCon's target synapse belongs to (`syn.get_segment()
.sec.cell()`), which mod type it is (`syn.hname()`), and which cell a spike
detector belongs to (`nc.precell()`).

The last tests are the mutation checks: the same assertion helpers are applied to a
deliberately wrong site (the WDR hillock instead of the soma) and a deliberately
wrong shifted set (the EX inhibitory synapses), and must FAIL.

    simulations/.venv/bin/python -B -m unittest test_sites    (from this directory)
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np  # noqa: E402

import dh_model as dm  # noqa: E402

# Roles of the shipped table, read from CellTemplates.hoc and the table itself
# (row ranges -> (source role, target cell, synapse type)).
EXPECTED_ROWS = [
    (range(0, 15), "abeta", "SG75", "AMPA_DynSyn"),
    (range(15, 30), "abeta", "WDR", "AMPA_DynSyn"),
    (range(30, 45), "abeta", "WDR", "NMDA_DynSyn"),
    (range(45, 60), "adelta", "SG75", "AMPA_DynSyn"),
    (range(60, 75), "adelta", "WDR", "AMPA_DynSyn"),
    (range(75, 90), "adelta", "WDR", "NMDA_DynSyn"),
    (range(90, 105), "surround", "SG76", "AMPA_DynSyn"),
    (range(105, 135), "c", "EX", "AMPA_DynSyn"),
    (range(135, 165), "c", "EX", "NMDA_DynSyn"),
    (range(165, 195), "c", "EX", "NK1_DynSyn"),
    (range(195, 225), "c", "WDR", "NK1_DynSyn"),
    ([225], "SG75", "EX", "GABAa_DynSyn"),
    (range(226, 256), "EX", "WDR", "AMPA_DynSyn"),
    (range(256, 286), "EX", "WDR", "NMDA_DynSyn"),
    ([286], "SG75", "WDR", "Glycine_DynSyn"),
    ([287], "SG75", "WDR", "GABAa_DynSyn"),
    ([288], "SG76", "EX", "GABAa_DynSyn"),
    ([289, 290], "SG76", "WDR", "GABAa_DynSyn"),
]
FIBRE_ROLE = {**{f: "abeta" for f in dm.ABETA}, **{f: "adelta" for f in dm.ADELTA},
              **{f: "surround" for f in dm.SURROUND}, **{f: "c" for f in dm.CFIB}}


def post_cell(nc):
    return str(nc.syn().get_segment().sec.cell())


def syn_type(nc):
    return nc.syn().hname().split("[")[0]


def pre_cell(nc):
    pc = nc.precell()
    return None if pc is None else str(pc)


def assert_recorder(case, model, name, cell_label):
    """The named recorder is on that cell's soma, at 0.5, as built."""
    r = model.rec[name]
    sec = r["section"]
    case.assertEqual(str(sec.cell()), cell_label)
    case.assertEqual(sec.name().split(".")[-1], "soma")
    case.assertEqual(r["x"], 0.5)
    # the NetCon itself is attached to that soma: its source variable is that section's v
    case.assertEqual(str(r["nc"].precell()), cell_label)


def assert_shifted_set(case, model, shifted):
    """`shifted` (list of synapses) must be exactly the inhibitory synapses on the WDR."""
    names = sorted((str(s.get_segment().sec.cell()), s.hname()) for s in shifted)
    case.assertEqual(len(shifted), 4)
    case.assertTrue(all(c == "WDR" for c, _ in names), names)
    case.assertEqual(sum(1 for _, n in names if n.startswith("Glycine_DynSyn")), 1)
    case.assertEqual(sum(1 for _, n in names if n.startswith("GABAa_DynSyn")), 3)


_MODEL = []


def shared_model():
    """One built network for the whole module: building a second one deletes the first's
    sections while its Python objects are still alive, which can crash NEURON."""
    if not _MODEL:
        m = dm.DorsalHorn()
        m.setup_recorders()
        _MODEL.append(m)
    return _MODEL[0]


class Topology(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.m = shared_model()

    def test_sg_section_geometry(self):
        for c in (self.m.sg75, self.m.sg76):
            ps = c.hillock.parentseg()
            self.assertTrue(ps.sec.same(c.soma) and ps.x == 1.0)
            self.assertTrue(c.hillock(0).sec.same(c.hillock))
            self.assertTrue(c.axon.parentseg().sec.same(c.hillock) and c.axon.parentseg().x == 1.0)
            self.assertTrue(c.dend.parentseg().sec.same(c.soma) and c.dend.parentseg().x == 0.0)

    def test_ex_wdr_section_geometry(self):
        for c in (self.m.ex, self.m.wdr):
            ps = c.hillock.parentseg()
            self.assertTrue(ps.sec.same(c.soma) and ps.x == 1.0)
            self.assertTrue(c.axon.parentseg().sec.same(c.hillock) and c.axon.parentseg().x == 1.0)
            self.assertTrue(c.dend.parentseg().sec.same(c.soma) and c.dend.parentseg().x == 0.0)

    def test_table_roles(self):
        m = self.m
        seen = set()
        for rows, src, tgt, typ in EXPECTED_ROWS:
            for k in rows:
                seen.add(k)
                nc = m.ncs[k]
                self.assertEqual(post_cell(nc), tgt, f"row {k} target cell")
                self.assertEqual(syn_type(nc), typ, f"row {k} synapse type")
                fibre = int(m.table.frm[k])
                if fibre < dm.N_FIBRES:
                    self.assertEqual(FIBRE_ROLE[fibre], src, f"row {k} source fibre class")
                    self.assertIsNone(pre_cell(nc), f"row {k} is afferent, must have no pre-cell")
                else:
                    self.assertEqual(pre_cell(nc), src, f"row {k} pre-synaptic cell")
        self.assertEqual(seen, set(range(291)), "every row of the shipped table is asserted")

    def test_c_fibres_reach_only_ex_and_wdr_nk1(self):
        m = self.m
        for k in m.afferent_rows:
            if FIBRE_ROLE[int(m.table.frm[k])] == "c":
                nc = m.ncs[k]
                self.assertIn((post_cell(nc), syn_type(nc)),
                              {("EX", "AMPA_DynSyn"), ("EX", "NMDA_DynSyn"), ("EX", "NK1_DynSyn"),
                               ("WDR", "NK1_DynSyn")})

    def test_surround_fibres_reach_only_sg76(self):
        m = self.m
        for k in m.afferent_rows:
            if FIBRE_ROLE[int(m.table.frm[k])] == "surround":
                self.assertEqual(post_cell(m.ncs[k]), "SG76")

    def test_abeta_reach_sg75_and_wdr_only(self):
        m = self.m
        targets = {post_cell(m.ncs[k]) for k in m.afferent_rows if FIBRE_ROLE[int(m.table.frm[k])] == "abeta"}
        self.assertEqual(targets, {"SG75", "WDR"})

    def test_recorders(self):
        assert_recorder(self, self.m, "WDR", "WDR")
        assert_recorder(self, self.m, "SG75", "SG75")
        assert_recorder(self, self.m, "EX", "EX")

    def test_shifted_set_is_the_four_wdr_inhibitory_synapses(self):
        m = self.m
        shifted = m.wdr_inhibitory_synapses()
        assert_shifted_set(self, m, shifted)
        # which table rows drive them
        rows = sorted(k for k, nc in enumerate(m.ncs) if any(nc.syn() == s for s in shifted))
        self.assertEqual(rows, [286, 287, 289, 290])

    def test_shift_changes_exactly_those_synapses(self):
        m = self.m
        ex_inh = [s for s in m.ex.synlist if s.hname().startswith("GABAa_DynSyn")]
        self.assertEqual(len(ex_inh), 4)
        before = {}
        for c in m.cells.values():
            for i, s in enumerate(c.synlist):
                before[(c.label, i)] = float(s.e)
        m.set_shift(20.0)
        after = {}
        for c in m.cells.values():
            for i, s in enumerate(c.synlist):
                after[(c.label, i)] = float(s.e)
        changed = sorted(k for k in before if before[k] != after[k])
        self.assertEqual(len(changed), 4, changed)
        self.assertTrue(all(c == "WDR" for c, _ in changed))
        for k in changed:
            self.assertAlmostEqual(after[k], -50.0)
        for s in ex_inh:
            self.assertAlmostEqual(float(s.e), -70.0)
        m.set_shift(0.0)
        for k in changed:
            self.assertAlmostEqual(float(m.cells[k[0]].synlist[k[1]].e), -70.0)

    def test_weight_groups_partition_known_rows(self):
        m = self.m
        rows = [r for g in dm.GROUP_ROWS.values() for r in g]
        self.assertEqual(len(rows), len(set(rows)))
        # each group touches only the intended cells
        for g, rs in dm.GROUP_ROWS.items():
            tgts = {post_cell(m.ncs[r]) for r in rs}
            expect = {"abeta_wdr": {"WDR"}, "abeta_sg": {"SG75"}, "sg_wdr": {"WDR"}, "sg_ex": {"EX"},
                      "c_ex": {"EX"}, "nk1": {"EX", "WDR"}, "ex_wdr": {"WDR"}, "adelta_wdr": {"WDR"},
                      "surround_out": {"EX", "WDR"}}[g]
            self.assertEqual(tgts, expect, g)

    def test_event_delivery_time(self):
        """An event queued with NetCon.event(t) reaches its synapse at t (the NetCon delay is
        not added); a tiny 12 ms run with one event, not a result."""
        m = self.m
        k = 15   # Abeta -> WDR AMPA
        syn = m.ncs[k].syn()
        g = dm.h.Vector()
        g.record(syn._ref_g)
        tv = dm.h.Vector()
        tv.record(dm.h._ref_t)
        m.run({k: np.array([5.0])}, tstop=12.0, dt=0.025)
        gv, t = np.array(g), np.array(tv)
        first = t[np.nonzero(gv > 0)[0][0]]
        self.assertGreaterEqual(first, 5.0 - 1e-9)
        self.assertLess(first, 5.0 + 0.2)


class Mutations(unittest.TestCase):
    """The helpers above must FAIL on a wrong site / wrong set (run with python -B)."""

    @classmethod
    def setUpClass(cls):
        cls.m = shared_model()

    def test_recorder_on_hillock_fails(self):
        m = self.m
        r = m.rec["WDR"]
        saved = dict(r)
        try:
            vec = dm.h.Vector()
            nc = dm.h.NetCon(m.wdr.hillock(0.5)._ref_v, None, sec=m.wdr.hillock)
            r.update(nc=nc, section=m.wdr.hillock, x=0.5)
            with self.assertRaises(AssertionError):
                assert_recorder(self, m, "WDR", "WDR")
        finally:
            r.update(saved)

    def test_recorder_on_wrong_cell_fails(self):
        m = self.m
        r = m.rec["WDR"]
        saved = dict(r)
        try:
            nc = dm.h.NetCon(m.ex.soma(0.5)._ref_v, None, sec=m.ex.soma)
            r.update(nc=nc, section=m.ex.soma, x=0.5)
            with self.assertRaises(AssertionError):
                assert_recorder(self, m, "WDR", "WDR")
        finally:
            r.update(saved)

    def test_shifted_set_on_ex_fails(self):
        m = self.m
        wrong = [s for s in m.ex.synlist if s.hname().startswith("GABAa_DynSyn")]
        with self.assertRaises(AssertionError):
            assert_shifted_set(self, m, wrong)

    def test_shifted_set_missing_glycine_fails(self):
        m = self.m
        wrong = [s for s in m.wdr_inhibitory_synapses() if s.hname().startswith("GABAa_DynSyn")]
        wrong = wrong + [m.wdr.synlist[0]]   # an AMPA synapse in place of the glycine one
        with self.assertRaises(AssertionError):
            assert_shifted_set(self, m, wrong)


if __name__ == "__main__":
    unittest.main()
