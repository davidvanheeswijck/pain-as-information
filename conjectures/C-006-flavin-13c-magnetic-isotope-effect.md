---
id: C-006
title: A carbon-13 magnetic isotope effect is detectable on a purified flavin radical pair at the bench
branch: C
status: refuted
prior: 0.35
posterior: 0.55
lineage: C-002
supersedes: C-002
created: 2026-09-01
bears_on: HC-4
---

## Claim

Site-specific ¹³C substitution at flavin C4a measurably changes the magnetic
field effect on the recombination yield of the flavin-tryptophan radical pair,
compared with natural-abundance flavin, in a purified in vitro preparation.
This is a bench measurement on a protein, not a claim about pain. It is filed
because it is the calibration step that any biological magnetic isotope claim
must pass first, and it has never been done.

## Why this, why now

This conjecture is the rebuilt survivor of C-002, which proposed testing
radical-pair mediation of magnetic-field antinociception using **²⁵Mg against
²⁴Mg** in an animal assay. That design failed a cheap-kill check. The failure
is instructive and is recorded in full in `ledger/REFUTED.md`, but the two
reasons matter here because they determine what replaces it.

**The objection that was raised turned out to be wrong.** Gate 00 argued that
²⁵Mg is quadrupolar (spin 5/2) and that fast quadrupolar relaxation in a
distorted binding site would average the hyperfine away. On the numbers it does
not: the worst measured protein-bound ²⁵Mg relaxation in the literature is
**T₂ ≈ 31 µs** in an enzyme ternary complex with a deliberately strained
coordination sphere, and 472 µs in the binary complex (Ehrlich & Colman,
PMID 7819280). Against a radical-pair window of about 1 µs that is 30 to 470
times too slow to matter. The objection retires.

**Two better reasons killed it instead.**

*No spin density, so no hyperfine, so no effect is possible in principle.* A
magnetic isotope effect requires unpaired electron spin density at the magnetic
nucleus. Closed-shell Mg²⁺ has none. The ²⁵Mg design therefore silently
presupposed a Mg⁺• radical, which is exactly the contested step: the
Buchachenko magnesium isotope literature failed independent replication
(Crotty et al., PMID 22198842), and Hore's adjudication notes there is "scant
evidence that Mg has any biologically relevant redox chemistry" (PMID 22307585).
A null result would then be uninformative, since it could not distinguish "no
radical pair mechanism" from "magnesium is not at a radical centre". **That
destroyed C-002's own claim to be decisive in both directions**, which was the
justification for filing a Branch C conjecture at all.

*The field range and the isotope were physically incompatible.* The ²⁵Mg⁺
ground-state hyperfine constant is **−596.254376(54) MHz** (Itano & Wineland,
doi:10.1103/PhysRevA.24.1364), that is about 21.3 mT, giving an effective
hyperfine field of order 63 mT. C-002 proposed 10 µT to 1 mT. Two to four
orders of magnitude apart, which is why every claimed magnesium effect in the
literature sits at 3 to 80 mT and none at microtesla.

**¹³C on flavin fixes all three problems at once**, and the reason it has not
been done is that the prediction machinery and the labelling chemistry were
published by different groups within the last three years and nobody has joined
them.

## Mechanism

The flavin-tryptophan radical pair [FAD•− TrpH•+] is the one radical pair with
a validated biological instance, in cryptochrome magnetoreception. Its
singlet-triplet interconversion is driven by hyperfine coupling to magnetic
nuclei in the two radicals, and its recombination is spin-selective, so an
applied field that changes the singlet-triplet branching changes product yield.

Adding a ¹³C at a position carrying substantial spin density adds a new
hyperfine coupling and changes the interconversion. Removing it, by using
natural-abundance flavin at 98.9% ¹²C, removes that coupling. ¹²C has **nuclear
spin 0**, so this is a genuine spin-off to spin-on substitution rather than a
change between two non-zero spins, which is what ¹⁴N to ¹⁵N would be.

**Quantitative audit, supplied here as gate 01 requires.**

*Energy.* Thermal energy at 310 K is 26.7 meV, that is 4.3e-21 J. The
hyperfine and Zeeman interactions here are of order 40 MHz, that is about
1.7e-7 eV, roughly 6e-6 of kT. **This cannot shift a Boltzmann population and
the conjecture does not claim it does.** The effect is kinetic: spin selection
rules make singlet-triplet interconversion compete with recombination, so the
observable is a yield, not a population. Any version of this argued from
populations should be refused.

*Timescale.* The radical pair must retain spin coherence for of order 1e-6 s,
that is about 1 µs, against a thermal decoherence timescale of 2.5e-14 s, that
is 25 fs, for strongly bath-coupled degrees of freedom. The nine-order gap is
survivable only because electron and nuclear spins are weakly coupled to the
lattice, which is measured rather than assumed: microsecond spin coherence in
flavin-tryptophan pairs is what makes cryptochrome work at all.

*Magnitude, which is the reason to expect a large effect.* The measured ¹³C
hyperfine tensor at flavin C4a in a flavoprotein semiquinone has principal
values 40, −13.5 and −9 MHz (Martínez, Frago, Medina & García-Rubio,
PMID 40771403). 40 MHz corresponds to about **1.43 mT**, against a
hyperfine-only B½ for the pair of **1.89 mT in solution and 2.46 mT in
cryptochrome** (Wong, Benjamin & Hore, PMID 36519379). A single ¹³C at C4a is
therefore a perturbation of the same order as the entire field scale of the
system, not a marginal one.

*Mass confound.* One ¹³C on a 785 Da flavin is a 0.13% mass change, against 4%
for ²⁴Mg to ²⁵Mg. The classical kinetic isotope effect that confounds the
lithium literature is not available here.

## Forbidden observation

Site-specific ¹³C substitution at flavin C4a will not change the shape or
amplitude of the magnetic field effect curve on radical pair yield, relative to
natural-abundance flavin measured under identical conditions.

## Killer

Transient absorption spectroscopy on purified flavoprotein, field-swept.

Prepare selectively ¹³C-labelled flavin biosynthetically, which is established
(Schleicher et al., PMID 34521887), and natural-abundance flavin as the
comparator. Measure the magnetic field effect on radical pair yield across
0 to 20 mT in fine steps, at least 5 independent preparations per condition,
with the operator blind to which sample is labelled.

Pre-register the predicted direction and approximate magnitude from the
published simulation machinery, which already identifies C4, C4a and C8α as the
highest-leverage positions (Pažėra, Benjamin, Mouritsen & Hore, PMID 36669149).

**Refutation threshold:** the conjecture is refuted if the B½ values of the
labelled and unlabelled preparations differ by less than 0.2 mT with a 95%
confidence interval excluding a 0.5 mT difference, given that the assay
resolves a known positive control.

Approximate cost **40,000 to 80,000 euro and 9 months**, in a laboratory with
an existing transient absorption setup. That is a small fraction of the
120,000 to 200,000 euro animal study C-002 proposed, and it is the reason this
conjecture replaces it rather than following it.

**Explicit warning carried forward:** do not build the isotope arm on
superoxide. O₂•− has an orbitally degenerate ground state and spin-orbit
coupling that relaxes its **electron** spin within a nanosecond, which
suppresses weak-field effects regardless of nuclear spin.

## Rivals

- **The effect is real but too small to resolve.** The ¹³C hyperfine is real,
  but its contribution is swamped by the many other magnetic nuclei already in
  the flavin and tryptophan radicals, so adding one more changes B½ by less
  than the measurement precision. This is the most likely way the conjecture
  fails and it is not a refutation of radical-pair physics.
  *Distinguished by:* the effect size scales as predicted when C4, C4a and C8α
  are labelled together rather than singly, which the design should include as
  a dose arm.
- **The preparation does not sustain the radical pair.** The purified protein
  outside its native context does not form or maintain [FAD•− TrpH•+] long
  enough, so the assay measures nothing. *Distinguished by:* the known
  magnetic field effect on the unlabelled preparation, which is the mandatory
  positive control and which the field has already measured.
- **Radical pair effects on this system are an artefact of the measurement.**
  Transient absorption under repeated laser excitation produces photodegradation
  that correlates with field exposure order. *Distinguished by:* randomised
  field order and interleaved sample identity, both cheap.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.15**.

The signature is specific: no classical mechanism predicts a dependence on
nuclear spin at constant mass and constant chemistry, and the 0.13% mass
difference is far too small to carry a kinetic isotope effect of the required
size. The main routes to a false pass are operator bias and photodegradation
ordering, both controlled by blinding and randomisation. The pre-registered
direction removes the option of reading either sign as confirmation.

## What it would change

If confirmed, the programme has a **calibrated instrument**: a bench assay in
which a magnetic isotope effect is known to be detectable, with a measured
effect size. Only then does it make sense to ask whether the same signature
appears in a biological antinociception assay, and any such experiment can be
powered from the bench number rather than guessed.

If refuted, and specifically if a ¹³C effect cannot be detected on the one
radical pair with a validated biological instance, then looking for a magnetic
isotope effect in a whole animal is not worth doing, and **Branch C should be
closed**. That is the outcome this conjecture is designed to make cheap, and it
is the more likely one.

The general point survives either way, and is the reason this is worth 40,000
euro rather than nothing: a bench null closes a branch for a fortieth of the
cost of an animal null.

## References

- Ehrlich RS, Colman RF. *Biochim Biophys Acta* 1995;1246:135-41. PMID 7819280. doi:10.1016/0167-4838(94)00192-j
- Crotty D, Silkstone G, Poddar S, Ranson R, Prina-Mello A, Wilson MT, Coey JMD. *PNAS* 2012;109:1437-42. PMID 22198842. doi:10.1073/pnas.1117840108
- Hore PJ. *PNAS* 2012;109:1357-8. PMID 22307585. doi:10.1073/pnas.1120531109
- Itano WM, Wineland DJ. *Phys Rev A* 1981;24:1364. doi:10.1103/PhysRevA.24.1364
- Wong SY, Benjamin P, Hore PJ. *Phys Chem Chem Phys* 2023;25:975-82. PMID 36519379. doi:10.1039/d2cp03793a
- Martínez JI, Frago S, Medina M, García-Rubio I. *Magn Reson* 2025;6:183. PMID 40771403. doi:10.5194/mr-6-183-2025
- Pažėra GJ, Benjamin P, Mouritsen H, Hore PJ. *J Phys Chem B* 2023;127:838-45. PMID 36669149. doi:10.1021/acs.jpcb.2c05335
- Schleicher E, et al. *Sci Rep* 2021;11:18106. PMID 34521887. doi:10.1038/s41598-021-97588-7
- Xu J, Jarocha LE, Zollitsch T, et al. *Nature* 2021;594:535-40. doi:10.1038/s41586-021-03618-9
- Zadeh-Haghighi H, Siguenza CR, Smith RP, Simon C, Craddock TJA. *Sci Adv* 2026;12:eady8317. PMID 41686898. doi:10.1126/sciadv.ady8317
