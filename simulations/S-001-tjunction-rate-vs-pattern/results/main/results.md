# S-1 results: DRG T-junction, rate versus pattern

**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.

Verdict logic: local rule (PREDICTION.md) (`simulations/verdict.py` exists on main and gives a t-interval of a mean against one threshold; it has no proportion/Wilson rule and no composite P1/P2 logic, so it is not used here and the local rule stays; `aggregate_s001.py` could cross-check the mean-difference cells with it). Pre-registration: `PREDICTION.md` (commit #1); amendments are listed in `PREDICTION.md` under 'Amendments made in the results commit'.

## Run notes

The run was started at 08:01:37 and **resumed at 11:12:14** (2 start lines in `run.log`) after the process was killed (machine restart). The resume reused cached per-model files and did not recompute them: the last candidate file was written at 08:38 and the last det model file at 10:37, both before the resume; the control stage (not cached) was recomputed, and the later stages (stochastic, tests, Aβ, convergence, visual) were run in the resumed process, computing only files not already present. Results are deterministic given the per-model seeds.

## Verdicts

| Item | Verdict |
|---|---|
| Positive control | **FAIL** |
| P1 pattern is approximately rate | **NO VERDICT (positive control failed)** |
| P2 no human ordering | **NO VERDICT (positive control failed)** |

Population: 200 accepted C-neuron variants; 30 in the stochastic subsample; 30 Aβ comparators.
Acceptance: 200/320 candidates (62%; 200 were in range, 0 of those were dropped because no stimulus up to 12x the from-rest threshold drove 90% of 20 Hz pulses), following frequency 2.0-40.0 Hz, median 11.6 Hz; 114 in the tight 2-15 Hz cut.

## Positive control

| Configuration | Sundt 2015 | Band (±25%) | Model | dt/2 check | Pass |
|---|---|---|---|---|---|
| Na + Kdr | 110 Hz | 82.5-137.5 | 89.1 Hz | 89.091 Hz | yes |
| + KCNQ/M | 30 Hz | 22.5-37.5 | 32.1 Hz | 35.982 Hz | yes |
| + Ca-dependent K | 6 Hz | 4.5-7.5 | 6.6 Hz | 6.574 Hz | yes |
| SK removed (mutation) | must leave 4.5-7.5 Hz | | 32.1 Hz | | control correctly fails |

Chao 2020 qualitative control at regular 20 Hz, 1.5x:

- (a) block defined within 20 s in 1.000 of models (need ≥0.5): pass; median time-to-block 556.699 ms (vacuous: block is immediate)
- (b) median F(late) - F(early) = 0.000 (need ≥0.20): FAIL
- (c) Aβ F = 0.005 [0.001, 0.011] (need CI upper < 0.05): pass

## F by regular rate (probe-only baseline: mean 0.000, max over models 0.017)

F is computed on *scored* probes only: probes that reach the pre-junction site and are not ambiguous with a stimulus spike (see `PREDICTION.md`, amendment E). `F_all` counts every arrived probe and treats any central crossing in the window as success, so it is a lower bound on F that includes stimulus spikes. Where the scored fraction is small, F is a statement about the gaps between stimulus volleys.

| Rate | Amp | F mean | 95% CI | F_all mean | n models | mean probes (test / arrived / scored) | scored / test | median fraction of pulses evoking a spike |
|---|---|---|---|---|---|---|---|---|
| 4 Hz | 1.0x | 0.994 | [0.993, 0.996] | 0.981 | 200 | 59.0 / 57.6 / 56.3 | 0.954 | 1.000 |
| 20 Hz | 1.0x | 0.958 | [0.954, 0.962] | 0.881 | 200 | 59.0 / 51.4 / 44.2 | 0.749 | 0.960 |
| 40 Hz | 1.0x | 0.882 | [0.874, 0.891] | 0.727 | 200 | 59.0 / 44.0 / 29.9 | 0.506 | 0.946 |
| 60 Hz | 1.0x | 0.618 | [0.599, 0.637] | 0.480 | 200 | 59.0 / 36.9 / 14.4 | 0.245 | 0.938 |
| 80 Hz | 1.0x | 0.297 | [0.278, 0.316] | 0.466 | 200 | 59.0 / 29.0 / 11.1 | 0.189 | 0.933 |
| 4 Hz | 1.5x | 0.994 | [0.993, 0.996] | 0.982 | 200 | 59.0 / 57.6 / 56.3 | 0.954 | 1.000 |
| 20 Hz | 1.5x | 0.961 | [0.957, 0.965] | 0.878 | 200 | 59.0 / 51.1 / 43.5 | 0.737 | 0.997 |
| 40 Hz | 1.5x | 0.878 | [0.870, 0.887] | 0.714 | 200 | 59.0 / 43.3 / 28.1 | 0.476 | 0.989 |
| 60 Hz | 1.5x | 0.529 | [0.505, 0.553] | 0.449 | 200 | 59.0 / 35.6 / 11.2 | 0.189 | 0.979 |
| 80 Hz | 1.5x | 0.049 | [0.037, 0.062] | 0.429 | 200 | 59.0 / 27.4 / 8.0 | 0.136 | 0.974 |

## P1: pattern versus rate (difference from regular 20 Hz, matched pulse count)

| Pattern | Amp | n | within 10 pts | Wilson 95% | mean diff | 95% CI |
|---|---|---|---|---|---|---|
| poisson | 1.0x | 30 | 1.000 | [0.886, 1.000] | 0.003 | [-0.008, 0.016] |
| poisson | 1.5x | 30 | 1.000 | [0.886, 1.000] | 0.007 | [-0.003, 0.017] |
| burst | 1.0x | 200 | 0.960 | [0.923, 0.980] | 0.033 | [0.028, 0.037] |
| burst | 1.5x | 200 | 0.985 | [0.957, 0.995] | 0.032 | [0.028, 0.036] |
| jitter | 1.0x | 30 | 1.000 | [0.886, 1.000] | -0.004 | [-0.014, 0.008] |
| jitter | 1.5x | 30 | 1.000 | [0.886, 1.000] | -0.000 | [-0.010, 0.010] |

*Conditional reading, NOT a verdict (positive control failed): the rule applied to these numbers would give supported. See 'Conditional readings, NOT verdicts' below.*

## P2: F(80 Hz) versus F(20 Hz)

| Amp | n | F20 | F80 | F80≥F20 (1-pt tol) | Wilson 95% | literal | models with ≥20% relative fall | Wilson 95% | evoked frac 20 / 80 Hz |
|---|---|---|---|---|---|---|---|---|---|
| 1.0x | 200 | 0.958 | 0.297 | 0.000 | [0.000, 0.019] | 0.000 | 0.990 (of 200) | [0.964, 0.997] | 0.960 / 0.933 |
| 1.5x | 200 | 0.961 | 0.049 | 0.000 | [0.000, 0.019] | 0.000 | 1.000 (of 200) | [0.981, 1.000] | 0.997 / 0.974 |

*Conditional reading, NOT a verdict (positive control failed): the rule applied to these numbers would give refuted. See 'Conditional readings, NOT verdicts' below.*

## Diagnostics (not pre-registered thresholds)

- Drive-matched, post hoc: 80 Hz at 1.5x its own drive threshold (found in 30/30 models) gives F = 0.008 [0.000, 0.025] against regular 20 Hz F = 0.962 on the same subsample.
- Pre-registered 10 Hz test train, subsample: F(none)=0.011, F(20 Hz)=0.966, F(80 Hz)=0.043, F(burst)=0.994, F(Poisson)=0.970, F(jitter)=0.960; F(80)-F(20) = -0.923 [-0.940, -0.906].
- 5 Hz test train: F(none)=0.002, F(20 Hz)=0.967, F(80 Hz)=0.049.
- dt-halving (0.025 vs 0.0125 ms), 10 models: median |dF| = 0.000, max 0.071; 1/29 comparisons with |dF| > 0.05; classification flips: 1; FAIL, INCONCLUSIVE.

## What this run shows

Nothing here rescues the verdicts: the positive control failed, so P1 and P2 are **NO VERDICT** as pre-registered.

**(a) Time course.** F at 1.5x is 0.994 at 4 Hz, 0.961 at 20 Hz and 0.049 at 80 Hz; median time-to-block at regular 20 Hz is 556.699 ms; median F(late) - F(early) is 0.000. The probe-only baseline is F = 0.000 (max over models 0.017), so any block is caused by the stimulation, not by the 2 Hz probe. Criterion (a) (block within 20 s) is **vacuous** here: the block is essentially immediate, so passing it says nothing about Chao's *progressive* block. Criterion (b) (progression) fails, so this model does not reproduce a progressive block. Candidate causes, by what the data can say: the 2 Hz probe is not one (baseline above); the 'threshold' definition is not one if the evoked fraction at 4 Hz is about 1 (it is 1.000); the remaining candidate is the tuning amendment (A in `PREDICTION.md`: Ca decay and SK conductance set against Sundt's 6 Hz following frequency). That last point is a hypothesis; it was not tested by re-tuning, which would need a new pre-registration.

**(b) Pattern against rate, in this model.** The largest mean difference from regular 20 Hz across the six cells is 0.033, and the smallest proportion of models within 10 points is 0.960. F at regular 20 Hz is above 0.9, so there is little room for any pattern to raise it: this is partly a ceiling effect and is weak evidence about pattern in a model that blocks progressively. 

**(c) What high rates do.** At the junction-side stem site, the median fraction of pulses that evoke a spike is 0.997 at 20 Hz and 0.974 at 80 Hz (1.5x); F(80) = 0.049 against F(20) = 0.961. The stimulus keeps evoking spikes at 80 Hz, so the F change is not explained by lost drive. F(80 Hz) is computed on probes that cross between stimulus volleys: 8.030 of 59.000 probes per model are scored at 80 Hz (0.136) against 43.510 of 59.000 at 20 Hz (0.737), and F_all is 0.429 at 80 Hz against 0.878 at 20 Hz. So a low F(80) means "drive intact, and gap probes rarely fail", not "a high rate passes the junction". 

**Context, not a result.** A model that could pass this control would have to reproduce Sundt's 6 Hz following frequency *and* a block that builds over tens of seconds, and keep the stem drivable at the high rates. A rival mechanism exists: Ladez, Liu, Chen and Feng (EMBC 2024, PMID 40039770, NEURON, Markov Nav models) report that DRG stimulation raises intra-axonal Na and lowers K, disrupting transaxonal gradients, with activity-dependent conduction slowing and eventual block in Aδ and C fibres. That is worth a separate pre-registered run; it is not built here.

## Conditional readings, NOT verdicts (control failed)

Applying the pre-registered rules to these numbers anyway: P1 would read supported; P2 would read refuted. These are shown only so the reasons are visible. They carry no evidential weight because the model failed its own control.

**The dt-halving check also FAILED** (1 pattern-versus-rate classification flip(s) and 1 of 29 comparisons with |dF| > 0.05, max |dF| 0.071), so even the conditional readings above are not numerically converged in the time step. This further weakens them; it is not a rounding detail.

## Aβ comparator F

| Condition | mean F | 95% CI |
|---|---|---|
| reg4@1.0 | 0.000 | [0.000, 0.000] |
| reg20@1.0 | 0.001 | [0.000, 0.002] |
| reg40@1.0 | 0.005 | [0.001, 0.011] |
| reg60@1.0 | 0.006 | [0.000, 0.014] |
| reg80@1.0 | 0.004 | [0.000, 0.010] |
| burst@1.0 | 0.001 | [0.000, 0.004] |
| poisson@1.0 | 0.004 | [0.000, 0.008] |
| jitter@1.0 | 0.005 | [0.000, 0.013] |
| reg4@1.5 | 0.001 | [0.000, 0.003] |
| reg20@1.5 | 0.005 | [0.001, 0.011] |
| reg40@1.5 | 0.008 | [0.002, 0.016] |
| reg60@1.5 | 0.015 | [0.004, 0.030] |
| reg80@1.5 | 0.019 | [0.001, 0.039] |
| burst@1.5 | 0.002 | [0.000, 0.005] |
| poisson@1.5 | 0.002 | [0.000, 0.006] |
| jitter@1.5 | 0.003 | [0.001, 0.006] |

