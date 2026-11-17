"""Unit tests for the S-1b search machinery (no NEURON needed).

    simulations/.venv/bin/python -B -m unittest test_tuning    (from this directory)
"""

import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tuning as T  # noqa: E402


class Lhs(unittest.TestCase):
    def test_one_point_per_stratum(self):
        u = T.lhs_unit(50, 5, np.random.default_rng(1))
        for j in range(5):
            self.assertEqual(sorted(np.floor(u[:, j] * 50).astype(int).tolist()), list(range(50)))

    def test_round1_in_range_and_reproducible(self):
        a, b = T.round1_candidates(), T.round1_candidates()
        self.assertEqual(a, b)
        self.assertEqual(len(a), T.N1)
        for p in a:
            for name, lo, hi, _ in T.SPACE:
                self.assertTrue(lo <= p[name] <= hi, (name, p[name]))
        frac = np.mean([p["sk_stem"] for p in a])
        self.assertTrue(0.35 < frac < 0.65)

    def test_round2_inside_box_and_global_range(self):
        c = T.round1_candidates()[0]
        out = T.round2_candidates([c, c, c])
        self.assertEqual(len(out), T.N2)
        box = T.local_box(c)
        for p in out:
            self.assertEqual(p["sk_stem"], c["sk_stem"])
            for name, lo, hi, _ in T.SPACE:
                self.assertTrue(lo - 1e-12 <= p[name] <= hi + 1e-12)
                self.assertTrue(box[name][0] - 1e-12 <= p[name] <= box[name][1] + 1e-12)


class Scoring(unittest.TestCase):
    OK = dict(na_k=110.0, kcnq=30.0, sk=6.0)

    def flags(self, fe, fl, tb_ms):
        return T.block_flags(dict(F_early=fe, F_late=fl, t_block_ms=tb_ms))

    def test_meets_all(self):
        f = self.flags(0.2, 0.95, 200.0 + 8000.0)
        self.assertTrue(T.meets_targets(self.OK, f))
        J, d = T.score_J(self.OK, f)
        self.assertAlmostEqual(J, 0.0, places=9)

    def test_each_target_is_necessary(self):
        good = self.flags(0.2, 0.95, 8200.0)
        for bad in (dict(self.OK, na_k=80.0), dict(self.OK, kcnq=40.0), dict(self.OK, sk=8.0)):
            self.assertFalse(T.meets_targets(bad, good))
        self.assertFalse(T.meets_targets(self.OK, self.flags(0.6, 0.95, 8200.0)))   # B1
        self.assertFalse(T.meets_targets(self.OK, self.flags(0.2, 0.7, 8200.0)))    # B2
        self.assertFalse(T.meets_targets(self.OK, self.flags(0.2, 0.95, 200.0 + 560.0)))  # B3 too early
        self.assertFalse(T.meets_targets(self.OK, self.flags(0.2, 0.95, 200.0 + 25000.0)))  # B3 too late
        self.assertFalse(T.meets_targets(self.OK, self.flags(0.2, 0.95, None)))     # no block

    def test_band_edges(self):
        self.assertTrue(T.in_band("sk", 7.5) and T.in_band("sk", 4.5))
        self.assertFalse(T.in_band("sk", 7.51) or T.in_band("sk", 4.49))
        self.assertAlmostEqual(T.d_term(7.5, 6.0), 1.0, places=9)

    def test_J_is_monotone_in_shortfall_and_ignores_nothing_else(self):
        a = T.score_J(self.OK, self.flags(0.2, 0.95, 8200.0))[0]
        b = T.score_J(self.OK, self.flags(0.9, 0.95, 8200.0))[0]
        c = T.score_J(self.OK, self.flags(0.2, 0.95, 560.0 + 200.0))[0]
        self.assertGreater(b, a)
        self.assertGreater(c, a)

    def test_missing_values_are_worst_case_not_crashes(self):
        f = self.flags(None, None, None)
        self.assertFalse(f["B1"] or f["B2"] or f["B3"])
        J, d = T.score_J(dict(na_k=0.0, kcnq=None, sk=0.0), f)
        self.assertGreater(J, 3 * T.D_CAP ** 2 - 1e-9)


if __name__ == "__main__":
    unittest.main()
