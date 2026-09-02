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

## What actually limits it: a false dichotomy, resolved

C-008 framed the question as sensitivity **or** rejection, and asserted
rejection. The simulation says **both, in that order**, and the order is why
the single-variable sweeps looked so misleading.

**Step 1, gain matching.** Rejection quality is set by sensor gain and
orientation matching, not by geometry:

| Gain matching | C-band mean | 95% CI |
|---|---|---|
| 1 : 333 (0.3%) | 0.573 | [0.480, 0.666] |
| 1 : 1,000 | 0.696 | [0.646, 0.746] |
| 1 : 3,333 | 0.866 | [0.815, 0.917] |
| 1 : 10,000 | 0.916 | [0.854, 0.978] |
| 1 : 33,000 | 0.925 | [0.864, 0.986] |

**It plateaus below 1.0.** Going from 1:10⁴ to 1:3.3×10⁴ buys 0.009. So gain
matching alone never gets there, and an early draft of this file claiming "the
crossing lies above 1:10⁴" was wrong.

**Step 2, the local muscle term.** At 1:33,000 with muscle removed: **0.948**
[0.873, 1.022]. Still short. Muscle is not common-mode and no gradiometer
rejects it, but it is not the dominant residual either.

**Step 3, and this is the one that works.** With rejection at 1:33,000, muscle
controlled, and the sensor improved from 1.0 to **0.2 fT/√Hz**:

> **C-band detectability = 4.718, CI [4.057, 5.378], 8 of 8 seeds above
> threshold.** Aβ control 260,639.

**Sensitivity was never irrelevant. It was masked.** The twentyfold sensitivity
sweep looked flat because at that point interference sat 17× above the signal,
so the noise floor was not what the measurement was touching. Remove the
interference and sensitivity immediately becomes the binding constraint, and a
factor of five in the sensor takes detectability from 0.95 to 4.7.

This is why the conjecture's own framing had to fail. "Sensitivity buys
nothing" is true in the interference-limited regime, which is the regime you
are in *before* you fix the interference, and false in the regime you are in
after. C-008 measured the first and legislated for the second.

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

## The trade-off surface, and a cheaper specification than the one above

The two-corner sampling above answered "do you need both?" but not "what is the
cheapest combination that works?". Sweeping both axes jointly, 6 seeds by 15
nulls per cell, muscle held at its literature-consistent 200 fT rather than
zeroed:

**C-band detectability, first-order gradiometer**

| sensor ASD fT/√Hz | 1 : 333 | 1 : 1,000 | 1 : 3,333 | 1 : 10,000 |
|---|---|---|---|---|
| **1.00** | 0.66 | 0.80 | 0.93 | 0.97 |
| **0.50** | 0.61 | 0.71 | 1.13 | **1.42** |
| **0.20** | 0.59 | 0.64 | **1.79** | **3.08** |
| **0.10** | 0.57 | 0.61 | **2.23** | **4.34** |

Bold marks cells whose **95% confidence interval lies entirely above 1.0**, not
merely the mean.

### Three things this settles

**1. Channel matching is a hard gate, and below it nothing else matters.** At
1:333 and 1:1,000, no sensor tested reaches detectability. Improving the sensor
tenfold, from 1.0 to 0.1 fT/√Hz, moves the result from 0.660 [0.507, 0.813] to
0.572 [0.391, 0.753]. Those intervals overlap, so the apparent *decline* is not
significant and should not be reported as one. The correct statement is that
**below about 1:3,000 matching, sensor sensitivity is simply irrelevant**.

**2. A 1 fT/√Hz sensor never suffices, at any matching tested.** The best cell
in that row is 0.967 [0.896, 1.038] at 1:10,000, which straddles the threshold.
Commercial OPMs sit at roughly this figure. **No amount of array engineering
rescues a 1 fT/√Hz sensor**, which is the cleanest negative on the surface.

**3. The specification stated earlier in this file was too expensive.** It
named 1:10⁴ matching *and* 0.2 fT/√Hz, which is the 3.08 cell. The frontier is
cheaper, and there are two distinct corners on it:

| Option | Matching | Sensor | Detectability |
|---|---|---|---|
| A | 1 : 3,333 | 0.20 fT/√Hz | 1.79 [1.34, 2.24], 6/6 seeds |
| B | 1 : 10,000 | 0.50 fT/√Hz | 1.42 [1.15, 1.70], 5/6 seeds |

**These are genuinely exchangeable.** A group with good balancing can use a
more ordinary sensor; a group with an exceptional sensor can tolerate looser
balancing. That exchange rate is the practical output of this simulation and it
is what a hardware group would actually want to know.

**Caveat, stated because it matters for anyone acting on this.** The frontier
cells use 6 seeds against the 18 used for the headline refutation, so they are
less precisely estimated, and cell B in particular has one seed below threshold.
Treat the frontier as located to within about a factor of two on each axis, not
as a procurement guarantee.

---

## What this closes, and what it opens

C-008 predicted that "if refuted with the Aβ control intact, **Branch B
closes**". The Aβ control is intact and the conjecture is refuted. **But the
refutation does not close Branch B; it specifies it.** That is the opposite of
what the conjecture expected its own death to mean, and it is the most useful
thing here.

**The specification, all three required together:**

| Requirement | Value | Status in the field |
|---|---|---|
| Channel gain/orientation matching | **≳ 1 : 3,333** | Reached by adaptive reference-array balancing in OPM-MEG; well beyond a bare hardware gradiometer at 1:100-1:1000 |
| Local myogenic interference | **controlled** | Quiescent limb, or a local reference channel; not solvable by gradiometry |
| Sensor noise floor | **≤ 0.5 fT/√Hz**, and 1.0 never suffices | At the edge: commercial OPMs run ~1 fT/√Hz, laboratory SERF magnetometers reach ~0.16 fT/√Hz |

Meet all three and the simulated C-band ridge is recovered above the matched
null in every seed, at **1.4× to 4.3×** depending on where you sit on the
trade-off surface below. Meet only the rejection requirement, which is
what C-008 proposed, and it is **0.64** and undetectable.

**So the honest verdict is: C-008 asked for one thing and needed three, and the
one it asked for is necessary but the least sufficient of the three.** Branch B
is not closed. It is now costed, and the cost is a five-fold better sensor plus
array balancing at the edge of demonstrated practice plus a quiet limb.

**What would settle it next**, and it is again cheap: sweep the sensitivity and
gain-matching axes jointly to find the cheapest point on the trade-off surface,
rather than the two corners sampled here. That is a few more minutes of compute
and it would turn this specification into a procurement decision.
