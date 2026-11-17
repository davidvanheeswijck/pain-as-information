"""Recording-site geometry test for S-1b, for every model class and variant used.

S-1b imports S-1's `tjmodel` unchanged (`CNeuron`, `ANeuron`) and builds C-neurons
with the search's parameters, including SK in the stem (`sk_stem=True`) and the
Na+Kdr and +KCNQ configurations.  Run 1 of S-1 recorded on the soma side of the
stimulus in the C-neuron (amendment H); the lesson is that every site comes from
topology and every model class has a geometry test with a mutation check.

Asserts, from path distance along the real connections (h.distance, measured from
the soma), that each named site sits where its role says:
soma < stem_mid (stimulus) < stem_pre (junction side) < tj, peri_pre and central
on the far side of tj.  The last test is the mutation check: with the site chosen
the wrong way round (as in run 1) the same check must FAIL.

    simulations/.venv/bin/python -B -m unittest test_sites    (from this directory)
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
S1 = os.path.join(os.path.dirname(HERE), "S-001-tjunction-rate-vs-pattern")
sys.path.insert(0, S1)
sys.path.insert(0, HERE)
import tjmodel  # noqa: E402  (S-1's module, imported unchanged)
import tuning  # noqa: E402


def dist_from_soma(cell, seg):
    h = tjmodel.h
    h.distance(0, cell.soma(0.5))
    return h.distance(1, seg)


def check(case, cell):
    s = cell.sites()
    d = {k: dist_from_soma(cell, seg) for k, seg in s.items()}
    case.assertLess(d["soma"], d["stem_mid"])
    case.assertLess(d["stem_mid"], d["stem_pre"], "stem_pre must be on the junction side of the stimulus")
    case.assertLess(d["stem_pre"], d["tj"], "stem_pre must be before the T-junction")
    case.assertGreater(d["peri_pre"], d["tj"] - 1e-9)
    case.assertGreater(d["central"], d["tj"] - 1e-9)
    case.assertGreater(d["peri_dist"], d["peri_pre"])


class SiteGeometry(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tjmodel.load_neuron()

    def test_c_neuron_default(self):
        check(self, tjmodel.CNeuron())

    def test_c_neuron_every_class_of_search_variant(self):
        base = tuning.round1_candidates(8)
        base[0]["sk_stem"], base[1]["sk_stem"] = False, True
        for p in base:
            check(self, tjmodel.CNeuron(**p))                         # SK configuration
            check(self, tjmodel.CNeuron(**dict(p, gsk=0.0)))          # +KCNQ/M configuration
            check(self, tjmodel.CNeuron(**dict(p, gsk=0.0, kcnq=0.0)))  # Na+Kdr configuration

    def test_a_beta(self):
        check(self, tjmodel.ANeuron())

    def test_both_models_agree_on_role(self):
        xs = [cls().sites()["stem_pre"].x for cls in (tjmodel.CNeuron, tjmodel.ANeuron)]
        self.assertEqual(xs, [0.1, 0.9])

    def test_mutation_wrong_side_site_fails_the_check(self):
        """Mutation check: choose the junction-side site backwards (the run-1 defect)
        and the geometry check must fail."""
        original = tjmodel.junction_side_stem_x
        tjmodel.junction_side_stem_x = lambda stem, tj_secs: 1.0 - original(stem, tj_secs)
        try:
            with self.assertRaises(AssertionError):
                check(self, tjmodel.CNeuron())
            with self.assertRaises(AssertionError):
                check(self, tjmodel.ANeuron())
        finally:
            tjmodel.junction_side_stem_x = original
        check(self, tjmodel.CNeuron())   # restored


if __name__ == "__main__":
    unittest.main()
