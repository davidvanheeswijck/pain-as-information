# Candidates

Presented in an order carrying no information about authorship or origin.


---

## CANDIDATE 1

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
bears_on: HC-1, HC-3, PB-2
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

Second, the failure it would explain is large and documented, and the numbers
got worse when E-05 was compiled. Vanloon et al. (PMID 39601733), 13 studies
and 634 patients, report pooled complication prevalence of 37% and
**explantation in 12%, primarily for insufficient pain relief**. Gatzinsky et
al. (PMID 39084704), n=400, gives the long horizon: cumulative explantation
**17% at 3 years, 23% at 5 years and 38% at 10 years**, with explantation
**specifically for diminished pain relief at 10%, 14% and 23%**. Eldabe et al.
(PMID 35302973) followed 32 implants for 5 to 7 years and found **only 50%
still using the device**, with only 2 of the 16 survivors still on their
original pulse generator.

That is a substantial population whose devices are being removed for a reason
nobody has mechanistically characterised.

**A support this conjecture originally leaned on has been withdrawn.** The
first draft cited Levy et al. (PMID 31494275) for the claim that DRG
stimulation habituates less than spinal cord stimulation. That study is
12-month, two of its authors are employees of the company that makes the DRG
device, and **Gatzinsky's independent 400-patient data find DRG carrying a
higher risk of explantation for diminished relief than SCS, not a lower one.**

The correction cuts both ways and it should be recorded as cutting both ways.
It removes a convenient citation. It also **strengthens the conjecture's
premise**, because the phenomenon to be explained is now larger and better
evidenced than when the conjecture was written. What it forbids is any future
version of this conjecture arguing that DRG is special because it does not
habituate. It is not, and it does.

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

- Chao D, Zhang Z, Mecca CM, Hogan QH, Pan B. *Pain* 2020;161(12):2872-86. PMID 32658148. doi:10.1097/j.pain.0000000000001982
- Kent AR, Min X, Hogan QH, Kramer JM. *Neuromodulation* 2018;21(3):234-46. PMID 29377442. doi:10.1111/ner.12754
- Deer TR, Levy RM, Kramer J, Poree L, et al. *Pain* 2017;158(4):669-81. PMID 28030470. doi:10.1097/j.pain.0000000000000814
- Vanloon M, et al. *Neuromodulation* 2025;28(2):234-48. PMID 39601733. doi:10.1016/j.neurom.2024.10.010
- Bhadra N, Lahowetz EA, Foldes ST, Kilgore KL. *J Comput Neurosci* 2007;22(3):313-26. PMID 17200886. doi:10.1007/s10827-006-0015-5
- Thomson SJ, et al. *Neuromodulation* 2018;21(1):67-76. PMID 29220121. doi:10.1111/ner.12746
- Levy RM, et al. *Neuromodulation* 2024;27(8):1393-1405. PMID 39254621. doi:10.1016/j.neurom.2024.07.003
- Coull JAM, Beggs S, Boudreau D, et al., De Koninck Y. *Nature* 2005;438:1017-21. PMID 16355225. doi:10.1038/nature04223


---

## CANDIDATE 2

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


---

## Gate verdicts returned against CANDIDATE 1

```
00-triage                          azure/openai-responses/gpt-5.6-sol@swedencentral VERDICT: CHEAP KILL AVAILABLE — run a small fixed-pattern-versus-sham chronic pilot to determine whether C-fibre T-junction filtering declines at all
01-physical-plausibility           tensorx/kimi-k3                                VERDICT: MINOR — supply the homeostatic decay time constant of T-junction filtering under chronic fixed-pattern stimulation, or pilot evidence that it decays within 28 days in rat; the conjecture assumes rodent decay runs ~1–1.5 orders of magnitude faster than the human clinical course (months–years), and the entire crossover is void if filtering has not decayed by day 28.
02-biological-plausibility         tensorx/deepseek-v4-pro-0424                   VERDICT: MAJOR — The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease.
03-evidence-integrity              vertex/gemini-3.5-flash@eu                     VERDICT: GATE FAILED TO RUN
04-falsifiability                  tensorx/glm-5.2                                VERDICT: MAJOR — the proposed test has false-pass probability ~0.5 and proves nothing, because it measures an electrophysiological proxy without behavioral allodynia, failing to distinguish the conjecture from central compensation.
05-prior-art                       azure/openai-responses/gpt-5.6-sol@swedencentral VERDICT: PASS — genuinely open or incremental with a stated delta
06-hostile-referee                 tensorx/kimi-k3                                VERDICT: GATE FAILED TO RUN
07-clinical-translation            tensorx/deepseek-v4-pro-0424                   VERDICT: NO VERDICT LINE — treat as MAJOR
```
