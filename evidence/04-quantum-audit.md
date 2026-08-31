# E-04. Quantum effects in biology and neuroscience: a sceptical audit

> Prepared 1 September 2026. Purpose: to fence this programme away from
> pseudoscience while preserving the genuinely defensible ground.
>
> Bears on: Branch B (quantum technology as instrument), Branch C (quantum
> effects in neural tissue), HC-4 (realisable transducer), and
> `pipeline/gates/01-physical-plausibility.md`, whose checklist is derived from
> Tier 4 below.

---

## The physical yardstick, stated once

At body temperature (310 K), *kT* = 26.7 meV. The corresponding thermal timescale is ħ/*kT* = 2.5 × 10⁻¹⁴ s, roughly **25 femtoseconds**. Any degree of freedom strongly coupled to the thermal bath loses phase coherence on that order. **This is the number every Tier 2 claim must survive**, and gate 01 demands it explicitly.

The crucial distinction, which almost all popular writing and much bad literature elides: **quantum effects survive in warm biology when the relevant degree of freedom is weakly coupled to the bath, or when the effect is kinetic rather than thermodynamic.**

Spin is the canonical example. The electron Zeeman splitting in the Earth's field (50 µT) is about 1.4 MHz, or 5.8 neV, which is 2 × 10⁻⁷ of *kT*. It cannot shift a Boltzmann population by anything measurable. It nonetheless changes chemistry, because spin selection rules make singlet-triplet interconversion compete kinetically with recombination. **Yield, not population.** That is why Tier 1 works and Tier 2 mostly does not, and any conjecture in Branch C has to say which side of that line it is on.

---

## TIER 1: Established or near-established

### 1.1 Radical pair magnetoreception (STRONG, the flagship result)

The radical pair mechanism is real physical chemistry, established in spin chemistry since the 1970s, entirely independent of any biological claim.

- Ritz T, Adem S, Schulten K. *Biophys J* 78:707-718 (2000). doi:10.1016/S0006-3495(00)76629-X. PMID 10653784. The founding proposal.
- Hore PJ, Mouritsen H. *Annu Rev Biophys* 45:299-344 (2016). doi:10.1146/annurev-biophys-032116-094545. PMID 27216936. The authoritative review.
- Xu J, Jarocha LE, Zollitsch T, et al. (Hore, Mouritsen). "Magnetic sensitivity of cryptochrome 4 from a migratory songbird." *Nature* 594:535-540 (2021). doi:10.1038/s41586-021-03618-9.

Xu et al. is the strongest single result in quantum biology: purified ErCRY4 from European robin shows magnetically sensitive photochemistry in vitro via a flavin-tryptophan radical pair cascade, and is more magnetically sensitive than CRY4 from chicken and pigeon.

**The honest caveat, which the authors state themselves:** the measured magnetic field effects are demonstrated at field strengths well above 50 µT, and the in-vitro protein is not shown to be sensitive enough at geomagnetic strength. Making the compass work in vivo needs additional ordering, immobilisation and probably amplification that have not been demonstrated. Mechanism strongly supported; in vivo pathway not closed. Required coherence is roughly **1 µs, nine orders of magnitude longer than 25 fs**, achievable precisely because spins are weakly bath-coupled.

### 1.2 Photosynthetic excitonic coherence (the field walked this back, and the programme must say so)

> Engel GS, Calhoun TR, Read EL, Ahn TK, Mančal T, Cheng YC, Blankenship RE, Fleming GR. *Nature* 446:782-786 (2007). doi:10.1038/nature05678. PMID 17429397.

This is the most-cited claim in quantum biology and it is **substantially retracted in substance, though not formally withdrawn**:

- Duan HG, Prokhorenko VI, Cogdell RJ, Ashraf K, Stevens AL, Thorwart M, Miller RJD. "Nature does not rely on long-lived electronic quantum coherence for photosynthetic energy transfer." *PNAS* 114:8493-8498 (2017). doi:10.1073/pnas.1702261114. PMID 28743751. At physiological temperature, no low-frequency quantum beats with dephasing beyond about 60 fs.
- Thyrhaug E, Tempelaar R, Alcocer MJP, et al., Zigmantas D. *Nat Chem* 10:780-786 (2018). doi:10.1038/s41557-018-0060-5. PMID 29785033. The long-lived oscillations are ground-state Raman-active vibrational modes, not inter-exciton electronic coherence.
- Cao J, Cogdell RJ, Coker DF, et al. (18 authors). "Quantum biology revisited." *Sci Adv* 6:eaaz4888 (2020). doi:10.1126/sciadv.aaz4888. PMID 32284982. A near-consensus statement from the 2D-spectroscopy community.

**Verdict:** electronic coherence in photosynthesis at physiological temperature lasts tens of femtoseconds, consistent with the 25 fs estimate, and is **not functionally load-bearing** for light harvesting. Vibronic coupling matters; "quantum computing in the leaf" does not exist.

**Any document that cites Engel 2007 without citing Duan 2017 and Cao 2020 is either uninformed or misleading.** Gate 03 checks for exactly this pairing.

### 1.3 Enzyme hydrogen tunnelling (established, and boring in the right way)

- Klinman JP, Kohen A. *Annu Rev Biochem* 82:471-496 (2013). doi:10.1146/annurev-biochem-051710-133623.
- Masgrau L, Roujeinikova A, Johannissen LO, et al., Scrutton NS, Leys D. *Science* 312:237-241 (2006). doi:10.1126/science.1126002. PMID 16614214.

Nuclear tunnelling of H, D and T through reaction barriers is not controversial. Signature: anomalously large and temperature-dependent kinetic isotope effects (soybean lipoxygenase KIE around 80, far above the semiclassical limit of about 7). This is quantum mechanics doing real work in enzymes at 310 K.

It is also the *least* exciting kind: a tunnelling correction to a rate constant. It carries no information and is compatible with wholly classical rate theory downstream. **It does not license anything about cognition**, and the move from "quantum effects exist in biology" to "therefore quantum cognition" usually passes through this citation.

### 1.4 Vibrational theory of olfaction (refuted; retire it)

- Keller A, Vosshall LB. *Nat Neurosci* 7:337-338 (2004). doi:10.1038/nn1215. PMID 15034588. Humans cannot distinguish acetophenone from its deuterated isotopomer.
- Block E, Jang S, Matsunami H, et al., Batista VS, Zhuang H. "Implausibility of the vibrational theory of olfaction." *PNAS* 112:E2766-E2774 (2015). doi:10.1073/pnas.1503054112. PMID 25901328.

Treat vibrational olfaction as a closed negative result, and continued advocacy for it as a mild red flag.

---

## TIER 2: Serious, published, unproven, nervous-system-adjacent

### 2.1 Fisher's nuclear-spin and Posner proposal (the best steelman in the field, and currently losing)

> Fisher MPA. "Quantum cognition: The possibility of processing with nuclear spins in the brain." *Ann Phys* 362:593-602 (2015). arXiv:1508.05929.

**Steelman it properly, because it deserves it.** Fisher did the one thing nobody else in quantum-brain theorising did: he asked what degree of freedom could *possibly* stay coherent in warm wet tissue, and answered correctly. Nuclear spins. ³¹P at 1 T has a Zeeman splitting of about 17 MHz, roughly 71 neV, about 10⁻⁶ of *kT*. Precisely because nuclear spins couple so weakly to everything, solution-phase ³¹P T₁ can reach seconds to minutes, and ⁶Li⁺ in solution has a reported coherence time of order **5 minutes**. He then identified a specific molecular protector (the Posner cluster Ca₉(PO₄)₆), a specific entangling reaction (pyrophosphatase cleaving PPᵢ into two Pᵢ), and specific falsifiable isotope predictions.

**Where it stands in 2026: mostly negative, with one interesting positive.**

Against:

- Player TC, Hore PJ. *J R Soc Interface* 15:20180494 (2018). doi:10.1098/rsif.2018.0494. PMC6228494. The required symmetry assumptions and long entanglement lifetimes do not hold up.
- Agarwal S, Straub JS, et al. "The Biological Qubit: Calcium Phosphate Dimers, Not Trimers." *J Phys Chem Lett* (2023). doi:10.1021/acs.jpclett.2c03945. PMID 36876913. MD simulation shows the trimer lacks the assumed rotational symmetry axis; Bell-state entanglement between spins in separate Posner molecules decays **sub-second**, far too fast for supracellular processing. Dimers do better, which reframes rather than rescues the proposal.
- Chen R, Li N, Qian H, Zhao RH, Zhang SH. *J Integr Neurosci* 19:595-600 (2020). doi:10.31083/j.jin.2020.04.250. Intracerebroventricular EGTA, ⁴⁰CaCl₂ and ⁴³CaCl₂ in mice: EGTA and ⁴⁰Ca moved the sevoflurane LORR ED50 in the *opposite* direction to prediction, and **⁴³Ca (spin 7/2) was indistinguishable from ⁴⁰Ca (spin 0)**. No calcium isotope dependence.

The lithium isotope behavioural line, which is the phenomenology that keeps this alive:

- Lieberman KW, Alexander GJ, Stokes P. *Pharmacol Biochem Behav* 10:933-935 (1979). PMID 482316.
- Ettenberg A, Ayala K, Krug JT, Collins L, Mayes MS, Fisher MPA. *Pharmacol Biochem Behav* 190:172875 (2020). doi:10.1016/j.pbb.2020.172875. PMID 32084493. ⁶Li produced greater and more prolonged reduction of ketamine hyperactivity than ⁷Li.

Complications that matter, and that a conjecture here must address:

- Bukhteeva I, et al. *Front Physiol* 15:1354091 (2024). PMID 38655027. No isotope difference in mitochondrial Ca efflux, but **preferential ⁶Li uptake by the inner mitochondrial membrane**. A mass-dependent transport difference is a classical explanation for a behavioural isotope effect, and ⁶Li versus ⁷Li is a **16% mass difference**, which is a large classical kinetic isotope effect for a transported cation. Any nuclear-spin interpretation must exclude this first.
- Deline ML, Straub J, Patel M, et al. *Front Physiol* 14:1200119 (2023). PMID 37781224. Isotope effects run in *opposite directions* for different readouts.
- Straub JS, Patel ML, Nowotarski MS, Rao L, Turiansky ME, Fisher MPA, Helgeson ME. *PNAS* 122(10):e2423211122 (2025). doi:10.1073/pnas.2423211122. PMID 40048269. ⁷Li promotes more calcium phosphate particles than ⁶Li. Note the title hedge ("possible"), the direction reversal against the behavioural work, and that this is Fisher's own group.

**Assessment.** The isotope phenomenology is real and repeatedly observed, and that is genuinely interesting. The *nuclear-spin* interpretation is not established, the Posner-trimer substrate has been substantially undermined, the one direct in vivo test of the consciousness prediction failed, and mass-dependent transport is an unexcluded classical confound.

**P(Fisher's mechanism as stated operates in the brain): 3-8%, trending down.** P(lithium isotope effects are real biology worth studying): high, but probably not for quantum reasons.

### 2.2 Xenon isotope anaesthesia (one study, never replicated)

> Li N, Lu D, Yang L, Tao H, Xu Y, Wang C, Fu L, Liu H, Chummum Y, Zhang S. "Nuclear Spin Attenuates the Anesthetic Potency of Xenon Isotopes in Mice." *Anesthesiology* 129:271-277 (2018). doi:10.1097/ALN.0000000000002226. PMID 29642079.

¹²⁹Xe (I=1/2) and ¹³¹Xe (I=3/2) were less potent than spinless ¹³²Xe and ¹³⁴Xe at matched polarisability, n=80 mice, loss-of-righting-reflex endpoint.

**Status as of 2026: no independent replication and no failed replication.** That is the single most important fact about this result. A striking, mechanistically provocative finding, one group, one species, one behavioural endpoint, sitting unreplicated for eight years. Note that the same senior author published the 2020 study *refuting* Fisher's calcium-isotope prediction, which argues for intellectual honesty rather than a house effect, but does not substitute for external replication. A theoretical rationalisation exists (Smith J, Zadeh-Haghighi H, Salahub D, Simon C. *Sci Rep* 11:6287 (2021). doi:10.1038/s41598-021-85673-w) but it is modelling, not evidence.

**An independent replication of Li et al. 2018 is the single highest-value experiment in this tier.** Cheap by physics standards, decisively interpretable either way, and nobody has done it.

### 2.3 Anaesthetic action, electron spin and terahertz modes

- Turin L, Skoulakis EMC, Horsfield AP. "Electron spin changes during general anesthesia in Drosophila." *PNAS* 111:E3524-E3533 (2014). doi:10.1073/pnas.1404387111. PMID 25114249.
- Craddock TJA, Kurian P, Preto J, et al., Hameroff SR, Tuszynski JA. *Sci Rep* 7 (2017). doi:10.1038/s41598-017-09992-7. PMID 28852014. **Simulation and docking only.**

Turin's EPR result is an experiment and shows something real. What it does not show is that this is *causal* for unconsciousness rather than a downstream metabolic or redox consequence. Anaesthetics have well-characterised classical targets (GABA_A, NMDA, TREK/K2P, HCN) with structural biology behind them. The quantum account is not needed to explain the data and does not outperform them.

### 2.4 Orch-OR and microtubules (weakest; do not build on it)

- Hameroff S, Penrose R. *Phys Life Rev* 11:39-78 (2014). doi:10.1016/j.plrev.2013.08.002. PMID 24070914.
- **Tegmark M. *Phys Rev E* 61:4194-4206 (2000).** Microtubule superposition decoherence time about 10⁻¹³ s.
- **Hagan S, Hameroff SR, Tuszyński JA. *Phys Rev E* 65:061901 (2002).** Rebuttal invoking ordered water, Debye screening and topological error correction; recovers 10⁻⁵ to 10⁻⁴ s.

**Do the arithmetic honestly.** Orch-OR requires coherence at the gamma timescale, roughly 25 ms. Tegmark's estimate is short by **eleven orders of magnitude**. The proponents' own most favourable rebuttal is **still short by two and a half to three orders of magnitude**. That is the decisive fact and it has never been closed.

The 2023-2024 experimental results, assessed honestly:

- Kalra AP, Benny A, Travis SM, et al., Hameroff SR, Tuszyński JA, Petry S, **Penrose R**, Scholes GD. "Electronic Energy Migration in Microtubules." *ACS Cent Sci* 9:352-361 (2023). doi:10.1021/acscentsci.2c01114. PMID 36968538. Tryptophan autofluorescence lifetime plus quencher titration gives electronic energy diffusion over **6.6 nm**, reduced by etomidate and isoflurane.

  **Read the number.** 6.6 nm is roughly half a tubulin dimer. This is short-range exciton hopping, the same physics as any aromatic-dense protein. A legitimate photophysics result. It is not delocalised coherence across a microtubule, still less across a neuron, and it says nothing about 25 ms. Penrose and Hameroff are co-authors, so it is not independent corroboration.

- Babcock NS, Montes-Cabrera G, Oberhofer KE, Chergui M, Celardo GL, Kurian P. "Ultraviolet Superradiance from Mega-Networks of Tryptophan in Biological Architectures." *J Phys Chem B* 128:4035-4046 (2024). doi:10.1021/acs.jpcb.3c07936. PMID 38641327. Microtubule quantum yield about 17.6% against about 12.4% for free tryptophan, a roughly 40% enhancement "consistent with what one would expect in the presence of superradiance".

  **Three things to be blunt about.** A quantum-yield ratio is weak evidence for superradiance, and the authors say lifetime measurements are required and were not performed. Their own predicted bright-state lifetimes are **hundreds of femtoseconds**, that is, exactly the thermal timescale, and therefore useless to any cognitive claim. And, to the paper's credit, **it makes no consciousness or Orch-OR claim whatsoever.** The consciousness framing is imported by others. Do not let a citation chain launder it in.

- Khan S, Huang Y, Timuçin D, et al., Wiest MC. "Microtubule-Stabilizer Epothilone B Delays Anesthetic-Induced Unconsciousness in Rats." *eNeuro* 11(8):ENEURO.0291-24.2024 (2024). doi:10.1523/ENEURO.0291-24.2024. PMID 39147581. Delayed loss of righting reflex under 4% isoflurane by a mean 69 s, Cohen's d = 1.9.

  A clean, well-powered behavioural result that should be taken seriously **as pharmacology**. But "therefore consciousness is a quantum microtubule state" is a non sequitur. Microtubule stabilisation changes membrane trafficking, receptor insertion and density, mitochondrial transport and axonal physiology, all entirely classical routes to shifting anaesthetic sensitivity. **The experiment does not discriminate.** Robustness of the effect is not evidence for the quantum interpretation.

Overreach to be aware of: Wiest MC. *Neurosci Conscious* 2025:niaf011. doi:10.1093/nc/niaf011. PMID 40342554. The title asserts far more than the cited evidence supports.

Anchor against two current critical reviews. Arias-Carrión O, Ortega-Robles E, Manjarrez E. *Brain Sci* 16:386 (2026). doi:10.3390/brainsci16040386. PMID 42041796, whose key line is: **"no study to date has demonstrated entanglement, long-lived coherence, or collapse dynamics in neural tissue under operational criteria comparable to those used in controlled quantum systems."** Also Ma X, Wang A. *Front Psychol* 17 (2026). doi:10.3389/fpsyg.2026.1730965. PMID 42137085.

### 2.5 Quantum effects and nociception specifically

**This is the most important negative finding in the brief, so state it plainly: there is essentially no literature.**

A systematic sweep of PubMed and Europe PMC for (quantum OR "radical pair") AND (nociception OR nociceptor OR pain OR analgesia) returns, on inspection:

1. **Quantum dots**, semiconductor nanocrystals used to build artificial nociceptor-mimicking optoelectronic devices. Materials science, no quantum biology.
2. **Quantum chemistry**, DFT calculations for analgesic drug design. Ordinary computational chemistry.
3. **Trade names**, including a "quantum consciousness index" and "quantum noxious index" on a proprietary depth-of-anaesthesia monitor. No physics involved.
4. **Zero papers** demonstrating coherence, entanglement, spin selectivity or tunnelling in pain signalling.

The closest three things that exist, and their honest weight:

- **Prato FS. "Non-thermal extremely low frequency magnetic field effects on opioid related behaviors: Snails to humans, mechanisms to therapy." *Bioelectromagnetics* 36:333-348 (2015). doi:10.1002/bem.21918. PMID 25962809.** Thirty years of work (Prato, Kavaliers, from 1984) showing ELF magnetic fields modulate opioid-mediated antinociception in *Cepaea nemoralis* and in mice, with amplitude and frequency dependence and light dependence, which Prato explicitly connects to the radical pair literature. Real, replicated within lab, peer-reviewed magnetobiology **on a pain endpoint**. Also small-effect, largely confined to a few groups, and mechanistically unresolved.
- **Nair PS, Zadeh-Haghighi H, Simon C. "Radical pair model for magnetic field effects on NMDA receptor activity." *Sci Rep* 14:3628 (2024). doi:10.1038/s41598-024-54343-y. PMID 38351304.** Pure theory. NMDA receptors are central to windup and central sensitisation, so this is the nearest formal bridge to pain that exists. **Caveat with teeth:** the Simon group has published radical-pair models for xenon anaesthesia, lithium, hypomagnetic neurogenesis, microtubule reorganisation, planarian regeneration, the circadian clock and now NMDA. **A model class that explains everything constrains nothing.** Hypothesis generation only.
- **Sonkodi B. *Int J Mol Sci* 26:1246 (2025). doi:10.3390/ijms26031246. PMID 39941012.** A single-author series proposing quantum-mechanical proton-coupled signalling at Piezo2, invoking quantum gravity. **No experimental test of any quantum claim.** This is the cautionary example: it is the only substantial "quantum and pain" body of work in the indexed literature and it is speculation.

---

## TIER 3: The defensible ground. Quantum technology applied to neuroscience.

Real engineering with real numbers. **This is where a serious programme should live**, and it is Branch B.

### 3.1 Quantum sensing of neural activity

#### What Barry et al. 2016 actually achieved

> Barry JF, Turner MJ, Schloss JM, Glenn DR, Song Y, Lukin MD, Park H, Walsworth RL. *PNAS* 113:14133-14138 (2016). doi:10.1073/pnas.1601513113. PMID 27911765. **Note the published correction, *PNAS* 114:E6730 (2017), doi:10.1073/pnas.1712523114**, a units fix on the volume-normalised sensitivity.

This paper is routinely cited as "single-neuron magnetic recording" and it is worth reading the numbers before relying on it.

| Quantity | Value |
|---|---|
| Broadband sensitivity | **15 ± 1 pT/√Hz** |
| Sensing volume | 13 × 200 × 2000 µm³, about 5 × 10⁻⁶ cm³ |
| Temporal resolution | about 32 µs |
| Excised fanworm axon signal | **4.1 ± 0.2 nT**, at 150 averages |
| Squid axon | 375 averages |
| **Live intact worm** | about **1 nT**, at **1,650 averages**, standoff about **1.2 mm** |
| Distance from the spin-projection limit | achieved sensitivity is about **3,000 times worse** |

**The honest reading.** This is a **4.1 nT** signal, four orders of magnitude above MEG, from an invertebrate giant axon roughly 500 µm across, at sub-millimetre standoff, still needing 150 to 1,650 averages. The paper is explicit that individual **mammalian** neurons are expected to give about 1 nT *at the NV layer*, and that real-time single-event detection there is future work.

#### The state of NV-diamond, and the band that matters

| Regime | Best reported | Citation |
|---|---|---|
| **DC and low frequency, the biomagnetic band** | **0.9 pT/√Hz** | Wolf et al., *PRX* 5:041001 (2015), doi:10.1103/PhysRevX.5.041001 (erratum *PRX* 13:029903, 2023); Fescenko et al., *Phys Rev Research* 2:023394 (2020) |
| RF, around 350 kHz | **about 70 fT/√Hz** | Silani et al., *Sci Adv* 9:eadh3189 (2023), doi:10.1126/sciadv.adh3189 |

**The only femtotesla NV result is at 350 kHz**, two to three orders of magnitude above the 1 Hz to 5 kHz band where neural signals live. In the band that matters, NV is stuck at about **1 pT/√Hz**, roughly **300 times worse than a commercial OPM** and 500 times worse than a MEG SQUID.

Subsequent NV work moved to tissue rather than single neurons, and there have been **no new single-neuron NV recordings since 2016**:

- Webb JL, Troise L, et al. *Sci Rep* 11:2412 (2021). doi:10.1038/s41598-021-81828-x. PMID 33510264. 50 pT/√Hz, optogenetically activated mouse muscle.
- **Hansen NW, Webb JL, Troise L, et al., Huck A, Andersen UL. *Sci Rep* 13:12407 (2023). doi:10.1038/s41598-023-39539-y. PMID 37524855.** Mouse corpus callosum. 50 pT/√Hz, 60 µm standoff, **minimum 300 averages to see anything, 28,800 trials per slice over 4 hours, on 3 slices.** The authors state plainly that "our sensitivity is as yet insufficient" for single-trial readout.
- Omar et al., arXiv:2601.18843 (2026). Human cardiac measurements at 6-26 pT/√Hz, averaged over **hundreds to thousands of heartbeats** to recover a magnetocardiogram that SQUID and OPM systems get in **one beat**.

**Standoff is the quiet killer.** Every NV neural result is at 60 µm to 1.2 mm. Field falls as 1/r² to 1/r³, so NV's spatial resolution advantage evaporates the moment you move off the tissue surface, which is exactly what non-invasive human recording requires.

#### OPM-MEG, and why it wins

> Boto E, Holmes N, Leggett J, et al., Bowtell R, Brookes MJ. *Nature* 555:657-661 (2018). doi:10.1038/nature26147. PMID 29562238.

**The value proposition in one line: a 13 times worse sensor, 4 times better signal, because it sits on the scalp.** Measured side by side, SQUID gives 3.36 ± 1.08 fT/√Hz and a helium-4 OPM gives 42.65 ± 2.97 fT/√Hz, and yet the OPM records **3.8 to 4.5 times stronger evoked fields** (Gutteling et al., *Sensors* 23:2801 (2023), doi:10.3390/s23052801). Commercial alkali OPMs reach 7-15 fT/√Hz. Brookes et al., *Trends Neurosci* 45:621-634 (2022), doi:10.1016/j.tins.2022.05.008, quantify the proximity gain as four- to fivefold.

**The benefit is geometric, not quantum-mechanical.** That is worth saying inside a programme with "quantum" in one of its branches.

Scale and clinical progress are real: 128-channel (Alem et al., *Front Neurosci* 17:1190310, 2023) and 192-channel systems (Rier et al., *eLife* 13:e94561, 2024); and in epilepsy, **68 patients with 90.0% concordance with the intracranially defined epileptogenic zone** (Shen et al., *Epilepsia* 67(8), 2026, doi:10.1002/epi.70273).

#### Magnetoneurography: the number is bimodal, and conflating the two modes is the field's commonest error

**This correction matters more to this programme than anything else in Tier 3.**

| Target | Signal | What it takes |
|---|---|---|
| **Superficial peripheral nerve** (median at the wrist, 6.5 mm standoff) | **about 1 pT (1,000 fT)** | 3 OPMs, 3 subjects, no shielded-room heroics |
| **Deep source** (cervical cord, 12-14 mm plus cryostat gap, partially cancelling currents) | **5-50 fT** | 132-channel sub-2 fT/√Hz SQUID array, **1,000 to 8,000 stimulus averages** |

The superficial figure is from **Bu Y, Prince J, ... Lerman I. *Front Physiol* 13:798376 (2022). doi:10.3389/fphys.2022.798376. PMID 35370794**, which recovered median nerve sensory action potentials at around 1 pT, back-calculated nerve current 0.195 µA and conduction velocity 50 m/s, all matching surface electrodes. Follow-up: Bu Y, Burks J, et al. *Commun Biol* 7:893 (2024). doi:10.1038/s42003-024-06435-8. PMID 39075164, tracking vagal and sympathetic compound action potential firing rates against TNF-α in nine subjects.

The deep figure is from **Adachi Y, Kawabata S. *Front Med Technol* 6:1351905 (2024). doi:10.3389/fmedt.2024.1351905. PMID 38690583**, and Sumiya et al. *Sci Rep* 7:2192 (2017). doi:10.1038/s41598-017-02406-8.

**Those are two different problems separated by a factor of about 100 in amplitude.** A programme that quotes the deep number while planning to record a superficial limb nerve has made itself look impossible for no reason. A programme that quotes the superficial number while planning to record the cord has made itself look easy for no reason.

**Two further constraints that a better sensor does not fix.**

*Averaging is set by interference, not by sensor noise.* At 2 fT/√Hz over a 100 Hz to 5 kHz band, single-trial sensor noise is about 140 fT rms, falling to about 2.2 fT after 4,000 averages, which puts a 5-to-1 recovery at about 11 fT and lands squarely in the observed range. But in practice environmental and biological interference (cardiac, muscular, respiratory) sets the floor. **A sensor ten times quieter does not turn magnetospinography into a single-shot measurement, and anyone promising that is selling the wrong bottleneck.**

*Bandwidth is a hard gate.* Peripheral nerve compound action potentials are about 1 ms events, and SQUID magnetospinography accordingly samples at 40 kHz with a 5 kHz analogue band. Commercial alkali OPMs run **150 Hz to about 350 Hz** (QuSpin specified 3-100 Hz; FieldLine closed-loop 350 Hz), and Bu et al. hit exactly this wall with a 500 Hz filter and a 15 ms ringing artefact. **Helium-4 OPMs (DC to 2 kHz, ±250 nT) are the only OPM class that clears the bandwidth bar, and they cost about 13 times in sensitivity.**

#### What this means for Branch B

The defensible target is **non-contact magnetoneurography of a superficial limb nerve**, where the signal is about 1 pT and already demonstrated in humans with three sensors, not the spinal cord, where it is 5-50 fT and interference-limited.

The open question, and it is a real one, is whether **unmyelinated C-fibre traffic** is reachable at all by this route. E-02 §4 records that magnetospinography has **never detected even Aδ fibres**, because conduction velocity dispersion phase-cancels the compound volley. C-fibres conduct ten times slower again. That tension between "superficial nerve magnetometry works" and "the fibres of interest disperse away" is the sharpest unwritten conjecture in this evidence base, and helium-4 OPM bandwidth is the parameter it turns on.

**Within Branch B, the OPM route dominates the NV route by about 300 times in the band that matters, and the helium-4 OPM variant dominates the alkali variant on bandwidth.**

### 3.2 Quantum computing as a chemistry tool

**Only two systems have rigorous fault-tolerant resource estimates, and both are metalloenzyme active sites.**

- Reiher M, Wiebe N, Svore KM, Wecker D, Troyer M. *PNAS* 114:7555-7560 (2017). doi:10.1073/pnas.1619152114. PMID 28674011. Nitrogenase FeMoco. About **10¹⁴ to 10¹⁵ T gates, 111 logical qubits**, and at a 10⁻³ physical error rate **1.8 × 10⁸ physical qubits**. The paper describes this as running "in reasonable time on **small** quantum computers". A small quantum computer here means 180 million physical qubits.
- Goings JJ, White A, Lee J, Tautermann CS, Degroote M, Gidney C, Shiozaki T, Babbush R, Rubin NC. *PNAS* 119:e2203533119 (2022). doi:10.1073/pnas.2203533119. PMID 36095200. Cytochrome P450, up to 63 electrons in 58 orbitals: **8.5 × 10⁹ Toffolis, 2,158 logical qubits, about 4.9 million physical qubits and 135 hours** at 0.1% error. Extrapolating to the full 500-orbital enzyme gives **1.5 × 10¹² Toffolis**, that is years of quantum wall-clock. The paper's *actual* headline result is classical: coupled cluster and DMRG converge acceptably on these spaces, so it puts most of P450 on the classical side of the line.

Nine years of algorithmic work cut the gate count by four to five orders of magnitude (10¹³-10¹⁴ down to about 2.4 × 10⁹ Toffolis) but pushed the **logical qubit count the wrong way, 111 up to 2,100-3,700**, because qubitisation trades ancillas for gates. Nobody has pushed the physical-qubit requirement below about 10⁶ at realistic error rates.

**There are essentially zero credible fault-tolerant estimates for ion channels, membrane proteins, neurotransmitter receptors or binding free energies.** Not few. Zero. Six independent database sweeps returned no qubit, Toffoli or runtime estimate for any of them. The absence is structural rather than accidental: these are 10⁴ to 10⁵ atoms in a lipid bilayer, and the pharmacologically interesting quantities (gating kinetics, conformational free-energy landscapes, binding free energy, permeation selectivity) are **thermodynamic and conformational**, dominated by sampling over 10⁶ to 10⁹ configurations plus solvation and entropy. Phase estimation prices **one energy at one geometry in a fixed active space**, and a single alchemical free-energy calculation needs 10⁴ to 10⁶ of them. Multiply Goings' 135 hours and 4.9 million physical qubits by 10⁴ and the answer is centuries.

**The sceptical anchor:** Lee S, Lee J, Zhai H, Tong Y, Dalzell AM, Kumar A, Helms P, Gray J, Cui ZH, Liu W, Kastoryano M, Babbush R, Preskill J, Reichman DR, Campbell ET, Valeev EF, Lin L, Chan GK. *Nat Commun* 14:1952 (2023). doi:10.1038/s41467-023-37587-6. PMID 37029105. Verbatim: *"evidence for such an exponential advantage across chemical space has yet to be found... it may be prudent to assume exponential speedups are not generically available for this problem."* Note the author list: Google Quantum AI, Caltech, Columbia and Berkeley, saying it about their own field. **No published formal rebuttal or Matters Arising exists.**

Their argument is quantitative and its middle step matters here. Phase estimation costs scale with the inverse of the **overlap** between the preparable initial state and the true ground state, and that overlap **decays exponentially in the number of metal centres**: for FeMoco it is already about 10⁻⁷. Adiabatic state preparation does not rescue it, since with mean-field initialisation the preparation costs more than the algorithm.

**And in 2026 the flagship benchmark fell to a classical computer.** Zhai H, Li C, Zhang X, Li Z, Lee S, Chan GK-L, arXiv:2601.04621. High-order coupled cluster plus DMRG plus extrapolation reach chemical accuracy on the FeMoco model classically, and the accompanying commentary states the Reiher 2017 model was "unrepresentatively easy to solve". `[Preprint; journal publication UNVERIFIED.]` The benchmark that justified a decade of quantum-chemistry resource estimates has been solved classically.

**Hardware reality check.** Google Quantum AI, *Nature* 638:920-926 (2025), doi:10.1038/s41586-024-08449-y, PMID 39653125: Willow, 105 qubits, a distance-7 surface code below threshold, Λ = 2.14, logical error per cycle 0.143%. That is **one** genuinely below-threshold logical qubit. The largest fault-tolerant circuit executed anywhere as of 2026 is about **12 logical qubits and nine logical T gates**. Neutral-atom and trapped-ion platforms show 48 to 94 "logical qubits" under error-**detecting** codes with post-selection, which cannot survive 10⁹ gates because the retention rate dies exponentially with circuit size.

| Axis | Best demonstrated 2026 | Required (cheapest published) | Gap |
|---|---|---|---|
| Logical qubits, genuinely below threshold | **1** | 1,000-3,700 | ~3 orders |
| Logical error per T gate | 2.6 × 10⁻³ | ≲ 10⁻¹⁰ | ~7 orders |
| Physical qubits | 105-448 | 4-5 × 10⁶ | ~4.5 orders |
| T or Toffoli gates in one algorithm | ≤ 9 | ~2 × 10¹⁰ | ~9-10 orders |

An independent check: at Λ = 2.14 per two units of distance, getting from 1.4 × 10⁻³ to 10⁻¹⁰ needs distance about 50, so about 5,000 physical qubits per logical qubit, so about 10⁷ physical qubits for a 2,000-logical-qubit algorithm. That reproduces the published estimates from the hardware side, which means the two are mutually consistent and **the gap is four to seven orders of magnitude**.

**Blunt conclusion for a Nav1.7 or Nav1.8 ligand problem.** A fault-tolerant quantum computer that beats classical methods on a channel-ligand binding free energy is not a 2020s technology and probably not an early-2030s one. Worse, **the bottleneck is not electronic structure at all**: it is conformational sampling, protein flexibility, membrane and solvent entropy, and state-dependent binding. Those are sampling problems, not correlated-electron problems, and quantum computers offer no known advantage on them.

That connects directly to E-03: the Nav1.7 drugs failed on **state dependence**, binding the depolarised conformation of voltage-sensing domain IV while resting-state channels dominate in uninjured tissue. That is precisely a conformational sampling problem. **Anyone promising quantum-computed analgesic design is selling.**

### 3.3 Quantum machine learning for biosignal decoding

**There is no credible advantage claim. State it flatly.**

- **Gupta RS, Wood CE, Engstrom T, Pole JD, Shrapnel S. "Quantum machine learning in digital health." *npj Digit Med* (2025). doi:10.1038/s41746-025-01597-z. PMID 40316703.** 169 eligible studies, 123 excluded for insufficient rigour, only 16 considered realistic operating conditions. Finding: "Performance differentials between quantum and classical algorithms show no consistent trend to support empirical quantum utility in digital health."
- **Bowles J, Ahmed S, Schuld M. arXiv:2403.07059 (2024).** 12 QML models, 6 tasks, 160 datasets: "out-of-the-box classical machine learning models outperform the quantum classifiers", and removing entangling gates did not degrade the top quantum models. Their own survey of 55 papers with "outperform" in the title found that **only 3 (4%)** report a quantum model failing to beat classical, and their simulation shows that selecting the best of 20 quantum models without also selecting the best classical model **reverses the observed ranking**. `[Still an unrefereed preprint; cite as such.]`
- **The one honest head-to-head, and it failed completely.** Cattan, Quemy, Andreev, arXiv:2302.02648 (2023). These are pyRiemann and MOABB authors, so they used the actual state of the art as comparator: a Riemannian tangent-space pipeline on P300 data, against a Qiskit quantum support vector classifier on identical folds. **QSVC training balanced accuracy 83.17%; test balanced accuracy 50.25%; test F1 2.84%.** Balanced accuracy of 50 on a binary task means every epoch was assigned to the same class. The quantum classifier memorised the training set and generalised at exactly chance, while the classical comparators did not. Runtime: about 8 hours per fold simulated, against **under 2 seconds** classical.
- **Thanasilp, Wang, Cerezo, Holmes. *Nat Commun* 15:5200 (2024). doi:10.1038/s41467-024-49287-w.** Quantum kernel values concentrate exponentially with qubit count, so the shot count needed to resolve kernel entries grows exponentially. Any quantum kernel result at 1,024 shots is sitting where estimator noise is comparable to kernel signal, which is one mechanism for the train-83 test-50 collapse above.
- **Gil-Fuster, Eisert, Bravo-Prieto. *Nat Commun* 15:2277 (2024). doi:10.1038/s41467-024-45882-z.** State-of-the-art quantum neural networks **accurately fit random labels**, so a reported high accuracy on a small cohort has no theoretical protection against having memorised.
- **Dequantisation.** Tang E, STOC 2019:217-228, doi:10.1145/3313276.3316310, **arXiv:1807.04271**; and Chia, Gilyén, Li, Lin, Tang, Wang, *JACM* 69(5):1-72 (2022), doi:10.1145/3549524. Applications explicitly dequantised include **support vector machines** and principal component analysis. For a quantum kernel on dimensionally reduced biosignals this is decisive: **any regime in which the quantum method would be exponentially fast is a regime in which a classical sampling algorithm is also exponentially fast.**

Published EEG QML papers reporting near-perfect accuracy run on simulators, omit dataset sizes and classical baselines, and show the classic signature of leakage or overfitting. **Zero of them produced a classification result on real quantum hardware**, a finding independently confirmed by a 2026 PRISMA review of 36 studies (Jafari, Tang, Acharya, Li, *Comput Methods Programs Biomed* 286:109565, doi:10.1016/j.cmpb.2026.109565), which reports that evidence "remains preliminary" and calls for "fair classical benchmarking".

**Treat any QML-on-biosignal accuracy above the best published classical result as a methodological error until proven otherwise.**

There is also a structural ceiling worth stating. One four-second 22-channel trial at 250 Hz is 22,000 real numbers. Under the angle encoding these papers actually use, that is 22,000 qubits; under amplitude encoding it is 15 qubits but generic state preparation costs O(2ⁿ) gates. The largest circuit simulated anywhere in the 160-dataset benchmark above was **18 qubits**. **This is why every such paper reduces to 3 to 10 dimensions first, and at 3 features logistic regression is a fine model with nothing left for a quantum computer to contribute.** The compression is not a preprocessing detail. It is the experiment.

---

## TIER 4: Excluded, and how to auto-flag it

Excluded categorically: Rife frequency generators and frequency therapy for cancer or infection; bioresonance and electrodermal screening (BICOM, MORA, Vega, Asyra, QXCI/SCIO/EPFX); quantum healing in the Chopra sense; scalar energy, zero-point energy, orgone and torsion-field devices; biofield devices making physical claims; holographic and ionised wristbands; quantum medicine clinics.

**Evidence and enforcement.** Bioresonance in controlled trials: Schöni MH, Nikolaizik WH, Schöni-Affolter F. *Int Arch Allergy Immunol* (1997), PMID 9066509, "no significant additive measurable effect" in paediatric atopic dermatitis and "has no place in the treatment" of it; Wille A. *Forsch Komplementarmed* (1999), PMID 10077720, no improvement in childhood stuttering. Positive trials cluster in a single low-impact journal with small n. **FTC v. QT, Inc., Q-Ray Company**, N.D. Ill. 03-C-3578, 448 F. Supp. 2d 908 (2006), affirmed **512 F.3d 858 (7th Cir., 3 January 2008)**: Q-Ray "ionised" bracelet marketing held deceptive. `[Power Balance ACCC action, FDA action on QXCI/SCIO, and the exact FTC 2022 guidance wording are UNVERIFIED here; verify before citing.]`

The **biofield** literature is worth noting structurally: largely self-referential, published in journals dedicated to the modality, with reviews conceding "little robust evidence of unique physiological changes has emerged" (Baldwin & Hammerschlag, *Explore* 2014, PMID 24767262) while other papers in the same community assert the discipline is viable. **That internal contradiction is itself diagnostic.**

### The physics failure modes, so the exclusion is principled rather than snobbish

1. **Thermal decoherence.** Any claim of macroscopic, long-lived coherence in tissue at 310 K must beat 25 fs. None do.
2. **No-communication theorem.** Entanglement transmits no information. Quantum healing at a distance is excluded by theorem, not by lack of data.
3. **Resonant frequency killing of pathogens.** A cell or virion in water is overdamped at kHz to MHz; Q factors are of order unity. There is no mechanical resonance to exploit.
4. **Observer-effect abuse.** Measurement is decoherence via interaction, not mind.
5. **Scalar and zero-point energy.** Scalar potentials are gauge artefacts; zero-point energy is not extractable. Word-shaped objects, not mechanisms.
6. **Water memory.** Benveniste (1988) failed under blinded conditions; Montagnier's 2011 claim was never independently replicated.

### Machine-checkable tells

Encoded into `pipeline/gates/01-physical-plausibility.md`.

**Lexical**, any two co-occurring: "quantum" adjacent to healing, wellness, frequency, vibration, resonance, energy, field, coherence, entanglement, consciousness, biofield, scalar, zero-point, torsion, orgone, subtle energy, life force, chi, Rife, bioresonance, radionics, "harmonises", "rebalances", "at the cellular level".

**Structural:**

7. A named frequency in Hz asserted to be specific to a disease or organism, with no dispersion relation, no dose, no absorption coefficient.
8. A claimed coherence, entanglement or superposition in tissue with **no stated timescale**, or a stated timescale above about 1 ms with no weak-coupling argument.
9. "Quantum" in the device name but never in the Methods.
10. Simulation or docking reported in language reserved for measurement ("we demonstrate", "we show").
11. A mechanism class that explains an implausibly broad set of unrelated phenomena.
12. Author-group closure: theory, confirming experiment and review all by overlapping authors.
13. Venue dedicated to the modality, or a special issue guest-edited by proponents.
14. Citing Engel 2007 without Duan 2017 or Cao 2020; citing the Tegmark rebuttals without stating the residual orders-of-magnitude gap; citing Turin's olfaction theory without Block 2015.
15. "Clinically proven" with no registered trial identifier.
16. Appeal to suppression, to a lone genius, or to Nobel-laureate authority outside their field.
17. **No stated null result and no stated falsification condition anywhere in the document.**
18. Dose-response absent, or effects claimed independent of distance, amplitude or duration.

---

## Verdict

**"Is there any scientifically defensible route by which quantum-level information manipulation could act on pain signalling?"**

**In the strict sense of coherently controlling a qubit-like degree of freedom to write, read or compute information within nociceptive pathways: no. P(such a route exists and is exploitable) is below 0.1%.** There is no candidate substrate, no demonstrated coherence in neural tissue under operational criteria, no proposed encoding, and no experiment in the entire indexed literature.

**In the weaker and more useful sense that a spin-dependent chemical step, controllable by an applied magnetic field, alters nociceptor excitability: plausible but unproven.**

| Claim | Probability |
|---|---|
| Radical-pair magnetic field effects on some pain-relevant biochemistry are real and reproducible | **25-35%** |
| The observed ELF-MF antinociception is specifically radical-pair rather than other magnetobiology or artefact | **15-25%**, conditional on the above |
| This becomes a clinically useful, mechanistically understood analgesic intervention within ten years | **about 5%** |
| Fisher's nuclear-spin and Posner mechanism operates in the brain as proposed | **3-8%**, trending down |
| Orch-OR is correct in any load-bearing sense | **about 1%** |

### The least-implausible route, stated concretely

Weak, precisely specified magnetic fields modulate the singlet-triplet branching of a radical pair in a flavin-containing or metal-centred enzyme within nociceptive tissue, shifting reactive oxygen species or nitric oxide production, which shifts nociceptor membrane excitability or NMDA-receptor-dependent central sensitisation.

The supporting scaffolding: the radical pair mechanism is established physics with a validated biological instance; three decades of ELF-MF opioid-analgesia phenomenology exist with light dependence and amplitude and frequency structure; **PEMF for chronic low back pain and osteoarthritis shows moderate but heterogeneous clinical effect sizes with no accepted mechanism** (Sun et al., *Clin Rehabil* 2022, PMID 35077249, SMD −1.01 against placebo; Yang et al., *Phys Ther* 2020, PMID 32251502), which is a mechanism-shaped hole; and an explicit radical-pair model of NMDA receptor magnetosensitivity now exists.

### The decisive experiment

Radical-pair mechanisms make a signature prediction no classical mechanism makes: a **magnetic isotope effect**. Substituting a zero-spin nucleus for a non-zero-spin one at the radical centre changes hyperfine coupling and therefore singlet yield, **at constant mass and chemistry**, which is exactly what defeats the mass-dependent-transport confound that undermines the lithium work.

Run an ELF-MF or PEMF antinociception assay (von Frey, Hargreaves, or formalin) in animals or cells enriched in ¹³C, ¹⁷O, ²⁵Mg or ⁶⁷Zn against their spinless counterparts. Blinded, pre-registered, mass-matched controls.

**A clean magnetic isotope effect would be the first genuine quantum result in pain biology. A null would close the question honestly. Either outcome is worth more than another decade of modelling papers.**

### Programme guidance

**Build in Tier 3**, where quantum technology measures classical neurons and the physics is unimpeachable. Concretely, that means **optically pumped magnetometry of a superficial limb nerve**, where the signal is about **1 pT at 6.5 mm** and has already been recovered in humans with three sensors, and **not** the spinal cord, where it is 5-50 fT and the averaging requirement is set by biological and environmental interference rather than by sensor noise, so a better sensor does not fix it. Prefer **helium-4 OPMs**, which are the only class whose bandwidth (DC to 2 kHz) clears the roughly 1 ms width of a compound action potential, and accept the roughly 13-fold sensitivity cost. **Do not reach for NV-diamond**: it is about 300 times worse in the band that matters and has produced no new single-neuron recording since 2016.

The live scientific question in this branch is whether **unmyelinated C-fibre traffic is reachable at all** by magnetometry, given that magnetospinography has never detected even Aδ fibres because conduction velocity dispersion phase-cancels the compound volley. That is a conjecture, it turns on OPM bandwidth, and it should be written.

**Fund at most one falsifiable Tier 2 probe:** the magnetic isotope effect described above, or an independent replication of Li et al. 2018.

**Do not fund quantum computation for ligand design.** The gap is four to seven orders of magnitude, there are zero fault-tolerant resource estimates for any ion channel or membrane protein, the bottleneck is conformational sampling rather than electronic structure, and the field's flagship benchmark was solved classically in 2026.

**Do not fund quantum machine learning for biosignal decoding.** There is no demonstrated advantage on real hardware against a strong classical baseline, and the one properly controlled head-to-head found the quantum classifier at exactly chance on held-out data.

Cite Tier 1 accurately, including the walk-backs. Exclude Tier 4 by the checklist, not by taste.
