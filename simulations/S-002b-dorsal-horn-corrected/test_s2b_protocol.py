"""Pure-numpy tests of the S-2b protocol, control judges and verdict logic (no NEURON).

    simulations/.venv/bin/python -B -m unittest test_s2b_protocol    (from this directory)
"""

import os
import sys
import unittest

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import aggregate_s002b as AG  # noqa: E402
import s2b_protocol as P  # noqa: E402


def from_vector():
    with open(os.path.join(P.DATA, "FromVector.txt")) as fh:
        return np.array([int(x) for x in fh.read().split()])


class Generators(unittest.TestCase):
    def test_run_constants_are_the_registered_ones(self):
        self.assertEqual((P.T_RUN, P.T_SCORE0, P.T_SCORE1), (5500.0, 1500.0, 5500.0))
        self.assertEqual(P.SEEDS, (1, 2))
        self.assertEqual(P.SCS_PRIMARY_HZ, 40)
        self.assertEqual(P.RC_GRID[0], 0.5)
        self.assertEqual(P.RC_GRID[-1], 2.5)
        self.assertEqual(len(P.RC_GRID), 17)

    def test_pairing_across_conditions(self):
        a = P.build_fibre_trains("T", 3, 1, 1.0)
        b = P.build_fibre_trains("TC", 3, 1, 1.0)
        c = P.build_fibre_trains("TCS", 3, 1, 1.0)
        for f in P.ABETA:
            np.testing.assert_array_equal(a[f], b[f])
            np.testing.assert_array_equal(a[f], c[f])
        for f in P.CFIB:
            np.testing.assert_array_equal(b[f], c[f])

    def test_c_thinning_is_a_subset(self):
        full, half = P.c_trains(2, 1, 1.5, 1.0), P.c_trains(2, 1, 1.5, 0.5)
        n_full = sum(len(t) for t in full.values())
        n_half = sum(len(t) for t in half.values())
        self.assertTrue(0.35 * n_full < n_half < 0.65 * n_full)
        for f in P.CFIB:
            self.assertTrue(set(half[f]) <= set(full[f]))

    def test_stimulation_is_on_the_surround_fibres_only(self):
        tr = P.scs_trains(40, "norm", 0, 1)
        self.assertEqual(sorted(tr), list(range(30, 45)))
        self.assertEqual(len(tr[30]), int(P.T_RUN // 25.0))
        self.assertAlmostEqual(float(tr[30][0]), 25.0)
        self.assertFalse(set(tr) & set(P.ABETA))

    def test_lead_drift_and_habituation_variants(self):
        norm = P.scs_trains(40, "norm", 0, 1)
        h = P.scs_trains(40, "H", 0, 1)
        self.assertEqual(sorted(h), sorted(norm))
        frac = np.mean([len(h[f]) / len(norm[f]) for f in h])
        self.assertTrue(0.4 < frac < 0.6)
        for f in h:
            self.assertTrue(set(h[f]) <= set(norm[f]))
        self.assertEqual(len(P.scs_trains(40, "D1", 0, 1)), 5)
        self.assertEqual(sorted(P.scs_trains(40, "D2", 0, 1)), sorted(list(P.SURROUND) + list(P.ADELTA)))

    def test_touch_rate_is_the_shipped_foreman_abeta_background(self):
        rows, tstop = P.base.read_shipped_inputs("foreman")
        frm = from_vector()
        by = {}
        for k, v in rows.items():
            by.setdefault(int(frm[k]), v)
        mean_hz = float(np.mean([len(by[f]) for f in P.ABETA])) / tstop * 1000.0
        self.assertAlmostEqual(mean_hz, P.TOUCH_HZ, delta=0.1)
        # the shipped stimulation is on the surround fibres, at 1 Hz, with one dummy event beyond the run
        for f in P.SURROUND:
            real = by[f][by[f] < 1e8]
            self.assertEqual(len(real), 25)
            self.assertAlmostEqual(float(np.median(np.diff(real))), 1000.0, delta=0.5)

    def test_shipped_afib_surround_events_are_dummies(self):
        rows, _ = P.base.read_shipped_inputs("afib")
        frm = from_vector()
        for k, v in rows.items():
            if 30 <= int(frm[k]) < 45:
                self.assertTrue(np.all(v >= 1e8))

    def test_scoring_window(self):
        sp = np.array([1000.0, 1500.0, 3000.0, 5499.0, 5500.0])
        self.assertAlmostEqual(P.rate_in_window(sp), 3 / 4.0)

    def test_candidate_factors(self):
        w0, c0 = P.sample_factors(0, ["a", "b"], (0.5, 2.0), {"x": (0.5, 2.0)})
        self.assertEqual(w0, {"a": 1.0, "b": 1.0})
        w, c = P.sample_factors(7, ["a", "b"], (0.5, 2.0), {"x": (0.8, 1.25)})
        w2, c2 = P.sample_factors(7, ["a", "b"], (0.5, 2.0), {"x": (0.8, 1.25)})
        self.assertEqual((w, c), (w2, c2))
        self.assertTrue(all(0.5 <= v <= 2.0 for v in w.values()) and 0.8 <= c["x"] <= 1.25)


class Control(unittest.TestCase):
    def test_windup_judge(self):
        up = np.array([1.0] * 5 + [2.0] * 10 + [4.0] * 5)
        self.assertTrue(P.judge_windup(up)["ok"])
        self.assertFalse(P.judge_windup(np.full(20, 3.0))["ok"])

    def test_afib_criterion_is_on_abeta_only(self):
        c = np.full(10, 11.0)
        # A-beta reduces to 8; A-delta and all-A excite: the OLD (S-2) criterion on all A fails, the new passes
        r = P.judge_afib_beta(c, np.full(10, 8.0), np.full(10, 23.0), np.full(10, 19.0))
        self.assertTrue(r["ok"])
        self.assertAlmostEqual(r["ratio_abeta"], 8 / 11)
        self.assertGreater(r["ratio_all"], 0.8)
        self.assertFalse(P.judge_afib_beta(c, np.full(10, 10.0))["ok"])
        self.assertFalse(P.judge_afib_beta(np.full(10, 0.5), np.zeros(10))["ok"])   # C only below 1 spike per cycle
        # the Adelta-only condition does not enter the criterion
        self.assertTrue(P.judge_afib_beta(c, np.full(10, 8.0), np.full(10, 0.0))["ok"])

    def test_drive_match_bisection(self):
        def rate(i):   # monotone, steep like the registered curve
            return [0.1, 0.4, 0.8, 0.9, 2.1, 3.5, 7.5, 13.5, 22.9][min(i, 8)] if i < 9 else 30.0 + i
        rc, r, tried, why = P.match_rc(rate)
        self.assertEqual(rc, P.RC_GRID[4])
        self.assertEqual(why, "ok")
        self.assertLess(len(tried), 8)
        rc, r, _, why = P.match_rc(lambda i: 0.0)
        self.assertIsNone(rc)
        self.assertIn("unreachable", why)
        rc, r, _, why = P.match_rc(lambda i: 0.0 if i < 5 else 40.0)
        self.assertIsNone(rc)
        self.assertEqual(why, "jumped over the band")

    def test_frequency_judge(self):
        base = 5.0
        win = {5: 1.3, 10: 1.2, 20: 1.15, 30: 0.7, 40: 0.5, 60: 0.4, 100: 0.6, 150: 1.4, 200: 1.6}
        ok = P.judge_frequency(base, {f: base * v for f, v in win.items()})
        self.assertTrue(ok["ok"] and ok["evaluable"])
        flat = P.judge_frequency(base, {f: base * 1.5 for f in win})        # excites everywhere
        self.assertFalse(flat["ok"])
        self.assertTrue(flat["evaluable"])
        low = P.judge_frequency(0.5, {f: 1.0 for f in win})
        self.assertFalse(low["ok"] or low["evaluable"])
        no_exc = dict(win)
        no_exc.update({150: 0.9, 200: 0.9})
        self.assertFalse(P.judge_frequency(base, {f: base * v for f, v in no_exc.items()})["ok"])

    def test_onset(self):
        r = [1.0, 1.5, 2.0, 3.5, 20.0]
        self.assertEqual(P.onset_shift(r, (0, 2.5, 5, 7.5, 10)), 7.5)
        self.assertIsNone(P.onset_shift([1.0, 1.5, 2.0], (0, 5, 10)))


class Verdicts(unittest.TestCase):
    def test_klass(self):
        self.assertEqual(AG.klass(0.25, 0.4), "R")
        self.assertEqual(AG.klass(-0.1, 0.19), "N")
        self.assertEqual(AG.klass(0.1, 0.3), "S")
        self.assertEqual(AG.klass(float("nan"), float("nan")), "-")

    def test_p0(self):
        self.assertEqual(AG.decide_p0(2.5, 7.5, 200), "SUPPORTED")
        self.assertEqual(AG.decide_p0(15, 20, 200), "REFUTED")
        self.assertEqual(AG.decide_p0(7.5, 15, 200), "INCONCLUSIVE")
        self.assertEqual(AG.decide_p0(2.5, 7.5, 150), "INCONCLUSIVE")   # below the floor

    def test_p1(self):
        sup = AG.decide_p1(list("RRNNNNNN"), list("RRRRRRRR"))
        self.assertEqual(sup, "SUPPORTED")
        self.assertEqual(AG.decide_p1(list("RRRRRRRR"), list("RRRRRRRR")), "REFUTED")
        # never reduced: clause (i) fails
        self.assertEqual(AG.decide_p1(list("NNNNNNNN"), list("RRRRRRRR")), "NOT SUPPORTED, NOT REFUTED")
        # reduced before, stops, but C does not reduce C-driven output beyond the stop
        self.assertEqual(AG.decide_p1(list("RRNNNNNN"), list("RRRNNNNN")), "NOT SUPPORTED, NOT REFUTED")
        # a spanning class at a deciding shift (the only possible "reduced before" cell, or a C-reduction cell)
        self.assertEqual(AG.decide_p1(list("SNNNNNNN"), list("RRRRRRRR")), "INCONCLUSIVE")
        self.assertEqual(AG.decide_p1(list("RRNNNNNN"), list("RRRRRRRS")), "INCONCLUSIVE")
        # a spanning class that cannot decide anything
        self.assertEqual(AG.decide_p1(list("NNNNNNNS"), list("RRRRRRRR")), "NOT SUPPORTED, NOT REFUTED")

    def test_p2(self):
        self.assertEqual(AG.decide_p2(list("NNNN")), "SUPPORTED")
        self.assertEqual(AG.decide_p2(list("RRRR")), "REFUTED")
        self.assertEqual(AG.decide_p2(list("NRNN")), "NOT SUPPORTED, NOT REFUTED")
        self.assertEqual(AG.decide_p2(list("NSNN")), "INCONCLUSIVE")
        self.assertEqual(AG.decide_p2(["N"]), "INCONCLUSIVE")

    def test_p3(self):
        self.assertEqual(AG.decide_p3((38, 40), {"H": (2, 40), "D1": (3, 40), "D2": (5, 40)}), "SUPPORTED")
        self.assertEqual(AG.decide_p3((3, 40), {"H": (2, 40), "D1": (3, 40), "D2": (5, 40)}), "REFUTED")
        self.assertEqual(AG.decide_p3((24, 40), {"H": (2, 40), "D1": (3, 40), "D2": (5, 40)}), "INCONCLUSIVE")
        self.assertEqual(AG.decide_p3((39, 40), {"H": (38, 40), "D1": (3, 40), "D2": (5, 40)}), "NOT SUPPORTED, NOT REFUTED")
        self.assertEqual(AG.decide_p3((19, 20), {"H": (2, 20), "D1": (3, 20), "D2": (5, 20)}), "INCONCLUSIVE")   # floor

    def test_convergence_rule(self):
        def rec(d):
            R = {}
            for c in ("C1", "T", "TS"):
                for s in (0, 20):
                    base = {"C1": 3.0, "T": 4.0 if s == 0 else 60.0, "TS": 2.0 if s == 0 else 55.0}[c]
                    R[f"{c}|{s}|{P.DT_MAIN}"] = base
                    R[f"{c}|{s}|{P.DT_PUB}"] = base + d
            return dict(R=R)
        ok = AG.convergence([rec(0.2) for _ in range(10)])
        self.assertTrue(ok["passed"])
        bad = AG.convergence([rec(3.0) for _ in range(10)])
        self.assertFalse(bad["passed"])
        few = AG.convergence([rec(0.2) for _ in range(3)])
        self.assertFalse(few["passed"])


if __name__ == "__main__":
    unittest.main()
