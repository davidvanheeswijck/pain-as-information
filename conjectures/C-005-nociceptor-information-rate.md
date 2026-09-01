---
id: C-005
title: A human C-nociceptor carries under 30 bits per second, with little information in fine timing beyond rate
branch: A
status: refuted
prior: 0.45
posterior: 0.25
lineage:
supersedes:
created: 2026-09-01
bears_on: HC-1, HC-2
---

## Claim

The information rate of a single human C-nociceptor axon under natural
stimulation is below 30 bits per second. Almost all of it is carried by
discharge rate and by which fibre class and subtype fired. Spike timing finer
than about 5 milliseconds adds little further information, because
activity-dependent conduction velocity slowing degrades timing precision
exactly when rate is high enough for fine timing to matter.

## Why this, why now

This conjecture exists because of an absence recorded in the programme's own
open ledger. **No published estimate exists for the information rate of a
nociceptor axon in bits per second** (E-01 §1). The figures the programme has
been reasoning with, tens of bits per second, are entropy-rate ceilings derived
from assumed rate and timing precision, not measurements.

That is a conspicuous hole for a programme whose founding premise is that pain
is an information problem. The channel capacity of the channel has never been
measured.

The evidence base also makes the specific prediction testable rather than
merely open. Human C-fibre subtypes are separable on the wire by
**activity-dependent slowing** of conduction velocity (Serra, Campero, Ochoa &
Bostock, PMID 10066906), and that same slowing is what corrupts timing at high
rates. The only direct temporal-pattern result is a single unreplicated ex vivo
study using chemical rather than natural stimuli, which classified three
chemicals at 79.7% from three-spike interval structure (Cho et al.,
doi:10.3389/fncom.2016.00118). One study, one preparation, never replicated in
vivo or in human microneurography.

**Why this is worth a conjecture rather than a literature review.** A number
this basic being absent is usually not an oversight. Human microneurography
yields two to six tracked fibres per session (Troglio et al., PMID 41004469),
recordings are unstable, and information-rate estimation needs long, repeated,
approximately stationary stimulus-response records. It is also unattractive to
publish if the answer is "low bandwidth". That combination is exactly how a
foundational measurement goes unmade for fifty years.

## Mechanism

Not a mechanism claim so much as a measurement claim, but the reasoning behind
the predicted magnitude is physical.

An unmyelinated C-fibre conducts at 0.4 to 1.4 metres per second. Its
conduction velocity depends on recent activity, which is why activity-dependent
slowing works as a subtype classifier at all. That dependence means the arrival
time of a spike at the recording site is a function not only of when it was
generated but of how many spikes preceded it, so **timing jitter grows with
discharge rate**. The mutual information available in fine timing therefore
falls in exactly the regime where a rate code saturates.

Taking the standard entropy-rate ceiling for a spike train of mean rate r and
timing resolution Δt, H ≈ r·log₂(e/(r·Δt)), a C-nociceptor at 10 Hz with 5 ms
resolution gives a ceiling near 58 bits per second, and the transmitted rate
will sit well below the ceiling because real spike trains are not maximum
entropy. Under 30 bits per second is the prediction.

## Forbidden observation

A human C-nociceptor will not be found to transmit more than 30 bits per second
about a natural stimulus, and shuffling spike times within a 5 millisecond
window will not destroy a substantial fraction of the transmitted information.

## Killer

Human microneurography with a stimulus rich enough to carry information, in
healthy volunteers.

Record single identified C-nociceptors, classified by activity-dependent
slowing, while delivering a long repeated mechanical or thermal stimulus
sequence with known statistics (a frozen-noise design, the same repeated
segment many times, which is what makes direct information estimation
possible). Target n=20 units across at least 8 participants, with at least 30
repeats of a 60 second frozen segment per unit.

Estimate transmitted information by the direct method on the repeated segment,
then repeat the estimate after jittering spike times within windows of 1, 5 and
20 milliseconds.

**Refutation threshold:** the conjecture is refuted if the point estimate
exceeds 30 bits per second with a lower confidence bound above 30, or if
jittering within 5 milliseconds destroys more than 30% of the transmitted
information, which would mean fine timing carries substantial information after
all.

Approximate cost 150,000 to 250,000 euro and 24 months, dominated by
microneurography session time rather than equipment. Reduced substantially if
run as a secondary analysis on existing archived recordings, which should be
attempted first.

## Rivals

- **Fine timing carries substantial information after all.** Burst structure
  encodes stimulus quality, as the single ex vivo study suggests, and the
  programme's HC-1 is right in its strong form. *Distinguished by:* jittering
  within 5 milliseconds destroys a large fraction of transmitted information.
- **The rate is far higher than 30 bits per second under natural stimulation.**
  Polymodal C-nociceptors follow electrical stimulation to 100 Hz without
  conduction failure (Werland et al., PMID 33369733), so a high-rate natural
  regime may exist that the estimate above underweights. *Distinguished by:*
  the measured rate distribution under natural stimuli, which this experiment
  produces as a by-product whatever the information estimate shows.
- **The question is ill-posed for a single axon.** Information about pain is
  carried by the population and by which classes co-fire, so a single-axon
  figure is true and irrelevant. E-01 §2 gives real support for this, since
  all C-nociceptor classes are broadly and overlappingly tuned.
  *Distinguished by:* it predicts single-unit information will be low **and**
  that the low value will not constrain anything, which is testable only by
  the multi-unit follow-up this experiment makes possible.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.2**.

The main route to a false pass is under-sampling: too few repeats, or a stimulus
too impoverished to elicit the fibre's full repertoire, would both bias the
information estimate downward and make a low number look confirmatory. The
frozen-noise design with a stated minimum repeat count is the control, and the
jitter analysis is an internal check that does not depend on the absolute
estimate being right.

## What it would change

If confirmed, the programme's HC-1 survives only in its weak form. Structure
beyond mean rate would exist mainly as *which population fired*, not as
temporal pattern within an axon, and every downstream conjecture about reading
or writing temporal patterns on a single fibre would be attacking a channel
with almost nothing in it. It would also mean high-bandwidth transducer work,
including the helium-4 magnetometry route in Branch B, is solving an assumed
requirement rather than a real one.

If refuted, HC-1 is confirmed in its strong form and the programme's central
premise gets its first direct empirical support, which it currently lacks.

**Either outcome moves the programme more than any other conjecture on the
board**, which is the argument for funding it first despite its unglamorous
shape.

## References

- Serra J, Campero M, Ochoa J, Bostock H. *J Physiol* 1999;515:799-811. PMID 10066906. doi:10.1111/j.1469-7793.1999.799ab.x
- Cho A, et al. *Front Comput Neurosci* 2016;10:118. doi:10.3389/fncom.2016.00118
- Werland F, et al. *J Physiol* 2021;599:1595-610. PMID 33369733. doi:10.1113/JP280269
- Troglio A, et al. *PLOS ONE* 2025;20:e0329537. PMID 41004469. doi:10.1371/journal.pone.0329537
- Schmidt R, Schmelz M, Forster C, Ringkamp M, Torebjörk E, Handwerker H. *J Neurosci* 1995;15:333-41. PMID 7823139. doi:10.1523/JNEUROSCI.15-01-00333.1995
- Ghitani N, et al. *Nature* 2025;642:1016-23. PMID 40269164. doi:10.1038/s41586-025-08875-6
- Prescott SA, Ma Q, De Koninck Y. *Nat Neurosci* 2014;17:183-91. PMID 24473266. doi:10.1038/nn.3629
