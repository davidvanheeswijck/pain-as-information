#!/usr/bin/env python3
"""Two checks for the P-004 registration. Standard library only. No network.

  python3 registration_checks.py reachability
      Recompute the synthetic examples and the reachability bands of
      REGISTRATION.md section 4, for total widenings from 0 to 2.0.
      Every input is synthetic or already in the repository (the sham
      median and IQR from the abstract). Nothing here is a guess at the paper.

  python3 registration_checks.py carried
      Check that every block of rule text this registration says it carries
      over from P-003 is present here byte for byte. Exit status 1 if not.
"""
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
P003 = HERE.parent / "P-003-sham-pain-against-pre-implant" / "REGISTRATION.md"
P004 = HERE / "REGISTRATION.md"

Z = 1.96
N = 20
SHAM_MEDIAN, SHAM_Q1, SHAM_Q3 = 6.0, 4.0, 7.0


def se_median(q1, q3, n=N):
    """SE of a median from its IQR: SD = IQR / 1.35, SE = 1.2533 * SD / sqrt(n)."""
    return 1.2533 * ((q3 - q1) / 1.35) / math.sqrt(n)


def score(pre_median, pre_q1, pre_q3, widening):
    """Method (C) of the scoring rule, then the verdict rule, in its order."""
    d = pre_median - SHAM_MEDIAN
    se = math.sqrt(se_median(pre_q1, pre_q3) ** 2 + se_median(SHAM_Q1, SHAM_Q3) ** 2)
    half = Z * se + widening
    lo, hi = d - half, d + half
    if d >= 1.0 and lo > 0:
        verdict = "SUPPORTED"
    elif hi < 1.0 or (d <= 0.5 and hi < 2.0):
        verdict = "REFUTED"
    else:
        verdict = "INCONCLUSIVE"
    return d, lo, hi, verdict


# (pre-implant median, Q1, Q3, total widening). The first seven rows are the
# rows of P-003; the rest are added for this registration.
EXAMPLES = [
    (8.0, 7.0, 9.0, 0.0),
    (6.0, 5.0, 7.0, 0.0),
    (7.0, 6.0, 8.0, 0.0),
    (6.5, 5.5, 7.5, 0.0),
    (8.0, 7.0, 9.0, 0.5),
    (7.5, 6.5, 8.5, 0.5),
    (6.0, 5.0, 7.0, 0.5),
    (8.5, 7.5, 9.5, 1.0),
    (8.0, 7.0, 9.0, 1.0),
    (5.5, 4.5, 6.5, 1.0),
    (9.5, 8.0, 10.0, 2.0),
    (8.0, 7.0, 9.0, 2.0),
    (4.5, 3.5, 5.5, 2.0),
]


def fmt(x):
    return f"{x:.2f}".replace("-", "−")


def reachability():
    se_sham = se_median(SHAM_Q1, SHAM_Q3)
    se_pre = se_median(0.0, 2.0)
    se_d = math.sqrt(se_pre ** 2 + se_sham ** 2)
    half = Z * se_d
    print(f"SE sham = {se_sham:.4f}; SE pre-implant (IQR two points wide) = {se_pre:.4f}")
    print(f"SE of D = {se_d:.4f}; half-width = {half:.3f}")
    print()
    print("| Synthetic pre-implant score, n = 20 | Total widening | D | 95% interval | Verdict |")
    print("|---|---|---|---|---|")
    for med, q1, q3, w in EXAMPLES:
        d, lo, hi, verdict = score(med, q1, q3, w)
        print(
            f"| Median {med:.1f} (IQR {q1:.1f} to {q3:.1f}) | {w:.1f} "
            f"| {d:.1f} ".replace("-", "−") +
            f"| {fmt(lo)} to {fmt(hi)} | {verdict} |"
        )
    print()
    print("| Total widening | SUPPORTED when D > | REFUTED when | INCONCLUSIVE between |")
    print("|---|---|---|---|")
    for w in (0.0, 0.5, 1.0, 1.5, 2.0):
        h = half + w
        sup = max(h, 1.0)
        # REFUTED: U < 1.0, or D <= 0.5 and U < 2.0.
        strict = 2.0 - h
        if strict > 0.5:
            ref = "D ≤ 0.50"
            between = f"0.50 < D ≤ {fmt(sup)}"
        else:
            ref = f"D < {fmt(strict)}"
            between = f"{fmt(strict)} ≤ D ≤ {fmt(sup)}"
        print(f"| {w:.1f} | {fmt(sup)} | {ref} | {between} |")
    return 0


# Each carried block is named by the text that starts its first line and the
# text that ends its last line, both as they stand in P-003.
CARRIED = [
    ("the quantity", "**The quantity.** Pain under blinded sham",
     "when pain under sham is lower than pain before implant."),
    ("primary claim and verdict rule", "### Primary claim",
     "under 2, that is, only when U < 1.0."),
    ("verdict rule alone", "### Verdict rule",
     "under 2, that is, only when U < 1.0."),
    ("reachability, as in P-003", "### All three verdicts are reachable",
     "narrower inconclusive band."),
    ("scoring rule (methods A, B, C; construct; widenings; special cases)",
     "### Scoring rule", "and each intermediate standard error to four."),
    ("secondary quantities", "### Secondary quantities (not part of the verdict)",
     "obtained: 0.35."),
    ("request conditions and routes 1 to 4", "Every request is scripted, sends",
     "request per file under the same conditions."),
    ("what full text obtained means", '### What "full text obtained" means',
     "UNSCORABLE (quantity not reported))."),
    ("the outcomes", "### The outcomes",
     "recorded, and it is not a verdict on the claim."),
    ("the stop rule sentence", "**Two registrations that end unscorable",
     "question of closing goes to the owner.**"),
    ("what scoring does not show", "## 6. What scoring does not show",
     "known (§2), and §3 says the test is not severe."),
]


def carried():
    old = P003.read_bytes()
    new = P004.read_bytes()
    bad = 0
    for name, start, end in CARRIED:
        s, e = start.encode(), end.encode()
        i = old.find(s)
        j = old.find(e, i)
        if i < 0 or j < 0 or old.count(s) != 1:
            print(f"FAIL  {name}: markers not found exactly once in P-003")
            bad += 1
            continue
        block = old[i:j + len(e)]
        if block in new:
            lines = block.count(b"\n") + 1
            print(f"ok    {name}: {lines} lines, {len(block)} bytes, identical")
        else:
            print(f"FAIL  {name}: block not present byte for byte in P-004")
            bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "reachability":
        sys.exit(reachability())
    if mode == "carried":
        sys.exit(carried())
    print(__doc__)
    sys.exit(2)
