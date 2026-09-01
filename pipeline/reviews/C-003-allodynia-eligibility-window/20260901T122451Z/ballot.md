# Candidates

Presented in an order carrying no information about authorship or origin.


---

## CANDIDATE 1

---
id: C-007
title: For a specified stimulus ensemble, sub-5-millisecond spike timing adds no information beyond rate and unit identity
branch: A
status: draft
prior: 0.40
posterior:
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


---

## CANDIDATE 2

---
id: C-003
title: Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain
branch: A
status: draft
prior: 0.30
posterior:
lineage:
supersedes:
created: 2026-09-01
bears_on: HC-1, HC-3, PB-3
---

## Claim

Mechanical allodynia is a coincidence phenomenon in time. Ongoing,
touch-independent C-nociceptor discharge opens a window of a few hundred
milliseconds during which Aβ input reaching the dorsal horn is routed to the
nociceptive output pathway. Aβ input arriving outside that window is felt as
touch. The percept therefore depends on the **relative timing** of two inputs
that are each individually normal, and not on either input being abnormal.

## Why this, why now

This resolves a sharp contradiction sitting inside the evidence base, which is
the highest-yield place to look for a conjecture.

**The contradiction.** E-01 §5 records that in established allodynia the
traffic that hurts arrives on Aβ fibres **whose own behaviour is normal**, and
that the pathology is central: microglial BDNF collapses the chloride gradient
in lamina I, disinhibiting a circuit that lets Aβ input reach nociceptive
output (Coull et al., PMID 12931188 and PMID 16355225; circuit dissection in
Duan et al., PMID 25467445; PKCγ route in Lu et al., PMID 23979158).

But E-01 §5 also records the 2025 finding that inflammation leaves nociceptor
**mechanical** responses minimally affected while inducing long-lasting
touch-independent spontaneous activity in specific classes, which the authors
themselves read as suggesting allodynia arises from **coincidence** of normal
touch input with ongoing nociceptor firing (Ghitani et al., PMID 40269164).

Those are two different stories. In the first, the gate is held open
tonically by a structural change in inhibition, and timing is irrelevant. In
the second, the gate is opened transiently by ongoing nociceptor traffic, and
timing is everything. **Both are supported, and they make opposite predictions
about whether allodynia can be interrupted without changing anything
structural.**

**Why not already done.** The peripheral imaging work and the spinal circuit
manipulations come from different groups using different preparations, and no
published experiment has independently controlled the *timing* of C-fibre
activity while holding C-fibre spike count and Aβ input constant. Doing so
requires optogenetic control of one population and calibrated mechanical
stimulation of the other in the same animal, which is a combination rather than
an invention.

## Mechanism

Ongoing C-nociceptor discharge produces sustained release of glutamate and
neuropeptides onto dorsal horn interneurons. Where the tonic-disinhibition
account has this raise excitability permanently, the coincidence account has it
raise excitability **transiently**, decaying over the timescale of the
underlying synaptic and second-messenger processes, which for windup-like
facilitation is of order hundreds of milliseconds to a few seconds.

Aβ input arriving while the network is in that facilitated state crosses
threshold onto the nociceptive projection pathway. Aβ input arriving after it
has decayed does not.

The prediction that separates this from tonic disinhibition is therefore a
**decaying function of inter-stimulus interval**: pair a burst of C-fibre
activity with a light touch at varying delays and the probability of a
nociceptive response should fall as the delay grows, rather than being flat.

Timescales and magnitudes are ordinary: spike arrival on the millisecond scale,
facilitation decaying over 1e-1 to 1e0 seconds, membrane potential offsets of a
few millivolts. No exotic physics is invoked.

## Forbidden observation

The probability that a calibrated light touch evokes a nociceptive dorsal horn
response will not depend on its delay after a burst of C-fibre activity, once
total C-fibre spike count and touch intensity are held constant.

## Killer

Mouse, neuropathic or inflammatory model with established mechanical allodynia,
using optogenetic control of a defined nociceptor population so that C-fibre
spike count is set by the experimenter rather than inferred.

Deliver a fixed-count C-fibre burst, then a calibrated von Frey touch at
delays of 50, 200, 500, 1000 and 3000 milliseconds, randomised, with a
no-burst control condition. Read out both dorsal horn projection neuron
responses electrophysiologically and nocifensive behaviour, in separate
cohorts. Target n=12 per group.

**Refutation threshold:** the conjecture is refuted if response probability is
flat across delays from 50 to 3000 milliseconds, that is, if the fitted decay
constant's 95% confidence interval includes infinity, while the no-burst
control confirms the paradigm can detect a difference at all.

Approximate cost 200,000 to 300,000 euro and 18 months, in a laboratory that
already has the optogenetic lines, which is the main constraint on where it can
run rather than on whether it can.

## Rivals

- **Tonic disinhibition, timing irrelevant.** The chloride gradient has
  collapsed, the gate is open, and any Aβ input is read as pain regardless of
  what preceded it. This is the mainstream account and it has strong support.
  *Distinguished by:* flat response probability across delays.
- **Peripheral sensitisation after all.** The Aβ fibres or the nociceptors are
  not behaving normally in the neuropathic state even if they are in the
  inflammatory one, so the coincidence framing imports a finding from the wrong
  model. *Distinguished by:* direct recording of Aβ and C-fibre responses to
  the calibrated stimuli, which this design produces anyway.
- **Both, at different disease stages.** Coincidence dominates early while
  disinhibition is incomplete, and tonic disinhibition dominates late. This is
  the most likely rival to be true and the least convenient, because it means
  the answer depends on when you look. *Distinguished by:* running the delay
  series at two timepoints after model induction, which this design should
  therefore do from the start rather than as a follow-up.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.2**.

The main route to a false pass is that any burst-then-touch paradigm produces
some decay simply through sensory adaptation or motor habituation, independent
of the proposed mechanism. The no-burst control and the randomised delay order
address it, and the requirement that the effect appear in dorsal horn recording
and not only in behaviour makes an attentional or motor explanation harder to
sustain.

## What it would change

If confirmed, allodynia becomes a **timing** problem rather than a purely
structural one, and that is the first thing in this programme that would make
temporal-pattern intervention clinically relevant rather than merely
mechanistically interesting. An intervention that suppressed ongoing
nociceptor discharge would close the window without needing to restore
inhibition, and, more usefully, an intervention that merely **desynchronised**
it might do the same.

It also bears directly on PB-3, the programme's hypothesis that night-time
mechanical allodynia has a distinct signature and therefore a distinct handle.
A coincidence mechanism would give it one.

If refuted, the tonic-disinhibition account stands alone, allodynia is
structural, and the programme should stop proposing to treat it by anything
acting on peripheral timing. That would remove the most clinically motivating
target in Branch A, which is a good reason to test it early rather than late.

## References

- Ghitani N, et al. *Nature* 2025;642:1016-23. PMID 40269164. doi:10.1038/s41586-025-08875-6
- Coull JAM, Boudreau D, Bachand K, et al., De Koninck Y. *Nature* 2003;424:938-42. PMID 12931188. doi:10.1038/nature01868
- Coull JAM, Beggs S, Boudreau D, et al., De Koninck Y. *Nature* 2005;438:1017-21. PMID 16355225. doi:10.1038/nature04223
- Duan B, et al. *Cell* 2014;159:1417-32. PMID 25467445. doi:10.1016/j.cell.2014.11.003
- Lu Y, et al. *J Clin Invest* 2013;123:4050-62. PMID 23979158. doi:10.1172/JCI70026
- Peirs C, et al. *Neuron* 2015;87:797-812. PMID 26291162. doi:10.1016/j.neuron.2015.07.029
- Mendell LM, Wall PD. *Nature* 1965;206:97-9. PMID 14334366. doi:10.1038/206097a0
- Woolf CJ. *Nature* 1983;306:686-8. PMID 6656869. doi:10.1038/306686a0


---

## CANDIDATE 3

---
id: C-006
title: A carbon-13 magnetic isotope effect is detectable on a purified flavin radical pair at the bench
branch: C
status: draft
prior: 0.35
posterior:
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


---

## Gate verdicts returned against CANDIDATE 2

```
00-triage                          azure/openai-responses/gpt-5.6-sol@swedencentral VERDICT: WRONG QUESTION — Is endogenous ongoing C-nociceptor activity necessary for Aβ-evoked pain in established allodynia, rather than merely capable of transiently facilitating an already disinhibited dorsal-horn circuit?
01-physical-plausibility           nebius/kimi-k3                                 VERDICT: NO VERDICT LINE — treat as MAJOR
02-biological-plausibility         tensorx/deepseek-v4-pro-0424                   VERDICT: MAJOR — The proposed transient eligibility window of hundreds of milliseconds to seconds is not supported by the physiology of C-fibre-evoked facilitation in the dorsal horn, which is either short (paired-pulse, tens of milliseconds) or long (central sensitisation, minutes to hours); the conjecture needs direct evidence for a facilitation time constant in the proposed range before the killer experiment is worth running.
03-evidence-integrity              vertex/gemini-3.5-flash@eu                     VERDICT: MAJOR — Ghitani et al., 2025 (PMID 40269164) does not support the claim that the authors proposed a temporal-coincidence mechanism for mechanical allodynia.
04-falsifiability                  tensorx/glm-5.2                                VERDICT: MAJOR — the proposed test has false-pass probability ~0.6 and proves nothing
05-prior-art                       azure/openai-responses/gpt-5.6-sol@swedencentral VERDICT: PASS — genuinely open or incremental with a stated delta
06-hostile-referee                 nebius/kimi-k3                                 VERDICT: NO VERDICT LINE — treat as MAJOR
07-clinical-translation            tensorx/deepseek-v4-pro-0424                   VERDICT: NOT APPLICABLE — mechanistic conjecture with no translational claim
```
