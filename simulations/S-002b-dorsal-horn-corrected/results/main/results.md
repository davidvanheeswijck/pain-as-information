These results are not stimulation settings.

# S-2b results: corrected dorsal-horn run

Every number below is generated from the data files in this directory. Model units: E_anion shifts are in model millivolts, frequencies are those of a synthetic pulse train in a four-cell model, rates are model WDR spikes per second. Pre-registration: `PREDICTION.md` (commit #1 of the branch).

## Gates

| Gate | Result |
|---|---|
| G6 oracle equivalence | passed |
| G1 calibration at candidate 0 | passed |
| G2 ensemble of 200 accepted | passed |
| G3 dt-halving convergence | passed |
| G4 wiring and protocol tests | passed |
| G5 held-out frequency feature at candidate 0 (gates P1, P3) | FAILED |

For P0 and P2: all of G1-G4 and G6 hold. For P1 and P3: G5 does not hold or an earlier gate failed.

## The control

### Candidate 0 (the unmodified shipped model)

| dt (ms) | W early / late (spikes per stimulus) | W | C only | C+Abeta | C+Adelta | C+all A | ratio Abeta | ratio Adelta | r_C (Hz per fibre) | C-only rate at r_C (Hz) | A-beta | F |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.025 | 20.6 / 37.2 | pass | 11.3 | 8.0 | 23.3 | 19.4 | 0.71 | 2.06 | 1.0 | 2.12 | pass | fail |
| 0.0125 | 20.8 / 38.2 | pass | 11.2 | 7.0 | 23.2 | 15.8 | 0.62 | 2.07 | 1.0 | 2.25 | pass | fail |

Spikes per cycle (A control) in the first 10 cycles of the shipped input.

### Port against the original hoc network (oracle)

The original ModelDB 168414 hoc network was executed by NEURON (`crosscheck_original_hoc.py`, NEURON 9.0.2); the port is `dh_model.py`. Spikes per cycle, mean of 10 cycles.

| dt (ms) | condition | original (hoc) | port (candidate 0) | reviewer's table |
|---|---|---|---|---|
| 0.025 | C_only | 11.3 | 11.3 | 11.3 |
| 0.025 | C_abeta | 8.0 | 8.0 | 8.0 |
| 0.025 | C_adelta | 23.3 | 23.3 | 23.3 |
| 0.025 | C_all_A | 19.4 | 19.4 | 19.4 |
| 0.0125 | C_only | 11.2 | 11.2 |  |
| 0.0125 | C_abeta | 7.0 | 7.0 |  |
| 0.0125 | C_adelta | 23.2 | 23.2 |  |
| 0.0125 | C_all_A | 15.8 | 15.8 |  |

All 17 mechanism files are identical to the originals after CRLF normalisation: True. Archive sha256 matches PROVENANCE.md: True.

### Ensemble funnel

Candidates considered (index order, candidate 0 included): 1441. Rejected: 1240 (at W: 600; at A-beta: 631; at the drive match: 9). Passed all calibration features: 201 (candidate 0 plus 200 of the others). Kept: 200, the target being 200; 1 candidate(s) that passed in the last batch were dropped by the cap. Accounting: 1441 considered = 1240 rejected + 201 passed.

## Verdicts

Networks measured: 200. Intervals are bootstrap 95% CIs over networks (10000 resamples), or Wilson for proportions.

### P0 (Q1): onset of touch-evoked projection-neuron output

Median onset shift 12.5 mV, CI [10.0, 15.0]; 100% of networks have an onset on the grid (onset = first shift at which R_T rises 2.0 Hz above its value at 0). Threshold: median at most 10.0 mV. Registered rule: SUPPORTED iff the CI upper bound is at most 10.0; REFUTED iff the CI lower bound is above 10.0; otherwise INCONCLUSIVE. The CI lower bound is 10.0 and the threshold is 10.0, so the lower bound equals the threshold. Resolution is limited by the shift grid, 0, 2.5, 5, 7.5, 10, 15, 20, 30 mV: onsets and the CI ends can only fall on grid values, and the median of an even-sized sample can fall between two of them. 100 of 200 networks have an onset at or below 10.0 mV, so the point estimate sits on the threshold. INCONCLUSIVE here is a discretisation outcome on the registered grid: a median that falls between two grid values cannot be placed on one side of the threshold. Verdict: **INCONCLUSIVE**.

### P1 (Q2a): stimulation on the surround input at 40 Hz, touch-evoked output

| shift (mV) | mean R_T (Hz) | mean R_TS (Hz) | red_S [CI] | class | red_C [CI] | class |
|---|---|---|---|---|---|---|
| 0 | 2.13 | 0.01 | 1.00 [0.99, 1.00] | R | 0.95 [0.94, 0.96] | R |
| 2.5 | 2.62 | 0.02 | 0.99 [0.98, 1.00] | R | 0.95 [0.94, 0.96] | R |
| 5 | 3.55 | 0.03 | 0.99 [0.98, 1.00] | R | 0.95 [0.94, 0.96] | R |
| 7.5 | 5.34 | 0.06 | 0.99 [0.97, 1.00] | R | 0.95 [0.94, 0.96] | R |
| 10 | 8.74 | 0.12 | 0.99 [0.97, 1.00] | R | 0.95 [0.94, 0.96] | R |
| 15 | 29.66 | 1.27 | 0.96 [0.93, 0.98] | R | 0.95 [0.94, 0.96] | R |
| 20 | 82.98 | 52.60 | 0.37 [0.33, 0.40] | R | 0.95 [0.94, 0.96] | R |
| 30 | 136.01 | 171.09 | -0.26 [-0.27, -0.24] | N | 0.95 [0.94, 0.96] | R |

red_S = 1 - mean(R_TS)/mean(R_T); red_C = 1 - mean(R_Ch)/mean(R_C1). Classes: R lower bound >= 0.2; N upper bound < 0.2; S spans 0.2; - undefined. Verdict: NO VERDICT (the conditional reading is under "Conditional readings, not verdicts" below).

### P2 (Q2b): reduced C input, touch-evoked output on background

| shift (mV) | mean R_C1 | mean R_TC | mean E | red_Ch [CI] | class |
|---|---|---|---|---|---|
| 0 | 4.54 | 3.03 | -1.52 | n/a [n/a, n/a] | - |
| 2.5 | 4.54 | 3.78 | -0.76 | n/a [n/a, n/a] | - |
| 5 | 4.54 | 5.18 | 0.64 | -5.30 [n/a, n/a] | - |
| 7.5 | 4.54 | 7.57 | 3.03 | -1.03 [-2.86, -0.55] | N |
| 10 | 4.54 | 12.15 | 7.61 | -0.31 [-0.52, -0.20] | N |
| 15 | 4.54 | 38.06 | 33.51 | 0.01 [-0.01, 0.02] | N |
| 20 | 4.54 | 89.95 | 85.41 | -0.01 [-0.01, -0.00] | N |
| 30 | 4.54 | 139.59 | 135.05 | -0.02 [-0.02, -0.02] | N |

Shifts considered (at or above the median onset 12.5 mV, E defined): [15, 20, 30]. Classes there: ['N', 'N', 'N']. Registered rule: SUPPORTED iff red_Ch is class N (upper bound below 0.2) at every considered shift, with at least two such shifts; REFUTED iff it is class R at every one; INCONCLUSIVE if re-classing spanning cells could decide it; otherwise NOT SUPPORTED, NOT REFUTED. Verdict: **SUPPORTED**.

**Diagnostic: the P2 test is not informative at these shifts.** red_Ch = 1 - mean(E_h)/mean(E). The largest reduction it could show is reached if halving C removed every influence of C on the total (R_TCh = R_T), which gives ceiling = 1 - (mean R_T - mean R_Ch)/mean E. Computed from the data:

| shift (mV) | ceiling of red_Ch | can reach class R (>= 0.2) | interaction TC - T - C1 (Hz) [CI] | total output reduction when C is halved, 1 - TCh/TC [CI] |
|---|---|---|---|---|
| 0 | n/a | no | -3.65 [-4.16, -3.13] | 0.17 [0.13, 0.21] |
| 2.5 | n/a | no | -3.38 [-3.92, -2.82] | 0.18 [0.14, 0.22] |
| 5 | -4.19 | no | -2.91 [-3.50, -2.31] | 0.18 [0.15, 0.22] |
| 7.5 | -0.69 | no | -2.31 [-2.97, -1.65] | 0.16 [0.14, 0.19] |
| 10 | -0.12 | no | -1.12 [-1.84, -0.40] | 0.16 [0.14, 0.18] |
| 15 | 0.12 | no | 3.85 [2.89, 4.85] | 0.12 [0.11, 0.13] |
| 20 | 0.03 | no | 2.43 [1.74, 3.11] | 0.04 [0.04, 0.04] |
| 30 | -0.01 | no | -0.96 [-1.49, -0.45] | 0.01 [0.01, 0.01] |

At the considered shifts [15, 20, 30] mV the ceiling is 0.12, 0.03, -0.01, so the registered rule **could not have returned REFUTED** there. The verdict word above is what the registered rule produces, and it is therefore **not informative** about whether touch-evoked output is independent of C input: E is almost the touch-only rate, and red_Ch is near 0 whenever C adds roughly additively. The informative quantity is the interaction (table), and total output does fall when C is halved: 12% at 15 mV, 4% at 20 mV, 1% at 30 mV.

In plain terms: at the shifts where touch drives the projection neuron, the excess over C alone (E) is nearly the touch-only rate, so removing half of the C input barely changes E; that is why red_Ch is about 0.01, -0.01, -0.02 there. It does not show that touch-evoked output is independent of C input: the total output (touch plus C) is lower when C is halved, by the percentages above, and the interaction is small relative to the touch-only rate. This is a property of this four-cell model, not a finding about people. No positive control was registered for red_Ch (PREDICTION.md Amendment 3). Cells below the registered read window, at 7.5 and 10 mV, give red_Ch of -1.03, -0.31; they are outside the rule and are not part of the verdict.

### P3 (Q3): which observable change separates the three causes

Sweep subsample: 40 networks. Networks showing the full signature (selective loss and a moved optimum) among the evaluable ones:

| change | full signature k/n | Wilson 95% | selective loss k/n | optimum moves k/n |
|---|---|---|---|---|
| progressive disinhibition (5 to 15 mV) | 1/15 | [0.01, 0.30] | 2/15 | 14/15 |
| habituation (H) | 0/15 | [0.00, 0.20] | 0/15 | 7/15 |
| lead drift D1 | 0/15 | [0.00, 0.20] | 0/15 | 10/15 |
| lead drift D2 | 7/15 | [0.25, 0.70] | 7/15 | 15/15 |

The rows are listed in a fixed order and no ordering of the changes is a finding: without a gated verdict the proportions are a descriptive table of a subsample.

Uniform-loss reading for H (|change in u| <= 0.10 and the optimum unchanged): 7 of 15 evaluable networks. Verdict: NO VERDICT (the conditional reading is under "Conditional readings, not verdicts" below).

No candidate observation is offered: P3 is not a gated SUPPORTED verdict.

## Conditional readings, not verdicts

These are what the registered rules would print if the gate that failed had held. They are not verdicts and no verdict word applies to them.

- p1, conditional reading, not a verdict: the registered rule applied to the surround-input stimulation data would read "supported" (classes of red_S: ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'N']; of red_C: ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']). The same driver fails the held-out frequency feature (R-F: 0 of 18 evaluable networks pass, and candidate 0 fails it at both dt), so the reduction it shows cannot be read as the published stimulation effect.
- p3, conditional reading, not a verdict: the registered rule applied to the sweep subsample would read "inconclusive". The same driver fails the held-out frequency feature (R-F: 0 of 18 evaluable networks pass, and candidate 0 fails it at both dt), so the reduction it shows cannot be read as the published stimulation effect.

## Registered readings (no verdict word)

- R-A, ratio to C only, C_abeta: median 0.66, IQR [0.55, 0.75], n = 200.
- R-A, ratio to C only, C_adelta: median 2.17, IQR [1.81, 2.91], n = 200.
- R-A, ratio to C only, C_all_A: median 1.37, IQR [1.06, 1.76], n = 200.
- R-A, share of accepted networks in which C plus A-delta exceeds C only: 200/200, Wilson [0.98, 1.00].
- R-F, held-out frequency feature on 60 accepted networks: evaluable 18, pass 0. Only 18 of 60 are evaluable because of the registered baseline rule: a network is evaluable only if its touch-plus-C rate without stimulation at shift 0 is at least 1.0 Hz (F_BASE_MIN), and 42 of 60 are below it (the tonic Abeta input inhibits the C-driven rate). Wilson 95% interval of the pass share: among the evaluable networks [0.00, 0.18]; among all 60 [0.00, 0.06].
- Median rho(f) over evaluable networks: 5 Hz 0.50; 10 Hz 0.14; 20 Hz 0.00; 30 Hz 0.00; 40 Hz 0.00; 60 Hz 0.00; 100 Hz 0.00; 150 Hz 0.00; 200 Hz 0.00.

## Convergence (dt halving)

10 networks at dt 0.025 and 0.0125 ms: median |dR| 0.00 Hz (limit 1.0); classifications flipped 0 of 30 (0%, limit 10%). G3: passed.

## Visual traces

`visual-traces.json` and `visual-traces.png`: one accepted network, WDR membrane potential at no shift and at a collapsed shift, touch alone and touch with stimulation on the surround input.

## Disclosures: checks and pilots run before the main run

The one unmodified-model response curve allowed before the pre-registration (candidate 0, shift 0, C input only; `results/prereg/response-curve.json`), used only to place the C-drive grid. WDR rate (Hz, mean of 2 seeds) against the rate per C fibre (Hz):

| rate per C fibre | 0.5 | 0.625 | 0.75 | 0.875 | 1.0 | 1.125 | 1.25 | 1.375 | 1.5 | 1.625 | 1.75 | 1.875 | 2.0 | 2.125 | 2.25 | 2.375 | 2.5 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| WDR rate | 0.1 | 0.4 | 0.8 | 0.9 | 2.1 | 3.5 | 7.5 | 13.5 | 22.9 | 30.8 | 38.5 | 42.4 | 50.5 | 56.8 | 64.4 | 66.6 | 73.0 |

A pipeline pilot with a smaller protocol ran under the gitignored `results/pilot/` after the code was committed; nothing from it is a result, and `PREDICTION.md` Amendments 1 and 3 record what was seen (Amendment 3 adds the P0 and P2 readings). The oracle (`results/oracle/original-hoc-crosscheck.json`) and the tests ran before the main run and are logged in `run.log`.

## Declared limits

See `PREDICTION.md`. The weights are under-constrained, so these outputs are discriminating hypotheses about a four-cell model and say nothing about any patient. The circuit has no descending (brainstem) input (`evidence/10-descending-modulation.md` §8.2). These results are not stimulation settings.
