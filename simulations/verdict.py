"""Seed-ensemble verdict guard, shared by the C-004 and C-008 simulations.

Standard library only, so it can be tested anywhere (the simulations need
numpy, this does not).

A verdict computed from one random seed is not a verdict. The C-004
sensor-realism run printed "OVERTURNED" from a single detectability ratio of
1.03; an 18-seed ensemble reversed it to a mean of 0.73 (see
ledger/OPEN.md, "Known gaps in the harness"). `decide` is the one place that
turns a statistic into a verdict word, and it refuses to name a side unless

  * there are at least `min_n` independent seeds, and
  * the `ci` confidence interval of the mean lies wholly on one side of the
    threshold.

Otherwise it returns "INCONCLUSIVE" with the reason. The interval is a
normal-approximation interval (z = 1.96 at 95%), the same one
simulate_c008.py has always reported, so adequately powered runs keep the
verdicts already recorded.
"""

from __future__ import annotations

import math
from statistics import NormalDist

INCONCLUSIVE = "INCONCLUSIVE"
DEFAULT_MIN_N = 10


def mean_ci(values, ci: float = 0.95) -> tuple[float, float, float]:
    """(mean, lo, hi). With n == 1 the interval degenerates to the point,
    which is exactly why `decide` must refuse small n rather than rely on it."""
    n = len(values)
    m = math.fsum(values) / n
    sd = math.sqrt(math.fsum((v - m) ** 2 for v in values) / (n - 1)) if n > 1 else 0.0
    h = NormalDist().inv_cdf(0.5 + ci / 2) * sd / math.sqrt(n)
    return m, m - h, m + h


def decide(values, threshold: float, above: str = "ABOVE", below: str = "BELOW",
           min_n: int = DEFAULT_MIN_N, ci: float = 0.95) -> tuple[str, str]:
    """Return (label, reason).

    `above` / `below` are the caller's words for a mean whose CI lies wholly
    above / below `threshold` (e.g. above="SURVIVES", below="REFUTED").
    Returns ("INCONCLUSIVE", reason) when n < min_n or the CI spans the
    threshold. No other word is ever returned.
    """
    vals = [float(v) for v in values]
    n = len(vals)
    if n < min_n:
        return INCONCLUSIVE, (
            f"{n} seed(s) is fewer than the {min_n} required to state a verdict; "
            f"a small-sample value is not evidence for either side of "
            f"{threshold:g}")
    m, lo, hi = mean_ci(vals, ci)
    span = f"mean {m:.3f}, {ci:.0%} CI [{lo:.3f}, {hi:.3f}], n={n}"
    if lo > threshold:
        return above, f"{span}: CI wholly above {threshold:g}"
    if hi < threshold:
        return below, f"{span}: CI wholly below {threshold:g}"
    return INCONCLUSIVE, f"{span}: CI spans {threshold:g}"
