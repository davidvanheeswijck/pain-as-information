"""Unit tests for the S-1b gates and held-out rules (no NEURON needed).

    simulations/.venv/bin/python -B -m unittest test_aggregate    (from this directory)
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import aggregate_s001b as A  # noqa: E402


class Gates(unittest.TestCase):
    def test_all_gates_pass_gives_the_rules_verdict(self):
        d = A.decide(True, True, "pass", True, "SUPPORTED", "REFUTED", True)
        self.assertEqual((d["P1"], d["P2"], d["gates_ok"]), ("SUPPORTED", "REFUTED", True))

    def test_each_gate_failing_gives_no_verdict_and_no_rule_word(self):
        for args in ((False, True, "pass", True), (True, False, "pass", True),
                     (True, True, "fail", True), (True, True, "inconclusive", True),
                     (True, True, "pass", False)):
            d = A.decide(*args, "SUPPORTED", "REFUTED", True)
            self.assertFalse(d["gates_ok"])
            for k in ("P1", "P2"):
                self.assertTrue(d[k].startswith("NO VERDICT"), d[k])
                self.assertNotIn("SUPPORTED", d[k])
                self.assertNotIn("REFUTED", d[k])

    def test_failed_convergence_is_inconclusive(self):
        d = A.decide(True, True, "pass", True, "SUPPORTED", "SUPPORTED", False)
        self.assertTrue(d["P1"].startswith("INCONCLUSIVE"))

    def test_cond_line_has_no_bold_when_gates_fail(self):
        R = dict(P1=dict(verdict_if_gates_pass="SUPPORTED"),
                 verdicts=dict(gates_ok=False, reasons=["G3 held-out validation fail"], P1="NO VERDICT (x)"))
        line = A.cond_line("P1", R)
        self.assertNotIn("**", line)
        self.assertIn("NOT a verdict", line)


class HeldOut(unittest.TestCase):
    def test_v1_needs_both_frequency_features(self):
        self.assertEqual(A.v1_state(190, 200, 190, 200), "pass")
        self.assertEqual(A.v1_state(190, 200, 5, 200), "fail")     # 2 Hz also amplified: fails
        self.assertEqual(A.v1_state(5, 200, 190, 200), "fail")     # 4 Hz not amplified: fails
        self.assertEqual(A.v1_state(105, 200, 190, 200), "inconclusive")
        self.assertEqual(A.v1_state(0, 0, 0, 0), "inconclusive")

    def test_v2_threshold(self):
        self.assertEqual(A.v2_state(200, 200), "pass")
        self.assertEqual(A.v2_state(150, 200), "fail")
        self.assertEqual(A.v2_state(0, 0), "inconclusive")
        self.assertEqual(A.v2_state(178, 200), "inconclusive")     # 0.89: below 0.90, upper bound above 0.85


if __name__ == "__main__":
    unittest.main()
