#!/usr/bin/env python3
"""Tally a panel run into a single verdict, by the rules in EPISTEMICS.md.

Refutation is the default. A conjecture does not accumulate support until it
passes; it survives only if a quorum of independent laboratories fails to kill
it. The thresholds live here rather than in a prompt so that they are fixed
before the run, visible in git history, and not adjustable by whichever model
happened to be persuasive.

Aggregation is by MEDIAN across laboratories, not mean across models, so that
one lab's family cannot dominate a panel even if it were somehow over-represented
(panel.py forbids that, but a tally that depends on panel.py being correct is a
tally with a single point of failure).

Standard library only.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import statistics
import sys
from typing import Any

VOTE_RE = re.compile(r"^\s*VOTE:\s*(REFUTED|NOT REFUTED|VACUOUS|ALREADY KNOWN)\s*$",
                     re.IGNORECASE | re.MULTILINE)
CAND_RE = re.compile(r"^\s*CANDIDATE:\s*(.+?)\s*$", re.IGNORECASE | re.MULTILINE)
PROB_RE = re.compile(r"^\s*P\(substantially correct\):\s*([01](?:\.\d+)?)\s*$",
                     re.IGNORECASE | re.MULTILINE)
GATE_RE = re.compile(r"^\s*VERDICT:\s*([A-Z ]+?)(?:\s*[—–-]\s*(.*))?\s*$", re.MULTILINE)

# Gate verdicts that stop a conjecture regardless of the vote. A single FATAL
# is dispositive: the panel is not asked to outvote physics.
FATAL_WORDS = {"FATAL", "VACUOUS", "ALREADY ANSWERED", "WRONG QUESTION"}
MAJOR_WORDS = {"MAJOR", "NO VERDICT LINE", "GATE FAILED TO RUN", "VOTE FAILED TO RUN"}


def parse_votes(outdir: str) -> list[dict[str, Any]]:
    """One record per panellist, for the FIRST candidate block that names the
    subject. Ballots may carry rivals; only the subject's votes are tallied."""
    votes = []
    for name in sorted(os.listdir(outdir)):
        if not name.startswith("vote-") or not name.endswith(".md"):
            continue
        text = open(os.path.join(outdir, name), encoding="utf-8").read()
        model = ""
        m = re.search(r"Reviewer:\s*`([^`]+)`", text)
        if m:
            model = m.group(1)
        lab = ""
        m = re.search(r"lab\s+(\S+)", text)
        if m:
            lab = m.group(1)
        # Split into per-candidate blocks so a rival's vote is never counted.
        blocks = re.split(r"(?=^\s*CANDIDATE:)", text, flags=re.MULTILINE)
        rec = {"file": name, "model": model, "lab": lab,
               "vote": None, "prob": None, "candidate": None}
        for b in blocks:
            cm, vm = CAND_RE.search(b), VOTE_RE.search(b)
            if not (cm and vm):
                continue
            # The subject is whichever candidate the gate verdicts were about,
            # which panel.sh records in the ballot. Absent that, take the first
            # complete block and say so.
            rec["candidate"] = cm.group(1)
            rec["vote"] = vm.group(1).upper()
            pm = PROB_RE.search(b)
            if pm:
                rec["prob"] = float(pm.group(1))
            break
        votes.append(rec)
    return votes


def parse_gates(outdir: str) -> list[tuple[str, str, str]]:
    path = os.path.join(outdir, "verdicts.txt")
    if not os.path.exists(path):
        return []
    rows = []
    for line in open(path, encoding="utf-8"):
        if not line.strip():
            continue
        parts = line.split()
        gate, model = parts[0], parts[1]
        m = GATE_RE.search(line)
        word = (m.group(1).strip().upper() if m else "NO VERDICT LINE")
        detail = (m.group(2) or "").strip() if m else line.strip()
        rows.append((gate, model, f"{word}|{detail}"))
    return rows


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("outdir")
    p.add_argument("--quorum", type=int, default=4,
                   help="laboratories that must fail to refute, for SURVIVES")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()

    votes = parse_votes(a.outdir)
    gates = parse_gates(a.outdir)
    if not votes and not gates:
        sys.exit(f"nothing to tally in {a.outdir}")

    labs = {v["lab"] for v in votes if v["lab"]}
    n_labs = len(labs) or len(votes)
    not_refuted = [v for v in votes if v["vote"] == "NOT REFUTED"]
    vacuous = [v for v in votes if v["vote"] == "VACUOUS"]
    known = [v for v in votes if v["vote"] == "ALREADY KNOWN"]
    unparsed = [v for v in votes if v["vote"] is None]

    fatal = [(g, m, d) for g, m, d in gates
             if d.split("|", 1)[0] in FATAL_WORDS]
    major = [(g, m, d) for g, m, d in gates
             if d.split("|", 1)[0] in MAJOR_WORDS]

    probs = [v["prob"] for v in votes if v["prob"] is not None]
    median_p = statistics.median(probs) if probs else None
    spread = (max(probs) - min(probs)) if len(probs) > 1 else None

    # --- the decision, by EPISTEMICS.md rule 1 --------------------------
    if fatal:
        verdict, why = "REFUTED", f"{len(fatal)} gate(s) returned FATAL"
    elif len(vacuous) >= 2:
        verdict, why = "REFUTED", "panel judged it vacuous"
    elif len(known) >= 2:
        verdict, why = "REFUTED", "panel judged it already known"
    elif len(not_refuted) >= a.quorum:
        if major:
            verdict, why = "WOUNDED", (f"quorum reached ({len(not_refuted)}/{n_labs}) "
                                       f"but {len(major)} gate(s) returned MAJOR")
        else:
            verdict, why = "SURVIVES", f"{len(not_refuted)}/{n_labs} laboratories failed to refute"
    elif len(not_refuted) == a.quorum - 1:
        verdict, why = "WOUNDED", f"only {len(not_refuted)}/{n_labs} laboratories failed to refute"
    else:
        verdict, why = "REFUTED", f"only {len(not_refuted)}/{n_labs} laboratories failed to refute"

    if unparsed:
        why += (f"; {len(unparsed)} vote(s) could not be parsed and were counted "
                "as refutations, because an unreadable vote is not a passing one")

    if a.json:
        print(json.dumps({"verdict": verdict, "why": why,
                          "labs": sorted(labs), "median_p": median_p,
                          "p_spread": spread,
                          "votes": votes, "gates": gates}, indent=2))
        # Exit 0 either way. REFUTED is a successful run of the harness, not a
        # tooling failure, and a non-zero exit here would make CI treat the
        # programme's most valuable output as an error.
        return 0

    out = [f"# Tally: {os.path.basename(os.path.dirname(a.outdir.rstrip('/')))}", "",
           f"**VERDICT: {verdict}** — {why}", ""]
    if median_p is not None:
        line = f"Median P(substantially correct) across laboratories: **{median_p:.2f}**"
        if spread is not None:
            line += f" (spread {spread:.2f}"
            if spread < 0.15:
                line += ", suspiciously tight: check whether the panel is actually independent"
            line += ")"
        out += [line, ""]

    out += ["## Gate verdicts", "", "| Gate | Reviewer | Verdict |", "|---|---|---|"]
    for g, m, d in gates:
        word, detail = (d.split("|", 1) + [""])[:2]
        out.append(f"| `{g}` | `{m}` | **{word}** {detail} |")
    out += ["", "## Panel", "", "| Laboratory | Reviewer | Vote | P |", "|---|---|---|---|"]
    for v in votes:
        prob = "-" if v["prob"] is None else format(v["prob"], ".2f")
        out.append(f"| {v['lab'] or '?'} | `{v['model'] or v['file']}` | "
                   f"**{v['vote'] or 'UNPARSED'}** | {prob} |")
    out += ["", "---", "",
            "Move this conjecture's `status` to match, record the posterior in its",
            "front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.",
            "Refuted conjectures are closed with a reason, never deleted."]
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
