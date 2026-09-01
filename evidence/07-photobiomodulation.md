# E-07. Photobiomodulation and laser therapy for neuropathic pain

> Literature brief, 1 September 2026. Picks up where E-03 stops. E-03 covers
> **infrared neural stimulation and inhibition** (pulsed 1450-2120 nm,
> photothermal, PMIDs 15789717, 24009039, 28607402, 17659590), **optogenetics**
> and **photopharmacology**. None of that is repeated here.
>
> Every identifier was resolved during preparation: PMIDs and journal, volume
> and pages against NCBI E-utilities; 40 DOIs against Crossref (all HTTP 200);
> NCT records against the ClinicalTrials.gov v2 API; device records against
> openFDA. Nothing is cited from memory. **Every negative claim carries its
> verbatim query in §7**, per EPISTEMICS.md rule 11.
>
> Bears on: HC-3 (structure-targeted beats channel destruction), HC-4
> (realisable transducer), PB-3 (night-time allodynia has a distinct handle).

---

## Bottom line

Photobiomodulation is **not one modality**. It is at least three physically
distinct things sold under one word, and the field's own best mechanistic work
on *analgesia* contradicts the mechanism the field advertises.

The clinical picture in neuropathic pain is unusually clean for a field with
this reputation, because the natural experiment has already run twice.
**Monochromatic infrared energy for diabetic neuropathy** and **808 nm
transcranial laser for stroke** both went from enthusiastic small positives to
adequately powered, properly sham-controlled trials, and both failed. The
transcranial null is Cochrane **high**-certainty at n=1420. The infrared null is
three independent double-blind sham trials plus a CMS national non-coverage
determination.

What survives is narrower and more interesting than the marketing: a
**reversible, small-fibre-selective conduction block produced by mitochondrial
depression at high irradiance**, which is the opposite of the "light boosts
ATP" story, and which is fibre-selective in the direction pain needs.

---

## 1. Terminology: what is actually being claimed

| Term | Typical parameters | What it physically is |
|---|---|---|
| PBM / LLLT / "cold laser" / class 3B | 600-1100 nm, CW or superpulsed, 5-500 mW, ≤100 mW/cm², 1-10 J/cm² | Sub-thermal photochemistry, claimed |
| Red/NIR LED panels | 630-850 nm, 10-100 mW/cm² | Same claim, incoherent source, consumer channel |
| MIRE (monochromatic infrared energy) | 890 nm LED, **1.5 J/cm²/min** at manufacturer preset (PMID 18579924) | Superficial NIR, borderline thermal |
| HILT / class IV | 810-1064 nm, **0.5-25 W**, tens of J/cm² | Demonstrably **photothermal** |
| INS (covered in E-03) | **1450-2120 nm**, pulsed, 0.3-0.5 J/cm² per pulse | Photothermal transient |

**The distinction from E-03's infrared neural inhibition is clean.** The
wavelength bands do not overlap: INS operates where water absorption is high
(1.45-2.1 µm) and works *because* of a rapid local temperature transient. PBM
operates inside the optical window (600-1100 nm) where water absorption is
minimal, and claims to work *without* heating. The FDA classification text
makes the non-thermal claim regulatorily binding (§5), so **any PBM device that
works by heating is, on its own regulatory theory, working off-label.**

**HILT is the honest exception and should not be pooled with PBM.** Under a
class IV laser, skin over an equine flexor tendon rose **+3.5 °C** (Zielińska
et al., *Animals* 2022;12(10):1253. PMID 35625098), and pigmented skin heated
while non-pigmented skin cooled, p<0.001 (PMID 34209183). Meta-analyses pooling
5 mW class 3B trials with 12 W class IV trials under "laser therapy" are
pooling two different physical interventions.

**The dose claim is not stable.** Hamblin's own parameter review states the
field variously recommends "less than 100 mW/cm² and an energy density of 4 to
10 J/cm² **at the level of the target tissue**" or "as much as **50 J/cm² at
the tissue surface**" (Zein, Selting & Hamblin, *J Biomed Opt* 2018;23(12):1-17.
PMID 30550048). A therapeutic window whose recommended values differ by a
factor of 12, quoted at two different anatomical planes, is not a dose
specification.

---

## 2. Mechanism, assessed critically

### The dominant claim, and how badly it is supported

Cytochrome c oxidase as the red and near-infrared chromophore is Karu's, from
action-spectrum work on cultured cells (PMID 16144476; PMID 16125966), with the
most-cited mammalian neuronal support from Wong-Riley et al., *J Biol Chem*
2005;280(6):4761-71. PMID 15557336.

Then, from inside the field:

> **Quirk BJ, Whelan HT. "What Lies at the Heart of Photobiomodulation: Light, Cytochrome C Oxidase, and Nitric Oxide." *Photobiomodul Photomed Laser Surg* 2020;38(9):527-30. PMID 32716711.**
>
> Verbatim: "**No reliable demonstration of any PBM-related light-induced mechanistic effect on CCO has been reported.** Studies on PBM have proven to be either nonreproducible, of questionable relevance, or involve wavelengths unlikely to be operative in vivo."

Whelan led the NASA LED programme. This is not a hostile source. Hamblin then
published an editorial titled "Photobiomodulation Therapy Mechanisms **Beyond**
Cytochrome c Oxidase" (PMID 34818111), whose co-author's listed affiliation is
a PBM device company.

An independent negative: Gutiérrez-Menéndez et al., *Front Neurosci*
2022;16:897225. PMID 35600629. Five days of PBM in 61 rats produced **no
difference in cytochrome c oxidase histochemistry or c-Fos** in prefrontal
cortex or hippocampus, in either sex. No competing interests.

### The competing chromophore is better supported, and it is a nociceptor channel

Wang Y, Huang YY, Wang Y, Lyu P, Hamblin MR. *Biochim Biophys Acta Gen Subj*
2017;1861(2):441-9. PMID 27751953. 980 nm raised cytosolic and lowered
mitochondrial calcium; the effect was abolished by **capsazepine (TRPV1)** and
**SKF96365 (TRPC)**, by cooling to 4 °C and by pre-warming to 42 °C, none of
which touched 810 nm. Peak dose for 980 nm was **0.03-0.3 J/cm², 10 to 100
times lower than 810 nm's 3 J/cm²**. Conclusion: 980 nm acts on
**temperature-gated ion channels via intracellular water**, not on cytochrome c
oxidase. TRPV1 recurs (PMID 41345138).

**That matters here more than anywhere.** TRPV1 is a nociceptor channel. A
light-gated thermal microgradient acting on TRPV1 in a sensory nerve is as
likely to *cause* sensation as to abolish it, which is the same structural
irony E-03 flags for sonogenetics.

### The biphasic dose response: object to the move, not the phenomenon

The phenomenon is real in vitro (PMID 20011653; PMID 22461763). The **move** is
not. Zein, Selting and Hamblin conclude that ineffective studies in
high-mitochondrial tissue "appeared to be more often due to **over**-dosing
than to under-dosing" (PMID 30550048).

Combined with the biphasic claim, this makes the theory unfalsifiable by any
negative trial: too little light and too much light both predict null, and the
window is not specified with error bars at the target plane. **A null is only
informative against a dose pre-registered as inside the window and measured at
the nerve.** No neuropathic-pain trial found in this brief did that.

### The one mechanism that fits analgesia, and it contradicts the marketing

> **Chow RT, David MA, Armati PJ. *J Peripher Nerv Syst* 2007;12(1):28-39. PMID 17374099.** 830 nm CW on cultured rat DRG neurons produced **reversible axonal varicosities**, a significant **fall** in mitochondrial membrane potential, and **blockade of fast axonal flow**, selectively in **small and medium diameter, TRPV1-positive** neurons.

> **Holanda VM, Chavantes MC, Wu X, Anders JJ. *Lasers Surg Med* 2017;49(5):516-24. PMID 28075022.** 808 nm at **270 mW/cm² at the nerve** in rat spared-nerve-injury rapidly reduced cold allodynia and mechanical hyperalgesia. Varicosities formed in neurites of DRG cells **≤30 µm first**, larger cells only at the longest exposure. Verbatim: "**Mitochondrial metabolism was significantly lower compared to controls for all LT groups.**" Mechanical allodynia was **not** affected at any timepoint, and the cold and pinprick effect washed out within 5 days.

Two things follow.

**This is small-fibre-selective in the therapeutically correct direction** — the
same inversion of the electrical constraint that E-03 identifies as infrared
inhibition's single best argument, reached at wavelengths that penetrate far
better than INS's 1875 nm. That is the real finding in this literature.

**And the analgesic mechanism is mitochondrial depression, not stimulation.**
The field sells "PBM increases ATP". Its own best analgesia mechanism is "PBM
lowers membrane potential until axonal transport fails". Those are opposite
claims about the same organelle, and only the biphasic dose response reconciles
them, which is an enormous amount of unearned work for one unfalsifiable
principle to do.

---

## 3. Clinical evidence in neuropathic pain

### The two decisive negatives

**(a) Carpal tunnel, the only Cochrane review of LLLT in a neuropathic condition.**
Rankin, Sargeant, Rehman, Gurusamy. *Cochrane Database Syst Rev* 2017;8(8):CD012765. PMID 35611937, PMC6483673. 22 trials, 1153 participants; 9 trials (525) LLLT against placebo.

| Outcome, under 3 months | MD (95% CI) | GRADE |
|---|---|---|
| Symptom Severity Score (1-5) | −0.36 (−0.78 to **0.06**) | very low |
| Functional Status Scale (1-5) | −0.56 (−1.03 to −0.09) | very low |
| VAS pain (0-10) | −1.47 (−2.36 to −0.58) | very low |
| Grip strength | +2.58 kg (1.22 to 3.95) | low |

Verbatim: "The evidence is of very low quality and we found **no data to support any clinical effect** of LLLT in treating CTS... There is low or very low-quality evidence to suggest that **LLLT is less effective than ultrasound**." No conflicts declared.

**(b) 808 nm transcranial laser, the field's only well-powered high-certainty result anywhere.**
He H et al. *Cochrane Database Syst Rev* 2025;7(7):CD012426.pub2. PMID 40704566, PMC12288111. 4 RCTs, **1420 participants**, all 808 nm, all sham-controlled. Unfavourable functional outcome at 90 days **RR 0.93 (0.85-1.02), I²=10%, high-certainty evidence.** Mortality RR 0.96 (0.72-1.28). Government-funded, no conflicts.

Not neuropathic pain, but the only place PBM has been tested at adequate power against a real sham with a hard outcome. The answer was no.

### Painful diabetic neuropathy: the natural experiment

Positive, uncontrolled or weakly controlled: PMID 15251618; Leonard et al., *Diabetes Care* 2004;27(1):168-72, PMID 14693984; PMID 15778471; PMID 16504836. Note that even Leonard's positive trial found **no significant benefit in the more severely affected subgroup**.

Then the properly designed trials:

- **Clifft et al. *Diabetes Care* 2005;28(12):2896-900. PMID 16306551.** n=39, double-blind, placebo device. Both arms improved; **no between-group difference at any timepoint.**
- **Lavery et al. *Diabetes Care* 2008;31(2):316-21. PMID 17977931.** n=69 randomised, 60 completers, 90 days home use, double-blind sham. "**No significant differences... for quality of life, MNSI, VPT, SWM, or nerve conduction velocities**" (all P>0.05).
- **Franzen-Korzendorfer et al. *Ostomy Wound Manage* 2008;54(6):16-31. PMID 18579924.** Within-patient, one foot active and one sham. Null on transcutaneous oxygen, pain and sensation; both feet improved from baseline. First author's affiliation is a device company, which makes the null more credible, not less.

**The pattern is E-03's pattern exactly: the effect appears when blinding is absent and disappears when it is present.**

Two later sham-controlled positives need care. Rastogi et al., *Neurol India* 2021;69(5):1331-7. PMID 34747807 (n=30 completing, no declared conflict) reported VAS decline 5.1 against 3.0 (p=0.01) but **no increase in intraepidermal nerve fibre density**, and a sham arm that itself dropped 3.0 points. Oggiam et al., *Pain Manag Nurs* 2025;26(1):45-54. PMID 39322522 is the largest (n=144) but the control arm received "the same treatment protocol **without** application", which is a no-treatment control inside a physiotherapy protocol, not a sham device.

Recent independent work is null on the comparison that matters: Almasi et al., *Lasers Med Sci* 2025;40(1):503. PMID 41320698, n=55, "between-group differences were not significant (p=0.292)".

### Chemotherapy-induced peripheral neuropathy

The entire literature is 18 PubMed records (§7).

- **Argenta et al. *Gynecol Oncol* 2017;144(1):159-66. PMID 27887804.** n=70, **quadruple-masked** (NCT02000908), sham used a heat probe with the device activated for visual and audible realism, which is a genuinely well-constructed sham. mTNS at 8 weeks **−6.8 (−52.6%) against +0.2 (0.0%)**, p<0.001, sustained at 16 weeks. Device: a class IV commercial laser.
  **The reason to distrust it is the sham arm.** It changed by −0.1, +0.2 and 0.0 at three consecutive timepoints. A sham arm with literally zero movement on a composite containing patient-reported items does not resemble any placebo arm in the neuropathic-pain literature. Funding `[UNVERIFIED: Europe PMC returns grantsList null and fundingList null; not open access.]`
- **Teng, Egger, Blinman, Vardy. *Support Care Cancer* 2022;31(1):52. PMID 36526802.** n=44, sham-controlled, no competing interests. Response **48% laser against 53% sham at 6 weeks**, 45% against 33% at 12. Designed as non-comparative against a 5% null, so its headline says only that symptoms improve over time. **On the between-arm comparison it is a null.**
- NEUROLASER (PMID 35312857): n=32 pilot, mTNS rose in *both* arms. NEUROLIGHT (PMID 41831101): n=60, **no sham arm**, compares 6 against 8 J/cm² and cannot speak to efficacy.

### Trigeminal neuralgia and post-herpetic neuralgia

Taddeucci et al., *Lasers Med Sci* 2026;41(1):19. PMID 41629512. 9 studies, 387 patients, meta-analysis of 5: **MD −2.17 (−3.30 to −1.04), p=0.0002, I² = 92%.** Sham in 6 of 9; **7 of 9 also received drugs**; parameters "varied widely and were often incompletely reported".

I² = 92% means the pooled estimate describes no single trial. This is the largest apparent effect in the neuropathic PBM literature and also the least interpretable.

The same review states: "**No studies involving patients with postherpetic neuralgia met the inclusion criteria.**"

### CRPS

**Essentially nothing.** One randomised sham-controlled trial: Khoramdel, Ravanbod, Akbari. *J Hand Ther* 2025;38(4):791-8. PMID 40118675. **n=24**, single-blind, HILT at 5 W and 20 J/cm² plus mirror therapy against sham plus mirror therapy, **6 sessions**. VAS change −4.2 ± 1.2 against −1.4 ± 0.6. Its stated conclusion is "conclusive evidence". A 24-patient, six-session, single-blind trial with an unblinded operator is not conclusive evidence of anything, and 5 W is thermal.

A citation-laundering risk this programme should not repeat: Cheng et al., *J Pain* 2021;22(7):763-77. PMID 33636371 asserts that red light "has been shown to reduce pain in neuropathies and **complex regional pain syndrome-I**". The primary basis for the CRPS half of that sentence is not visible in any systematic search reported here.

### Sham adequacy, and the single most telling registry entry

Laser sham is unusually easy: identical housing, indicator lights, fan, no emission. So the field *can* blind. Whether it does:

> **NCT02798393.** Sponsor a device manufacturer. "Randomized Double-Blind Study of the Efficacy of Near Infrared Phototherapy on Sensation and Pain in Type 2 Diabetic Neuropathy". Quadruple masking. **Status: TERMINATED. `whyStopped`: "Study blind compromised."**

A manufacturer terminated its own quadruple-masked neuropathy trial because the blind broke. That is the most informative single datum on sham adequacy in this field, and it is the manufacturer's own filing.

### The placebo benchmark, and what it does to the industry trials

Häuser et al., *Pain* 2011;152(8):1709-17. PMID 21429668. 70 RCTs, 10,297 patients in painful diabetic neuropathy. Pooled placebo-arm improvement **17.11 (16.41-17.90)** on 0-100; active-drug arms 22.54. **Placebo accounted for 62% of the drug-arm response.** Cepeda et al., PMID 22390269, puts the placebo responder rate at **20% (14.6-25.8%)**.

Now the pivotal trial behind a marketed neuropathy laser, **NCT02461225** (registry results; no journal publication found, §7):

| | Active (n=19) | Placebo laser (n=11) |
|---|---|---|
| Baseline VAS (0-100) | 68.89 ± 12.49 | 65.91 ± 10.69 |
| ≥30% responders | 18/19 | 4/11 |
| VAS change at 6 weeks | **−60.97 ± 23.28** | **−9.09 ± 34.06** |

The active arm outperformed the *pooled active-drug* response across 70 trials by a factor of **2.7**, and the placebo arm underperformed the *pooled placebo* response by a factor of **1.9**. Both deviations point the same way. A 19:11 split is also odd to describe as randomised at n=30. **This is the signature of a trial whose control condition is not behaving like a control, and it is the evidence base for a marketed device.**

### NNT and clinical importance

**No NNT is derivable from any systematic review of PBM in a neuropathic indication.** Against Farrar's standard of at least 30% or 2 points on 0-10 (PMID 11690728), the Cochrane carpal tunnel VAS estimate (−1.47, upper bound −0.58) sits below the minimum clinically important difference across most of its interval, and Cochrane says where such thresholds were met the estimates "are likely to be overestimates".

---

## 4. Dose, penetration and the physics: the one place this programme's case is strong

### The best direct human measurement, from proponents

**Haslerud, Naterstad, Bjordal, Lopes-Martins et al. *Photomed Laser Surg* 2017;35(10):567-75. PMID 28677985.** 54 Achilles tendons in 27 healthy adults, transmitted energy measured skin to skin:

- **810 nm, 200 mW CW: 0.24-0.25%** of incident energy transmitted
- **904 nm, 60 mW superpulsed: 0.34-0.39%**

These authors are PBM proponents. **This is a proponent's own measurement showing roughly 2.6 orders of magnitude loss through about 2 cm of human tissue.**

### The arithmetic

Fitting a single effective exponential to the 810 nm figure over a ~20 mm path: 0.0025 = e^(−µ_eff·2 cm), so **µ_eff ≈ 3.0 cm⁻¹ and penetration depth ≈ 3.3 mm.**

| Depth | Fraction of surface fluence | From a 10 J/cm² surface dose |
|---|---|---|
| 3 mm | about 40% | about 4.0 J/cm² |
| 5 mm | about 22% | about 2.2 J/cm² |
| 10 mm | about 5% | about 0.5 J/cm² |
| 20 mm | about 0.25% | about 0.025 J/cm² |

**Caveat so this is not over-read:** the fit ignores lateral loss (over-estimating attenuation) and backscatter enhancement, which raises fluence above incident in the first millimetre (under-estimating surface-referenced dose). Both are large. Order of magnitude only.

Monte Carlo work is often cited here, and **this brief originally cited it wrongly.** Ash, Dubec, Donne, Bashford. *Lasers Med Sci* 2017;32(8):1909-18. PMID 28900751, PMC5653719 is quoted everywhere for a "5378 µm maximum penetration depth". Read directly:

- It is a **simulation**, not a measurement, of an intense pulsed light source on **skin type 2 only**.
- Its wavelength sweep is **300 to 750 nm**. It contains **no data at 810, 904 or 1064 nm**, which are the wavelengths that matter here.
- The 5378 µm figure is at **750 nm at the 1% intensity contour**, meaning 99% of the light is already gone. Its Discussion gives the other number: **"5 mm using the 1% criterion and 0.37 mm using the 13.5% criterion"**. The 1/e² depth is **370 micrometres**.
- Its stated purpose was a **safety risk assessment**, concluding that "photons are unable to reach vital organs". It was written to show light does *not* penetrate.

Its genuinely useful result is on beam width: a 10 mm beam delivers **73-88%** of an infinitely wide beam's fluence at 1-3 mm depth, so below about 10 mm spot size costs depth and above it buys almost nothing.

**A properly layered calculation from Jacques' 2013 optical-property review gives a more defensible answer** and, importantly, one that is *more* favourable than the figure above: effective penetration depth of **2.2 mm in dermis and 3.2 mm in subcutis at 810 nm**, giving surviving fractions of **31% at 3 mm, 17% at 5 mm and 3.6% at 10 mm**. Three independent lines (Jacques-derived layered model, Sandell and Zhu's measured in vivo ranges, Girasol's 2026 measured coefficients) converge on an effective penetration depth of **2 to 5 mm** across 630 to 1064 nm.

**And 1064 nm is not worse than 810 nm**, contrary to the usual water-absorption story: water absorption rises sixfold from 810 to 1064 nm, but reduced scattering falls faster, so net penetration is slightly *better*. `[Caveat: this excludes lipid absorption, which peaks near 1040-1210 nm and could reverse the ordering in a fat-rich foot. The available fat absorption data file had ambiguous units and was deliberately excluded rather than risk a tenfold error.]`

### The finding that matters more than the penetration depth

**The sceptical case is not that light cannot reach the nerve. It is that
nobody knows what dose arrived, to within about two orders of magnitude.**

Taking only the two ends of the *published measured range* for human skin at
630 nm (Sandell & Zhu, PMID 22167862, Table 1: absorption 0.05 to 1.11 cm⁻¹,
reduced scattering 2.26 to 20.95 cm⁻¹), effective penetration depth ranges from
**17.0 mm to 1.17 mm**. The same nominal protocol therefore delivers between
**0.14 and 7.45 J/cm² at 5 mm — a 54-fold spread**, from a single 10 J/cm²
surface dose, driven entirely by where a patient sits within already-published
human variability.

**The claimed therapeutic window is about 100-fold wide. The patient-to-patient
optical uncertainty is the same order as the entire window.** For any
individual, you cannot distinguish sub-threshold from optimal from inhibitory.
That, rather than penetration, is why this field cannot settle its own dose
question, and it is why the trial design in §6 insists on measuring
transmission per participant rather than assuming it.

At 10 mm the spread is 2900-fold, and delivery collapses to about 3.6% even in
the favourable case. **Deep targets are genuinely out of reach; superficial
ones are genuinely reachable; and the difference between two superficial
patients can be 54-fold.**

### The consequence, stated plainly

**A sural or superficial fibular nerve 3 to 5 mm below the dorsum of the foot
sits inside the reachable zone**: roughly 20 to 40% of surface fluence,
comfortably within the 1-10 J/cm² window at a realistic surface dose, and well
inside Ash's 5.4 mm modelled maximum.

**This programme's target geography is the one geography where PBM is not
physically implausible.** By the same arithmetic, transcranial, spinal and
deep-joint PBM deliver 10⁻³ or less of the claimed dose to their nominal
targets, which is one plausible reading of why the 1420-patient transcranial
trial set was flatly null.

### Wavelength and pigment, where the field contradicts itself

- 830 nm transmits measurably better than 660 nm through human skin and tendon in vivo, and transmitted power differed significantly by **melanin index, p<0.0001** (Girasol et al., PMID 38194210).
- A second study disagrees: Hu, van Zeyl, Valter, Potas. *J Biophotonics* 2019;12(7):e201900010. PMID 30851081 found 660 nm penetration "unaffected by skin tone" but affected by sex.

**These are in genuine conflict and the field has not resolved it**, which alone
should end any claim that PBM dosimetry is settled.

### Does delivered dose match the positive trials?

No, and it cannot be checked, because positive trials report **surface**
parameters while the therapeutic window is specified at the **target**. Given a
3.3 mm penetration depth, the field's two prescriptions differ by more than an
order of magnitude at any plausible nerve depth. **No neuropathic-pain trial in
this brief measured or estimated fluence at the nerve.**

---

## 5. Regulatory and commercial reality

**The classification text is the story.** openFDA, product code **NHN**,
regulation 21 CFR 890.5500, **Class II**: "Powered Light Based Laser
Non-Thermal Instrument With Non-Heating Effect For **Adjunctive** Use In Pain
Therapy... provides **non-heating and non-thermal effect**... **It does not
provide therapeutic topical heating.**"

Three things follow. Clearance is for **adjunctive** pain therapy, not primary
treatment. It is 510(k), meaning **substantial equivalence to a predicate, not
proof of efficacy**. And it is legally predicated on a **non-thermal** effect,
which sits awkwardly beside HILT and beside the 270 mW/cm² dose in the field's
best analgesia mechanism paper.

From openFDA, a device explicitly named for diabetic peripheral neuropathy now
holds a 510(k) (K251903, decided 2026-02-19, code NHN). **Its supporting
clinical data are registry postings. A PubMed search returns 20 records, none
of which publishes those neuropathy trials** (§7). The evidence supporting a
marketed neuropathy device exists on ClinicalTrials.gov and nowhere in the
peer-reviewed literature.

**Payer verdict, the harshest available.** CMS National Coverage Determination
**270.6**, effective 24 October 2006: infrared and near-infrared devices
including monochromatic infrared energy are **nationally non-covered** for
diabetic and non-diabetic peripheral sensory neuropathy, including pain arising
from those conditions. `[Verbatim NCD text UNVERIFIED: cms.gov returned HTTP 403
to automated retrieval. Date, CAG number and direction come from search-result
summaries, not the page itself.]`

`[UNVERIFIED and incomplete: consumer red-light panel regulatory status and FDA
or FTC enforcement history were not queried. Treat §5's enforcement coverage as
a gap in coverage, not as a finding that no enforcement actions exist.]`

---

## 6. Verdict

### ESTABLISHED
- Red and near-infrared light at 600-1100 nm penetrates human soft tissue with a penetration depth of roughly 3-5 mm; about 0.25% of 810 nm energy crosses 2 cm (PMID 28677985; PMID 28900751).
- 830 nm CW reversibly blocks fast axonal transport and lowers mitochondrial membrane potential **preferentially in small-diameter TRPV1-positive DRG neurons** (PMID 17374099; PMID 28075022).
- 808 nm transcranial laser does **not** improve outcome after ischaemic stroke: RR 0.93 (0.85-1.02), n=1420, **high** certainty (PMID 40704566).
- Monochromatic infrared energy is **not** superior to sham in diabetic neuropathy across three double-blind trials (PMIDs 16306551, 17977931, 18579924), and is nationally non-covered by CMS.
- LLLT for carpal tunnel: very low certainty, no supported clinical effect, possibly inferior to ultrasound (PMID 35611937).
- HILT is photothermal: +3.5 °C measured, pigment-dependent (PMIDs 35625098, 34209183).
- The placebo response in painful diabetic neuropathy is large and characterised: 17.1/100 pooled, 20% responder rate (PMIDs 21429668, 22390269).

### CONTESTED
- Whether cytochrome c oxidase is the operative chromophore at all.
- Whether PBM beats sham in trigeminal neuralgia (MD −2.17 but I²=92%, mostly add-on to drugs).
- Whether PBM beats sham in chemotherapy-induced neuropathy (one positive with an implausibly inert sham, one null).
- Whether skin pigmentation materially changes delivered dose.

### SPECULATIVE
- PBM for CRPS. One n=24 single-blind thermal-laser trial and nothing else.
- PBM for post-herpetic neuralgia. A 2026 review found **zero** eligible RCTs.
- Any claim that a specific dose at a specific wavelength is therapeutic at a peripheral nerve.

### The probability

**That PBM produces a clinically meaningful effect, beating a 30% or 2-point
threshold against an adequate sham with blinding verified, in some neuropathic
indication: about 20%.**

Against: both adequately powered sham-controlled programmes failed; the
headline chromophore is unsupported by the field's own reviewers; the largest
positives sit in trials with anomalous sham arms, manufacturer sponsorship or
unpublished data; and the biphasic dose response makes the theory
unfalsifiable in practice.

For: the physics **does** permit a therapeutic dose at a superficial foot nerve,
unlike almost every other PBM target; the small-fibre-selective conduction
block is real, replicated and points the right way for pain; and it is
genuinely under-tested at the parameters that produce it, because most clinical
trials use doses two orders of magnitude below the 270 mW/cm² at which the
block appears.

Conditional on a trial delivering at least 270 mW/cm² **at the nerve** and
measuring it: **about 35%.** Conditional on a trial reporting the 1-10 J/cm²
surface doses typical of the current literature: **about 10%.**

**If photobiomodulation works in neuropathic pain, it works as a transient
optical nerve block at doses the field mostly does not use, in territory the
field mostly does not target, by a mechanism the field mostly does not claim.**

### The single best-designed trial

**Indication:** painful distal symmetric diabetic polyneuropathy of the feet,
small-fibre predominant. Superficial, bilateral, a measurable placebo benchmark
and a target 3-5 mm deep.

**Design:** randomised, **within-patient crossover with contralateral-limb
control**, plus a parallel confirmation cohort to guard against carry-over.

**Dose, pre-registered and measured:** 810 nm CW titrated to deliver **at least
270 mW/cm² at the nerve**, with fluence at depth estimated per participant from
a calibrated transcutaneous transmission measurement at the treatment site, not
assumed from surface output. Skin phototype and dorsum thickness as
pre-specified covariates. Publish the per-participant delivered-dose
distribution.

**Sham:** identical housing, emitter shuttered, matched surface warming so
thermal sensation is equalised, with the thermal match **verified by
thermography rather than asserted**. **Blinding integrity is a pre-registered
primary outcome**, tested with Bang's index in both arms and reported whatever
it shows. Not optional, given NCT02798393.

**Primary outcome:** proportion achieving at least 30% reduction in weekly
average NRS at 8 weeks, with the sham responder rate reported against the 20%
benchmark. **Pre-specify that a sham responder rate below 10% triggers an
integrity review rather than a positive conclusion.**

**Mechanistic co-primary:** quantitative sensory testing separating small-fibre
(thermal, mechanical pain threshold) from large-fibre (vibration, monofilament)
function, plus intraepidermal nerve fibre density. If the mechanism is
small-fibre conduction block, **thermal thresholds should shift and vibration
should not.** That is the severe test, and one the intervention would fail if it
were working by expectation.

**Size:** about 180 per parallel cohort for 80% power on a 20-percentage-point
responder difference over a 20% sham rate.

**Governance:** results posted regardless of outcome, manufacturer excluded
from data custody, analysis pre-specified and independently held.

---

## 6b. The regulatory position, which is more damning than the trial record

Every identifier below was retrieved from the openFDA API, FDA document PDFs at
`accessdata.fda.gov`, the eCFR versioner API, or EUR-Lex.

### The category runs on a 1983 rule for a heating lamp

**21 CFR 890.5500**, verbatim: "An infrared lamp is a device intended for
medical purposes that emits energy at infrared frequencies (approximately 700
nanometers to 50,000 nanometers) **to provide topical heating**."

Two product codes with opposite definitions sit under that one regulation:

| Code | Device name, verbatim | 510(k)? | Clearances |
|---|---|---|---|
| **NHN** | "Powered Light Based Laser Non-Thermal Instrument With Non-Heating Effect For Adjunctive Use In Pain Therapy" | Required | 54 |
| **ILY** | "Lamp, Infrared, Therapeutic Heating" | **Exempt since 30 Dec 2019** | 229 |

NHN's own FDA definition concedes the mismatch: it "does not provide
therapeutic topical heating", while "the classification regulation for infrared
lamps describes a device that emits energy in the infrared wavelength to provide
topical heating". The one device cleared for a neuropathic indication operates
at **405 nm and 640 nm**, both *below* the regulation's 700 nm floor, delivering
the *opposite* of its stated effect, under its authority.

**The 2019 exemption is visible in the data.** ILY clearances ran 5 to 11 per
year from 2012 to 2017, then **zero in 2018, 2019 and 2021** and about one per
year since. The high-intensity class IV therapy laser market now needs no FDA
review at all, provided it stays inside the heating claim.

### Every high-intensity laser is cleared as a heating lamp, not as photobiomodulation

LiteCure/LightForce (K173067), K-Laser (K120604), Aspen (K142078) and Avant
(K123474) are all in **ILY**, with the generic boilerplate: "provide topical
heating for the purpose of elevating tissue temperature for a temporary relief
of minor muscle and joint pain". **Nothing in the HILT segment is cleared for
photobiomodulation. They are cleared to warm tissue.** Any meta-analysis pooling
class 3B and class IV devices is pooling two legally and physically distinct
interventions.

### Exactly one neuropathic-pain clearance exists, and it is narrower than it sounds

**Erchonia DPN Laser, K251903, decided 19 February 2026**, product code NHN.
Verbatim indication: "indicated while using the red and violet diode
simultaneously **for prescription home use as an adjunctive treatment in
providing temporary relief of diabetic peripheral neuropathy foot pain**."

It carries a real trial: randomised, double-blind, placebo-controlled,
multi-centre, **n=64**, 42 self-administered treatments over 3 weeks, primary
endpoint at least 30% VAS reduction at week 3. **Result 72.73% against 32.26%.**
Two non-serious adverse events.

**Relieving the pain of neuropathy is not treating neuropathy, and that is
FDA's own explicit position**, from the Vevazz warning letter (MARCS-CMS
592118, 26 December 2019), verbatim:

> "While pain may be a symptom of neuropathy or other tissue damage, use of the
> Contour to temporarily relieve a symptom does not treat the underlying disease
> or condition causing the symptom. **The treatment of neuropathy is a different
> intended use than the temporary relief of pain** ... To date, FDA is unaware of
> any low level LED light therapy device approved or cleared for the treatment
> of neuropathy."

K251903 does not disturb that. **Nothing is cleared for chemotherapy-induced
peripheral neuropathy, post-herpetic neuralgia, trigeminal neuralgia or CRPS.**
Verified: `device_name:"photobiomodulation"` returns `NOT_FOUND`;
`device_name:"DPN"` returns K251903 alone.

The contrast case shows what a real neuropathic-pain authorisation requires:
**Nevro Senza, PMA P130022/S039**, approved 2021, indicated for pain "associated
with diabetic neuropathy" — Class III, the only pathway with a statutory
efficacy standard.

### What clearance is actually based on

From the FTC's own complaint in *FTC v. Physician's Technology* (2:20-cv-11694,
E.D. Mich.), paragraph 24, verbatim: the 510(k) pathway "**does not require
clinical data demonstrating efficacy or safety, only a showing that a new device
is 'substantially equivalent' to an existing device already legally marketed**".

Worked examples from the actual record:

- **K232813** (2024, carpal tunnel): "Substantial equivalence ... has been
  established through the results of **nonclinical testing**." The predicate is a
  2003 device and the summary asserts the indications are identical.
- **K241057** (2025, neck, shoulder and carpal tunnel): "**No clinical study is
  included in this submission.**"
- **K180197**: "Erchonia FX-635 is **substantially equivalent to itself**".
- **K190572** broadened the indication to all "nociceptive musculoskeletal pain"
  by aggregating three pre-existing studies, total n=213, done for three
  different body sites.
- **19 of 54 NHN clearances filed a 510(k) statement rather than a summary**, so
  their public file contains no evidence basis, no predicate discussion and
  nothing else. This includes several of the most-marketed devices.

**FDA knows.** Its draft guidance "Photobiomodulation (PBM) Devices — Premarket
Notification [510(k)] Submissions" (Docket FDA-2022-D-3116) has been **draft
since January 2023**, still marked "Not for implementation. Contains non-binding
recommendations."

### Consumer red-light panels are registered, not cleared

Joovv (establishment 3014184914), Mito Red Light (3015313684) and PlatinumLED
(3015619571) all list under **ILY with `k_number: None`**. None holds a 510(k).

**21 CFR 807.39**, verbatim: "**Registration of a device establishment or
assignment of a registration number does not in any way denote approval** of the
establishment or its products. Any representation that creates an impression of
official approval because of registration or possession of a registration number
is misleading and **constitutes misbranding**."

Against which, one brand states its lights "**Achieve** FDA Class II Medical
Device status" and another answers "Is Joovv FDA registered?" with "Yes. Joovv
products are registered as class II devices."

The General Wellness guidance (final, 6 January 2026) is a weaker shield than
assumed. Verbatim: "**A product's inclusion under the general wellness policy in
this guidance does not establish that it has been shown to be safe and/or
effective for its intended use.**" And its risk prong excludes products posing
"risks from lasers or radiation exposure", or whose labelling includes
"references to specific diseases, clinical conditions, or diagnostic
thresholds".

**The exemption may not even fit.** 21 CFR 890.9 voids it when the device "is
intended for a use different from the intended use of a legally marketed device
in that generic type" or "operates using a **different fundamental scientific
technology**". A 660 nm panel sold on a non-thermal cytochrome c oxidase
mechanism is below the 700 nm floor and asserts the opposite mechanism to
topical heating.

### Enforcement: the mechanism is the exemption collapsing

Four warning letters follow one template — *you left the heating claim, so you
lost the exemption*. **Diowave** (CMS 712715, 26 Sept 2025), verbatim: "the
Diowave 100 WLS and Diowave 250 WLS devices **do not provide topical heating.
Instead, they use a different fundamental scientific technology.**" Its
marketing had claimed "laser therapy is the only treatment in medicine that
actually heals living tissue". **Spectra Therapy** (CMS 698026, 22 July 2025)
had claimed it "can markedly decrease the pain of neuropathy in the lower
extremeities [sic]" and "can **cure** both acute and chronic inflammatory
issues". Also **Curewave** (CMS 593692) and **Mectronic** (CMS 707997), the
latter drawing the verbatim response that "**FDA is currently unaware of any
evidence that could support the above intended uses**".

The FTC case is *Willow Curve*: **$22,000,000 judgment**, suspended on payment
of $200,000 each, permanently enjoining claims about "severe or chronic pain due
to ... diabetic neuropathy, nerve damage, fibromyalgia, shingles" absent
randomised, double-blind, placebo-controlled human testing.

### The EU is not better, and in one respect is worse

Under **MDR Annex VIII Rule 9**, therapeutic energy-emitting devices are
**Class IIa**, or IIb for lasers. **Article 61(4)** mandates clinical
investigations only "In the case of implantable devices and class III devices",
so **a PBM device is never required to run a trial**. Equivalence-by-literature
is permitted under Article 61(3)(a).

And **nothing is published**. **Article 32(1)** requires a public Summary of
Safety and Clinical Performance only "For implantable devices and for class III
devices". PBM devices are IIa or IIb, so no SSCP exists, and EUDAMED's public
records expose UDI, trade name, manufacturer and risk class but **no indication,
intended purpose or clinical evidence**. **There is no EU counterpart to the FDA
510(k) summary and Indications for Use form**, so the EU publishes strictly less
than the United States about what these devices are for.

The cosmetic-use common specifications (Implementing Regulation (EU) 2022/2346)
carry a carve-out mirroring the US gap exactly: "**This Annex does not apply to
equipment using infrared optical radiation to warm the body.**" The same
topical-heating framing that buys the US 510(k) exemption buys an exit from the
EU cosmetic regime.

### What this section can be relied on for

1. The category is regulated under a 1983 infrared **heating lamp** rule that
   matches neither its wavelengths nor its claimed mechanism, and since December
   2019 the heating variant needs no FDA review at all.
2. Cleared indications are uniformly **adjunctive, temporary, minor**
   symptomatic relief for named musculoskeletal sites, and several were granted
   with no clinical study in the submission.
3. **Exactly one device is cleared for a neuropathic-pain indication**, since
   February 2026, on a 64-subject trial, and it is cleared to relieve pain, not
   to treat neuropathy.
4. **Neither regulator has ever asked whether these devices work in the way they
   are sold.**

**Two limits on the negatives above, stated so they are not over-read.** FDA's
warning-letter database indexes only letters issued from 4 January 2021, so a
pre-2021 letter to any of these manufacturers cannot be excluded. The FTC case
index searches metadata rather than PDF text, proven by the fact that "diabetic
neuropathy" returns nothing despite appearing verbatim in the Willow Curve
complaint. These are "not found in a database with known blind spots", not
"does not exist".

**One citation defect worth knowing before quoting the FTC.** The Willow Curve
complaint cites "21 C.F.R. § 890.5550" for the infrared-lamp exemption. **That
section does not exist** in any year checked against the eCFR versioner. It is
890.5500, and the 2018 text contained no exemption clause at all. At least one
manufacturer's public FAQ reproduces the same wrong citation, apparently copied
from the complaint.

---

## 7. Search log for negative claims

Per EPISTEMICS.md rule 11. Databases: NCBI PubMed E-utilities (1 September
2026), ClinicalTrials.gov v2 API, openFDA, Crossref.

| Claim of absence | Verbatim query | Database | Result |
|---|---|---|---|
| Only one Cochrane review of PBM in a neuropathic condition | `"Cochrane Database Syst Rev"[Journal] AND (photobiomodulation OR "low level laser" OR "low-level laser" OR "laser therapy" OR phototherapy) AND (pain[ti] OR neuropath*)` | PubMed | 16 records; only CD012765 is PBM-in-neuropathy |
| Same, title-field variant | `"Cochrane Database Syst Rev"[Journal] AND (photobiomodulation[ti] OR laser[ti] OR light[ti]) AND (neuropath* OR neuralgia OR pain)` | PubMed | 25 records; confirms none for DPN, CIPN, PHN, TN or CRPS |
| PBM/CIPN literature is small | `(photobiomodulation OR "low level laser" OR "low-level laser" OR "light therapy") AND (chemotherapy-induced peripheral neuropathy OR CIPN)` | PubMed | **18 records total** |
| Almost nothing for CRPS | `(photobiomodulation OR "low level laser" OR "low-level laser" OR "laser therapy" OR "light therapy") AND (complex regional pain syndrome OR reflex sympathetic dystrophy OR causalgia)` | PubMed | 25 records; one randomised sham-controlled human trial |
| No PHN RCTs met inclusion | `(photobiomodulation OR "low level laser" OR "low-level laser" OR "laser therapy") AND (postherpetic neuralgia OR post-herpetic OR herpes zoster)` | PubMed | 53 records, no adequate RCT; corroborated verbatim by PMID 41629512 |
| No recent pooled meta-analysis in painful DPN | `(photobiomodulation OR "low level laser" OR "low-level laser" OR "light therapy" OR phototherapy) AND (diabetic peripheral neuropathy OR diabetic polyneuropathy) AND (meta-analysis[pt] OR systematic review[pt]) AND 2022:2026[dp]` | PubMed | 14 records, all wound-healing or narrative |
| The marketed device's neuropathy trials are unpublished | `Erchonia OR FX-635 OR EVRL` | PubMed | 20 records, none reports the pivotal neuropathy trials |
| Registered PBM neuropathic-pain trials mostly unreported | `AREA[InterventionSearch](photobiomodulation OR "low level laser" OR "laser therapy" OR "light therapy") AND AREA[ConditionSearch]("neuropathic pain" OR "peripheral neuropathy" OR neuralgia OR "diabetic neuropathy" OR "complex regional pain syndrome")` | ClinicalTrials.gov v2 | 100 returned; only NCT02000908 and the manufacturer set have posted results |
| Retractions present but not epidemic | `(photobiomodulation OR "low level laser" OR "low-level laser") AND (retracted publication[pt] OR retraction of publication[pt] OR expression of concern[pt])` | PubMed | 18 records |
| No NNT derivable | Inspected results and conclusions of CD012765, PMID 41629512, PMID 39871648, PMID 36214096, PMID 37622461 | PubMed efetch | None reports an NNT |
| CMS NCD 270.6 verbatim text | `cms.gov/medicare-coverage-database/view/ncd.aspx?NCDId=315` | cms.gov | **HTTP 403**, marked UNVERIFIED in §5 |
| Argenta 2017 funding | Europe PMC core record for the DOI; PMC link; NCT02000908 sponsor module | Europe PMC, NCBI, CTG | grantsList null, fundingList null, not open access; marked UNVERIFIED |

---

*Two commissioned sub-searches, on FDA and FTC enforcement history and consumer
device regulatory status, and a deeper optical-properties tabulation, had not
returned when this brief was written. §5's enforcement coverage and §4's
tabulated coefficients are therefore incomplete. **These are gaps in coverage,
not negative findings, and must not be recorded as "no enforcement actions
exist."***
