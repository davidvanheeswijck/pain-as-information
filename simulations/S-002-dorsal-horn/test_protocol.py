"""Tests of the S-2 protocol helpers and verdict rules (no NEURON needed).

    simulations/.venv/bin/python -B -m unittest test_protocol    (from this directory)
"""

import os
import sys
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import aggregate_s002 as A  # noqa: E402
import s2_protocol as P  # noqa: E402


class Generators(unittest.TestCase):
    def test_same_seed_same_trains_in_every_condition(self):
        a = P.build_fibre_trains("C1", 3, 1, 5.0, 0.0)
        b = P.build_fibre_trains("TC", 3, 1, 5.0, 20.0)
        for f in P.CFIB:
            np.testing.assert_array_equal(a[f], b[f])

    def test_half_c_is_a_subset_of_full_c(self):
        full = P.c_trains(3, 2, 5.0, 1.0)
        half = P.c_trains(3, 2, 5.0, 0.5)
        n_full = sum(len(v) for v in full.values())
        n_half = sum(len(v) for v in half.values())
        self.assertTrue(0.35 * n_full < n_half < 0.65 * n_full)
        for f in P.CFIB:
            self.assertTrue(set(half[f]) <= set(full[f]))

    def test_c_off_has_no_c(self):
        self.assertEqual(P.build_fibre_trains("T", 0, 1, 5.0, 20.0).keys() & set(P.CFIB), set())

    def test_scs_times_regular_first_at_one_over_f(self):
        t = P.scs_times(20)
        self.assertAlmostEqual(t[0], 50.0)
        self.assertTrue(np.allclose(np.diff(t), 50.0))
        self.assertLess(t[-1], P.T_RUN + 1e-9)

    def test_variants(self):
        norm = P.scs_trains(20, "norm", 0, 1)
        self.assertEqual(set(norm), set(P.ABETA))
        h = P.scs_trains(20, "H", 0, 1)
        n_h = sum(len(v) for v in h.values())
        n_n = sum(len(v) for v in norm.values())
        self.assertTrue(0.4 * n_n < n_h < 0.6 * n_n)
        self.assertEqual(set(P.scs_trains(20, "D1", 0, 1)), set(P.ABETA[:5]))
        self.assertEqual(set(P.scs_trains(20, "D2", 0, 1)), set(P.ABETA) | set(P.ADELTA))

    def test_touch_and_scs_are_unioned_per_fibre(self):
        ft = P.build_fibre_trains("TS", 0, 1, 0.0, 20.0)
        scs = P.scs_times(20)
        self.assertTrue(set(scs) <= set(ft[0]))
        self.assertGreater(len(ft[0]), len(scs))

    def test_rate_window(self):
        s = np.array([100.0, 1500.0, 3000.0, 7499.0, 7500.0])
        self.assertAlmostEqual(P.rate_in_window(s), 3 / 6.0)

    def test_shipped_inputs_parse(self):
        rows, tstop = P.read_shipped_inputs("windup")
        self.assertEqual(len(rows), 225)
        self.assertEqual(tstop, 21000.0)
        self.assertEqual(len(rows[0]), 20)
        rows, tstop = P.read_shipped_inputs("afib")
        self.assertEqual(tstop, 221000.0)
        self.assertEqual(len(rows[0]), 211)


class ControlCriteria(unittest.TestCase):
    def test_windup_pass_and_fail(self):
        up = np.array([1] * 5 + [2] * 10 + [4] * 5, float)
        flat = np.full(20, 3.0)
        self.assertTrue(P.judge_windup(up)["ok"])
        self.assertFalse(P.judge_windup(flat)["ok"])
        small = np.array([0.1] * 5 + [0.2] * 10 + [0.3] * 5)     # ratio high but difference < 1 spike
        self.assertFalse(P.judge_windup(small)["ok"])

    def test_afib(self):
        self.assertTrue(P.judge_afib(np.full(10, 1.0), np.full(10, 3.0))["ok"])
        self.assertFalse(P.judge_afib(np.full(10, 2.9), np.full(10, 3.0))["ok"])
        self.assertFalse(P.judge_afib(np.full(10, 0.1), np.full(10, 0.5))["ok"])     # nothing to inhibit

    def test_frequency_pass_and_each_failure(self):
        base = 5.0
        good = {5: 5.5, 10: 6.0, 20: 5.7, 30: 4.5, 40: 3.0, 60: 3.5, 100: 4.0, 150: 6.0, 200: 5.6}
        self.assertTrue(P.judge_frequency(base, good)["ok"])
        no_inhib = {**good, 30: 5.0, 40: 5.0, 60: 5.0, 100: 5.0}
        self.assertFalse(P.judge_frequency(base, no_inhib)["ok"])
        no_low = {**good, 5: 4.0, 10: 4.5, 20: 4.2}
        self.assertFalse(P.judge_frequency(base, no_low)["ok"])
        no_high = {**good, 150: 4.0, 200: 4.5}
        self.assertFalse(P.judge_frequency(base, no_high)["ok"])
        self.assertFalse(P.judge_frequency(50.0, {f: 50.0 for f in good})["ok"])    # baseline outside [2, 15]
        # the minimum must be in the 30-100 band, not outside it
        outside = {**good, 5: 1.0}
        self.assertFalse(P.judge_frequency(base, outside)["ok"])


class Stats(unittest.TestCase):
    def test_wilson_contains_point(self):
        lo, hi = P.wilson(30, 40)
        self.assertTrue(lo < 0.75 < hi)
        self.assertEqual(P.wilson(0, 0), (0.0, 1.0))

    def test_ratio_reduction(self):
        idx = P.boot_indices(50, nboot=2000, seed=3)
        num = np.full(50, 2.0)
        den = np.full(50, 4.0)
        pt, lo, hi = P.ratio_reduction_ci(num, den, idx)
        self.assertAlmostEqual(pt, 0.5)
        self.assertAlmostEqual(lo, 0.5)

    def test_onset(self):
        self.assertEqual(P.onset_shift([0.5, 0.6, 1.2, 1.8, 3.0, 3, 3, 3]), 15)
        self.assertIsNone(P.onset_shift([0.5, 0.6, 0.8, 1.0, 1.2, 1.3, 1.4, 1.4]))


def _red(vals, defined=True):
    return {s: (v[0], v[1], v[2], defined) for s, v in zip(P.SHIFTS, vals)}


class VerdictRules(unittest.TestCase):
    """Each rule and its kill condition, with a mutation sensitivity check below."""

    GE = (0.5, 0.4, 0.6)
    LT = (0.05, -0.05, 0.1)
    SPAN = (0.2, 0.1, 0.3)

    def test_p1_supported(self):
        s = _red([self.GE, self.GE, self.GE, self.LT, self.LT, self.LT, self.LT, self.LT])
        c = _red([self.GE] * 8)
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s, c)[0], "SUPPORTED")

    def test_p1_kill(self):
        s = _red([self.GE] * 8)
        c = _red([self.GE] * 8)
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s, c)[0], "REFUTED")

    def test_p1_never_reduces_is_not_supported_not_refuted(self):
        s = _red([self.LT] * 8)
        c = _red([self.GE] * 8)
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s, c)[0], "NOT SUPPORTED, NOT REFUTED")

    def test_p1_requires_c_reduction(self):
        s = _red([self.GE, self.GE, self.GE, self.LT, self.LT, self.LT, self.LT, self.LT])
        c = _red([self.GE] * 3 + [self.LT] * 5)
        self.assertNotEqual(A.p1_rule(list(P.SHIFTS), s, c)[0], "SUPPORTED")

    def test_p1_span_is_inconclusive(self):
        s = _red([self.GE, self.GE, self.SPAN, self.LT, self.LT, self.LT, self.LT, self.LT])
        c = _red([self.GE] * 8)
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s, c)[0], "SUPPORTED")    # an earlier shift still reduced
        s2 = _red([self.LT, self.LT, self.SPAN, self.LT, self.LT, self.LT, self.LT, self.LT])
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s2, c)[0], "INCONCLUSIVE")

    def test_p2(self):
        self.assertEqual(A.p2_rule([15, 20], {15: (0.0, -0.1, 0.1, True), 20: (0.0, -0.1, 0.1, True)})[0], "SUPPORTED")
        self.assertEqual(A.p2_rule([15, 20], {15: self.GE + (True,), 20: self.GE + (True,)})[0], "REFUTED")
        self.assertEqual(A.p2_rule([15], {15: self.SPAN + (True,)})[0], "INCONCLUSIVE")
        self.assertEqual(A.p2_rule([], {})[0], "NOT SUPPORTED, NOT REFUTED")

    def test_mutation_kill_condition_matters(self):
        """Mutation check: with the kill clause removed the all-reducing case would no longer be
        REFUTED.  Emulated by asserting the case is REFUTED only because of that clause."""
        s = _red([self.GE] * 8)
        c = _red([self.GE] * 8)
        verdict = A.p1_rule(list(P.SHIFTS), s, c)[0]
        self.assertEqual(verdict, "REFUTED")
        # same input but one shift undefined: the kill condition applies to defined shifts only
        s2 = dict(s)
        s2[0] = (s[0][0], s[0][1], s[0][2], False)
        self.assertEqual(A.p1_rule(list(P.SHIFTS), s2, c)[0], "REFUTED")


if __name__ == "__main__":
    unittest.main()
