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
Student-t interval of the mean (exact table at 95% for df <= 30, a
Cornish-Fisher expansion of the t quantile otherwise). simulate_c008.py used
z = 1.96, which is too narrow at small n; the committed 18-seed verdicts are
unchanged under t. `min_n` is a floor on the seed count, not a power guarantee:
a run that clears it can still be INCONCLUSIVE, and 10 seeds can still be too
few for a small effect.
"""

from __future__ import annotations

import math
from statistics import NormalDist

# Two-sided 95% Student-t critical values, df = 1..30.
_T95 = (12.706, 4.303, 3.182, 2.776, 2.571, 2.447, 2.365, 2.306, 2.262, 2.228,
        2.201, 2.179, 2.160, 2.145, 2.131, 2.120, 2.110, 2.101, 2.093, 2.086,
        2.080, 2.074, 2.069, 2.064, 2.060, 2.056, 2.052, 2.048, 2.045, 2.042)

INCONCLUSIVE = "INCONCLUSIVE"
DEFAULT_MIN_N = 10


def t_crit(df: int, ci: float = 0.95) -> float:
    """Two-sided Student-t critical value for `ci` with `df` degrees of freedom."""
    if df < 1:
        return 0.0
    if ci == 0.95 and df <= len(_T95):
        return _T95[df - 1]
    z = NormalDist().inv_cdf(0.5 + ci / 2)
    return (z + (z**3 + z) / (4 * df)
            + (5 * z**5 + 16 * z**3 + 3 * z) / (96 * df**2)
            + (3 * z**7 + 19 * z**5 + 17 * z**3 - 15 * z) / (384 * df**3))


def mean_ci(values, ci: float = 0.95) -> tuple[float, float, float]:
    """(mean, lo, hi). With n == 1 the interval degenerates to the point,
    which is exactly why `decide` must refuse small n rather than rely on it."""
    n = len(values)
    m = math.fsum(values) / n
    sd = math.sqrt(math.fsum((v - m) ** 2 for v in values) / (n - 1)) if n > 1 else 0.0
    h = t_crit(n - 1, ci) * sd / math.sqrt(n)
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
