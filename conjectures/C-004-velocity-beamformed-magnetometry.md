---
id: C-004
title: Velocity-domain matched filtering can recover an evoked C-fibre magnetic component from a superficial nerve
branch: B
status: draft
prior: 0.20
posterior:
lineage:
supersedes:
created: 2026-09-01
bears_on: HC-2, HC-4
---

## Claim

Unmyelinated C-fibre volleys have never been detected magnetically because
biomagnetism averages in laboratory time, and a slow dispersed volley
phase-cancels under that operation. Averaging instead in the **velocity
domain**, by applying a matched filter that shifts each sensor's trace by the
propagation delay expected for an assumed conduction velocity and sweeping that
assumed velocity, will recover a coherent C-fibre component from a superficial
human nerve that time-domain averaging destroys.

## Why this, why now

Three facts from the evidence base collide, and the collision is the
conjecture.

**One.** A superficial human nerve gives a magnetic signal of about **1 pT at
6.5 mm standoff**, which is large and has been recovered in humans with three
optically pumped magnetometers (Bu et al., PMID 35370794). This is not the
5-50 fT deep-cord problem, and conflating the two is the commonest error in the
field (E-04 §3.1).

**Two.** Despite that, **Aδ fibres have never been detected magnetically, and
C-fibres are ten times slower again**, because conduction velocity dispersion
spreads the compound volley over tens of milliseconds so it cancels on
averaging (E-02 §4, Adachi & Kawabata, PMID 38690583).

**Three.** Helium-4 optically pumped magnetometers reach DC to 2 kHz bandwidth,
where common alkali magnetometers stop between 150 and 350 Hz, at a cost of
roughly 13 times in sensitivity (E-04 §3.1). Bu et al. hit exactly this wall,
with a 500 Hz filter and a 15 ms ringing artefact.

So the signal is large, the sensor bandwidth now exists, and the only thing in
the way is a signal-processing operation chosen decades ago for myelinated
fibres.

**Why not already done.** Biomagnetism systems average channels in laboratory
time because that is correct for fast synchronous myelinated volleys, which is
what the field grew up measuring. Velocity-domain matched filtering is entirely
standard in radar, sonar and seismic array processing, where it is called
beamforming or slant stacking, but those communities do not work on peripheral
nerve and the biomagnetism community does not use their tools. This is a
transplant between fields that do not talk, not a new idea in either.

## Mechanism

A propagating volley is a moving current dipole. At a linear sensor array along
the nerve, a spike arriving at position x at time t appears at position x + Δx
at time t + Δx/v, where v is conduction velocity. Time-domain averaging across
trials preserves anything phase-locked to the stimulus at a **fixed latency**,
which is true for a fast volley with narrow velocity spread and false for a
slow one with wide spread.

The matched filter is: for a hypothesised velocity v, shift each sensor's trace
by −x/v, then sum. Components travelling at v add coherently; everything else
adds incoherently. Sweeping v produces a velocity spectrum, and a C-fibre
population should appear as a ridge between 0.4 and 1.4 metres per second,
separated from the Aβ ridge above 30 metres per second by nearly two orders of
magnitude in velocity, which is an enormous separation for a matched filter.

The dispersion that destroys time-domain averaging is precisely what makes the
velocity domain informative: a wide velocity spread is a broad ridge, not a
cancelled signal.

Nothing exotic is invoked. This is array signal processing on a magnetic field
of about 1 pT, with sensor bandwidth to 2 kHz and propagation delays of order
10 to 100 milliseconds over a 10 cm array.

## Forbidden observation

A velocity sweep over a superficial nerve after a C-fibre-selective stimulus
will not show any coherent ridge in the 0.4 to 1.4 metres per second band above
the noise floor of the same analysis applied to unstimulated recordings.

## Killer

Human forearm or lower-leg superficial nerve, helium-4 optically pumped
magnetometer array of at least 8 sensors in a line along the nerve over at
least 10 cm, in a magnetically shielded room.

Stimulate with a protocol that preferentially recruits C-fibres, for example
transcutaneous slow depolarising pulses or capsaicin-sensitised heat, with
simultaneous **microneurography in the same nerve as ground truth** so that the
presence and timing of C-fibre traffic is known independently rather than
assumed. Target 2,000 stimulus repeats per condition, n=8 participants.

Analyse by velocity-domain matched filtering, sweeping assumed velocity from
0.2 to 100 metres per second, and compare against time-domain averaging on the
identical data.

**Refutation threshold:** the conjecture is refuted if no ridge appears in the
0.4 to 1.4 metres per second band at signal-to-noise above 3 when
microneurography confirms C-fibre traffic was present, or if velocity-domain
analysis does not outperform time-domain averaging on the same recordings.

Approximate cost 250,000 to 400,000 euro and 24 months, dominated by
helium-4 magnetometer access and shielded-room time. **The analysis half can be
run first for almost nothing** on existing archived magnetoneurography
recordings, if any include a slow-fibre stimulus, and that should be attempted
before any hardware is bought.

## Rivals

- **The signal is genuinely absent, not hidden.** C-fibre currents are too
  small to produce a detectable external magnetic field at any standoff,
  because current dipole moment scales with axon cross-section and C-fibres are
  0.2 to 1.5 µm against 6 to 12 µm for Aβ. *Distinguished by:* the velocity
  sweep shows no ridge even when microneurography confirms traffic, which is
  why the simultaneous ground truth is not optional.
- **Asynchrony, not dispersion, is the problem.** C-fibres do not fire
  synchronously enough for any coherent summation, regardless of the domain
  the averaging happens in, because each fibre's latency varies trial to trial
  through activity-dependent slowing. *Distinguished by:* this predicts the
  ridge is absent but that single-trial velocity-domain energy in the C band
  still rises above baseline; the conjecture predicts a coherent ridge.
- **Volume conduction smears the array geometry.** The assumed straight-line
  propagation geometry does not hold through tissue, so the matched filter is
  mis-specified and cancels the very signal it is meant to recover.
  *Distinguished by:* the Aβ ridge. If the method cannot recover the known,
  large, fast component at its known velocity on the same recording, the
  geometry is wrong and the C-band null is uninterpretable. **This makes the Aβ
  ridge a mandatory positive control**, and it is free.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.15**.

The chief route to a false pass is that a velocity sweep with enough free
parameters will find a ridge somewhere in noise. The controls against it are
the pre-specified velocity band, the unstimulated-recording null distribution
computed through the identical pipeline, and the requirement that
microneurography independently confirm traffic was present on the trials
analysed. The Aβ positive control additionally prevents a mis-specified filter
from being read as a negative result.

## What it would change

If confirmed, non-contact reading of nociceptive traffic becomes possible in
humans without penetrating the nerve, which is the single hardest bottleneck in
E-02 and the thing every downstream closed-loop idea is blocked on. It would
also be the first genuinely useful contribution of quantum technology to this
programme, and it would be an instrument rather than a theory.

If refuted with the Aβ control intact, Branch B narrows sharply: magnetometry
can read myelinated traffic and not nociceptive traffic, and the programme
should stop proposing to read pain magnetically. **That is a cheap way to close
a whole branch**, and closing it is worth nearly as much as opening it.

## References

- Bu Y, Prince J, Mojtahed H, Kimball D, Shah V, Coleman T, Sarkar M, Rao R, Huang M, Schwindt P, Borna A, Lerman I. *Front Physiol* 2022;13:798376. PMID 35370794. doi:10.3389/fphys.2022.798376
- Adachi Y, Kawabata S. *Front Med Technol* 2024;6:1351905. PMID 38690583. doi:10.3389/fmedt.2024.1351905
- Sumiya S, Kawabata S, Hoshino Y, Adachi Y, Sekihara K, et al. *Sci Rep* 2017;7:2192. doi:10.1038/s41598-017-02406-8
- Boto E, Holmes N, Leggett J, et al., Bowtell R, Brookes MJ. *Nature* 2018;555:657-61. PMID 29562238. doi:10.1038/nature26147
- Bu Y, Burks J, Yang K, et al. *Commun Biol* 2024;7:893. PMID 39075164. doi:10.1038/s42003-024-06435-8
- Serra J, Campero M, Ochoa J, Bostock H. *J Physiol* 1999;515:799-811. PMID 10066906. doi:10.1111/j.1469-7793.1999.799ab.x
- Verardo C, Romeni S, Micera S. *iScience* 2025;28:112495. PMID 40458190. doi:10.1016/j.isci.2025.112495
