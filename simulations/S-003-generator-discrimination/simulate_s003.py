"""S-3: which clinical observations separate the pain generator.

A decision-analysis model, not biophysics. Four hypotheses about the generator
of long-standing, CRPS-labelled, post-surgical neuropathic foot pain; five
observations with discrete outcomes; expected information gain (mutual
information, bits) of every single test, pair and triple, of the best adaptive
policy, and a sensitivity ensemble over priors and likelihoods.

Everything that defines the model (hypotheses, observations, parameter ranges,
thresholds, verdict rules, seeds) is fixed in PREDICTION.md, which was
committed before this file existed. Change it there first, as an amendment.

Not medical advice. Population level only. No protocol, dose or device setting.

    simulations/.venv/bin/python simulations/S-003-generator-discrimination/simulate_s003.py --label main

The default label is "pilot" (gitignored), so a smoke run cannot land at the
canonical results/main/ path.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import infogain as ig  # noqa: E402
import verdict as vd  # noqa: E402

# --------------------------------------------------------------------------
# The model, as pre-registered (PREDICTION.md, "Operational definitions")
# --------------------------------------------------------------------------

HYP = ["H1", "H2", "H3", "H4"]
HYP_LABEL = {
    "H1": "peripheral focal lesion",
    "H2": "ganglion ectopia",
    "H3": "central amplification of normal input",
    "H4": "central, input-independent",
}
TESTS = ["T1", "T2", "T3", "T4", "T5"]
TEST_LABEL = {
    "T1": "single peripheral block",
    "T2": "comparative block",
    "T3": "dilute anaesthetic at the ganglion",
    "T4": "ganglion stimulation on/off",
    "T5": "ultrasound or MR neurography",
}
EXCLUSIVE = {"T1": ("T2",), "T2": ("T1",)}
PRIOR_ALPHA = (6.0, 5.0, 5.0, 4.0)
FLAT_ALPHA = (1.0, 1.0, 1.0, 1.0)
BASE_SEED = 20261117
FLAT_SEED = 20262117
N_SEEDS = 20
N_DRAWS = 200
PAIRS = [(i, j) for i in range(4) for j in range(i + 1, 4)]
ALL_FOUR = ("T2", "T3", "T4", "T5")

# name: (lo, hi, status, basis)
PARAMS = {
    "a": (0.60, 0.95, "anchored", "PMID 24704366: abolished in all 14, none with CRPS"),
    "u": (0.30, 0.70, "elicited", ""),
    "f": (0.15, 0.45, "anchored", "PMID 29913995: about 30%, zygapophysial joint blocks; transferred"),
    "g": (0.20, 0.60, "elicited", ""),
    "d": (0.00, 0.50, "elicited", ""),
    "r": (0.20, 0.60, "elicited", "PMID 29913995 gives no number"),
    "s": (0.00, 0.25, "elicited", ""),
    "e": (0.50, 0.95, "anchored (direction)", "PMID 24769187: phantom limb, no proportion"),
    "u3": (0.30, 0.70, "elicited", ""),
    "c": (0.00, 0.30, "elicited", ""),
    "f3": (0.05, 0.35, "elicited", "PMID 24769187: control injections ineffective, no number"),
    "g3": (0.20, 0.60, "elicited", ""),
    "s1": (0.30, 0.80, "elicited", "direction from PMID 33990112, 32658148 (rat, one lineage)"),
    "s2": (0.40, 0.85, "elicited", "same"),
    "s3": (0.10, 0.60, "elicited", "same"),
    "s4": (0.05, 0.35, "elicited", "same"),
    "v1": (0.30, 0.80, "elicited", "same"),
    "v2": (0.40, 0.85, "elicited", "same"),
    "v3": (0.30, 0.80, "elicited", "same"),
    "v4": (0.05, 0.50, "elicited", "same"),
    "q1": (0.45, 0.85, "anchored", "PMID 21701028: sensitivity 67% for neuroma, ten studies"),
    "q2": (0.10, 0.50, "elicited", ""),
    "q3": (0.05, 0.30, "elicited", ""),
    "q4": (0.05, 0.30, "elicited", ""),
}
PNAMES = list(PARAMS)
PARAM_TEST = {"a": "T1, T2, T3", "u": "T1, T2, T3", "f": "T1, T2", "g": "T1, T2",
              "d": "T1, T2", "r": "T2", "s": "T2", "e": "T3", "u3": "T3", "c": "T3",
              "f3": "T3", "g3": "T3", **{f"{k}{i}": "T4" for k in "sv" for i in "1234"},
              **{f"q{i}": "T5" for i in "1234"}}

# Hand point predictions from PREDICTION.md (bits unless stated): (lo, hi).
PREDICTED = {
    "T2": (0.35, 0.45), "T1": (0.27, 0.37), "T3": (0.20, 0.30),
    "T5": (0.10, 0.17), "T4": (0.07, 0.15),
    "best pair": (0.55, 0.70), "best triple": (0.70, 0.90),
    "min H1-H3 error, sets of at most 3": (0.20, 0.27),
    "H3-H4 error, all four tests": (0.09, 0.14),
}
PREDICTED_PROB = {"P1": 0.97, "P2": 0.80, "P2b": 0.85, "P3": 0.75, "Kill": 0.80}
THRESHOLDS = {"P1": 0.80, "P2": 0.50, "P2b": 0.70, "P3": 0.80, "Kill": 0.50}
P3_ERROR = 0.15
BIT = 1.0
CONTROL_TOL = 1e-9

ORACLE = [[1.0 if y == h else 0.0 for y in range(4)] for h in range(4)]
NOISE = [[0.2, 0.5, 0.3] for _ in range(4)]


def feasible_sets(tests):
    out = []
    for k in (1, 2, 3):
        for combo in itertools.combinations(tests, k):
            if "T1" in combo and "T2" in combo:
                continue
            out.append(combo)
    return out


SETS_A = feasible_sets(TESTS)
SETS_B = [s for s in SETS_A if "T3" not in s]
TESTS_B = [t for t in TESTS if t != "T3"]


def _nonspecific(row, f, g):
    """A non-specific response (probability f, share g reported as abolition)
    applied to a genuine (abolished, partial, none) row."""
    pa, pp, pn = row
    return [pa + (pp + pn) * f * g,
            pp * (1 - f * g) + pn * f * (1 - g),
            pn * (1 - f)]


def _mix(w, row):
    pa, pp = w * row[0], w * row[1]
    return [pa, pp, 1.0 - pa - pp]


def build_tests(th: dict) -> dict:
    """Likelihood rows for T1..T5 from one parameter draw. H1 and H3 share one
    row object under T1, T2 and T3 (the C-009 constraint)."""
    a, u = th["a"], th["u"]
    dep = [a, (1 - a) * u, (1 - a) * (1 - u)]
    none = [0.0, 0.0, 1.0]

    f, g = th["f"], th["g"]
    t1_dep = _nonspecific(dep, f, g)
    t1 = [t1_dep, _nonspecific(_mix(th["d"], dep), f, g), t1_dep,
          _nonspecific(none, f, g)]

    s = th["s"]
    dep2 = [a * (1 - s), (1 - a) * u + a * s, (1 - a) * (1 - u)]
    f2 = f * th["r"]
    t2_dep = _nonspecific(dep2, f2, g)
    t2 = [t2_dep, _nonspecific(_mix(th["d"], dep2), f2, g), t2_dep,
          _nonspecific(none, f2, g)]

    e, u3, f3, g3 = th["e"], th["u3"], th["f3"], th["g3"]
    t3_leak = _nonspecific(_mix(th["c"], dep), f3, g3)
    t3 = [t3_leak, _nonspecific([e, (1 - e) * u3, (1 - e) * (1 - u3)], f3, g3),
          t3_leak, _nonspecific(none, f3, g3)]

    t4 = []
    for i in "1234":
        sp, ev = th["s" + i], th["v" + i]
        t4.append([sp * ev, sp * (1 - ev), (1 - sp) * ev, (1 - sp) * (1 - ev)])

    t5 = [[th["q" + i], 1 - th["q" + i]] for i in "1234"]
    return {"T1": t1, "T2": t2, "T3": t3, "T4": t4, "T5": t5}


def _balanced(i, j):
    return [0.5 if h in (i, j) else 0.0 for h in range(4)]


def key(combo) -> str:
    return "+".join(combo)


def compute_draw(prior, th, check_order=False) -> dict:
    """Every per-draw quantity. Exact enumeration; no sampling."""
    tests = build_tests(th)
    out = {}
    joint = {s: ig.joint_rows([tests[t] for t in s]) for s in SETS_A}
    for s in SETS_A:
        out["ig:" + key(s)] = ig.mutual_information(prior, joint[s])
    all4 = ig.joint_rows([tests[t] for t in ALL_FOUR])
    out["ig:" + key(ALL_FOUR)] = ig.mutual_information(prior, all4)

    if check_order:
        worst = 0.0
        for s in SETS_A:
            if len(s) == 1:
                continue
            for perm in itertools.permutations(s):
                v = ig.mutual_information(
                    prior, ig.joint_rows([tests[t] for t in perm]))
                worst = max(worst, abs(v - out["ig:" + key(s)]))
        out["order_max_diff"] = worst

    for depth in (2, 3):
        gain, first = ig.adaptive_gain(prior, tests, depth, EXCLUSIVE)
        out[f"adaptA{depth}"] = gain
        out[f"adaptA{depth}_first"] = first
        gain, first = ig.adaptive_gain(
            prior, {t: tests[t] for t in TESTS_B}, depth, EXCLUSIVE)
        out[f"adaptB{depth}"] = gain
        out[f"adaptB{depth}_first"] = first

    out["pe13_min"] = min(ig.pairwise_bayes_error(prior, joint[s], 0, 2)
                          for s in SETS_A)
    # Post hoc diagnostic (PREDICTION.md, amendment B): the same error with the
    # pair's priors set equal, so that a lopsided prior cannot pass for a test.
    out["peb13_min"] = min(ig.pairwise_bayes_error(_balanced(0, 2), joint[s], 0, 2)
                           for s in SETS_A)
    for i, j in PAIRS:
        tag = f"{HYP[i]}-{HYP[j]}"
        out[f"pe_all:{tag}"] = ig.pairwise_bayes_error(prior, all4, i, j)
        out[f"peb_all:{tag}"] = ig.pairwise_bayes_error(_balanced(i, j), all4, i, j)
        out[f"pe_none:{tag}"] = min(prior[i], prior[j]) / (prior[i] + prior[j])
        for t in TESTS:
            out[f"pe:{t}:{tag}"] = ig.pairwise_bayes_error(prior, tests[t], i, j)
            out[f"rowdiff:{t}:{tag}"] = max(
                abs(x - y) for x, y in zip(tests[t][i], tests[t][j]))

    # Positive control, under this draw's prior.
    h0 = ig.entropy(prior)
    err = abs(ig.mutual_information(prior, ORACLE) - h0)
    err = max(err, abs(ig.mutual_information(prior, NOISE)))
    for t in TESTS:
        alone = out["ig:" + t]
        err = max(err, abs(ig.mutual_information(
            prior, ig.joint_rows([tests[t], NOISE])) - alone))
        err = max(err, abs(ig.mutual_information(
            prior, ig.joint_rows([tests[t], ORACLE])) - h0))
    out["control_err"] = err
    out["prior_entropy"] = h0
    out["structural_identical"] = all(
        tests[t][0] == tests[t][2] for t in ("T1", "T2", "T3"))
    return out


def run_ensemble(alpha, base_seed, n_seeds, n_draws, log):
    """Returns (per-draw dict of arrays, parameter matrix, priors, seed index)."""
    lo = np.array([PARAMS[p][0] for p in PNAMES])
    hi = np.array([PARAMS[p][1] for p in PNAMES])
    rows, thetas, priors, seed_idx = [], [], [], []
    for k in range(n_seeds):
        seed = base_seed + k
        rng = np.random.default_rng(seed)
        pri = rng.dirichlet(alpha, size=n_draws)
        theta = lo + (hi - lo) * rng.beta(2.0, 2.0, size=(n_draws, len(PNAMES)))
        for n in range(n_draws):
            prior = [float(x) for x in pri[n]]
            th = {p: float(theta[n, m]) for m, p in enumerate(PNAMES)}
            rows.append(compute_draw(prior, th, check_order=(n < 5)))
        thetas.append(theta)
        priors.append(pri)
        seed_idx += [k] * n_draws
        log(f"seed {seed}: {n_draws} draws done")
    cols = {}
    for name in rows[0]:
        if name == "order_max_diff":
            continue
        vals = [r[name] for r in rows]
        cols[name] = np.array(vals) if not isinstance(vals[0], (str, type(None))) \
            else np.array([v or "none" for v in vals])
    cols["order_max_diff"] = np.array(
        [r["order_max_diff"] for r in rows if "order_max_diff" in r])
    return cols, np.vstack(thetas), np.vstack(priors), np.array(seed_idx)


# --------------------------------------------------------------------------
# Statistics and verdicts
# --------------------------------------------------------------------------

def wilson(k: int, n: int, z: float = 1.959963984540054):
    if n == 0:
        return 0.0, 1.0
    p = k / n
    den = 1 + z * z / n
    mid = (p + z * z / (2 * n)) / den
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return max(0.0, mid - half), min(1.0, mid + half)


def proportion_verdict(flags, seed_idx, n_seeds, threshold, above, below):
    """The pre-registered ensemble rule: verdict.decide on the per-seed
    proportions, a pooled Wilson interval beside it, INCONCLUSIVE unless both
    name the same side."""
    flags = np.asarray(flags, dtype=bool)
    per_seed = [float(flags[seed_idx == k].mean()) for k in range(n_seeds)]
    label_t, reason = vd.decide(per_seed, threshold, above=above, below=below)
    k, n = int(flags.sum()), int(flags.size)
    w_lo, w_hi = wilson(k, n)
    if w_lo >= threshold:
        label_w = above
    elif w_hi < threshold:
        label_w = below
    else:
        label_w = vd.INCONCLUSIVE
    final = label_t if label_t == label_w else vd.INCONCLUSIVE
    if len(per_seed) >= 2:
        m, t_lo, t_hi = vd.mean_ci(per_seed)
    else:
        m, t_lo, t_hi = per_seed[0], float("nan"), float("nan")
    return {
        "verdict": final, "threshold": threshold, "proportion": k / n,
        "k": k, "n": n, "wilson95": [w_lo, w_hi],
        "per_seed_mean": m, "t95": [t_lo, t_hi], "n_seeds": len(per_seed),
        "per_seed": per_seed, "decide_label": label_t, "decide_reason": reason,
        "wilson_label": label_w,
    }


def describe(x, seed_idx, n_seeds):
    x = np.asarray(x, dtype=float)
    per_seed = [float(x[seed_idx == k].mean()) for k in range(n_seeds)]
    m, lo, hi = vd.mean_ci(per_seed) if n_seeds > 1 else (per_seed[0], float("nan"), float("nan"))
    q = np.percentile(x, [2.5, 50, 97.5])
    return {"median": float(q[1]), "p2.5": float(q[0]), "p97.5": float(q[2]),
            "mean": float(x.mean()), "mean_t95": [lo, hi]}


def rank_table(cols, sets, seed_idx, n_seeds):
    """Per size: rank distribution, P(top), IG summary for each set."""
    out = {}
    for size in (1, 2, 3):
        group = [s for s in sets if len(s) == size]
        mat = np.column_stack([cols["ig:" + key(s)] for s in group])
        order = (-mat).argsort(axis=1)
        ranks = np.empty_like(order)
        ar = np.arange(mat.shape[0])
        for pos in range(len(group)):
            ranks[ar, order[:, pos]] = pos + 1
        for m, s in enumerate(group):
            d = describe(mat[:, m], seed_idx, n_seeds)
            d["size"] = size
            d["p_top"] = float((ranks[:, m] == 1).mean())
            d["p_top_wilson95"] = list(wilson(int((ranks[:, m] == 1).sum()), mat.shape[0]))
            d["mean_rank"] = float(ranks[:, m].mean())
            d["rank_counts"] = [int((ranks[:, m] == r + 1).sum()) for r in range(len(group))]
            d["p_at_least_1_bit"] = float((mat[:, m] >= BIT).mean())
            out[key(s)] = d
    return out


def best_of(cols, sets, size):
    group = [s for s in sets if len(s) == size]
    mat = np.column_stack([cols["ig:" + key(s)] for s in group])
    idx = mat.argmax(axis=1)
    return mat.max(axis=1), [group[i] for i in idx]


def spearman(x, y) -> float:
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def analyse(cols, theta, priors, seed_idx, n_seeds, with_verdicts=True) -> dict:
    res = {"n_draws": int(seed_idx.size), "n_seeds": n_seeds}
    res["sets_A"] = rank_table(cols, SETS_A, seed_idx, n_seeds)
    res["sets_B"] = rank_table(cols, SETS_B, seed_idx, n_seeds)
    res["all_four"] = describe(cols["ig:" + key(ALL_FOUR)], seed_idx, n_seeds)
    res["prior_entropy"] = describe(cols["prior_entropy"], seed_idx, n_seeds)

    best1, _ = best_of(cols, SETS_A, 1)
    best2, best2_sets = best_of(cols, SETS_A, 2)
    best3, _ = best_of(cols, SETS_A, 3)
    best3b, _ = best_of(cols, SETS_B, 3)
    best_fixed = np.maximum(np.maximum(best1, best2), best3)
    best_le3 = np.maximum(best_fixed, cols["adaptA3"])
    best_le3_b = np.maximum(best3b, cols["adaptB3"])

    res["best"] = {
        "single": describe(best1, seed_idx, n_seeds),
        "pair": describe(best2, seed_idx, n_seeds),
        "triple": describe(best3, seed_idx, n_seeds),
        "adaptive depth 2": describe(cols["adaptA2"], seed_idx, n_seeds),
        "adaptive depth 3": describe(cols["adaptA3"], seed_idx, n_seeds),
        "at most 3, fixed or adaptive": describe(best_le3, seed_idx, n_seeds),
        "adaptive depth 3 minus best triple": describe(cols["adaptA3"] - best3, seed_idx, n_seeds),
        "set B triple": describe(best3b, seed_idx, n_seeds),
        "set B adaptive depth 3": describe(cols["adaptB3"], seed_idx, n_seeds),
        "set B at most 3, fixed or adaptive": describe(best_le3_b, seed_idx, n_seeds),
    }
    res["adaptive_first"] = {
        name: {t: float((cols[name + "_first"] == t).mean()) for t in TESTS}
        for name in ("adaptA2", "adaptA3", "adaptB2", "adaptB3")}
    res["p_best_le3_at_least_1_bit_set_B"] = float((best_le3_b >= BIT).mean())
    res["p_T2_above_T1"] = float((cols["ig:T2"] > cols["ig:T1"]).mean())

    res["pairwise"] = {}
    for i, j in PAIRS:
        tag = f"{HYP[i]}-{HYP[j]}"
        entry = {"all_four": describe(cols[f"pe_all:{tag}"], seed_idx, n_seeds),
                 "all_four_balanced": describe(cols[f"peb_all:{tag}"], seed_idx, n_seeds),
                 "no_test": describe(cols[f"pe_none:{tag}"], seed_idx, n_seeds),
                 "single": {t: describe(cols[f"pe:{t}:{tag}"], seed_idx, n_seeds)
                            for t in TESTS}}
        med = entry["all_four"]["median"]
        entry["class"] = ("not separated" if med >= 0.15 else
                          "partly separated" if med >= 0.05 else "separated")
        entry["structurally_unseparated_by"] = [
            t for t in TESTS
            if float(np.max(cols[f"rowdiff:{t}:{tag}"])) == 0.0]
        res["pairwise"][tag] = entry
    res["pe13_min"] = describe(cols["pe13_min"], seed_idx, n_seeds)
    res["pe13_min_balanced"] = describe(cols["peb13_min"], seed_idx, n_seeds)
    res["p_pe13_min_balanced_at_least_threshold"] = float(
        (cols["peb13_min"] >= P3_ERROR).mean())
    res["p_pe13_no_test_below_threshold"] = float(
        (cols["pe_none:H1-H3"] < P3_ERROR).mean())

    target = best3
    sens = []
    for m, p in enumerate(PNAMES):
        sens.append({"parameter": p, "tests": PARAM_TEST[p], "status": PARAMS[p][2],
                     "rho_best_triple": spearman(theta[:, m], target),
                     "rho_best_le3": spearman(theta[:, m], best_le3)})
    for h in range(4):
        sens.append({"parameter": f"prior {HYP[h]}", "tests": "all", "status":
                     "anchored" if h == 0 else "elicited",
                     "rho_best_triple": spearman(priors[:, h], target),
                     "rho_best_le3": spearman(priors[:, h], best_le3)})
    sens.sort(key=lambda d: -abs(d["rho_best_triple"]))
    res["sensitivity"] = sens

    control = {
        "max_abs_error_bits": float(np.max(cols["control_err"])),
        "tolerance": CONTROL_TOL,
        "oracle_uniform_prior_bits": ig.mutual_information([0.25] * 4, ORACLE),
        "noise_uniform_prior_bits": ig.mutual_information([0.25] * 4, NOISE),
        "order_max_diff_bits": float(np.max(cols["order_max_diff"])),
        "order_draws_checked": int(cols["order_max_diff"].size),
        "h1_h3_rows_identical_T1_T2_T3": bool(np.all(cols["structural_identical"])),
    }
    control["pass"] = bool(
        control["max_abs_error_bits"] <= CONTROL_TOL
        and abs(control["oracle_uniform_prior_bits"] - 2.0) <= CONTROL_TOL
        and abs(control["noise_uniform_prior_bits"]) <= CONTROL_TOL
        and control["order_max_diff_bits"] <= CONTROL_TOL
        and control["h1_h3_rows_identical_T1_T2_T3"])
    res["control"] = control

    flags = {
        "P1": best1 < BIT,
        "P2": np.array(["T3" in s for s in best2_sets]),
        "P2b": np.array([("T1" in s or "T2" in s) for s in best2_sets]),
        "P3": cols["pe13_min"] >= P3_ERROR,
        "Kill": best_le3 >= BIT,
    }
    words = {"P1": ("SUPPORTED", "NOT SUPPORTED"), "P2": ("SUPPORTED", "NOT SUPPORTED"),
             "P2b": ("SUPPORTED", "NOT SUPPORTED"), "P3": ("SUPPORTED", "NOT SUPPORTED"),
             "Kill": ("NOT TRIGGERED", "TRIGGERED")}
    res["claims"] = {}
    for name, fl in flags.items():
        v = proportion_verdict(fl, seed_idx, n_seeds, THRESHOLDS[name], *words[name])
        if not with_verdicts:
            v["verdict"] = "secondary, no verdict"
        elif not control["pass"]:
            v["verdict"] = "NO VERDICT (positive control failed)"
        res["claims"][name] = v
    return res


def midpoint_check() -> dict:
    """The hand arithmetic in PREDICTION.md, redone by machine at the same
    point: every parameter at the midpoint of its range, the mean prior."""
    th = {p: (PARAMS[p][0] + PARAMS[p][1]) / 2 for p in PNAMES}
    prior = [a / sum(PRIOR_ALPHA) for a in PRIOR_ALPHA]
    d = compute_draw(prior, th)
    hand = {"T1": 0.32, "T2": 0.40, "T3": 0.26, "T4": 0.11, "T5": 0.13}
    return {"hand": hand, "machine": {t: d["ig:" + t] for t in TESTS},
            "rows": build_tests(th),
            "best_pair": max(((key(s), d["ig:" + key(s)]) for s in SETS_A if len(s) == 2),
                             key=lambda kv: kv[1]),
            "best_triple": max(((key(s), d["ig:" + key(s)]) for s in SETS_A if len(s) == 3),
                               key=lambda kv: kv[1]),
            "pe13_min": d["pe13_min"]}


# --------------------------------------------------------------------------
# Output
# --------------------------------------------------------------------------

QUESTIONS = {
    "T1": "Does spontaneous pain depend on input from the limb at all? (A single block can ask this; "
          "it cannot say whether that input is abnormal.)",
    "T2": "Does spontaneous pain depend on input from the limb, when the answer is checked against a "
          "second, controlled block rather than taken from one?",
    "T3": "Is the ganglion itself the source? (The only observation here aimed at that question; "
          "it is a research procedure, reported in one human series in another condition.)",
    "T4": "Where a ganglion stimulator is already present: do background pain and touch-evoked pain "
          "respond together or apart when it is on and off?",
    "T5": "Is there a focal nerve lesion on high-resolution imaging, knowing that a visible lesion "
          "need not be the generator and a missed one is common?",
}


def f3(x) -> str:
    return f"{0.0 if abs(x) < 5e-4 else x:.3f}"


def interval(d) -> str:
    return f"[{d['p2.5']:.3f}, {d['p97.5']:.3f}]"


def claim_row(name, text, c) -> str:
    return (f"| {name} | {text} | {c['proportion']:.3f} ({c['k']}/{c['n']}) | "
            f"[{c['wilson95'][0]:.3f}, {c['wilson95'][1]:.3f}] | "
            f"{c['per_seed_mean']:.3f} [{c['t95'][0]:.3f}, {c['t95'][1]:.3f}] | "
            f"{c['threshold']:.2f} | **{c['verdict']}** |")


def in_range(x, lo_hi) -> str:
    lo, hi = lo_hi
    return "inside" if lo <= x <= hi else ("above" if x > hi else "below")


def write_markdown(path: Path, R: dict) -> None:
    main, flat, mid = R["main"], R["flat_prior"], R["midpoint_check"]
    A = main["sets_A"]
    c = main["claims"]
    ctl = main["control"]
    L = []
    w = L.append
    w("# S-3 results: which observations separate the pain generator")
    w("")
    w("Not medical advice; these are questions a treating team might consider, at population level.")
    w("")
    w("This is a decision-analysis model. It gives no protocol, dose or device setting, and it says "
      "nothing about any individual. **No likelihood in it is fully sourced**: every range is elicited, "
      "some anchored on a number or a direction read from an abstract (table at the end). The intervals "
      "below measure Monte Carlo error and the spread across those elicited ranges. They do not measure "
      "whether the ranges are right.")
    w("")
    w(f"Pre-registration: `PREDICTION.md` (commit #1). Run: {main['n_seeds']} seeds of "
      f"{main['n_draws'] // main['n_seeds']} draws, {main['n_draws']} draws, seeds "
      f"{R['seeds']['main'][0]} to {R['seeds']['main'][-1]}; code at commit `{R['code_commit']}`"
      f"{' (working tree had uncommitted changes to the code)' if R['code_dirty'] else ''}. "
      f"Verdict rule: `simulations/verdict.py` `decide` on the per-seed proportions, with a pooled "
      f"Wilson 95% interval beside it; INCONCLUSIVE unless both name the same side.")
    if R["label"] != "main" or main["n_seeds"] < vd.DEFAULT_MIN_N:
        w("")
        w(f"**This is run `{R['label']}`, not the pre-registered main run. Nothing here is a result.**")
    w("")
    w("## Verdicts")
    w("")
    w("| Claim | Statement | Proportion of draws | Wilson 95% | Per-seed mean [t 95%] | Threshold | Verdict |")
    w("|---|---|---|---|---|---|---|")
    w(claim_row("P1", "every single test is below 1 bit", c["P1"]))
    w(claim_row("P2", "the best pair includes T3", c["P2"]))
    w(claim_row("P2b", "the best pair includes a block (T1 or T2)", c["P2b"]))
    w(claim_row("P3", f"H1 against H3: pairwise Bayes error is at least {P3_ERROR} under every set of at most 3 tests", c["P3"]))
    w(claim_row("Kill", "the best sequence of at most 3 tests, fixed or adaptive, reaches 1 bit (triggered when below 0.50)", c["Kill"]))
    w("")
    k = c["Kill"]
    b = main["best"]["at most 3, fixed or adaptive"]
    if k["verdict"] == "TRIGGERED":
        w(f"**The kill is triggered.** In the median draw the best sequence of at most three observations "
          f"yields {f3(b['median'])} bits (central 95% of draws {interval(b)}), against a prior "
          f"uncertainty of {f3(main['prior_entropy']['median'])} bits, and it reaches 1 bit in "
          f"{k['proportion']:.3f} of draws. Within this model and these ranges, the available clinical "
          f"observations cannot localise the generator. That is a result, not a failure.")
    elif k["verdict"] == "NOT TRIGGERED":
        w(f"**The kill is not triggered.** The best sequence of at most three observations reaches 1 bit "
          f"in {k['proportion']:.3f} of draws (median {f3(b['median'])} bits, central 95% of draws "
          f"{interval(b)}; prior uncertainty {f3(main['prior_entropy']['median'])} bits).")
    else:
        w(f"**The kill is {k['verdict']}.** The best sequence of at most three observations reaches 1 bit "
          f"in {k['proportion']:.3f} of draws (median {f3(b['median'])} bits, central 95% of draws "
          f"{interval(b)}).")
    w("")
    w("## Positive control")
    w("")
    w(f"- Oracle test, uniform prior: {ctl['oracle_uniform_prior_bits']:.9f} bits (need 2).")
    w(f"- Pure-noise test, uniform prior: {ctl['noise_uniform_prior_bits']:.9f} bits (need 0).")
    w(f"- Across all {main['n_draws']} drawn priors (oracle equals the prior entropy; noise is 0; noise "
      f"added to each test changes nothing; oracle added to each test returns the prior entropy): "
      f"largest absolute error {ctl['max_abs_error_bits']:.2e} bits (tolerance {ctl['tolerance']:.0e}).")
    w(f"- Order of a fixed sequence: largest difference between orderings of the same set "
      f"{ctl['order_max_diff_bits']:.2e} bits, checked on {ctl['order_draws_checked']} draws.")
    w(f"- H1 and H3 rows identical under T1, T2 and T3 in every draw (C-009): "
      f"{'yes' if ctl['h1_h3_rows_identical_T1_T2_T3'] else 'NO'}.")
    w(f"- **Control: {'PASS' if ctl['pass'] else 'FAIL'}.**")
    w("")
    w("## Single tests")
    w("")
    w("Information gain in bits. \"Central 95%\" is the 2.5th to 97.5th percentile across draws: the "
      "spread from the elicited ranges, not a confidence interval of a mean.")
    w("")
    w("| Test | Median IG | Central 95% of draws | Mean [t 95% across seeds] | P(top single) | Mean rank | P(IG at least 1 bit) |")
    w("|---|---|---|---|---|---|---|")
    singles = sorted([s for s in A if A[s]["size"] == 1], key=lambda s: -A[s]["median"])
    for s in singles:
        d = A[s]
        w(f"| {s} {TEST_LABEL[s]} | {f3(d['median'])} | {interval(d)} | {f3(d['mean'])} "
          f"[{d['mean_t95'][0]:.3f}, {d['mean_t95'][1]:.3f}] | {d['p_top']:.3f} | "
          f"{d['mean_rank']:.2f} | {d['p_at_least_1_bit']:.3f} |")
    w("")
    w(f"The comparative block is above the single block in {main['p_T2_above_T1']:.3f} of draws. "
      f"That ordering comes from the elicited ranges for r and s (how much a control removes false "
      f"responses against how many true responders it loses), not from data: no source read here "
      f"gives either number for peripheral nerve blocks.")
    w("")
    for size, title in ((2, "Pairs"), (3, "Triples")):
        group = sorted([s for s in A if A[s]["size"] == size], key=lambda s: -A[s]["p_top"])
        w(f"## {title} (set A)")
        w("")
        w(f"| Set | Median IG | Central 95% of draws | Mean [t 95% across seeds] | P(top) | Wilson 95% of P(top) | Mean rank | Rank counts, 1st to {len(group)}th | P(IG at least 1 bit) |")
        w("|---|---|---|---|---|---|---|---|---|")
        for s in group:
            d = A[s]
            w(f"| {s} | {f3(d['median'])} | {interval(d)} | {f3(d['mean'])} "
              f"[{d['mean_t95'][0]:.3f}, {d['mean_t95'][1]:.3f}] | {d['p_top']:.3f} | "
              f"[{d['p_top_wilson95'][0]:.3f}, {d['p_top_wilson95'][1]:.3f}] | {d['mean_rank']:.2f} | "
              f"{' / '.join(str(x) for x in d['rank_counts'])} | {d['p_at_least_1_bit']:.3f} |")
        w("")
    top2 = max((s for s in A if A[s]["size"] == 2), key=lambda s: A[s]["p_top"])
    top3 = max((s for s in A if A[s]["size"] == 3), key=lambda s: A[s]["p_top"])
    w(f"The pair most often on top is **{top2}** (P(top) {A[top2]['p_top']:.3f}); the triple most "
      f"often on top is **{top3}** (P(top) {A[top3]['p_top']:.3f}). All four of "
      f"{', '.join(ALL_FOUR)} together: median {f3(main['all_four']['median'])} bits, central 95% "
      f"{interval(main['all_four'])}.")
    w("")
    w("**Order.** Under the model's conditional independence a fixed sequence has the same information "
      "gain in any order (checked above), so the 18 ordered pairs and 42 ordered triples collapse onto "
      "the 9 and 7 sets in these tables. What order changes is what is known after the first step, "
      "which is the single-test table.")
    w("")
    w("## Adaptive policies")
    w("")
    bb = main["best"]
    w("| Policy | Median IG | Central 95% of draws |")
    w("|---|---|---|")
    for name in ("single", "pair", "adaptive depth 2", "triple", "adaptive depth 3",
                 "at most 3, fixed or adaptive", "adaptive depth 3 minus best triple"):
        label = {"single": "best single test", "pair": "best fixed pair",
                 "triple": "best fixed triple"}.get(name, name)
        w(f"| {label} | {f3(bb[name]['median'])} | {interval(bb[name])} |")
    w("")
    first = main["adaptive_first"]["adaptA3"]
    w("First test of the best depth-3 adaptive policy, share of draws: "
      + ", ".join(f"{t} {first[t]:.3f}" for t in sorted(first, key=lambda t: -first[t])) + ".")
    w("")
    w("## Set B: without T3")
    w("")
    w("T3 is a research procedure, so the same analysis is repeated without it. Secondary, no verdict.")
    w("")
    B = main["sets_B"]
    w("| Set | Median IG | Central 95% of draws | P(top in set B) |")
    w("|---|---|---|---|")
    for size in (2, 3):
        for s in sorted([s for s in B if B[s]["size"] == size], key=lambda s: -B[s]["p_top"]):
            w(f"| {s} | {f3(B[s]['median'])} | {interval(B[s])} | {B[s]['p_top']:.3f} |")
    w("")
    w(f"Best sequence of at most three without T3, fixed or adaptive: median "
      f"{f3(bb['set B at most 3, fixed or adaptive']['median'])} bits, central 95% "
      f"{interval(bb['set B at most 3, fixed or adaptive'])}; reaches 1 bit in "
      f"{main['p_best_le3_at_least_1_bit_set_B']:.3f} of draws.")
    w("")
    w("## Which pairs of hypotheses are separated")
    w("")
    w("Pairwise Bayes error: the error rate of the best possible reader told that the truth is one of "
      "the two. Median across draws. \"No test\" is the starting point (the smaller of the two "
      "renormalised priors). Classes as pre-registered: not separated at 0.15 or above with all four "
      "tests, partly separated from 0.05, separated below 0.05.")
    w("")
    w("| Pair | No test | " + " | ".join(TESTS) + " | All of " + ", ".join(ALL_FOUR)
      + " | Central 95%, all four | Class | Identical rows under | Equal priors, all four (post hoc) |")
    w("|---|---|" + "---|" * len(TESTS) + "---|---|---|---|---|")
    for tag, e in main["pairwise"].items():
        w(f"| {tag} | {f3(e['no_test']['median'])} | "
          + " | ".join(f3(e["single"][t]["median"]) for t in TESTS)
          + f" | {f3(e['all_four']['median'])} | {interval(e['all_four'])} | {e['class']} | "
          + (", ".join(e["structurally_unseparated_by"]) or "none")
          + f" | {f3(e['all_four_balanced']['median'])} {interval(e['all_four_balanced'])} |")
    w("")
    notsep = [t for t, e in main["pairwise"].items() if e["class"] == "not separated"]
    partly = [t for t, e in main["pairwise"].items() if e["class"] == "partly separated"]
    sep = [t for t, e in main["pairwise"].items() if e["class"] == "separated"]
    w(f"- **Not separated by anything available:** {', '.join(notsep) or 'none'}.")
    w(f"- Partly separated: {', '.join(partly) or 'none'}.")
    w(f"- Separated: {', '.join(sep) or 'none'}.")
    w(f"- H1 against H3, the best any set of at most three tests does: median error "
      f"{f3(main['pe13_min']['median'])}, central 95% {interval(main['pe13_min'])}.")
    w("")
    w(f"**A weakness of the pre-registered measure, found in the pilot.** The pairwise error can never "
      f"exceed the smaller of the two renormalised priors, so a lopsided prior draw gives a low error "
      f"with no test at all: for H1 against H3 the no-test error is already below {P3_ERROR} in "
      f"{main['p_pe13_no_test_below_threshold']:.3f} of main draws and "
      f"{flat['p_pe13_no_test_below_threshold']:.3f} of flat-prior draws. P3 is scored as "
      f"pre-registered. The last column is a post hoc diagnostic, not a threshold: the same error with "
      f"the pair's priors set equal (0.5 with no test). On that measure the best any set of at most "
      f"three tests does for H1 against H3 is median {f3(main['pe13_min_balanced']['median'])}, central "
      f"95% {interval(main['pe13_min_balanced'])}, and it is at least {P3_ERROR} in "
      f"{main['p_pe13_min_balanced_at_least_threshold']:.3f} of draws "
      f"({flat['p_pe13_min_balanced_at_least_threshold']:.3f} under the flat prior, where the likelihood "
      f"ranges are the same).")
    w("")
    w("Hypotheses: " + "; ".join(f"{h} {HYP_LABEL[h]}" for h in HYP) + ".")
    w("")
    w("## Questions a treating team might consider, in the order the model ranks them")
    w("")
    w("Ranked by median information gain of the single observation. These are questions, not steps. "
      "Risk, burden, cost and availability are not in the model, and information gain is not clinical "
      "value.")
    w("")
    for n, s in enumerate(singles, 1):
        w(f"{n}. **{s}, {TEST_LABEL[s]}** (median {f3(A[s]['median'])} bits; in the top pair in "
          f"{sum(A[p]['p_top'] for p in A if A[p]['size'] == 2 and s in p.split('+')):.3f} of draws). "
          f"{QUESTIONS[s]}")
    w("")
    w("## Sensitivity: which elicited number moves the answer")
    w("")
    w("Spearman rank correlation, across draws, between each drawn quantity and the information gain "
      "of the best fixed triple. The ten largest in absolute value.")
    w("")
    w("| Quantity | Used by | Status | Spearman rho |")
    w("|---|---|---|---|")
    for d in main["sensitivity"][:10]:
        w(f"| {d['parameter']} | {d['tests']} | {d['status']} | {d['rho_best_triple']:+.3f} |")
    w("")
    w("## Flat-prior ensemble (secondary, no verdict)")
    w("")
    w(f"The same likelihood ranges with a Dirichlet(1, 1, 1, 1) prior, seeds "
      f"{R['seeds']['flat_prior'][0]} to {R['seeds']['flat_prior'][-1]}.")
    w("")
    w("| Quantity | Main ensemble | Flat prior |")
    w("|---|---|---|")
    w(f"| prior entropy, median bits | {f3(main['prior_entropy']['median'])} | {f3(flat['prior_entropy']['median'])} |")
    for name, label in (("single", "best single test, median bits"), ("pair", "best pair, median bits"),
                        ("triple", "best triple, median bits"),
                        ("at most 3, fixed or adaptive", "best of at most 3, fixed or adaptive, median bits")):
        w(f"| {label} | {f3(main['best'][name]['median'])} | {f3(flat['best'][name]['median'])} |")
    for name, label in (("P1", "every single test below 1 bit, proportion"),
                        ("P2", "best pair includes T3, proportion"),
                        ("P2b", "best pair includes a block, proportion"),
                        ("P3", "H1-H3 error at least 0.15 under every set, proportion"),
                        ("Kill", "best of at most 3 reaches 1 bit, proportion")):
        w(f"| {label} | {main['claims'][name]['proportion']:.3f} | {flat['claims'][name]['proportion']:.3f} |")
    w("")
    w("## Prediction against result")
    w("")
    w("| Quantity | Predicted by hand (PREDICTION.md) | Result (median) | |")
    w("|---|---|---|---|")
    got = {t: A[t]["median"] for t in TESTS}
    got["best pair"] = bb["pair"]["median"]
    got["best triple"] = bb["triple"]["median"]
    got["min H1-H3 error, sets of at most 3"] = main["pe13_min"]["median"]
    got["H3-H4 error, all four tests"] = main["pairwise"]["H3-H4"]["all_four"]["median"]
    for name, rng in PREDICTED.items():
        w(f"| {name} | {rng[0]:.2f} to {rng[1]:.2f} | {f3(got[name])} | {in_range(got[name], rng)} |")
    gap = bb["adaptive depth 3 minus best triple"]["median"]
    w(f"| adaptive depth 3 minus best triple | at most 0.05 | {f3(gap)} | "
      f"{'inside' if gap <= 0.05 else 'above'} |")
    w(f"| unseparated pairs | H1-H3 only | {', '.join(notsep) or 'none'} | "
      f"{'as predicted' if notsep == ['H1-H3'] else 'not as predicted'} |")
    w(f"| pairs below 0.05 | none | {', '.join(sep) or 'none'} | "
      f"{'as predicted' if not sep else 'not as predicted'} |")
    w("")
    w("| Claim | My stated probability | Verdict |")
    w("|---|---|---|")
    for name in ("P1", "P2", "P2b", "P3"):
        w(f"| {name} supported | {PREDICTED_PROB[name]:.0%} | {c[name]['verdict']} |")
    w(f"| Kill triggered | {PREDICTED_PROB['Kill']:.0%} | {c['Kill']['verdict']} |")
    w("")
    w("Hand arithmetic at the midpoint of every range, redone by machine at the same point:")
    w("")
    w("| Test | By hand | By machine |")
    w("|---|---|---|")
    for t in TESTS:
        w(f"| {t} | {mid['hand'][t]:.2f} | {f3(mid['machine'][t])} |")
    w("")
    w(f"At the midpoint the best pair is {mid['best_pair'][0]} at {f3(mid['best_pair'][1])} bits and "
      f"the best triple is {mid['best_triple'][0]} at {f3(mid['best_triple'][1])} bits.")
    w("")
    w("## Likelihood parameters and their status")
    w("")
    n_anch = sum(1 for p in PNAMES if PARAMS[p][2].startswith("anchored"))
    w(f"{len(PNAMES)} parameters: {n_anch} anchored on a source, {len(PNAMES) - n_anch} elicited, "
      f"none fully sourced. Each is drawn as lo + (hi - lo) x Beta(2, 2). Prior: Dirichlet"
      f"{tuple(int(a) for a in PRIOR_ALPHA)}; the H1 mean is anchored on PMID 40211731 (26% and 33%), "
      f"the rest is elicited.")
    w("")
    w("| Parameter | Used by | Range | Status | Basis |")
    w("|---|---|---|---|---|")
    for p in PNAMES:
        lo, hi, status, basis = PARAMS[p]
        w(f"| {p} | {PARAM_TEST[p]} | {lo:.2f} to {hi:.2f} | {status} | {basis} |")
    w("")
    w("## Declared limits")
    w("")
    w("- The likelihoods are largely elicited. The result describes how the ranking behaves across "
      "the stated ranges; it is not a measurement of any test's accuracy.")
    w("- It says nothing about any individual and is not a protocol.")
    w("- The four hypotheses are treated as exclusive and exhaustive, the tests as independent given "
      "the hypothesis, and the parameters as independent. Each of these flatters the tests.")
    w("- Sources are small and mostly not in CRPS; two mechanisms rest on rat work from one lineage each.")
    w("- Information gain is not clinical value.")
    w("")
    path.write_text("\n".join(L) + "\n")


def make_figures(out: Path, R: dict) -> list:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    main = R["main"]
    A = main["sets_A"]
    names = sorted(A, key=lambda s: (A[s]["size"], -A[s]["median"]))[::-1]
    colours = {1: "#7a7a7a", 2: "#2b6cb0", 3: "#c05621"}
    fig, ax = plt.subplots(figsize=(8, 7.5))
    for y, s in enumerate(names):
        d = A[s]
        ax.plot([d["p2.5"], d["p97.5"]], [y, y], color=colours[d["size"]], lw=2.5,
                solid_capstyle="round")
        ax.plot(d["median"], y, "o", color=colours[d["size"]], ms=6)
        ax.text(1.55, y, f"P(top) {d['p_top']:.2f}", va="center", fontsize=7)
    ax.axvline(BIT, color="k", ls="--", lw=1)
    ax.text(BIT + 0.01, len(names) - 0.4, "1 bit (kill line)", fontsize=8)
    ax.set_ylim(-0.8, len(names) + 0.2)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=8)
    ax.set_xlim(0, 2)
    ax.set_xlabel("expected information gain, bits (maximum log2 4 = 2)")
    ax.set_title(f"S-3: information gain of every set, median and central 95% of "
                 f"{main['n_draws']} draws\n(grey single, blue pair, orange triple; P(top) within size). "
                 f"Not medical advice.", fontsize=9)
    fig.tight_layout()
    f1 = out / "information-gain-by-set.png"
    fig.savefig(f1, dpi=140)
    plt.close(fig)

    cols = ["no test"] + TESTS + ["all four"]
    tags = list(main["pairwise"])
    mat = np.array([[main["pairwise"][t]["no_test"]["median"]]
                    + [main["pairwise"][t]["single"][x]["median"] for x in TESTS]
                    + [main["pairwise"][t]["all_four"]["median"]] for t in tags])
    fig, ax = plt.subplots(figsize=(8, 4.2))
    im = ax.imshow(mat, cmap="viridis_r", vmin=0, vmax=0.5, aspect="auto")
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            ax.text(j, i, f"{mat[i, j]:.2f}", ha="center", va="center", fontsize=8,
                    color="white" if mat[i, j] > 0.25 else "black")
    ax.set_xticks(range(len(cols)))
    ax.set_xticklabels(cols, fontsize=8)
    ax.set_yticks(range(len(tags)))
    ax.set_yticklabels(tags, fontsize=8)
    fig.colorbar(im, ax=ax, label="pairwise Bayes error (median)")
    ax.set_title("S-3: which test separates which pair (0 = separated; 'no test' column = not at all)\n"
                 "H1 lesion, H2 ganglion, H3 central amplification, H4 central input-independent. "
                 "Not medical advice.", fontsize=9)
    fig.tight_layout()
    f2 = out / "pairwise-separation.png"
    fig.savefig(f2, dpi=140)
    plt.close(fig)
    return [f1.name, f2.name]


def rel(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO))
    except ValueError:
        return path.name


def git_state():
    try:
        sha = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=HERE,
                             capture_output=True, text=True, check=True).stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain", "--", "simulate_s003.py", "infogain.py",
             "PREDICTION.md", "../verdict.py"],
            cwd=HERE, capture_output=True, text=True, check=True).stdout.strip() != ""
        return sha, dirty
    except (OSError, subprocess.CalledProcessError):
        return "unknown", True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--label", default="pilot",
                    help="results/<label>/. Default 'pilot' (gitignored). The "
                         "pre-registered run is --label main.")
    ap.add_argument("--seeds", type=int, default=N_SEEDS)
    ap.add_argument("--draws", type=int, default=N_DRAWS, help="draws per seed")
    ap.add_argument("--no-figures", action="store_true")
    args = ap.parse_args()
    if args.label == "main" and (args.seeds, args.draws) != (N_SEEDS, N_DRAWS):
        print("refusing: results/main/ is the pre-registered run "
              f"({N_SEEDS} seeds of {N_DRAWS} draws) and nothing else")
        return 2

    out = HERE / "results" / args.label
    out.mkdir(parents=True, exist_ok=True)
    log_path = out / "run.log"
    log_lines = []

    def log(msg):
        line = f"{time.strftime('%H:%M:%S')} {msg}"
        print(line, flush=True)
        log_lines.append(line)

    sha, dirty = git_state()
    log(f"start label={args.label} seeds={args.seeds} draws_per_seed={args.draws} "
        f"numpy={np.__version__} python={sys.version.split()[0]} code_commit={sha} "
        f"dirty={dirty} out={rel(out)}")

    R = {"simulation": "S-003-generator-discrimination", "label": args.label,
         "date": time.strftime("%Y-%m-%d"), "code_commit": sha, "code_dirty": dirty,
         "numpy": np.__version__,
         "seeds": {"main": [BASE_SEED + k for k in range(args.seeds)],
                   "flat_prior": [FLAT_SEED + k for k in range(args.seeds)]},
         "draws_per_seed": args.draws,
         "prior_alpha": list(PRIOR_ALPHA), "flat_alpha": list(FLAT_ALPHA),
         "thresholds": THRESHOLDS, "p3_error_threshold": P3_ERROR,
         "parameters": {p: {"lo": v[0], "hi": v[1], "status": v[2], "basis": v[3],
                            "tests": PARAM_TEST[p]} for p, v in PARAMS.items()},
         "feasible_sets": {"A": [key(s) for s in SETS_A], "B": [key(s) for s in SETS_B],
                           "ordered_pairs": sum(2 for s in SETS_A if len(s) == 2),
                           "ordered_triples": sum(6 for s in SETS_A if len(s) == 3)}}

    R["midpoint_check"] = midpoint_check()
    log("midpoint check: " + json.dumps(
        {t: round(v, 4) for t, v in R["midpoint_check"]["machine"].items()}))

    log("main ensemble")
    cols, theta, priors, seed_idx = run_ensemble(PRIOR_ALPHA, BASE_SEED, args.seeds, args.draws, log)
    R["main"] = analyse(cols, theta, priors, seed_idx, args.seeds)
    log("flat-prior ensemble (secondary)")
    cols, theta, priors, seed_idx = run_ensemble(FLAT_ALPHA, FLAT_SEED, args.seeds, args.draws, log)
    R["flat_prior"] = analyse(cols, theta, priors, seed_idx, args.seeds, with_verdicts=False)

    ctl = R["main"]["control"]
    log(f"control: {'PASS' if ctl['pass'] else 'FAIL'} oracle={ctl['oracle_uniform_prior_bits']:.9f} "
        f"noise={ctl['noise_uniform_prior_bits']:.9f} max_err={ctl['max_abs_error_bits']:.2e}")
    for name, cl in R["main"]["claims"].items():
        log(f"{name}: {cl['verdict']} proportion={cl['proportion']:.4f} "
            f"wilson=[{cl['wilson95'][0]:.4f}, {cl['wilson95'][1]:.4f}] "
            f"t=[{cl['t95'][0]:.4f}, {cl['t95'][1]:.4f}] threshold={cl['threshold']}")

    if not args.no_figures:
        R["figures"] = make_figures(out, R)
        log("figures: " + ", ".join(R["figures"]))
    (out / "results.json").write_text(json.dumps(R, indent=1) + "\n")
    write_markdown(out / "results.md", R)
    log(f"wrote {rel(out / 'results.json')} and {rel(out / 'results.md')}")
    log_path.write_text("\n".join(log_lines) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
