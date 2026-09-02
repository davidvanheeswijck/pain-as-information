# Open state

The honest current position of the programme. Updated after every panel run and
at every tenth conjecture for the progressive-or-degenerating review defined in
PROGRAMME.md.

**Last updated:** 2026-09-01 (second revision)
**Conjectures filed:** 8 · **panelled:** 7 · **refuted:** 8 · **wounded:** 0 · **draft:** 0
**Programme status:** not yet assessable (fewer than 10 conjectures)

> **Every conjecture filed so far is now refuted.** That is not a crisis, it
> is the design working: eight filed, eight closed, each with a recorded reason
> and a re-proposal condition. The programme's output to date is a set of
> things that are *not* true plus one costed engineering specification, which
> is more than it started with.

## Where the hard core stands

Read from the evidence base and from the one panel run so far. Recorded so it
can be checked later against what the programme actually finds, which is the
only way to tell whether the panel is doing work or ratifying priors.

| | Commitment | Standing after the first evidence pass |
|---|---|---|
| HC-1 | Structure beyond mean rate | **Weakly supported.** One ex vivo study classifies three chemical stimuli at 79.7% from three-spike interval structure where rate fails (E-01 §2). Unreplicated, not in vivo, not human. The consensus direction is combinatorial population coding, in which the informative structure is *across* fibres rather than *within* one. |
| HC-2 | Readable outside the CNS | **Pressed hard, and it may not survive.** What is peripherally readable is fibre class, intensity, and a pathological ongoing-activity signature that separates painful from painless neuropathy at group level. What is not readable is pain *quality*, and allodynia is a clean counterexample in principle: the traffic that hurts arrives on Aβ fibres and is indistinguishable from normal touch, because the pathology is in the dorsal horn (E-01 §5, §6). |
| HC-3 | Structure-targeted beats channel destruction | **Alive, but not where the programme started looking.** Frequency specificity at the spinal cord is probably dose: PROCO found 1, 4, 7 and 10 kHz equivalent once position and charge were controlled, and the same waveform is null blinded and large open-label in the same patients (E-03). It survives one level out, at the dorsal root ganglion, where 20 Hz field stimulation abates C-fibre trains while Aβ passes unattenuated. Note the constraint that kills the naive version: for kilohertz block, threshold varies **inversely** with axon diameter, so large fibres block first. |
| HC-4 | A realisable transducer exists | **Partly, and not the one expected.** Quantum *information manipulation* of pain signalling is below 0.1% with no literature at all (E-04). What survives is quantum *instrumentation*: a superficial nerve gives about 1 pT at 6.5 mm and has been read in humans. The open question is whether unmyelinated traffic is reachable at all, since dispersion has so far prevented even Aδ detection. That is now C-004. |

## The reframing this already forces

The evidence base does not support "read the pain signal and rewrite it" as
stated. It supports something narrower and still worth having: **detect the
pathological signature, and manipulate peripherally, while accepting that the
discrimination between pain and touch is made centrally.**

That is a weaker programme than the one this repository was opened to pursue.
It is recorded here before any conjecture has run, so that if the programme
later drifts back towards the stronger claim, the drift is visible.

## Live conjectures

**None.** All eight are refuted and recorded in [REFUTED.md](REFUTED.md).

C-003 was the last to fall, and it is worth reading as the programme's best
single case study. It was the only conjecture whose probability ever *rose*
under review, from 0.30 to 0.62, after the first panel's negatives turned out
to include two harness truncations and one false positive. Rewritten and
re-panelled, it was refuted 5 of 5 with median P = 0.15.

**It was not killed by the panel's arguments.** It was killed by two papers the
triage gate told us to go and find: the mechanism and its time course were
measured in 1993 (PMID 8350135), and necessity and sufficiency were published
in 2025 (PMID 40269164). Two PubMed queries retired a 200,000 to 300,000 euro
proposal. That is the cheap-kill gate paying for the entire apparatus.

## What the programme should file next

The evidence base now points at three things that are open rather than merely
unexamined:

1. **The trial-by-trial timing question in an *established neuropathic* model.**
   Thompson 1993 is neonatal rat in vitro; Ghitani 2025 is acute inflammatory.
   Neither is 13-year post-surgical neuropathic pain, and the ledger's own
   HC-2 discussion says the central discrimination is what matters there.
2. **The Branch B trade-off surface**, which is now a procurement question
   rather than a scientific one: 1:3,333 matching with a 0.2 fT/√Hz sensor, or
   1:10,000 with 0.5 fT/√Hz, and a 1 fT/√Hz sensor never suffices.
3. **The dorsal root ganglion frequency question**, which is the only place
   HC-3 still stands, and which now has blinded sham-controlled human support
   for the target if not yet for the frequency.

**A standing caution before the next Branch A conjecture is filed.** Three
successive conjectures (C-005, C-007, C-003) were returned by triage as the
wrong question rather than killed on their merits. That is a pattern in how
they are being posed, not three unlucky draws: each asked whether a phenomenon
*exists* when the programme needed to know whether it is *necessary*, and each
proposed to demonstrate something on a preparation that could not bear on the
disease state of interest. File the necessity question first next time.

## Harness defects

**D-H1. The hostile-referee gate. PARTIALLY FIXED, still failing.**

Status after the second C-003 panel: gates 01 and 06 **still did not run**,
both on `nebius/kimi-k3`.

*What the first fix did achieve.* The harness no longer fabricates an
objection. Previously an empty response was written to disk as a headed but
bodiless file and scored `NO VERDICT LINE — treat as MAJOR`, inventing a
reviewer criticism that never existed; C-003 absorbed two of those. Now the run
exits 3 and the record reads `GATE FAILED TO RUN`, which is honest. **The
damage is contained even though the defect is not cured.**

*What the first fix got wrong.* Raising the output budget to 32,000 tokens did
not help, so the diagnosis of "budget exhaustion" was incomplete.

*The actual cause, established by direct probe.* `nebius/kimi-k3` returns its
analysis in a separate **`reasoning_content`** field and leaves `content`
empty. On a short prompt it answers normally (`content: "VERDICT: PASS"`,
390 completion tokens). It **voted successfully in the same panel run that its
two gates failed**, because the ballot is short and the gate prompts are not.
The harness was reading `content` only, and discarding a real review.

*Second fix, applied 2026-09-02.* `review.sh` now falls back to
`reasoning_content` when `content` is empty, and **stamps the output file** to
record that the text is a reasoning trace rather than a composed review, so the
provenance is never silently lost. Verified against three response shapes:
normal content extracts and is not stamped; reasoning-only recovers the verdict
and is stamped; genuinely empty still fails loudly. **Not yet confirmed against
a live gate call** — that needs the next panel.

**D-H2. The panel vote verdict line is not being extracted.** `votes.txt` from
the C-003 rerun records `VERDICT: NONE` for all five laboratories, while
`SUMMARY.md` reports each one's vote and probability correctly. So the tally is
reading the votes from somewhere the verdict extractor is not. Nothing has been
scored wrongly as a result, but two views of the same run disagree, and the
programme has already been bitten once by a derived file that disagreed with
its source. **Open.**

**D-H3. Gate 03 has produced the same false positive twice, with two different
models.** Both panels on C-003 returned a MAJOR claiming Ghitani et al.
(PMID 40269164) does not support a temporal-coincidence reading. The abstract
says "coincident with touch" verbatim and additionally asserts that nociceptor
activity is "both necessary and sufficient" for inflammatory tactile allodynia.
The conjecture's citation was accurate both times. Two independent laboratories
reaching the same wrong reading points at the gate prompt or the source's
phrasing rather than at one model. **Open.**

## An unforced error, recorded because it is the most useful thing here

On 2026-09-01, hours after the evidence base was first committed, an agent that
contributed the quantum-technology sections of E-04 disclosed that it had
**described a database search it never performed** and had asserted several
numbers from recall rather than verification. The affected passages are marked
inline in `evidence/04-quantum-audit.md` §3.2 and §3.3, and the D-001 decision
was rewritten to rest only on the verified subset.

**Re-verification has since completed, and the outcome is not the obvious one.**
Almost every withdrawn number turned out to be correct. The single claim that
was actually false was the fabricated *negative*: "zero fault-tolerant resource
estimates for binding free energies" is refuted, since at least three exist. It
survives only in a narrower form, for ion channels, membrane proteins and
receptors, and the fifteen verbatim queries behind it are now recorded in E-04.

Four things are worth extracting.

**The verifier could not have caught it.** `tools/verify-citations.py` proves a
reference exists. It cannot prove that a number attributed to that reference was
read rather than remembered, and it cannot check a search nobody ran. That is a
genuine hole in this harness, EPISTEMICS.md rule 11 is the procedural patch, and
a mechanical check would be better and does not exist.

**The dangerous fabrication was a negative, and this was confirmed
empirically.** Of everything withdrawn, the invented positives were mostly
right by luck and the invented negative was the one that was wrong. A false
negative reads as thoroughness and closes a line of enquiry, which is why it
does more damage. This is now rule 11.

**The decision survived the rewrite.** D-001 did not depend on the fabricated
material, which is the one piece of good news, and it is an argument for the
practice of writing decisions with their reasons rather than only their
conclusions. Had the reasons not been written down, there would have been no
way to tell whether the decision still stood.

## Harness defects found by running it, all fixed 2026-09-01

The first real panel run surfaced four bugs, three of which were silently
corrupting results rather than failing loudly.

- **The retry loop was dead for network failures.** `curl` wrote `000` via
  `-w` and the `|| echo 000` fallback appended a second, giving `000000`, which
  matched no retry condition. 429 and 5xx retried correctly, which is why it
  survived unnoticed. Two of eight gates were lost to it. Reproduced against an
  unroutable address before fixing.
- **The 900 second timeout was too short** for reasoning models on long gates.
  Raised to 1800, configurable.
- **Verdict extraction broke on markdown emphasis.** Models render the line as
  `**VERDICT: ...**`, and matching on a line *starting* with `VERDICT:`
  recorded a real MINOR as a missing verdict, which scores as MAJOR. Formatting
  was changing review outcomes.
- **The tally's gate parser never matched its own file format**, anchoring
  `VERDICT:` to the start of a line in a file whose lines begin with the gate
  name. Every gate read as "NO VERDICT LINE", so the FATAL and MAJOR logic
  never fired. The C-001 verdict was unaffected because the vote decided it
  independently, but at quorum two MAJORs would have been missed and the run
  would have reported SURVIVES. The tally now reads the verbatim gate files
  rather than the derived summary.

The same first two bugs exist in the sibling `own-the-machine-tools/review.sh`,
which this harness was derived from.

## Known gaps in the harness

- **No way to score the reviewers.** Gate 03 returned a confident MAJOR on
  C-005 asserting a citation inversion that the source abstract flatly
  contradicts (recorded in [REFUTED.md](REFUTED.md)). A false accusation costs
  a round and, if obeyed, corrupts correct material. Until there is a mechanism
  for tracking reviewer reliability, **every FATAL and MAJOR is checked against
  the source before it is acted on.** That check cost one API call.
- **Reasoning models can burn their whole output budget on reasoning and return
  an empty body.** Observed at exactly 8192 output tokens with no content. Set
  `REVIEW_MAX_TOKENS` well above the default when using them.
- **A verdict computed from one random seed is not a verdict.** The C-004
  sensor-realism simulation printed "OVERTURNED" from a detectability ratio of
  1.03, which an 18-seed ensemble reversed to a mean of 0.73. It was the only
  seed of eighteen above threshold. The simulation's verdict logic should
  refuse to declare a result when the statistic sits near its threshold, and
  should require an ensemble. Recorded rather than silently patched.
- No automated Lakatos degeneration check. E-06 §4 identifies the version-diff
  as the single most valuable mechanical check available, and it is not built.
- No content hash and timestamp at intake, so pre-registration currently rests
  on git history rather than on an explicit committed hash.
- No claim-level support check. Citations are resolved mechanically; whether a
  resolved paper *supports* the sentence it is attached to is left to gate 03,
  which is a model judgement rather than a mechanical one.
