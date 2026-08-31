---
id: C-002
title: Magnetic field modulation of antinociception is radical-pair mediated and shows a magnetic isotope effect
branch: C
status: draft
prior: 0.12
posterior:
lineage:
supersedes:
created: 2026-09-01
bears_on: HC-4
---

## Claim

The reproducible modulation of opioid-mediated antinociception by weak
extremely-low-frequency magnetic fields proceeds through a radical pair
mechanism, in which an applied field alters singlet-triplet interconversion in
a transient radical pair and thereby shifts reaction yield. It follows that the
effect depends on the nuclear spin of nuclei at the radical centre, and not
only on their mass. Substituting a non-zero-spin isotope for a spinless one at
constant mass and chemistry will therefore change the magnitude of the
antinociceptive response, in a direction and size predicted by the hyperfine
coupling.

## Why this, why now

This conjecture exists because E-04 §2.5 records a striking absence: across the
entire indexed literature there are **zero papers** demonstrating coherence,
entanglement, spin selectivity or tunnelling in pain signalling. What does
exist is three decades of magnetobiology on a pain endpoint that nobody has
mechanistically closed. Prato (PMID 25962809) reviews work from 1984 onward
showing that weak magnetic fields modulate opioid-mediated antinociception in
snails and mice, with amplitude dependence, light dependence, and structure
that he explicitly connects to the animal-navigation literature.

Separately, pulsed electromagnetic field therapy for chronic low back pain and
osteoarthritis shows moderate but heterogeneous clinical effect sizes with **no
accepted mechanism** (Sun et al., PMID 35077249, SMD −1.01 against placebo).
A clinical effect with no mechanism is a mechanism-shaped hole, and it is the
kind of hole that attracts bad explanations if a good one is not tested.

The radical pair mechanism is the only candidate that is not speculative
physics: it is established spin chemistry with a validated biological instance
in cryptochrome magnetoreception (Xu et al. 2021, doi:10.1038/s41586-021-03618-9),
and a formal radical-pair model of NMDA receptor magnetosensitivity now exists
(Nair, Zadeh-Haghighi and Simon, PMID 38351304).

This conjecture is filed in Branch C with a prior of 0.12 and the honest
expectation that it will be refuted. It is filed anyway because the test is
cheap, decisive in both directions, and because the alternative to testing it
is that this territory is occupied entirely by people who will not test it.

## Mechanism

A photochemical or enzymatic step generates a spin-correlated radical pair in
a singlet state. The two unpaired electrons interconvert between singlet and
triplet at a rate set by hyperfine coupling to nearby magnetic nuclei and by
the Zeeman interaction with any applied field. Because recombination is
spin-selective, shifting the singlet-triplet branching shifts product yield.
Downstream, a change in reactive oxygen species or nitric oxide production
alters nociceptor membrane excitability or NMDA-receptor-dependent central
sensitisation.

**The quantitative audit gate 01 will demand, supplied here.**

*Energy.* Thermal energy at 310 K is 26.7 meV, that is 4.3e-21 J. The electron
Zeeman splitting in a 50 µT field is about 1.4 MHz, that is 5.8 neV, roughly
2e-7 of kT. **This interaction cannot shift a Boltzmann population by anything
measurable, and the conjecture does not claim it does.** The mechanism is
kinetic: spin selection rules make singlet-triplet interconversion compete with
recombination, so the field changes a yield and not a population. That
distinction is the whole reason the claim is not immediately excluded, and any
version of this conjecture that argues from populations should be refused.

*Timescale.* The required coherence is roughly 1e-6 s, that is about 1 µs,
against a thermal decoherence timescale of 2.5e-14 s, that is 25 fs, for
strongly bath-coupled degrees of freedom. The nine-order-of-magnitude gap is
survivable only because electron and nuclear spins are weakly coupled to the
lattice, which is a documented property rather than a hope: microsecond spin
coherence in flavin-tryptophan radical pairs is what makes cryptochrome
magnetoreception work at all.

*Field.* The relevant regime is 10 µT to 1 mT at 1 to 100 Hz, which is far
below any thermal or stimulation safety limit and requires no exotic hardware.

## Forbidden observation

Isotopic substitution at the radical centre that changes nuclear spin while
holding mass and chemistry constant will not change the magnitude of the
magnetic field effect on antinociception.

## Killer

Blinded, pre-registered animal antinociception assay under an
extremely-low-frequency magnetic field, with isotope as the manipulated
variable.

Enrich the preparation in a non-zero-spin nucleus at a candidate radical
centre and compare against its spinless counterpart: 25Mg (spin 5/2) against
24Mg (spin 0), or 67Zn (spin 5/2) against 64Zn (spin 0), or 17O against 16O.
Magnesium is the first choice because the mass difference between 24Mg and
25Mg is about 4%, small enough that a classical kinetic isotope effect of the
size that confounds the lithium literature is implausible, and because
Mg2+ sits at the NMDA receptor that the existing radical-pair model targets.

Design: two-by-two, isotope by field-on/field-off, n=24 per cell, von Frey and
Hargreaves endpoints, experimenter blinded to both isotope and field state,
with a mass-matched control arm and a sham-coil arm. Pre-register the predicted
direction from the hyperfine coupling before unblinding.

**Refutation threshold:** the conjecture is refuted if the isotope-by-field
interaction term is null with a 95% confidence interval excluding an effect of
20% of the field-on effect size. A null here is a real result and should be
published as one.

Approximate cost 120,000 to 200,000 euro and 12 months. This is the cheapest
decisive experiment in Branch C, which is the main argument for running it
before anything else in that branch.

## Rivals

- **Mass-dependent transport, not spin.** The isotope effect, if any, is an
  ordinary classical kinetic isotope effect on ion transport. This is not a
  hypothetical rival: it is the live confound in the lithium literature, where
  6Li and 7Li differ by about 16% in mass and preferential 6Li uptake by the
  inner mitochondrial membrane has been directly observed (Bukhteeva et al.,
  PMID 38655027). *Distinguished by:* choosing a nucleus pair with a small mass
  difference, and by the mass-matched control arm. This rival is the reason
  25Mg is preferred to 6Li.
- **Induced current, not spin chemistry.** A time-varying field induces eddy
  currents in conductive tissue, which alter excitability by ordinary
  electromagnetic induction with no spin physics involved. *Distinguished by:*
  induced current scales with dB/dt and predicts no isotope dependence
  whatsoever, so the isotope arm separates the two cleanly.
- **The magnetobiology phenomenology is not real.** Thirty years of
  small-effect results from a few laboratories, on endpoints with large
  behavioural variance, in a field with a long history of non-replication.
  E-04 rates the probability that radical-pair magnetic field effects on
  pain-relevant biochemistry are real at 25 to 35%, so this rival carries most
  of the remaining probability mass. *Distinguished by:* the field-on against
  field-off contrast in the spinless arm, which is a direct replication test of
  the base phenomenon and should be reported whatever the isotope arm does.

## Severity

Given the conjecture is false, the probability the proposed test still comes
out favourable is about **0.10**.

The design is unusually severe for this subject area because the signature is
specific: no classical mechanism predicts a dependence on nuclear spin at
constant mass. The main routes to a false pass are an unblinded experimenter,
a mass difference large enough to carry a classical effect, and multiplicity
across two endpoints. All three are controlled, and the pre-registered
directional prediction removes the option of interpreting either sign as
confirmation after the fact.

## What it would change

If confirmed, this would be the first genuine quantum result in pain biology,
and it would give pulsed electromagnetic field therapy the mechanism it has
lacked for decades, which would in turn make it optimisable rather than
empirical.

If refuted, it closes the most credible remaining route by which anything
quantum could act on pain signalling, and Branch C should then be closed
entirely rather than kept alive on weaker arguments. **That is the more likely
outcome and it is worth paying for.** A programme that keeps a speculative
branch open indefinitely because nobody has bothered to kill it is
degenerating by PROGRAMME.md's own definition.

## References

- Prato FS. *Bioelectromagnetics* 2015;36(5):333-48. PMID 25962809. doi:10.1002/bem.21918
- Nair PS, Zadeh-Haghighi H, Simon C. *Sci Rep* 2024;14:3628. PMID 38351304. doi:10.1038/s41598-024-54343-y
- Xu J, Jarocha LE, Zollitsch T, et al. *Nature* 2021;594:535-40. doi:10.1038/s41586-021-03618-9
- Hore PJ, Mouritsen H. *Annu Rev Biophys* 2016;45:299-344. PMID 27216936. doi:10.1146/annurev-biophys-032116-094545
- Bukhteeva I, et al. *Front Physiol* 2024;15:1354091. PMID 38655027. doi:10.3389/fphys.2024.1354091
- Sun X, et al. *Clin Rehabil* 2022;36(5):636-49. PMID 35077249. doi:10.1177/02692155221074052
- Li N, Lu D, Yang L, et al. *Anesthesiology* 2018;129(2):271-77. PMID 29642079. doi:10.1097/ALN.0000000000002226
- Fisher MPA. *Ann Phys* 2015;362:593-602. arXiv:1508.05929
