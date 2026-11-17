# S-3 results: which observations separate the pain generator

Not medical advice; these are questions a treating team might consider, at population level.

This is a decision-analysis model. It gives no protocol, dose or device setting, and it says nothing about any individual. **No likelihood in it is fully sourced**: every range is elicited, some anchored on a number or a direction read from an abstract (table at the end). The intervals below measure Monte Carlo error and the spread across those elicited ranges. They do not measure whether the ranges are right.

Pre-registration: `PREDICTION.md` (commit #1). Run: 20 seeds of 200 draws, 4000 draws, seeds 20261117 to 20261136; code at commit `dc9713c`. Verdict rule: `simulations/verdict.py` `decide` on the per-seed proportions, with a pooled Wilson 95% interval beside it; INCONCLUSIVE unless both name the same side.

## Verdicts

| Claim | Statement | Proportion of draws | Wilson 95% | Per-seed mean [t 95%] | Threshold | Verdict |
|---|---|---|---|---|---|---|
| P1 | every single test is below 1 bit | 1.000 (4000/4000) | [0.999, 1.000] | 1.000 [1.000, 1.000] | 0.80 | **SUPPORTED** |
| P2 | the best pair includes T3 | 0.789 (3155/4000) | [0.776, 0.801] | 0.789 [0.775, 0.803] | 0.50 | **SUPPORTED** |
| P2b | the best pair includes a block (T1 or T2) | 0.990 (3961/4000) | [0.987, 0.993] | 0.990 [0.988, 0.992] | 0.70 | **SUPPORTED** |
| P3 | H1 against H3: pairwise Bayes error is at least 0.15 under every set of at most 3 tests | 0.964 (3855/4000) | [0.957, 0.969] | 0.964 [0.958, 0.969] | 0.80 | **SUPPORTED** |
| Kill | the best sequence of at most 3 tests, fixed or adaptive, reaches 1 bit (triggered when below 0.50) | 0.040 (159/4000) | [0.034, 0.046] | 0.040 [0.033, 0.046] | 0.50 | **TRIGGERED** |

**The kill is triggered.** In the median draw the best sequence of at most three observations yields 0.797 bits (central 95% of draws [0.568, 1.023]), against a prior uncertainty of 1.900 bits, and it reaches 1 bit in 0.040 of draws. Within this model and these ranges, the available clinical observations cannot localise the generator. That is a result, not a failure.

## Positive control

- Oracle test, uniform prior: 2.000000000 bits (need 2).
- Pure-noise test, uniform prior: 0.000000000 bits (need 0).
- Across all 4000 drawn priors (oracle equals the prior entropy; noise is 0; noise added to each test changes nothing; oracle added to each test returns the prior entropy): largest absolute error 5.29e-16 bits (tolerance 1e-09).
- Order of a fixed sequence: largest difference between orderings of the same set 2.22e-16 bits, checked on 100 draws.
- H1 and H3 rows identical under T1, T2 and T3 in every draw (C-009): yes.
- **Control: PASS.**

## Single tests

Information gain in bits. "Central 95%" is the 2.5th to 97.5th percentile across draws: the spread from the elicited ranges, not a confidence interval of a mean.

| Test | Median IG | Central 95% of draws | Mean [t 95% across seeds] | P(top single) | Mean rank | P(IG at least 1 bit) |
|---|---|---|---|---|---|---|
| T2 comparative block | 0.389 | [0.227, 0.568] | 0.392 [0.389, 0.395] | 0.819 | 1.19 | 0.000 |
| T1 single peripheral block | 0.309 | [0.176, 0.486] | 0.316 [0.313, 0.319] | 0.000 | 2.43 | 0.000 |
| T3 dilute anaesthetic at the ganglion | 0.256 | [0.106, 0.470] | 0.265 [0.262, 0.268] | 0.171 | 2.83 | 0.000 |
| T4 ganglion stimulation on/off | 0.156 | [0.055, 0.316] | 0.164 [0.162, 0.165] | 0.005 | 4.16 | 0.000 |
| T5 ultrasound or MR neurography | 0.134 | [0.050, 0.281] | 0.142 [0.140, 0.143] | 0.006 | 4.39 | 0.000 |

## Pairs (set A)

| Set | Median IG | Central 95% of draws | Mean [t 95% across seeds] | P(top) | Wilson 95% of P(top) | Mean rank | Rank counts, 1st to 9th | P(IG at least 1 bit) |
|---|---|---|---|---|---|---|---|---|
| T2+T3 | 0.635 | [0.408, 0.860] | 0.635 [0.632, 0.639] | 0.779 | [0.766, 0.791] | 1.35 | 3115 / 518 / 249 / 83 / 25 / 5 / 5 / 0 / 0 | 0.001 |
| T2+T4 | 0.534 | [0.322, 0.747] | 0.535 [0.532, 0.539] | 0.109 | [0.100, 0.119] | 3.33 | 437 / 776 / 1194 / 717 / 468 / 312 / 86 / 10 / 0 | 0.000 |
| T2+T5 | 0.511 | [0.330, 0.713] | 0.514 [0.511, 0.517] | 0.102 | [0.093, 0.112] | 3.82 | 408 / 537 / 804 / 888 / 629 / 457 / 253 / 24 / 0 | 0.000 |
| T3+T5 | 0.398 | [0.227, 0.612] | 0.403 [0.400, 0.407] | 0.008 | [0.005, 0.011] | 6.49 | 31 / 72 / 330 / 284 / 380 / 400 / 1092 / 985 / 426 | 0.000 |
| T3+T4 | 0.398 | [0.206, 0.618] | 0.403 [0.400, 0.406] | 0.002 | [0.001, 0.004] | 6.56 | 8 / 35 / 261 / 432 / 337 / 493 / 952 / 978 / 504 | 0.000 |
| T1+T3 | 0.559 | [0.349, 0.790] | 0.563 [0.560, 0.567] | 0.000 | [0.000, 0.001] | 3.14 | 1 / 1864 / 815 / 633 / 407 / 196 / 51 / 29 / 4 | 0.000 |
| T1+T4 | 0.460 | [0.270, 0.669] | 0.463 [0.460, 0.466] | 0.000 | [0.000, 0.001] | 5.63 | 0 / 86 / 201 / 639 / 1008 / 884 / 671 / 433 / 78 | 0.000 |
| T1+T5 | 0.436 | [0.272, 0.640] | 0.442 [0.439, 0.445] | 0.000 | [0.000, 0.001] | 6.11 | 0 / 112 / 140 / 309 / 721 / 1190 / 577 / 793 / 158 | 0.000 |
| T4+T5 | 0.290 | [0.150, 0.469] | 0.295 [0.293, 0.297] | 0.000 | [0.000, 0.001] | 8.56 | 0 / 0 / 6 / 15 / 25 / 63 / 313 / 748 / 2830 | 0.000 |

## Triples (set A)

| Set | Median IG | Central 95% of draws | Mean [t 95% across seeds] | P(top) | Wilson 95% of P(top) | Mean rank | Rank counts, 1st to 7th | P(IG at least 1 bit) |
|---|---|---|---|---|---|---|---|---|
| T2+T3+T5 | 0.752 | [0.527, 0.981] | 0.754 [0.750, 0.757] | 0.531 | [0.516, 0.546] | 1.72 | 2124 / 1133 / 534 / 145 / 61 / 3 / 0 | 0.019 |
| T2+T3+T4 | 0.745 | [0.490, 0.975] | 0.742 [0.739, 0.746] | 0.421 | [0.406, 0.436] | 2.00 | 1684 / 1238 / 684 / 224 / 147 / 23 / 0 | 0.014 |
| T2+T4+T5 | 0.647 | [0.431, 0.873] | 0.648 [0.645, 0.651] | 0.048 | [0.042, 0.055] | 4.12 | 191 / 416 / 696 / 739 / 1351 / 607 / 0 | 0.001 |
| T1+T3+T4 | 0.677 | [0.437, 0.907] | 0.676 [0.672, 0.679] | 0.000 | [0.000, 0.001] | 4.02 | 1 / 483 / 938 / 1296 / 684 / 486 / 112 | 0.003 |
| T1+T3+T5 | 0.682 | [0.469, 0.914] | 0.685 [0.682, 0.689] | 0.000 | [0.000, 0.001] | 3.74 | 0 / 709 / 1040 / 1229 / 662 / 320 / 40 | 0.002 |
| T1+T4+T5 | 0.577 | [0.376, 0.798] | 0.579 [0.576, 0.582] | 0.000 | [0.000, 0.001] | 5.98 | 0 / 18 / 73 / 269 / 505 / 1892 / 1243 | 0.000 |
| T3+T4+T5 | 0.526 | [0.331, 0.752] | 0.530 [0.526, 0.533] | 0.000 | [0.000, 0.001] | 6.43 | 0 / 3 / 35 / 98 / 590 / 669 / 2605 | 0.000 |

The pair most often on top is **T2+T3** (P(top) 0.779); the triple most often on top is **T2+T3+T5** (P(top) 0.531). All four of T2, T3, T4, T5 together: median 0.852 bits, central 95% [0.610, 1.083].

**Order.** Under the model's conditional independence a fixed sequence has the same information gain in any order (checked above), so the 18 ordered pairs and 42 ordered triples collapse onto the 9 and 7 sets in these tables. What order changes is what is known after the first step, which is the single-test table.

## Adaptive policies

| Policy | Median IG | Central 95% of draws |
|---|---|---|
| best single test | 0.401 | [0.256, 0.569] |
| best fixed pair | 0.644 | [0.434, 0.860] |
| adaptive depth 2 | 0.672 | [0.459, 0.890] |
| best fixed triple | 0.776 | [0.553, 0.997] |
| adaptive depth 3 | 0.797 | [0.568, 1.023] |
| at most 3, fixed or adaptive | 0.797 | [0.568, 1.023] |
| adaptive depth 3 minus best triple | 0.018 | [-0.000, 0.058] |

First test of the best depth-3 adaptive policy, share of draws: T2 0.977, T4 0.017, T3 0.006, T5 0.001, T1 0.000.

## Set B: without T3

T3 is a research procedure, so the same analysis is repeated without it. Secondary, no verdict.

| Set | Median IG | Central 95% of draws | P(top in set B) |
|---|---|---|---|
| T2+T4 | 0.534 | [0.322, 0.747] | 0.595 |
| T2+T5 | 0.511 | [0.330, 0.713] | 0.405 |
| T1+T4 | 0.460 | [0.270, 0.669] | 0.000 |
| T1+T5 | 0.436 | [0.272, 0.640] | 0.000 |
| T4+T5 | 0.290 | [0.150, 0.469] | 0.000 |
| T2+T4+T5 | 0.647 | [0.431, 0.873] | 1.000 |
| T1+T4+T5 | 0.577 | [0.376, 0.798] | 0.000 |

Best sequence of at most three without T3, fixed or adaptive: median 0.647 bits, central 95% [0.431, 0.873]; reaches 1 bit in 0.001 of draws.

## Which pairs of hypotheses are separated

Pairwise Bayes error: the error rate of the best possible reader told that the truth is one of the two. Median across draws. "No test" is the starting point (the smaller of the two renormalised priors). Classes as pre-registered: not separated at 0.15 or above with all four tests, partly separated from 0.05, separated below 0.05.

| Pair | No test | T1 | T2 | T3 | T4 | T5 | All of T2, T3, T4, T5 | Central 95%, all four | Class | Identical rows under | Equal priors, all four (post hoc) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| H1-H2 | 0.396 | 0.224 | 0.193 | 0.193 | 0.355 | 0.304 | 0.117 | [0.064, 0.181] | partly separated | none | 0.126 [0.074, 0.189] |
| H1-H3 | 0.392 | 0.392 | 0.392 | 0.392 | 0.334 | 0.254 | 0.234 | [0.144, 0.332] | not separated | T1, T2, T3 | 0.250 [0.160, 0.344] |
| H1-H4 | 0.361 | 0.145 | 0.106 | 0.355 | 0.256 | 0.253 | 0.080 | [0.043, 0.127] | partly separated | none | 0.087 [0.051, 0.133] |
| H2-H3 | 0.395 | 0.229 | 0.199 | 0.190 | 0.314 | 0.371 | 0.121 | [0.066, 0.186] | partly separated | none | 0.132 [0.077, 0.196] |
| H2-H4 | 0.374 | 0.351 | 0.343 | 0.136 | 0.230 | 0.357 | 0.101 | [0.052, 0.161] | partly separated | none | 0.110 [0.060, 0.169] |
| H3-H4 | 0.376 | 0.147 | 0.107 | 0.366 | 0.300 | 0.372 | 0.099 | [0.054, 0.151] | partly separated | none | 0.104 [0.060, 0.154] |

- **Not separated by anything available:** H1-H3.
- Partly separated: H1-H2, H1-H4, H2-H3, H2-H4, H3-H4.
- Separated: none.
- H1 against H3, the best any set of at most three tests does: median error 0.234, central 95% [0.144, 0.332].

**A weakness of the pre-registered measure, found in the pilot.** The pairwise error can never exceed the smaller of the two renormalised priors, so a lopsided prior draw gives a low error with no test at all: for H1 against H3 the no-test error is already below 0.15 in 0.011 of main draws and 0.309 of flat-prior draws. P3 is scored as pre-registered. The last column is a post hoc diagnostic, not a threshold: the same error with the pair's priors set equal (0.5 with no test). On that measure the best any set of at most three tests does for H1 against H3 is median 0.250, central 95% [0.160, 0.344], and it is at least 0.15 in 0.987 of draws (0.988 under the flat prior, where the likelihood ranges are the same).

Hypotheses: H1 peripheral focal lesion; H2 ganglion ectopia; H3 central amplification of normal input; H4 central, input-independent.

## Questions a treating team might consider, in the order the model ranks them

Ranked by median information gain of the single observation. These are questions, not steps. Risk, burden, cost and availability are not in the model, and information gain is not clinical value.

1. **T2, comparative block** (median 0.389 bits; in the top pair in 0.990 of draws). Does spontaneous pain depend on input from the limb, when the answer is checked against a second, controlled block rather than taken from one?
2. **T1, single peripheral block** (median 0.309 bits; in the top pair in 0.000 of draws). Does spontaneous pain depend on input from the limb at all? (A single block can ask this; it cannot say whether that input is abnormal.)
3. **T3, dilute anaesthetic at the ganglion** (median 0.256 bits; in the top pair in 0.789 of draws). Is the ganglion itself the source? (The only observation here aimed at that question; it is a research procedure, reported in one human series in another condition.)
4. **T4, ganglion stimulation on/off** (median 0.156 bits; in the top pair in 0.111 of draws). Where a ganglion stimulator is already present: do background pain and touch-evoked pain respond together or apart when it is on and off?
5. **T5, ultrasound or MR neurography** (median 0.134 bits; in the top pair in 0.110 of draws). Is there a focal nerve lesion on high-resolution imaging, knowing that a visible lesion need not be the generator and a missed one is common?

## Sensitivity: which elicited number moves the answer

Spearman rank correlation, across draws, between each drawn quantity and the information gain of the best fixed triple. The ten largest in absolute value.

| Quantity | Used by | Status | Spearman rho |
|---|---|---|---|
| prior H4 | all | elicited | +0.408 |
| e | T3 | anchored (direction) | +0.374 |
| a | T1, T2, T3 | anchored | +0.360 |
| d | T1, T2 | elicited | -0.257 |
| prior H3 | all | elicited | -0.225 |
| prior H1 | all | anchored | -0.223 |
| f3 | T3 | elicited | -0.218 |
| q1 | T5 | anchored | +0.206 |
| prior H2 | all | elicited | +0.168 |
| f | T1, T2 | anchored | -0.167 |

## Flat-prior ensemble (secondary, no verdict)

The same likelihood ranges with a Dirichlet(1, 1, 1, 1) prior, seeds 20262117 to 20262136.

| Quantity | Main ensemble | Flat prior |
|---|---|---|
| prior entropy, median bits | 1.900 | 1.611 |
| best single test, median bits | 0.401 | 0.386 |
| best pair, median bits | 0.644 | 0.594 |
| best triple, median bits | 0.776 | 0.694 |
| best of at most 3, fixed or adaptive, median bits | 0.797 | 0.707 |
| every single test below 1 bit, proportion | 1.000 | 1.000 |
| best pair includes T3, proportion | 0.789 | 0.703 |
| best pair includes a block, proportion | 0.990 | 0.970 |
| H1-H3 error at least 0.15 under every set, proportion | 0.964 | 0.636 |
| best of at most 3 reaches 1 bit, proportion | 0.040 | 0.015 |

## Prediction against result

| Quantity | Predicted by hand (PREDICTION.md) | Result (median) | |
|---|---|---|---|
| T2 | 0.35 to 0.45 | 0.389 | inside |
| T1 | 0.27 to 0.37 | 0.309 | inside |
| T3 | 0.20 to 0.30 | 0.256 | inside |
| T5 | 0.10 to 0.17 | 0.134 | inside |
| T4 | 0.07 to 0.15 | 0.156 | above |
| best pair | 0.55 to 0.70 | 0.644 | inside |
| best triple | 0.70 to 0.90 | 0.776 | inside |
| min H1-H3 error, sets of at most 3 | 0.20 to 0.27 | 0.234 | inside |
| H3-H4 error, all four tests | 0.09 to 0.14 | 0.099 | inside |
| adaptive depth 3 minus best triple | at most 0.05 | 0.018 | inside |
| unseparated pairs | H1-H3 only | H1-H3 | as predicted |
| pairs below 0.05 | none | none | as predicted |

| Claim | My stated probability | Verdict |
|---|---|---|
| P1 supported | 97% | SUPPORTED |
| P2 supported | 80% | SUPPORTED |
| P2b supported | 85% | SUPPORTED |
| P3 supported | 75% | SUPPORTED |
| Kill triggered | 80% | TRIGGERED |

Hand arithmetic at the midpoint of every range, redone by machine at the same point:

| Test | By hand | By machine |
|---|---|---|
| T1 | 0.32 | 0.317 |
| T2 | 0.40 | 0.397 |
| T3 | 0.26 | 0.260 |
| T4 | 0.11 | 0.120 |
| T5 | 0.13 | 0.131 |

At the midpoint the best pair is T2+T3 at 0.643 bits and the best triple is T2+T3+T5 at 0.757 bits.

## Likelihood parameters and their status

24 parameters: 4 anchored on a source, 20 elicited, none fully sourced. Each is drawn as lo + (hi - lo) x Beta(2, 2). Prior: Dirichlet(6, 5, 5, 4); the H1 mean is anchored on PMID 40211731 (26% and 33%), the rest is elicited.

| Parameter | Used by | Range | Status | Basis |
|---|---|---|---|---|
| a | T1, T2, T3 | 0.60 to 0.95 | anchored | PMID 24704366: abolished in all 14, none with CRPS |
| u | T1, T2, T3 | 0.30 to 0.70 | elicited |  |
| f | T1, T2 | 0.15 to 0.45 | anchored | PMID 29913995: about 30%, zygapophysial joint blocks; transferred |
| g | T1, T2 | 0.20 to 0.60 | elicited |  |
| d | T1, T2 | 0.00 to 0.50 | elicited |  |
| r | T2 | 0.20 to 0.60 | elicited | PMID 29913995 gives no number |
| s | T2 | 0.00 to 0.25 | elicited |  |
| e | T3 | 0.50 to 0.95 | anchored (direction) | PMID 24769187: phantom limb, no proportion |
| u3 | T3 | 0.30 to 0.70 | elicited |  |
| c | T3 | 0.00 to 0.30 | elicited |  |
| f3 | T3 | 0.05 to 0.35 | elicited | PMID 24769187: control injections ineffective, no number |
| g3 | T3 | 0.20 to 0.60 | elicited |  |
| s1 | T4 | 0.30 to 0.80 | elicited | direction from PMID 33990112, 32658148 (rat, one lineage) |
| s2 | T4 | 0.40 to 0.85 | elicited | same |
| s3 | T4 | 0.10 to 0.60 | elicited | same |
| s4 | T4 | 0.05 to 0.35 | elicited | same |
| v1 | T4 | 0.30 to 0.80 | elicited | same |
| v2 | T4 | 0.40 to 0.85 | elicited | same |
| v3 | T4 | 0.30 to 0.80 | elicited | same |
| v4 | T4 | 0.05 to 0.50 | elicited | same |
| q1 | T5 | 0.45 to 0.85 | anchored | PMID 21701028: sensitivity 67% for neuroma, ten studies |
| q2 | T5 | 0.10 to 0.50 | elicited |  |
| q3 | T5 | 0.05 to 0.30 | elicited |  |
| q4 | T5 | 0.05 to 0.30 | elicited |  |

## Declared limits

- The likelihoods are largely elicited. The result describes how the ranking behaves across the stated ranges; it is not a measurement of any test's accuracy.
- It says nothing about any individual and is not a protocol.
- The four hypotheses are treated as exclusive and exhaustive, the tests as independent given the hypothesis, and the parameters as independent. Each of these flatters the tests.
- Sources are small and mostly not in CRPS; two mechanisms rest on rat work from one lineage each.
- Information gain is not clinical value.

