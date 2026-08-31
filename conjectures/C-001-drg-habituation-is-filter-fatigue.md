---
id: C-001
title: Loss of benefit in chronic DRG stimulation is decay of T-junction filtering, not tolerance to charge
branch: A
status: draft
prior: 0.25
posterior:
lineage:
supersedes:
created: 2026-09-01
---

## Claim

Dorsal root ganglion stimulation relieves neuropathic pain by amplifying the
low-pass filtering already present at the sensory neuron T-junction, so that
nociceptive C-fibre trains fail to propagate while large-fibre traffic passes.
The decline in benefit seen over months to years is decay of that filtering
enhancement under an unvarying stimulus, and not tolerance to delivered charge.
Because the two have different causes they have different remedies: the first
is addressed by varying the temporal pattern of stimulation at constant charge,
the second only by delivering more charge. Current clinical practice on loss of
benefit does the second.

## Why this, why now

E-03 §3 establishes the mechanism in rat. Chao, Zhang, Mecca, Hogan and Pan
(PMID 32658148) showed that ganglion field stimulation at 20 Hz progressively
abated C-fibre activity over about 20 seconds while Aβ activity persisted
unabated, with Aδ intermediate, and attributed it to use-dependent enhancement
of T-junction filtering. Kent, Min, Hogan and Kramer (PMID 29377442) modelled
the same effect and found it depends on Ca2+ and SK channels producing a
somatic hyperpolarising offset, amplified at 2.8 to 5.5 times threshold and
above 2 Hz. Neither has a declared conflict for the first paper, which matters
in a literature where E-03 documents that industry sponsorship and unblinded
design track with large effects.

Three things make this the right conjecture now rather than five years ago.

First, the mechanism was never tested as the operative mechanism of the
clinical device. ACCURATE (PMID 28030470) established efficacy against dorsal
column stimulation without a sham arm and without any mechanistic endpoint, and
no sham-controlled DRG trial exists anywhere.

Second, the failure it would explain is large and documented. Vanloon et al.
(PMID 39601733), 13 studies and 634 patients, report pooled complication
prevalence of 37% and **explantation in 12%, primarily for insufficient pain
relief**. That is a substantial population whose devices are being removed for
a reason nobody has mechanistically characterised.

Third, the alternative is now cheap to distinguish. ECAP-capable hardware
demonstrates that delivered neural dose can be measured to about 2.8 µV in the
cord (E-02 §2, Levy et al., PMID 39254621), so "same charge, different pattern"
is an experimentally controllable contrast rather than a rhetorical one.

This conjecture also inherits PB-2 from PROGRAMME.md, and it is the concrete
form in which PB-2 can be tested.

## Mechanism

The T-junction of a pseudounipolar sensory neuron is an impedance mismatch: a
spike arriving from the periphery must charge a much larger membrane area to
continue centrally. Propagation across it is therefore marginal and
state-dependent, and it fails preferentially for the fibres with the smallest
safety factor, which are the unmyelinated C-fibres.

Ganglion stimulation is proposed to drive Ca2+ entry, activate SK
conductances, and hold the soma at a hyperpolarised offset that lowers the
safety factor further, converting a marginal junction into a failing one for
C-fibre trains specifically. The selectivity comes from the anatomy, not from
the waveform, which is why it points the opposite way to kilohertz block, where
block threshold varies inversely with axon diameter and large fibres block
first (PMID 17200886).

The proposed decay mechanism is homeostatic. A fixed input to a plastic system
is a training signal. Sustained Ca2+-driven SK activation at an unvarying rate
invites the same compensations that follow any chronic conductance change:
altered channel expression, shifted Ca2+ handling, and adaptation of the SK
response itself. The prediction that follows is that the filtering enhancement
is a function of the *novelty* of the stimulus pattern and not only of its
amplitude, so that a pattern varied within the 2 Hz to 50 Hz band at fixed
total charge restores filtering that a fixed 20 Hz train has lost.

Nothing exotic is invoked. This is ion channel kinetics and cable theory, at
energies and timescales that ordinary electrophysiology already measures:
membrane potential offsets of order 5 mV and spike failure decided over
milliseconds, against a stimulus delivered over about 20 s.

## Forbidden observation

In an animal in which DRG stimulation has lost its C-fibre filtering effect
after chronic fixed-pattern delivery, a varied-pattern stimulus at identical
total charge will not restore C-fibre conduction failure.

## Killer

Chronic single-fibre preparation, rat tibial nerve injury model, following the
Chao et al. design. Implant ganglion field stimulation and deliver a fixed
20 Hz pattern continuously for 28 days, confirming by weekly teased-fibre
recording that C-fibre conduction failure declines from its day-1 value.

Then, in a within-animal crossover with n=16 per arm and the recorder blinded
to condition, compare three conditions at matched total charge: fixed 20 Hz,
pattern varied stochastically within 2 to 50 Hz, and amplitude raised by 50%
at fixed 20 Hz. Outcome measure is the proportion of C-fibre spikes failing to
propagate centrally, with Aβ propagation as the within-animal control.

**Refutation threshold:** the conjecture is refuted if varied-pattern
stimulation does not restore C-fibre failure to within 20 percentage points of
the day-1 value, or if raising amplitude restores it at least as well as
varying pattern does. Either result kills it, and the second is the more
interesting failure because it would make the clinical practice correct.

Approximate cost 180,000 to 250,000 euro and 18 months, which is one
mid-sized grant and is within reach of any of the three or four laboratories
already doing chronic ganglion recording.

## Rivals

- **Tolerance to charge.** The decline is ordinary neural accommodation to a
  sustained input, of the same kind seen across chronic stimulation therapies,
  and depends only on delivered charge. *Distinguished by:* raising amplitude
  at fixed pattern restores the effect and varying pattern at fixed charge does
  not. This is the current implicit clinical model and the reason reprogramming
  usually means turning it up.
- **Mechanical and anatomical drift.** The decline is lead migration,
  encapsulation and the growing distance between contacts and the ganglion, not
  a neural adaptation at all. E-02 §3 documents that the foreign-body capsule
  peaks at two weeks and that the characteristic failure mode of intraneural
  interfaces is physical separation of axons from contacts. *Distinguished by:*
  impedance and ECAP threshold rise together with the loss of effect, and
  neither pattern variation nor amplitude increase restores it.
- **Disease progression.** The device is working as well as it ever did, and
  the underlying condition has worsened, so benefit falls without any change in
  the device-tissue interaction. *Distinguished by:* the day-1 filtering effect
  is recoverable in the same animal at any timepoint by explant-and-reimplant at
  a fresh site, which the other three rivals do not predict.
- **Central compensation.** Peripheral filtering is undiminished, but central
  disinhibition has advanced to the point where the reduced afferent traffic is
  still sufficient to drive the percept. E-01 §5 gives the mechanism. This is
  the most uncomfortable rival, because it is compatible with the entire
  peripheral story being correct and clinically useless. *Distinguished by:*
  measured C-fibre propagation failure holds steady while behavioural
  allodynia returns.

## Severity

Given the conjecture is false, the probability the proposed test still comes
out favourable is about **0.15**.

The main route to a false pass is regression: a preparation degrading over 28
days could show apparent restoration on any manipulation applied late. That is
controlled by the third arm, since amplitude increase and pattern variation
degrade identically, and by the within-animal Aβ control. The blinded recorder
removes the largest remaining source. A false-pass probability of 0.15 is above
what one would want but below the 0.3 threshold at which gate 04 treats a test
as not evidence.

## What it would change

If true, the first response to declining benefit from an implanted ganglion
stimulator is to vary the pattern rather than raise the amplitude, which is
free, immediately available in existing hardware, and the opposite of current
practice. It would also mean that the 12% explantation rate for insufficient
relief is partly iatrogenic.

If false, and specifically if the amplitude arm wins, it removes PB-2 from the
protective belt and materially weakens the programme's case that pattern is
doing work that dose is not. Given PROCO already showed that stimulation rate is not
the active variable across 1 to 10 kHz in spinal stimulation once charge and
position are controlled (PMID 29220121), a second independent result in the
same direction would be strong evidence that the whole tuning thesis is dose in
disguise.

That is the outcome this conjecture is designed to be able to deliver.

## References

- Chao D, Zhang Z, Mecca CM, Hogan QH, Pan B. *Pain* 2020;161(12):2872-86. PMID 32658148. doi:10.1097/j.pain.0000000000001954
- Kent AR, Min X, Hogan QH, Kramer JM. *Neuromodulation* 2018;21(3):234-46. PMID 29377442. doi:10.1111/ner.12754
- Deer TR, Levy RM, Kramer J, Poree L, et al. *Pain* 2017;158(4):669-81. PMID 28030470. doi:10.1097/j.pain.0000000000000814
- Vanloon M, et al. *Neuromodulation* 2025;28(2):234-48. PMID 39601733. doi:10.1016/j.neurom.2024.10.001
- Bhadra N, Lahowetz EA, Foldes ST, Kilgore KL. *J Comput Neurosci* 2007;22(3):313-26. PMID 17200886. doi:10.1007/s10827-006-0015-5
- Thomson SJ, et al. *Neuromodulation* 2018;21(1):67-76. PMID 29220121. doi:10.1111/ner.12746
- Levy RM, et al. *Neuromodulation* 2024;27(8):1393-1405. PMID 39254621. doi:10.1016/j.neurom.2024.07.003
- Coull JAM, Beggs S, Boudreau D, et al., De Koninck Y. *Nature* 2005;438:1017-21. PMID 16355225. doi:10.1038/nature04223
