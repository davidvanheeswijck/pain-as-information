#!/usr/bin/env python3
"""Three checks for the P-004 registration. Standard library only. No network.

  python3 registration_checks.py reachability
      Recompute the synthetic examples and the reachability bands of
      REGISTRATION.md section 4, for total widenings from 0 to 2.0.
      Every input is synthetic or already in the repository (the sham
      median and IQR from the abstract). Nothing here is a guess at the paper.

  python3 registration_checks.py carried
      Check that every block of rule text this registration says it carries
      over from P-003 is present here byte for byte. Exit status 1 if not.

  python3 registration_checks.py selftest
      Negative test of the carried check. For each carried block, take a copy
      of the registration in memory, change one character inside that block,
      and confirm that the carried check then reports a mismatch (its inner
      exit status is 1). Nothing on disk is changed. Prints PASS and exits 0
      if every mutation is caught; prints FAIL and exits 1 otherwise.
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


def fmt(x, places=2):
    return f"{x:.{places}f}".replace("-", "−")


def reachability():
    se_sham = se_median(SHAM_Q1, SHAM_Q3)
    se_pre = se_median(0.0, 2.0)
    se_d = math.sqrt(se_pre ** 2 + se_sham ** 2)
    half = Z * se_d
    print(f"SE sham = {se_sham:.4f}; SE pre-implant (IQR two points wide) = {se_pre:.4f}")
    print(f"SE of D = {se_d:.4f}; half-width = {half:.4f} (printed as {half:.3f} or {half:.2f})")
    print()
    print("| Synthetic pre-implant score, n = 20 | Total widening | D | 95% interval | Verdict |")
    print("|---|---|---|---|---|")
    for med, q1, q3, w in EXAMPLES:
        d, lo, hi, verdict = score(med, q1, q3, w)
        print(
            f"| Median {med:.1f} (IQR {q1:.1f} to {q3:.1f}) | {w:.1f} "
            f"| {fmt(d, 1)} | {fmt(lo)} to {fmt(hi)} | {verdict} |"
        )
    print()
    print("Bands, rounded to two decimals (the value to three decimals in brackets):")
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
            ref = f"D < {fmt(strict)} ({fmt(strict, 3)})"
            between = f"{fmt(strict)} ≤ D ≤ {fmt(sup)}"
        print(f"| {w:.1f} | {fmt(sup)} ({fmt(sup, 3)}) | {ref} | {between} |")
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


def block_from_p003(old, start, end):
    """The carried block as bytes, or None if its markers are not found once."""
    s, e = start.encode(), end.encode()
    i = old.find(s)
    j = old.find(e, i)
    if i < 0 or j < 0 or old.count(s) != 1:
        return None
    return old[i:j + len(e)]


def carried_check(old, new, out=print):
    """Return 0 if every carried block of `old` is in `new` byte for byte, else 1."""
    bad = 0
    for name, start, end in CARRIED:
        block = block_from_p003(old, start, end)
        if block is None:
            out(f"FAIL  {name}: markers not found exactly once in P-003")
            bad += 1
        elif block in new:
            lines = block.count(b"\n") + 1
            out(f"ok    {name}: {lines} lines, {len(block)} bytes, identical")
        else:
            out(f"FAIL  {name}: block not present byte for byte in P-004")
            bad += 1
    return 1 if bad else 0


def carried():
    return carried_check(P003.read_bytes(), P004.read_bytes())


def selftest():
    """Mutate one character inside each carried block, in memory, and require
    the carried check to fail and to name that block."""
    old = P003.read_bytes()
    new = P004.read_bytes()
    if carried_check(old, new, out=lambda _line: None) != 0:
        print("FAIL  selftest needs a passing carried check to start from")
        return 1
    missed = 0
    for name, start, end in CARRIED:
        block = block_from_p003(old, start, end)
        at = new.find(block) + len(block) // 2
        # Step to an ASCII letter or digit so that one byte is one character.
        while not (new[at:at + 1].isalnum() and new[at] < 128):
            at += 1
        before = new[at:at + 1]
        after = b"X" if before != b"X" else b"Y"
        mutated = new[:at] + after + new[at + 1:]
        lines = []
        status = carried_check(old, mutated, out=lines.append)
        named = any(line.startswith("FAIL") and f" {name}:" in line for line in lines)
        offset = at - new.find(block)
        if status == 1 and named:
            print(
                f"caught  {name}: byte {offset} of the block changed "
                f"{before.decode()!r} -> {after.decode()!r}; inner check exit {status}"
            )
        else:
            print(f"MISSED  {name}: inner check exit {status}, block named: {named}")
            missed += 1
    unchanged = P004.read_bytes() == new
    print(f"file on disk unchanged: {unchanged}")
    if missed or not unchanged:
        print("FAIL")
        return 1
    print(f"PASS  {len(CARRIED)} of {len(CARRIED)} one-character mutations caught")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "reachability":
        sys.exit(reachability())
    if mode == "carried":
        sys.exit(carried())
    if mode == "selftest":
        sys.exit(selftest())
    print(__doc__)
    sys.exit(2)
