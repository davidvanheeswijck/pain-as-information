# S-1 results: DRG T-junction, rate versus pattern

**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.

Verdict logic: local rule (PREDICTION.md) (`simulations/verdict.py` exists on main and gives a t-interval of a mean against one threshold; it has no proportion/Wilson rule and no composite P1/P2 logic, so it is not used here and the local rule stays; `aggregate_s001.py` could cross-check the mean-difference cells with it). Pre-registration: `PREDICTION.md` (commit #1); amendments are listed in `PREDICTION.md` under 'Amendments made in the results commit'.

## Verdicts

| Item | Verdict |
|---|---|
| Positive control | **FAIL** |
| P1 pattern is approximately rate | **NO VERDICT (positive control failed)** |
| P2 no human ordering | **NO VERDICT (positive control failed)** |

Population: 200 accepted C-neuron variants; 30 in the stochastic subsample; 30 Aβ comparators.
Acceptance: 200/644 candidates (31%; 401 were in range, 201 of those were dropped because no stimulus up to 12x the from-rest threshold drove 90% of 20 Hz pulses), following frequency 2.0-40.0 Hz, median 11.6 Hz; 122 in the tight 2-15 Hz cut.

## Positive control

| Configuration | Sundt 2015 | Band (±25%) | Model | dt/2 check | Pass |
|---|---|---|---|---|---|
| Na + Kdr | 110 Hz | 82.5-137.5 | 89.1 Hz | 89.091 Hz | yes |
| + KCNQ/M | 30 Hz | 22.5-37.5 | 32.1 Hz | 35.982 Hz | yes |
| + Ca-dependent K | 6 Hz | 4.5-7.5 | 6.6 Hz | 6.574 Hz | yes |
| SK removed (mutation) | must leave 4.5-7.5 Hz | | 32.1 Hz | | control correctly fails |

Chao 2020 qualitative control at regular 20 Hz, 1.5x:

- (a) block defined within 20 s in 1.000 of models (need ≥0.5): pass; median time-to-block 573.782 ms
- (b) median F(late) - F(early) = 0.000 (need ≥0.20): FAIL
- (c) Aβ F = 0.005 [0.001, 0.011] (need CI upper < 0.05): pass

## F by regular rate (probe-only baseline: 0.000)

| Rate | Amp | F mean | 95% CI | n | median fraction of pulses evoking a spike |
|---|---|---|---|---|---|
| 4 Hz | 1.0x | 0.995 | [0.994, 0.996] | 200 | 1.000 |
| 20 Hz | 1.0x | 0.965 | [0.962, 0.969] | 200 | 0.957 |
| 40 Hz | 1.0x | 0.790 | [0.777, 0.802] | 200 | 0.021 |
| 60 Hz | 1.0x | 0.464 | [0.451, 0.477] | 200 | 0.009 |
| 80 Hz | 1.0x | 0.432 | [0.418, 0.446] | 200 | 0.007 |
| 4 Hz | 1.5x | 0.995 | [0.994, 0.996] | 200 | 1.000 |
| 20 Hz | 1.5x | 0.962 | [0.958, 0.966] | 200 | 0.953 |
| 40 Hz | 1.5x | 0.754 | [0.741, 0.767] | 200 | 0.013 |
| 60 Hz | 1.5x | 0.454 | [0.441, 0.467] | 200 | 0.008 |
| 80 Hz | 1.5x | 0.430 | [0.416, 0.443] | 200 | 0.004 |

## P1: pattern versus rate (difference from regular 20 Hz, matched pulse count)

| Pattern | Amp | n | within 10 pts | Wilson 95% | mean diff | 95% CI |
|---|---|---|---|---|---|---|
| poisson | 1.0x | 30 | 1.000 | [0.886, 1.000] | -0.009 | [-0.020, 0.003] |
| poisson | 1.5x | 30 | 0.967 | [0.833, 0.994] | -0.007 | [-0.021, 0.008] |
| burst | 1.0x | 200 | 0.980 | [0.950, 0.992] | 0.027 | [0.024, 0.031] |
| burst | 1.5x | 200 | 0.975 | [0.943, 0.989] | 0.030 | [0.026, 0.035] |
| jitter | 1.0x | 30 | 1.000 | [0.886, 1.000] | -0.024 | [-0.036, -0.012] |
| jitter | 1.5x | 30 | 1.000 | [0.886, 1.000] | -0.023 | [-0.036, -0.008] |

P1 if the control passes: **SUPPORTED**.

## P2: F(80 Hz) versus F(20 Hz)

| Amp | n | F20 | F80 | F80≥F20 (1-pt tol) | Wilson 95% | literal | models with ≥20% relative fall | Wilson 95% | evoked frac 20 / 80 Hz |
|---|---|---|---|---|---|---|---|---|---|
| 1.0x | 200 | 0.965 | 0.432 | 0.000 | [0.000, 0.019] | 0.000 | 1.000 (of 200) | [0.981, 1.000] | 0.957 / 0.007 |
| 1.5x | 200 | 0.962 | 0.430 | 0.000 | [0.000, 0.019] | 0.000 | 1.000 (of 200) | [0.981, 1.000] | 0.953 / 0.004 |

P2 if the control passes: **REFUTED**.

## Diagnostics (not pre-registered thresholds)

- Drive-matched 80 Hz, post hoc: **unavailable.** The search tries multiples of the from-rest threshold up to 12x and accepts the first at which at least 90% of the late pulses of a 4 s regular 80 Hz train evoke a stem spike. It found none in 30/30 subsample models, so no 'drive-matched' run exists (the earlier 'n/a' was this, not a missing stage). Within a 12x amplitude range the stem cannot be driven at 80 Hz in these models; that is itself the lost-drive result, and is why P2 cannot be read as filtering.
- Pre-registered 10 Hz test train, subsample: F(none)=0.012, F(20 Hz)=0.964, F(80 Hz)=0.427, F(burst)=0.995, F(Poisson)=0.950, F(jitter)=0.929; F(80)-F(20) = -0.537 [-0.558, -0.517].
- 5 Hz test train: F(none)=0.002, F(20 Hz)=0.964, F(80 Hz)=0.426.
- dt-halving (0.025 vs 0.0125 ms), 10 models: median |dF| = 0.000, max 0.111; pass.

## What this run shows

Nothing here rescues the verdicts: the positive control failed on Chao criterion (b), so P1 and P2 are **NO VERDICT** as pre-registered. The conditional readings above are shown only so that the reasons are visible.

**(a) The model does not reproduce a progressive block.** Block is almost complete from the start at every rate of 4 Hz and above (F = 0.995 at 4 Hz, 0.96 at 20 Hz), with a median time-to-block of about 0.6 s, against Chao's block developing over about 20 s. The probe-only baseline is F = 0.000, so the block is caused by the stimulation, not by the 2 Hz probe, which makes the probe choice an unlikely culprit. At 4 Hz every pulse evokes a spike, so the threshold definition is not the culprit either. The most likely cause is the tuning amendment (A in `PREDICTION.md`): Ca decay of 1500 ms and the SK conductance were tuned so that a 21-pulse train fails above 6 Hz (Sundt), and a Ca-dependent K current that strong and that fast accumulates in under a second at 4 Hz plus probes. This is a hypothesis; it was not tested by re-tuning, which would need a new pre-registration.

**(b) Under that model, matched-rate patterns are indistinguishable from rate.** Poisson, burst and jitter are all within 3 points of regular 20 Hz (the largest mean difference is burst, +0.030, CI [0.026, 0.035]), and at least 96% of models are within 10 points in every cell. Because F is already near 1 at 20 Hz there is little room for a pattern to raise it, so this is also a ceiling effect: it is weak evidence that pattern does not matter and cannot show that pattern would not matter in a model that blocks progressively.

**(c) High rates lower F only by failing to drive the stem.** At 40 Hz and above 0.4-2% of pulses evoke a spike (median), against 95% at 20 Hz, and no amplitude up to 12x found a drive at 80 Hz. F falls from 0.96 to 0.43 because the stimulus stops generating spikes, not because the T-junction passes more. The 10 Hz and 5 Hz test trains on the subsample show the same ordering (F(80)-F(20) = -0.54).

**What the next model would have to do differently** to make the control passable: reproduce Sundt's 6 Hz following frequency *and* a block that builds over tens of seconds, which a single Ca-dependent K time constant evidently cannot do here, and keep the stem drivable at 80 Hz (for example by a stimulus that does not depend on the same channels the filter depends on). A rival mechanism exists: Ladez, Liu, Chen and Feng (EMBC 2024, PMID 40039770, NEURON, Markov Nav models incl. Nav1.6) report that DRG stimulation raises intra-axonal Na and lowers K, disrupting the transaxonal gradients, giving activity-dependent conduction slowing and eventual block in both Aδ and C fibres. That would give a slow progressive block of the kind Chao saw and is worth a **separate pre-registered run**; it is not built here.

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
| reg80@1.5 | 0.019 | [0.001, 0.040] |
| burst@1.5 | 0.002 | [0.000, 0.005] |
| poisson@1.5 | 0.002 | [0.000, 0.006] |
| jitter@1.5 | 0.003 | [0.001, 0.006] |

