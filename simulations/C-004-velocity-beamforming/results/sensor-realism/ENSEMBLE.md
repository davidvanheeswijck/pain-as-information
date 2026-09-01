# Ensemble result: the single-seed verdict was an outlier

**Run 2026-09-01, 18 seeds, identical pipeline.**

The `--sensor-realism` run at seed 0 printed
`HEADLINE: C-004's refutation is OVERTURNED`. **That headline is wrong, and it
is wrong because seed 0 is a 1-in-18 fluctuation.** Repeating the identical
analysis across 18 seeds inverts the conclusion.

## The numbers

Detectability ratio for the research alkali OPM (1 fT/√Hz, 350 Hz bandwidth).
A ratio above 1.0 means the C-band peak exceeds the 95th percentile of the
noise-only null distribution computed through the same pipeline.

| Condition | Mean | 95% CI | Seeds above 1.0 | Range |
|---|---|---|---|---|
| Sensor noise only | **1.246** | [1.178, 1.314] | **18 / 18** | 1.004 – 1.558 |
| With interference | **0.731** | [0.649, 0.814] | **1 / 18** | 0.359 – 1.029 |
| With interference + 50/100/150 Hz notch | **0.783** | [0.698, 0.869] | **2 / 18** | 0.386 – 1.039 |

Seed 0 gave 1.029 and 1.036 in the two interference conditions: the only seed
above 1.0 in the first, one of two in the second. **The automated verdict was
driven entirely by which random draw it happened to get.**

## What is now settled, and it is not what the first refutation said

**1. The bandwidth premise was wrong, decisively.** C-band signal energy is
50% below 2.8 Hz, **90% below 29.7 Hz, 99% below 106 Hz**. Aβ energy is 90%
below 557 Hz. The kilohertz requirement in the evidence base is real for
*myelinated* volleys and was carried over to C-fibres, where it does not apply.
A 350 Hz alkali magnetometer has ample bandwidth for C-fibre traffic, with
room to spare.

So the original refutation's stated reason, that no sensor is simultaneously
quiet enough and fast enough, is **false**. The quiet sensors are fast enough.

**2. Against sensor noise alone, it would work.** 18 of 18 seeds detectable,
CI [1.178, 1.314], comfortably above threshold. A 1 fT/√Hz alkali OPM does
recover the C-band ridge when white sensor noise is the only obstacle.

**3. Against realistic interference, it does not.** 1 of 18 seeds, CI
[0.649, 0.814], well below threshold. Notching the mains harmonics helps a
little (0.731 to 0.783) and nowhere near enough.

## The conclusion, and it is more useful than the original

**C-004's refutation stands, but the reason has changed completely.**

The barrier is **not sensor sensitivity and not bandwidth**. It is
**interference rejection**. That is exactly what E-04 §3.1 already said about
magnetospinography, in terms this simulation has now independently reproduced:

> the averaging requirement is set by biological and environmental
> interference, not by sensor noise. A sensor ten times quieter does not turn
> magnetospinography into a single-shot measurement, and anyone promising that
> is selling the wrong bottleneck.

The evidence base warned about this and the first simulation omitted
interference entirely, which is why its answer was both too optimistic in one
place and too pessimistic in another.

## What this redirects the branch towards

If the obstacle is interference rather than sensitivity, then buying a quieter
magnetometer is the wrong move and always was. The relevant engineering is
**interference rejection**: gradiometric configurations, reference sensor
arrays, and adaptive cancellation, which is precisely how OPM-MEG systems
already achieve usable signal-to-noise in the presence of far larger
environmental fields.

That is a different literature and a different conjecture. It has not been
written and should not be assumed to succeed.

## Method note, recorded because it nearly went the other way

A verdict computed from one random seed is not a verdict. The pipeline printed
a confident, plausible, wanted answer that a resampling of the same analysis
reversed. The result was appealing precisely because it confirmed a prediction
made in advance, which is when it warranted the most suspicion rather than the
least.

The simulation's own verdict logic should not declare OVERTURNED or SURVIVES
from a single run when the ratio sits near 1. That is recorded as a defect in
`ledger/OPEN.md` rather than silently patched here.
