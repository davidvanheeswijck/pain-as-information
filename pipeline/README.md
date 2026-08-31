# The pipeline

Eight gates, then a five-laboratory vote, then a tally. About thirteen model
calls per conjecture.

    tools/panel.sh conjectures/C-001-your-slug.md

## Gate order, and why it is this order

Cheap kills first. Every gate that runs after a conjecture is already dead is
wasted money, and more importantly a wasted opportunity to learn the cheap
thing first.

| # | Gate | Kills |
|---|---|---|
| 00 | [triage](gates/00-triage.md) | Wrong question, vacuous, already answered, or Branch C laundered as Branch A |
| 01 | [physical plausibility](gates/01-physical-plausibility.md) | Arithmetic. Energy, timescale, field, resolution, signal-to-noise |
| 02 | [biological plausibility](gates/02-biological-plausibility.md) | The nervous system described is not the one that exists |
| 03 | [evidence integrity](gates/03-evidence-integrity.md) | Citations that are real but do not say what they are cited for |
| 04 | [falsifiability](gates/04-falsifiability.md) | Forbids nothing; the proposed test would pass anyway |
| 05 | [prior art](gates/05-prior-art.md) | Known, refuted, or reinvented under a new name |
| 06 | [hostile referee](gates/06-hostile-referee.md) | Everything else, from someone with a grant renewal in six weeks |
| 07 | [clinical translation](gates/07-clinical-translation.md) | Cannot reach a patient, or the effect is below the MCID |

Then:

| # | Gate | Role |
|---|---|---|
| 10 | [panel vote](gates/10-panel-vote.md) | Five laboratories, independently, default REFUTED |
| 08 | [steelman](gates/08-steelman.md) | Run on a WOUNDED conjecture. Rebuild strictly weaker, or declare no core |
| 09 | [generate](gates/09-generate.md) | Run against the evidence base and both ledgers to propose new conjectures |

Gate 01 runs before gate 02 deliberately. A mechanism that fails an
order-of-magnitude estimate does not need a physiologist's time, and gate 01 is
instructed to refuse to discuss biology until the numbers are on the table.

## Laboratory rotation

Each gate runs on a **different laboratory's** model, rotating through the
panel that `tools/panel.py` assembled. One lab's blind spot therefore cannot
shape the whole gate record, and the cost is one call per gate rather than
gates times models.

The panel vote is the opposite: **every** panellist sees the same ballot, and
they are five distinct laboratories by hard constraint. See EPISTEMICS.md
rule 2, and E-06 §2 for the measured result that motivates it.

## The ballot

The vote does not receive "the author's conjecture". It receives a set of
candidates in an order derived from a content hash, unattributed, with the gate
verdicts attached. Add rivals with `--rivals`.

This is not decoration. Sycophancy is a measured property of RLHF-trained
assistants (arXiv:2310.13548), and models are poor at rejecting a false premise
when one is presented as the user's (arXiv:2212.10003). **The fix is to remove
the preference signal, not to ask the model politely to ignore it.**

## Reading a verdict

`pipeline/reviews/<conjecture>/<timestamp>/` holds, for every run:

    panel.json.md     who reviewed, which lab, and what the router reported
    gate-NN-*.md      verbatim gate output, one per gate
    verdicts.txt      the one-line verdicts, in gate order
    ballot.md         exactly what the panel saw
    vote-*.md         verbatim vote output, one per laboratory
    votes.txt         the one-line votes
    SUMMARY.md        the tally

**Nothing here is edited after the fact.** If a model produced a bad verdict,
that is a fact about the panel and it belongs in the record. Every run is
committed, including the failures, including the runs that killed the author's
favourite idea. See ETHICS.md clause 6 for why that is a requirement rather
than a virtue.

## Scoring

Applied by `tools/tally.py`, fixed before the run, in git history, and not
adjustable by whichever model happened to be persuasive:

    SURVIVES   >= 4 of 5 laboratories return NOT REFUTED, and no gate FATAL
    WOUNDED    3 of 5, or any gate MAJOR
    REFUTED    <= 2 of 5, or any gate FATAL

A single FATAL is dispositive. The panel is not asked to outvote physics.

An unparsable vote counts as a refutation, because an unreadable vote is not a
passing one. A gate that fails to run is recorded as a gap and counts as MAJOR,
because a missing verdict must never read as a passing one.

**REFUTED is a successful run.** The tally exits zero either way, so CI never
treats the programme's most valuable output as an error.
