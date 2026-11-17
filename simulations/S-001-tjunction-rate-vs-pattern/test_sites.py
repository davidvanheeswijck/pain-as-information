"""Recording-site geometry test for S-1 (Amendment H).

Asserts, from path distance along the real connections (h.distance), that each
named site sits where its role says, for both the C-neuron and the A-beta
comparator:  soma  <  stem_mid (stimulus)  <  stem_pre (junction side)  <  tj,
peri_pre on the peripheral side of tj, central on the central side of tj.
The distance is measured from the soma, so a stem_pre on the soma end of the stem
(the run-1 defect) fails the ordering.

    simulations/.venv/bin/python -m unittest test_sites    (from this directory)
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tjmodel  # noqa: E402


def dist_from_soma(cell, seg):
    h = tjmodel.h
    h.distance(0, cell.soma(0.5))
    return h.distance(1, seg)


class SiteGeometry(unittest.TestCase):
    def check(self, cell):
        s = cell.sites()
        d = {k: dist_from_soma(cell, seg) for k, seg in s.items()}
        # the stimulus is at stem_mid; the junction-side stem site is strictly
        # farther from the soma than the stimulus, and nearer the T-junction
        self.assertLess(d["soma"], d["stem_mid"])
        self.assertLess(d["stem_mid"], d["stem_pre"], "stem_pre must be on the junction side of the stimulus")
        self.assertLess(d["stem_pre"], d["tj"], "stem_pre must be before the T-junction")
        # both branch recording sites are beyond the junction
        self.assertGreater(d["peri_pre"], d["tj"] - 1e-9)
        self.assertGreater(d["central"], d["tj"] - 1e-9)
        self.assertGreater(d["peri_dist"], d["peri_pre"])

    def test_c_neuron(self):
        self.check(tjmodel.CNeuron())

    def test_a_beta(self):
        self.check(tjmodel.ANeuron())

    def test_both_models_agree_on_role(self):
        # stem_pre is the junction side in both, whichever x that is
        xs = []
        for cls in (tjmodel.CNeuron, tjmodel.ANeuron):
            cell = cls()
            xs.append(cell.sites()["stem_pre"].x)
        self.assertEqual(xs, [0.1, 0.9])


if __name__ == "__main__":
    unittest.main()
