# C-008 pre-registration and result

**Written before the ensemble was run**, in the sense that the refutation
threshold is C-008's own, filed 2026-09-01 and not altered afterwards:

> The conjecture is refuted if the mean detectability ratio across seeds
> remains below 1.0 with a 95% confidence interval excluding 1.0, with
> interference present and rejection applied, while the Aβ positive control
> still passes for the same configuration.

## Result: REFUTED, and its central premise is confirmed

**18 seeds, 40 null repeats per seed, 2000 trials, 1 fT/√Hz sensor, 350 Hz
bandwidth, first- and second-order gradiometers plus reference regression.**

| Scheme | C-band mean | 95% CI | above 1.0 | Aβ control | Verdict |
|---|---|---|---|---|---|
| none | 0.790 | [0.700, 0.880] | 3/18 | 0.784 | baseline |
| **grad1** | **0.638** | **[0.516, 0.759]** | 2/18 | **15731** (18/18) | **REFUTED** |
| **grad2** | **0.663** | **[0.524, 0.801]** | 1/18 | **3321** (18/18) | **REFUTED** |
| refreg | 0.696 | [0.597, 0.795] | 1/18 | 0.714 (0/18) | inconclusive, control lost |

The Aβ positive control passes overwhelmingly for both gradiometer
configurations, so this is a refutation and not a broken pipeline.

## The result is more interesting than the verdict

**C-008's premise was right. Its prediction was wrong. Both matter.**

*The premise — that sensor sensitivity is not the obstacle — is confirmed.*
Sweeping the sensor noise floor from 1.0 down to **0.05 fT/√Hz, a twentyfold
improvement, does not move the C-band detectability at all**: 0.661, 0.609,
0.587, 0.575, 0.563, 0.559. Buying a quieter magnetometer buys nothing, exactly
as C-008 said.

*The prediction — that interference rejection unblocks it — fails, and by a
measurable margin.* Decomposing the null shows gradiometry does its job
spectacularly:

| Condition | C-band null energy, no rejection | with grad1 |
|---|---|---|
| interference only | 8.90e-22 | **3.11e-27** |
| sensor noise only | 5.60e-28 | 1.11e-27 |

Gradiometry suppresses interference by a factor of **287,000 in energy**, about
540 in amplitude, and raises the sensor-noise floor by exactly the expected
factor of 2 in energy from differencing two independent channels.

And yet it is not enough. Measured directly:

| | interference / C-signal energy |
|---|---|
| no rejection | **2,897,340×** |
| first-order gradiometer | **17.2×** |

**Gradiometry closes a factor of 168,000 and still lands 17× short.** That is
why the ratio sits near 0.64 rather than near either 0 or 2, and it is why
better sensors do not help: the residual is interference, not noise.

## What actually limits it, and the specification that follows

The binding constraint is **sensor gain and orientation matching**, which sets
how well any gradiometer can reject a common-mode field. Sweeping it:

| Gain matching | C-band mean | 95% CI |
|---|---|---|
| 1 : 333 (0.3%) | 0.573 | [0.480, 0.666] |
| 1 : 1,000 | 0.696 | [0.646, 0.746] |
| 1 : 3,333 | 0.866 | [0.815, 0.917] |
| 1 : 10,000 | **0.916** | [0.854, 0.978] |

Monotonic, and **still below 1.0 at 1 part in 10⁴** (0.916, CI [0.854, 0.978],
Aβ control passing 8/8 at 27,175). The crossing therefore lies somewhere above
1:10⁴, and this simulation brackets it rather than pinning it: the honest
statement is **better than 1 part in 10⁴, and not yet measured how much
better**.

**So the engineering statement C-008 was looking for is not "build a
gradiometer". It is "match the channels to about 1 part in 10⁴".** A hardware
first-order gradiometer typically achieves 1:100 to 1:1000. Software and
adaptive reference-array balancing in OPM-MEG reach roughly 1:10⁴. The
requirement is therefore **at or just beyond the edge of demonstrated
practice**, which is a more useful place to have landed than either "solved" or
"impossible". It is also the one number in this programme that a hardware group
could act on tomorrow.

## Three ways this was kept honest

**1. Interference was given spatial structure.** C-004 added interference as
`extra_field_T[None, :]`, numerically identical at every sensor. A first-order
gradiometer cancels a perfectly uniform field exactly, so reusing that model
would have confirmed C-008 by construction. Every interferer here sits at a
stated distance with a stated falloff. Measured non-uniformity across the
10 cm array: cardiac 1.073, mains 1.013, drift 1.000, muscle 8.847.

**2. Sensor gain mismatch was added, and it was the decisive term.** Geometry
is not what limits a real gradiometer; channel matching is. The first draft of
this simulation omitted it and produced an Aβ detectability ratio of **7,991**,
which is what a null collapsed to machine precision looks like. That number was
the tell.

**3. A local muscle source was added**, because C-008's own second rival named
it as the most likely failure route and noted the simulation "does not
currently model muscle at all". Its amplitude, 200 fT at 30 mm, is consistent
with the only relevant measurement found: OPM magnetomyography could not
robustly detect a finger flexor beyond **two centimetres** against 0.5-1 pT RMS
noise (PMID 40542043).

**And the muscle term turned out not to be the answer.** Setting muscle to
zero leaves the C-band at 0.578, slightly *worse* than with it. Rival 2 was
wrong, and it was worth building in order to find that out.

## What this closes and what it leaves open

C-008 said: "If refuted with the Aβ control intact, **Branch B closes**, and it
closes on a quantitative statement rather than a hunch."

The Aβ control is intact. **Branch B closes on this statement:** with a 1 fT/√Hz
array over a superficial nerve at 6.5 mm, first- and second-order gradiometry
leave the C-fibre signal a factor of 17 in energy below the interference
residual, sensor sensitivity is irrelevant to that gap, and closing it requires
channel matching better than 1 part in 10⁴ rather than a quieter magnetometer.

That is a procurement specification, not a hunch, and it is the outcome C-008
was filed to produce. It cost a few minutes of laptop compute and no money.
