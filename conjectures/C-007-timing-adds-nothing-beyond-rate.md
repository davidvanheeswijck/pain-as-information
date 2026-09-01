---
id: C-007
title: For a specified stimulus ensemble, sub-5-millisecond spike timing adds no information beyond rate and unit identity
branch: A
status: refuted
prior: 0.40
posterior: 0.32
lineage: C-005
supersedes: C-005
created: 2026-09-01
bears_on: HC-1, HC-2
---

## Claim

Fix a stimulus ensemble. Decode it from a single human C-nociceptor's spike
train using only discharge rate and the identity of the unit, established by
activity-dependent slowing. Adding spike timing at resolutions finer than 5
milliseconds does not increase the information recovered about that ensemble.

## Why this, why now

C-005 asked how many bits per second a nociceptor carries. Triage returned
**WRONG QUESTION**, and the reformulation it supplied is this conjecture. The
objection is correct and worth stating in full, because it is a mistake the
programme is likely to make again.

**An information rate is only defined relative to a stimulus ensemble.** "A
C-nociceptor carries 30 bits per second" is not a property of the axon. It is a
property of the axon *together with* the distribution of stimuli you present.
Change the ensemble and the number changes, so an absolute figure is
under-specified and two honest laboratories could report different values
without either being wrong.

**And the absolute number was never what the programme needed.** What HC-1
actually asserts is that nociceptive traffic carries structure **beyond mean
rate**. That is a comparative claim, and comparative claims are both better
posed and cheaper to measure than absolute ones: the ensemble cancels when you
compare two decoders on the same data, and estimator bias that would corrupt an
absolute information estimate largely cancels too.

So C-005 was a well-specified answer to a slightly wrong question. This is the
same question asked properly.

**What carries over unchanged from C-005**, because the reformulation does not
touch it: the absence in the literature is real, no published estimate exists,
human microneurography yields two to six tracked fibres per session (Troglio et
al., PMID 41004469), and the only direct temporal-pattern result is a single
unreplicated ex vivo study using chemical stimuli (Cho et al.,
doi:10.3389/fncom.2016.00118).

## Mechanism

A measurement claim, but with a physical reason to expect the answer.

Conduction velocity in an unmyelinated fibre depends on recent activity, which
is why activity-dependent slowing works as a subtype classifier at all (Serra,
Campero, Ochoa & Bostock, PMID 10066906). A spike's arrival time at the
recording site therefore depends not only on when it was generated but on how
many spikes preceded it. **Timing jitter grows with discharge rate**, so
whatever information fine timing could carry is degraded precisely in the
regime where a rate code begins to saturate and fine timing would start to
matter.

The prediction is therefore not that timing is uninformative in principle, but
that the axon destroys its own timing precision as a by-product of conducting
at all. Timescales are ordinary: spikes on the millisecond scale, slowing
accumulating over 1e-1 to 1e0 seconds, conduction at 0.4 to 1.4 metres per
second over tens of centimetres.

## Forbidden observation

A decoder given spike times at 1 millisecond resolution will not recover more
information about the stimulus ensemble than one given only rate in 50
millisecond bins plus unit identity.

## Killer

Human microneurography, healthy volunteers, frozen-noise stimulus design.

Record single identified C-nociceptors, classified by activity-dependent
slowing, and present a repeated 60 second mechanical or thermal segment with
known statistics, at least 30 repeats per unit, target n=20 units across at
least 8 participants.

Then compare decoders **on the same recordings**: rate-plus-identity against
rate-plus-identity-plus-timing at 1, 5 and 20 millisecond resolution. Report the
difference in recovered information with a bias-corrected estimator and a
shuffled-timing null computed through the identical pipeline.

**Refutation threshold:** the conjecture is refuted if adding 1 millisecond
timing increases recovered information by more than 20% relative to
rate-plus-identity, with a confidence interval excluding zero, on the same
ensemble.

Approximate cost 150,000 to 250,000 euro and 24 months, dominated by
microneurography session time. **Attempt the archived-recording reanalysis
first**: several laboratories hold marked C-fibre recordings, the comparison is
cheaper than the collection, and a negative on existing data would settle it for
a fraction of the price.

## Rivals

- **Timing does carry information, and the ensemble used was too impoverished
  to reveal it.** A stimulus set that varies slowly cannot demonstrate a fast
  code. *Distinguished by:* the result must hold across at least two ensembles
  of different temporal bandwidth, which this design should include rather than
  add later.
- **The information is in the population, not the axon.** Quality is read from
  which classes co-fire, so a single-unit comparison is true and irrelevant
  (E-01 §2, all C-nociceptor classes broadly and overlappingly tuned).
  *Distinguished by:* it predicts the single-unit comparison comes out null
  **and** that a simultaneous two-unit recording shows cross-fibre synchrony
  carrying information that neither unit carries alone.
- **The decoder, not the axon, is the limit.** A linear or binned decoder can
  miss structure a better model would find, so a null reflects the analysis
  rather than the biology. *Distinguished by:* running at least two decoder
  families, including one that does not assume a fixed bin, and reporting the
  best of each.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.15**.

This is lower than C-005's stated severity, and the reformulation is why. A
comparison between two decoders on identical data cancels the ensemble, cancels
most estimator bias, and cannot be rescued by under-sampling in the way an
absolute estimate can, because under-sampling degrades both arms. The residual
risk is decoder mis-specification, which the two-decoder-family requirement
addresses directly.

## What it would change

If confirmed, HC-1 survives only in its weak form. Structure beyond mean rate
would live **across** fibres rather than **within** one, and every conjecture
about reading or writing a temporal pattern on a single axon is attacking a
channel that does not carry one. That would redirect Branch A towards
population and synchrony measures, and it would mean the bandwidth argument for
helium-4 magnetometry in C-004 needs restating in terms of population
synchrony rather than single-fibre timing.

If refuted, HC-1 gets its first direct empirical support, which the programme
currently lacks entirely, and the case for pattern-based intervention becomes
an evidential case rather than a plausibility argument.

## References

- Serra J, Campero M, Ochoa J, Bostock H. *J Physiol* 1999;515:799-811. PMID 10066906. doi:10.1111/j.1469-7793.1999.799ab.x
- Cho A, et al. *Front Comput Neurosci* 2016;10:118. doi:10.3389/fncom.2016.00118
- Troglio A, et al. *PLOS ONE* 2025;20:e0329537. PMID 41004469. doi:10.1371/journal.pone.0329537
- Werland F, et al. *J Physiol* 2021;599:1595-610. PMID 33369733. doi:10.1113/JP280269
- Schmidt R, Schmelz M, Forster C, Ringkamp M, Torebjörk E, Handwerker H. *J Neurosci* 1995;15:333-41. PMID 7823139. doi:10.1523/JNEUROSCI.15-01-00333.1995
- Ghitani N, et al. *Nature* 2025;642:1016-23. PMID 40269164. doi:10.1038/s41586-025-08875-6
- Prescott SA, Ma Q, De Koninck Y. *Nat Neurosci* 2014;17:183-91. PMID 24473266. doi:10.1038/nn.3629
- Borst A, Theunissen FE. *Nat Neurosci* 1999;2:947-57. doi:10.1038/14731
