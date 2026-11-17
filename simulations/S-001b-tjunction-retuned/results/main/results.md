# S-1b results: re-tuned T-junction model, rate versus pattern

**These results are not stimulation settings.** They describe an acute, simplified biophysical model and say nothing about any patient.

Pre-registration: `PREDICTION.md` (commit #1). Rules for P1 and P2 are S-1's, imported unchanged; they were not applied because the search found no set to apply them to.

## Verdicts

| Item | Result |
|---|---|
| Tuning | **No tuning of this model class within the declared space produces progressive block with Sundt following frequencies.** |
| P1 pattern is approximately rate | NOT RUN: no parameter set met the calibration targets |
| P2 no human ordering | NOT RUN: no parameter set met the calibration targets |

**What this found, and how far it reaches.** Of the 22 calibrated candidates (8 of 240 in round 1, 14 of 96 in round 2), 19 block in under 2 s; B1 (F in the first 5 s at most 0.50) holds in 0, B2 in 22 and B3 (onset 2 to 20 s) in 3. B1 fails because F in the first 5 s is above 0.50 in 22 candidates and because it is undefined (fewer than 3 scored probes) in 0. Of the 3 with onset between 2 and 20 s, 0 also meet B1. The nearest miss is candidate 1035 (J = 2.52): following frequencies 84.2 / 32.1 / 5.0 Hz, 3 of 3 inside their Sundt bands, onset 5.237 s, F in the first 5 s 0.750 (misses B1 by 0.25), failing B1. Best J is 4.119 in round 1 and 2.521 in round 2 (round 2, which is a local search around round-1 candidates, produced the best candidates, so J was still improving when the search stopped). The search stopped at its pre-registered budget, not at convergence. A block that builds progressively by the B1 to B3 definition was not found within this declared space and channel set. That points to a slower process, for example the ion-gradient run-down mechanism of Ladez, Liu, Chen and Feng (EMBC 2024, PMID 40039770), as a candidate for a next pre-registered run, alongside a longer or wider search of this space. This is a pointer, not a conclusion; nothing here tests that mechanism.

This statement is about the declared space and model class only (nine parameters, ranges in `PREDICTION.md`; Sundt-type channels). It is a search result, not an exhaustive scan: 336 sampled candidates, of which 22 reached the calibration run (the funnel is in the table below). Stimulus amplitude (fixed at 1.5x of the drive threshold), stimulus site (mid-stem) and the 20 Hz rate were not search dimensions. The following-frequency scan has about 6% resolution, so some candidates just outside a band might sit inside it on a finer scan: 55 candidates were stopped at the Na+Kdr or +KCNQ/M band with a following frequency within 6% beyond a band edge. It does not say that no model could do both, and it is not a result about patients.

## Tuning

Search space, method and selection criterion: `PREDICTION.md` ('Tuning search space'). Round 1: 240 Latin-hypercube candidates; round 2 ran (96 local candidates around candidates 95, 150, 186), because fewer than 3 round-1 candidates met the targets.

Calibration targets: Na+Kdr 82.5-137.5 Hz, +KCNQ/M 22.5-37.5 Hz, +Ca-dependent K 4.5-7.5 Hz (Sundt 2015); and, at regular 20 Hz, 1.5x, B1 F(first 5 s) <= 0.50, B2 F(last 10 s) >= 0.80, B3 block onset between 2 and 20 s after stimulation starts (Chao 2020).

| Stage of the funnel (all search candidates) | Rounds 1 + 2 | Round 1 | Round 2 |
|---|---|---|---|
| candidates | 336 | 240 | 96 |
| Na+Kdr following frequency in band | 210 | 141 | 69 |
| +KCNQ/M in band (of those that passed the first) | 37 | 16 | 21 |
| +SK following frequency in 2-40 Hz (calibration run attempted; undrivable ones are counted in the next rows) | 23 | 8 | 15 |
| of which in the 4.5-7.5 Hz band | 6 | 1 | 5 |
| undrivable (no calibration run) | 1 | 0 | 1 |
| calibration runs completed | 22 | 8 | 14 |
| B1 holds (of calibrated) | 0 | 0 | 0 |
| B2 holds | 22 | 8 | 14 |
| B3 holds (onset 2-20 s) | 3 | 0 | 3 |
| B1, B2 and B3 all hold, counting only the calibration-run candidates and ignoring whether their Sundt bands hold | 0 | 0 | 0 |
| **meet every calibration target** | 0 | 0 | 0 |

Among the 22 calibrated candidates: median F in the first 5 s = 1.000, median F in the last 10 s = 1.000; block onset is under 2 s in 19, between 2 and 20 s in 3, over 20 s in 0 and absent in 0; median onset where defined 0.345 s.

Best five calibrated candidates by J (calibration targets only; d = ln(ff/target)/ln(1.25) for the three following frequencies; the bands are ±25% linear, so the band edges are at d = +1.00 and d = -1.29, and the 'in Sundt bands' column states directly whether each following frequency is inside its band):

| id | J | ff Na+Kdr / +KCNQ / +SK (Hz) | d | in Sundt bands (Na+Kdr / +KCNQ / +SK) | F early / late | onset (s) | SK in stem | meets |
|---|---|---|---|---|---|---|---|---|
| 1035 | 2.521 | 84.2 / 32.1 / 5.0 | -1.20 / 0.31 / -0.86 | yes / yes / yes | 0.750 / 1.000 | 5.237 | True | no |
| 1068 | 2.741 | 89.1 / 36.0 / 5.0 | -0.94 / 0.81 / -0.86 | yes / yes / yes | 0.833 / 1.000 | 2.826 | True | no |
| 1081 | 3.252 | 89.1 / 34.0 / 7.0 | -0.94 / 0.56 / 0.66 | yes / yes / yes | 0.889 / 0.909 | 1.129 | True | no |
| 1065 | 3.788 | 84.2 / 36.0 / 5.5 | -1.20 / 0.81 / -0.35 | yes / yes / yes | 0.875 / 1.000 | 0.770 | True | no |
| 95 | 4.119 | 84.2 / 34.0 / 5.2 | -1.20 / 0.56 / -0.61 | yes / yes / yes | 1.000 / 0.929 | 0.334 | True | no |

**0 of 336 candidates met every calibration target; 0 set(s) selected** (selected sets must also reproduce the three bands at dt/2 and break the third band when SK is removed).

## Visual traces

`visual-traces.json` holds 30 s voltage traces (soma, T-junction, central axon) of the best-scoring calibrated candidate under no stimulation, regular 20 Hz, regular 80 Hz and burst, so that the failure can be inspected. It is labelled in the file as not meeting the calibration targets.

