"""Information-gain arithmetic for S-3. Standard library only.

A *test* is a list of rows, one per hypothesis; each row is the probability of
each outcome given that hypothesis and sums to one. Everything here is exact
enumeration over discrete outcomes: there is no sampling in this module, so
its numbers carry no Monte Carlo error.

Kept free of numpy so that test_infogain.py runs anywhere, like
simulations/verdict.py.
"""

from __future__ import annotations

import math

TOL = 1e-9


def _check(prior, rows) -> None:
    if len(prior) != len(rows):
        raise ValueError("one likelihood row per hypothesis is required")
    if abs(math.fsum(prior) - 1.0) > TOL or min(prior) < 0:
        raise ValueError("prior must be non-negative and sum to one")
    width = len(rows[0])
    for row in rows:
        if len(row) != width:
            raise ValueError("likelihood rows differ in length")
        if abs(math.fsum(row) - 1.0) > TOL or min(row) < -TOL:
            raise ValueError("each likelihood row must be non-negative and sum to one")


def entropy(p) -> float:
    """Shannon entropy in bits."""
    return -math.fsum(x * math.log2(x) for x in p if x > 0)


def joint_rows(tests):
    """Rows of the joint outcome of several tests, assuming the outcomes are
    independent given the hypothesis. `tests` is a sequence of tests."""
    n_h = len(tests[0])
    out = []
    for h in range(n_h):
        row = [1.0]
        for t in tests:
            row = [a * b for a in row for b in t[h]]
        out.append(row)
    return out


def mutual_information(prior, rows) -> float:
    """Expected information gain about the hypothesis from one observation of
    `rows`, in bits: I(H; Y) = sum_h sum_y p(h) p(y|h) log2(p(y|h) / p(y))."""
    _check(prior, rows)
    width = len(rows[0])
    marginal = [math.fsum(prior[h] * rows[h][y] for h in range(len(prior)))
                for y in range(width)]
    terms = []
    for h, ph in enumerate(prior):
        if ph <= 0:
            continue
        for y in range(width):
            p = rows[h][y]
            if p > 0:
                terms.append(ph * p * math.log2(p / marginal[y]))
    return math.fsum(terms)


def pairwise_bayes_error(prior, rows, i: int, j: int) -> float:
    """Error rate of the best possible reader who is told the truth is
    hypothesis i or j: priors renormalised over the pair, then the sum over
    outcomes of the smaller joint probability. With an uninformative test it
    is the smaller renormalised prior; with a perfect one it is 0."""
    _check(prior, rows)
    z = prior[i] + prior[j]
    if z <= 0:
        raise ValueError("the pair has zero prior mass")
    pi, pj = prior[i] / z, prior[j] / z
    return math.fsum(min(pi * a, pj * b) for a, b in zip(rows[i], rows[j]))


def adaptive_gain(prior, tests: dict, depth: int, exclusive: dict | None = None):
    """Best adaptive policy of at most `depth` tests, the next test chosen
    after the previous outcomes are seen. Exact dynamic programming.

    `tests` maps a name to its rows; `exclusive` maps a name to the names that
    may not share a sequence with it. Returns (expected information gain in
    bits, name of the first test or None).
    """
    exclusive = exclusive or {}
    n_h = len(prior)

    def rec(post, avail, k):
        h_now = entropy(post)
        if k == 0 or not avail:
            return h_now, None
        best, best_t = h_now, None
        for t in avail:
            rows = tests[t]
            nxt = tuple(x for x in avail
                        if x != t and x not in exclusive.get(t, ()))
            total = 0.0
            for y in range(len(rows[0])):
                py = math.fsum(post[h] * rows[h][y] for h in range(n_h))
                if py <= 0:
                    continue
                newpost = [post[h] * rows[h][y] / py for h in range(n_h)]
                total += py * rec(newpost, nxt, k - 1)[0]
            if total < best - 1e-15:
                best, best_t = total, t
        return best, best_t

    remaining, first = rec(list(prior), tuple(tests), depth)
    return entropy(prior) - remaining, first
