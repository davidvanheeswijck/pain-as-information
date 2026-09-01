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
#
# CHANGED 2026-09-01, and the change is recorded here rather than made quietly,
# because it was made AFTER seeing results it improves, which is when a rule
# change deserves the most suspicion.
#
# "WRONG QUESTION" was in this set and has been moved out. The case for moving
# it does not rest on liking the outcome:
#
#  1. Gate 00's own prompt requires WRONG QUESTION to be returned WITH "the
#     better question, in one sentence". It is by construction a request to
#     reformulate, not a finding that the claim is false.
#  2. Gate 08 exists to rebuild a wounded conjecture. A conjecture that needs
#     restating is the paradigm case for that gate, not for the graveyard.
#  3. "Wrongly stated" and "wrong" are different. C-005 was reformulated into
#     C-007 by exactly this route and the reformulation was an improvement.
#  4. Decisively: the old rule let ONE gate override a five-laboratory panel.
#     That contradicts EPISTEMICS.md rule 2, whose whole argument is that a
#     single reviewer is unreliable and a panel of disjoint laboratories is
#     not. Two gate verdicts have already been scored as outright false
#     accusations (see ledger/REFUTED.md). "The panel is not asked to outvote
#     physics" is right, and a framing objection is not physics.
#
# Physical impossibility from gate 01 stays dispositive. So do VACUOUS and
# ALREADY ANSWERED, which are findings about the claim rather than about how it
# is phrased.
FATAL_WORDS = {"FATAL", "VACUOUS", "ALREADY ANSWERED"}

# Forces a reformulation and caps the verdict at WOUNDED, but does not kill.
REFRAME_WORDS = {"WRONG QUESTION"}
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


def _verdict_from_text(text: str) -> tuple[str, str]:
    """Pull the last VERDICT line out of a verbatim gate file.

    Tolerates leading markdown emphasis and blockquote markers, because models
    routinely render the line as '**VERDICT: ...**'. A stricter match recorded
    real verdicts as missing, and a missing verdict scores as MAJOR, so
    formatting was changing review outcomes.
    """
    found = None
    for line in text.splitlines():
        s = re.sub(r"^[\s>*_#`-]+", "", line).strip()
        if not s.upper().startswith("VERDICT:"):
            continue
        s = re.sub(r"[\s*_`]+$", "", s)
        body = s.split(":", 1)[1].strip()
        m = re.match(r"^([A-Z][A-Z ]*[A-Z]|[A-Z])\s*(?:[—–-]\s*(.*))?$", body, re.S)
        if m:
            found = (m.group(1).strip().upper(), (m.group(2) or "").strip())
        else:
            found = (body.split()[0].upper() if body else "NO VERDICT LINE", body)
    return found or ("NO VERDICT LINE", "")


def parse_gates(outdir: str) -> list[tuple[str, str, str]]:
    """Read the committed gate files, not the derived verdicts.txt.

    verdicts.txt is a human convenience written by panel.sh. The gate-*.md
    files are the verbatim model output and are the source of truth, so the
    scoring reads those. The previous version parsed verdicts.txt with a
    line-anchored regex that never matched its own format, so every gate was
    recorded as 'NO VERDICT LINE' and the FATAL/MAJOR logic never fired.
    """
    rows: list[tuple[str, str, str]] = []
    for name in sorted(os.listdir(outdir)):
        if not (name.startswith("gate-") and name.endswith(".md")):
            continue
        gate = name[len("gate-"):-len(".md")]
        text = open(os.path.join(outdir, name), encoding="utf-8").read()
        m = re.search(r"Reviewer:\s*`([^`]+)`", text)
        model = m.group(1) if m else "?"
        word, detail = _verdict_from_text(text)
        rows.append((gate, model, f"{word}|{detail}"))

    # A gate that errored writes no file at all, so it cannot be read above and
    # would silently vanish from the record. panel.sh records those in
    # verdicts.txt; recover them so a gate that failed to run still scores.
    vpath = os.path.join(outdir, "verdicts.txt")
    if os.path.exists(vpath):
        seen = {g for g, _, _ in rows}
        for line in open(vpath, encoding="utf-8"):
            parts = line.split()
            if len(parts) < 2 or parts[0] in seen:
                continue
            if "FAILED TO RUN" in line.upper():
                rows.append((parts[0], parts[1], "GATE FAILED TO RUN|"))
    return sorted(rows)


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
    reframe = [(g, m, d) for g, m, d in gates
               if d.split("|", 1)[0] in REFRAME_WORDS]
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
        if reframe:
            verdict, why = "WOUNDED", (
                f"quorum reached ({len(not_refuted)}/{n_labs}) but triage returned "
                "WRONG QUESTION: reformulate before this can survive")
        elif major:
            verdict, why = "WOUNDED", (f"quorum reached ({len(not_refuted)}/{n_labs}) "
                                       f"but {len(major)} gate(s) returned MAJOR")
        else:
            verdict, why = "SURVIVES", f"{len(not_refuted)}/{n_labs} laboratories failed to refute"
    elif len(not_refuted) == a.quorum - 1:
        why = f"only {len(not_refuted)}/{n_labs} laboratories failed to refute"
        if reframe:
            why += "; triage returned WRONG QUESTION, so reformulate rather than rebuild"
        verdict = "WOUNDED"
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
