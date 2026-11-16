"""Tests for verdict.py. Standard library only.

Run from the repo root:  python3 -m unittest simulations/test_verdict.py

The committed-results tests re-derive the recorded verdicts from the committed
JSON; they do not re-run any simulation.
"""

import ast
import json
import re
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import verdict as vd  # noqa: E402

C008_MAIN = HERE / "C-008-interference-rejection" / "results" / "main" / "results.json"
C004_ENSEMBLE = (HERE / "C-004-velocity-beamforming" / "results"
                 / "sensor-realism" / "ensemble.json")


class DecideSmallN(unittest.TestCase):
    def test_single_seed_above_threshold_is_inconclusive(self):
        # The C-004 sensor-realism incident: one seed, ratio 1.03, threshold 1.0.
        label, reason = vd.decide([1.03], 1.0, above="OVERTURNED", below="SURVIVES")
        self.assertEqual(label, "INCONCLUSIVE")
        self.assertIn("1 seed", reason)

    def test_nine_seeds_is_still_inconclusive_ten_is_not(self):
        nine = [0.5 + 0.001 * i for i in range(9)]
        ten = [0.5 + 0.001 * i for i in range(10)]
        self.assertEqual(vd.decide(nine, 1.0)[0], "INCONCLUSIVE")
        self.assertEqual(vd.decide(ten, 1.0)[0], "BELOW")

    def test_min_n_is_overridable_by_the_caller(self):
        vals = [0.5, 0.52, 0.48]
        self.assertEqual(vd.decide(vals, 1.0)[0], "INCONCLUSIVE")
        self.assertEqual(vd.decide(vals, 1.0, min_n=3)[0], "BELOW")


class DecideCI(unittest.TestCase):
    def test_ci_spanning_threshold_is_inconclusive(self):
        vals = [0.8, 1.2, 0.9, 1.1, 1.0, 0.95, 1.05, 1.15, 0.85, 1.0, 0.9, 1.1]
        label, reason = vd.decide(vals, 1.0)
        self.assertEqual(label, "INCONCLUSIVE")
        self.assertIn("spans", reason)

    def test_clear_sides_use_the_callers_words(self):
        hi = [2.0 + 0.01 * i for i in range(12)]
        lo = [0.2 + 0.01 * i for i in range(12)]
        self.assertEqual(vd.decide(hi, 1.0, above="SURVIVES", below="REFUTED")[0], "SURVIVES")
        self.assertEqual(vd.decide(lo, 1.0, above="SURVIVES", below="REFUTED")[0], "REFUTED")

    def test_only_three_words_can_ever_come_out(self):
        for vals in ([1.03], [0.2] * 12, [2.0] * 12, [0.9, 1.1] * 6):
            label, _ = vd.decide(vals, 1.0, above="A", below="B")
            self.assertIn(label, {"A", "B", "INCONCLUSIVE"})


@unittest.skipUnless(C008_MAIN.exists(), "committed C-008 results not present")
class RecordedC008(unittest.TestCase):
    def setUp(self):
        self.res = json.loads(C008_MAIN.read_text())["results"]

    def test_grad1_c_main_run_is_refuted(self):
        vals = self.res["grad1:C"]["values"]
        self.assertEqual(len(vals), 18)
        label, _ = vd.decide(vals, 1.0, above="SURVIVES", below="REFUTED")
        self.assertEqual(label, "REFUTED")

    def test_grad2_c_main_run_is_refuted(self):
        label, _ = vd.decide(self.res["grad2:C"]["values"], 1.0,
                             above="SURVIVES", below="REFUTED")
        self.assertEqual(label, "REFUTED")

    def test_two_seed_subset_of_the_same_run_is_inconclusive(self):
        # The smoke-run failure mode: two seeds must never yield a verdict.
        label, _ = vd.decide(self.res["grad1:C"]["values"][:2], 1.0)
        self.assertEqual(label, "INCONCLUSIVE")


@unittest.skipUnless(C004_ENSEMBLE.exists(), "committed C-004 ensemble not present")
class RecordedC004(unittest.TestCase):
    def test_interference_ensemble_does_not_overturn(self):
        per_seed = json.loads(C004_ENSEMBLE.read_text())["per_seed"]
        self.assertEqual(len(per_seed), 18)
        for key in ("with_interference", "with_interference_and_notch"):
            vals = [r[key] for r in per_seed]
            label, _ = vd.decide(vals, 1.0, above="OVERTURNED", below="SURVIVES")
            self.assertEqual(label, "SURVIVES", key)
        # ...while seed 0 alone, the old single-seed verdict, is refused.
        seed0 = per_seed[0]["with_interference"]
        self.assertGreater(seed0, 1.0)
        self.assertEqual(vd.decide([seed0], 1.0, above="OVERTURNED", below="SURVIVES")[0],
                         "INCONCLUSIVE")


class NoUnguardedVerdictWords(unittest.TestCase):
    """Every upper-case verdict word in a simulation's string literals must sit
    inside a function that goes through verdict.decide (or tests its
    INCONCLUSIVE result). A bare print("OVERTURNED") in an unguarded function,
    or at module level, fails. Limit: a bare word added inside an already
    guarded function is not caught by this structural check."""

    WORDS = re.compile(r"OVERTURNED|REFUTED|SURVIVE")
    FILES = [
        HERE / "C-004-velocity-beamforming" / "simulate.py",
        HERE / "C-008-interference-rejection" / "simulate_c008.py",
    ]

    @staticmethod
    def _guarded(fn):
        return any(isinstance(n, ast.Attribute) and isinstance(n.value, ast.Name)
                   and n.value.id == "vd" and n.attr in ("decide", "INCONCLUSIVE")
                   for n in ast.walk(fn))

    def offenders(self, source, name="<src>"):
        tree = ast.parse(source, name)
        docstrings = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.Module, ast.FunctionDef, ast.ClassDef)):
                body = node.body
                if (body and isinstance(body[0], ast.Expr)
                        and isinstance(body[0].value, ast.Constant)):
                    docstrings.add(id(body[0].value))
        out = []

        def visit(node, guarded):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                guarded = guarded or self._guarded(node)
            if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                    and id(node) not in docstrings
                    and self.WORDS.search(node.value) and not guarded):
                out.append((node.lineno, node.value[:60]))
            for child in ast.iter_child_nodes(node):
                visit(child, guarded)

        visit(tree, False)
        return out

    def test_simulations_have_no_unguarded_verdict_words(self):
        for f in self.FILES:
            self.assertEqual(self.offenders(f.read_text(), str(f)), [], str(f))

    def test_the_check_catches_a_bare_verdict_print(self):
        src = self.FILES[0].read_text() + '\n\ndef _stray():\n    print("OVERTURNED")\n'
        self.assertTrue(self.offenders(src))
        self.assertTrue(self.offenders('print("CONJECTURE REFUTED")\n'))


if __name__ == "__main__":
    unittest.main()
