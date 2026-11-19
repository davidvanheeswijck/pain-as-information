# Pre-registered prediction for S-2b: corrected dorsal-horn run

**Written 2026-11-18, before any verdict-bearing simulation.** This file is commit #1 of its
branch and alone in that commit. Intent: `intent/simulation/2026-11-17-s2-dorsal-horn.md`
(decision log row of 18/11/2026). This is a **fresh registration**, not a continuation of S-2
(`simulations/S-002-dorsal-horn/PREDICTION.md`, which stays as it is, with its Amendments 1 and 2).
If the simulation disagrees with this file, the simulation is probably right and this file is the
record of my being wrong.

## What was done before this commit (all of it, disclosed)

1. Read S-2: its `PREDICTION.md` with Amendments 1 and 2, the port (`dh_model.py`), the protocol,
   the driver, `results/main/results.md`, `PROVENANCE.md`, `data/`, and the S-2 entry of
   `ledger/OPEN.md`.
2. Created `simulations/.venv` (python3.13, `neuron==9.0.2`) and compiled the S-2 mechanisms in
   `S-002-dorsal-horn/mod/` with `nrnivmodl` (the output is gitignored).
3. Fetched the ModelDB 168414 mirror archive into a new empty directory outside the repository.
   Its sha256 equals the one in S-2's `PROVENANCE.md`
   (`ae2967d4...fa36cc`). I **read** `CellTemplates.hoc`, `MakeNetwork.hoc` and `RunSim_EP.hoc` of
   the `A Fiber Inhibition` folder and scanned them for `system(`, `popen` and `unix` (no match).
   **No shipped hoc file was executed.** The oracle (below) has not been run.
4. Read the shipped `Foreman SCS`, `A Fiber Inhibition` and `WindUp` input files as data
   (spike counts per fibre class and event times; no simulation). What they show is in "The
   shipped inputs" below.
5. One smoke run of 200 ms of the unmodified network with no input (it fired no WDR spike; it checked
   that the new protocol module imports and the port runs).
6. **The one unmodified-model response curve** the brief allows (`prereg_response_curve.py`, a
   pilot: its raw output is under the gitignored `results/pilot/`, a copy is committed in
   `results/prereg/`). It measures a single quantity: the WDR rate of the **unmodified shipped
   network, E_anion shift 0, C input only** (no touch, no stimulation), against the Poisson rate per C
   fibre, on this study's run protocol (5.5 s, scored on [1.5, 5.5) s, `dt` 0.025 ms, seeds 1 and 2,
   the C trains that candidate 0 will use). It was run once, 17 values, 8 workers, 2026-11-18
   15:00:16 to 15:01:13. It bears on no verdict: it places the C-drive grid. Result (mean of 2 seeds,
   WDR Hz): 0.5 Hz per fibre 0.12; 0.625 0.38; 0.75 0.75; 0.875 0.88; **1.0 2.12**; 1.125 3.50; 1.25 7.50;
   **1.375 13.50**; 1.5 22.88; 1.625 30.75; 1.75 38.50; 1.875 42.38; 2.0 50.50; 2.125 56.75;
   2.25 64.38; 2.375 66.62; 2.5 73.00. The steep range is about 0.9 to 1.5 Hz per fibre; the band
   [2, 15] Hz of the drive match is reached at 1.0 to 1.375 Hz per fibre in this model. The curve
   also fixes candidate 0's drive match (below), so I know it.

**Facts from the S-2 record that I carry in and that shape this design** (disclosed so that no
prediction below passes as blind): (a) candidate 0 touch-only, 10 Hz per Aβ fibre, S-2 diagnostics:
WDR 3.2 / 28.7 / 103.5 / 143.2 / 167.2 Hz at shifts 0 / 10 / 20 / 30 / 40 mV, one seed, so touch
begins to drive the projection neuron between 0 and 10 mV in the unmodified model (Amendment 1); (b)
the wind-up feature passed for candidate 0 at both `dt` in S-2 (Amendment 1); (c) a reviewer's
original-hoc table, which I have **not** reproduced: spikes per cycle C only 11.3, all A fibres 19.4,
C plus Aβ only 8.0, C plus Aδ only 23.3 (Amendment 2). This study's oracle exists to reproduce those four
numbers in the repository; until it has, they are the reviewer's, not mine.

## What S-2 got wrong, and how each fix answers it

S-2's result was NO VERDICT because its own positive control failed at candidate 0
(`results/main/results.md`). The causes, as recorded in Amendments 1 and 2:

| S-2 defect | Where recorded | S-2b answer |
|---|---|---|
| The A-fibre control counted Aβ and Aδ together. In the shipped table Aδ excites the WDR directly (rows 60-89) and has weight 0 onto the inhibitory interneuron SG75; Aβ is the inhibiting class. The feature could not isolate Aβ inhibition. | Amendment 2, point 1 | The A control registers **C only, C plus Aβ only, C plus Aδ only, C plus all A** separately. **The calibration criterion is on C plus Aβ only.** Aδ-only is registered and not part of any criterion. |
| The stimulation driver pulsed Aβ fibres 0-14 (direct WDR excitation). The shipped Foreman SCS file puts its pulses on fibres 30-44, the surround input to SG76, whose GABA-A outputs go to WDR and EX (rows 288-290). | Amendment 2, point 3 | Pulses go to **fibres 30-44**. The Aβ background of the shipped file is part of the driver and is declared (below). The frequency effect is tested on this driver. |
| The C drive set {2.5, 5, 10, 20} Hz per fibre could not reach the model's [2, 15] Hz band (78 Hz at 2.5). | Amendment 1 | A grid of 0.5 to 2.5 Hz per fibre in steps of 0.125, bracketing the steep range of the pre-registration curve above. |
| The faithfulness of the port was asserted from a reviewer's scratch run that the repository did not hold; my own attempt was blocked and not retried. | Amendment 2, point 1 | `crosscheck_original_hoc.py` builds the original hoc network (only `CellTemplates.hoc`, `MakeNetwork.hoc`, `RunSim_EP.hoc`; GUI line stripped in a copy; no `mosinit.hoc`, `Shell.hoc` or save procedure), refuses to run if a file contains `system(`, `popen` or `unix`, and commits its numbers as JSON. A test compares the port to it. |
| P0's interval [10, 25] mV and the "touch level" (own per-network level from {10, 20, 40, 80} Hz, onset rise 1 Hz) did not match what candidate 0 does: onset below 10 mV, and a touch level that already drives 3 Hz at shift 0. | Amendment 1 | Touch is **fixed at the shipped Aβ background rate, 9 Hz per Aβ fibre**, for every network; a finer shift grid; P0 is re-posed (below) with the diagnostic disclosed. |
| One control feature (F) gated the whole ensemble, so a failure of my own driver ended the study. | Amendment 1 | **Calibration is separated from validation** (below): the ensemble is accepted on W, A-beta and the drive match; F, the published stimulation-frequency window, is **held out** and gates only the stimulation questions. |
| A-fibre inhibition ran the whole shipped 221 s file; only the first 10 cycles are scored. | code review | Runs stop at 21 s (the scored cycles end at 21 s); the oracle checks that this does not change the counts. |
| The wind-up control ran with `Foreman SCS` weights, where rows 288-290 are non-zero (the original `WindUp` folder has 0). | Amendment 2, point 4 | Unchanged and declared: the surround fibres are silent in the wind-up input, so the rows carry no event. |

## The questions

From the intent file; the phenotype is a population-level one (post-surgical CRPS-labelled foot pain
with a ganglion stimulator: touch-evoked allodynia plus a separate background pain). Nothing about any
individual.

- **Q1.** As the anion reversal potential E_anion of the WDR neuron shifts upward, at what shift does
  touch-type (Aβ) input start to drive the projection (pain-output) neuron?
- **Q2.** Once inhibition has collapsed, do two manipulations still reduce touch-evoked output,
  separately from C-driven output? (a) Stimulation on the inhibitory surround input at a frequency in
  the published inhibitory window; (b) reduced C input (the T-junction reading).
- **Q3.** Which observable change over time would distinguish progressive disinhibition from
  habituation and from lead drift? A **candidate observation for a treating team to consider, never
  advice**.

## Prior art and the starting model

The S-2 registration's prior-art search (PubMed and ModelDB, queries verbatim in its Appendix A, run
2026-11-17) stands. **No new search was run for S-2b.** The starting model is unchanged:

- **Zhang, Janik & Grill 2014** (J Neurophysiol 112:552-567, PMID 24790169), ModelDB 168414, NEURON.
  Abstract, verbatim: "Spinal cord stimulation (SCS) is a clinical therapy for chronic, neuropathic
  pain, but an incomplete understanding of the mechanisms underlying SCS contributes to the lack of
  improvement in SCS efficacy over time. To study the mechanisms underlying SCS, we constructed a
  biophysically based network model of the dorsal horn circuit consisting of interconnected dorsal horn
  interneurons and a wide-dynamic range (WDR) projection neuron and representations of both local and
  surround receptive field inhibition. We validated the network model by reproducing cellular and
  network responses relevant to pain processing including wind-up, A fiber-mediated inhibition, and
  surround receptive field inhibition. We then simulated the effects of SCS on the activity of the WDR
  projection neuron and found that the response of the model WDR neuron to SCS depends on the SCS
  frequency; SCS frequencies of 30-100 Hz maximally inhibited the model WDR neuron, while frequencies
  under 30 Hz and over 100 Hz excited the model WDR neuron. We also studied the impacts on the effects
  of SCS of loss of inhibition due to the loss of either GABA or KCC2 function. Reducing the influence
  of local and surround GABAergic interneurons by weakening their inputs or their connections to the WDR
  neuron and shifting the anionic reversal potential of the WDR neurons upward each reduced the range of
  optimal SCS frequencies and changed the frequency at which SCS had a maximal effect. The results of
  this study provide insights into the mechanisms of SCS and pave the way for improved SCS parameter
  selection."
  **What kind of numbers these are:** "30-100 Hz", "under 30 Hz" and "over 100 Hz" are the published
  **frequency effect for the model WDR neuron under SCS** (a model result, not a clinical one). The
  abstract gives **no size for the E_anion shift** and no wind-up magnitude; every threshold below that
  looks like a number from the paper is **my operationalisation, chosen before the run**.
- The other models considered in S-2 (Medlock 2022, PMID 35232767; Gilbert 2023, PMID 37727912) are
  unchanged in status: partial overlaps, none a full answer, on abstracts only.
- The evidence base this serves: `evidence/01-nociceptive-coding.md` §5 (allodynia: how Aβ touch comes
  to be read as pain) and §6 (is there a peripherally decodable pain code); `evidence/03-writing-the-signal.md`
  §3 (DRG stimulation).

## The model and the shipped inputs (read, not simulated)

The network, the 291-connection table (Foreman SCS weights), the cell templates, the E_anion rule
(the four inhibitory synapses on the WDR neuron, rows 286, 287, 289, 290, are shifted; the two onto EX are
not) and the output (WDR soma upward crossing of -30 mV) are those of S-2's `PREDICTION.md`, reused by
import (`dh_model.py`); `S-002-dorsal-horn/` is not edited. Fibres: 0-14 Aβ, 15-29 Aδ, 30-44 the
surround input (SG76), 45-74 C. Temperature 36 C.

**The shipped inputs (from the data files, per-fibre means).** `Foreman SCS` (41 s): Aβ fibres
**8.96 Hz** each (independent trains), Aδ 8.42 Hz, C 2.68 Hz, surround fibres 26 events each: 25 pulses
at 1 Hz from t = 16100.8 ms plus one dummy event at 1e9 ms. `A Fiber Inhibition` (221 s): one cycle every 2 s;
C fibres once per cycle; Aβ and Aδ fibres twice per cycle (in the first cycle Aβ at 1002.4 and 1152.4 ms,
C at 1095.9 ms, Aδ at 1019 and 1169 ms); surround fibres only dummy events at 1e9 ms. `WindUp` (21 s): 20 stimuli at 1 Hz,
all of Aβ, Aδ and C. **Declared background Aβ input:** the S-2b stimulation experiments carry
**9.0 Hz per Aβ fibre** (independent Poisson trains), taken from the shipped Foreman SCS file
(8.96 Hz, rounded). The shipped file's Aδ background (8.42 Hz) is **not** carried, a declared
departure: the Aδ route excites the WDR directly and would add a second driver to a study that
separates touch from C. This 9 Hz Aβ train is also **the touch level** of Q1 and Q2.

## Operational definitions (fixed here)

- **Run.** From `finitialize` at rest, **5.5 s**, scored on **[1.5 s, 5.5 s)** (spike = soma upstroke
  crossing in the window). Main `dt` 0.025 ms; 0.0125 ms (the published value) for candidate 0's control
  and the convergence check. Wind-up and A-fibre runs use the shipped timing (21 s each).
- **Shift grid.** Δ in {0, 2.5, 5, 7.5, 10, 15, 20, 30} mV (E = -70 + Δ).
- **Seeds.** 2 per cell (4 for the held-out feature F), paired: the same C, touch and stimulation
  trains in every condition and at every shift of a network.
- **Generators.** C: 30 independent Poisson trains at `r_C` per fibre; "C = 0.5" is the same trains thinned
  with probability 0.5. Touch: 15 independent Poisson trains at 9.0 Hz. **Stimulation:** regular pulses on
  the 15 surround fibres 30-44, all in step, first pulse at 1/f; primary frequency **40 Hz** (inside the
  published 30-100 Hz window, chosen before any run). The Aβ background of the stimulation experiments is
  the touch train.
- **C drive match (per network).** `r_C` is the smallest value of {0.5, 0.625, ..., 2.5} Hz per fibre at
  which the mean (2 seeds) C-only WDR rate at Δ = 0 is >= 2 Hz, found by bisection on the grid (the
  rate is monotone up to noise); the network is **accepted on this feature iff that rate is also <= 15 Hz**
  (a rate above 15 Hz, or a grid top below 2 Hz, is a counted rejection). For candidate 0, the curve
  above gives `r_C` = 1.0 Hz per fibre (2.12 Hz) at `dt` 0.025.
- **Conditions** (touch, C level, stimulation): C1 (C only), Ch (C = 0.5), T (touch only), TC (touch plus C),
  TCh (touch plus C = 0.5), TS (touch plus stimulation), and, on subsamples, CS (C plus stimulation) and TCS.
  R_x(Δ) is the mean WDR rate (Hz) over seeds.
- **Touch-evoked output (clean):** R_T(Δ), C off. **C-driven output:** R_C1(Δ). **Touch on background:**
  E(Δ) = R_TC - R_C1; with C = 0.5, E_h(Δ) = R_TCh - R_Ch.
- **Onset shift (Q1), per network:** the smallest grid Δ > 0 with R_T(Δ) >= R_T(0) + **2.0 Hz**; "none" if
  no grid shift does (counted as 45 mV in the median, and the share with an onset is reported).
- **Reductions (population level; ratio of means over networks).** red_S(Δ) = 1 - mean(R_TS)/mean(R_T),
  defined only where mean(R_T) >= 0.5 Hz. red_C(Δ) = 1 - mean(R_Ch)/mean(R_C1). red_Ch(Δ) = 1 -
  mean(E_h)/mean(E), defined only where mean(E) >= 0.5 Hz. Intervals are **bootstrap 95% CIs**
  (10000 resamples of whole networks, percentile).

## The control: calibration and validation are separate

**Calibration features** (an ensemble member is accepted on these, and only these):

- **W, wind-up** (abstract: "reproducing ... wind-up"). Unchanged from S-2: shipped WindUp input; per
  stimulus k = 1..20 WDR spikes in [1000k, 1000k+1000) ms; pass iff mean(16-20) >= 1.5 x mean(1-5) and the
  difference >= 1.0 spike per stimulus.
- **A-beta, A-fibre inhibition** (abstract: "A fiber-mediated inhibition"). Shipped A-fibre-inhibition
  input, first 10 cycles (21 s), four runs: C only; C plus Aβ only; C plus Aδ only; C plus all A. WDR spikes
  per cycle in [1000 + 2000k, 3000 + 2000k) ms, k = 0..9. **Pass iff mean(C only) >= 1.0 spike per cycle and
  mean(C plus Aβ only) <= 0.80 x mean(C only).** The Aδ-only and all-A runs are recorded for accepted networks
  and are not part of the criterion.
- **C drive match** (above).

**Held-out validation feature (not used to accept a network):**

- **F, the stimulation-frequency window** (abstract: "SCS frequencies of 30-100 Hz maximally inhibited the
  model WDR neuron, while frequencies under 30 Hz and over 100 Hz excited"). At Δ = 0, condition TCS
  (touch 9 Hz, C at `r_C`, stimulation on the surround fibres) at f in {5, 10, 20, 30, 40, 60, 100, 150,
  200} Hz against TC without stimulation, **4 seeds**; rho(f) = R(f)/R(no stimulation). Evaluable iff the
  TC baseline >= 1.0 Hz. **Pass iff** evaluable and (i) min over {30, 40, 60, 100} of rho <= 0.80 **and** lower
  than the min over {5, 10, 20, 150, 200}, (ii) max over {5, 10, 20} of rho >= 1.10, (iii) max over {150, 200}
  of rho >= 1.10. Run for candidate 0 at both `dt`, and for the first 60 accepted networks at 0.025 ms.

Because F is held out, "the ensemble was selected to show the published frequency window" is false by
construction; the share of networks that show it is a result. A second held-out registration is the
Aδ-only run (reading R-A below).

## Ensemble

- **Sampled** (log-uniform, multiplicative on the shipped value; `numpy default_rng(20261119 + i)` for
  candidate i, candidate 0 all factors 1; a fresh draw, not S-2's): the nine weight groups of S-2
  (`GROUP_ROWS`) each x [0.5, 2], and five conductance factors (WDR iCaL, WDR iKCa, WDR iNaP x [0.5, 2]; SG
  hillock B_Na, WDR hillock HH2 x [0.8, 1.25]). The surround **input** weights (rows 90-104) are not
  varied, only their outputs (declared).
- **Acceptance** is the three calibration features. Candidates are taken in index order until **200 are
  accepted**, up to **1500 considered**; if 200 cannot be accepted in 1500 the result is NO VERDICT and the
  counts at each stage (W, A-beta, drive match) are reported.
- **Main measurement** on all accepted networks: conditions C1, Ch, T, TC, TCh, TS x 8 shifts x 2 seeds
  (96 runs of 5.5 s) plus the Aδ-only and all-A runs of the A control.
- **Validation subsample** (F): the first 60 accepted networks.
- **Sweep subsample** (Q3 and P3): the first 40 accepted networks. Frequency sweep f in {5, 10, 20, 40, 80,
  160} Hz in TCS at Δ in {0, 5, 10, 15, 30}; and, at Δ_ref = 5 and Δ_prog = 15, the conditions TS and CS under
  each variant (below) and CS under no variant.
- **Convergence:** the first 10 accepted networks, conditions C1, T, TS at Δ in {0, 20}, seed 1, at `dt`
  0.025 and 0.0125 ms. **Pass iff** the median |dR| over cells is <= 1.0 Hz **and at most 10% of the 30
  classifications flip**. The classifications are (a) R_T(20) >= R_T(0) + 2.0, (b) R_TS(0) < 0.8 R_T(0), (c)
  R_TS(20) < 0.8 R_T(20). Otherwise the result is INCONCLUSIVE regardless of the numbers.

## Predictions with thresholds and kill conditions

Verdict words: **SUPPORTED**, **REFUTED**, **INCONCLUSIVE**, **NOT SUPPORTED, NOT REFUTED**. A shift's
interval is classed **R** (lower bound >= 0.20), **N** (upper bound < 0.20) or **S** (spans 0.20) for
reductions. **INCONCLUSIVE** means: the verdict as classified is not SUPPORTED or REFUTED, but re-classing
the S cells as R or N in some assignment would make it one. Floor: **n >= 200 networks** (40 for the
sweep subsample) before any word other than INCONCLUSIVE is printed; never a headline from one network or
one seed.

- **P0 (Q1, onset).** Median onset shift over accepted networks is **<= 10 mV** (touch begins to drive the
  projection neuron before E_anion rises 10 mV, to -60 mV). **SUPPORTED** iff the bootstrap CI of the median
  has upper bound <= 10. **REFUTED (kill)** iff the CI lower bound is > 10. Otherwise INCONCLUSIVE. My
  guess is a median of **5 mV**; 60% SUPPORTED, 10% REFUTED, 30% INCONCLUSIVE. This leans on the S-2
  diagnostic of candidate 0 (onset in (0, 10] mV at 10 Hz), disclosed above; whether it carries to an
  ensemble is the open point.
- **P1 (Q2a, stimulation on the surround input at 40 Hz, touch-evoked output).** "Once inhibition has
  collapsed, stimulation on the surround input stops reducing touch-evoked output while reduced C input
  still reduces C-driven output." With red_S (T against TS) and red_C (C1 against Ch) classed over the 8
  shifts. **REFUTED (kill)** iff red_S is R at **every** defined shift (stimulation keeps reducing
  touch-evoked output at all shifts). **SUPPORTED** iff there is a first grid shift Δ* such that (i) some
  smaller shift is R, (ii) red_S is N at Δ* and at every larger defined shift, and (iii) red_C is R at every
  grid shift >= Δ*. **Gated by G5.** My prediction: SUPPORTED **40%**, REFUTED 10%, INCONCLUSIVE 25%, NOT
  SUPPORTED NOT REFUTED 25%. The mechanism I expect, which the result may refute: the stimulation acts
  through SG76's GABA-A synapses onto the WDR, whose reversal potential is the shifted one, so its effect
  should weaken and change sign as Δ rises, while the synapse onto EX (not shifted) keeps reducing the
  C pathway.
- **P2 (Q2b, reduced C input, touch-evoked output on background).** Reduced C input (C = 0.5) leaves
  touch-evoked-on-background output largely unchanged after collapse. Over grid shifts >= the population
  median onset shift where mean(E) >= 0.5 Hz (at least two such shifts needed, else INCONCLUSIVE):
  **SUPPORTED** iff red_Ch is N at every one of them; **REFUTED (kill)** iff red_Ch is R at every one. Reported
  next to it and not gated by it: red_C (C = 0.5 reduces C-driven output; prediction: R at >= 6 of 8
  shifts, 80%). My prediction: SUPPORTED **45%**, REFUTED 15%, INCONCLUSIVE 25%, NOT SUPPORTED NOT REFUTED
  15%. The live alternative is that C input amplifies touch-evoked output through NK1 and the calcium
  currents, the coincidence mechanism of C-003 (closed from both sides in `ledger/REFUTED.md`).
- **P3 (Q3, which observable change separates the three causes).** On the 40-network sweep subsample,
  reference state Δ_ref = 5 mV at the primary frequency (40 Hz) and the sweep.
  - **Selectivity** u = relief_T - relief_C, with relief_T = 1 - R_TS/R_T and relief_C = 1 - R_CS/R_C1 at
    the same shift and variant (relief can be negative); **mean relief** = (relief_T + relief_C)/2.
    A network is evaluable at a state only if R_T >= 1.0 Hz and R_C1 >= 1.0 Hz there; non-evaluable networks
    are excluded and counted.
  - **Optimum** f*(state) = the first frequency of the 6-point sweep at which R_TCS is lowest.
  - **Three modelled causes**, each a change from the reference state: **progressive disinhibition** = Δ
    from 5 to 15 mV; **habituation** (H) = at Δ = 5 each pulse fails independently on each surround fibre
    with probability 0.5 (a uniform loss of stimulation efficacy that does not touch the circuit; recovery off
    stimulation is true of it by definition and is not simulated); **lead drift** = D1: stimulation reaches 5 of
    the 15 surround fibres; D2: stimulation reaches all 15 surround fibres and, in addition, the 15 Aδ fibres.
    Both at Δ = 5.
  - **Signature** of a change: *selective loss* (u falls by >= 0.20 against the reference) **and** *the optimum
    moves* (f* changes by at least one step of the 6-point grid).
  - **Prediction:** progressive disinhibition shows the full signature in more than half of the evaluable
    networks; H does not (uniform loss: |change in u| <= 0.10 and f* unchanged) ; D1 moves the optimum without
    selective loss; D2 is not predicted. **SUPPORTED** ("the pair (selectivity, optimum) separates
    disinhibition from the other three in this model") iff the proportion of evaluable networks showing the
    **full signature** has Wilson 95% lower bound > 0.5 for progressive disinhibition **and** Wilson upper
    bound < 0.5 for each of H, D1, D2. **REFUTED (kill)** iff for progressive disinhibition the Wilson upper
    bound < 0.5. **INCONCLUSIVE** if any of these four intervals spans 0.5. Otherwise NOT SUPPORTED, NOT
    REFUTED. **Gated by G5.** My probability of SUPPORTED: **20%**; the likeliest failure is D1 or D2 also
    showing the signature, or H changing the optimum.
  - **Candidate observation for a treating team (conditional on P3, a hypothesis, never advice):** if, over
    time, relief of touch-evoked pain falls before relief of background pain does, and the stimulation
    frequency at which the combined pain is lowest moves, that is the pattern the model associates with
    progressive disinhibition; a uniform fall in both, with the optimum unchanged and recovery after a
    stimulation-off interval, is the habituation pattern; a change in which body region the paraesthesia
    covers is the lead-drift observation and is **outside this model**.
- **Registered readings (not predictions, no verdict word):** R-A, the share of accepted networks in which
  C plus Aδ only exceeds C only (the reviewer's candidate-0 ratio is 2.06) and the Aβ-only and all-A ratios;
  R-F, the share of the validation subsample that passes F (Wilson interval) and the median rho(f) curve; the
  onset histogram; red_S per frequency in the sweep.

## Verdict rule

`simulations/verdict.py` computes a Student-t interval of one mean against one threshold; it has no
ratio-of-means interval, no median interval, no Wilson interval. So, as S-2 and S-1b did, a local rule with
the same intent: **bootstrap 95% CI** (10000 resamples of networks, percentile) for medians and ratios of
means, **Wilson 95% intervals** for proportions, INCONCLUSIVE whenever an interval spans its threshold in a way
that decides the outcome, and the floor above.

## Gates: what must hold before P0 to P3 may be read

- **G6, the oracle.** `crosscheck_original_hoc.py`'s committed JSON reproduces the reviewer's four numbers
  (to 0.1 spike per cycle) at `dt` 0.025, and the equivalence test (port against original on the same
  protocol) passes. **If not, the port is not trusted: everything below is NO VERDICT.**
- **G1, calibration at candidate 0.** Candidate 0 passes W and A-beta and has a drive match at `dt` 0.025
  **and** 0.0125. If not, NO VERDICT and nothing beyond candidate 0's control numbers (S-2's rule).
- **G2, ensemble.** 200 accepted within 1500 considered.
- **G3, convergence.** The dt-halving check passes.
- **G4, wiring.** `test_s2b_sites.py` and `test_s2b_protocol.py` pass at the start of the run; their result and
  file hashes are logged.
- **G5, validation (gates P1 and P3 only).** Candidate 0 passes F at 0.025 and 0.0125 ms. If G5 fails, P1 and P3
  print "NO VERDICT" and a plainly labelled "conditional reading, not a verdict"; P0 and P2 are read
  under G1-G4 and G6.

If any gate fails, the affected P print no bold verdict word.

## Tests (in the repository, run at the start of the run)

- `test_s2b_sites.py`: topology-derived. The surround fibres are the fibres whose every connection targets
  SG76, derived from the built network, and equal the protocol's stimulation fibres 30-44; SG76's outputs are
  GABA-A onto WDR and EX (rows 288-290); the Aβ fibres are the ones with a non-zero path to SG75, the Aδ
  fibres have none; the shift changes exactly the four WDR inhibitory synapses; the WDR recorder is on the soma
  at 0.5. **Mutation checks** (run with `python -B`, reported): pulses assigned to Aβ fibres 0-14 (S-2's
  error), the recorder moved to the hillock, and a shift set that includes the EX synapses must each make it
  fail.
- `test_s2b_protocol.py`: generators, pairing, the drive match, the judges and the verdict classes, on
  synthetic numbers.
- `test_s2b_oracle.py`: the **non-circular** check. The committed original-hoc numbers (produced by NEURON
  executing the authors' hoc, not by this code) against the port on the same four A-fibre conditions at
  `dt` 0.025; a mutated port (Aβ-to-SG75 weight set to 0) must fail it.

## Compute budget

Not measured before this commit except the 200 ms smoke run and the curve above (a 5.5 s run takes about
9 s). By count: the control about 100 simulated seconds per candidate; the main measurement 96 runs of 5.5 s
and 2 of 21 s per accepted network, about 15 to 20 minutes of one core; the sweep, validation and convergence
subsamples a few hours of one core in total. Workers: 12 or fewer. Any reduction is a disclosed amendment made
without looking at P0 to P3 quantities.

## Declared limits

- **Under-constrained weights.** The shipped weights are one parameter set; the ensemble samples a box
  around it (x0.5 to x2); the data for most weights are not in the abstract. Medlock 2022's degeneracy result
  (abstract, PMID 35232767) is a warning that many weight sets give the same normal function and different
  pathological ones. **The outputs are discriminating hypotheses, not verdicts about patients.**
- **What it cannot settle:** whether any patient has a KCC2/BDNF-type disinhibition (E-01 §5 says it is the
  dominant allodynia route in animal work, not that it is the mechanism in any person with CRPS); the size of
  any real E_anion shift (the grid is in model millivolts); anything about stimulation settings, amplitudes,
  charge, lead position, or weeks (the model is acute, seconds long, with synthetic spike trains); one
  projection-neuron type and a four-cell circuit, no PKCγ or SOM-neuron circuit and no receptive-field
  geometry; independent Poisson afferents; stimulation as synchronous pulses on a surround input with no conduction
  failure, collision or antidromic effects; and whether clinical-amplitude ganglion stimulation reaches the surround
  inhibitory route at all (the model's "surround input" is the authors' representation of Aβ-driven surround
  inhibition; the mapping of a ganglion stimulator to it is **an assumption**, not a result).
- **The positive control is my operationalisation** of three qualitative claims; passing it shows the port and
  driver behave like the starting model in those respects and says nothing about whether the starting model is
  right about dorsal horns.
- **The wind-up and A-fibre inputs** are the shipped ones; the paper's figure values were not consulted (full
  text not read).
- **Short runs.** 4 s scored windows after 1.5 s of transient; the NK1 synapse decays with a 3 s time constant,
  so slow components are not at steady state. A 2-seed average per network, 4 for F.
- **Nothing here is a stimulation setting or advice.** E_anion shifts are model millivolts, frequencies are those
  of a synthetic pulse train in a four-cell model. **These results are not stimulation settings.**

## Hand prediction summary, before running

| Quantity | My guess | Probability |
|---|---|---|
| Oracle reproduces the reviewer's four numbers (G6) | yes | 90% |
| Candidate 0 passes W, A-beta and the drive match at both `dt` (G1) | yes | 70% |
| 200 accepted in 1500, given G1 (acceptance rate guessed at 15% to 30%) | yes | 70% |
| G3 convergence passes | yes | 65% |
| Candidate 0 passes the held-out F at both `dt` (G5) | yes | 30% |
| P0 SUPPORTED (median onset <= 10 mV; guess 5 mV) | supported | 60% |
| P1 SUPPORTED, given G5 | supported | 40% |
| P2 SUPPORTED | supported | 45% |
| P3 SUPPORTED, given G5 | supported | 20% |

About 0.9 x 0.7 x 0.7 x 0.65 = **29%** that G6, G1-G4 all hold so that P0 and P2 are read as verdicts; about
**9%** that G5 holds as well. The likeliest single outcome is a partial reading (P0, P2) or NO VERDICT at the
control, with the control numbers reported. The most informative failure would be G5 failing while G1 holds:
the model reproduces its own inhibitory and wind-up behaviour but not its published stimulation-frequency
window on this driver.

---

## Amendments (appended after commit #1; the text above is not edited)

### Amendment 1 (2026-11-18, after commit #2 and before the main run): the pipeline pilot

**Disclosure.** After the code was committed (`7afbdf7`, then `b89c639`), `simulate_s002b.py --pilot` was run
once end to end, 2026-11-18 15:33 to 15:57, 8 workers, writing only the gitignored `results/pilot/`. It uses a
smaller protocol (3 s runs scored on [1, 3) s, one seed, shifts 0, 5, 15 and 20 mV, an ensemble target of 4
networks, 2 networks for the validation, sweep and convergence subsamples). **Nothing from it is a result**; G2
and G3 fail there by construction. A first start of the pilot, minutes earlier, stopped at its own gate because
the gate tests (which check the registered constants) inherited the pilot environment; the fix is `b89c639`.

**What the pilot showed, and what I did about it (nothing).**

1. The pipeline runs end to end and writes results.json, results.md, the PNGs, the traces and the zip. The
   candidate-0 A-control counts of the port equal the oracle's at both `dt` (C only, C plus Aβ, C plus Aδ, C plus
   all A: 11.3, 8.0, 23.3, 19.4 at 0.025 ms; 11.2, 7.0, 23.2, 15.8 at 0.0125 ms).
2. **The held-out frequency feature F failed for candidate 0 at both `dt` in the pilot protocol.** With touch 9 Hz
   and C input (baseline 7.5 Hz), stimulation on the surround fibres lowered the WDR rate to 4.5 Hz at 5 Hz, 1.0 Hz
   at 10 Hz and 0 at 20 Hz and every higher frequency in the grid; nothing excited it under 30 Hz or over
   100 Hz (one seed, 2 s scored window, so a pilot reading, not a result). If that holds in the main
   protocol, G5 fails.
3. In the pilot protocol candidate 0's drive match was 1.25 Hz per fibre (the registered protocol's curve gives
   1.0); the windows differ, and the match in the main run is whatever the registered rule gives.

**No design change was made on the basis of the pilot**: F stays held out, G5 stays as registered, thresholds
and predictions above are unchanged. The only change is my belief: I now put the probability that candidate 0
passes F at both `dt` (G5) at **10%**, not 30%, so about **3%** that P1 and P3 are read as verdicts. If G5 fails,
P1 and P3 print NO VERDICT and a labelled conditional reading, as registered, and the result for Q2a and Q3 is
that the model does not reproduce its published stimulation-frequency window on this driver.

**Compute estimate** (simulated seconds times the observed 1.7 to 2 s of wall per simulated second per core):
control about 4 h, main measurement about 5 h, validation, sweep and convergence about 2 h, at 12 workers:
**about 11 hours of wall time**, dominated by the main measurement and the control of 1000 or so candidates.

### Amendment 2 (2026-11-19, after the main run; append only): a declared limit added

No rule, number or result changed. One declared limit is added to the list above: **the circuit has no
descending (brainstem) input.** The four-cell network contains afferent fibres, two inhibitory interneurons, one
excitatory interneuron and one projection neuron, and nothing that stands for descending facilitation or
inhibition. Whether such input would change any of the model's outputs here is not tested. Source:
`evidence/10-descending-modulation.md` §8.2. The report (`results/main/results.md`) was also reworded after the
run, display only: the P1 and P3 conditional readings moved under a "not verdicts" heading, the registered rules
for P0 and P2 are quoted beside their verdicts, and P2's SUPPORTED is stated in plain terms.

### Amendment 3 (2026-11-19, after review of PR #15; append only): the P2 rule was non-diagnostic as registered

No simulation was re-run and no registered rule, threshold or number changed; the verdict words stand as the
registered rules produced them.

1. **P2 as registered could not have returned REFUTED at the shifts it reads.** The rule reads red_Ch at shifts
   at or above the median onset (here 15, 20 and 30 mV) and REFUTES only if red_Ch is class R (lower bound >= 0.20)
   at every one. There the excess E = R_TC - R_C1 is almost the touch-only rate R_T, so red_Ch is near 0 whenever C adds
   roughly additively. The largest red_Ch reachable (if halving C removed every influence of C on the total, R_TCh =
   R_T) is 1 - (R_T - R_Ch)/E, computed in `results.md` from the data: 0.12, 0.03 and -0.01 at 15, 20 and 30 mV,
   all below 0.20. **The P2 SUPPORTED is therefore not informative** about whether touch-evoked output is
   independent of C input. **No positive control was registered for red_Ch** (a case in which the rule would have
   to return REFUTED); that was a design omission of this file. The report now labels the verdict so, prints the
   ceiling, and reports the informative quantities: the interaction TC - T - C1 per shift with bootstrap CIs, and
   the fall in total output when C is halved (12% at 15 mV in the data).
2. **Pilot disclosure, explicit.** The pipeline pilot of Amendment 1 ran the full pipeline, and I did read its
   `results/pilot/results.md`, which contains P0 and P2 quantities on 4 networks of a smaller protocol (3 s runs, 1
   seed, shifts 0, 5, 15, 20 mV): a median onset of 15 mV with CI [5, 20], red_S, red_C and red_Ch tables, and P2
   classes N at 15 and 20 mV with E of 31.9 and 81.6 Hz. Amendment 1 disclosed only the F reading, which was the part
   I acted on; the P0 and P2 readings were seen too, and they did not change any threshold, rule or prediction. The
   predictions above were written before that pilot.
3. **Report changes, display and output only:** `results.json` now carries `verdict` ("NO VERDICT" for P1 and P3) and
   `conditional_reading_not_a_verdict` in lower case instead of an upper-case verdict field; R-F explains that 42 of 60
   networks fall below the registered baseline rule F_BASE_MIN = 1.0 Hz and prints both Wilson intervals; P0 states the
   onset distribution (100 of 200 networks at or below 10 mV, so the estimate sits on the threshold and INCONCLUSIVE is
   a discretisation outcome on the registered grid); the funnel accounting is explicit.
