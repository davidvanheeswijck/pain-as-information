# Open state

The honest current position of the programme. Updated after every panel run and
at every tenth conjecture for the progressive-or-degenerating review defined in
PROGRAMME.md.

**Last updated:** 2026-09-01 (second revision)
**Conjectures filed:** 8 · **panelled:** 6 · **refuted:** 6 · **wounded:** 1 · **draft, never panelled:** 1
**Programme status:** not yet assessable (fewer than 10 conjectures)

> **Read the harness-defect section below before reading any verdict on this
> page.** The hostile-referee gate produced reviewable text in **one of six**
> panel runs. Five conjectures were judged without the gate designed to be
> hardest on them, and in two runs the truncation was scored *against* the
> conjecture as an objection no reviewer had made.

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

**Refuted and closed:** C-001 (0.25 → 0.15), C-002 (0.12 → 0.05), C-004
(0.20 → 0.07), C-005 (0.45 → 0.25), C-006 (0.35 → 0.55) and C-007
(0.40 → 0.32). All recorded in [REFUTED.md](REFUTED.md). None deleted.

Note that **C-006 and C-007 carry posteriors that moved in unusual directions**,
and both are honest. C-006's rose because the panel found the flavin bench
experiment *more* likely to succeed than filed, while killing it on a
different axis: gate 02 returned FATAL because the flavin-tryptophan radical
pair requires photoexcitation and is validated only in avian cryptochrome, so
no mechanism was offered by which it forms in mammalian nociceptive tissue.
The physics was fine; the biological bridge was absent. C-007 fell only
modestly because it was killed at triage as still the wrong question, with a
better one supplied.

**The single live conjecture.**

| id | branch | prior | posterior | status |
|---|---|---|---|---|
| [C-003](../conjectures/C-003-allodynia-eligibility-window.md) | A | 0.30 | **0.62** | wounded |

**C-003 is the only conjecture in this programme whose probability rose under
adversarial review**, and it is now the most interesting live object here. It
proposes that mechanical allodynia is a coincidence phenomenon in time: ongoing
C-fibre discharge opens a window of a few hundred milliseconds during which
otherwise-normal Aβ touch input is routed to nociceptive output.

**Its wounding needs re-reading, because three of its five negative gates are
artefacts rather than objections.**

| Gate | Recorded | Actually |
|---|---|---|
| 01 physical plausibility | NO VERDICT LINE → MAJOR | **Harness truncation.** Empty content, `out=8192`. No reviewer said anything. |
| 02 biological plausibility | MAJOR | **Real, and the strongest objection.** C-fibre-evoked dorsal-horn facilitation is either short (paired-pulse, tens of ms) or long (central sensitisation, minutes to hours). The proposed few-hundred-millisecond constant sits in a gap with no direct evidence. |
| 03 evidence integrity | MAJOR | **Verified false positive.** The gate claimed Ghitani et al. (PMID 40269164) does not propose temporal coincidence. The abstract says "coincident with touch". Checked against NCBI directly. |
| 04 falsifiability | MAJOR | **Real.** False-pass probability estimated ~0.6; the killer as written does not discriminate. |
| 06 hostile referee | NO VERDICT LINE → MAJOR | **Harness truncation.** No file was written at all. |

So C-003 stands on **two real objections, not five**, and both are about the
*design of the test* rather than the truth of the claim: an unevidenced time
constant, and a killer too weak to discriminate. Neither touches the
contradiction that motivated it, which remains live in the literature.

**What C-003 needs, and it is cheap.** Not a new conjecture. A rewritten
Killer with (a) a pre-registered facilitation time constant justified from
published paired-pulse and wind-up data, or an explicit sweep across the
disputed range, and (b) a design that lowers false-pass probability below ~0.2,
which the Rivals section already contains but the Killer does not import.
Then re-panel it with a working hostile-referee gate.

**Never panelled:** [C-008](../conjectures/C-008-interference-rejection-not-sensitivity.md)
(branch B, prior 0.35), which claims that gradiometric interference rejection
rather than sensor sensitivity is what blocks magnetic detection of C-fibre
traffic. It is lint-clean and its killer is a simulation extension costing a
day of compute and no money. It is the cheapest open item in the programme.

## Harness defects, open

**D-H1. The hostile-referee gate has produced reviewable text once in six
runs.** Present and substantive for C-005 (9,736 bytes). A 411-byte header with
an empty body for C-003. **Absent entirely** for C-001, C-002, C-006 and C-007.

Root cause, reproduced: reasoning-tier models consume the entire completion
budget on hidden thinking and return HTTP 200 with `content: ""` and
`finish_reason: length`. The C-003 stub records `tokens in=7794 out=8192`, a
full budget spent with nothing emitted. The hostile-referee prompt is not the
longest (3,068 bytes, smaller than gates 01, 04 and 07), so this is reasoning
demand rather than prompt size.

**The second-order defect was worse than the first.** `review.sh` wrote the
empty response to disk as a headed but bodiless file and emitted
`VERDICT: NO VERDICT LINE — treat as MAJOR`. Failing closed is right for a
*missing* verdict, but this was not a missing verdict from a reviewer that ran;
it was a reviewer that never spoke. The harness manufactured an objection and
scored it against the conjecture. C-003 absorbed two of these.

**Fixed 2026-09-01** in `tools/review.sh`: empty or `finish_reason: length`
responses are now detected, retried once at 32,000 output tokens, and if still
empty the run **exits 3 with `GATE TRUNCATED`** rather than producing a
scoreable verdict. Verified by replaying the actual truncated C-003 response
against the detector, and confirming a well-formed response still scores.

**Still outstanding:** C-001, C-002, C-006 and C-007 were never seen by a
hostile referee. C-006 and C-007 died on other gates and a FATAL from gate 02
is decisive regardless, so re-running is optional for those. **C-003 should be
re-panelled** once its Killer is rewritten, because it is the survivor and it
is the one whose score the defect most distorted.

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
