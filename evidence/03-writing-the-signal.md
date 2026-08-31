# E-03. Writing to, tuning and selectively blocking nerve signals

> Literature brief, 1 September 2026. All citations resolved against NCBI
> PubMed E-utilities (PMID plus DOI plus journal, volume and pages verified
> against the retrieved record), the openFDA drug database, and the
> ClinicalTrials.gov v2 API. Nothing here is cited from memory. Items that could
> not be confirmed are marked `[UNVERIFIED]`.
>
> Bears on: HC-1 (structure beyond rate), HC-3 (structure-targeted beats
> channel destruction), HC-4 (realisable transducer), PB-4 (frequency effects
> are mechanistic, not dose).

---

## Bottom line

Frequency-dependent and pattern-dependent neuromodulation is **physically real and mechanistically demonstrable at the level of single axons and ganglia**. It is **not yet demonstrated to be the operative mechanism of any approved clinical device for pain**. The gap between those two sentences is the whole opportunity, and the whole risk.

The clinical waveform literature is dominated by unblinded, industry-sponsored comparative-effectiveness trials. When blinding is tightened, the frequency-specific effect tends to disappear while the stimulation-versus-nothing effect often survives. Meanwhile the cleanest evidence of genuine frequency selectivity comes from preclinical single-fibre work that has never been commercialised.

---

## 1. Spinal cord stimulation waveform science

### The claims

| Paradigm | Anchor trial | Design quality |
|---|---|---|
| Tonic 40-60 Hz, paraesthesia-based | 1967 onward | Never placebo-tested until recently |
| 10 kHz (Nevro Senza) | Kapural et al., *Anesthesiology* 2015;123(4):851-60. PMID 26218762, doi:10.1097/ALN.0000000000000774 | **Unblindable by construction**, industry-sponsored |
| Burst (De Ridder) | De Ridder et al., *Neurosurgery* 2010;66(5):986-90. PMID 20404705; SUNBURST: Deer et al., *Neuromodulation* 2018;21(1):56-66. PMID 28961366 | n=12 open-label; SUNBURST crossover, industry |
| Differential Target Multiplexed | Fishman et al., *Pain Pract* 2021;21(8):912-23. PMID 34363307, doi:10.1111/papr.13066 | **Open-label**, Medtronic-funded, the DTM inventor is an author and CEO of the licensor |

SENZA-RCT reported 84.5% back-pain responders on 10 kHz versus 43.8% on tonic at 3 months (relative ratio 1.9, 95% CI 1.4-2.5), sustained at 12 and 24 months (PMID 26218762; Kapural et al., *Neurosurgery* 2016;79(5):667-77, PMID 27584814). DTM reported 80.1% versus 51.2% responders at 3 months (PMID 34363307). Both are large effects. **Neither trial could blind patients**, because paraesthesia versus no paraesthesia is self-evident to the participant, and both compared an actively optimised novel arm against a legacy arm.

### The decisive negative: PROCO

> **Thomson SJ et al. "Effects of Rate on Analgesia in Kilohertz Frequency Spinal Cord Stimulation: Results of the PROCO Randomized Controlled Trial." *Neuromodulation* 2018;21(1):67-76. PMID 29220121, doi:10.1111/ner.12746.**

Multicentre, double-blind, crossover. Patients had the 10 kHz "sweet spot" located over eight weeks, then received 1, 4, 7 and 10 kHz at that same location in randomised order, four weeks each, with pulse width and amplitude titrated at each frequency. **All frequencies gave equivalent analgesia**, and 1 kHz did it with 60-70% less charge.

This is Level I evidence that within 1-10 kHz, frequency is not the active variable once electrode position and charge delivery are optimised. It is the single strongest argument that kilohertz SCS is dosing, not mechanism, and it bears directly on PB-4.

### Sham-controlled trials

- **Perruchoud C et al., *Neuromodulation* 2013;16(4):363-9. PMID 23425338.** First double-blind sham-controlled SCS trial. HF versus sham, n=33 completers. Responders 42.4% versus 30.3%, p=0.30. A highly significant **period effect** (p=0.006) meant order in the sequence, not treatment, predicted response.
- **Al-Kaisy A et al., *Neuromodulation* 2018;21(5):457-65. PMID 29608229.** Sham, 1200 Hz, 3030 Hz and 5882 Hz, four-phase crossover, n=24. **Sham reduced pain by 2.92 cm on a 10 cm VAS and was statistically indistinguishable from 1200 Hz and 3030 Hz.** Only 5882 Hz beat sham (p=0.002). Two co-authors were Medtronic Clinical Research employees. An awkward result for both camps: a large placebo response *and* a non-monotonic frequency effect that a pure dose account does not easily explain.
- **Hara S et al., *JAMA* 2022;328(15):1506-14. PMID 36255427, doi:10.1001/jama.2022.18231.** Placebo-controlled crossover of **burst** stimulation, n=50, four 3-month periods. ODI change −10.6 with burst versus −9.3 with placebo, difference **−1.3 points (95% CI −3.9 to 1.3), p=0.32**, against a 10-point minimum clinically important difference. No secondary outcome differed. 18% had adverse events, 8% required surgical revision. **The authors reported no conflicts of interest**, and the trial drew at least nine published rebuttal letters. Six-month follow-up confirmed the null: *JAMA* 2023;329(22):1985-6. PMID 37314281.
- **Gulisano HA et al., *Eur J Pain* 2024;28(9):1627-39. PMID 38988274.** 1000 Hz paraesthesia-free SCS versus sham in chronic pancreatitis, n=16. NRS 4.2 versus 4.3. Null on every outcome. The open-label extension of the same patients showed NRS falling from 5.2 to 2.9 at six months (p=0.001).

**The same patients, the same device: null when blinded, large when open.** That contrast is the most instructive single datum in this literature, and any conjecture in this programme proposing a waveform effect has to reckon with it.

### The systematic reviews

- **Duarte RV, Nevitt S, McNicol E, Taylor RS, Buchser E, North RB, Eldabe S. *Pain* 2020;161(1):24-35. PMID 31453983.** Eight placebo or sham RCTs. Pooled mean difference **−1.15 points (95% CI −1.75 to −0.55)** on a 10-point scale, below the usual 2-point MCID. The authors distinguish *placebo* controls (device off, procedures differ) from true *sham* (all procedures including device behaviour identical) and find **larger effects in the weaker designs**. North and Eldabe are long-standing SCS proponents, so this is not a hostile review.
- **Traeger AC, Gilbert SE, Harris IA, Maher CG. *Cochrane Database Syst Rev* 2023;3(3):CD014789. PMID 36878313.** 13 studies, 699 participants. **No included study assessed pain at 12 months or beyond.** Conclusion: "Data in this review do not support the use of SCS to manage low back pain outside a clinical trial."
- A 2025 counterweight: **Glinka Przybysz A et al., *Interv Pain Med* 2025;4(3):100635. PMID 40896549.** GRADE moderate-quality evidence that tonic SCS beats conventional medical management for persistent spinal pain syndrome type 2 at six months, while conceding that the only sham-controlled study included did not demonstrate efficacy, and that no included study used high-frequency, closed-loop or multi-waveform SCS.

### Mechanism: is anything actually different?

**For difference.** Lee KY, Bae C, Lee D, Kagan Z, Bradley K, Chung JM, La JH. *Neuroscience* 2020;428:132-9. PMID 31917342. Sub-sensory-threshold **10 kHz, but not 1 kHz or 5 kHz**, selectively activated inhibitory interneurons in rat superficial dorsal horn. A genuine frequency-specific, non-monotonic neuronal effect. Caveat: Bradley and Kagan were Nevro-affiliated. De Ridder's EEG work (*Neuromodulation* 2016;19(1):47-59, PMID 26586145; and 2026, doi:10.1016/j.neurom.2026.05.014, PMID 42536009, n=10, open, De Ridder holds the BurstDR IP) argues burst engages a medial "suffering" pathway that tonic does not. The 2026 paper actually **narrows** the claim: burst and 10 kHz share pregenual ACC beta activation, and their direct comparison on back pain was not significant.

**Against difference.** Lempka SF, McIntyre CC, Kilgore KL, Machado AG. *Anesthesiology* 2015;122(6):1362-76. PMID 25822589. Finite-element plus cable modelling: at clinical 10 kHz amplitudes (0.5-5 mA), direct excitation of dorsal column or dorsal root fibres requires amplitudes at or above the clinical ceiling, and conduction block is only reachable with an unusually thin dorsal CSF layer. Conclusion: clinical kHz SCS probably works through neither direct activation nor conduction block of those fibres, so **the field's stated mechanism is unsupported**. Follow-up: Rogers ER, Zander HJ, Lempka SF. *J Pain* 2022;23(3):434-49. PMID 34583022. Modelling conventional, burst and 10 kHz in one framework: local cell thresholds were always above afferent thresholds, and **although absolute thresholds differed between paradigms, the recruitment order was identical**. That is the modelling analogue of PROCO.

---

## 2. KHFAC nerve block, and the fibre-selectivity constraint

Reference review: Kilgore KL, Bhadra N. *Neuromodulation* 2014;17(3):242-54. PMID 23924075. (Both authors hold equity in Neuros Medical.)

Foundational in vivo: Bhadra N, Kilgore KL. *Muscle Nerve* 2005;32(6):782-90. PMID 16124008. Complete, reversible motor block at 10-30 kHz. Block threshold rises **linearly with frequency**. Block has three phases: an **onset response** (a burst of firing as the block engages), asynchronous firing, then steady-state block. The onset response is the central engineering problem and has driven a decade of mitigation work: ramped amplitudes (PMID 18057506), frequency-and-amplitude-transitioned waveforms (PMID 20966536), combined kHz plus DC (PMID 20890673), thermoelectric cooling plus kHz (PMID 20705099).

### The constraint, stated precisely

**For classical KHFAC block, block threshold varies *inversely* with axon diameter.** Bhadra N, Lahowetz EA, Foldes ST, Kilgore KL. *J Comput Neurosci* 2007;22(3):313-26. PMID 17200886: "Block threshold varied inversely with axon diameter." Large myelinated fibres block **first**, at the lowest amplitude. Since large fibres are also recruited first by conventional stimulation, KHFAC does **not** invert recruitment order. It preserves it.

**The consequence for pain: you cannot naively block C-fibres while sparing Aβ.** Raising amplitude until unmyelinated nociceptive C-fibres are blocked guarantees that Aβ touch, proprioception and motor efferents are already fully blocked. Any device claiming selective nociceptor block by brute kilohertz amplitude is claiming the physics backwards.

This is the condition PROGRAMME.md names as a potential killer of HC-3. It holds for classical KHFAC. It does not hold universally, and the escape routes below are where HC-3 survives.

### Three legitimate escape routes

1. **Exploit non-monotonicity in frequency, not amplitude.** Patel YA, Butera RJ. *J Neurophysiol* 2015;113(10):3923-9. PMID 25878155. In rat sciatic and vagus, the fast motor CAP component had a **monotonically increasing** block threshold with frequency while the slow sensory component was **non-monotonic**, so an appropriate frequency-amplitude pair blocks one and spares the other. **But** Peña E, Pelot NA, Grill WM. *Sci Rep* 2021;11(1):5077. PMID 33658552, doi:10.1038/s41598-021-84503-3 showed the non-monotonicity **arises from amplitude- and frequency-dependent charge imbalance** shifting the system between a KHFAC regime and a DC-block regime. Selective small-fibre block at lower thresholds is achievable, but the mechanism is partly DC, not kHz. Honest reading: **selectivity is real, but it is not the clean frequency-tuning story it was sold as.**

2. **Go sub-kilohertz and use activity-dependent block.** Zhang S, Chen L, Ladez SR, Seferge A, Liu J, Feng B. *Front Neurosci* 2024;18:1404903. PMID 39077428, doi:10.3389/fnins.2024.1404903. Ex vivo single-fibre recording from mouse sciatic, saphenous and vagal nerves. Conduction velocity falls progressively until block. **Aδ fibres are efficiently blocked at 50-1000 Hz; C fibres at 10-50 Hz.** NEURON simulation attributes it to disrupted transmembrane Na+/K+ gradients. This is an inverse relationship between fibre conduction velocity and optimal blocking frequency, that is, genuine frequency-tuned fibre selectivity in the therapeutically desirable direction.

3. **Move away from AC entirely.** Charge-balanced DC needs a safe interface: Ackermann DM Jr et al. *J Neurosci Methods* 2011;201(1):173-6. PMID 21276819. The most clinically advanced version: **Jones MG, Rogers ER, Harris JP, Sullivan A, Ackermann DM, Russo M, Lempka SF, McMahon SB. *Sci Transl Med* 2021;13(608):eabg9890. PMID 34433642.** Ultra-low-frequency biphasic current produced rapid, fully reversible block in **over 85% of spinal sensory fibres** in anaesthetised rats, blocked ectopic activity in a neuropathic model, and in **20 human subjects** with chronic leg and back pain epidural ULF improved pain ratings by 90% at two weeks, reverting to 72% of screening value one week after explant. **Caveat: open-label, uncontrolled, n=20, externalised leads, Presidio Medical authors.** The reversion on explant is a useful internal control but not a substitute for a sham.

### The one KHFAC device that cleared a proper sham

> **Kapural L et al. "Primary 3-Month Outcomes of a Double-Blind Randomized Prospective Study (The QUEST Study)." *J Pain Res* 2024;17:2001-14. PMID 38860215, doi:10.2147/JPR.S463727.**

Neuros Medical Altius, high-frequency block of the transected peripheral nerve in lower-limb amputees. **Multicentre, randomised, double-blind, active-sham controlled**, 180 enrolled, 170 implanted. Responder rate at 30 minutes: **24.7% treatment versus 7.1% active-sham, p=0.002**; at 120 minutes 46.8% versus 22.2%, p=0.001. BPI interference improved 2.3 versus 1.3 points, p=0.01. Opioid reduction trended but did not reach significance. Extensive industry conflicts across the author list.

**This is the strongest sham-controlled evidence in the entire electrical-block field, and it is a peripheral nerve block, not a spinal paradigm.** That geography matters and recurs below.

A physical caution for anyone extrapolating kilohertz carriers: Keesey R, Hofstoetter U, et al. *Nat Biomed Eng* 2026, doi:10.1038/s41551-026-01684-w. PMID 42120752. In 28 participants, kHz waveforms **raise** response thresholds and bias recruitment toward motor efferents.

---

## 3. DRG stimulation

**ACCURATE:** Deer TR, Levy RM, Kramer J, Poree L, et al. *Pain* 2017;158(4):669-81. PMID 28030470, doi:10.1097/j.pain.0000000000000814. Pivotal, prospective, multicentre, randomised **comparative effectiveness** trial, 152 subjects with CRPS or causalgia of the lower extremities, DRG stimulation versus dorsal column SCS. Treatment success at 3 months **81.2% DRG versus 55.7% SCS, p<0.001**, maintained at 12 months. Less postural paraesthesia variation (p<0.001) and less extraneous stimulation (p=0.014). **Unblinded. St. Jude Medical (now Abbott) employees are co-authors.** No sham arm exists for DRG stimulation anywhere.

### Why the DRG is the most convincing tuning story in clinical neuromodulation

The mechanism is anatomically privileged. The DRG T-junction is a natural low-pass filter, and stimulation amplifies that filter rather than blocking the axon.

> **Chao D, Zhang Z, Mecca CM, Hogan QH, Pan B. "Analgesic dorsal root ganglionic field stimulation blocks conduction of afferent impulse trains selectively in nociceptive sensory afferents." *Pain* 2020;161(12):2872-86. PMID 32658148.**

Rat, tibial nerve injury. At **20 Hz**, ganglion field stimulation progressively abated C-fibre activity over about 20 seconds while **Aβ activity persisted unabated**, with Aδ intermediate. Peripherally generated activity was blocked in C units and minimally affected in Aβ. Mechanism: use-dependent enhancement of T-junction filtering. **No declared conflict of interest.**

Supporting model: Kent AR, Min X, Hogan QH, Kramer JM. *Neuromodulation* 2018;21(3):234-46. PMID 29377442. T-junction filtering is amplified at 2.8-5.5 times threshold and at **frequencies above 2 Hz**, dependent on Ca2+ and SK channels producing a somatic hyperpolarising offset. (Kent and Kramer were Abbott and St. Jude.)

**This is the clearest existing demonstration that a low-frequency stimulus can selectively silence nociceptive traffic while leaving large-fibre traffic intact.** It is preclinical, in rat, and the clinical device was never validated against the mechanism. That last clause is the opening.

**Safety, honestly.** Vanloon M et al., *Neuromodulation* 2025;28(2):234-48. PMID 39601733. 13 studies, 634 patients: pooled complication prevalence **37% (95% CI 19-57%)**, device-related 27%, lead fracture 6%, migration 6%, **explantation 12%, primarily for insufficient pain relief**.

---

## 4. Other modalities

**Focused ultrasound.** The only novel modality with sham-controlled human pain data, and the studies are tiny. Badran BW et al., *Brain Stimul* 2020;13(6):1805-12. PMID 33127579: thalamic LIFU, n=19 (accurately sonicated in 17), p=0.046, and both arms' thresholds fell, so the effect is attenuation of drift rather than analgesia. A co-author is employed by BrainSonix. Strohman A, Payne B, In A, Stebbins K, Legon W. *J Neurosci* 2024;44(8):e1011232023. PMID 38182418: dorsal anterior cingulate LIFU, n=16, pain ratings reduced 1.09 ± 0.20 points versus sham, 38.1% reduction in contact-heat evoked P2, no competing interests. In A et al., *Brain Stimul* 2024;17(4):911-24. PMID 39089647: only posterior insula attenuated temporal summation, **no effect on conditioned pain modulation at any target**, a useful internal negative. Peripheral: McCune EP et al., *IEEE Trans Biomed Eng* 2026;73(3):1255-67. PMID 40857198: median nerve LIFU, n=18 healthy plus **n=6 carpal tunnel patients, mean 40.6% pain reduction lasting 1-3 days**, with off-nerve sonication as a spatial control. New and unreplicated.

**The auditory confound is real and unresolved.** Sato T, Shapiro MG, Tsao DY. *Neuron* 2018;98(5):1031-41.e5. PMID 29804920, and Guo H et al. *Neuron* 2018;98(5):1020-30.e4. PMID 29804919: ultrasound-evoked cortical activity is largely cochlear, abolished by deafening or auditory nerve transection. Counter-evidence: Mohammadjavadi M et al., *Brain Stimul* 2019;12(4):901-10. PMID 30880027. Then the damaging follow-up from Shapiro's own group: **Guo H et al., *iScience* 2023;26(12):108372. PMID 38047084**, in an inducibly deafened clean model, "under the acoustic conditions we tested, we did not observe direct calcium responses in the mouse cortex", with tissue damage and spreading depolarisation at higher pressures. Safety framework: Aubry JF et al., ITRUSST consensus, *Brain Stimul* 2025;18(6):1896-1905. PMID 41072763.

**Temporal interference.** Grossman N, Bono D, Dedic N, ... Boyden ES. ***Cell*** **2017;169(6):1029-1041.e16. PMID 28575667** (*Cell*, not *Nature*). Human translation: Violante IR et al., *Nat Neurosci* 2023;26(11):1994-2004. PMID 37857775; Wessel MJ et al., *Nat Neurosci* 2023;26(11):2005-16. PMID 37857774. Boyden, Grossman, Kuster, Pascual-Leone and Neufeld co-founded TI Solutions AG and hold the MIT patent. **For pain, TI is purely speculative:** no peer-reviewed study, no registered trial. The only item is a preprint and should not be cited as evidence. Do not conflate TI with interferential current therapy, an unrelated physiotherapy modality. The critical physics paper is **Mirzakhalili E, Barra B, Capogrosso M, Lempka SF. *Cell Syst* 2020;11(6):557-572.e5. PMID 33157010**, which argues TI cannot work by passive low-pass filtering and requires ion-channel rectification, the same mechanism that produces **off-target conduction block**, undercutting the selectivity claim.

**Infrared neural stimulation and inhibition.** Wells J, Kao C, Mariappan K, Albea J, Jansen ED, Konrad P, Mahadevan-Jansen A. *Opt Lett* 2005;30(5):504-6. PMID 15789717. Mechanism is photothermal (*Biophys J* 2007;93(7):2567-80. PMID 17526565) or capacitive (Shapiro MG, Homma K, Villarreal S, Richter CP, Bezanilla F. *Nat Commun* 2012;3:736. PMID 22415827). Inhibition: **Duke AR, Jenkins MW, Lu H, McManus JM, Chiel HJ, Jansen ED. *Sci Rep* 2013;3:2600. PMID 24009039** (*Sci Rep*, not *J Neural Eng*).

**Crucially, INS block is fibre-selective in the right direction:** Lothet EH et al., "Selective inhibition of small-diameter axons using infrared light." *Sci Rep* 2017;7(1):3275. PMID 28607402 shows small-diameter axons inhibited at *lower* radiant exposures than large. That is the inverse of the electrical constraint and is the single best argument for optical block in pain.

**But the thermal window is brutal.** Wells JD et al., *Lasers Surg Med* 2007;39(6):513-26. PMID 17659590: rat sciatic damage threshold 0.66-0.70 J/cm² against stimulation at 0.34-0.48 J/cm², a safety ratio of only about 1.4-2, with roughly a 5 Hz repetition ceiling. In brain it is worse: Chernov MM, Chen G, Roe AW. *Brain Stimul* 2014;7(3):476-82. PMID 24529644, lesions at or above 0.4 J/cm² per pulse against a damage threshold of 0.3-0.4 J/cm², overlapping effective doses. There is also an INS analogue of the ultrasound auditory confound: Thompson AC et al., *Hear Res* 2015;324:46-53. PMID 25796297. One human study exists (Cayce JM et al., *Neurophotonics* 2015;2(1):015007. PMID 26157986, spinal nerve roots during selective dorsal rhizotomy, threshold activation in only 63% of nerves). **No INS pain application exists.**

**Optogenetics and chemogenetics.** Iyer SM, Montgomery KL, Towne C, Lee SY, Ramakrishnan C, Deisseroth K, Delp SL. *Nat Biotechnol* 2014;32(3):274-8. PMID 24531797: intrasciatic AAV, inhibitory opsin reversed mechanical allodynia and thermal hyperalgesia in freely moving neuropathic mice via transdermal light. Wireless hardware: Jeong JW, McCall JG, ... Gereau RW, Rogers JA. *Cell* 2015;162(3):662-74. PMID 26189679; Zhang Y, Mickle AD, ... *Sci Adv* 2019;5(7):eaaw5296. PMID 31281895; Montgomery KL ... Poon ASY. *Nat Methods* 2015;12(10):969-74. PMID 26280330. Note that Michoud F et al., *Nat Biotechnol* 2021;39(2):179-85. PMID 32958958 *causes* pain and inflammation; it is a model-building tool, not an analgesic.

Chemogenetics carries a field-wide confound: Gomez JL et al., *Science* 2017;357(6350):503-7. PMID 28774929, clozapine-N-oxide does not appreciably cross the blood-brain barrier and is back-metabolised to clozapine, retrospectively confounding DREADD studies lacking a CNO-only control. Improved ligand: Nagai Y et al., *Nat Neurosci* 2020;23(9):1157-67. PMID 32632286. **Human status: zero. No optogenetic or chemogenetic pain trial is registered anywhere.** The translation ceiling is Sahel JA et al., *Nat Med* 2021;27(7):1223-9. PMID 34031601: **n=1**, retina, requiring external light-amplifying goggles.

**Photopharmacology.** Mourot A, Fehrentz T, ... Trauner D, Kramer RH. *Nat Methods* 2012;9(4):396-402. PMID 22343342. QAQ is membrane-impermeant and enters nociceptors **through their own noxious-stimulus-gated channels, principally TRPV1**, requiring no genetic modification, and served as a light-sensitive analgesic in rats in vivo. Elegant and stalled: *Br J Pharmacol* 2018;175(12):2296-2311. PMID 28635081 notes QAQ needs near-UV light, "precluding use deep inside neural tissue", and the trans/cis potency ratio is only about 6.

**Magnetogenetics: treat as refuted for engineering purposes.** Claims: Wheeler MA et al., *Nat Neurosci* 2016;19(5):756-61. PMID 26950006; Stanley SA et al., *Nature* 2016;531(7596):647-50. PMID 27007848; *Nat Med* 2015;21(1):92-8. PMID 25501906. Refutation: **Meister M. "Physical limits to magnetogenetics." *eLife* 2016;5:e17210. PMID 27529126** — ferritin is paramagnetic, not ferromagnetic, so magnetic force, torque and hysteretic heating each fall short of the required energy by, verbatim, "**from 5 to 10 log units**". Anikeeva P, Jasanoff A, *eLife* 2016;5:e19569. PMID 27606500 is an Insight **endorsing** Meister, not rebutting him. Three independent replication failures published together as Matters Arising, *Nat Neurosci* 2020;23(9): PMIDs 31570863, 31570861, 31570862; reply PMID 31570860. The physically sound neighbour, not subject to this objection, is magnetothermal stimulation with real magnetic nanoparticles: Chen R, Romero G, Christiansen MG, Mohr A, Anikeeva P. *Science* 2015;347(6229):1477-80. PMID 25765068.

This is the model case for gate 01. A published, high-profile, mechanistically appealing claim, killed by an order-of-magnitude energy estimate that anyone could have done first.

**Sonogenetics.** Ibsen S, Tong A, Schutt C, Esener S, Chalasani SH. *Nat Commun* 2015;6:8264. PMID 26372413, TRP-4 in *C. elegans*, but the effect **required gas-filled microbubbles**. Duque M et al., *Nat Commun* 2022;13(1):600. PMID 35140203, hsTRPA1 confers ultrasound sensitivity. *The widely miscited "Huang et al. 2020" is Nano Lett 2020;20(2):1089-1100, PMID 31884787, uses an engineered prestin, not TRPA1, and is from the Fan and Yeh lab, not Chalasani's.* **No pain application, and a structural irony: hsTRPA1 is itself a nociceptor channel, so sonogenetic gating in sensory neurons would be expected to produce pain, not block it.** The field now acknowledges the confound in its own titles (Xian Q et al., *iScience* 2025;28(12):114030. PMID 41377656).

---

## 5. Pharmacological precision

**The Nav1.7 story is the field's cautionary tale.** Human genetics is unimpeachable: Cox JJ et al. *Nature* 2006;444(7121):894-8. PMID 17167479 (three consanguineous families, homozygous nonsense mutations S459X, I767X, W897X). Gain-of-function at the other extreme: Fertleman CR et al. *Neuron* 2006;52(5):767-74. PMID 17145499. The drugs failed anyway.

**McDonnell A, Collins S, Ali Z, Iavarone L, Surujbally R, Kirby S, Butt RP. *Pain* 2018;159(8):1465-76. PMID 29578944**: PF-05089771 150 mg twice daily in painful diabetic peripheral neuropathy, NCT02215252, n=135, mean posterior difference versus placebo **−0.41 (90% CrI −1.00 to 0.17), not significant**, while pregabalin in the same trial achieved −0.53 (90% CrI −0.91 to −0.20). Assay sensitivity was therefore intact: the trial could detect a drug, and this drug was not one. Stopped at interim.

The wider programme is a graveyard. Funapide/TV-45070 (topical, blocks Nav1.7 *and* Nav1.8) missed its primary and all secondary endpoints in postherpetic neuralgia (NCT02365636, n=300). Vixotrigine/BIIB074 completed a Phase 2 in lumbosacral radiculopathy (NCT02935608, n=502), had its extension and its small-fibre neuropathy trial **terminated**, and had **both Phase 3 trigeminal neuralgia trials withdrawn with zero enrolled**. GDC-0276 and GDC-0310 were discontinued after Phase 1 in October 2018 and never entered Phase 2.

### Why they failed, stated correctly

**The enkephalin explanation is contested and should not be presented as settled.** Minett MS et al. *Nat Commun* 2015;6:8967. PMID 26634308 showed *Penk* mRNA and met-enkephalin protein up more than two-fold in Nav1.7-null mice, with naloxone reversal. But **the human arm is n=1**, and **Genentech and Merck independently found that naloxone did not affect thermal or mechanical nociceptive deficits.**

The better-supported pharmacological account is in **Mulcahy JV, Pajouhesh H, Beckley JT, Delwig A, Du Bois J, Hunter JC. *J Med Chem* 2019;62(19):8695-8710. PMID 31012583, PMC6786914** (open access), and it is three quantitative facts:

- **Occupancy.** Analgesia appears to require roughly **80-90% channel block**. PF-05089771 had IC50 = 11 nM and plasma exposures above 10,000 ng/mL and still missed.
- **Protein binding.** First-generation aryl sulfonamides are **at least 99% plasma-protein bound**, so free fraction, not total exposure, is the binding constraint.
- **State dependence, the core problem.** The sulfonamides preferentially bind the **depolarised conformation of voltage-sensing domain IV**, but steady-state dynamics in uninjured tissue favour the resting state, for which they have low affinity. **Target engagement is worst exactly where the channel is not already firing.**

Mulcahy et al. conclude that "acute inhibition of NaV1.7 is sufficient to produce analgesia", which directly contradicts the enkephalin-as-explanation reading. See also Yang J, Xie YF, Smith R, Ratté S, Prescott SA. "Discordance between preclinical and clinical testing of NaV1.7-selective inhibitors for pain." *Pain* 2025;166(3):481-501. PMID 39928833, PMC11808711: 44 preclinical studies against 73 clinical trials, 83% of preclinical work male-only, preclinical emphasis on inflammatory pain (40%) against clinical neuropathic (88%), 84% preclinical single-dose against 93% clinical repeat-dose. It notes that **Nav1.7 may not be essential for neuropathic pain at all**.

**A selectivity caveat the field under-reports:** Nav1.7 loss is not pain-only. SCN9A-null humans are **anosmic** (Weiss J, Pyrski M, ... Wood JN, Zufall F. *Nature* 2011;472(7342):186-90. PMID 21441906).

**Channel genetics identified the target; it did not deliver the drug.** Any conjecture in this programme that reasons from a genetic phenotype to a therapeutic handle has to answer this, and the specific thing it has to answer is state dependence, not opioid tone.

**Suzetrigine is the counter-example, and it is Nav1.8, not Nav1.7.** Verified against openFDA and DailyMed: **NDA 219209, JOURNAVX (suzetrigine), Vertex, approved 30 January 2025**, indicated for "moderate to severe acute pain, including postoperative pain, in adults", 100 mg loading then 50 mg every 12 h, **not studied beyond 14 days**.

Mechanistically it is the mirror image of the failed Nav1.7 compounds, and that is the interesting part: suzetrigine binds **VSD2 and stabilises the closed state, giving tonic inhibition**, where the aryl sulfonamides bound VSD4 and needed the channel already depolarised. Selectivity is reported at **at least 31,000-fold** over other NaV subtypes (Osteen JD et al. *Pain Ther* 2025;14(2):655-74. PMID 39775738, all nine authors Vertex employees; independent electrophysiology by Bean's group, Jo S et al. *J Gen Physiol* 2025;157(4):e202413719. PMID 40136042).

Pivotal evidence: **Bertoch T, D'Aunno D, McCoun J, Solanki D, Taber L, et al. *Anesthesiology* 2025;142(6):1085-99. PMID 40117446.** Abdominoplasty NCT05558410 n=1,118 and bunionectomy NCT05553366 n=1,073, randomised double-blind, placebo- and active-controlled.

| | SPID48 versus placebo | versus hydrocodone/paracetamol 5/325 |
|---|---|---|
| Abdominoplasty | **48.4 (95% CI 33.6-63.1), p<0.0001** | +6.6 (95% CI −5.4 to 18.7), interval crosses zero |
| Bunionectomy | **29.3 (95% CI 14.0-44.6), p=0.0002** | **−20.2 (95% CI −32.7 to −7.7), interval excludes zero, favouring the opioid** |

Verbatim from the abstract: "Neither trial achieved the first key secondary endpoint of superiority of suzetrigine versus hydrocodone bitartrate/acetaminophen on SPID48." **In the bunionectomy trial suzetrigine was not merely non-superior; the interval favours the opioid.** Five Vertex-employee authors with stock, multiple others taking personal fees from Vertex.

So: a genuinely novel, non-addictive, peripherally restricted mechanism that is **at best as good as, and in one of two pivotal trials worse than, a weak opioid** in acute post-surgical pain.

The chronic-pain extension is where selectivity is really being tested, and the registry needs reading carefully, because the two Phase 2 results are **not symmetric evidence**:

- Painful **lumbosacral radiculopathy** Phase 2 (NCT06176196, n=218) completed 16 October 2024, no results posted, no Phase 3. Suzetrigine −2.02 on the NPRS against placebo −1.98, so no separation. But the study **was not designed or powered for a suzetrigine-versus-placebo comparison**; the "met its primary endpoint" framing refers to the *within-group* reduction. `[UNVERIFIED: these figures come from secondary reporting of a Vertex release, not the primary document.]`
- Painful **diabetic peripheral neuropathy** Phase 2 (NCT05660538, n=194) reported positive in December 2023, and progressed to three Phase 3 trials (NCT06628908, NCT07231419, NCT06696443). But **there was no placebo arm**: the four arms were three suzetrigine doses against pregabalin as reference. An active-controlled dose-ranging study without placebo cannot establish efficacy against placebo.

The differential progression is suggestive. It is not the clean "failed in radiculopathy, succeeded in neuropathy" story it is usually told as, and this programme should not repeat that framing.

**Ligand-gated selectivity, the most elegant idea in the section.** Binshtok AM, Bean BP, Woolf CJ. "Inhibition of nociceptors by TRPV1-mediated entry of impermeant sodium channel blockers." *Nature* 2007;449(7162):607-10. PMID 17914397. QX-314, a charged and membrane-impermeant lidocaine derivative, is inert alone but enters nociceptors through the open TRPV1 pore when co-applied with capsaicin, producing **over 2 hours of thermal and mechanical analgesia without motor or tactile deficit**.

This is *nociceptor-specific local anaesthesia*: the exact selectivity electrical block cannot achieve, delivered by using the target cell's own channel as the gate. It is 19 years old and has not reached the clinic. Why not is a question worth a conjecture of its own.

### TRPV1 ablation, and a large unpublished negative

Resiniferatoxin, intrathecal, for cancer pain: Mannes AJ, Heiss JD, ... Sapio MR, Iadarola MJ. *NEJM Evid* 2025;4(6):EVIDoa2400423. PMID 40423401. NCT00804154, **open-label Phase 1, single arm, n=19** of a planned 45. Worst pain −38%, opioid use −57% at day 15. **No control arm, so no between-group effect size and no NNT.** 213 treatment-emergent adverse events, **37 serious in 14 patients, 9 deaths** (mean 70 days, attributed to advanced cancer), **3 with loss of heat sensation in the exposed dermatomes**, **7 with urinary retention beyond 24 h** (about 37%, consistent with TRPV1-positive bladder afferents), five with transient QT prolongation.

**Two things matter more than the efficacy number.**

First, **the mechanism was revised by the originating laboratory**. Karai 2004 and Brown 2015 describe permanent ablation of TRPV1-positive DRG cell bodies. Sapio MR, Neubert JK, ... Mannes AJ, Iadarola MJ. *J Clin Invest* 2018;128(4):1657-70. PMID 29408808, PMC5873867, from the same group, found intrathecal RTX instead causes **central chemo-axotomy**: it "largely spares susceptible neuronal perikarya, which remain active peripherally but unable to transmit signals to the spinal cord". That is an internal contradiction in the programme's own literature and it changes the permanence and reversibility story.

Second, **two Grünenthal Phase 3 knee osteoarthritis trials completed, were null, posted results to ClinicalTrials.gov and were never published.** NCT05248386 (466 analysed): WOMAC pain at week 12 **−2.959 RTX versus −2.847 placebo**, a difference of about 0.11, with RTX numerically *worse* at weeks 26 and 52. NCT05449132 (n=466): **−3.25 versus −2.99**. Placebo response was about 3 points; the differences are far below any WOMAC minimum clinically important difference. Sorrento's own programme collapsed: two Phase 3 trials withdrawn at zero enrolment, and an epidural Phase 2 suspended with `whyStopped` recorded as "Sorrento Therapeutics filed for chapter 11 bankruptcy".

**Currency trap.** The most recent narrative review, Iadarola MJ, Sapio MR, Nahama A, Mannes AJ, *Pain Manag* 2025;15(10):659-70, PMID 40776673, calls intra-articular RTX of "strong therapeutic promise" and contains **zero mentions of Phase 3**, because it was accepted on 14 July 2025 and the first results posting was 12 August 2025. Do not cite it as current evidence. Contrast Matta C et al., "The rise and fall of TRPV1-targeted analgesia in osteoarthritis", *Expert Opin Pharmacother* 2026;27(11):1179-96. PMID 42373560: "TRPV1-targeted therapy in OA has completed a full translational cycle without yielding regulatory approval."

Note also that **"trans-capsaicin" (CNTX-4975) is Centrexion's molecule, not Sorrento's RTX.** They are routinely conflated.

**Is RTX selective? Only relative to alcohol and phenol neurolysis.** Motor function, touch, proprioception and high-threshold mechanonociception are preserved and no deafferentation pain syndrome was seen. But loss of noxious heat sensation is an on-target consequence, not an off-target surprise, and thermoregulatory and cardiovascular effects are large in animals.

### Capsaicin 8% patch

Derry S, Rice ASC, Cole P, Tan T, Moore RA. *Cochrane Database Syst Rev* 2017;1(1):CD007393. PMID 28085183, PMC6464756. **8 studies, 2,488 participants.**

**Only postherpetic neuralgia, on patient global impression of change, reached moderate GRADE, and on 2 studies and 571 people:** NNT **8.8 (95% CI 5.3-26) at 8 weeks** and **7.0 (4.6-15) at 12 weeks**. Everything else is very low certainty. Painful diabetic neuropathy is a single study (n=369) whose responder risk ratios all cross 1.0.

**Do not propagate the PubMed abstract's error.** It renders these as "8.8 with high-concentration capsaicin and 7.0 with active placebo", which is meaningless. The published table shows the two figures are **8 weeks and 12 weeks**. The inconsistency is in the Cochrane text, not only in PubMed, so cite the table with timepoint labels.

**The active-control problem is material.** Cochrane, verbatim: "Two studies used a placebo control and **six used 0.04% topical capsaicin as an 'active' placebo** to help maintain blinding." Control arms in those six show 25-37% response, so the comparator is plausibly not inert. The **only true-placebo pivotal trial (STEP, Simpson 2017, *J Pain* 18(1):42-53, PMID 27746370, n=369, quadruple-masked, Astellas) produced the smallest absolute separation, 6.5 percentage points, p=0.025.** And one of the six active-placebo pivotal trials failed outright on its primary endpoint (Clifford 2012, *JAIDS* 59(2):126-33, PMID 22067661, n=494, −29.5% versus −24.5%, p=0.097).

Cochrane's own conclusion is framed accordingly: benefit "than control treatment **using a much lower concentration of capsaicin**".

### Botulinum toxin A

Attal N, de Andrade DC, Adam F, Ranoux D, Teixeira MJ, Galhardoni R, Raicher I, Üçeyler N, Sommer C, Bouhassira D (BOTNEP). *Lancet Neurol* 2016;15(6):555-65. PMID 26947719. NCT01251211, Phase 4, quadruple-masked. **152 enrolled but 68 randomised and 66 analysed**; the registry lists 66 as enrolment, so the 152 figure is a registry-publication mismatch and should not be quoted as the sample size. Adjusted effect **−0.77 (95% CI −0.95 to −0.59), p<0.0001** on a 0-10 weekly NRS over 24 weeks. Funded by INSERM and Fondation CNP. `[Europe PMC's structured grant field lists "Astellas Pharma US" for this DOI, contradicting the printed funding statement. That is a metadata artefact; do not cite Astellas as a BOTNEP funder.]`

**The effect is under one point, below the usual 2-point or 30% minimum clinically important difference.** Clean design, small effect.

The NeuPSIG guideline (Finnerup NB, Attal N, Haroutounian S, et al. *Lancet Neurol* 2015;14(2):162-73. PMID 25575710, PMC4493167) gives botulinum a **weak recommendation, third line, quality of evidence LOW**, on an NNT of 1.85 (95% CI 1.5-2.4). **If that NNT is quoted it must carry three qualifiers:** it rests on 137 patients, the placebo response is implausibly low at 4/67, and the guideline's own words are that "one large unpublished study was negative". That is why the recommendation is weak despite the lowest NNT in the review.

There is **no Cochrane review of botulinum toxin A for neuropathic pain.** The meta-analyses that exist are small-trial-dominated with documented publication bias: Datta Gupta A et al., *Toxins* 2022;14(1):36, PMID 35051013, reports I² = 88.1% and **Egger's test p=0.002**, with sleep, anxiety, depression and quality of life all null, and concludes the evidence does *not* support first-line use.

### Ketamine

Sigtermans MJ, van Hilten JJ, Bauer MCR, Arbous SM, Marinus J, Sarton EY, Dahan A. *Pain* 2009;145(3):304-11. PMID 19604642. n=60 CRPS-1, double-blind, 4.2-day continuous intravenous S(+)-ketamine, median disease duration 7.4 years. Nadir at end of week 1: **2.68 ± 0.51 versus 5.45 ± 0.48**, about 2.8 NRS points. Significant at weeks 1 through 11, and verbatim: **"In week 12, significance in pain relief between groups was lost (P=0.07)."** A paper titled "long-term pain relief" reports an effect that decays to null by week 12.

**Two facts the title obscures, and both matter.** "Treatment did not cause functional improvement" at any point. And **the blind failed: 28 of 30 ketamine patients correctly guessed their allocation**, with psychotomimetic adverse events at 76% versus 18%.

The second CRPS trial (Schwartzman RJ et al. *Pain* 2009;147(1-3):107-15. PMID 19783371) was **terminated early, analysed completers only, n about 19-21, with both arms also receiving clonidine and midazolam, no published effect size, and a baseline imbalance favouring the ketamine group.**

**The two appraisals of these same trials disagree, and the disagreement should be resolved in favour of the newer one.** The ASRA/AAPM/ASA consensus (Cohen SP et al. *Reg Anesth Pain Med* 2018;43(5):521-46. PMID 29870458, PMC6023575) reads them at face value and gives CRPS "moderate evidence, improvements up to 12 weeks, grade B". **Ferraro MC, Cashin AG, Visser EJ, ... O'Connell NE, McAuley JH. *Cochrane Database Syst Rev* 2025;8(8):CD015373. PMID 40819842, PMC12358209** applies RoB 2 and GRADE to 67 RCTs and 2,309 participants and finds intravenous ketamine versus placebo: immediate **MD −15.79 (95% CI −32.09 to 0.51)**, very low certainty; short term **−5.32 (−15.51 to 4.87)**, low; medium term one study of 19 patients; **no long-term evidence at all**; and **increased adverse events, RR 3.26 (1.05-10.09)**.

A brief quoting ASRA's grade B without the 2025 Cochrane result is citing a 2018 consensus over a 2025 systematic review of the same data. The 2013 Cochrane CRPS overview is also superseded by Ferraro MC et al. 2023, CD009416.pub3, PMID 37306570, which found no high-certainty evidence for any comparison and no longer lists ketamine among interventions with even low-certainty support.

### Low-dose naltrexone

**The evidence inverts as rigour increases, which is the pattern to watch for.**

The two positive trials are small and from one laboratory. Younger & Mackey 2009 (*Pain Med* 10(4):663-72, PMID 19453963) is **n=10 analysed, single-blind and NOT randomised**: a fixed sequence of baseline, placebo, naltrexone, washout, so order effects and regression to the mean are fully confounded with treatment. Younger, Noor, McCue & Mackey 2013 (*Arthritis Rheum* 65(2):529-38, PMID 23359310) is n=28 analysed, double-blind crossover, 28.8% versus 18.0% reduction, p=0.016, **with no between-group effect size or confidence interval reported** and heavily overlapping within-arm intervals in the registry.

**Both adequately powered, properly blinded, parallel-group trials failed.**

- **FINAL:** Bruun KD, Christensen R, Amris K, Vaegter HB, Blichfeldt-Eckhardt MR, Bye-Møller L, Holsgaard-Larsen A, Toft P. *Lancet Rheumatol* 2024;6(1):e31-e39. PMID 38258677. NCT04270877, 99 randomised, 12 weeks, no loss to follow-up. **Between-group difference −0.34 (95% CI −0.95 to 0.27), p=0.27, Cohen's d 0.23.** Verbatim: "This study did not show that treatment with low-dose naltrexone was superior to placebo in relieving pain."
- **INNOVA:** Rodríguez-Freire C, Navarrete J, ... Luciano JV. *Eur J Pain* 2026;30(6):e70321. PMID 42385209, PMC13322712. NCT04739995, 98 randomised, 4.5 mg/day, 12 months. **Adjusted between-group difference 0.49 in favour of PLACEBO (95% CI −0.32 to 1.31, p=0.236).** Blinding held.

**The mechanism story is weaker than advertised.** The TLR4 account rests on Hutchinson MR et al. *Eur J Neurosci* 2008;28(1):20-29. PMID 18662331, which showed TLR4 antagonism at **1-10 µM in vitro with intrathecal rodent dosing**, orders of magnitude above the low-nanomolar plasma levels produced by oral 4.5 mg. No source demonstrates TLR4 antagonism at human low-dose exposures.

**Handle the positive meta-analysis carefully.** Vatvani AD et al. *Korean J Pain* 2024;37(4):367-78, PMID 39344363, reports pain MD −0.86 (95% CI −1.20 to −0.51) and **contains a documented extraction error with a published corrigendum**: it inflated FINAL's responder data by summing the 30% and 50% responder counts. On re-analysis, pain-score pooling shows **no significant difference at 12 weeks, SMD −0.25 (95% CI −0.59 to 0.09)**. See Bruun KD et al. *Korean J Pain* 2026;39(1):140-43, PMID 41469218, and the corrigendum, PMID 41469220. **If Vatvani is cited, the correction must be cited with it.**

### Topical phenytoin cream

**The evidence base is thinner than its advocacy, and this matters because it is a treatment patients in this population actively seek out.**

A PubMed search for phenytoin cream in neuropathic pain returns **13 records in total, 11 of them Kopsky and/or Keppel Hesselink**. Of the two exceptions, one is a general review and one is a single case report co-authored by the same two. **There is no independent replication by an unaffiliated group.**

What exists: a case series (n=70, *Pharmaceuticals* 2018;11(2):53, PMID 29843362), a single-blind within-patient contralateral response test at 30 minutes (n=21, PMID 30424471), a double-blind within-patient response test at 30 minutes (n=12, 6 of 12 responders, mean difference 1.3 NRS, *J Pain Res* 2020;13:877-82, PMID 32431536), pharmacokinetics showing no detectable plasma levels (PMID 35173477), and a retrospective series (n=65, of whom 31 test-positive, *Pharmaceuticals* 2025;18(2):228, PMID 40006041).

Two structural problems. The response tests measure pain change **30 minutes** after application in a **within-patient contralateral** design, which is a pharmacological bioassay rather than evidence of sustained analgesia. And the impressive sustained-relief figures in the 2025 paper are computed **only within the enriched, test-positive subgroup, with no control arm**.

**The one adequately designed trial finished and has not reported.** EPHENE, the enriched-enrolment randomised double-blind placebo-controlled triple crossover trial, protocol at *Trials* 2022;23(1):888, PMID 36273216, **NCT04647877, registry status COMPLETED, n=81 actual, primary completion 15 June 2023**. Results are still not posted and no results publication is indexed, more than three years on. That non-publication is itself the finding.

**Declared conflict, from the papers themselves:** both authors hold two patents (WO2018106107 and WO2018106108), and the 2025 paper adds that one author, through Topical Innovations B.V., is a co-holder and **has received licensing fees from Xeolas Pharmaceuticals**.

**Treat topical phenytoin as unproven.**

---

## 6. Closed loop

**What exists.** One closed-loop SCS system has randomised, blinded evidence: Mekhail N, Levy RM, Deer TR, Kapural L, et al. (Evoke Study Group). *Lancet Neurol* 2020;19(2):123-34. PMID 31870766, with durability at 24 months (PMID 34998276) and 36 months (PMID 37640452). Full numbers in E-02 §2.

**What it senses, and the gap.** The ECAP is the evoked compound action potential of dorsal column Aβ fibres: a direct electrophysiological readout of *how much large-fibre tissue the stimulus recruited*. It is a real neural signal, not an accelerometer proxy like earlier posture-responsive systems (Schultz DM et al., *Pain Physician* 2011;14(5):407-17. PMID 21927044), and that is why Evoke works: it holds recruitment inside the therapeutic window against postural changes in CSF thickness.

**But the ECAP is not the pain signal.** It measures delivery fidelity, not therapeutic effect. Closed-loop SCS today is closed on the *actuator*, not on the *symptom*. A cleaner framing, and one this programme should adopt: Evoke proves that **dose control** matters, which is itself an argument that much of the waveform debate has been mis-specified dose all along.

**The first genuine pain-signal loop is intracranial and n=4.** Shirvalkar P et al. *Nat Neurosci* 2023;26(6):1090-9. PMID 37217725. Detailed in E-02 §5, including the important caveat that intensity regression failed.

---

## Established / contested / speculative

**ESTABLISHED.** Kilohertz alternating current produces rapid, complete and reversible conduction block in peripheral nerve, with block threshold rising with frequency and falling with axon diameter (PMIDs 16124008, 17200886). A kHz peripheral nerve block device passed a double-blind active-sham pivotal trial and is FDA-approved for post-amputation pain (PMID 38860215). DRG field stimulation at 20 Hz selectively abates C-fibre trains while sparing Aβ, in rat (PMID 32658148). ECAP-controlled closed-loop SCS beats open-loop in a double-blind RCT out to 36 months. Suzetrigine is approved for acute pain and beats placebo but not a weak opioid. Ultrasound neuromodulation in rodents is substantially confounded by a cochlear pathway.

**CONTESTED.** Whether 10 kHz, burst and DTM SCS work through mechanisms distinct from tonic SCS. Whether any SCS waveform beats a true sham for low back pain. Whether the roughly 1-point pooled sham-controlled effect is clinically meaningful. Whether kHz fibre selectivity is a frequency phenomenon or a charge-imbalance and DC artefact. Whether ultrasound has any direct, non-auditory cortical effect at safe pressures. Whether topical phenytoin does anything.

**SPECULATIVE.** Temporal interference for pain. Optogenetic or chemogenetic analgesia in humans. Sonogenetic analgesia. Photopharmacological analgesia beyond 2012 rat data. Magnetogenetics, which should be treated as physically refuted.

---

## The strongest evidence FOR frequency and pattern specificity being real and mechanistic

Three findings, in ascending order of relevance to pain.

1. **Frequency-tuned fibre selectivity in isolated nerve.** Zhang, Chen, Feng et al. 2024, PMID 39077428. **C fibres block optimally at 10-50 Hz and Aδ at 50-1000 Hz**, an inverse relationship between conduction velocity and optimal blocking frequency, with a mechanistic account and a matching simulation. This is frequency doing something a scalar dose cannot do, and it points selectivity the *right* way for pain.
2. **Selective nociceptor silencing at the DRG T-junction.** Chao, Zhang, Mecca, Hogan & Pan 2020, PMID 32658148. At 20 Hz, C-fibre trains progressively fail while Aβ trains pass unattenuated, with a specific anatomical mechanism and a supporting biophysical model. No industry conflict. **This is the closest thing in existence to "block the pain wire, keep the touch wire."**
3. **Non-monotonic, cell-type-specific dorsal horn effects at 10 kHz.** Lee et al. 2020, PMID 31917342. Sub-threshold 10 kHz but not 1 or 5 kHz selectively activated inhibitory interneurons. Non-monotonicity in frequency is intrinsically incompatible with a pure dose account. Weakened by Nevro affiliation and by not having been independently replicated.

## The strongest evidence AGAINST

1. **PROCO.** PMID 29220121. Double-blind crossover: 1, 4, 7 and 10 kHz gave equivalent analgesia at the same optimised location once pulse width and amplitude were titrated, with 1 kHz needing 60-70% less charge. Frequency was not the active variable. Charge and position were.
2. **The same waveform, blinded versus unblinded, in the same patients.** Gulisano et al. 2024, PMID 38988274, plus Hara et al. 2022, PMID 36255427, the latter with no declared conflicts. The effect appears exactly when blinding is removed.
3. **Modelling says the recruitment order does not change.** Rogers, Zander & Lempka 2022, PMID 34583022, plus Lempka et al. 2015, PMID 25822589. Across conventional, burst and 10 kHz, absolute thresholds differ but recruitment order is identical, and clinical amplitudes reach neither direct activation nor conduction block of dorsal column fibres.
4. **Sham beats the middle of the frequency range.** Al-Kaisy et al. 2018, PMID 29608229.

---

## Synthesis, and what it means for this programme

Frequency and pattern specificity is a real physical property of nerve, demonstrated repeatedly at the axon and the ganglion. **It has not been shown to be what the current generation of spinal devices is exploiting.** The commercially successful paradigms appear to be delivering charge to the right place, and the strongest blinded result in the field, Evoke, is a **dose-control** result.

The most promising route to genuine tuning is **not the spinal cord at all**. It is the DRG T-junction and the peripheral nerve, where the filtering physics is favourable, an approved sham-tested block device already exists, and low-frequency and ultra-low-frequency waveforms show selectivity that kilohertz amplitude scaling cannot achieve.

That is a substantial redirection of the programme: away from the cord and towards the ganglion and the peripheral nerve, and away from higher frequencies towards lower ones.
