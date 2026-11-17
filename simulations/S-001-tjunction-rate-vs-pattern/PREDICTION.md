# Pre-registered prediction for S-1: T-junction filtering, rate versus pattern

**Written 2026-11-16, before any simulation run that bears on P1, P2 or the
positive control.** This file is commit #1 of its branch and no results file
exists in the history before it. Intent:
`intent/simulation/2026-11-16-act-on-fable-review.md` (Proposed outcome item 2;
it lands via PR #1 and may not be on this branch's base). If the simulation
disagrees with this file, the simulation is probably right and this file is the
record of my being wrong.

What was done before this commit, and nothing else: the Sundt, Gamper & Jaffe
2015 ModelDB code (187473) was downloaded, every file read, five mechanisms
copied into `mod/` and compiled (it compiles; nothing was run). No NEURON
simulation of any kind had been executed.

## The questions

- **Q1.** Does stimulation *pattern* change T-junction filtering beyond mean
  rate? (Specificity: pattern versus dose. C-001 is refuted; this is the acute
  biophysical version of its "vary the pattern at constant charge" idea.)
- **Q2.** Can a T-junction low-pass account retrodict the blinded human
  frequency ordering of Piedade et al. 2022 (PMID 35217898; n=19; 20 Hz best,
  VAS 3.7 at 20 Hz rising to 5.8 at 80 Hz) and 2023 (PMID 36705762; n=17; 4 Hz,
  20 Hz and 60 Hz all better than sham, not separable from each other)?
  (Specificity: mechanism versus the human ordering.) Data:
  `evidence/05-crps.md`, the DRG frequency-trial table.

## Operational definitions (fixed here so they cannot drift)

- **Model.** Pseudounipolar C-neuron after Sundt 2015: soma, stem, T-junction,
  peripheral and central axons; Na (nahh, shifted -6/+6 mV), Kdr, KCNQ/M (im),
  and, for the third configuration, L-type Ca (cal) plus SK. Aβ comparator: a
  myelinated pseudounipolar neuron of generic node-and-internode construction,
  built for this study rather than taken from ModelDB 51022.
- **Stimulus.** Rectangular 1 ms current pulses injected at the soma for 30 s.
  **Threshold** is per model: the smallest single 1 ms pulse from rest that
  produces a soma spike propagating to the mid-stem (bisection to 1%). Runs at
  1.0x and 1.5x that threshold.
- **Test spikes.** Single suprathreshold peripheral pulses launched at the
  distal peripheral end during the whole stimulation. Primary test train
  10 Hz (300 spikes per run). A 5 Hz test train is run for the regular 20 Hz
  and 80 Hz conditions at 1.5x only (secondary; two extra runs per model).
  Test trains add their own load to the soma if they invade it; this is the
  same in every condition and is a declared limit.
- **F (filtering index).** Over test spikes that are recorded at the
  pre-junction peripheral site (0.95 of the peripheral section), the fraction
  that do **not** produce a spike at the mid central axon within 15 ms of
  expected conduction delay. **Head-on collisions are excluded from the
  denominator**: a test spike is excluded if a stimulus-evoked spike crosses
  that same pre-junction site within +/-2 ms of it. (Otherwise F would rise
  with rate through collisions alone, which is not low-pass filtering and
  would bias P2.) F_all, without the exclusion, is reported as a sensitivity.
- **Aβ F** is the same quantity in the myelinated comparator.
- **Time-to-block.** The onset time of the first run of 5 consecutive failed
  test spikes; undefined (reported as "none") if there is no such run.
- **Following frequency** (positive control and ensemble acceptance): the
  highest frequency at which all 21 pulses of a train launched at the
  peripheral end reach the central axon, as Sundt 2015 and Gemes 2013 measure
  it (their trains are 21 and 20 spikes respectively). Found by bisection to
  2%, assuming monotonicity, with no DRG stimulation.
- **Patterns, all 600 pulses over 30 s (20 Hz mean).**
  *Regular:* 4, 20, 40, 60, 80 Hz (these have 120 to 2400 pulses; only the
  20 Hz one is pulse-matched to the patterns).
  *Poisson:* 2 ms dead time plus exponential intervals, rescaled so exactly
  600 pulses span 30 s.
  *Burst:* 5 pulses at 100 Hz repeated every 250 ms.
  *Jitter:* instantaneous rates r_i uniform over 2 to 50 Hz, interval 1/r_i,
  all intervals scaled by one factor so exactly 600 pulses span 30 s (so the
  realised range is slightly narrower than 2 to 50 Hz and this is a
  consequence of matching the mean to 20 Hz).

## Pre-registered thresholds (verbatim)

- **P1 (pattern ≈ rate):** every matched-rate pattern (Poisson, burst = 5
  pulses at 100 Hz every 250 ms, uniform jitter over 2-50 Hz; all at 20 Hz
  mean and matched pulse count) gives filtering index F within 10 percentage
  points of regular 20 Hz in ≥80% of models. **Refuted** if any matched-rate
  pattern raises population-mean F by ≥20 points with the 95% CI excluding 10.
- **P2 (no human ordering):** F(80 Hz) ≥ F(20 Hz) in ≥90% of models.
  **Refuted** if F falls by ≥20% relative from 20 to 80 Hz in most models
  (then the T-junction account is consistent with the blinded human ordering).
- **Positive control (must pass or NO verdict):** reproduce Sundt 2015's
  following frequencies, within +/-25%, ~110 Hz (Na+Kdr only), ~30 Hz (with
  KCNQ/M), ~6 Hz (with Ca-dependent K), and Chao 2020's qualitative result:
  progressive C-type block within ~20 s at 20 Hz while an Aβ comparator's F
  < 5%.
- **Ensemble rule:** population of ≥200 C-neuron variants (vary stem-axon
  diameter, Na density, KCNQ, SK/Ca-K, Ca decay), accepted only if their
  unstimulated following frequency lies in the experimental C-type range.
  Stochastic patterns: ≥20 seeds on a subsample of ≥30 models. dt-halving
  convergence check. Report INCONCLUSIVE whenever a CI spans its threshold;
  never a headline from a single run.
- **Declared limits:** says nothing about chronic decay of filtering over
  weeks, nor whether clinical amplitudes reach C-neurons at all
  (Graham/Lempka 2019, 2022, PMIDs 30981900, 36387415 argue they do not);
  charge was not matched across frequencies in the human trials (n=19, n=17).

### Source check done while writing this (what the sources say)

- **Sundt 2015 abstract (PMID 26334005, read via efetch):** "A model
  containing only fast voltage-gated Na+ and delayed-rectifier K+ channels
  conducted trains of spikes up to frequencies of 110 Hz. The addition of ...
  KCNQ ... reduced the following frequency to 30 Hz. ... a Ca2+-dependent K+
  current, was needed to reduce the following frequency to 6 Hz." The numbers
  in the spec are the paper's own; no change. Acceptance bands are therefore
  82.5 to 137.5 Hz, 22.5 to 37.5 Hz and 4.5 to 7.5 Hz.
- **Gemes 2013 abstract (PMID 23148321, read via efetch) gives no numeric
  following-frequency range.** It gives only the ordering (lowest in C-type,
  then inflected A-type, then non-inflected A-type) and that following is
  slower for 20 spikes than for 2. **The range I use is 2 to 40 Hz,** chosen
  to bracket Sundt's mechanistic 6 to 30 Hz with margin on both sides, and
  chosen *before* seeing the model's population, so it does not pre-select the
  answer. A tighter sensitivity cut (2 to 15 Hz) is reported alongside it.
  Gemes's own table has the real numbers and was not consulted; this is a
  weakness and is named.

### Verdict rules (also fixed here)

`simulations/verdict.py` does not exist on this branch's base. A local rule
with the same intent is used and noted in the PR: bootstrap 95% CI (10000
resamples across models, percentile) for means; Wilson 95% interval for
proportions.

- **P1 SUPPORTED** only if, for all six cells (3 patterns x 2 amplitudes), the
  proportion of models with |F_pattern - F_reg20| <= 10 points is ≥0.80 **and**
  the Wilson interval's lower bound is ≥0.80. **REFUTED** if any cell has
  population-mean difference ≥ +20 points and the bootstrap CI lower bound >
  +10 points. **INCONCLUSIVE** if, in any cell, the Wilson interval spans 0.80
  or a mean difference ≥ +20 has a CI lower bound ≤ +10 (and nothing is
  refuted). Otherwise **NOT SUPPORTED, NOT REFUTED** (the prediction fails but
  the refutation bar is not met).
- **P2 SUPPORTED** if the proportion of models with F80 ≥ F20 - 0.01 (a
  one-point tolerance for numerical noise; the literal count is also reported)
  is ≥0.90 with Wilson lower bound ≥0.90, at both amplitudes. **REFUTED** if,
  among models with F20 ≥ 0.05, more than half show (F20 - F80)/F20 ≥ 0.20 and
  the Wilson lower bound of that proportion exceeds 0.50. **INCONCLUSIVE** if
  either interval spans its threshold.
- **Positive control PASS** requires all three Sundt following frequencies
  inside their bands on the canonical parameter set and, at 20 Hz 1.5x on the
  accepted population, (a) time-to-block defined and ≤ 20 s in ≥50% of
  models, (b) F in the last 10 s exceeding F in the first 5 s by ≥ 20 points
  in the population median, and (c) the Aβ population mean F < 5% with the
  bootstrap CI upper bound < 5%. Otherwise **NO VERDICT** for P1 and P2.
- **Convergence:** on 10 models, regular 20 Hz, 80 Hz and burst at 1.5x, 10 s
  windows, dt = 0.025 against 0.0125 ms. Pass if the median |dF| ≤ 0.02 and
  no pattern-versus-rate classification flips; otherwise INCONCLUSIVE.
- Positive-control mutation (remove the SK/Ca-K conductance) must push the
  third configuration out of its 4.5-7.5 Hz band; I will run it and report it.

### What I am allowed to tune, and what I am not

To pass the positive control the model's free parameters are SK location
(soma only versus soma plus stem), gsk, Ca-channel density and Ca decay time
constant, and axon segmentation. They are tuned **against the three Sundt
following frequencies only**. No parameter is adjusted after looking at any
P1 or P2 quantity, and the tuning history is logged in the results.

## Independent arithmetic, done by hand first

**Time scales.** M-current time constant at -60 mV: tau = 1000 / (3.3 *
(exp(-1.25) + exp(1.25))) / 3^((35-23.5)/10) = 1000 / (3.3 * 3.78) / 3.54 =
**about 23 ms**. A following frequency of about 30 Hz is a 33 ms period, the
same order, so M is a short-memory process that sums over a few spikes. The
Ca-dependent K conductance has Ca decay 500 ms in Sundt's Fig. 8c; a 6 Hz
following frequency is a 167 ms period, **a third of that time constant**, so
SK integrates over about 3 spikes at 6 Hz and over about **40 spikes at
80 Hz**.

**Ca per spike.** Ca entry per spike is B * cascale * integral(ica dt) =
0.26 * 0.1 * (about 2.5e-3 mA/cm2 over about 1 ms) = about **65 nM** against a
resting 70 nM. In steady state Ca is raised by 65 nM * rate * tau = **130 nM at
4 Hz, 650 nM at 20 Hz, 2.6 uM at 80 Hz**, i.e. about 2x, 10x and 40x resting.
Because SK gating goes as the cube of Ca, SK activation is roughly dose
dependent and saturating in this range.

**What that implies.**

1. The slow variable that causes the filtering sees **pulse count and mean
   rate**, not pattern, so long as the interval structure is short against the
   500 ms integration. By that reasoning P1 should hold for Poisson and jitter.
2. **Burst is the likeliest violation of P1.** A 5-pulse 100 Hz burst
   (10 ms intervals) is far above any 6 to 30 Hz following frequency, so
   within-burst spikes are likelier to fail locally, and M (tau about 23 ms)
   decays by e^-2.2 = 0.11 between 50 ms regular pulses but barely at all
   within a burst, so a burst gives more M activation per pulse than regular
   firing. I expect burst to **raise F in M-limited models** by a few to
   ~15 points, and to be about neutral in SK-dominated models.
3. Rate dose is monotone, so F should **rise** from 4 to 80 Hz, probably
   saturating near 1 at 40 to 80 Hz in SK-bearing models. That makes
   F(80) >= F(20) near-trivially, and P2 should **hold**: the model does not
   produce "20 Hz better than 80 Hz".
4. F at 4 Hz, below the 6 Hz following frequency, should be small (well under
   0.1), which would also fail to explain "4 Hz better than sham" in the 2023
   trial. That is not a pre-registered threshold but I record the expectation.

**Point predictions.** F(20 Hz, 1.5x), median across accepted models:
**0.5 to 0.9**, wide because it depends on how many accepted variants carry
SK. Aβ F: below 0.01. Burst minus regular-20 mean difference: **+5 to +15
points** (not meeting the +20 refutation bar). Poisson and jitter: within
**+/-5 points**.

**Probabilities (my own, for calibration later).** P2 not refuted: 90%. P1
refuted: 15%. P1 supported as stated: 45%. P1 "not supported, not refuted"
or inconclusive: the remaining 40%, mostly through the burst cell. The
positive control failing on the first parameterisation: 50%; the ~6 Hz
configuration is the one I expect to need tuning, because Sundt's own Fig. 8c
gives gsk and tau but not a full recipe for the soma-plus-stem geometry.

## What would make me wrong in the interesting direction

If F is **non-monotone in rate**: if at 80 Hz the soma stops following (Na
inactivation at the half-density soma, K and SK hyperpolarisation) so that
fewer spikes enter the stem and less Ca enters, then F(80) could fall below
F(20) through *loss of stimulus drive* rather than through any filtering
property. That would hit the P2 refutation bar for a reason that is not a
T-junction effect, and it is why F is reported alongside the number of
stimulus pulses that evoked a soma spike. I have not modelled that by hand
and it is the place where the simulation could most plausibly surprise me.

## Declared limits

As in the thresholds above: acute only (nothing about decay of filtering over
weeks); an intracellular soma current, which says nothing about whether
clinical extracellular amplitudes ever reach C-neuron somata; charge was not
matched across frequencies in the human trials; a morphologically simplified
neuron with a single set of ion channels; no dorsal-horn model. **These
results are not stimulation settings.**

---

## Amendments made in the results commit (commit #2)

Everything above is as committed in commit #1 and is not edited. What follows
was decided while building the model, **before any P1, P2 or ensemble result
existed**, but after the pre-registration; each item says what changed and why,
so a reader can judge whether it moves the goalposts. The thresholds, the
patterns, the verdict rules and the positive-control criteria are unchanged.

**A. Tuning freedoms.** The pre-registered list of tunables was too short. To
pass the Sundt 30 Hz and 6 Hz controls, free parameters were: Na density
(0.0385 S/cm2 against Sundt's 0.04), KCNQ density (0.0015 against Fig. 5d's
0.0004), stem length (75 um, Fig. 5d), SK conductance (0.02 against Fig. 8c's
0.001), Ca decay (1500 ms against Fig. 8c's 500 ms) and segmentation (50 um
axons, 10 um junction and stem). All were chosen against the three Sundt
following frequencies only. The Sundt 2015 values did not reproduce the paper's
own following frequencies with the ModelDB mechanisms in this rebuild (KCNQ
alone only reached 38 to 50 Hz at the paper's densities); that is itself a
finding about reproducibility, not about the T-junction.

**B. Following frequency is scanned, not bisected.** In these models following
is not monotone in frequency (a 150 Hz value was seen for a neuron that failed
at 118 Hz). The following frequency is the first failing grid frequency on a
12% geometric grid, refined once to about 6%.

**C. Stimulation site and amplitude.** (i) The stimulus is a 1 ms current pulse
at the mid-stem, not the soma: with SK present the soma stopped generating
spikes after a few pulses (8 to 10 of 100 at 20 Hz), so the "stimulation" was
mostly doing nothing. (ii) "Threshold" is a **steady-state drive threshold**:
the smallest multiple (up to 12x) of the from-rest threshold at which at least
90% of the pulses in the second half of a 4 s regular 20 Hz train evoke a stem
spike. 1.0x and 1.5x are multiples of that. Variants that cannot be driven are
dropped and counted (they are a declared selection effect). (iii) The number of
pulses that evoked a spike (`n_evoked`) is reported for every run, as the
pre-registration promised.

**D. Test (probe) spikes.** The pre-registered primary was a 10 Hz test train.
In the SK-bearing configuration that is **above the 6 Hz following frequency, so
the probe train blocks itself with no stimulation at all** (F is about 1 with
no stimulus in the models where following frequency is below 10 Hz). The
**primary probe is therefore a 2 Hz train** (mean rate, each spike jittered
+/-30% of its slot so that all phases of the stimulus train are sampled; the
same probe times in every condition of a model). The pre-registered 10 Hz
primary and the 5 Hz train are run and reported on the 30-model subsample only
(1.5x; regular 20 Hz, regular 80 Hz, burst, and 5 seeds each of Poisson and
jitter). Both sets of numbers are shown in `results.md`.

**E. F definition.** The central recording site is 60 um into the central axon
(closer to the junction than "mid central axon", so that latencies are short).
The ambiguity exclusion replaces the +/-2 ms collision rule: a probe spike is
excluded if a stimulus-evoked spike crosses the mid-stem site in a window that
could produce a central crossing inside the success window (the stimulus spike
would otherwise be mistaken for the probe at the central site). Probes that do
not reach the pre-junction site (annihilated by a stimulus spike en route) are
also excluded. Spikes the probe itself sends into the stem within about one
conduction step are not counted as ambiguity. `F_all` (no exclusion) is a lower
bound on F and is stored per run.

**F. Aβ comparator.** Rest at -65 mV, because the unshifted Traub-Miles sodium
kinetics are unstable at -60 mV (a spike fired at 1 pA); everything else as
built in `tjmodel.py`. Its conduction velocity is about 3.7 m/s against about
0.3 m/s for the C model: it is a comparator for "myelinated passes", not a
calibrated Aβ fibre.

**G. Diagnostics added, not thresholds.** A post hoc "drive-matched" 80 Hz
run (1.5x of its own steady-state drive threshold) is reported on the subsample
because the pre-registration itself named loss of stimulus drive as the likeliest
route to a spurious P2 refutation.

### Prior art found after pre-registration

**Ladez SR, Liu J, Chen L, Feng B. "Computational Modeling of Dorsal Root
Ganglion Stimulation: Understanding Pain Suppression Mechanisms." 2024 46th
Annual International Conference of the IEEE EMBC, 2024, 4 pages, doi
10.1109/EMBC53108.2024.10782923 (IEEE Xplore document 10782923;
University of Connecticut).** Title, authors, venue and year verified through
Crossref. **Update (results commit):** PMID 40039770; the abstract was then read
via PubMed. It is a NEURON model of Aδ- and C-fibre transmission under DRG
stimulation with Markov-type sodium channel models (including NaV1.6), and
reports that stimulation raises intra-axonal Na+ and lowers K+, disrupting
transaxonal ionic gradients, causing activity-dependent conduction slowing and
eventual conduction block in both fibre types. That is a **rival mechanism**
to the Ca-dependent-K T-junction filter modelled here. What S-1 asks is
different: whether stimulation **pattern at matched mean rate** changes
T-junction filtering (the acute version of the refuted C-001 idea), and whether
a T-junction account can **retrodict the blinded human frequency ordering** of
Piedade 2022 and 2023, with thresholds fixed in advance and a positive control
that can disqualify the result. It does
not supersede or reproduce that work. Kent et al. 2018 (PMID 29377442), already
cited above, remains the closest earlier DRG-stimulation computational model.
