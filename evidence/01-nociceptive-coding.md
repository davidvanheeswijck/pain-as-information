# E-01. How pain information is encoded on nerves

> Literature brief, September 2026. Identifiers were resolved against PubMed
> E-utilities or the publisher record; anything unresolved is marked
> `[UNVERIFIED]`. Quantitative statements that are arithmetic rather than a
> published figure are marked **[DERIVED]**.
>
> Bears on: HC-1 (structure beyond rate), HC-2 (peripheral readability).

---

## 1. The physical substrate: what is actually on the wire

**ESTABLISHED.** Nociceptive information leaves the periphery as all-or-none action potentials on three fibre classes distinguished by diameter and myelination. Conduction velocities: unmyelinated C-fibres ~0.4-1.4 m/s, thinly myelinated Aδ ~5-30 m/s, thickly myelinated Aβ >30 m/s (Dubin & Patapoutian 2010, *J Clin Invest* 120:3760-72, PMID 21041958, doi:10.1172/JCI42843). The existence of a *specifically nociceptive* myelinated afferent, rather than an intensity-graded mechanoreceptor, was established by Burgess & Perl, who recorded 74 fibres conducting 6-37 m/s in cat that fired only to frankly damaging mechanical stimulation (Burgess & Perl 1967, *J Physiol* 190:541-62, PMID 6051786, doi:10.1113/jphysiol.1967.sp008227).

Human C-nociceptors are not one population. Microneurography identifies mechano-heat units (CMH), mechano-only (CM), heat-only (CH) and mechano-insensitive "silent" units (CMiHi) (Schmidt et al. 1995, *J Neurosci* 15:333-41, PMID 7823139, doi:10.1523/JNEUROSCI.15-01-00333.1995). These subtypes are separable on the wire itself by **activity-dependent slowing** of conduction velocity, which is the workhorse classifier in human recordings (Serra, Campero, Ochoa & Bostock 1999, *J Physiol* 515:799-811, PMID 10066906, doi:10.1111/j.1469-7793.1999.799ab.x).

**Firing rates and refractoriness.** The textbook claim that C-nociceptors saturate at 10-30 Hz is wrong as a general statement. Werland et al. showed in pig that polymodal C-nociceptors follow electrical stimulation up to 100 Hz without conduction failure, whereas silent nociceptors cannot follow 5 Hz; NGF sensitisation raises the silent units' maximum following frequency (Werland et al. 2021, *J Physiol* 599:1595-610, PMID 33369733, doi:10.1113/JP280269). **[DERIVED]** A 100 Hz following frequency implies an effective refractory period below 10 ms in polymodal C-fibres. Absolute refractory periods for myelinated afferents (~0.5-1 ms, permitting several hundred Hz) are textbook values with no primary source located `[UNVERIFIED]`.

**Channel capacity.** There is **no published bits-per-second estimate for a single nociceptor axon.** This is a genuine gap, not a search failure. What exists is generic spike-train information theory (Borst & Theunissen 1999, *Nat Neurosci* 2:947-57, PMID 10526332, doi:10.1038/14731), which finds ~1-3 bits per spike for well-characterised sensory neurons.

**[DERIVED]** Using the standard entropy-rate ceiling for a spike train of mean rate *r* and timing resolution Δt, H ≈ r·log₂(e/(r·Δt)):

| Case | Ceiling | Comment |
|---|---|---|
| C-nociceptor, r = 10 Hz, Δt = 5 ms | ~58 bits/s | realistic transmitted rate ~10-30 bits/s |
| C-nociceptor, r = 100 Hz, Δt = 1 ms | ~480 bits/s | almost certainly unattainable: activity-dependent slowing degrades timing precisely when rate is high |
| Aδ, r = 50 Hz, Δt = 1 ms | ~330 bits/s | |

Treat these as order-of-magnitude bounds, not measurements. The honest summary is that a single nociceptor axon is a **low-bandwidth channel, plausibly tens of bits per second**, and that nobody has measured it directly.

---

## 2. Coding schemes

### Labelled line

**CONTESTED, and losing ground.** Craig's strong labelled-line position holds that lamina I receives modality-dedicated inputs conveying thermosensory and nociceptive activity in high-fidelity labelled lines (Craig 2003, *Annu Rev Neurosci* 26:1-30, PMID 12651967, doi:10.1146/annurev.neuro.26.041002.131022). Genetic ablation gave it real support: killing Mrgprd+ unmyelinated afferents in adult mice selectively reduces behavioural sensitivity to noxious mechanical stimuli while sparing heat and cold, and killing TRPV1+ afferents does the converse (Cavanaugh et al. 2009, *PNAS* 106:9075-80, PMID 19451647, doi:10.1073/pnas.0901507106). Transcriptomics is consistent with discrete types: eleven molecularly distinct DRG classes in mouse (Usoskin et al. 2015, *Nat Neurosci* 18:145-53, PMID 25420068, doi:10.1038/nn.3881), with human DRG showing broadly conserved architecture but divergent nociceptor subsets and sex differences (Tavares-Ferreira et al. 2022, *Sci Transl Med* 14:eabj8186, PMID 35171654, doi:10.1126/scitranslmed.abj8186).

### Population and combinatorial

**ESTABLISHED as the current consensus direction.** Ma argued that labelled lines exist but "meet and talk", with percepts arising combinatorially (Ma 2010, *J Clin Invest* 120:3773-8, PMID 21041959, doi:10.1172/JCI43426). The decisive recent evidence is Ghitani et al., who combined in vivo calcium imaging of trigeminal neurons with post-hoc multiplexed in situ hybridisation in 1,588 neurons across 15 mice, matching function to ten transcriptomic classes. **All C-nociceptor classes were broadly tuned with overlapping but distinct response profiles**, explicitly analogised to cone photoreceptors in colour vision. Peptidergic neurons, long treated as *the* heat line, were only ~25% of heat-responsive cells (Ghitani et al. 2025, *Nature* 642:1016-23, PMID 40269164, doi:10.1038/s41586-025-08875-6). This is the strongest single piece of evidence that quality is not read off a dedicated wire.

### Rate coding

**ESTABLISHED for intensity.** Nociceptor discharge rate tracks stimulus intensity and correlates with human psychophysical magnitude estimates for tonic mechanical pain (Andrew & Greenspan 1999, *J Neurophysiol* 82:2641, PMID 10561433, doi:10.1152/jn.1999.82.5.2641). Intraneural microstimulation of single identified human C-polymodal nociceptors evokes dull or burning pain projected accurately to that unit's receptive field, and the sensation survives A-fibre block (Ochoa & Torebjörk 1989, *J Physiol* 415:583-99, PMID 2640470, doi:10.1113/jphysiol.1989.sp017737). Stimulating single ultrafast A-fibre high-threshold mechanoreceptors in humans evokes painful percepts, and patients lacking thick myelinated fibres show impaired graded mechanical pain judgements (Nagi et al. 2019, *Sci Adv* 5:eaaw1297, PMID 31281886, doi:10.1126/sciadv.aaw1297).

### Temporal and burst pattern coding

**SPECULATIVE, thinly evidenced, and the most directly relevant to this programme.** The best direct test located is Cho et al., who recorded ex vivo from mouse saphenous and sural C-fibres under KCl, GABA and capsaicin. Spike count and instantaneous frequency did **not** separate GABA from KCl responses (both ~1.5 Hz versus capsaicin's 17.5 Hz), but a "spikelet" analysis over three consecutive spikes, parameterised by temporal span and inter-spike-interval symmetry, classified the three chemicals at **79.7% accuracy** (chance 33%). Under chronic constriction injury the GABA-evoked pattern shifted toward the capsaicin-like pattern, coinciding with pain behaviour (Cho et al. 2016, *Front Comput Neurosci* 10:118, doi:10.3389/fncom.2016.00118, PMID 27917120).

**[DERIVED]** 79.7% three-way accuracy corresponds to roughly 0.8-0.9 bits of the available 1.58 bits about stimulus identity. That is a real, non-zero, pattern-carried signal, but it is one paper, in one preparation, with chemical rather than natural stimuli, and it has not been replicated in vivo or in human microneurography.

**The honest state:** there is *no* verified demonstration that burst structure in a nociceptor axon distinguishes burning from stabbing from itch. The claim is plausible and partially supported, not established. Prescott, Ma & De Koninck's synthesis is the fair summary: cross-talk between somatosensory labelled lines means the nociceptive system operates under **combinatorial** encoding rules, with pain quality emerging from which populations fire together rather than from a private code on one fibre (Prescott, Ma & De Koninck 2014, *Nat Neurosci* 17:183-91, PMID 24473266, doi:10.1038/nn.3629).

---

## 3. Dorsal horn processing

**ESTABLISHED.** Melzack & Wall proposed that large-diameter input closes a spinal gate by driving an inhibitory interneuron onto projection neurons, while nociceptor input opens it (Melzack & Wall 1965, *Science* 150:971-9, PMID 5320816, doi:10.1126/science.150.3699.971). The specific 1965 wiring diagram is wrong in detail, but the architectural claim survived: Braz, Solorzano, Wang & Basbaum give the modern circuit-level restatement, in which molecularly defined excitatory and inhibitory interneurons implement gating (Braz et al. 2014, *Neuron* 82:522-36, PMID 24811377, doi:10.1016/j.neuron.2014.01.018).

Todd's anatomy is the reference frame: projection neurons concentrate in lamina I and are scattered in III-VI, ~80% of lamina I projection cells express NK1R, and inputs are processed through defined excitatory and inhibitory interneuron populations before ascending (Todd 2010, *Nat Rev Neurosci* 11:823-36, PMID 21068766, doi:10.1038/nrn2947).

**Windup** is frequency-dependent facilitation of dorsal horn discharge to repetitive C-fibre input, first described by Mendell & Wall (1965, *Nature* 206:97-9, PMID 14334366, doi:10.1038/206097a0). It is a short-term, use-dependent amplifier and is distinct from central sensitisation.

**Central sensitisation** was established by Woolf, who showed that a conditioning noxious stimulus produces long-lasting threshold reduction and receptive-field expansion in flexor motoneurons that is generated centrally, not peripherally (Woolf 1983, *Nature* 306:686-8, PMID 6656869, doi:10.1038/306686a0). This is the single most important reason a purely peripheral read of pain is inadequate: the same afferent traffic produces different central output depending on the network's recent history.

---

## 4. Neuropathic pain: what abnormal traffic looks like on the wire

**ESTABLISHED.** Ectopic impulses originate not only from injured axon tips but from the DRG somata themselves: in 2,731 intact or acutely sectioned myelinated fibres, 4.75% carried DRG-generated impulses, rising to 8.6% in 2,555 axons sectioned 2-109 days earlier (Wall & Devor 1983, *Pain* 17:321-39, PMID 6664680, doi:10.1016/0304-3959(83)90164-1).

**Human microneurography is the key evidence.** Serra et al. recorded from patients and five rat neuropathy models and found spontaneous activity in mechano-insensitive C-nociceptors in 59.5% of units in focal traumatic injury models, 18.6% in polyneuropathy models and 33.3% in patients (Serra et al. 2012, *Pain* 153:42-55, PMID 21993185, doi:10.1016/j.pain.2011.08.015). Kleggetveit, Namer, Schmidt, Schmelz and colleagues showed that C-nociceptor spontaneous activity is significantly higher in *painful* than *painless* polyneuropathy, which is the closest thing in the field to a peripheral correlate of ongoing pain (Kleggetveit et al. 2012, *Pain* 153:2040-7, PMID 22986070, doi:10.1016/j.pain.2012.05.017). The same signature appears in fibromyalgia: silent nociceptors were abnormal in 76.6% of patients, with spontaneous activity in 31% of silent units versus 2.2% in controls, and unusually high activity-dependent slowing as a possible distinguishing feature (Serra et al. 2014, *Ann Neurol* 75:196-208, PMID 24243538, doi:10.1002/ana.24065).

So: **abnormal traffic looks like ongoing, irregular, low-rate discharge in units that should be silent, plus altered activity-dependent conduction-velocity signatures.** That is a rate-and-provenance abnormality, not an exotic waveform.

**Molecular substrate.** Nav1.8 (SCN10A) carries the slow TTX-resistant current in nociceptors and its deletion raises C-fibre electrical activation thresholds (Akopian et al. 1999, *Nat Neurosci* 2:541-8, PMID 10448219, doi:10.1038/9195). Nav1.7 (SCN9A) sets the human phenotype at both extremes: biallelic nonsense mutations abolish pain entirely (Cox et al. 2006, *Nature* 444:894-8, PMID 17167479, doi:10.1038/nature05413), while gain-of-function mutations cause paroxysmal extreme pain disorder (Fertleman et al. 2006, *Neuron* 52:767-74, PMID 17145499, doi:10.1016/j.neuron.2006.10.006). Nav1.9 (SCN11A) is the counterintuitive case: a *de novo* **gain**-of-function mutation causes loss of pain perception, because sustained depolarisation impairs AP generation (Leipold et al. 2013, *Nat Genet* 45:1399-404, PMID 24036948, doi:10.1038/ng.2767). HCN2 is required for the cAMP-driven component of nociceptor firing; nociceptor-specific HCN2 deletion leaves normal thresholds but abolishes inflammatory heat hyperalgesia (Emery et al. 2011, *Science* 333:1462-6, PMID 21903816, doi:10.1126/science.1206243), extended to diabetic neuropathy models in *Sci Transl Med* (doi:10.1126/scitranslmed.aam6072, PMID 28954930).

**Ephaptic and non-ephaptic crosstalk. CONTESTED in magnitude.** Stable ephaptic interaction between injured axon pairs after neuroma, suture or crush was described by Seltzer & Devor (1979, *Neurology* 29:1061, PMID 224343, doi:10.1212/WNL.29.7.1061). Non-ephaptic, chemically mediated cross-excitation in the DRG is better documented: A-neuron firing depolarises ~90% of neighbouring passive C-neurons and raises their firing probability (Amir & Devor 2000, *Neuroscience* 95:189-95, PMID 10619475, doi:10.1016/s0306-4522(99)00388-7). In vivo imaging of >1,600 neurons per DRG showed injury-induced **coupled activation** of adjacent neurons via upregulated satellite-glial gap junctions; blocking gap junctions reduced both coupling and mechanical hyperalgesia (Kim et al. 2016, *Neuron* 91:1085-96, PMID 27568517, doi:10.1016/j.neuron.2016.07.044).

This matters enormously for any decoding programme: **after injury, the DRG stops being a bundle of independent channels.**

**Why single-target drugs keep failing.** Ratté, Zhu, Lee & Prescott showed that neuropathic hyperexcitability arises when molecular pathologies push spike-initiation dynamics past a tipping point (criticality), and that *several different* pathologies each independently suffice (degeneracy), so no single one is necessary (Ratté et al. 2014, *eLife* 3:e02370, PMID 24692450, doi:10.7554/eLife.02370).

---

## 5. Allodynia: how Aβ touch comes to be read as pain

**ESTABLISHED that this is central, not peripheral.** The dominant mechanism is loss of spinal inhibition that normally prevents Aβ input reaching the nociceptive output pathway.

- **Anion-gradient collapse.** Peripheral nerve injury causes a trans-synaptic shift in the anion reversal potential of lamina I neurons, so GABA_A and glycine receptor activation becomes weakly inhibitory or even excitatory (Coull et al. 2003, *Nature* 424:938-42, PMID 12931188, doi:10.1038/nature01868). The upstream driver is BDNF released from activated microglia acting via TrkB to downregulate KCC2 (Coull et al. 2005, *Nature* 438:1017-21, PMID 16355225, doi:10.1038/nature04223).
- **The circuit that gets uncovered.** PKCγ+ excitatory interneurons at the lamina II inner border receive direct Aβ input and are normally held in check by feed-forward glycinergic inhibition; removing that inhibition lets Aβ input drive the nociceptive pathway (Lu et al. 2013, *J Clin Invest* 123:4050-62, PMID 23979158, doi:10.1172/JCI70026).
- **Genetic dissection.** Somatostatin+ excitatory neurons are required to transmit mechanical pain, and dynorphin+ inhibitory neurons are the gate preventing Aβ fibres from activating them (Duan et al. 2014, *Cell* 159:1417-32, PMID 25467445, doi:10.1016/j.cell.2014.11.003). A parallel deep-to-superficial route runs through transiently VGLUT3-expressing deep dorsal horn neurons onto lamina II calretinin neurons and up to lamina I projection neurons (Peirs et al. 2015, *Neuron* 87:797-812, PMID 26291162, doi:10.1016/j.neuron.2015.07.029).

**Important nuance from 2025:** Ghitani et al. found that inflammation left nociceptor *mechanical* responses minimally affected while inducing long-lasting spontaneous activity in specific classes, suggesting that tactile allodynia arises from **coincidence** of normal touch input with touch-independent ongoing nociceptor firing, rather than from sensitised peripheral mechanoreception (PMID 40269164). This is a coincidence-detection model, and it is testable.

---

### The temporal-coincidence route already has a name, a measurement and a date

Added 2026-09-02, after a triage gate objected that C-003's "eligibility
window" was renaming an established literature. It was right, and the primary
source is worth recording precisely because it *both* supports the mechanism
and destroys the conjecture's novelty claim.

> **Thompson SW, Woolf CJ, Sivilotti LG. "Small-caliber afferent inputs produce
> a heterosynaptic facilitation of the synaptic responses evoked by primary
> afferent A-fibers in the neonatal rat spinal cord in vitro." *J Neurophysiol*
> 1993;69(6):2116-28. PMID 8350135, doi:10.1152/jn.1993.69.6.2116.**

Conditioning one dorsal root while testing another, in vitro:

- **The selectivity is exactly what a coincidence account predicts.**
  "conditioning at A beta-fiber strength had no effect, whereas A delta- and
  C-fiber strength conditioning were equally effective." And the facilitation
  ran one way only: "Heterosynaptic facilitation of only A beta- or A
  delta-fiber-evoked Test EPSPs was observed, no enhancement of C-fiber
  strength Test EPSPs could be demonstrated."
- **The timescale is seconds to tens of seconds, not milliseconds.** Single
  Aδ/C-strength EPSPs "lasted for 4-6 s"; repeated conditioning summated into a
  cumulative depolarisation that "slowly decayed back to the control Vm over
  tens of seconds"; and the facilitation "decayed after the completion of the
  conditioning stimulus with a time course that was parallel to but not
  superimposable on" that depolarisation.
- Facilitation appeared in **7 of 20** neurons, and tracked the size of the
  cumulative depolarisation (9.1 ± 3.1 mV in facilitating trials against
  3.3 ± 0.5 mV in non-facilitating ones, p<0.05).

`[The exact facilitation decay constant is UNVERIFIED: the abstract truncates
at 400 words and the paper is not open access. The three quoted durations above
are verbatim from the abstract.]`

**Three consequences for this programme.**

1. **C-fibre activity gating Aβ input is a real, measured, thirty-year-old
   phenomenon.** Any conjecture proposing it as new is renaming it.
2. **Its timescale is seconds to tens of seconds.** A proposal of "a few
   hundred milliseconds" is wrong by one to two orders of magnitude, and even
   1-10 s sits at the low end of the measured range.
3. **The control a conjecture would design has already been run.** Aβ-strength
   conditioning produced no facilitation, which is precisely the
   adaptation-versus-mechanism control, and it passed in 1993.

**What is still genuinely open** is not whether this facilitation exists but
whether it is *necessary* for established allodynia and *trial-by-trial coupled
to it under natural, unstimulated conditions*, as opposed to being a real
phenomenon that is not what maintains the disease. That is a necessity
question, and it needs spontaneous activity silenced rather than artificial
bursts delivered. Note the caveat that this preparation is **neonatal rat
in vitro**, so its transfer to established adult neuropathic allodynia is an
assumption rather than a finding.

### The strongest counterweight to the central-discrimination account, and it is human

Added 2026-09-02. This section exists because the programme spent an evidence
base concluding that HC-2 was its weakest commitment, and then found a human
experiment pointing the other way.

> **Haroutounian S, Nikolajsen L, Bendtsen TF, Finnerup NB, Kristensen AD,
> Hasselstrøm JB, Jensen TS. "Primary afferent input critical for maintaining
> spontaneous pain in peripheral neuropathy." *Pain* 2014;155:1272-9.
> PMID 24704366, doi:10.1016/j.pain.2014.03.022.**

14 patients, 7 with unilateral foot pain from peripheral nerve injury and 7
with distal polyneuropathy. Ultrasound-guided peripheral nerve block and
intravenous lidocaine, randomised order, with full quantitative sensory
testing.

- "The peripheral nerve block resulted in a **complete abolition of ipsilateral
  pain within 10 min (median) in all patients**, with lidocaine plasma
  concentrations being too low to account for a systemic effect of the drug."
- Intravenous lidocaine reduced spontaneous pain by only **45.5% (±31.7%)**,
  which is the control that makes the block result interpretable.
- "the improvement in evoked hypersensitivity was **not related** to the effect
  of the drug on spontaneous pain intensity" — so spontaneous pain and evoked
  hypersensitivity are dissociable and should not be treated as one outcome.
- Conclusion: "regardless of the individual somatosensory phenotype and **signs
  of central sensitization, primary afferent input is critical for maintaining
  neuropathic pain** in peripheral nerve injury and distal polyneuropathy."

**How this changes the reading of §5 and §6.** It does not contradict the
mechanism described there. Allodynia's discrimination really is made centrally,
and the Aβ traffic that hurts really is indistinguishable from touch. What it
contradicts is the *practical inference* the programme had been drawing from
that: that because the discrimination is central, peripheral intervention is
aimed at the wrong level. In these patients the central changes were present
and demonstrable, and removing the peripheral input removed the pain anyway.
**Central sensitisation behaved as a gain applied to an input, not as a
generator.**

**What it does not establish.** The study contains no CRPS patients. The
generalisation to CRPS is currently carried by a narrative review, Baron, Hans
& Dickenson, *Ann Neurol* 2013;74:630-6, PMID 24018757, which states that "In
postherpetic neuralgia and complex regional pain syndrome, for example, these
symptoms are maintained and modulated by peripheral nociceptive input", plus a
single case report in which a block abolished both spontaneous pain and
allodynia in one CRPS patient (Kato et al., *Pain Med* 2013;14:293-6,
PMID 23198747). Assertion by authoritative people and n=1 are not a trial. That
gap is now filed as C-009.

**A methodological note for this programme.** A peripheral nerve block cannot
be blinded, which is why the intravenous arm at matched plasma concentration is
the load-bearing control rather than a placebo. Any future design here inherits
that constraint.

## 6. The critical question: is there a peripherally decodable pain code?

**Honest reading: partially, and much less than the programme would want.**

### What IS peripherally readable (ESTABLISHED)

1. **Which fibre class fired**, from conduction velocity, and **which C-subtype**, from activity-dependent slowing (Serra et al. 1999, PMID 10066906).
2. **Stimulus intensity**, from rate (Andrew & Greenspan 1999, PMID 10561433).
3. **Pathological ongoing activity in units that should be silent**, which statistically separates painful from painless neuropathy at the group level (Kleggetveit et al. 2012, PMID 22986070; Serra et al. 2014, PMID 24243538).
4. **Causal sufficiency**: stimulating single identified C-nociceptors or A-HTMRs evokes pain (PMID 2640470; PMID 31281886). A nociceptor axon is therefore a genuine "pain-capable" line, even if not a "pain-labelled" one.

### Arguments AGAINST a peripherally-readable pain code

These are strong and the programme should take them seriously.

1. **Broad tuning kills the quality code.** All C-nociceptor classes are broadly and overlappingly tuned; quality must be read from the *relative* activity across classes, which a single axon cannot express (Ghitani et al. 2025, PMID 40269164).
2. **Combinatorial cross-talk is the rule.** Prescott, Ma & De Koninck's conclusion is that labelled lines meet and mix; the peripheral signal is an ingredient, not a message (PMID 24473266).
3. **The same input maps to different output.** Windup (PMID 14334366) and central sensitisation (PMID 6656869) mean identical afferent traffic produces different percepts depending on spinal state. Any peripheral decoder is therefore state-blind by construction.
4. **Allodynia is the clean counterexample.** In allodynia the painful percept is carried on Aβ fibres whose traffic is *indistinguishable from normal touch*. The pathology is entirely in the dorsal horn (PMID 12931188; PMID 16355225; PMID 25467445). No peripheral decoder can succeed here in principle.
5. **Dissociation runs both ways.** Nociceptor activity without pain, and pain without nociceptor activity, both occur. Nav1.9 gain-of-function producing *analgesia* (PMID 24036948) shows that more depolarisation can mean less signal, breaking any monotonic rate-to-pain mapping.
6. **After injury the channels are not independent.** Gap-junction-mediated coupled activation (PMID 27568517) and DRG cross-excitation (PMID 10619475) mean the "population vector" you would try to decode is partly an artefact of glial coupling.
7. **Even central signals are not pain-specific.** Iannetti & Mouraux showed that most macroscopically measurable cortical response to transient nociceptive stimulation is not specific to nociception (2010, *Exp Brain Res* 205:1-12, PMID 20607220, doi:10.1007/s00221-010-2340-1). If the cortex does not give a specific readout, the axon will not either.

### Verdict

There is a **detectable abnormality signature** in nociceptive traffic (ongoing activity in silent nociceptors, altered activity-dependent slowing) that is manipulable and clinically meaningful. There is **weak, single-study evidence** for a temporal-pattern code carrying stimulus-identity information (~0.8-0.9 bits, Cho et al. 2016). There is **no evidence** for a peripherally-readable code distinguishing pain *qualities*, and there are principled reasons (allodynia, central sensitisation, broad tuning) to expect that discrimination is substantially central.

A programme betting on peripheral decoding should target **(a)** ongoing-activity detection as a biomarker and **(b)** peripheral *manipulation*, which is well supported. It should not assume a rich readable semantics on the axon.

---

## Five most important open problems, and who is working on them

1. **Measure the actual information rate of a nociceptor axon in bits/s, and how much of it is timing-carried.** No published estimate exists. Requires simultaneous natural stimulation and long single-unit records with stimulus reconstruction. *Groups positioned to do it:* Prescott lab (SickKids Toronto, spike-initiation dynamics and information transfer), Schmelz & Rukwied (Heidelberg and Mannheim, pig and human C-fibre following frequency), Namer (Erlangen and Aachen, human microneurography), Bostock (UCL, axonal excitability quantification).

2. **Replicate and extend the temporal-pattern claim in vivo and in humans.** Does burst structure carry quality information beyond rate under natural stimuli? *Groups:* Nagi, Olausson and Ackerley (Linköping, Gothenburg, Marseille), Jung lab (Hanyang, originators of the spikelet analysis) `[group activity UNVERIFIED]`, Chesler lab (NIH NCCIH, population imaging).

3. **Resolve labelled-line versus distributed coding now that broad tuning is established.** What is the minimal population read-out that predicts percept? *Groups:* Chesler and von Buchholtz (NIH), Ma lab (Dana-Farber Harvard), Basbaum lab (UCSF), Patapoutian lab (Scripps), Ernfors lab (Karolinska).

4. **Turn nociceptor ongoing activity into a validated, individual-level biomarker and trial endpoint.** Current evidence is group-level. *Groups:* Serra (Barcelona and King's College Hospital), Bostock (UCL), Namer and Schmelz, Jørum and Kleggetveit (Oslo), Bennett lab (Oxford, deep phenotyping).

5. **Determine whether peripheral intervention can ever be sufficient once central disinhibition is installed** (KCC2 collapse, PKCγ and SOM circuit unmasking), and whether degeneracy dooms single-channel drugs. *Groups:* De Koninck lab (Laval), Coull (Laval), Todd lab (Glasgow), Zeilhofer lab (Zurich), Seal lab and Ross lab (Pittsburgh), Goulding lab (Salk), Waxman lab (Yale), Wood lab (UCL), Price lab (UT Dallas), Prescott lab.

---

## Verification notes

> **Update 2026-09-01.** The Borst & Theunissen identifier, previously `[UNVERIFIED]`, was resolved while checking a downstream conjecture: PMID 10526332, doi:10.1038/14731, both confirmed against Crossref and PubMed. One fewer unverified reference in this brief.

All PMIDs and DOIs above were resolved against PubMed E-utilities except where marked. Specifically unverified: Cho et al. 2016 PMID (DOI and full text confirmed at frontiersin.org); Emery et al. HCN2 diabetic-neuropathy *Sci Transl Med* PMID (DOI confirmed at science.org); myelinated-fibre absolute refractory period figures (textbook value, no primary source located).

Two PMIDs initially guessed during preparation (5828044, 24559671) resolved to unrelated papers and were corrected to 14334366 and 24811377. That is the reason `tools/verify-citations.py` exists and runs in CI: PMIDs must never be inferred.
