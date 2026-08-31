# E-02. Reading neural signals from peripheral nerve and spinal cord in humans

> Literature brief, September 2026. Citations resolved against the Europe PMC
> REST API (title, journal, volume, pages, DOI, PMID cross-checked) unless
> marked `[UNVERIFIED]`. Two corrections to commonly repeated claims are flagged
> inline.
>
> Bears on: HC-2 (readable outside the CNS), HC-4 (realisable transducer).

---

## 1. Microneurography: the only technique that reads human C-fibres

**ESTABLISHED.** A tungsten microelectrode inserted percutaneously into a fascicle of an awake human is the sole method that has ever resolved single unmyelinated nociceptor action potentials in a conscious person. Origin: Vallbo & Hagbarth, *Exp Neurol* 1968;21:270-289 (doi:10.1016/0014-4886(68)90041-1, PMID 5673644) for mechanoreceptors; Torebjörk & Hallin, *Brain Res* 1974;67:387-403 (doi:10.1016/0006-8993(74)90489-2, PMID 4470432) for C units.

The **marking technique** is what makes it work. C-fibres cannot be identified by waveform: they sit in Remak bundles, their spikes are of the order of the noise floor, and their shapes are near-identical. Instead, low-frequency electrical stimulation (typically 0.25 Hz) produces activity-dependent slowing of conduction velocity that is characteristic per fibre, and a spike that "marks" (shifts latency) after an intervening natural stimulus is thereby assigned to a specific unit.

This yielded the modern nociceptor taxonomy. Schmidt, Schmelz, Forster, Ringkamp, Torebjörk & Handwerker, *J Neurosci* 1995;15:333-341 (doi:10.1523/JNEUROSCI.15-01-00333.1995, PMID 7823139) recorded 194 cutaneous C-fibres from human peroneal nerve and found 45% CMH, 13% CM, 6% CH, **24% mechano- and heat-insensitive "silent" nociceptors** and 12% sympathetic units. Review: Ackerley & Watkins, *J Neurophysiol* 2018;120:2834-2846 (doi:10.1152/jn.00109.2018, PMID 30256737); C-fibres are roughly 80% of all axons in a peripheral nerve. Current synthesis: Namer & Lampert, *Pain* 2025;166:2220-2235 (doi:10.1097/j.pain.0000000000003605, PMID 40294386).

**Clinical reach.** Serra et al., *Ann Neurol* 2014;75:196-208 (doi:10.1002/ana.24065, PMID 24243538) found spontaneous activity in **31% of silent nociceptors in fibromyalgia versus 2.2% in controls**. Serra et al., *Pain* 2015;156:2175-2183 (doi:10.1097/j.pain.0000000000000249, PMID 26035253) used spontaneous C-nociceptor activity as the **primary endpoint of a randomised placebo-controlled drug trial** (the T-type calcium blocker ABT-639 in painful diabetic neuropathy). The drug failed; the assay worked. That is an important precedent for this programme: a peripheral electrophysiological readout has already served as a regulatory-grade primary endpoint. Most recently Ribeiro et al., *Ann Neurol* 2026;99:356-368 (doi:10.1002/ana.78045, PMID 40977575): 32 of 36 long-COVID patients (88.9%) had objective C-fibre abnormalities, 61.1% with spontaneous nociceptor activity.

**Why it has not scaled.** Dunham, Sales & Pickering, *Clin Neurophysiol* 2018;129:2475-2481 (doi:10.1016/j.clinph.2018.07.011, PMID 30107982) state it plainly: the method "requires technical expertise, investment in specialised equipment and has sparse data yields". Their ultrasound guidance across 32 volunteers cut skin-to-nerve time from **28.5 min to 4.5 min** (p<0.0001), a real advance that still leaves a technique where a productive session may deliver a handful of fibres. Troglio et al., *PLOS ONE* 2025;20:e0329537 (doi:10.1371/journal.pone.0329537, PMID 41004469): across 26 datasets, recordings contained **2 to 6 tracked fibres**, sampled at 10-30 kHz; supervised spike sorting on raw waveform features reached mean accuracy 0.73 with a range of **0.19 to 0.99**, and works only for electrically marked spikes, not spontaneous traffic.

Single electrode, single fascicle, subject motionless, hours per unit, no chronic version. That is the ceiling.

---

## 2. ECAP-controlled closed-loop SCS: the only deployed "read the cord" technology

**ESTABLISHED, and the strongest RCT evidence in neuromodulation.**

**What is measured.** An epidural lead delivers a stimulus and neighbouring contacts record the resulting evoked compound action potential: a triphasic P1/N1/P2 waveform from the **synchronous volley of large myelinated Aβ dorsal column axons**, latency under 2 ms proximal to the stimulus. Parker et al., *Neuromodulation* 2020;23:82-95 (doi:10.1111/ner.12968, PMID 31215718) measured conduction velocity of **109 m/s** in sheep, implying fibres up to 20 µm diameter. Amplitudes are small: in real-world European data (Nijhuis et al., *Pain Ther* 2024;13:1119-1136, doi:10.1007/s40122-024-00628-z, PMID 38954217) the median ECAP threshold sat near single-digit µV and the amplitude at maximum discomfort near 55 µV, with therapy delivered at a median **90% of stimuli above ECAP threshold, dose ratio 1.3, dose accuracy 4.4 µV**. Technical constraints: Chakravarthy, Bink & Dinsmoor, *J Pain Res* 2020;13:3269-3279 (doi:10.2147/JPR.S289098, PMID 33328760).

**The RCT.** Mekhail et al., *Lancet Neurol* 2020;19:123-134 (doi:10.1016/S1474-4422(19)30414-4, PMID 31870766). 134 patients randomised 1:1 at 13 US sites, double-blind, parallel-arm. Primary endpoint (at least 50% reduction in overall back and leg pain with no medication increase) reached by **82.3% (51/62) closed-loop versus 60.3% (38/63) open-loop at 3 months** (difference 21.9%, 95% CI 6.6-37.3, p=0.0052) and **83.1% versus 61.0% at 12 months** (p=0.0060). Durability: 24 months, 79.1% versus 53.7% (p=0.001), Mekhail et al., *JAMA Neurol* 2022;79:251-260 (doi:10.1001/jamaneurol.2021.4998, PMID 34998276). 36 months, 77.6% versus 49.3% (p<0.001) and **at least 80% relief in 49.3% versus 31.3%** (p=0.032), with no explants for loss of efficacy in the closed-loop arm: Mekhail et al., *Reg Anesth Pain Med* 2024;49:346-354 (doi:10.1136/rapm-2023-104751, PMID 37640452).

**Dose-response.** Levy et al., *Neuromodulation* 2024;27:1393-1405 (doi:10.1016/j.neurom.2024.07.003, PMID 39254621) pooled n=180 across three studies and derived a neurophysiological dose regimen: **dose accuracy 2.8 µV and dose ratio 1.4 gave maximal analgesic effect of 79 ± 1% pain reduction**. This is genuinely novel and directly relevant: a neurostimulation therapy with a measurable delivered dose rather than a dial setting.

**Devices.** Saluda Evoke (FDA approved March 2022) adjusts over 100 times per second. Medtronic Inceptiv (FDA approved 26 April 2024) senses at 50 Hz and is the only closed-loop SCS with full-body 3T MRI labelling. **Medtronic AdaptiveStim/RestoreSensor is not neural sensing at all**: it is accelerometer-based posture detection, and conflating it with ECAP is a common error. Abbott's marketed portfolio (Proclaim, Eterna, BurstDR) has no commercial ECAP closed loop.

**CONTESTED, and this is the point that matters most for the programme.** ECAP amplitude is a measure of **Aβ dorsal column recruitment, not of nociception**. The closed loop compensates for the fact that the dorsal CSF layer, and therefore activation, changes with posture, breathing and heartbeat. It does not read pain. The trial also carried methodological criticism (Maher & Littlewood, *Lancet Neurol* 2020;19:380, doi:10.1016/S1474-4422(20)30110-1, PMID 32333889; author reply PMID 32333890), and the unusually high open-loop responder rate of 60% at 3 months invites scrutiny of generalisability.

The state of the art in closed-loop pain neuromodulation is therefore excellent at holding a physical dose constant, and blind to what the patient feels.

---

## 3. Peripheral nerve interfaces

| Interface | Human data | Channels | Chronic life | Recording? |
|---|---|---|---|---|
| **USEA** (Normann, Clark, Greger, Utah) | Davis 2016 (2 subj, 30 d); Wendelken 2017 (2 subj, 4-5 wk); George 2020 (3 subj, 7 arrays, 84-503 d) | 100 shanks, 96 active | 6 of 7 arrays lost functional electrodes **within 2 months**; 502 days in one outlier | Yes, peak **34 simultaneously active** electrodes, median neural **SNR 5.0-5.7** |
| **TIME / tf-LIFE** (Micera, Rossini) | Rossini 2010 (1 subj, 4 wk, tf-LIFE4); Petrini 2019 *Ann Neurol* (3 subj, 6 months) | 4-56 sites | 6 months verified maximum | Micera 2011: 3 grasps plus rest decoded at **~85%** |
| **FINE / spiral cuff** (Tyler, Case Western) | Tan 2014 (2 subj, 16 and 24 months) | 16-20 contacts | **2 years**, impedance stable ~3 kΩ | **No.** Stimulation only |
| **RPNI** (Cederna, Kemp, Michigan) | Vu 2020 (4 subj); Vu 2023 | Muscle grafts | **300 days** control without recalibration; SNR above 15 for 276 and 1054 days | Yes, **2.77 ± 0.66 mV peak-to-peak, SNR 102** |
| **Sieve / microchannel** | None | - | Rat, 3-7 months | 35-170 µV (FitzGerald 2012) |

Citations: Davis et al., *J Neural Eng* 2016;13:036001 (doi:10.1088/1741-2560/13/3/036001, PMID 27001946); Wendelken et al., *J NeuroEng Rehabil* 2017;14:121 (doi:10.1186/s12984-017-0320-4, PMID 29178940); George et al., *J Neural Eng* 2020;17:056042 (doi:10.1088/1741-2552/abc025, PMID 33045689); Rossini et al., *Clin Neurophysiol* 2010;121:777-783 (PMID 20110193); Micera et al., *J NeuroEng Rehabil* 2011;8:53; Raspopovic et al., *Sci Transl Med* 2014;6:222ra19 (PMID 24500407, **stimulation only**, control came from surface EMG); Petrini et al., *Ann Neurol* 2019;85:137-154 (doi:10.1002/ana.25384, PMID 30474259); Petrini et al., *Nat Med* 2019;25:1356-1363 (PMID 31501600, leg amputees, tibial nerve, stimulation); Dhillon & Horch, *IEEE TNSRE* 2005;13:468-472 (PMID 16425828); Tan et al., *Sci Transl Med* 2014;6:257ra138 (PMID 25298320) and *J Neural Eng* 2015;12:026002 (PMID 25627310); Vu et al., *Sci Transl Med* 2020;12:eaay2857 (PMID 32132217) and *J Neural Eng* 2023;20:026039; FitzGerald et al., *J Neural Eng* 2012;9:016010; Musick and Lacour et al., *Sci Rep* 2015;5:14363.

**Two corrections worth carrying forward**, because both are repeated incorrectly in secondary sources: Rossini 2010 used tf-LIFE4, not TIME. The six-month human TIME implant is *Annals of Neurology* 2019, not *Nature Medicine*.

**Anatomy sets the limit.** Delgado-Martínez et al., *Front Neurosci* 2016;10:286: 8 human median nerves, **18,122 fascicles**, mean 19.85 ± 1.23 fascicles per cross-section, **94% in the smallest size class**.

**Foreign-body response.** de la Oliva, Navarro & del Valle, *J Biomed Mater Res A* 2018;106:746-757 (doi:10.1002/jbm.a.36274): the capsule around intraneural polyimide peaks at **2 weeks** then compacts, with macrophages giving way to CD90+ fibroblasts by 32 weeks. The failure mode is **physical separation of axons from contacts**, not nerve destruction. Christensen et al., *Acta Biomater* 2014;10:4650-4660: USEA in cat sciatic to 350 days with persistent activated macrophages but preserved fibre count.

**No chronic human peripheral interface has ever recorded a C-fibre.** Lacour's e-dura (*Science* 2015;347:159-163) is rat spinal, not human peripheral. Mesh electronics has no peripheral nerve data.

---

## 4. Emerging and less invasive

**Neural dust.** Seo, Neely, Shen, Singhal, Alon, Rabaey, Carmena & Maharbiz, *Neuron* 2016;91:529-539 (doi:10.1016/j.neuron.2016.06.034, PMID 27497221). Mote 0.8 × 3 × 1 mm, transducer at 8.9 mm standoff, **anaesthetised rat**; EMG was convincing, ENG marginal. StimDust (Piech et al., *Nat Biomed Eng* 2020;4:207-222) is 1.7 mm³ and a **stimulator**. Iota Biosciences was acquired by Astellas in 2020; its 2024 IDE is for a bladder **stimulator** (n=3 expanding to at most 10). **There is no published human neural-dust recording.**

**Mesh electronics.** Fu, Hong, Zhou, Schuhmann, Viveros & Lieber, *Nat Methods* 2016;13:875-882 (doi:10.1038/nmeth.3969): stable single-unit mouse brain recording for at least 8 months; Zhou et al., *PNAS* 2017;114:5894-5899: gliosis-free. The "one year of stable single units" claim appears in a protocol paper (*J Vis Exp* 2018;137:e58003) and should be treated as CONTESTED. No peripheral nerve, no human.

**OPM-MEG and magnetospinography.** Boto et al., *Nature* 2018;555:657-661 (doi:10.1038/nature26147) for wearable OPM-MEG. Spinal cord: Sumiya, Kawabata, Adachi et al., *Sci Rep* 2017;7:2192 (doi:10.1038/s41598-017-02406-8), 120-channel SQUID magnetospinography. Adachi & Kawabata, *Front Med Technol* 2024;6:1351905 give the honest engineering: **under 2 fT/√Hz noise floor, 132 channels, 1,000 to 8,000 stimulus repetitions of averaging**, spatial resolution of the order of 10 mm, evoked signals only, and **Aδ fibres have never been detected** because of conduction velocity dispersion. Peripheral: Bu et al., *Front Physiol* 2022;13:798376 (PMID 35370794): OPM noise 17.7 ± 3.5 fT/√Hz, signals around **1 pT**, but n=1 for the sensory nerve action potential and n=2 for the H-reflex.

**NV-diamond.** Barry, Turner, Schloss, Glenn, Song, Lukin, Park & Walsworth, *PNAS* 2016;113:14133-14138 (doi:10.1073/pnas.1601513113): single-neuron magnetic action potentials from **marine worm and squid** axons of 500-1000 µm diameter at micrometre standoff. Best near-DC NV sensitivity is around 9.4 pT/√Hz (Sekiguchi et al., *Phys Rev Applied* 2024;21:064010), which is **50 to 100 times worse than OPMs**, against a target signal of about 1 pT. In vivo human NV nerve recording is not currently plausible. This is the quantitative answer to the "quantum sensing will read the nerve" branch, and it is negative for now.

**MRN.** Filler et al., *Lancet* 1993;341:659-661. MRN images fascicular anatomy, T2/STIR signal and DTI. It is structural. Kwee, Chhabra, Wang, Marker & Carrino, *AJR* 2014;203:1303-1309 (doi:10.2214/AJR.13.12403) found significant between-study heterogeneity and no criteria achieving both high sensitivity and specificity. NS-RADS standardisation: Chhabra et al., *AJR* 2022;219:279-291. **MRN says nothing about firing or nociceptive traffic.**

**Non-invasive decoding.** High-density surface EMG motor unit decomposition is the one genuine non-invasive read of spinal output: Grison, Mendez Guerra, Clarke, Muceli, Ibáñez & Farina, *J Physiol* 2025;603:2281-2300 (doi:10.1113/JP287913), 25.9 ± 5.8 motor units versus 13.9 ± 2.7 for prior state of the art, validated against three 40-channel intramuscular arrays. It reads α-motor neurons: efferent, myelinated and superficial, which is the easy case in every dimension. Functional ultrasound in humans still requires a skull defect (Rabut et al., *Sci Transl Med* 2024;16:eadj3143) and measures haemodynamics, not spikes.

---

## 5. Decoding pain state

**Intracranial, the most relevant result.** Shirvalkar, Prosky, Chin, Ahmadipour, Sani, Desai, Schmitgen, Dawes, Shanechi, Starr & Chang, *Nat Neurosci* 2023;26:1090-1099 (doi:10.1038/s41593-023-01338-z, PMID 37217725, PMC10330878). Four patients with refractory neuropathic pain, Medtronic Activa PC+S, **two bipolar LFP channels at 422 Hz**, 30-second recordings, ACC depth leads plus OFC paddle leads, 89 to 452 recordings over 78 to 184 days.

Results: dichotomised high-versus-low pain classification **AUC 0.673, 0.851, 0.721 and 0.802** across the four participants, driven by sustained **OFC delta power**. Critically, and less often quoted: **regression of continuous pain intensity was poor in all four, R² between −0.2 and 0.1**; acute pain decoding succeeded in only two of four; and the authors concede the models "may be predicting other variables strongly correlated with reported pain metrics such as arousal or attention". Companion comment: *Nat Neurosci* 2023;26:928-929 (doi:10.1038/s41593-023-01340-5, PMID 37217729). Trial design: Shirvalkar et al., *J Clin Med* 2020;9:3155 (PMID 33003443). Related spinal work from the same group: Shukla, Burke, Kunwar, Shirvalkar & Wang, *J Neurosci* 2024;44:e2258232024 (PMID 38960719), five subjects, cervical epidural electrogram, theta-band and theta-gamma coupling mapping volitional movement, not pain.

**fMRI.** Wager, Atlas, Lindquist, Roy, Woo & Kross, *NEJM* 2013;368:1388-1397 (doi:10.1056/NEJMoa1204471, PMID 23574118): the Neurologic Pain Signature discriminated painful heat from warmth with **93-94% sensitivity and specificity**, but only **85% sensitivity and 73% specificity** against social pain. Han et al., *NeuroImage* 2022;247:118844 (doi:10.1016/j.neuroimage.2021.118844, PMID 34942367), n=295: **within-person d=1.45 but between-person d=0.49**; ICC 0.84 same-day with about 70 trials, 0.74 at 5 days, **0.46 at one month with 5 trials**. The authors' own conclusion is that the NPS "is not a surrogate for individual differences in pain reports". Chronic back pain aligns more with affective-motivational systems than with the NPS.

**EEG and evoked potentials.** Mouraux & Iannetti, *J Neurophysiol* 2009;101:3258-3269 (doi:10.1152/jn.91181.2008, PMID 19339457) is the decisive negative result: laser-evoked potentials "do not reflect nociceptive-specific neural activity" and are explained by multimodal saliency plus somatosensory-specific but not nociceptive-specific activity. LEPs remain clinically useful for **spinothalamic pathway integrity** (Treede et al., *Neurophysiol Clin* 2003;33:303-314, PMID 14678844), not for pain magnitude. Machine-learning EEG pain classifiers cluster around **75-80% accuracy** for pain versus no pain, typically with specificity well below sensitivity `[UNVERIFIED at the level of specific studies; the primary sources found were preprints and small-n reports]`.

---

## 6. Honest assessment

**Can we today read, from a nerve or the cord, a signal that specifically corresponds to pain, with enough fidelity to modify it selectively? No.**

Three findings converge.

1. **Nothing chronic reads C-fibres.** A targeted search for human epidural or spinal-cord recording of C-fibre or nociceptive compound action potentials returned **only preclinical animal studies**. Verma et al., *J Neural Eng* 2023;20:026004 recorded pig vagus with noise floors of 0.26 µV rms (microneurography electrode) and 0.11 µV rms (cuff and LIFE) and resolved **only Aβ and B/Aδ components; C-fibres were not recorded**. Jiman et al., *Sci Rep* 2020;10:15501 got carbon-fibre intraneural clusters at 15.1-91.7 µV with conduction velocities of 0.7-8.8 m/s but could not sort single units.

2. **The physics is unfavourable but not absolutely prohibitive, and this is the lead.** Verardo, Romeni & Micera, *iScience* 2025;28:112495 (doi:10.1016/j.isci.2025.112495, PMID 40458190) is the best quantitative treatment. At a cuff 20 µm outside the fascicle, myelinated single-unit action potentials are **20 to 200 times larger** than unmyelinated ones. But at 2 µm from the fibre, intrafascicular electrodes see unmyelinated units **comparable to or larger than** myelinated ones and above 10 µV. Their conclusion is that C-fibre recording is plausible with intrafascicular electrodes and implausible with cuffs, and that its absence to date **may reflect experimental design as much as hardware**.

3. **Even a perfect nerve read would not equal pain.** Nociception is not pain. The NPS loses most of its power between persons; evoked potentials are saliency; the best intracranial chronic-pain decoder achieves AUC 0.67-0.85 for a binary split and **fails outright at regressing pain intensity**. Any closed loop built on a peripheral nociceptive readout would still need a validated mapping from afferent traffic to experienced pain, and that mapping does not exist.

**Hard limits, quantified.** Extracellular amplitude scales roughly with axon diameter squared: C-fibres are 0.2-1.5 µm against 6-12 µm for Aβ. Conduction at 0.5-2 m/s disperses any compound volley over tens of milliseconds, so it phase-cancels over centimetres (Eiber, Grill et al., *PLoS Comput Biol* 2024;20:e1011833). Remak bundling makes waveforms non-separable. The human median nerve carries about 20 fascicles per cross-section with 94% in the smallest size class. Encapsulation peaks at two weeks and separates axons from contacts. Six of seven human USEAs lost functional electrodes within two months.

### Tiering

- **ESTABLISHED:** microneurography of single human C-nociceptors (acute, research only); ECAP recording of Aβ dorsal column volleys and its superiority as a closed-loop control variable through 36 months; RPNI recording at millivolt amplitudes for years; FINE cuff stimulation stability at 2 years; magnetospinography of evoked myelinated responses; HD-sEMG motor unit decomposition; the NPS as a within-person nociception index.
- **CONTESTED:** chronic multi-month USEA recording stability; year-scale single-unit mesh electronics; whether OFC delta genuinely encodes pain rather than arousal; MRN as any kind of pain biomarker; EEG chronic-pain classifiers; whether TIME-class electrodes can reach C-fibres at all.
- **SPECULATIVE:** neural dust for nerve recording in humans; NV-diamond in vivo magnetoneurography; regenerative sieve interfaces in humans; any non-invasive read of spontaneous unmyelinated traffic, which is physically implausible with current or near-term sensors.

---

## The five hardest engineering bottlenecks, and who is attacking each

1. **C-fibre signal amplitude and dispersion.** Micron-scale axons, single-microvolt extracellular fields, 0.5-2 m/s conduction that phase-cancels compound responses. *Attacking it:* Micera and Romeni (EPFL) with the intrafascicular-proximity modelling; Namer and Kutafina (Aachen) plus Pickering (Bristol) on spike sorting and ultrasound-guided microneurography; Bennett and Themistocleous (Oxford) on clinical phenotyping. No company.
2. **Chronic intraneural stability against the foreign-body response.** The capsule peaks at 2 weeks, contacts separate from axons, most human arrays degrade inside 2 months. *Attacking it:* Navarro and del Valle (UAB Barcelona) on quantified foreign-body response; Lacour (EPFL) on soft conformable substrates; Cederna and Kemp (Michigan) sidestepping the problem with muscle-amplified RPNIs; Malliaras and Barone (Cambridge) on conducting-polymer interfaces.
3. **Selectivity within a 20-fascicle nerve.** 94% of human median-nerve fascicles are in the smallest size class and no electrode geometry addresses them individually. *Attacking it:* Normann, Clark and George (Utah) with 100-shank slanted arrays; Tyler (Case Western) with FINE reshaping; Grill (Duke) on field shaping and selectivity modelling; Delgado-Martínez and Navarro on the anatomical substrate.
4. **A validated nociception-to-pain decoder.** Best in class is AUC 0.67-0.85 binary with R² near zero for intensity. *Attacking it:* Shirvalkar (UCSF), Chang and Starr (UCSF), Shanechi (USC) on intracranial biomarkers; Wager (Dartmouth) and Woo (SKKU) on multivariate imaging signatures; Iannetti and Mouraux on the specificity critique any candidate must survive.
5. **Closing the loop on a variable that is actually pain, not dose.** Today's clinical closed loop regulates Aβ recruitment to ±2.8 µV and calls it therapy. *Attacking it:* Saluda Medical (Evoke, over 100 Hz adjustment), Medtronic (Inceptiv at 50 Hz sensing, plus the Percept and Summit RC+S platforms that made the Shirvalkar work possible), Abbott (no commercial ECAP loop), Nevro and Nalu (no sensing), Iota and Astellas (ultrasonic, stimulation only).

## Where a serious programme should push

The highest-leverage unexploited claim in this literature is Verardo, Romeni & Micera 2025: that C-fibre recording fails on cuffs for geometric reasons but should be achievable at 2 µm intrafascicular proximity, and that its absence to date reflects experimental design rather than a physical wall.

**A chronic, high-density, intrafascicular array validated against acute microneurography ground truth in the same nerve is the missing experiment.** Everything downstream, including any nociception-specific closed loop, is blocked on it.
