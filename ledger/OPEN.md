# Open state

The honest current position of the programme. Updated after every panel run and
at every tenth conjecture for the progressive-or-degenerating review defined in
PROGRAMME.md.

**Last updated:** 2026-11-17 (S-1 recorded)
**Conjectures filed:** 9 · **panelled:** 7 (eight runs; C-003 twice) · **refuted:** 9 · **wounded:** 0 · **draft:** 0
**Programme status:** not yet assessable (fewer than 10 conjectures)

> **Every conjecture filed so far is now refuted.** That is not a crisis, it
> is the design working: nine filed, nine closed, each with a recorded reason
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

**None.** Nine filed, nine refuted, each closed with a reason and a
re-proposal condition.

C-009 is the most recent and the most instructive. It was built on a real human
result, filed after the cheap literature check that C-003 taught the programme
to run first, and killed anyway because **the design could not do what the
claim required**. A complete sensory block removes ordinary touch along with
any pathological traffic, so it cannot separate a peripheral generator from
central reinterpretation of normal input.

**The pattern in how these are being posed is now unambiguous.** Four
consecutive conjectures were returned by triage as the wrong question:

| | asked | should have asked |
|---|---|---|
| C-005 | how many bits does a nociceptor carry | does timing beat rate on the same data |
| C-007 | does single-fibre timing add information | does across-fibre structure predict the percept |
| C-003 | does a coincidence window exist | is ongoing activity necessary for allodynia |
| C-009 | is pain input-dependent | does *selective* suppression beat *nonselective* blockade |

The progression is real: existence, then necessity, and now **specificity**.
Each time the programme asked whether something is true when it needed to know
whether the measurement could tell the difference. **The next conjecture should
be checked against that column before it is filed**, not after.

## Simulations

**S-1, DRG T-junction rate versus pattern: NO VERDICT, positive control failed.**
2026-11-17, `simulations/S-001-tjunction-rate-vs-pattern/`, PR #3.

- **Controls.** The model reproduces Sundt 2015's following frequencies: 89, 32 and 6.6 Hz against 110, 30 and 6. Removing SK breaks the 6 Hz control, as it should. The Chao 2020 qualitative control fails. Block is essentially immediate (median 0.56 s, F about 0.99 even at 4 Hz), not progressive, so P1 and P2 cannot be scored. The dt-halving check also failed, with one classification flip.
- **Run 1 is void.** It counted evoked spikes on the soma side of the stimulus site, found in review. It is kept in `results/run1-void-site-defect/`. Its "lost drive at 80 Hz" explanation was an artefact of that defect.
- **Conditional readings from run 2, not verdicts.** Matched-rate patterns sit within about 3 points of regular 20 Hz, at a ceiling. F falls from 20 to 80 Hz with the stimulus still driving the stem. The size of that fall depends on the probe-exclusion rule: F goes 0.96 to 0.05, F_all goes 0.88 to 0.43, and at 80 Hz excluded probes fail at 0.59 against 0.05 for scored ones. A mechanism that blocks C-type traffic almost completely at 4 Hz is not an account of the blinded human frequency ordering.
- **Standing.** S-1 neither supports nor refutes the T-junction account, and C-001 stays refuted. Do not cite S-1 as evidence for or against pattern-specific ganglion stimulation.
- **Next.** A model that could pass this control must keep Sundt's ~6 Hz following frequency *and* block over tens of seconds. The re-tuning route was tried as S-1b (below) and found nothing within its budget. That leaves a longer or wider search of the same space, or the rival ion-gradient run-down mechanism (Ladez, Liu, Chen & Feng, EMBC 2024, PMID 40039770), which reports conduction slowing leading to eventual block. Either needs its own pre-registered run.
- **Known gap.** The generated "(c)" paragraph in `results.md` does not itself carry the caveat that the size of the fall depends on the exclusion rule. The caveat is in the table note and in PREDICTION.md's correction to amendment E.

**S-1b, re-tuned T-junction model: no tuning found within the budget, P1 and P2 not run.**
2026-11-17, `simulations/S-001b-tjunction-retuned/`, PR #9.

- **Search.** The calibration targets were Sundt 2015's three following frequencies and a progressive block at regular 20 Hz, 1.5×, read from Chao 2020 ("progressively abated over 20 seconds"). The search was a 240-candidate Latin hypercube plus 96 local candidates over nine parameters. The selection score used calibration targets only. Two checks were held out, named in advance, and not reached: the stimulation-frequency dependence in Kent 2018 and the cumulative failure in Gemes 2013.
- **Result.** 0 of 336 candidates met every target. 22 reached the calibration run. Of those, 19 block in under 2 s and none keeps F in the first 5 s at or below 0.50. The nearest miss, candidate 1035, sits inside all three Sundt bands with block onset at 5.2 s and F_early 0.75, missing B1 by 0.25.
- **How far it reaches.** The search stopped at its pre-registered budget, not at convergence. The local round 2 produced all five best candidates (best J 2.52 against 4.12 in round 1), so the score was still improving. Twenty-two evaluated points in nine dimensions is a thin sample. Stimulus amplitude, stimulus site and rate were not search dimensions. 55 candidates were stopped within one 6% grid step beyond a band edge. This is a search result, not an exhaustive scan, and not a result about patients.
- **Standing.** S-1's NO VERDICT stands, and C-001 stays refuted. The quick re-tune inside this channel set did not rescue S-1. It is not shown to be impossible.
- **Next.** Two candidates, each needing its own pre-registration: a longer or finer search of this space, starting near candidate 1035, or the slower ion-gradient mechanism (PMID 40039770). This is a pointer, not a conclusion.

**S-2, dorsal-horn model of touch-evoked pain: NO VERDICT, positive control failed by its own design.**
2026-11-18, `simulations/S-002-dorsal-horn/`, PR #12.

- **Model.** A Python port of Zhang, Janik & Grill 2014 (ModelDB 168414): afferents, two substantia gelatinosa interneurons, an inhibitory interneuron and a wide-dynamic-range projection neuron. The port is faithful as far as checked: a reviewer built the original hoc network and got identical control numbers. That cross-check is the reviewer's result. It is not reproduced in the repository; the coder's own run was blocked by a permission check.
- **Control.** Wind-up passes. The pre-registered A-fibre inhibition feature fails: 19.4 spikes per cycle with A fibres against 11.3 without. The cause is the control's design, not the model. It counted Aβ and Aδ together. In the published network Aβ inhibits via an interneuron (8.0 against 11.3 when Aβ is added alone), while Aδ excites the projection neuron directly (23.3). P0 to P3 were not run.
- **Stimulation driver.** The pre-registered driver pulsed the Aβ fibres. The authors' shipped input applies the stimulation pulses to a separate inhibitory surround input. The pilot's "excites at every frequency" is therefore expected from the wiring, and it is not evidence about the published 30 to 100 Hz window. This comes from the data file, not from a simulation.
- **Pilot, not results.** Touch-evoked onset fell between 0 and 10 mV of anion shift in the unmodified model. The pre-registered C-input drive grid could not reach its target band.
- **Standing.** Nothing about allodynia, ganglion stimulation or fading benefit was tested. Questions 1 to 3 of the S-2 intent remain open.
- **Next.** Run a fresh pre-registration with three changes: an Aβ-only versus Aδ-only decomposition of the control, a stimulation driver on the surround input as the authors' data show, and a C-input drive grid of about 0.5 to 2 Hz per fibre. Commit an original-hoc oracle script alongside it, as a hard requirement.

**S-3, generator discrimination: kill TRIGGERED, positive control passed.**
2026-11-17, `simulations/S-003-generator-discrimination/`, PR #6. A decision-analysis model, not biophysics.

- **Inputs.** Of 24 likelihood parameters, 4 are anchored on an abstract and 20 are elicited. The prior is elicited in full.
- **Result.** Across 4,000 draws, the best sequence of at most three available observations, fixed or adaptive, yields a median 0.797 bits of a possible 1.900. That removes about 42% of prior entropy, and it reaches the pre-registered 1 bit in 0.040 of draws. No single test reaches 1 bit in any draw. Within this model's ranges, the available observations do not localise the generator. Whether 0.8 bits is clinically useful is a separate question.
- **The specificity column, answered for this question.** No available observation separates a peripheral lesion (H1) from central amplification of normal input (H3): the median pairwise error with every test together is 0.234. Blocks and the ganglion-directed test cannot separate the two by construction (C-009). Only imaging and, weakly, stimulation on/off bear on that pair. P3 depends on the prior: it holds in 0.964 of draws under the pre-registered prior and 0.636 under a flat prior.
- **Ranking.** A comparative block plus the ganglion-directed test is the top pair in 0.779 of draws. The ganglion-directed test is a research procedure. Without it, the best of three is a median 0.647 bits.
- **Standing.** This describes how the ranking behaves across elicited ranges. Do not cite it as a measured accuracy of any test, and not as a protocol.
- **Known gaps.** A 60-draw pilot was seen before the code commit. The pre-registered P3 measure mixes prior imbalance with test performance. The 30% false-positive anchor comes from zygapophysial joint blocks. Conditional independence between tests flatters sequences.

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

**D-H1. The hostile-referee gate. FIXED AND CONFIRMED LIVE, 2026-09-02.**

**The C-009 panel produced the first complete gate record in this programme's
history: all eight gates returned a verdict.** Before it, the hostile-referee
gate had produced reviewable text in one of seven attempts, so five conjectures
were judged without the reviewer designed to be hardest on them.

*Confirmation, from the run log.* Gates 01 and 06 both drew `nebius/kimi-k3`,
both took `HTTP 504` from the gateway, both retried at 20s and 60s, both still
failed, and both were then **recovered on the fallback laboratory** with the
substitution recorded in the verdict line:

> `note: gate 06-hostile-referee failed on nebius/kimi-k3, recovered on azure/openai-responses/gpt-5.6-sol@swedencentral`

*And the gate immediately earned its cost.* Its first successful verdict in
eight attempts was a **FATAL at 97% confidence** that killed C-009 on a defect
no other gate had stated so decisively: a complete sensory block cannot
distinguish a pathological peripheral generator from central reinterpretation
of ordinary input, because it removes both. Five conjectures were reviewed
without this gate. It is worth asking what it would have said about them.

*The three fixes, in the order they mattered.*

1. **Empty-content detection** (`review.sh`). The worst of the three, because
   the old behaviour wrote a headless file and scored it
   `NO VERDICT LINE — treat as MAJOR`, **manufacturing objections no reviewer
   had made**. C-003 absorbed two.
2. **`reasoning_content` fallback** (`review.sh`), stamped in the output file so
   a reasoning trace is never passed off as a composed review. Not exercised in
   this run, since the failures were 504s rather than empty bodies.
3. **Gate model fallback** (`panel.sh`). The fix that closed it. One extra call,
   and it preserves the design intent: each gate reviewed once by *some*
   independent laboratory rather than by one particular one.

*Known cost, accepted.* A 504 takes roughly 15 minutes to surface, so three
retries plus a fallback is around 50 minutes for one failing gate, and this run
spent about that twice. Shortening the first attempt's timeout would find
failures faster and is the obvious next improvement, but it was deliberately
not changed mid-run.

*Residual.* `nebius/kimi-k3` reliably 504s on long reasoning prompts through
this router while answering short ones normally, and it also dropped out of the
C-009 panel vote, leaving four laboratories instead of five. It is a candidate
for removal from the panel pool rather than continued rescue.

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

## Independent review, 2026-11-16

An independent reviewer read the programme. Their main findings are recorded
here as **recorded, not resolved**: none has been acted on beyond the
housekeeping named below, and none is a decision.

- **(a) The HC-3 foothold at the ganglion is argued from one side.** The
  positive evidence is a rat result and a supporting model from one research
  lineage. Two models from an independent group report direct activation of
  Aβ fibres and no direct activation of C-fibres at clinical amplitude (one
  does not model T-junction silencing at all), and, in one population of model
  neurons, C-neuron activation only at several mA against typically ≤1 mA
  clinically. A rat study from the original lineage finds the T-junction filter
  already weakened after injury. Added to `evidence/03-writing-the-signal.md`
  §3 ("Two Michigan models disagree with the lineage above").
  The HC-3 row above still reads as "alive" and has not been revised.
- **(b) HC-2's killer is arguably met for allodynia, and the programme was
  narrowed rather than the hard core changed.** E-01 §6 says no peripheral
  decoder can succeed in principle for allodynia, because the traffic that hurts
  is indistinguishable from normal touch. The "reframing" section above narrows
  the programme instead of recording a hard-core change. **Whether that is the
  right bookkeeping is a decision for the owner. It is flagged here, not
  taken.**
- **(c) The work has gone to Branch B, which bears on none of the motivating
  phenotype's questions.** Those are: which generator (neuroma, ganglion or
  central) drives the pain; why the benefit of ganglion stimulation fades in
  some people; and whether touch-evoked allodynia and background pain separate.
  A costed magnetometry specification answers none of them.
- **(d) The Branch B specification is uncalibrated.** The C-004 forward model
  gives a peak field of 4.524 pT for a synchronous Aβ volley at 6.5 mm
  (`simulations/C-004-velocity-beamforming/results/results.md`, check 2),
  against about 1 pT measured in humans. The check is scored PASS only because
  its tolerance is an order-of-magnitude band of 0.10 to 10 pT. A factor of
  about 4.5 in amplitude is a factor of about 20 in energy, which is the
  quantity the C-008 trade-off surface is built on.

All four are population-level observations about the programme's design.

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
  **Guarded 2026-11-16:** `simulations/verdict.py` is now the only place either
  simulation turns a statistic into a verdict word, and it returns INCONCLUSIVE
  from fewer than 10 seeds or a CI that spans the threshold
  (`simulations/test_verdict.py`). A single-seed C-004 run now prints
  INCONCLUSIVE; the recorded 18-seed verdicts are re-derived from the committed
  JSON by the tests. Previously committed single-seed result files, which
  predate the guard, still carry their old verdict text and are not
  regenerated.
- No automated Lakatos degeneration check. E-06 §4 identifies the version-diff
  as the single most valuable mechanical check available, and it is not built.
- No content hash and timestamp at intake, so pre-registration currently rests
  on git history rather than on an explicit committed hash.
- No claim-level support check. Citations are resolved mechanically; whether a
  resolved paper *supports* the sentence it is attached to is left to gate 03,
  which is a model judgement rather than a mechanical one.
