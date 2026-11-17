"""Tests for infogain.py. Standard library only, no network, no numpy.

Run from the repo root:
    python3 -m unittest simulations/S-003-generator-discrimination/test_infogain.py

Mutation check: `mutation_check.py` replaces log2 with the natural log in
`mutual_information`, and separately drops the division by the marginal, in a
temporary copy; both must make these fail.
"""

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import infogain as ig  # noqa: E402

UNIFORM4 = [0.25, 0.25, 0.25, 0.25]
ORACLE = [[1.0 if y == h else 0.0 for y in range(4)] for h in range(4)]
NOISE = [[0.2, 0.5, 0.3] for _ in range(4)]


class PositiveControl(unittest.TestCase):
    def test_oracle_returns_two_bits(self):
        self.assertAlmostEqual(ig.mutual_information(UNIFORM4, ORACLE), 2.0, places=12)

    def test_noise_returns_zero(self):
        self.assertAlmostEqual(ig.mutual_information(UNIFORM4, NOISE), 0.0, places=12)

    def test_oracle_returns_prior_entropy_for_any_prior(self):
        prior = [0.5, 0.25, 0.125, 0.125]  # entropy 1.75 bits by hand
        self.assertAlmostEqual(ig.mutual_information(prior, ORACLE), 1.75, places=12)

    def test_noise_adds_nothing_and_oracle_saturates(self):
        prior = [0.3, 0.25, 0.25, 0.2]
        weak = [[0.8, 0.2], [0.3, 0.7], [0.3, 0.7], [0.1, 0.9]]
        alone = ig.mutual_information(prior, weak)
        self.assertAlmostEqual(
            ig.mutual_information(prior, ig.joint_rows([weak, NOISE])), alone, places=12)
        self.assertAlmostEqual(
            ig.mutual_information(prior, ig.joint_rows([weak, ORACLE])),
            ig.entropy(prior), places=12)


class HandComputed(unittest.TestCase):
    def test_binary_symmetric_channel(self):
        # Two equally likely hypotheses, a test that is wrong a quarter of the
        # time. I = 1 - H(0.25). By hand: H(0.25) = 0.25*2 + 0.75*log2(4/3)
        # = 0.5 + 0.75*0.415037 = 0.811278, so I = 0.188722 bits.
        rows = [[0.75, 0.25], [0.25, 0.75]]
        self.assertAlmostEqual(ig.mutual_information([0.5, 0.5], rows), 0.188722, places=6)

    def test_asymmetric_two_by_two(self):
        # Rows (1, 0) and (0.5, 0.5). Marginal (0.75, 0.25), H(Y) = 0.811278;
        # H(Y|H) = 0.5*0 + 0.5*1 = 0.5; I = 0.311278 bits.
        rows = [[1.0, 0.0], [0.5, 0.5]]
        self.assertAlmostEqual(ig.mutual_information([0.5, 0.5], rows), 0.311278, places=6)

    def test_bits_not_nats(self):
        # A perfect binary test is worth exactly 1 bit (0.693 nats).
        rows = [[1.0, 0.0], [0.0, 1.0]]
        self.assertAlmostEqual(ig.mutual_information([0.5, 0.5], rows), 1.0, places=12)

    def test_identical_rows_are_not_separated(self):
        # Two hypotheses with the same row (the C-009 case) gain nothing
        # about each other, whatever the other hypotheses do.
        prior = [0.3, 0.25, 0.25, 0.2]
        rows = [[0.8, 0.2], [0.2, 0.8], [0.8, 0.2], [0.1, 0.9]]
        self.assertAlmostEqual(
            ig.pairwise_bayes_error(prior, rows, 0, 2), 0.25 / 0.55, places=12)
        self.assertAlmostEqual(ig.pairwise_bayes_error(prior, ORACLE, 0, 2), 0.0, places=12)


class Sequences(unittest.TestCase):
    def test_order_does_not_change_a_fixed_sequence(self):
        prior = [0.3, 0.25, 0.25, 0.2]
        a = [[0.8, 0.2], [0.3, 0.7], [0.3, 0.7], [0.1, 0.9]]
        b = [[0.6, 0.3, 0.1], [0.1, 0.2, 0.7], [0.5, 0.3, 0.2], [0.2, 0.2, 0.6]]
        self.assertAlmostEqual(
            ig.mutual_information(prior, ig.joint_rows([a, b])),
            ig.mutual_information(prior, ig.joint_rows([b, a])), places=12)

    def test_adaptive_is_at_least_the_best_fixed_pair(self):
        prior = [0.3, 0.25, 0.25, 0.2]
        tests = {
            "a": [[0.8, 0.2], [0.3, 0.7], [0.3, 0.7], [0.1, 0.9]],
            "b": [[0.6, 0.3, 0.1], [0.1, 0.2, 0.7], [0.5, 0.3, 0.2], [0.2, 0.2, 0.6]],
            "c": [[0.9, 0.1], [0.9, 0.1], [0.2, 0.8], [0.5, 0.5]],
        }
        names = list(tests)
        fixed = max(
            ig.mutual_information(prior, ig.joint_rows([tests[x], tests[y]]))
            for i, x in enumerate(names) for y in names[i + 1:])
        gain, first = ig.adaptive_gain(prior, tests, 2)
        self.assertGreaterEqual(gain, fixed - 1e-12)
        self.assertIn(first, names)
        one, _ = ig.adaptive_gain(prior, tests, 1)
        self.assertAlmostEqual(
            one, max(ig.mutual_information(prior, t) for t in tests.values()), places=12)

    def test_exclusive_tests_never_share_a_sequence(self):
        prior = [0.5, 0.5, 0.0, 0.0]
        weak = [[0.7, 0.3], [0.3, 0.7], [0.5, 0.5], [0.5, 0.5]]
        tests = {"x": weak, "y": weak}
        both, _ = ig.adaptive_gain(prior, tests, 2)
        barred, _ = ig.adaptive_gain(prior, tests, 2, {"x": ("y",), "y": ("x",)})
        self.assertGreater(both, barred + 1e-6)
        self.assertAlmostEqual(barred, ig.mutual_information(prior, weak), places=12)


class Validation(unittest.TestCase):
    def test_rows_that_do_not_sum_to_one_are_refused(self):
        with self.assertRaises(ValueError):
            ig.mutual_information([0.5, 0.5], [[0.6, 0.6], [0.5, 0.5]])

    def test_prior_that_does_not_sum_to_one_is_refused(self):
        with self.assertRaises(ValueError):
            ig.mutual_information([0.5, 0.6], [[0.5, 0.5], [0.5, 0.5]])


if __name__ == "__main__":
    unittest.main()
