# Pre-registered prediction for S-2: dorsal-horn model of touch-evoked pain

**Written 2026-11-17, before any simulation run of any kind, including pilots.**
This file is commit #1 of its branch and alone in that commit; no code and no
results file exist in the history before it. Intent:
`intent/simulation/2026-11-17-s2-dorsal-horn.md`. If the simulation disagrees
with this file, the simulation is probably right and this file is the record of
my being wrong.

What was done before this commit, and nothing else: the literature and ModelDB
searches in Appendix A were run; the abstracts quoted below were fetched through
NCBI E-utilities efetch; the ModelDB 168414 code was downloaded from the GitHub
mirror into an empty scratch directory, its zip checked with `file` and
sha256, and every `.mod`, `.hoc` and data file that this study uses was **read**
(none was executed; no `mosinit.hoc`, `Shell.hoc` or other script was run); a
Python 3.13 virtual environment with `neuron==9.0.2` was created and `import
neuron` was run once to print its version. **No NEURON simulation, no mechanism
compilation and no network build has been executed for S-2.** What I know about
the starting model's behaviour is what its abstract and its shipped input files
say and nothing else.

## The questions

Taken from the intent file. The phenotype is a population-level one: long-standing
post-surgical CRPS-labelled foot pain with a ganglion stimulator, touch-evoked
allodynia plus a separate background pain. Nothing about any individual.

- **Q1.** As the anion reversal potential E_anion shifts upward (collapsing
  inhibition), at what shift does touch-type (Aβ) input start to drive the
  projection (pain-output) neuron?
- **Q2.** Once inhibition has collapsed, do two manipulations still reduce
  touch-evoked output, separately from C-driven output? (a) Aβ recruitment at
  stimulation frequencies (the Graham 2019 reading of clinical-amplitude
  ganglion stimulation, PMID 30981900); (b) reduced C input (the T-junction
  reading).
- **Q3.** Which observable change over time would distinguish progressive
  disinhibition from habituation and from lead drift? This is the "specificity
  column" in `ledger/OPEN.md`. It is phrased below as a **candidate observation
  for a treating team to consider, never as advice**.

## Prior art and the starting model

Appendix A records every query verbatim. In summary, no model found answers all
three questions (reading **abstracts only**; I did not read full texts, which are
mostly paywalled). The closest:

- **Zhang, Janik & Grill 2014** (J Neurophysiol 112:552-567, PMID 24790169),
  ModelDB 168414, NEURON. This is the starting model. Its abstract, verbatim:
  "Spinal cord stimulation (SCS) is a clinical therapy for chronic, neuropathic
  pain, but an incomplete understanding of the mechanisms underlying SCS
  contributes to the lack of improvement in SCS efficacy over time. To study the
  mechanisms underlying SCS, we constructed a biophysically based network model
  of the dorsal horn circuit consisting of interconnected dorsal horn
  interneurons and a wide-dynamic range (WDR) projection neuron and
  representations of both local and surround receptive field inhibition. We
  validated the network model by reproducing cellular and network responses
  relevant to pain processing including wind-up, A fiber-mediated inhibition,
  and surround receptive field inhibition. We then simulated the effects of SCS
  on the activity of the WDR projection neuron and found that the response of the
  model WDR neuron to SCS depends on the SCS frequency; SCS frequencies of
  30-100 Hz maximally inhibited the model WDR neuron, while frequencies under 30
  Hz and over 100 Hz excited the model WDR neuron. We also studied the impacts on
  the effects of SCS of loss of inhibition due to the loss of either GABA or KCC2
  function. Reducing the influence of local and surround GABAergic interneurons
  by weakening their inputs or their connections to the WDR neuron and shifting
  the anionic reversal potential of the WDR neurons upward each reduced the range
  of optimal SCS frequencies and changed the frequency at which SCS had a maximal
  effect. The results of this study provide insights into the mechanisms of SCS
  and pave the way for improved SCS parameter selection."
  What kind of numbers these are: "30-100 Hz", "under 30 Hz", "over 100 Hz" are
  the published frequency effect, for the model WDR neuron, under SCS. The
  abstract gives **no number for the size of the E_anion shift** and no
  wind-up magnitude, so the control below is built on the three qualitative
  features and on tolerances I chose (declared as mine).
- **Medlock et al. 2022** (J Neurosci 42:3133-3149, PMID 35232767), ModelDB
  267056, NetPyNE. Considered and **not chosen**. Reasons (my reading of its
  abstract): its validation is disinhibition and cell-type ablation, not
  stimulation frequency or a shifted anion reversal; its network is large and
  its synaptic weights come from a genetic algorithm that reveals degeneracy,
  which would make a 200-network ensemble that also needs the Zhang-style
  frequency control far heavier; and the question needs the published
  frequency effect as a positive control, which Zhang has and Medlock 2022 does
  not report. Medlock's degeneracy result is relevant to the declared limits.
- Partial overlaps, none a full answer (abstracts read): **Gilbert et al. 2023**
  (PMID 37727912) reports that changing synaptic weights unmasks a low-threshold
  excitatory pathway from Aβ afferents to a nociceptive-specific projection
  neuron and that optimal stimulation frequencies differ across neuropathic
  conditions; **Medlock & Prescott 2026** (PMID 41735055) reports that
  kilohertz-frequency SCS preferentially activates inhibitory neurons and so
  reduces allodynia in a receptive-field model; **Ginsberg et al. 2025**
  (PMID 39808669) analyses E-I balance in firing-rate subcircuits; **Rogers et
  al. 2024** (PMID 38744531) models frequency-dependent dorsal-horn output.
  Zhang 2014's abstract already says that an upward shift of the anion reversal
  narrows the effective frequency range and moves the optimum, so part of Q3 (the
  "frequency optimum moves" signature) is **stated in the starting model's own
  abstract**; S-2 tests it in an ensemble and adds the contrast against the
  other two causes. What no abstract states is: the shift at which Aβ input
  starts to drive the projection neuron, across an ensemble; a separate
  accounting of touch-evoked and C-driven output under both manipulations;
  or the time-course contrast. That is the only reason this study is built; if a
  full-text reading shows otherwise, this file is the record of what was known.

## The starting model, as read (not yet run)

All of this comes from reading ModelDB 168414's `CellTemplates.hoc`, the
`FromVector`, `ToVector`, `SynapseVector`, `WeightVector`, `DelayVector`,
`CellTempList.dat` and `CellTypeVector.txt` data files, and the mechanism files.
My Python re-implementation reads the data files as **data** and re-creates the
templates in Python; it does not execute any shipped script.

- **Cells (4).** Cell 75 and cell 76 are `MelnickSG` neurons (substantia
  gelatinosa, GABA and glycine releasing; cell 75 receives local Aβ input,
  cell 76 receives the "surround" input from fibres 30 to 44); cell 77 is
  `AguiarIN` ("EX cell", excitatory interneuron); cell 78 is `AguiarWDR`
  ("T cell", the wide-dynamic-range projection neuron). Input "fibres": 0 to 14
  Aβ, 15 to 29 Aδ, 30 to 44 the surround input, 45 to 74 C (30 fibres).
- **Connectivity (291 connections, rows 0 to 290), weights as shipped in the
  Foreman SCS folder** (identical to the A-fibre-inhibition folder; the WindUp
  folder differs only in setting surround inhibition 288 to 290 to zero): Aβ to
  SG75 AMPA (rows 0-14); Aβ to WDR AMPA (15-29) and NMDA (30-44); Aδ to WDR
  AMPA and NMDA (60-89; Aδ to SG75 has weight 0); surround 30-44 to SG76
  (90-104); C to EX AMPA, NMDA and NK1 (105-194); C to WDR NK1 (195-224);
  SG75 to EX GABA-A (225); EX to WDR AMPA and NMDA (226-285); SG75 to WDR
  glycine (286) and GABA-A (287); SG76 to EX GABA-A (288) and to WDR GABA-A
  (289, 290).
- **E_anion.** The six inhibitory connections carry E = -70 mV (the shipped
  `ERevVector.txt`; the loader that would apply it is commented out in the shipped
  `MakeNetwork.hoc`, and the template sets `e = -70` on the GABA-A synapses and
  the glycine synapse defaults to -70). **My shift applies to the four inhibitory
  synapses on the WDR neuron** (rows 286, 287, 289, 290; WDR synapse indices 150
  to 153), as in the Zhang abstract ("shifting the anionic reversal potential of
  the WDR neurons upward"). The two onto the excitatory interneuron (225, 288)
  are not shifted. That is my choice and a declared limit.
- **Projection-neuron output** is WDR soma spikes: soma `v(0.5)` crossing -30 mV
  upward (the shipped output recorder). Inhibitory-interneuron trace: SG75 soma.
- **Mechanisms (17)** to be copied into `mod/`: AMPA_DynSyn, NMDA_DynSyn,
  GABAa_DynSyn, Glycine_DynSyn, NK1_DynSyn, B_Na, B_A, B_DR, KDR, KDRI, SS, HH2,
  CaIntraCellDyn, iKCa, iCaL, iNaP, iCaAN. Their only `VERBATIM` blocks are
  `return 0;`; there is no `system`, `popen` or file call in any of them.
- Temperature 36 C; the published `dt` is 0.0125 ms.

## Operational definitions (fixed here, not re-opened)

- **Run.** Every run starts from `finitialize` at rest, lasts **7.5 s**, and is
  scored on the window **[1.5 s, 7.5 s)** (a spike counts if its soma upstroke
  crossing falls in the window). Input events are delivered through the shipped
  connection table (one event per afferent spike per connection). Main `dt` =
  0.025 ms; the published 0.0125 ms is used for the default-network control and
  for the convergence check. A run is **at one E_anion shift Δ** (E = -70 + Δ mV
  on the four WDR inhibitory synapses).
- **Shift grid.** Δ in {0, 5, 10, 15, 20, 25, 30, 40} mV.
- **Input generators** (numpy `default_rng`, seeded from the network index, the
  condition's seed index 1 to 3, and a fixed fibre index, so that the same seed
  gives the **same** C and touch spike trains at every shift and in every
  condition of a network: paired comparisons).
  - **C background:** the 30 C fibres, independent Poisson trains, rate `r_C` per
    fibre. `C = 1` means `r_C`; `C = 0.5` the same trains thinned by
    independent probability 0.5 (the T-junction reading, "reduced C input"); `C = 0`
    none.
  - **Touch:** the 15 Aβ fibres, independent Poisson trains, rate `r_T` per fibre.
  - **SCS (the Aβ-recruiting stimulus, the Graham 2019 reading):** all 15 Aβ
    fibres fire together as regular pulses at frequency `f`, first pulse at
    `1/f`. Where touch and SCS are both on, each Aβ fibre's spike train is the
    **union** of its touch spikes and the SCS pulses (no collision, no
    refractoriness between them; a declared simplification).
  - **Matched levels.** `r_C` and `r_T` are **per-network, set at Δ = 0**:
    `r_C` is the smallest of {2.5, 5, 10, 20} Hz per fibre at which the mean WDR rate
    over 3 seeds with C only is in [2, 15] Hz (the "ongoing, C-driven"
    activity); `r_T` is the smallest of {10, 20, 40, 80} Hz per fibre at which
    the mean WDR rate over 3 seeds with touch only (C off) is >= 0.5 Hz, and 80 Hz if none
    reaches it. A network with no `r_C` in the set is rejected (counted).
    Touch is therefore each network's own "normal touch" level, not a pain level.
- **Conditions per (network, Δ, seed).** Nine: C1 (C only), Ch (C = 0.5 only), CS
  (C = 1 with SCS at 20 Hz), T (touch only), S (SCS only), TS (touch with SCS),
  TC (touch with C = 1), TCh (touch with C = 0.5), TCS (touch, C = 1, SCS).
  Rate R_x(Δ) is the mean WDR firing rate (Hz) in the scored window, averaged over
  3 seeds. 8 shifts x 9 conditions x 3 seeds = 216 runs per network.
- **Touch-evoked output (primary, "clean"):** R_T(Δ), touch alone with C off.
  **C-driven output:** R_C(Δ). **Touch-evoked on background:**
  E(Δ) = R_TC(Δ) - R_C(Δ); with C = 0.5, E_h(Δ) = R_TCh(Δ) - R_Ch(Δ).
- **Onset shift (Q1), per network:** the smallest grid Δ at which
  R_T(Δ) >= R_T(0) + 1.0 Hz; "none" if no grid Δ does. Population summary: the
  median with networks that have "none" counted as 45 mV (above the grid), and
  the proportion with an onset.
- **Reduction by a manipulation, population level (ratio of means over
  networks).** For SCS at 20 Hz on touch-evoked output: red_S(Δ) = 1 -
  mean(R_TS) / mean(R_T), defined only where mean(R_T) >= 0.5 Hz (so there is
  something to reduce). For reduced C on C-driven output: red_C(Δ) = 1 -
  mean(R_Ch) / mean(R_C). For reduced C on touch-evoked-on-background output:
  red_Ch(Δ) = 1 - mean(E_h) / mean(E), defined only where mean(E) >= 0.5 Hz.
  Intervals: **bootstrap 95% CI** (10000 resamples of whole networks,
  percentile).
- **Frequency sweep (control and Q3).** Control: f in {5, 10, 20, 30, 40, 60,
  100, 150, 200} Hz. Q3 sweep: f in {5, 10, 20, 40, 80, 160} Hz.
  `f*` is the first f of the grid at which the mean WDR rate is lowest.

## The positive control (reproduce the starting model's own published results)

Three features, each from the abstract or the shipped inputs, each with a
tolerance **I chose, before any run**. They are my operationalisations, not
numbers in the paper. A network is **accepted only if it passes all three** (and
has an `r_C`). The control is run on the unmodified shipped model first
(**candidate 0**, at `dt` = 0.025 ms **and** 0.0125 ms); **if candidate 0 fails
any feature at either dt, the result is NO VERDICT and nothing more is run
beyond reporting candidate 0's control numbers.**

- **W, wind-up** (abstract: "reproducing ... wind-up"). The shipped WindUp
  input file read as data: 20 stimuli at 1 Hz (Aβ, Aδ and C fibres each fire
  once per stimulus), 21 s. Per stimulus k = 1..20, WDR spikes in
  [1000k, 1000k + 1000) ms. **Pass** iff mean(stimuli 16 to 20) >= 1.5 x
  mean(stimuli 1 to 5) **and** the difference >= 1.0 spike per stimulus.
- **A, A-fibre inhibition** (abstract: "A fiber-mediated inhibition"). The
  shipped A-fibre-inhibition input read as data, first 10 cycles: C fibres once
  every 2 s, with Aβ and Aδ pairs at 94 ms before and 56 ms after each C event.
  Run twice: as shipped, and with all Aβ and Aδ events removed (same C events).
  WDR spikes per cycle in [1000 + 2000k, 3000 + 2000k) ms, k = 0..9. **Pass**
  iff mean(without A) >= 1.0 spike per cycle **and** mean(with A) <= 0.80 x
  mean(without A).
- **F, the SCS frequency effect** (abstract: "SCS frequencies of 30-100 Hz
  maximally inhibited the model WDR neuron, while frequencies under 30 Hz and over
  100 Hz excited"). At Δ = 0, C background at the network's `r_C`, SCS (no touch)
  at each control frequency, ratio rho(f) = R(f) / R(no SCS), 3 seeds.
  **Pass** iff (i) R(no SCS) is in [2, 15] Hz (that is the `r_C` rule) and
  (ii) min over {30, 40, 60, 100} of rho <= 0.80 **and** it is lower than the
  minimum over {5, 10, 20, 150, 200} of rho, and (iii) max over {5, 10, 20} of rho
  >= 1.10, and (iv) max over {150, 200} of rho >= 1.10.

I put "default passes all three" at about **20%** (W 65%, A 55%, F 30%, not
independent). If candidate 0 fails, the likeliest reason is my SCS driver
(synchronous Aβ pulses on all 15 fibres) not being the one the authors used,
which is a finding about this study's reproduction and **not** a finding about
dorsal horns. That risk is accepted rather than tuned away.

## Ensemble

- **Sampled (independent log-uniform, multiplicative on the shipped value,
  numpy `default_rng(20261118 + i)` for candidate i; candidate 0 is all
  factors 1):** nine weight groups, each x [0.5, 2]: Aβ to WDR (rows 15-44),
  Aβ to SG75 (0-14), SG75 to WDR (286, 287), SG75 to EX (225), C to EX
  (105-164), NK1 (165-194 and 195-224), EX to WDR (226-285), Aδ to WDR (60-89),
  surround SG76 outputs (288-290); and five conductance factors: WDR iCaL pcabar
  (soma and dend) x [0.5, 2], WDR iKCa gbar (soma and dend) x [0.5, 2], WDR iNaP
  gnabar x [0.5, 2], SG hillock B_Na gnabar (both SG cells) x [0.8, 1.25], WDR
  hillock HH2 gnabar x [0.8, 1.25].
- **Acceptance** is the positive control above (plus an `r_C`). Candidates are
  taken in index order until **200 are accepted**, up to a maximum of **1500
  considered**; if 200 cannot be accepted in 1500 the result is NO VERDICT and
  the acceptance counts are reported. The selection effect (rejected candidates)
  is reported with the count at each stage (W, A, r_C, F).
- **Main measurement** on all 200 accepted networks: the 216 runs per network.
- **Subsample for sweeps (Q3 and the secondary P1b):** the first 40 accepted
  networks. Per network: sweep f in the Q3 set in condition TCS at Δ in {0, 10,
  15, 20, 25, 40} (6 x 6 x 3 runs), and the three variants below at Δ = 15
  (3 x 6 x 3 runs) in condition TCS; plus, at Δ = 15, conditions TS and CS under
  each variant (3 x 2 x 3 runs).
- **Convergence:** first 10 accepted networks, conditions C1, T, TS and TCS, Δ in
  {0, 20}, seed 1, at `dt` = 0.025 and 0.0125 ms. Pass iff the median |dR| <= 0.5
  Hz and **at most 10% of the classifications flip**, where the classifications
  are (a) R_T(Δ) >= R_T(0) + 1.0 Hz and (b) R_TS < 0.8 R_T; otherwise the result is
  INCONCLUSIVE regardless of the numbers.

## Predictions with thresholds

- **P0 (Q1: onset).** Median onset shift among accepted networks lies in
  [10, 25] mV. **SUPPORTED** if the bootstrap 95% CI of the median lies wholly in
  [10, 25]; **REFUTED** if it lies wholly outside [5, 30]; otherwise
  INCONCLUSIVE. My guess is a median of **15 mV** (E_anion near -55 mV, above the
  WDR rest of about -65 mV and below its spike threshold), 55% that P0 is supported.
- **P1 (Q2a: SCS at 20 Hz on touch-evoked output).** "Beyond some shift, Aβ
  drive at 20 Hz stops reducing touch-evoked projection output, while removing C
  input still reduces C-driven output." Operationally, with red_S and red_C above
  (threshold 0.20 for both):
  - **Kill (P1 REFUTED):** red_S >= 0.20 with the CI lower bound >= 0.20 at
    **every** grid shift where it is defined (touch-evoked output is reduced by
    >= 20% at every shift across the ensemble).
  - **SUPPORTED:** there is a first grid shift Δ* such that (i) at least one
    smaller shift has red_S defined with CI lower bound >= 0.20 (it did reduce
    before), (ii) at Δ* and every larger shift the CI upper bound of red_S is
    < 0.20, and (iii) at every grid shift >= Δ* the CI lower bound of red_C is
    >= 0.20.
  - **INCONCLUSIVE** if, and only if, one of these CIs spans 0.20 at a shift
    where it decides the outcome.
  - Otherwise **NOT SUPPORTED, NOT REFUTED**.
  **My prediction: P1 will read NOT SUPPORTED, NOT REFUTED (55%)**, because the
  starting model's own abstract says SCS under 30 Hz **excites** the model WDR
  neuron, so 20 Hz SCS should add to touch-evoked output at every shift and
  never reduce it (clause (i) fails). SUPPORTED 15%, REFUTED 5%, INCONCLUSIVE 25%.
  This is a real prediction that the premise behind the question may be wrong
  for 20 Hz in this model; the frequency-resolved secondary P1b is there for that.
- **P1b (secondary, 40-network subsample, frequency-resolved).** The same rule as
  P1 with the reduction defined on touch-plus-background total output and the
  stimulation frequency chosen per network as the best of the 6-frequency Q3 grid:
  red_best(Δ) = 1 - mean over networks of min_f R_TCS(f) / mean R_TC, at the
  sweep shifts {0, 10, 15, 20, 25, 40}. Reported as secondary: the best-of-six
  choice biases it toward reduction, and n = 40 is smaller than the ensemble.
  Prediction: red_best >= 0.20 at Δ = 0 and falling below 0.20 by Δ = 25 or 40
  (60%).
- **P2 (Q2b: reduced C input and touch-evoked output).** Reduced C input (C =
  0.5) leaves touch-evoked-on-background output largely unchanged after collapse:
  at every grid shift >= the population median onset shift where mean(E) >= 0.5
  Hz, the CI upper bound of red_Ch is < 0.20. **SUPPORTED** if so; **REFUTED** if
  the CI lower bound of red_Ch is >= 0.20 at every such shift (reduced C does reduce
  touch-evoked output after collapse); INCONCLUSIVE if a CI spans 0.20 at a shift
  that decides it; otherwise NOT SUPPORTED, NOT REFUTED. Prediction: supported
  (50%); the live alternative is that C input amplifies touch-evoked output
  through NK1 and the calcium currents, which is a coincidence mechanism the
  programme has a conjecture about (C-003, closed from both sides in
  `ledger/REFUTED.md`).
  Reported next to it, not gated by it: red_C (as in P1 clause iii) at every
  shift: C = 0.5 should reduce C-driven output (prediction: >= 0.20 at every
  shift, 85%).
- **P3 (Q3: which observable change distinguishes the three causes).** Defined
  on the 40-network subsample at reference shift Δ_ref = 15 mV:
  - **Selectivity** u = relief_T - relief_C at 20 Hz, where relief_T = 1 - R_TS /
    R_T (C off) and relief_C = 1 - R_CS / R_C, both at the same shift/variant
    (relief can be negative); **mean relief** = (relief_T + relief_C) / 2.
  - **Optimum** f*(Δ) of R_TCS over the Q3 grid.
  - **Three modelled causes**, each a change from the reference state:
    **Progressive disinhibition** = Δ from 15 to 25 mV (two grid steps).
    **Habituation** (variant H) = at Δ = 15 each SCS pulse independently fails on
    each Aβ fibre with probability 0.5 (a uniform loss of stimulation efficacy that
    does not touch the circuit; **recovery off stimulation is true of it by
    definition and is not simulated**). **Lead drift** (a change in the recruited
    population): variant D1 = SCS recruits 5 of the 15 Aβ fibres; variant D2 = SCS
    recruits all 15 Aβ **and** the 15 Aδ fibres. Both at Δ = 15.
  - **Signature** of a change: *selective loss* = u falls by >= 0.20 against the
    reference **and** *optimum moves* = f* changes by at least one step of the
    6-point grid.
  - **Prediction:** progressive disinhibition shows both (selective loss and
    optimum moves) in more than half of networks (Wilson lower bound > 0.5);
    habituation shows **neither** in most (uniform loss: |change in u| <= 0.10
    with mean relief falling by >= 0.10, and f* unchanged); lead drift D1 moves the
    optimum without selective loss, D2 is not predicted (the Aδ route is direct
    excitation of the WDR, which could look like disinhibition or like
    habituation).
  - **Verdict rule.** **SUPPORTED** ("the pair (selectivity, optimum) separates
    disinhibition from the other two in this model") iff the proportion of
    networks showing **both** parts of the signature has Wilson 95% lower bound
    > 0.5 for progressive disinhibition **and** Wilson upper bound < 0.5 for each
    of H, D1, D2. **REFUTED** if for progressive disinhibition the upper bound is
    < 0.5. **INCONCLUSIVE** if any of these four intervals spans 0.5. Otherwise
    **NOT SUPPORTED, NOT REFUTED** (for instance if habituation also shows the
    signature). My probability that P3 is SUPPORTED is **35%**; the likeliest
    failure is D1 or D2 also showing it.
  - **Candidate observation for a treating team (conditional on P3, phrased as a
    hypothesis, never advice):** if, over time, relief of touch-evoked pain falls
    before relief of background pain does, and the stimulation frequency at which
    the combined pain is lowest moves, that pattern is the one the model
    associates with progressive disinhibition; a uniform fall in both, with the
    optimum unchanged and recovery after a stimulation-off interval, is the
    habituation pattern; a change in which body region the paraesthesia covers is
    the lead-drift observation and is **outside this model**.
- **Gating of conditional readings (S-1's lesson).** When any gate below fails,
  results.md prints no bold verdict word for P0 to P3: it prints "NO VERDICT"
  and a plainly labelled "conditional reading, not a verdict" sentence.

## Verdict rule

`simulations/verdict.py` computes a Student-t interval of **one mean** against one
threshold; it has no ratio-of-means interval, no median, no Wilson interval for
proportions. So, as in S-1b, a local rule with the same intent: **bootstrap 95%
CI (10000 resamples of networks, percentile)** for means, ratios of means and
medians; **Wilson 95% interval** for proportions; and an **INCONCLUSIVE** report
whenever an interval spans its threshold; a floor of **n >= 200 networks** (40
for the subsample) before any word other than INCONCLUSIVE is printed. Never a
headline from one network or one seed.

## Gates: what must hold before P0 to P3 may be read

- **G1, control.** Candidate 0 passes W, A and F at `dt` = 0.025 and 0.0125 ms.
- **G2, ensemble.** 200 accepted networks within 1500 considered.
- **G3, convergence.** The dt-halving check above passes.
- **G4, wiring.** The recording-site and connectivity test (below, in the
  repository as `test_sites.py`) passes at the start of the run; its result and
  the file's sha256 are logged.

If any gate fails, P0 to P3 are NO VERDICT.

## Recording-site and connectivity test

`test_sites.py` builds the network and asserts, from the **built topology**
(not from labels): the WDR output recorder is on the WDR soma at 0.5; the
SG75 recorder is on the SG75 soma; each of the six inhibitory connections has
the named pre-synaptic cell and post-synaptic cell and the named synapse type
(Glycine_DynSyn for row 286, GABAa_DynSyn otherwise), and the E_anion shift
changes exactly the four WDR synapses and no other; Aβ fibres 0 to 14 drive
SG75 and the WDR; C fibres drive EX and the WDR NK1 synapses only; surround
fibres reach SG76 only. A mutation (swapping the recorder to the WDR hillock,
or the shifted set to the EX inhibitory synapses) must make it fail; the
mutation check is run with `python -B` and reported.

## Compute budget

Not measured before commit #1. Per network: control about 20 runs of 7.5 to 21 s;
the main measurement 216 runs of 7.5 s. If the budget cannot be met, any
reduction (fewer seeds, fewer shifts, fewer subsample networks) is a disclosed
amendment made without looking at P0 to P3 quantities. Workers: 12 or fewer.

## Declared limits

- **Under-constrained weights.** The shipped weights come from one parameter
  set; the ensemble samples a box around it (x0.5 to x2); the data for most of
  these weights are not in the paper's abstract and not in this file.
  Medlock 2022's degeneracy result is a warning that many weight sets give the
  same normal function and different pathological ones. **The results are
  discriminating hypotheses, not verdicts about patients.**
- **What it cannot settle:** whether any patient has a KCC2/BDNF-type
  disinhibition (E-01 §5 says it is the dominant allodynia route in animal
  work, not that it is the mechanism in any person with CRPS); the size of
  any real E_anion shift (the abstract gives none and the grid is in model
  millivolts, not a measurement); anything about stimulation settings,
  amplitudes, charge, lead position or time courses in weeks (the model is
  acute, seconds long, with synthetic spike trains); one projection-neuron type
  (WDR) and a four-cell circuit, no PKCγ or SOM-neuron circuit (Duan 2014) and no
  receptive-field geometry; independent Poisson afferents; SCS modelled as
  synchronous Aβ pulses with no conduction failure, no collision with touch and
  no antidromic effects; the habituation variant is a gain change on the
  stimulating input and recovery off stimulation is definitional, so the model
  cannot separate habituation from lead drift, only from disinhibition; the
  lead-drift variants are two of many; the C reduction is thinning, not a
  frequency-dependent T-junction filter. Whether clinical-amplitude ganglion
  stimulation reaches Aβ fibres only (Graham 2019) or C-fibres too (Chao 2020,
  Kent 2018) is not tested; the Aβ recruitment is simply assumed.
- **The positive control is my operationalisation** of three qualitative
  claims. Passing it shows the Python re-implementation and driver behave like the
  starting model in those three respects and says nothing about whether the
  starting model is right about dorsal horns.
- **Wind-up and A-fibre inhibition** use the shipped input files; the paper's
  figure values were not consulted (full text not read), so "reproduced" means
  "the abstract's qualitative claims hold at my tolerances".
- **Nothing here is a stimulation setting or advice.** E_anion shifts are model
  millivolts, frequencies are those of a synthetic Aβ pulse train in a four-cell
  model. **These results are not stimulation settings.**

## Hand prediction summary, before running

| Quantity | My guess | Probability |
|---|---|---|
| Candidate 0 passes W, A and F | yes | 20% |
| 200 accepted in 1500, given candidate 0 passes | yes | 60% |
| P0: median onset in [10, 25] mV (guess 15) | supported | 55% |
| P1: 20 Hz SCS never reduces touch-evoked output (not supported, not refuted) | yes | 55% |
| P1b: best-frequency reduction >= 20% at 0 and < 20% by 25 or 40 mV | yes | 60% |
| P2: reduced C does not reduce touch-evoked-on-background output after collapse | supported | 50% |
| P3: signature separates disinhibition from H, D1, D2 | supported | 35% |
| G3 convergence passes | yes | 70% |

About 20% x 60% x 70% = **8%** that every gate holds and P0 to P3 are read as
verdicts; the likeliest single outcome (about 80%) is NO VERDICT at the control,
with candidate 0's three control numbers reported.

---

## Appendix A: prior-art search, verbatim

Run 2026-11-17. PubMed: NCBI E-utilities `esearch` (db=pubmed, retmax 40) then
`esummary`; the query string is the `term` exactly as written. Hits are PMID,
first author, year, journal, title (long titles shortened with "..."). A hit
list is **screened by title only**; the abstracts of the hits marked [read]
were fetched with `efetch` and read.

### A.1 PubMed queries

1. `dorsal horn model disinhibition allodynia spinal cord stimulation`: 4 hits.
   41735055 Medlock 2026 J Neurosci, Spinal Processing of Spatiotemporally
   Diverse Tactile Stimuli: Computational Insights into Allodynia and Spinal Cord
   Stimulation [read]; 25932687 Werdehausen 2015 Pain (N-ethylglycine, not a
   model); 23692698 Franca 2013 Behav Brain Res (motor cortex stimulation, not a
   model); 11793144 Mense 2001 Schmerz (low back pain review, not a model).
2. `computational model dorsal horn KCC2 chloride allodynia`: 0 hits.
3. `dorsal root ganglion stimulation computational model dorsal horn`: 2 hits.
   31295266 Crodelle 2019 PLoS Comput Biol (Modeling the daily rhythm of human
   pain processing in the dorsal horn); 30981900 Graham 2019 Clin Neurophysiol
   (DRG stimulation modulates Aβ-fiber but not C-fiber activity).
4. `dorsal horn network model Abeta input projection neuron disinhibition`: 0 hits.
5. `spinal cord stimulation model wide dynamic range neuron anion reversal
   potential`: 2 hits. 26934510 Medrano 2016 Pain (loss of inhibitory tone in
   a mouse model, not a computational model); 24790169 Zhang 2014 J
   Neurophysiol [read; the starting model].
6. `computational model spinal dorsal horn circuit chronic pain`: 9 hits.
   39808669 Ginsberg 2025 PLoS Comput Biol (E-I balance, allodynia subcircuits)
   [read]; 35232767 Medlock 2022 J Neurosci [read]; 34867259 Kearns 2021 Front
   Synaptic Neurosci (opioid-induced hyperalgesia mouse, not a model); 31946365
   Beauchene 2019 IEEE EMBC (Modeling Responses to Peripheral Nerve Stimulation
   in the Dorsal Horn); 25972582 Zhang 2015 J Neurophysiol [read]; 24802658 Zhang
   2014 Brain Res (Mechanisms and models of SCS, review); 24790169 Zhang 2014
   [read]; 24750347 Arle 2014 Neuromodulation (Mechanism of dorsal column
   stimulation... analysis with a computational model); 22780956 Smits 2013 Pain
   Pract (review).
7. `spinal cord stimulation computational model dorsal horn network`: 11 hits.
   41735055 Medlock 2026 [read]; 39819320 Metzger 2025 (clinical outcomes);
   38744531 Rogers 2024 J Neurosci (Biophysics of Frequency-Dependent Variation in
   Paresthesia and Pain Relief during SCS) [read]; 37727912 Gilbert 2023 J
   Neurophysiol (Network model of nociceptive processing in the superficial
   spinal dorsal horn... hyperalgesia, allodynia, and SCS) [read]; 35918052
   Gilbert 2022 Brain Stimul (Evaluating optimized temporal patterns of SCS);
   31946365 Beauchene 2019; 31792247 Jabbari 2019 Sci Rep (bladder pressure, not
   relevant); 28700536 Samineni 2017 Pain (spinal optogenetics devices, not a
   model); 26335379 Khan 2015 (fMRI, not a model); 24790169 Zhang 2014; 20668279
   Le Franc 2010 J Neurophysiol (deep dorsal horn firing patterns, single-neuron).
8. `dorsal horn microcircuit simulation touch-evoked pain mechanical allodynia`: 0 hits.
9. `KCC2 BDNF disinhibition lamina I neuron model simulation`: 0 hits.
10. `gate control theory computational model spinal cord stimulation`: 5 hits.
    42300150 Lambert 2026 Pain (dual-frequency SCS, clinical); 40183725 Zannou
    2025 Neuromodulation (Computational Optimization of SCS for Dorsal Horn
    Interneuron Polarization); 28368982 Vallejo 2017 Spine (review); 25972582
    Zhang 2015; 24750347 Arle 2014.
11. `dorsal root ganglion stimulation mechanism allodynia model spinal`: 166 hits,
    40 listed and screened by title; none is a dorsal-horn computational model
    (they are rodent mechanism, immunology and acupuncture papers) except 32658148
    Chao 2020 Pain (DRG field stimulation, already in the evidence base; an
    afferent-conduction study, not a dorsal-horn model).
12. `spinal cord stimulation frequency dorsal horn computational model projection
    neuron`: 3 hits. 37727912 Gilbert 2023; 25972582 Zhang 2015; 24790169 Zhang 2014.
13. `dorsal root ganglion stimulation computational model Abeta fibres C fibres`:
    1 hit. 30981900 Graham 2019.
14. `KCC2 computational model spinal cord disinhibition`: 0 hits.
15. `dorsal horn model habituation spinal cord stimulation`: 0 hits.
16. `computational model spinal cord stimulation loss of efficacy over time`: 3
    hits. 42300150 Lambert 2026; 37727912 Gilbert 2023; 24790169 Zhang 2014.
17. `Sagalajev synchrony sensation paresthesia-free spinal cord stimulation`: 0
    hits (the paper behind ModelDB 267768 was not found by this phrasing; known
    by title only).
18. `Delrocq ASIC1a synaptic cleft pH wind-up wide dynamic range`: 0 hits (ModelDB
    267666 known by title only).

### A.2 ModelDB

ModelDB's own search is not scriptable and its API took about 35 s per request
on the day, so a keyword scan of the whole index (every model's notes) was
**started and abandoned**: it did not finish. It is not a negative result. The
substitute was the search of the public GitHub mirror `ModelDBRepository`
(GitHub API `search/repositories`, query string `<term> org:ModelDBRepository
in:name,description`, which covers **model names and one-line descriptions
only**, not the notes), 2026-11-17:

| Term | Hits |
|---|---|
| `dorsal horn` | 168414 Zhang et al 2014; 267056 Medlock et al 2022; 256628 Balachandar & Prescott 2018 (spiking patterns of single neurons); 267614 Ma et al 2023 (parvalbumin interneuron HH model) |
| `spinal cord stimulation` | 168414; 267768 Sagalajev et al 2024 (role of synchrony, paresthesia-free SCS) |
| `allodynia` | 0 |
| `disinhibition` | 0 |
| `KCC2` | 0 |
| `wide dynamic range` | 267666 Delrocq (ASIC1a and synaptic cleft pH modulating wind-up in WDR neurons) |
| `gate control` | 0 |
| `nociceptive` | 266782 Suleimanova 2020 (meningeal neuro-immune synapse, not spinal) |
| `spinal dorsal` | the same four as `dorsal horn` |
| `neuropathic` | 0 |
| `dorsal root ganglion` | 51022 Amir & Devor 2003; 190261 Rho & Prescott 2012; 140038 Kovalsky 2009; 2018004 Farooqui 2024 (all single-neuron DRG models) |
| `projection neuron` | 12 striatal, subthalamic and olfactory models, none spinal |
| `chloride` | 206365 Buchin 2016 (subiculum); 148253 Jedlicka 2011 (GABA transmission with chloride accumulation, not spinal) |

### A.3 Does anything already answer the question?

**No single model found does**, on the evidence searched (abstracts and model
names; no full texts). Gilbert 2023, Zhang 2014 and Medlock 2026 each answer a
piece of Q1 to Q3 qualitatively (Aβ unmasked by disinhibition; frequency
optimum moved by a shifted anion reversal; kilohertz SCS recruiting inhibition),
and the pieces are recorded above. None of the abstracts reports the shift at
which Aβ input starts to drive the projection neuron across a weight ensemble,
a separate accounting of touch-evoked and C-driven output under both
manipulations, or the contrast of three causes of fading benefit. This is a
statement about what the **abstracts** say; a full-text reading could change it.
Models in ModelDB found only by name (Sagalajev 2024, Delrocq) were not read.

---

## Amendments (appended after commit #1; the text above is not edited)

### Amendment 1 (2026-11-18, after the main run): pilots, the main run's outcome, and what they say about the design

**Pilots and checks run before the main run, all disclosed.** Commit #2 (`43228b8`)
holds the code. Before the main run the following simulations were executed, none
of them under `results/main/`:

1. The wiring test `test_sites.py` runs one 12 ms simulation with one event, to check that
   `NetCon.event(t)` delivers at t (first non-zero conductance within 0.2 ms after t).
2. A timing script and two short diagnostic scripts (not committed; throw-away, scratch
   directory) ran the unmodified network on the pre-registered generators: a 7.5 s run took
   about 12.5 s of wall time at `dt` 0.025 ms; the network is silent with no input; with C
   input only, 4 s runs gave WDR spike counts of 0 (0.5 Hz per fibre), 2 (1 Hz) and 204 (2.5
   Hz), and touch only (20 Hz per fibre) gave 21 WDR spikes in 4 s. This is how the
   steepness of the response became known; it was **not** known when this file was written.
3. A forced-control pilot of the whole pipeline under `results/pilot/` (4 candidates, a C
   rate forced to 0.5 Hz per fibre, a reduced grid, `S2_PILOT=1`). Its first attempt hung
   (cause inferred, not proven: a second network built in a live worker process, which crashed
   the worker and left the pool waiting; the change in `6374d81` gives one network per process
   and the hang did not recur); the second ran to completion in about 8 minutes
   including the aggregator. **Nothing from it is a result**; it showed the pipeline runs
   end to end and that its report refuses to call itself a result when the control is forced.
4. `diag_candidate0.py` (commits `d03458e`, `992343f` and `d8ce9e3`; the last two came after the main run started and change only that script), a diagnostic of
   candidate 0 only, seed 1, one 6 s window per cell; its numbers are in
   `results/main/pilot-diag-candidate0.json`. One run of the diagnostic with
   `multiprocessing.Pool` hung with idle workers (cause not established; a dead worker is the
   likely reason, and the pool does not report one); it was replaced by
   `ProcessPoolExecutor` for the diagnostic. **The main driver still uses
   `multiprocessing.Pool`**, with one network per process, and could hang in the same way if
   a worker is killed; this did not occur in the main run.

**What the diagnostics show** (candidate 0, one seed, WDR Hz; from the JSON above):

- C-only rate against C rate (Hz per fibre): 0.25 gives 0.0, 0.5 gives 0.0, 1.0 gives 2.0,
  1.5 gives 17.5, 2.0 gives 55.5, 2.5 gives 78.3, 5.0 gives 112.2, 10.0 gives 122.5. The
  pre-registered drive-matching set {2.5, 5, 10, 20} therefore **cannot** reach the band
  [2, 15] Hz for this model (the lowest set value already gives 78 Hz), so feature F's
  clause (i) fails by construction; that is a design error in this file, not a property
  of the model.
- Touch-only rate at 10 Hz per Aβ fibre by shift (0, 10, 20, 30, 40 mV): 3.2, 28.7, 103.5,
  143.2, 167.2; at 20 Hz per fibre: 4.5, 67.2, 139.7, 177.0, 201.3. For candidate 0 the
  onset of "touch drives the projection neuron by >= 1 Hz" lies between 0 and 10 mV, i.e.
  **below** the pre-registered P0 interval [10, 25] mV. P0 as written looks wrong for
  candidate 0; whether it is wrong for an ensemble is not known.
- SCS as pre-registered (all 15 Aβ fibres firing synchronously) with a C background gives a
  WDR rate that rises with SCS frequency at every frequency tried (C background 1.0 Hz per
  fibre, no-SCS rate 2.0 Hz: 14.2, 20.0, 31.7, 30.0, 52.5, 93.0, 138.8, 209.8, 234.7 Hz at 5,
  10, 20, 30, 40, 60, 100, 150, 200 Hz; the 1.5 Hz background is similar). There is **no**
  30 to 100 Hz inhibitory window in this driver. The published effect is therefore **not**
  reproduced by my SCS driver and shipped weights; the likeliest reasons are the driver
  (the authors' recruitment pattern is not in the abstract; mine recruits all 15 fibres
  every pulse) and the shipped weights; I cannot tell which from the abstract.

**The main run, as pre-registered, unchanged.** Started 2026-11-17 23:58:48 CET from commit
`6374d81`, `python simulate_s002.py --workers 12`. Candidate 0 failed feature A at both
`dt` (G1 failed): wind-up passed (mean 20.6 to 37.2 WDR spikes per stimulus at 0.025 ms,
20.8 to 38.2 at 0.0125 ms) and A-fibre inhibition **failed** (with A-fibre events 19.4 against
11.3 spikes per cycle without at 0.025 ms; 15.8 against 11.2 at 0.0125 ms: the A fibres
add spikes rather than remove them, and the two `dt` values differ for the with-A figure).
Per the rules above the result is **NO VERDICT** for P0 to P3 and nothing beyond the
control record, the labelled visual traces of candidate 0 (control not passed) and the
report was produced. The control stops at the first failing feature, so the drive match and
F were not evaluated in the main run; the diagnostics above are their only (pilot)
evidence.

**Reporting change after the run, display only:** one explanatory paragraph under the
control table in `aggregate_s002.py`; results.md was regenerated from the same files; no
measured number changed.

**What this does not establish.** It does not show the published model is wrong or that the
Zhang 2014 results are not reproducible: my A and F operationalisations are my own and the
full text (figures, methods) was not read. A successor study would need, at least, (a) a drive
match grid that reaches the model's steep range (about 0.5 to 2 Hz per fibre), (b) the paper's
own SCS and A-fibre protocols from the full text instead of my synchronous-all-fibres driver
and whole-cycle spike counts, and (c) a fresh pre-registration, since the numbers above were
seen. It would not be a continuation of this registration.
