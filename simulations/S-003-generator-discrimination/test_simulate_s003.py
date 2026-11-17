"""Tests for the verdict rule in simulate_s003.py. Needs numpy, no network.

Run from the repo root:
    simulations/.venv/bin/python -m unittest simulations/S-003-generator-discrimination/test_simulate_s003.py

The pre-registered ensemble rule names a side only when `verdict.decide` on
the per-seed proportions and the pooled Wilson interval agree. These tests pin
the disagreement path in both directions; `mutation_check.py` removes the
agreement requirement and requires them to fail.
"""

import sys
import unittest
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import simulate_s003 as sim  # noqa: E402


def flags_from(per_seed_hits, draws):
    flags, seed_idx = [], []
    for k, hits in enumerate(per_seed_hits):
        flags += [True] * hits + [False] * (draws - hits)
        seed_idx += [k] * draws
    return np.array(flags), np.array(seed_idx)


class ProportionVerdict(unittest.TestCase):
    def test_decide_names_a_side_but_wilson_spans(self):
        # 10 seeds of 4 draws, 3 hits in each: every per-seed value is 0.75,
        # so the t-interval is the point 0.75, above 0.70. Pooled 30/40 has a
        # Wilson interval of about [0.60, 0.86], which spans 0.70.
        flags, seed_idx = flags_from([3] * 10, 4)
        v = sim.proportion_verdict(flags, seed_idx, 10, 0.70, "ABOVE", "BELOW")
        self.assertEqual(v["decide_label"], "ABOVE")
        self.assertEqual(v["wilson_label"], "INCONCLUSIVE")
        self.assertLess(v["wilson95"][0], 0.70)
        self.assertGreater(v["wilson95"][1], 0.70)
        self.assertEqual(v["verdict"], "INCONCLUSIVE")

    def test_wilson_names_a_side_but_decide_spans(self):
        # 10 seeds of 100 draws: five at 1.00 and five at 0.40. Pooled
        # 700/1000 has a Wilson interval near [0.67, 0.73], above 0.50. The
        # per-seed values have sd 0.316, t-interval about [0.47, 0.93], which
        # spans 0.50.
        flags, seed_idx = flags_from([100] * 5 + [40] * 5, 100)
        v = sim.proportion_verdict(flags, seed_idx, 10, 0.50, "ABOVE", "BELOW")
        self.assertEqual(v["wilson_label"], "ABOVE")
        self.assertEqual(v["decide_label"], "INCONCLUSIVE")
        self.assertEqual(v["verdict"], "INCONCLUSIVE")

    def test_agreement_names_the_side(self):
        flags, seed_idx = flags_from([95] * 10, 100)
        v = sim.proportion_verdict(flags, seed_idx, 10, 0.50, "ABOVE", "BELOW")
        self.assertEqual(v["verdict"], "ABOVE")
        flags, seed_idx = flags_from([5] * 10, 100)
        v = sim.proportion_verdict(flags, seed_idx, 10, 0.50, "ABOVE", "BELOW")
        self.assertEqual(v["verdict"], "BELOW")

    def test_too_few_seeds_is_inconclusive(self):
        flags, seed_idx = flags_from([100] * 3, 100)
        v = sim.proportion_verdict(flags, seed_idx, 3, 0.50, "ABOVE", "BELOW")
        self.assertEqual(v["verdict"], "INCONCLUSIVE")


if __name__ == "__main__":
    unittest.main()
