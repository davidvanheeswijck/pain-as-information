# Pre-registered prediction for S-3: which observations separate the pain generator

**Written 2026-11-17, before any code for this simulation was run.** This file
is commit #1 of its branch and no results file exists in the history before
it. Intent: `intent/simulation/2026-11-16-act-on-fable-review.md` (S-3 is named
under Open questions; the owner's go is dated 17/11/2026). If the computation
disagrees with this file, the computation is probably right and this file is
the record of my being wrong.

**Not medical advice.** This is a population-level decision-analysis model. Its
output is a ranked list of questions a treating team might consider. It gives
no protocol, dose or device setting (ETHICS.md §3) and says nothing about any
individual (ETHICS.md §1).

What was done before this commit, and nothing else: nine PubMed abstracts were
read through E-utilities efetch (`retmode=text`), and the arithmetic below was
done by hand. No simulation code existed and nothing was computed by machine.

## The question

The setting is long-standing, CRPS-labelled, post-surgical neuropathic foot
pain, as a class of patients. The generator is taken to be one of four:

- **H1** a peripheral focal lesion (neuroma or neuroma-in-continuity);
- **H2** dorsal root ganglion ectopia;
- **H3** central amplification of input that is itself normal (input-dependent,
  no abnormal peripheral generator);
- **H4** central and input-independent.

- **Q1.** Which sequence of clinically available observations is expected to
  discriminate best between these, given realistic false-positive rates?
- **Q2.** How robust is that ranking to uncertainty in the likelihoods?
- **Q3.** Which pairs of hypotheses does no available observation separate?
  (The specificity column in `ledger/OPEN.md`: can the measurement tell the
  difference.)

## Operational definitions (fixed here so they cannot drift)

### Observations

Every observation is a discrete outcome. "Spontaneous pain" outcomes are
abolished (A), partial relief (P), none (N).

- **T1. Single diagnostic peripheral nerve block**, proximal to the suspected
  lesion and distal to the ganglion, with a confirmed complete sensory block.
  Outcome: spontaneous pain A / P / N. **Evoked pain is not recorded for T1 or
  T2**: numb skin cannot be tested (C-009).
- **T2. Comparative (controlled) block.** Outcome: concordant relief (A) /
  partial or discordant (P) / none (N).
- **T3. Dilute local anaesthetic at the ganglion**, at a concentration meant to
  silence ectopia without blocking conduction. Outcome: spontaneous pain
  A / P / N. This is a research procedure reported in one human series in
  another condition, not a routine test. See "Feasible sets".
- **T4. Ganglion stimulation on versus off**, in people who already carry such
  a device at the relevant level. Outcome, four cells: both spontaneous and
  evoked pain relieved / spontaneous only / evoked only / neither.
- **T5. High-resolution ultrasound or MR neurography** read for a focal
  neuroma. Outcome: positive / negative.

### Structural constraints

1. **C-009.** A complete sensory block removes ordinary touch along with any
   pathological traffic. **The T1 and T2 likelihood rows for H1 and H3 are
   therefore identical in every draw** (one shared row, not two similar ones).
   The same holds for T3, where the only route to relief under H1 or H3 is
   that the agent removes afferent input, which acts on both alike.
2. **T2 supersedes T1.** A comparative block contains a single block, and the
   two share the same responder. A sequence never contains both.
3. **No test is repeated in a sequence.**
4. **Conditional independence.** Given the hypothesis, the outcomes of
   different tests are independent. This is an assumption, and it favours
   sequences (a person who reports relief for non-specific reasons on one test
   is likelier to do so on the next). Declared as a limit.
5. **The four hypotheses are treated as exclusive and exhaustive.** C-009's
   panel said they are not ("A recurrent central network can be both
   pathologically altered and input-dependent"). Mixed generators are outside
   this model. Declared as a limit.

### Feasible sets

- **Set A (generous):** T1 to T5 under the constraints above. 5 single tests,
  9 unordered pairs, 7 unordered triples (18 and 42 ordered sequences).
- **Set B (routine):** set A without T3. Reported alongside. Any verdict on
  set B is secondary.

The kill is evaluated on set A, the set most favourable to localisation.

### Priors

Dirichlet(6, 5, 5, 4) over (H1, H2, H3, H4): mean (0.30, 0.25, 0.25, 0.20),
concentration 20. The H1 mean is the midpoint of the sourced 26% to 33% (see
the source check). The other three means and the concentration are **elicited**.
Secondary ensemble, no verdict: Dirichlet(1, 1, 1, 1).

### Likelihood parameters

Each parameter is drawn independently as lo + (hi - lo) x Beta(2, 2), so its
mean is the midpoint of its range. "Elicited" means the range is my judgement.
"Anchored" means a source gives a number or a direction that the range is
built around; the range itself is still elicited.

| Par. | Meaning | Range | Status |
|---|---|---|---|
| a | P(spontaneous pain abolished) when pain depends on input from the blocked territory and the block is complete | 0.60 to 0.95 | anchored: PMID 24704366, all 14 patients, none with CRPS |
| u | share of the not-abolished who report partial relief | 0.30 to 0.70 | elicited |
| f | P(relief reported with no specific effect), single uncontrolled block | 0.15 to 0.45 | anchored: PMID 29913995, "about 30%", zygapophysial joint blocks; transferred to peripheral nerve blocks by me |
| g | share of non-specific responders who report abolition | 0.20 to 0.60 | elicited |
| d | P(ganglion ectopia behaves as input-dependent under a distal block) | 0.00 to 0.50 | elicited |
| r | non-specific response of a comparative block, as a multiple of f | 0.20 to 0.60 | elicited (PMID 29913995 gives no number) |
| s | P(a true responder gives a discordant comparative result) | 0.00 to 0.25 | elicited |
| e | P(spontaneous pain abolished by T3) under H2 | 0.50 to 0.95 | anchored in direction: PMID 24769187 (phantom limb; no proportion in the abstract) |
| u3 | as u, for T3 | 0.30 to 0.70 | elicited |
| c | P(the T3 agent also removes afferent input), H1 and H3 alike | 0.00 to 0.30 | elicited |
| f3 | P(relief with no specific effect) for T3 | 0.05 to 0.35 | elicited (PMID 24769187: "Control injections were ineffective", no number) |
| g3 | as g, for T3 | 0.20 to 0.60 | elicited |
| s1, s2, s3, s4 | P(spontaneous pain relieved with stimulation on) under H1..H4 | 0.30-0.80, 0.40-0.85, 0.10-0.60, 0.05-0.35 | elicited; direction from PMID 33990112 and 32658148 (rat, one lineage) |
| v1, v2, v3, v4 | P(evoked pain relieved with stimulation on) under H1..H4 | 0.30-0.80, 0.40-0.85, 0.30-0.80, 0.05-0.50 | elicited; same |
| q1 | P(imaging positive) under H1 | 0.45 to 0.85 | anchored: PMID 21701028, sensitivity 67% for neuroma detection, ten studies |
| q2 | P(imaging positive) under H2 | 0.10 to 0.50 | elicited (an injured nerve can show a neuroma that is not the generator) |
| q3, q4 | P(imaging positive) under H3, H4 | 0.05 to 0.30 each | elicited (no specificity in the abstract) |

**No likelihood in this model is fully sourced.** Three ranges are anchored on
a number read from an abstract (a, f, q1), two on a direction (e, and the T4
ordering). Everything else is elicited.

### Rows

Let a "genuine" outcome be (pA, pP, pN). A non-specific response with
probability f, of which a share g is reported as abolition, turns it into

    A = pA + (pP + pN) f g
    P = pP (1 - f g) + pN f (1 - g)
    N = pN (1 - f)

- **T1.** Genuine row for H1 and for H3: (a, (1-a)u, (1-a)(1-u)). For H4:
  (0, 0, 1). For H2: (d a, d (1-a) u, remainder). Non-specific: (f, g).
- **T2.** Genuine row for H1 and for H3: (a(1-s), (1-a)u + a s, (1-a)(1-u)).
  H2: d times that row plus (1-d) times (0, 0, 1). H4: (0, 0, 1).
  Non-specific: (f r, g).
- **T3.** Genuine row for H2: (e, (1-e)u3, (1-e)(1-u3)). For H1 and for H3:
  (c a, c (1-a) u, remainder). H4: (0, 0, 1). Non-specific: (f3, g3).
- **T4.** Spontaneous and evoked relief independent given the hypothesis:
  both = s v, spontaneous only = s (1-v), evoked only = (1-s) v, neither =
  (1-s)(1-v).
- **T5.** Positive with probability q under each hypothesis.

### Quantities

- **Information gain (IG)** of a set of tests: the mutual information, in bits
  (log base 2), between the hypothesis and the joint outcome, computed exactly
  by enumeration. The maximum is the prior entropy, at most log2 4 = 2 bits.
- **Order.** Under conditional independence the IG of a fixed sequence does not
  depend on its order. Ordered sequences are enumerated and this is asserted
  in code. Ranking is over unordered sets. What order does change is the gain
  at the first step, which is reported.
- **Adaptive policy.** The best policy of depth 2 and of depth 3 in which the
  next test is chosen after seeing the previous outcomes (exact dynamic
  programming). Its value is at least that of the best fixed set.
- **Pairwise Bayes error** for hypotheses i and j under a set of tests: with
  the two priors renormalised to sum to one, the sum over joint outcomes of
  the smaller of the two joint probabilities. It is the error rate of the
  best possible reader told that the truth is one of the two. With no test it
  is the smaller renormalised prior (about 0.45 for H1 against H3).

## Pre-registered thresholds (verbatim)

- **P1 (no single test is enough):** no single test yields ≥1 bit in ≥80% of
  draws. Read as: the proportion of draws in which every single test is below
  1 bit is ≥0.80.
- **P2 (the ganglion test carries the pair):** the best 2-test set includes T3
  in ≥50% of draws.
- **P2b (mine, a block is needed):** the best 2-test set includes a block (T1
  or T2) in ≥70% of draws.
- **P3 (H1 against H3 stays poorly separated):** in ≥80% of draws, the
  pairwise Bayes error for H1 against H3 is ≥0.15 under **every** set of at
  most 3 tests in set A (that is, the minimum over those sets is ≥0.15). At
  0.15 the best possible reader still mislabels about one case in seven.
- **Kill:** if no feasible sequence of ≤3 tests yields ≥1 bit in the median
  draw, the conclusion is that the available clinical observations cannot
  localise the generator. That is a result, not a failure. Read as: the
  proportion of draws in which the best set-A sequence of ≤3 tests, **fixed or
  adaptive**, reaches ≥1 bit is below 0.50.
- **Positive control (must pass or NO verdict):** a synthetic oracle test
  (identity likelihood) returns 2 bits under a uniform prior, and the prior
  entropy under every drawn prior; a pure-noise test (identical rows) returns
  0; adding the noise test to any set changes nothing; adding the oracle to
  any set returns the prior entropy. Tolerance 1e-9 bits.
- **Ensemble rule:** 20 seeds of 200 draws each, 4,000 draws, seeds
  20261117 to 20261136 (secondary flat-prior ensemble: 20262117 to 20262136).
  For each claim the per-seed proportion is computed, and
  `simulations/verdict.py` `decide` is applied to the 20 per-seed values
  against the threshold (t-interval of the mean, at least 10 seeds). A pooled
  Wilson 95% interval over the 4,000 draws is reported beside it. **If the two
  disagree, or either interval spans the threshold, the verdict is
  INCONCLUSIVE.** Never a headline from a single seed.
- **Declared limits:** the likelihoods are largely elicited, so the
  sensitivity analysis is the product. The model says nothing about any
  individual.

### Verdict words

- P1, P2, P2b, P3: **SUPPORTED** if both intervals lie wholly at or above the
  threshold; **NOT SUPPORTED** if both lie wholly below; otherwise
  **INCONCLUSIVE**.
- Kill: **TRIGGERED** if both intervals lie wholly below 0.50; **NOT
  TRIGGERED** if both lie wholly above; otherwise **INCONCLUSIVE**.
- If the positive control fails: **NO VERDICT** for everything.

**What the intervals do and do not mean.** They measure Monte Carlo error over
draws from the ranges above. They do not measure whether the ranges are right.
A tight interval here is a statement about the model, not about the world.

### Unseparated pairs (Q3), fixed here

For each of the six pairs, the pairwise Bayes error under all of T2, T3, T4
and T5 together (the most any reader could have in set A), median over draws:

- **not separated** if the median is ≥0.15;
- **partly separated** from 0.05 to 0.15;
- **separated** below 0.05.

A pair is also reported as **structurally unseparated by a test** when its two
rows under that test are identical by construction.

### Reported without a threshold

Rank distribution, P(top) and the central 95% ensemble interval of IG for
every set; the first test of the best adaptive policy; set B; the flat-prior
ensemble; and the Spearman rank correlation between each drawn parameter and
the IG of the best triple, to show which elicited number moves the answer
most.

## Source check done while writing this (what the abstracts say)

All read via efetch on 2026-11-17. Where the brief I was given and the abstract
differ, the abstract wins.

- **PMID 29913995 (Curatolo & Bogduk 2010).** "Single blocks are associated
  with about 30% false-positive responses." The sentence before it is
  "Diagnostic blocks for cervical and lumbar zygapophysial joint pain have
  been extensively studied." For other blocks: "For all other types of blocks,
  very little research has been conducted." **The 30% is not a figure for
  peripheral nerve blocks.** I transfer it, with a range of 15% to 45%. On
  comparative blocks: "the validity of comparative blocks strongly decreases
  with decreasing prevalence of the condition." No number for them.
- **PMID 24704366 (Haroutounian et al. 2014).** "Fourteen patients with
  neuropathic pain (7 with unilateral foot pain due to peripheral nerve injury
  and 7 with bilateral pain in the feet due to distal polyneuropathy)". "The
  peripheral nerve block resulted in a complete abolition of ipsilateral pain
  within 10 min (median) in all patients". No CRPS patients, no control
  block. It supports input-dependence of spontaneous pain. It cannot place the
  generator (C-009).
- **PMID 24769187 (Vaso et al. 2014).** "In 31 amputees, the local anesthetic
  lidocaine was applied intrathecally and/or to the DRG surface
  (intraforaminal epidural block). This rapidly and reversibly extinguished
  PLP". "Control injections were ineffective." "The suppression of PLP and
  npPLS could also be demonstrated using dilute lidocaine concentrations that
  are sufficient to suppress DRG ectopia but not to block the propagation of
  impulses generated further distally in the nerve." Phantom limb pain, not
  CRPS. The abstract gives no proportion for the dilute arm.
- **PMID 31095098 (Yatziv & Devor 2019), rat.** "Observations in the spinal
  nerve ligation (SNL) model in rats suggest that cell bodies in the dorsal
  root ganglion (DRG) contribute 3 times more to the ectopic barrage than the
  site of nerve injury (neuroma)." That sentence is the paper's background,
  not its own result. Its result: "Lidocaine applied to the cut spinal nerve
  end or the L4 DRG did not affect allodynia". The endpoint is tactile
  allodynia, not spontaneous pain.
  **Lineage:** Vaso 2014 and Yatziv 2019 share their senior author. They are
  one lineage, not two independent supports for T3.
- **PMID 33990112 (Chao et al. 2021), rat.** "Ganglion field stimulation
  delivered at the L5 dorsal root ganglion blocked mechanical hyperalgesia
  behavior, mechanical allodynia, and ongoing spontaneous pain indicated by
  conditioned place preference, whereas GFS at L4 blocked evoked pain behavior
  but not spontaneous pain."
- **PMID 32658148 (Chao et al. 2020), rat.** "Activity generated peripherally
  by electrical stimulation of the sciatic nerve and punctate mechanical
  stimulation of the receptive field (glabrous skin) was likewise fully
  blocked by GFS within 20 seconds in C-type units". So traffic from a
  peripheral lesion passes the same junction as ganglion ectopia, which is why
  s1 and s2 overlap and T4 is not expected to separate H1 from H2.
  **Lineage:** Chao 2020 and Chao 2021 are one group (same first and last
  authors, same department). `evidence/03-writing-the-signal.md` §3 records two models
  from an independent group that dispute the mechanism at clinical amplitude.
- **PMID 21701028 (Chhabra et al. 2011).** "Ten MRN studies of nine patients".
  "The sensitivity of MRN was 91% for the presence of focal fibrosis affecting
  the three nerves and 67% for neuroma detection." **The 67% is a sensitivity,
  not an accuracy**, in ten studies after failed tarsal tunnel release. The
  abstract gives no specificity for neuroma.
- **PMID 40211731 (Raasveld et al. 2025).** "In 33% of patients labeled with
  CRPS type I, an inciting nerve injury was identified. Following
  retrospective assessment, 42% of patients were determined to have CRPS by
  all raters, 26% were determined not to have CRPS, and 32% showed
  inconsistent agreement." 53 patients at a peripheral nerve clinic, which
  selects for nerve injury. **An inciting nerve injury is not the same thing
  as a peripheral lesion that generates the pain today.** The 26% to 33% is
  an anchor for the H1 prior, not a measurement of it.
- **PMID 25339179 (Mailis-Gagnon et al. 2014).** "Only 27.7% were classified
  as CRPS by the clinical expert." "Of the 39 non-CRPS patients, 74% had other
  diagnosable entities (1/3 suffering from specific neuropathic pain
  conditions, e.g., radiculopathy, diabetic neuropathy, etc. and 2/3 from
  discreet musculoskeletal entities)". This supports diagnostic instability.
  It does not itself give a 26% to 33% figure. **Lineage:** no author is
  shared with Raasveld 2025, and the centres differ.

## Independent arithmetic, done by hand first

All at the midpoint of every range and the mean prior (0.30, 0.25, 0.25,
0.20). Entropies in bits, rounded.

**T1.** f g = 0.12. Row for H1 and H3: (0.802, 0.119, 0.079). H2: (0.291,
0.165, 0.545). H4: (0.12, 0.18, 0.70). Marginal (0.538, 0.143, 0.319), entropy
1.41. Conditional entropy 0.55 x 0.91 + 0.25 x 1.42 + 0.20 x 1.17 = 1.09.
**IG about 0.32 bits.**

**T2.** Non-specific 0.12, of which abolition 0.048. Row for H1 and H3:
(0.693, 0.207, 0.099). H2: (0.21, 0.106, 0.685). H4: (0.048, 0.072, 0.88).
Marginal entropy 1.47, conditional 1.07. **IG about 0.40 bits.**

**T3.** H2: (0.747, 0.143, 0.11). H1 and H3: (0.187, 0.12, 0.694). H4: (0.08,
0.12, 0.80). Marginal entropy 1.36, conditional 1.10. **IG about 0.26 bits.**

**T5.** P(positive) = 0.349, entropy 0.93, conditional 0.80. **IG about 0.13
bits.**

**T4.** From spontaneous relief alone 0.08 bits; the evoked cell adds a
little. **IG about 0.11 bits.**

**What that implies.**

1. A block can at best split {H1, H3} from {H2, H4}, which is worth at most
   about 1 bit even if it were noiseless, and T3 can at best split H2 from the
   rest, at most about 0.81 bits. No single test comes near 1 bit. **P1 should
   hold in essentially every draw.**
2. T2 and T3 cut the hypotheses along different lines, so their gains should
   roughly add: **best pair T2 + T3 at about 0.6 to 0.7 bits.** T2 + T5 is the
   rival, at about 0.5. T1 replaces T2 in draws where the comparative block
   loses more true responders than it removes false ones.
3. Adding T5 to that pair gives **about 0.75 to 0.85 bits for the best
   triple.** That is below 1 bit. **I expect the kill to trigger.**
4. Only T5, and weakly T4, tell H1 from H3. With T5 alone the pairwise Bayes
   error is 0.545 x 0.35 + 0.455 x 0.175 = 0.27; with T4 added, about 0.24.
   At the favourable corner (q1 = 0.85, q3 = 0.05) it is 0.105, so a minority
   of draws will fall below 0.15.

**Point predictions.** Median IG: T2 0.35 to 0.45, T1 0.27 to 0.37, T3 0.20 to
0.30, T5 0.10 to 0.17, T4 0.07 to 0.15 bits. Best pair, median: 0.55 to 0.70.
Best triple, median: 0.70 to 0.90. Best adaptive depth-3 policy: at most 0.05
bits above the best fixed triple. Minimum pairwise Bayes error for H1 against
H3 over sets of at most three tests, median: 0.20 to 0.27. Unseparated pairs
under all four tests: **H1 with H3 only**; H3 with H4 the next worst, at 0.09
to 0.14; **no pair below 0.05**.

**Probabilities (my own, for calibration later).** P1 supported: 97%. P2
supported: 80%. P2b supported: 85%. P3 supported: 75% (the 0.15 line is the
one I am least sure of). Kill triggered: 80%; not triggered: 12%;
inconclusive: 8%. Positive control fails on the first run: 3%.

## What would make me wrong in the interesting direction

If the gains are **more than additive**. Two tests that each split the four
hypotheses along a different line can, together, isolate a cell that neither
isolates alone, and my hand sum does not capture that. If the best triple
clears 1 bit in most draws, it will be through that route, and the kill does
not trigger. The other route is the prior: a draw that puts most of its mass on
two hypotheses that a block separates well makes a single test look strong.
The flat-prior ensemble is reported so that this can be seen.

## Declared limits

- **The likelihoods are largely elicited.** No row is fully sourced. The
  result is a statement about how the ranking behaves across my stated
  ranges, and the sensitivity analysis is the product.
- **It says nothing about any individual**, and it is not a protocol. Risk,
  burden, cost and availability of each observation are not modelled. T3 is a
  research procedure; T4 applies only where a device is already present.
- Exclusive and exhaustive hypotheses; conditional independence between
  tests; independent parameters; Beta(2, 2) on each range. Each of these
  makes the tests look better or the ensemble narrower than it should.
- Sources are small, mostly not in CRPS, and two of the mechanisms rest on rat
  work from a single lineage each.
- Information gain is not clinical value. A bit that separates two hypotheses
  with the same management is worth less than one that changes it.

---

## Amendments made in the code commit (commit #2)

Everything above this line is as committed in commit #1 and is not edited. This
section was appended with the code, **before the main run**. No threshold,
range, seed or verdict rule above is changed.

**A. A pilot was run before the code was committed, and I saw its output.**
Two smoke runs of the pipeline, 3 seeds of 20 draws (60 draws, the first three
main seeds), written to the gitignored `results/pilot/`. They are not results.
What they showed: control passed; every claim INCONCLUSIVE as it must be from
3 seeds; best pair T2+T3; best of at most three about 0.82 bits; the machine
midpoint within 0.01 bits of the hand arithmetic for every test. So the
direction of the main run was visible to me before it started. The only code
changes made after seeing pilot output are B and D below and two figure
layout fixes.

**B. A weakness in the P3 measure, found in the pilot. P3 is scored as
pre-registered; a diagnostic is added beside it.** The pairwise Bayes error
cannot exceed the smaller of the two renormalised priors, so a lopsided prior
draw gives a low error with no test at all. My hand figure of "about 0.45"
with no test holds at the mean prior only; across pilot draws the no-test
median was 0.375, and under the flat prior the no-test error was already below
0.15 in more than a third of draws. The measure therefore mixes what the tests
do with what the prior does. **Post hoc diagnostic, not a threshold:** the same
error with the pair's two priors set equal (0.5 with no test), reported for
every pair under all four tests and for H1 against H3 under the best set of at
most three. The pre-registered classes for Q3 also use the prior-weighted
measure and are reported as pre-registered, with the equal-prior column
beside them.

**C. Strict inequality.** `verdict.decide` names a side only when the interval
lies strictly above or below the threshold. The text above says "at or above".
The difference can only turn a verdict into INCONCLUSIVE.

**D. "Structurally unseparated by a test"** is decided from the rows
themselves (largest row difference exactly zero in every draw), not from the
error equalling the no-test error, which can also happen when a weak test
never changes the best guess.

**E. Order check.** The assertion that order does not change a fixed
sequence is evaluated on the first five draws of each seed (every permutation
of every set), not on all draws.

**F. Mutation check.** `mutation_check.py` breaks the log base and the
normalisation of `mutual_information` in a temporary copy and requires
`test_infogain.py` to fail by assertion.

## Amendment made after the main run

**G. Reporting only.** After reading the main-run output I added one generated
sentence to `results.md` (the share of draws in which T2 is above T1, and that
this ordering comes from elicited ranges) and stopped a rounding artefact
printing as "-0.000". The model, ranges, seeds and verdict rules are
untouched. The main run was repeated from the new code; its numbers are
identical to the first main run, which is kept in git history (the results
commit before this one).

## Amendments made after review of the pull request (2026-11-17)

Text above is not edited. Two statements above are wrong as written and are
corrected here. No number, range, seed, threshold or verdict changes.

**H. PMID 24704366 and CRPS.** The parameter table and the source check above
say "none with CRPS" and "No CRPS patients". **The abstract does not say
that.** It lists "7 with unilateral foot pain due to peripheral nerve injury
and 7 with bilateral pain in the feet due to distal polyneuropathy" and does
not mention CRPS either way. The correct statement is: the abstract does not
mention CRPS. The note on parameter `a` in the code and in the generated
results table now reads that way.

**I. The H1 prior is elicited, not sourced.** Above, the H1 prior mean is
called "the midpoint of the sourced 26% to 33%" and "an anchor". In PMID
40211731 those are two different quantities: 26% of patients "were determined
not to have CRPS", and "In 33% of patients labeled with CRPS type I, an
inciting nerve injury was identified". They are not two estimates of one
thing, they have different denominators, and neither is the share of patients
whose pain is generated by a peripheral lesion. A midpoint of the two has no
meaning. **The whole prior, H1 included, is elicited; the paper is context for
choosing a value near 0.30, not a source for it.** The count is therefore:
24 likelihood parameters, of which 4 are anchored on an abstract (a, f, q1 on
a number; e on a direction) and 20 elicited; all four prior means and the
concentration elicited. The sensitivity table in `results.md` now labels
"prior H1" as elicited.

**J. Tests added in review.** A hand-computed mid-range pairwise Bayes error;
a hand-computed case in which the adaptive policy strictly beats every fixed
pair (2 bits against 1.5); and the disagreement path of the verdict rule in
both directions (`test_simulate_s003.py`, needs numpy). `mutation_check.py`
now also removes the agreement requirement and requires those tests to fail.
While adding it I found that the check could reuse a stale bytecode file for
a second mutant of the same length written in the same second; it now runs
without a bytecode cache.

**K. Wording in `results.md`.** Next to the verdicts it now says that P3
depends on the prior, that the kill is a statement about the pre-registered
1-bit threshold and not about clinical usefulness, and, in the P2 row, that T3
is a research procedure.
