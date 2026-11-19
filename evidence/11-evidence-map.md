# E-11. Evidence map for the three questions, from full texts

> Evidence map, 19 November 2026. Implements step 1 of D-003
> (`ledger/DECISIONS.md`; intent:
> `intent/programme/2026-11-19-pivot-to-evidence-appraisal.md`).
>
> **What this is.** One table per question. Each row is an observation a
> clinician could make (a test, an examination finding, a response to an
> intervention, a device reading), with the best number found for it and where
> that number was read. It is a map of what the published record can and cannot
> support at population level. It is not a protocol and it ranks nothing.
>
> **Not medical advice.** Nothing here is a diagnosis, a recommendation or a
> device setting (ETHICS.md §1 and §3). The closing section phrases what
> follows as questions a treating team might consider. No dose and no
> stimulation setting is given anywhere. Where a quoted passage contained one,
> the quotation stops before it.
>
> **How it was built.** Every identifier was resolved live on 2026-11-19
> against NCBI E-utilities or the ClinicalTrials.gov v2 API. Nothing is cited
> from memory. For every source the map says whether the number was read in
> the full text or only in the PubMed abstract. **15 full texts were read, in
> part or in whole, and are used in a row; 32 further sources were read as
> abstracts only.** What was tested for those 32: 31 are not in PMC, and the
> publisher pages that were requested by script returned no article text.
> Europe PMC full text was not used. At least one of them states a CC BY
> licence and is still not in PMC, and one has a PMC copy that was not read
> (appendix C). "Not read in full" therefore means not retrieved by these
> routes, not that no open copy exists. The appendix lists every query
> verbatim with its hit count, every full text with how it was obtained and
> which sections were read, and every abstract-only source.
>
> Out of scope by instruction: congenital insensitivity to pain, ion-channel
> and growth-factor drug programmes, gene silencing or editing, doses,
> stimulation settings, and any case-specific material. Where a study used a
> drug as a probe, it is described by class; a drug name appears only inside
> a verbatim quotation, and in the search queries reproduced verbatim in
> appendix A.
>
> Sentences that begin **Reading:** are this map's interpretation, not a
> statement made by the paper cited.

---

## Bottom line

1. **The full-text pass did not anchor the S-3 model.** Of S-3's 24 likelihood
   parameters, none can be anchored on a number read in a full text in a
   relevant population. Three (a, f, q1) rest on a number read in an abstract,
   which is where S-3 already stood. By the stop rule given for this map, the
   finding is: **the data to rank these observations do not exist.** The
   scope of that sentence is: not found in open full text by these queries;
   32 sources were not read in full. The count and its definitions are in
   "Anchoring count".
2. **Which generator (Q-A).** Every human number found for a diagnostic
   peripheral nerve block is from an abstract, from 4 to 16 people, and none
   is from a cohort described as both CRPS-labelled and long-standing. No
   controlled diagnostic block aimed at a suspected peripheral lesion in
   CRPS-labelled pain was found by these queries. Placebo-controlled
   therapeutic trials of local anaesthetic in CRPS do exist; two are in row
   A17, and neither tests a lesion. The full-text numbers that exist are for
   imaging and for surgery, in populations that do not match.
3. **Why benefit fades (Q-B).** The best-matched full texts describe the
   first year, in which group benefit holds, and hardware, which fails often.
   Beyond a year the cohorts disagree on how common fading is. The largest
   series that contains CRPS (249 implants, 43% CRPS, abstract only) makes it
   look rarest: about 2% explanted per year, 6 for inadequate relief. The
   only independent long-term full text contains 16 ganglion-stimulation
   devices, 8 of them explanted. No study of ganglion stimulation was found
   that takes people whose benefit has faded and reports what a device
   reading, lead imaging or a pause in stimulation shows. The three candidate
   explanations have not been compared for ganglion stimulation in any source
   read here.
4. **Whether allodynia and background pain separate (Q-C).** No row has a
   number read in a full text. The abstracts point both ways at once, and
   that is the finding: the two can be separated by which fibres carry them
   and by some drug classes, and they rise and fall together in the same
   person. No source read here gives paired numbers for the two in people
   with a ganglion stimulator; the one CRPS study gives a number for
   background pain and shows allodynia only in a figure that was not read.
5. **Full text changed what the abstracts said in eleven places**, listed in
   "What reading the full text changed". Three of them bear on statements in
   an earlier brief.

## How to read the tables

**Columns.** (1) The observation. (2) What it would separate, and in which
direction. (3) Best source or sources. (4) Source status, exactly one tag.
(5) The number, verbatim with its denominator, the kind of number it is, the
population, and whether that population matches the question. (6)
Independence: group lineage, sponsor, replication. (7) The main reason the
number may not transfer.

**Status tags.** `number read in full text`: the methods or results passage
was read in the open full text and is quoted. `number from abstract only`: a
number exists, and it was read only in the PubMed abstract. `direction only`:
the source gives a direction and no usable number, or gives a number for only
one side of the comparison the row is about. `no data found`: nothing on
point came back from the logged queries, including a looser cross-check. A
`no data found` row is a statement about those queries, not about the
literature (EPISTEMICS.md rule 11).

**Population match.** The question's population is long-standing,
post-surgical, lower-limb, CRPS-labelled pain, and for Q-B a
ganglion-stimulation implant. Each row says which of those five features the
source population has. "Not stated" means the passage read did not say.

**Hypotheses.** Q-A: **P** a peripheral focal lesion, **G** the dorsal root
ganglion, **C** central. C-009's point is carried throughout: a complete
block removes ordinary touch along with any abnormal traffic, so relief under
a block shows that pain depends on input from the blocked territory and does
not show that the input is abnormal. Q-B: **H** habituation or tolerance,
**L** lead or hardware drift, **D** disease progression. Q-C: separable or
not.

---

## Q-A. Which generator maintains long-standing regional neuropathic or CRPS-labelled pain

Seventeen observations. Five have a number read in a full text. Only one of
those five (A7) is a block result, and it comes from a mixed group in which
5 of 20 people carried a CRPS label.

| # | Observation | What it would separate | Best source(s) | Source status | The number, its kind, its population | Independence | Main reason it may not transfer |
|---|---|---|---|---|---|---|---|
| A1 | Peripheral nerve block proximal to the painful area: is background (spontaneous) pain abolished? | Abolished: pain depends on input from the blocked territory (P, or C acting on normal input). Unchanged: G or input-independent C. It does not separate P from C acting on normal input (C-009). | Haroutounian et al. 2014, PMID 24704366 | `number from abstract only` | "The peripheral nerve block resulted in a complete abolition of ipsilateral pain within 10 min (median) in all patients". A proportion, 14 of 14. Comparator in the same people, a systemic local anaesthetic infusion: "reduced the spontaneous pain by 45.5% (±31.7%)", a mean percentage reduction. Population: "7 with unilateral foot pain due to peripheral nerve injury and 7 with bilateral pain in the feet due to distal polyneuropathy". Match: lower limb yes; CRPS label, duration and post-surgical origin not stated in the abstract. | Aarhus. A3 shares three authors with it, so A1 and A3 are one lineage. No sponsor named in the abstract. | Fourteen people, none described as CRPS-labelled; the abstract does not mention CRPS either way. S-3's original text says "none with CRPS", and its Amendment H already corrects that to the wording used here. The block cannot be blinded. The full text was not retrieved (not in PMC; the publisher address returned an abstract page only), so how completeness of the block was confirmed was not read. |
| A2 | Local anaesthetic at a painful focus left by earlier trauma, in people labelled with reflex sympathetic dystrophy (the older CRPS label) | Abolition of background pain and allodynia together points to a peripheral focus maintaining both (P), against input-independent C. | Gracely, Lynch & Bennett 1992, PMID 1484715; Koltzenburg, Torebjörk & Wahren 1994, PMID 8032867 | `number from abstract only` | Gracely: "Local anesthetic block of painful foci associated with previous trauma abolished mechano-allodynia, cold allodynia, and spontaneous pain in all patients". A proportion, 4 of 4. Population: "4 patients diagnosed with reflex sympathetic dystrophy (RSD)"; one had "tonic contractures of the toes". Match: CRPS-labelled yes; limb, duration and surgical origin not stated for the group. Koltzenburg, nine people with "chronic neuralgia (15 years mean duration)": "Complete relief of both ongoing and stimulus-induced pain was obtained in two patients with intravenous regional guanethedine block and in two other individuals by local anaesthetic blocks of nerves supplying the symptomatic skin". Counts, 2 and 2 of 9. Match: long-standing yes; CRPS label and limb not stated. | Two groups with no shared author. Neither names a sponsor in the abstract. | Four people and four people. Pre-1994 diagnostic labels. No control injection is described in either abstract. The Koltzenburg abstract is truncated at 400 words. |
| A3 | The same block with saline as a blinded control | Specific relief (input-dependence) against non-specific relief. This is the nearest human number for S-3's parameter f. | Buch et al. 2019, PMID 30817438 | `number from abstract only` | "Nine of 9 patients reported at least some pain relief after lidocaine injection compared with only 2 of 9 patients after saline injection (P = 0.02)". A proportion reporting any relief. The primary outcome was not significant: "-2.0 (interquartile range, -4.0 to 0.0) (n = 9, P = 0.12)", a median difference in change of worst pain. Population: amputees with constant postamputation pain; "Twelve amputees were randomized and 9 patients were included in the analysis". Match: post-surgical yes in the sense of amputation; CRPS label no; limb not stated in the abstract. | Aarhus, same lineage as A1. Randomised, double-blind, crossover. | Nine people. Postamputation pain is not CRPS-labelled pain. "At least some pain relief" is a lower bar than abolition, so 2 of 9 is not a false-positive rate for abolition. |
| A4 | A single uncontrolled diagnostic block: how often is relief reported for non-specific reasons? | Sets how much a positive single block is worth. | Curatolo & Bogduk 2010, PMID 29913995 | `number from abstract only` | "Single blocks are associated with about 30% false-positive responses." A false-positive rate. Population: the preceding sentence is "Diagnostic blocks for cervical and lumbar zygapophysial joint pain have been extensively studied." Match: none of the five features. The abstract adds: "For all other types of blocks, very little research has been conducted. The few studies that have been published did not use controlled blocks." | A narrative review by two authors. | The figure belongs to spinal joint blocks. The abstract itself says the research for other blocks is missing. |
| A5 | A comparative or placebo-controlled diagnostic block aimed at a suspected peripheral lesion, in CRPS-labelled pain | Would give the specificity that A1 and A2 lack. | none | `no data found` | No number for this observation. Queries Q24 (PubMed, 1 record: the review in A4), Q25 (PubMed, 5, none on peripheral nerve lesions in CRPS by title), Q4 (PubMed, 18, case reports and continuous-block treatment reports by title), Q38 (ClinicalTrials.gov, 31, none a controlled diagnostic block study by title), Q39 (Europe PMC full text, 1, unrelated) and the broad cross-check Q42 (PubMed, 35). Q42 does return placebo-controlled work with local anaesthetic in CRPS: two therapeutic trials (row A17), trials and reviews of sympathetic and intravenous regional blocks, and systemic infusion studies. By title and, for the two trials, by abstract, none is a diagnostic block of a suspected nerve lesion with a control injection. | n/a | The claim is narrow: it is about a controlled diagnostic block of a peripheral lesion, not about placebo-controlled blocks in CRPS in general, which exist. Screening was by title except where an abstract is named. A controlled block reported inside a surgical series would not have been seen. |
| A6 | Local anaesthetic applied at the ganglion (intraforaminal), at a concentration meant to silence ectopic firing without blocking conduction | Relief points to G over P. This is S-3's T3. | Vaso et al. 2014, PMID 24769187 | `direction only` | "In 31 amputees, the local anesthetic lidocaine was applied intrathecally and/or to the DRG surface (intraforaminal epidural block). This rapidly and reversibly extinguished PLP"; "Control injections were ineffective." The abstract gives no proportion for the dilute arm and no count for the controls. Population: amputees with phantom limb pain. Match: post-surgical in the sense of amputation; CRPS label no. | One group. The rat work cited in S-3 for the same idea (PMID 31095098) shares its senior author, so there is one lineage and no replication found (Q22, Q23). | Phantom limb pain, one lineage, no proportion, full text not retrieved (not in PMC; publisher page refused the scripted request). No use of the procedure in CRPS-labelled pain was found by Q22 (PubMed, 7 records, none on point by title). |
| A7 | A conduction-blocking injection at the nerve root (periradicular), before a ganglion-stimulation trial: does the numb area match the painful area, and does a match go with later benefit? | Would link a ganglion-level observation to response. It cannot separate P, G and C: at that concentration it stops all input through the root. | Sievert et al. 2021, PMID 33564905, PMC8270871 | `number read in full text` | Results: "From overall 20 included patients, PRT was congruent with the pain region in 18 cases (90%)." A proportion with a topographic match; pain relief was asked about and "Complete pain relief was not required for a positive PRT assessment". Outcome under stimulation: "a total of 47.4% of the patients achieved sustained significant pain relief in the last follow-up (9/19)", a responder proportion at up to 12 months. In the five implanted without a trial because the block result looked clearest: "only two patients (40%) reported relevant sustained pain relief". Population: "five patients were affected by CRPS, four patients by FBSS, and most patients had another form of postsurgical neuropathic pain". Match: ganglion-stimulation candidates yes; post-surgical for most; CRPS-labelled 5 of 20; limb mixed; duration not stated in the passages read. | Düsseldorf, single centre, no control. Two authors report honoraria or consultancy from the device manufacturer. | This is a root block done before a stimulation trial, with no control injection, and only 2 of 20 had a non-matching block, so it has no specificity comparison. The authors' own limitation: "No conclusions can be drawn regarding its predictive value to stimulation outcomes." A match in 18 of 20 with benefit in 9 of 19 says the match is common whether or not stimulation later helps. |
| A8 | MR neurography read for a focal neuroma | Positive supports P. Negative is weak against P if sensitivity is low. | Chhabra et al. 2011, PMID 21701028 | `number from abstract only` | "The sensitivity of MRN was 91% for the presence of focal fibrosis affecting the three nerves and 67% for neuroma detection." A sensitivity, against clinical and intraoperative findings. Population: "Ten MRN studies of nine patients ... who had been referred to a peripheral nerve specialist because of persistent symptoms after tarsal tunnel release". Match: post-surgical yes, lower limb (foot) yes; CRPS label no; duration not stated. The abstract gives no specificity for neuroma. | One group, retrospective. No replication in a post-surgical foot population was found by Q3 and Q15. | Ten studies. No specificity, so the false-positive side is unknown. A visible neuroma is not shown to be what generates the pain. |
| A9 | High-resolution ultrasound read for a focal nerve lesion or neuroma | As A8. | Tagliero et al. 2025, PMID 40310559, PMC12045816; Nischal et al. 2021, PMID 34376930, PMC8328747 | `number read in full text` | Tagliero, results: "Eleven patients had intraoperative findings consistent with a neuroma. US correctly identified whether there was a neuroma-in-continuity or a stump neuroma in 7 of 11 cases. MRI correctly identified whether there was a neuroma-in-continuity or a stump neuroma in 1 out of 8 cases." A proportion with the type of neuroma correctly named, against surgery. **Reading:** in the paper's Table 3 the ultrasound report names some neuroma in all 11 operated cases with one and in neither of the 2 without, so detection and correct typing are different quantities; the paper reports only the second. The MRI was a standard knee study, not neurography. Population: 13 people operated for common peroneal nerve injury, ultrasound a mean 3.8 months after injury. Match: lower limb yes; long-standing no; post-surgical no (one iatrogenic injury of 13); CRPS label no. Nischal, Table 1: ultrasound "Sensitivity \| 80.49% \| 65.13–91.18%" and "Specificity \| 100.00% \| 54.07–100.00%"; MR neurography "92.68%" and "66.67% \| 22.28–95.67%". Sensitivity and specificity for any nerve pathology, 47 nerves in 38 people, against a standard that was "surgical (29%), histopathological (10.5%), clinical (13.1%), and/or electrodiagnostic evaluation (47.3%)". Match: none of the five features; most nerves were in the upper limb. | Two unrelated groups (United States, India). Both report no funding and no competing interest. | Neither population has long-standing pain. In Nischal the specificity rests on about six unaffected nerves and the reference standard was surgical in under a third. Neither study asks whether the lesion seen is the source of pain. |
| A10 | Re-examination of a CRPS label at a peripheral nerve clinic: is an inciting nerve injury identified? | A documented nerve injury makes P possible. It does not show that the injury generates the pain now. | Raasveld et al. 2025, PMID 40211731 | `number from abstract only` | "In 33% of patients labeled with CRPS type I, an inciting nerve injury was identified." A proportion; the abstract does not give its denominator (the type I subgroup of 53). Population: "53 patients treated for CRPS at a peripheral nerve clinic within a tertiary care center". Match: CRPS-labelled yes; limb, duration and surgical origin not stated. | One centre, retrospective. Two authors consult for nerve-repair device companies. | Referral to a nerve clinic selects for nerve injury, so 33% is not a population rate. S-3 Amendment I already records that this is not the share whose pain is generated by a peripheral lesion. |
| A11 | Outcome of surgery on a painful neuroma, as an observation made after the fact | Durable relief after removal or relocation supports P for those operated. | Poppler et al. 2018, PMID 29189515, PMC5997533 | `number read in full text` | Results: "Among all studies, the proportion of patients with a meaningful reduction in pain was 77% [95% confidence interval (CI): 73–83]." A pooled proportion improved, 54 studies, 1,381 patients, with "I2 range 85.7% – 95.6%". How patients were chosen: "In all cases, the physical exam was the primary method of neuroma identification. Twenty-nine studies (54%) supplemented this with a diagnostic nerve block. Three studies (6%) also used an MRI or ultrasound". Population: "Thirty-five studies (65%) reported treatment of neuromas in the upper extremity, 12 (22%) reported on lower extremity neuromas"; "median duration of symptoms prior to surgery reported was 21 months". Match: lower limb in a minority; long-standing in part; CRPS label not a criterion. | One meta-analysis group. Four of 54 studies were prospective. No financial interest declared. | People who were operated on were selected because a focal lesion was already believed. There is no unoperated comparison, and the outcome scale was "non-standard" in 70% of studies. The abstract prints the interval as 73 to 81 and the results text as 73 to 83. |
| A12 | A small injection of local anaesthetic at sub-anaesthetic concentration beside a known painful neuroma | Fast relief of background and evoked pain points to the lesion as a driver (P). | Miclescu, Schmelz & Gordh 2015, PMID 29911636 | `number from abstract only` | "Lidocaine dose-dependently reduced spontaneous and evoked pain scores by more than 80%". A percentage reduction in pain score. Population: "Sixteen patients with neuropathic pain due to painful neuromas caused by nerve injury". Match: nerve injury yes; limb, duration, surgical origin and CRPS label not stated. The control was the lower of two concentrations, not an inactive injection. | Uppsala with a Mannheim co-author. Randomised, double-blind between the two concentrations. | No inactive control, so the non-specific share is unknown. Sixteen people with a neuroma already identified, which is the thing Q-A is trying to establish. |
| A13 | Response of background pain to a topical local anaesthetic patch over the painful skin | Relief points to a generator in the skin itself, a narrower claim than P. | Landmann et al. 2022, PMID 35834539, PMC9282664 | `number read in full text` | Results: "A reduction by a value exceeding NRS 1 was reported from n = 8 patients (“pain amelioration”), 15 patients did not report a change, whereas 4 patients recorded an increase of pain by NRS > 1". A proportion with more than one point of relief, 8 of the 27 these counts add up to; the abstract says "8 of 28". Population: 33 people with mono- or polyneuropathy, five of the mononeuropathy group with radiculopathy. Match: none of the five features. | One group, no conflict declared. | Not CRPS-labelled, no placebo patch described in the passages read, and a one-point change is small. |
| A14 | Response to ganglion stimulation, compared between people labelled CRPS and people labelled causalgia (a documented nerve injury) | If a documented nerve injury changed the response, the label would carry information about the generator. | Deer et al. 2017 (ACCURATE), PMID 28030470, PMC5359787; Huygen et al. 2020, PMID 31730273, PMC7079258 | `number read in full text` | ACCURATE, results 3.3: "For CRPS, a greater proportion of DRG subjects (82.5%) met the primary end point at 3 months than SCS subjects (57.5%) ... For causalgia, the proportion of subjects who met the primary end point was higher for DRG (79.3%) than for SCS (53.3%)". Responder proportions on a composite end point (at least 50% reduction in pain score and no neurological deficit); the denominators for the two diagnostic subgroups are not in the text read. Population: "CRPS (DRG: 44/76 [57.9%] ...) and causalgia (DRG: 32/76 [42.1%] ...)", lower limb, "average duration of chronic lower limb pain was 7.5 years for the DRG arm". Match: long-standing yes, lower limb yes, CRPS-labelled yes, implanted yes; post-surgical not stated. Huygen, Table 2, pooled at 12 months: responder rates "68%" for causalgia (n = 104) and "71%" for CRPS-I (n = 46). | ACCURATE: "sponsored by Spinal Modulation, LLC, a wholly owned company of St. Jude Medical"; "Subjects, investigators, and study site staff were not blinded". Huygen: "five were industry‐initiated" of seven pooled studies, three authors are employees of the manufacturer, and the ACCURATE arm is inside the pool, so the two sources are not independent. | **Reading:** the two labels respond alike, so this observation does not separate P from the rest. That agrees with S-3, where stimulation on or off was a weak discriminator. An unblinded responder rate cannot be read as a likelihood under any one generator. |
| A15 | Sensory profile on quantitative sensory testing | If CRPS without a documented nerve injury looked different from CRPS with one, the profile would carry information about P. | Gierthmühlen et al. 2012, PMID 22154921 | `number from abstract only` | "CRPS-I and CRPS-II had almost identical somatosensory profiles, with the exception of a stronger loss of mechanical detection in CRPS-II." Supporting proportion: "The majority of patients (66%-69%) exhibited a combination of sensory loss and gain." Population: "upper-limb CRPS-I (n=298), CRPS-II (n=46), and PNI (n=72)". Match: CRPS-labelled yes; lower limb no; duration not stated. | One national research network. | Upper limb. **Reading:** a profile that is the same with and without a documented nerve injury does not separate the candidates. |
| A16 | How often background pain persists under a confirmed complete peripheral block, in CRPS-labelled pain | Persistence would point to G or to input-independent C. Its frequency is the complement of S-3's parameter a in this population. | none | `no data found` | No number. Q1 (PubMed, 1 record, an animal study), Q4 (PubMed, 18, none a series reporting the proportion by title), Q14 (PubMed free full text, 7, none on point), Q38 (ClinicalTrials.gov, 31, none by title) and Q42 (PubMed, 35). The nearest record from Q42 is an uncontrolled series of repeated plexus blocks given as treatment in six people with reflex sympathetic dystrophy of an arm (Ribbers et al. 1997, PMID 9459103, abstract only): "Three patients responded well ... Three patients showed poor response". That is a count of treatment response over months, not of pain persisting during a confirmed block. | n/a | Title screening, with one abstract read. A2 is the nearest thing for pain during a block and holds four people. |
| A17 | Local anaesthetic given as treatment in CRPS, against a placebo injection or infusion | Not a test of a lesion. It bears on Q-A in one way: it shows how much a placebo procedure changes the outcome in CRPS-labelled people, which is what S-3's parameter f stands for. | Fallico et al. 2022, PMID 34903493; Taskaynatan et al. 2004, PMID 15372383 | `number from abstract only` | Fallico, 150 consecutive people with CRPS in three arms; change in the Impairment Sum Score, a composite severity score and not a pain score: "The combined treatment proved to be more effective (ISS 47.6 to 12.6) than local anaesthetic alone (ISS 47.5 to 21.5) and to placebo (ISS 47.2 to 29.9)." Group means before and after; the abstract does not say where the injections were placed, how long after them the score was taken, or whether assessors were blinded. Taskaynatan, 22 people with CRPS type I of an arm, mean pain duration about three months, intravenous regional block with a corticosteroid and a local anaesthetic against saline, double-blind: "improvement in pain severity was statistically significant ( P <.05) in both groups", and "its short-term benefit is not superior to placebo". No effect size in the abstract. Match: CRPS-labelled yes for both; lower limb no (Taskaynatan) or not stated (Fallico); long-standing no (Taskaynatan) or not stated. | Two groups with no shared author. No sponsor named in either abstract. | **Reading:** these are therapeutic trials and they do not count toward A5, because neither injects at a suspected lesion and neither measures pain during the block. What they add is that the placebo arm improved in both: by about 17 points on the composite score in one, and significantly on pain in the other. In the first, the local-anaesthetic arm improved more than placebo; the abstract's paired tests are within group, so the between-arm difference is not tested in what was read. Neither number is a false-positive rate for a diagnostic block. |

**What the Q-A table says, in plain terms.**

- The human evidence from diagnostic blocks is consistent in direction. In 14
  of 14, 4 of 4 and 9 of 9 people across three abstracts, removing peripheral
  input removed or reduced background pain. All of it is from abstracts and
  from small groups. Only the four-person series is in a CRPS-labelled group.
- Placebo-controlled trials of local anaesthetic given as treatment in CRPS
  exist (A17). They are not diagnostic blocks of a lesion. In both that were
  read as abstracts the placebo arm improved, which is a caution about
  reading any single uncontrolled block.
- That direction supports "pain depends on input from the limb". By C-009 it
  cannot say whether the input is abnormal, so it does not separate a
  peripheral lesion from central amplification of normal input.
- Nothing found tests the ganglion as generator in CRPS-labelled pain. The one
  human series is in phantom limb pain, from one lineage, with no proportion
  in its abstract.
- Imaging has full-text numbers, and they are from acute nerve trauma and
  mixed nerve pathology. The one post-surgical foot series is ten studies read
  in an abstract, with no specificity.
- Response to ganglion stimulation does not differ between the CRPS and
  causalgia labels in the one matched trial, so it carries no information
  about the generator on present evidence.

---

## Q-B. Why the benefit of ganglion (DRG) stimulation fades

Sixteen observations. Six have a number read in a full text. None of the six
was made in people selected because their benefit had faded, which is the
group the question is about.

| # | Observation | What it would separate | Best source(s) | Source status | The number, its kind, its population | Independence | Main reason it may not transfer |
|---|---|---|---|---|---|---|---|
| B1 | Share of people still meeting a responder criterion at 3 and at 12 months after implant | Sets how much fading there is to explain in the first year. All three candidates predict little here. | Deer et al. 2017 (ACCURATE), PMID 28030470, PMC5359787 | `number read in full text` | Results 3.3: "treatment success at 3 months in the DRG arm (81.2%; 56/69)" and "treatment success at 12 months in the DRG arm (74.2%; 49/66)". Responder proportions on a composite end point, with people who failed the trial phase counted as failures. Group mean pain score: "80.6 mm at baseline, which reduced to 13.1 mm at 3 months and remained low, at 15.0 mm, at 12 months". Flow: "A total of 61 DRG subjects ... continued to permanent implant. By the 12-month visit, 55 DRG subjects ... had evaluable data." Population: CRPS or causalgia of the lower limb, "average duration of chronic lower limb pain was 7.5 years for the DRG arm". Match: long-standing, lower limb, CRPS-labelled and implanted yes; post-surgical not stated. | Sponsor-run and unblinded: "All authors were paid by Spinal Modulation & St Jude Medical as investigators"; four authors are company employees. | Twelve months is short against a question about fading over years. The paper's tables are images in the open full text and were not read, so the per-visit counts behind the figure are not checked here. The registry lists results for this trial that were not read (see "Candidate predictions"). |
| B2 | Mean percentage pain relief at each visit to 12 months, ganglion stimulation against dorsal column stimulation | A fall over the year with intact hardware would favour H. | Levy et al. 2020, PMID 31494275 | `number from abstract only` | "Following permanent DRG system implantation, none of the time points were significantly different from one another in PPR (range = 69.3-73.9%)." A mean percentage pain relief per visit, in "all subjects that completed trial stimulation (DRG:N = 73 ...)". Also: "For both groups, mean PPR was significantly greater at end-of-trial (DRG = 82.2% ...) than all other follow-ups." For the comparator the abstract gives responder rates ("from 1-month (68.1%) to 12-months (61.1%)"); for ganglion stimulation it gives none. The abstract's central conclusion: "DRG stimulation resulted in more stable pain relief through 12-months, while tonic SCS demonstrated therapy habituation at 9- and 12-months." This is the sponsor-authored claim that E-05 contests. Population: the ACCURATE cohort, as B1. | The same trial as B1, so not independent of it. Three authors give the manufacturer as their affiliation, one of them the corresponding author. | One sponsor-authored sub-study of one unblinded trial. **Reading:** the drop from end of trial to the first visit after implant is present in both arms and is not discussed in the abstract as fading. |
| B3 | Explantation because pain relief had diminished, over years, in routine practice | Counts fading that was severe enough to remove the device, and how often a hardware reason was recorded instead. | Gatzinsky et al. 2025, PMID 39084704, PMC12703264 | `number read in full text` | Results: "8 of 16 devices, which were all implanted to treat conditions with focal neuropathic pain, were explanted during the whole study period, rendering a 3-year, 5-year and 10-year accumulated explantation risk of 31%, 38% and 63%, respectively. The median time to explantation was 21 months (IQR 12–57). Five explantations were due to diminished pain relief, two because of lead dysfunction and one because of the need for an MRI." Counts and Kaplan-Meier risks. In the Cox model of 5-year explantation due to diminished relief (395 patients, ganglion stimulation against all other devices): "HR 6.73; 95% CI 1.26 to 35.88; p=0.03" in the multivariable analysis. For the whole cohort of 400 (all device types): "Explantation risk due to diminished pain relief at the same intervals was 10%, 14% and 23%." Population: one Swedish university hospital, 2012 to 2022; 16 ganglion-stimulation devices. Match: implanted yes; CRPS label, limb and duration not stated for the 16. | Independent of the manufacturer: "The authors have not declared a specific grant"; one author reports lecture fees from two other manufacturers. All 16 were implanted by one surgeon. | Sixteen devices. The headline figures in the abstract (10%, 14%, 23%) are for all 400 devices together, mostly dorsal column systems. "Diminished pain relief" is the recorded reason for removal; the paper does not say whether lead position or disease course was examined first, so the five cannot be assigned to H, L or D. |
| B4 | Share still using the therapy at 5 to 7 years | As B3, at a longer horizon. | Eldabe et al. 2022, PMID 35302973 | `number from abstract only` | "At the final follow-up, 50% (16/32) of participants were still using DRG stimulation." A proportion still using. "Implantable pulse generators of 8 patients were explanted because of dissatisfaction with pain relief." A count. "this study had a revision rate of 42% within the first 24 months". Population: one UK centre, implants 2013 to 2015, "patients suffering with neuropathic pain". Match: implanted yes; the rest not stated in the abstract. | Independent of B3. No sponsor named in the abstract. | Thirty-two implants. The abstract does not say why the other eight stopped, or whether the eight dissatisfied people had had a revision. |
| B5 | Lead fracture and lead migration within 12 months, in prospective studies | The base rate of L in the first year. | Huygen et al. 2020, PMID 31730273, PMC7079258 | `number read in full text` | Results: "A total of 15 lead fractures and 15 lead migrations (both 5.9%) were reported." Event counts over 256 permanent implants in seven studies. Table 4 also lists "Increased lead impedance \| 5" and "Loss of stimulation \| 2". Explants: "a total of 16 (6.3%) were explanted, and were due to infection (8/16), lack of pain relief (5/16), noncompliance (2/16), and by patient request (1/16)". Population: mixed diagnoses; causalgia 48%, CRPS-I 21% of those followed. Match: implanted yes; CRPS-labelled in a minority. | "five were industry‐initiated"; three authors are employees of the manufacturer. | Events are counted per implant, not per person-year, and only to 12 months. The paper does not relate any of these events to loss of benefit. |
| B6 | Lead fracture and migration over several years, in registries and national cohorts | The base rate of L over the horizon at which fading is reported. | Chapman et al. 2026, PMID 42439846; Horan et al. 2021, PMID 32539189; Vanloon et al. 2025, PMID 39601733; Chapman et al. 2021, PMID 34145740 | `number from abstract only` | Four different quantities, listed separately. Chapman 2026: "Lead fracture occurred in 37 of 375 leads (9.9%), affecting 21 of 92 patients (22.8%)", a proportion of patients over a median 1059 days, with "an estimated 15% at 60 months" as a Kaplan-Meier figure. Horan: "Thirteen patients experienced complications related to defect leads (39% of implanted systems)" of 33 implanted, and "58% of fully implanted patients were still implanted; 42% had fully functional systems". Vanloon, pooled over 13 studies and 634 participants: "Lead fractures and migrations ... respectively, 6% (95% CI: 2%-12%) and 6% (95% CI: 2%-10%)". Chapman 2021, migration by fixation technique: "13 patients (21.0%)" without anchoring against "5 patients (2.7%)" with it. Match: implanted yes; CRPS label, limb and duration not stated in these four abstracts. | Chapman 2021 and 2026 are one group with overlapping centres. Horan (Denmark) and Vanloon (Belgium) are independent of it. Vanloon's pool will contain some of the same primary studies. | The spread, from 6% pooled to 39% in one national cohort, is itself the finding: the rate depends on technique, era and follow-up. None of the four abstracts says what share of people with fading benefit had a lead problem. |
| B7 | Device reports to a regulator's adverse-event database | Which hardware failures are reported at all. | Sivanesan, Bicket & Cohen 2019, PMID 30640660, PMC6363531 | `number read in full text` | Results: "we identified 979 unique episodes"; "migration and lead damage were the most common, being reported 272 and 99 times, respectively". Counts of reports, May 2016 to December 2017. Limitations: the manufacturer did not supply implant volumes, "Therefore, we cannot calculate the rates of these complications." Match: implanted yes; nothing else known. | Independent academic group; one author had consulted for the manufacturer on another product. | Counts without a denominator. Voluntary reports. Not a rate and not linked to benefit. |
| B8 | A device reading or lead imaging in a person whose benefit has faded: how often does it show a hardware cause? | A displaced or broken lead, or a changed impedance, would point to L; normal findings would leave H and D. | none with a number; Chapman et al. 2023 (consensus guidance), PMID 36942306, PMC10024474 | `no data found` | No number. Q20 (PubMed, 4 records, none on ganglion stimulators), Q21 (PubMed, looser, 0), Q8 (PubMed, 21, none reporting a yield by title), Q31 (PMC full text, 22, reviews and guidance by title) and Q41 (Europe PMC full text, 13, reviews by title). The consensus guidance names reprogramming and a review of imaging for lead position as the checks when pain worsens, and gives no figure for what they find. It also states: "loss of efficacy, or habituation, has not yet been demonstrated with DRG-S". | The guidance is from a professional society; its first author reports research funding from the manufacturer. | Full-text hits were screened by title. **Reading:** the guidance sentence conflicts with B3 and B4, where devices were removed for diminished relief. |
| B9 | Blinded switch to sham stimulation, in people with a stable response | If pain returns when stimulation is off, the benefit still depends on stimulation after months to years. That speaks against complete tolerance in those people. | Piedade et al. 2022, PMID 35217898, PMC8967770; Piedade et al. 2023, PMID 36705762, PMC10068636; Tabatabaei et al. 2026, PMID 42128597 (abstract only) | `number read in full text` | Piedade 2022, results: "Patients reported a mean VAS of 8.6 (SD 1.0) before the implantation of the DRG-S system and a mean baseline VAS of 3.9 (SD 1.9)." Under sham the mean in Table 1 is 8.57 (SD 1.26), and Table 2 gives the difference between pre-implant and sham as "0.000 (n.s.)". Mean pain scores per blinded phase, four days each. "all 19 patients reported an increase" in analgesic use during sham. Population: 19 people "using DRG-S for a mean of 17.2 months (range: 4–102)", "chronic regional pain syndrome (CRPS) (7 subjects)", "All patients ... had reached a stable therapeutic response." Piedade 2023, 17 people implanted "for an average of 32.8 months (range: 2–120)", CRPS in 6: baseline "3.2 (SD 2.2)", sham 5.3 (SD 3.0), and two "could not undergo the phase of sham stimulation due to unacceptable pain". Tabatabaei, abstract: "median NRS 3.0 (IQR 2.0-4.0) vs 6.0 (IQR 4.0-7.0)" active against sham, 20 established responders. Match: implanted yes; CRPS-labelled in about a third; limb and duration of pain not stated. | Two centres (Düsseldorf, Umeå). Whether the two Düsseldorf cohorts overlap is not stated in the passages read. Authors at both centres consult for the manufacturer. | These are people chosen because the therapy still works. They say nothing about people in whom it has faded. **Reading:** in the 2022 trial, pain under blinded sham equals pain before implant, so at group level those responders showed neither a carried-over effect nor a higher underlying pain than at implant; the phases were days long and the pre-implant score came from charts. |
| B10 | A pause in stimulation, then restart, in people with loss of benefit: dorsal column systems | Return of benefit with unchanged hardware would favour a reversible H. | D'Souza & Her 2022, PMID 35985769, PMC9613866 | `number read in full text` | Results: "Of 212 patients, 40 (18.9%) experienced loss of efficacy and underwent stimulation holiday". Table 2, at least 50% relief before and one month after the pause: "0 (0) \| 23 (57.5)". A responder proportion. "Ten patients experienced 0% pain relief before and after stimulation holiday." Design: "Exclusion criteria were any patient complications or hardware issues that may explain loss of efficacy (eg, lead migration, lead fracture, etc)"; before the pause, reprogramming "failed to salvage any relief". Population: one high-frequency dorsal column system at one centre; failed back surgery syndrome 65%; no CRPS group in Table 1. Match: none of the five features, and not a ganglion device. | One centre. One author holds an investigator-initiated grant from that system's manufacturer. | Not ganglion stimulation and not CRPS-labelled. Retrospective, with no group that restarted without a pause, so regression to the mean and expectation are not excluded. E-05 already records that carrying this figure to a ganglion system is an extrapolation. |
| B11 | The same pause, or a change of schedule, in people with a ganglion stimulator and fading benefit | As B10, in the right device. | none | `no data found` | No number. Q8 (PubMed, 21 records: schedule studies in responders, salvage after failed dorsal column stimulation, one single-patient report of an added lead), Q37 (ClinicalTrials.gov, 4, none on point), Q32 (PMC full text, 37, reviews by title). Two registered studies of intermittent schedules in ganglion stimulation exist (NCT04727216, NCT04909138); neither lists results. | n/a | The published schedule studies enrolled people who were doing well, so they do not test rescue. |
| B12 | After a fractured or migrated lead is revised, does benefit return? | Return of benefit after revision would attribute that episode of fading to L. | Chapman et al. 2026, PMID 42439846 | `direction only` | "Most patients with fractured leads underwent revision (17/21); four experienced a second fracture." The conclusion says events "were usually manageable with restoration of therapeutic effect"; the abstract gives no count for restoration. Full text (PMC8270871, as A7) for scale in another cohort: "A total of 7 patients underwent revision surgery, which included broken leads and lead defects, among other causes", of 19 who received stimulation, within 12 months. | Chapman: one registry; one author later joined the manufacturer. | No number for the outcome that matters. Horan (B6) reports the opposite hazard: "three patients suffered permanent nerve damage during attempts to replace broken leads". |
| B13 | Baseline features that go with later loss of benefit | A predictor tied to one mechanism would help choose among H, L and D. | Hagedorn et al. 2021, PMID 33508161; Gatzinsky et al. 2025, PMC12703264 | `direction only` | Hagedorn, abstract: "A history of prior chronic opioid use was associated with significantly lower rates of responder status", 93 implanted patients at one private practice; no effect size in the abstract. Gatzinsky, full text: "No other variable was a significant predictor for explantation in the univariable or multivariable analyses, including the type of indication for implantation". | Hagedorn's last author is the first author of B1. Gatzinsky is independent. | Opioid use travels with many things. Neither source measured anything specific to H, L or D. E-10 §6.3 and §6.4 looked for sensory-testing predictors and found none. |
| B14 | Signs of disease progression (spread, new signs, rising pain off stimulation) in implanted people whose benefit has faded | Progression with intact hardware and unchanged response to stimulation would point to D. | none | `no data found` | No number. Q36 (PubMed, 1 record, a review of another condition), Q32 (PMC full text, 37, reviews and guidance by title), Q41 (Europe PMC full text, 13, by title). B9 gives the only indirect reading, in responders. | n/a | No study of ganglion stimulation was found by these queries that measures pain with the device off, at intervals, in the same people over years. That is the measurement D needs. |
| B15 | Long-term course of dorsal column stimulation in CRPS, as the nearest older record | Shows that group benefit can fade over years in CRPS under another device. | Kemler et al. 2008, PMID 18240925; Geurts et al. 2013, PMID 23363081 | `number from abstract only` | Kemler: "At 5 years posttreatment, SCS+PT produced results similar to those following PT for pain relief and all other measured variables", 36 allocated to stimulation and 18 to physical therapy alone; the abstract gives a subgroup "pain relief (p=0.06)" and no effect size. Geurts: "41% (95% CI: 27-55) of the patients experience at least 30% pain relief at assessment end point", a responder proportion among 84 implanted, with "122 reinterventions" in 51 patients. Match: CRPS-labelled yes, long-standing yes; not a ganglion device. | One Dutch lineage for both. | A different target. **Reading:** in a randomised comparison, a narrowing gap can come from the comparison arm improving as well as from the treated arm fading, and the abstract does not say which. |
| B16 | Explantation rate and stated reasons in pooled multi-centre series, and whether explanted people had an earlier hardware event | A low rate would say fading severe enough to remove the device is uncommon. A hardware event before explantation is the only link between L and loss of the therapy found in any source here. | Chapman et al. 2022, PMID 35429364; Vanloon et al. 2025, PMID 39601733 | `number from abstract only` | Chapman 2022: "The explantation rate was ~2% per year (n = 10 total)", a crude rate over "249 patients with 756 leads and a mean 27-month follow-up". "Six patients were explanted for inadequate pain relief", a count, 6 of 249. "Five explanted patients experienced a therapy-related complication before eventual explantation: one transient post-procedural neuritis and pocket site pain, one lead fracture, two lead migrations, and one experienced a fracture, a migration, and pocket site pain." A count among the 10 explanted: 4 of 10 had a lead fracture or migration first. Population: "CRPS (n = 106, 43%), followed by FBSS (n = 64, 26%)". Match: implanted yes; CRPS-labelled in 43%, the largest CRPS-containing series in this table; limb and duration not stated. Vanloon, pooled over 13 studies and 634 participants: "The prevalence of DRGS explantations was 12%, primarily due to insufficient pain relief", a pooled prevalence over studies of differing length. | Chapman 2022: four pain centres; author affiliations are a private pain institute in New York, several US university hospital departments, a private spine and nerve centre, and one Dutch hospital. The PubMed record carries no sponsor and no conflict statement. It is the same 249-patient cohort as the 2021 lead paper in B6. One author is the first author of the pivotal trial (B1), and the first author also leads the consensus document in B8, which cites this series as evidence that fading has not been shown. Vanloon is independent of that group. | **The largest series that contains CRPS makes fading look rarest.** About 2% a year against 5 of 16 (B3) and 8 of 32 (B4). The three are different quantities over different horizons and are not merged: this one is a crude rate at a mean of 27 months, from implanting centres reviewing their own patients, and explantation undercounts fading, since a device can be left in place and switched off. The abstract does not say whether the six explanted for inadequate relief are among the five with an earlier complication, so "4 of 10 had a lead event first" links hardware to loss of the therapy, not specifically to fading. The full text was not retrieved (not in PMC). |

**What the Q-B table says, in plain terms.**

- In the one matched trial, group benefit held from 3 to 12 months: 56 of 69
  responders, then 49 of 66. That trial was unblinded and run by the
  manufacturer.
- Beyond a year, the cohorts disagree on how often a device is removed
  because relief diminished. Two independent single-centre cohorts: 5 of 16
  (full text, B3) and 8 of 32 (abstract, B4). One pooled four-centre series,
  from authors close to the pivotal trial: 6 of 249 at a mean of 27 months,
  about 2% explanted a year for any reason (abstract, B16). A pooled review
  gives 12% explanted, "primarily due to insufficient pain relief" (abstract,
  B16), and the 12-month prospective pool gives 5 of 256 explanted for lack
  of relief (full text, B5). These are different quantities over different
  horizons and are not merged.
- **The largest series that contains CRPS (43% of 249) makes fading look
  rarest.** The two cohorts in which it looks common hold 16 and 32 devices.
  Nothing read here says which picture is nearer the truth, and explantation
  is a narrower event than fading.
- Hardware failure is common and varies widely between reports. Three sources
  touch the link to loss of the therapy, and none settles it. In the pooled
  series, 4 of the 10 explanted people had a lead fracture or migration
  first (abstract, B16). In the 16-device cohort, 2 of 8 explants were
  recorded as lead dysfunction (full text, B3). One registry abstract says
  fractures were usually followed by "restoration of therapeutic effect"
  after revision, without a count (B12). No source read here reports how
  many people with fading benefit had a lead problem, or how many with a
  lead problem lost benefit.
- In people chosen because stimulation still works, blinded switch-off brings
  the pain back, in two centres. That shows continued dependence on
  stimulation in responders. It does not describe people whose benefit has
  faded.
- **For ganglion stimulation, the three explanations have not been
  compared.** No study of ganglion stimulation was found by these queries
  that takes people with fading benefit and reports lead position, a device
  reading, the effect of a pause, or pain with the device off over time. The
  one study of a pause after loss of benefit is in a different device (B10).
  Recorded reasons such as "diminished pain relief" do not distinguish the
  three.

---

## Q-C. Whether touch-evoked allodynia and background pain are separable mechanisms

Thirteen observations. None is tagged as a number read in a full text: every
human number that bears on separability is from an abstract. Two full texts
bear on the question (one human, one rat). The human one, row C9, does carry
a full-text number, for background pain only; it has no paired number for
allodynia, so under the tag definition it is `direction only` and Q-C counts
zero full-text rows.

"Separable" is used in two senses, and the rows keep them apart. **Carried
separately:** the two symptoms travel on different afferent fibres or respond
to different interventions. **Maintained separately:** one can persist or
remit without the other because a different process keeps it going. The first
does not imply the second.

| # | Observation | What it would separate | Best source(s) | Source status | The number, its kind, its population | Independence | Main reason it may not transfer |
|---|---|---|---|---|---|---|---|
| C1 | Selective block of large (Aβ) fibres by nerve compression: does touch-evoked pain go while background pain stays? | Yes: carried separately. | Koltzenburg, Torebjörk & Wahren 1994, PMID 8032867; Gracely, Lynch & Bennett 1992, PMID 1484715 | `number from abstract only` | Koltzenburg: "In six patients, differential block of A beta-fibres eliminated touch-evoked pain, but ongoing pain persisted when only C-fibres were conducting." A count, 6; the abstract does not say how many of the nine were tested this way. Population: "nine patients with chronic neuralgia (15 years mean duration)". Match: long-standing yes; CRPS label, limb and surgical origin not stated. Gracely: allodynia mediated by large fibres was supported "in 1 patient, by differential cuff blocks which abolished A beta function and allodynia while thermal sensation (warm and cold) were preserved", in a group of four labelled with reflex sympathetic dystrophy. | Two groups with no shared author. | Six people and one person. The Koltzenburg abstract is cut at 400 words. The compression block is a laboratory method. |
| C2 | Complete block of the peripheral input: do both go together? | Yes: both depend on input from the periphery, so this observation does not separate them. | Gracely et al. 1992, PMID 1484715; Buch et al. 2019, PMID 30817438 | `number from abstract only` | Gracely: local anaesthetic at the painful focus "abolished mechano-allodynia, cold allodynia, and spontaneous pain in all patients", 4 of 4, and "When the local anesthetic block waned, spontaneous pain, allodynia, and motor symptoms returned." Buch: "In all 9 amputees, evoked responses were eliminated after lidocaine injection", 9 of 9, alongside relief of background pain in 9 of 9 (row A3). Proportions. Match: as rows A2 and A3. | Two groups. | A block that numbs the skin removes the touch that would evoke allodynia (C-009), so "both abolished" is partly true by construction. In Gracely the abstract reports that touch and thermal perception were preserved, which is the more informative case, in four people. |
| C3 | Within one person, does brush-evoked pain rise and fall with background pain? | Yes: maintained together, with background input setting the gain for touch-evoked pain. | Koltzenburg et al. 1994, PMID 8032867 | `number from abstract only` | In four patients with heat hyperalgesia, warming the skin raised ongoing pain, "which was closely correlated (r = 0.94) with the level of brush-evoked pain". In the other five, "when the intensity of the background pain fluctuated spontaneously there were also parallel changes (r = 0.88) of the severity of brush-evoked pain". Correlation coefficients; the abstract does not say whether they are within-person or pooled. Population: as C1. | One group. The 2025 mouse imaging study recorded in E-01 §5 (coincidence of touch with ongoing nociceptor firing) points the same way in another species; it was not re-read for this map. | Nine people, 1994. A correlation in magnitude does not show which drives which. |
| C4 | Systemic drugs of two classes: do they move background pain and brush-evoked pain differently? | Yes: the two have at least partly different pharmacology. | Gottrup et al. 2006, PMID 16508401; Haroutounian et al. 2014, PMID 24704366 | `direction only` | Gottrup, 20 people with nerve injury pain, randomised, double-blind, placebo-controlled crossover: "Ketamine significantly reduced ongoing pain and evoked pain to brush and pinprick, whereas lidocaine only reduced evoked pain to repetitive pinprick stimuli. In individual patients, there was no correlation between the pain-relieving effect of lidocaine and ketamine on ongoing or mechanically evoked pains." No effect size in the abstract. Haroutounian, under the systemic infusion: "the improvement in evoked hypersensitivity was not related to the effect of the drug on spontaneous pain intensity"; no statistic in the abstract. Match: nerve injury yes; lower limb yes in Haroutounian's group and not stated in Gottrup's; CRPS label not stated. | Both from Aarhus, one senior author in common, so one lineage. | Acute infusions in the laboratory. "Not related" without a statistic cannot be weighed, and with 14 or 20 people an absent correlation is weak evidence of independence. |
| C5 | Spinal (intrathecal) agents of two classes in lower-limb CRPS: does pain relief track the shrinking of the allodynic area? | No tracking: maintained at least partly separately at spinal level. | Rauck, North & Eisenach 2015, PMID 25599305 | `number from abstract only` | "The percentage change in pain report did not correlate with the percentage change in areas of hyperalgesia (P = 0.09, r = 0.08) or allodynia (P = 0.24, r = 0.24) after drug treatment." Correlation coefficients. "Both drugs similarly reduced areas of hyperalgesia and allodynia by approximately 30%", a mean percentage reduction in area. Population: "Twenty-two subjects with pain and hyperalgesia in a lower extremity from complex regional pain syndrome", double-blind crossover. Match: CRPS-labelled yes, lower limb yes; duration and surgical origin not stated. | One group. No replication found by Q7. | Measured two hours after one injection. The outcome is the area of allodynia, not its intensity. **Reading:** the first pair as printed (P = 0.09 with r = 0.08) does not look self-consistent for 22 people, so the abstract's numbers should be checked against the full text before use. |
| C6 | A sub-anaesthetic local anaesthetic injection beside a painful neuroma: do the two recover on the same time course? | Different time courses: different processes, both needing peripheral drive. | Miclescu, Schmelz & Gordh 2015, PMID 29911636 | `number from abstract only` | "While evoked pain normalized rapidly reaching about 50% of the control level 20min after the injection, spontaneous pain levels continue to be lower in comparison with baseline values for more than 60min." Time-course figures; both were reduced "by more than 80%" at peak. The authors' own inference: "Spontaneous pain and evoked pain need an ongoing peripheral drive". Population: 16 people with painful neuromas after nerve injury. | One group. | Sixteen people with an identified neuroma. No inactive control. A difference in time course after one injection can reflect drug distribution as well as mechanism. |
| C7 | Brush-evoked allodynia at baseline as a predictor of outcome of dorsal column stimulation in CRPS | If allodynia marked a mechanism the stimulation does not reach, it would predict failure. | van Eijs et al. 2010, PMID 19942463; Kriek et al. 2023, PMID 36050204 | `number from abstract only` | van Eijs: "the diagnostic sensitivity for successful SCS was 0.75 and the specificity 0.81", from a receiver-operating curve on the maximum allodynia value. Sensitivity and specificity for treatment success at one year, with the cut-off chosen on the same data. Population: "36 chronic CRPS patients enrolled in a randomized controlled trial". Kriek, 31 people with CRPS before and after three months: "Pain, allodynia (sign and symptom), and hyperalgesia (symptom) were all significantly reduced after SCS therapy"; the authors say this "contradicts previous findings derived from retrospective analysis and animal research". Match: CRPS-labelled yes, long-standing yes (van Eijs); a different device from the one in Q-B. | Two Dutch groups (Maastricht, Rotterdam). The second does not confirm the first. | A cut-off fitted and tested on the same 36 people overstates accuracy. Dorsal column stimulation is not ganglion stimulation. |
| C8 | Blinded switching of dorsal column stimulation on and off: do sensory signs change with it? | A change in evoked signs without a change in background pain, or the reverse, would show separate handling. | Meier et al. 2015, PMID 25119512 | `direction only` | "Thermal and mechanical thresholds were similar during SCS activation and deactivation. The same result was found for intensity of pain and areas with painful symptoms even though all patients had documented long-term benefit of the treatment." No values in the abstract. Population: 14 people in long-term treatment, "complex regional pain syndrome (n=5) or pain following peripheral nerve injury (n=9)", sessions 12 hours apart. | One group (Aarhus), randomised and double-blinded. | Neither symptom moved, so nothing was dissociated. Twelve hours may be too short for either to change. Not a ganglion device. |
| C9 | Ganglion stimulation in CRPS: is touch-evoked allodynia reported separately from background pain? | Separate reporting is the precondition for any answer in the implanted population. | Kinfe et al. 2020, PMID 33087129, PMC7579938 | `direction only` | Full text, background pain: "Levels of spontaneous pain at baseline were 76 ± 4 on a 0–100 NRS. Following L4-DRG-stimulation, pain levels at 3 months follow-up diminished to 51 ± 8 NRS on average (p < 0.05)"; "eight patients reported reduced pain, three patients the same level of pain and only one patient reported a modest pain increase". For allodynia the passages read give no paired figure: the discussion says "the majority of patients reported bilateral pain to light touch (dynamic mechanical allodynia)", and the change after stimulation is shown in a figure that was not read. Population: 12 people with CRPS of the knee. Match: CRPS-labelled, lower limb and implanted yes. | One group. "This research was funded as an Investigator Initiated Trial ... from Abbott"; the first author consults for the manufacturer. | Twelve people, unblinded, three months. The number read is for one of the two symptoms only, which is why the row is tagged as direction. |
| C10 | In the rat, does stimulating the ganglion of the injured nerve differ from stimulating its uninjured neighbour? | Background pain relieved only at the injured level, evoked pain at either: maintained by different inputs. | Chao et al. 2021, PMID 33990112, PMC8486885 | `direction only` | Full text, results: stimulation "at either L4 or L5 increased mechanical thresholds and lowered response rates to tactile and noxious mechanical stimuli", and "SNL rats developed a strong preference for the chamber paired with L5 GFS, but L4 GFS lacked this effect". The values are in figures and a supplementary table that were not read. Rat, spinal nerve ligation. Match: none; animal model. | The Medical College of Wisconsin lineage recorded in E-03 §3. No independent replication is recorded there. | Rat, an acute model, a behavioural proxy for background pain. It supports separate maintenance in that model only. |
| C11 | How often brush-evoked (dynamic mechanical) allodynia is present at all in CRPS-labelled pain | If most people with CRPS-labelled pain have no brush allodynia on testing, background pain commonly exists without it. | Gierthmühlen et al. 2012, PMID 22154921; Maier et al. 2010, PMID 20627413 | `number from abstract only` | Gierthmühlen: "In CRPS-I and -II, cold hyperalgesia/allodynia (28%-31%) and dynamic mechanical allodynia (24%-28%) were less frequent than heat or pressure hyperalgesia". Proportions with the sign on standard testing, upper-limb CRPS-I (n=298) and CRPS-II (n=46). Maier, 1,236 people across neuropathic pain syndromes: "dynamic mechanical allodynia (20%)". Match: CRPS-labelled yes (Gierthmühlen); lower limb no; duration not stated. | One national network produced both, with shared authors, so they are not independent. | Upper limb. The test area and method are standardised, so a patient-reported "pain on touch" can be present with a negative test. The abstracts do not give the share with background pain, so the co-occurrence table cannot be built from them. |
| C12 | Over years, do the two remit or persist separately? | Separate courses would be the strongest evidence for separate maintenance. | none | `no data found` | No number. Q34 (PubMed, 1 record, a single-centre report on dorsal column stimulation) and the looser Q35 (PubMed, 1, the same record). | n/a | Two narrow queries. Natural-history cohorts that record allodynia as one sign among many would not be found by them. |
| C13 | In people with a ganglion stimulator whose benefit is fading, which returns first? | An ordering would link Q-B to Q-C. | none | `no data found` | No number. Q6 (PubMed, 18 records, none reporting the two symptoms separately over time by title), Q33 (PMC full text, 19, by title) and Q40 (Europe PMC full text, 3: row C9, and two reviews). E-10's scan of registered outcomes in six ganglion-stimulation studies found no allodynia outcome. | n/a | Title screening. The pivotal trial (row B1) measured one overall pain score. |

**What the Q-C table says, in plain terms.**

- **Carried separately: yes, on old and small evidence.** Blocking large
  fibres removed touch-evoked pain and left background pain in six people in
  one 1994 abstract, with one supporting case in another.
- **Maintained separately: unresolved.** For it: two drug-probe studies and
  one spinal-probe study report that relief of one does not track relief of
  the other. Against it: in the same 1994 study the two rose and fell
  together within a person (r = 0.88 and 0.94), and removing peripheral input
  removed both in every series that tried it.
- **Reading:** those two findings fit one account, in which ongoing input
  from the periphery sets a central gain that touch then reads out. On that
  account the two are separable by fibre and by some drugs and are not
  independent. This is the account E-01 §5 already records. Nothing read here
  tests it in CRPS-labelled lower-limb pain.
- **In people with a ganglion stimulator, the question has not been asked.**
  No source read here gives paired numbers for the two symptoms; row C9 has
  a number for background pain only.

---

## What reading the full text changed

Eleven places where the full text says something the abstract does not, or
says it differently. The first three bear on statements in E-05; that brief is
not edited here.

1. **The "higher risk with ganglion stimulation" result rests on 16 devices**
   (PMID 39084704, PMC12703264). The abstract reports "a higher risk was noted
   for ... DRG stimulation". The results give the base: 16 devices, 8
   explanted, 5 of those for diminished relief, with a hazard ratio whose
   interval runs from 1.26 to 35.88. The abstract's 10%, 14% and 23% are for
   all 400 devices. **Reading:** this is a signal from one centre, and E-05's
   sentence that independent data show ganglion stimulation "habituates more"
   is stronger than 16 devices can carry.
2. **The pause-and-restart figure excludes hardware causes by design**
   (PMID 35985769, PMC9613866). The methods exclude anyone whose loss of
   benefit could be explained by a lead problem, every participant had already
   had reprogramming that "failed to salvage any relief", and "Ten patients
   experienced 0% pain relief before and after". The abstract gives the mean
   gain and the responder rate without these. E-05 already says the device is
   not a ganglion stimulator.
3. **A p-value differs between abstract and text** in the second Düsseldorf
   trial (PMID 36705762, PMC10068636). The abstract gives p = 0.001 for the
   lowest tested frequency against sham. The results text gives p = 0.017 for
   that comparison, and p < 0.001 for the baseline setting against sham. E-05
   records the abstract's figure.
4. **Under blinded sham, pain returned to its pre-implant level** in the first
   Düsseldorf trial (PMID 35217898, PMC8967770): 8.57 before implant and 8.57
   under sham in Table 1, a difference of "0.000 (n.s.)" in Table 2. The
   abstract gives neither the sham score nor this comparison. The same text
   prints "Fourteen patients ... (76.7%)" of 19, where 14 of 19 is 73.7%.
5. **The root-block study cannot speak to prediction, by its authors' own
   statement** (PMID 33564905, PMC8270871). The abstract calls the block "a
   helpful tool to confirm the stimulation targets". The limitations say "No
   conclusions can be drawn regarding its predictive value to stimulation
   outcomes." The text also reports seven revision operations among 19
   people within a year, which the abstract omits, and gives 11 where the
   abstract gives 12 for leads placed at the tested level.
6. **"A neuroma was correctly identified" means the type was named
   correctly** (PMID 40310559, PMC12045816). The abstract's "7 of 11" reads
   as detection. The results say ultrasound "correctly identified whether
   there was a neuroma-in-continuity or a stump neuroma in 7 of 11 cases",
   and the MRI it is compared with was a standard knee study.
7. **The surgical meta-analysis prints two intervals** (PMID 29189515,
   PMC5997533): 73 to 81 in the abstract and 73 to 83 in the results. The
   results also show how patients were chosen (examination in all, a
   diagnostic block in 54% of studies) and that 22% of studies were in the
   lower limb.
8. **The regulator-database study prints two shares** for procedural
   complications (PMID 30640660, PMC6363531): 28% in the abstract and 24.2%
   in the results. Its limitations state that no rate can be calculated.
9. **The patch study's counts add to 27, and its abstract says 28**
   (PMID 35834539, PMC9282664).
10. **The pivotal trial prints two comparator success rates** (PMID 28030470,
    PMC5359787): 55.7% (39/70) in the results and 56.7% in the discussion.
    The denominators for the ganglion arm, 56 of 69 and 49 of 66, are only in
    the text. All ten tables are images in the open full text and were not
    read.
11. **A consensus document states that fading has not been shown, citing two
    sources that do not settle it** (PMID 36942306, PMC10024474). It writes
    that "loss of efficacy, or habituation, has not yet been demonstrated with
    DRG-S", on the strength of the 12-month sub-study in row B2 and a
    retrospective explant series (PMID 35429364). It reports "only 7 explanted
    for inadequate pain relief" from that series, where the series' abstract
    says "Six patients were explanted for inadequate pain relief."

None of these changes a direction. Several change how much weight a number
can bear, which is the reason the map was built from full texts.

---

## Anchoring count

### Rows by source status

| Question | Rows | `number read in full text` | `number from abstract only` | `direction only` | `no data found` |
|---|---|---|---|---|---|
| Q-A, which generator | 17 | 5 (A7, A9, A11, A13, A14) | 9 (A1, A2, A3, A4, A8, A10, A12, A15, A17) | 1 (A6) | 2 (A5, A16) |
| Q-B, why benefit fades | 16 | 6 (B1, B3, B5, B7, B9, B10) | 5 (B2, B4, B6, B15, B16) | 2 (B12, B13) | 3 (B8, B11, B14) |
| Q-C, separable or not | 13 | 0 | 7 (C1, C2, C3, C5, C6, C7, C11) | 4 (C4, C8, C9, C10) | 2 (C12, C13) |
| **All** | **46** | **11** | **21** | **7** | **7** |

Row C9 is tagged `direction only` although it carries a full-text number,
because that number is for background pain alone and the row is about the
pair. That is why Q-C counts zero full-text rows.

About a quarter of the rows (11 of 46) carry a number read in a full text. Of
those eleven:

- **2** are in a population that matches the question on four of its five
  features (A14 and B1, both the same sponsor-run trial);
- **4** are in people with, or being assessed for, a ganglion stimulator, with
  CRPS-labelled pain a minority or not stated (A7, B3, B5, B9);
- **5** are in populations that do not match (A9, A11, A13, B7, B10).

So the full-text numbers sit mostly where the population is wrong, and the
numbers closest to the question sit in abstracts.

### The S-3 likelihood parameters

S-3 (`simulations/S-003-generator-discrimination/`) has 24 likelihood
parameters. It recorded 4 as anchored on an abstract (a, f and q1 on a number,
e on a direction) and 20 as elicited.

**What "anchored" means here.** A parameter counts as anchored only if all
three hold: (i) a published number of the same kind as the parameter, that
is, the probability of that outcome under that condition; (ii) read in a full
text; (iii) measured in people with long-standing limb neuropathic or
CRPS-labelled pain, or in people with a ganglion stimulator. This definition
is this map's. It was fixed after the tables were built and before the
parameters were gone through one by one. It was not pre-registered.

| Parameter(s) | Meaning in S-3 | Best number now | Row | Anchored |
|---|---|---|---|---|
| a | background pain abolished by a complete block, when pain depends on input | 14 of 14 (foot nerve injury and polyneuropathy); 4 of 4 (reflex sympathetic dystrophy) | A1, A2 | **No.** Right kind, relevant population, abstract only. |
| u, g | split of partial against none; share of non-specific responders reporting abolition | none | n/a | No. |
| f | relief reported with no specific effect, single block | 2 of 9 after saline (postamputation pain, any relief); "about 30%" (spinal joint blocks) | A3, A4, A17 | **No.** The saline figure is the right kind in a limb population, abstract only. The 30% is the wrong population. The two placebo-controlled treatment trials in CRPS (A17) show placebo arms improving, on a composite score and on pain; neither is a rate of relief after a single diagnostic block, and both are abstract only. |
| d | ganglion ectopia behaving as input-dependent under a distal block | none | n/a | No. No study design read here could give it. |
| r, s | what a comparative block removes and what it costs | none | A5 | No. No data found. |
| e | background pain abolished by dilute anaesthetic at the ganglion, when the ganglion is the generator | direction only (phantom limb pain) | A6 | No. |
| u3, c, f3, g3 | the remaining ganglion-test terms | none; "Control injections were ineffective", no count | A6 | No. |
| s1, s2, s3, s4 | background pain relieved with stimulation on, under each generator | responder proportions by diagnostic label, not by generator: 82.5% and 79.3% at 3 months; 71% and 68% pooled at 12 months | A14, B1 | **No.** Full text and matched population, but the wrong kind: an unblinded responder rate on overall pain, not conditional on a generator. It constrains a prior-weighted mixture of the four and no one of them. |
| v1, v2, v3, v4 | evoked pain relieved with stimulation on, under each generator | none in humans; direction in one rat lineage | C9, C10 | No. |
| q1 | imaging positive when a peripheral lesion is the generator | 67% sensitivity for neuroma, ten studies after failed foot nerve surgery | A8 | **No.** Right kind, relevant population, abstract only. The full-text ultrasound numbers (A9) are in acute trauma and mixed pathology. |
| q2, q3, q4 | imaging positive under the other three generators | specificity 100% on about six unaffected nerves, mixed pathology | A9 | No. Wrong population, and specificity for "any pathology" is a different quantity. |

**Count.** Anchored on a number read in a full text in a relevant population:
**0 of 24.** If condition (ii) is dropped and an abstract is accepted: **3 of
24 (a, f, q1), which is 12.5%.** Those are the same three S-3 already listed.

**What did change.**

- f now has a human number from a nerve block (2 of 9 after saline) in place
  of a figure carried over from spinal joint blocks. It is still from an
  abstract, in nine people, and it measures any relief.
- a gained a second small series in a CRPS-labelled group (4 of 4), also from
  an abstract.
- S-3's assumption that stimulation on or off barely separates the generators
  now has one full-text check that agrees with it: response did not differ
  between the CRPS and causalgia labels (A14).

### The stop rule

The rule was given with the brief for this map, as set at the programme
review of 2026-11-19 before the map was built: if fewer than a third of the
24 parameters can be anchored, the finding is "the data to rank these
observations do not exist"; at least half is success. This map did not find
the rule written in a repository file (search of `intent/`, `ledger/`,
`PROGRAMME.md` and `README.md` for "a third", "one third", "at least half"
and "stop rule"), so it is quoted as given.

A third of 24 is 8. The count is 0 on the definition above and 3 if abstracts
are accepted.

**Outcome: fewer than a third. By the rule, the finding is that the data to
rank these observations do not exist.**

**Scope of that finding.** It means: not found in open full text by these 42
queries. Thirty-two sources were read as abstracts only and not in full,
among them the four that carry the best-matched block and imaging numbers.
What was tested for them is narrow: no PMC copy, and publisher pages not
retrievable by script. Europe PMC full text was not used, at least one such
source states a CC BY licence, and no library route was tried. The finding is
a statement about what this pass retrieved. It is not a demonstration that
the numbers are absent from the literature.

It holds on either count above, 0 or 3.

**Reading, and a prediction about papers that were not read.** If the four
abstract-only sources behind a, f, q1 and e were read in full and bore their
abstracts out, the count would be 4 of 24, still under a third. That is a
guess about unread papers and could be wrong in either direction: a full text
could supply a number for a further parameter, or could undercut an abstract.
For 15 of the 24 parameters (d, c, r, s, s1 to s4, v1 to v4 and q2 to q4) no
source found by these queries has the design that would be needed, a study in
which the generator is established independently of the test being evaluated.
That is an observation about what these queries returned, not proof that no
such study exists.

**What this does to S-3.** Its result stands as it was recorded: a
description of how a ranking behaves across elicited ranges. This map gives no
basis for replacing those ranges with measured values, and none for treating
its ranking as an ordering of real tests.

**Scope.** S-3 models Q-A only. No likelihood model exists in this repository
for Q-B or Q-C. The row counts above are the only anchoring statement this
map makes for those two questions: Q-B has six full-text rows, none in people
whose benefit had faded, and Q-C has none.

---

## Candidate predictions against unread data

Step 2 of D-003 is one prediction registered against data not yet read, and
scored. This section only lists candidates. **No prediction is registered
here, no direction is stated, and none of the sources below was opened beyond
what is declared.** Each entry says exactly what has already been seen, so
that a later registration can state its own exposure honestly.

| # | Unread source | Quantity that could be predicted | Why it bears | Already seen | What could make it unscorable |
|---|---|---|---|---|---|
| P-1 | The posted results of the manufacturer's post-approval study of ganglion stimulation in lower-limb CRPS types I and II, NCT02800863 (426 enrolled, completed 2021, results first posted 2024-07-08). | (a) The value posted for the registered secondary outcome "Percent Change From Baseline to 12 Months Post-permanent Implant for Overall Pain Intensity", with the number of participants analysed for it. (b) From the participant-flow table, which counts all enrolled participants and not only those implanted: the stated reasons for not completing, and the share of non-completers under each. The totals themselves are already known (see "Already seen") and are not a candidate. (c) Withdrawn: a count of participants with a lead migration or lead fracture. The review of this map reports that the record's adverse-event terms include no lead migration or lead fracture term, so (c) cannot be scored from this record. | Q-B. It is the largest cohort in the matching population, and it is single-arm and routine-practice, where row B1 is a randomised trial. (a) and (b) would give, in one cohort, a 12-month figure and how much attrition sits behind it. | Through this map's own registry request (protocol section only): title, status, sponsor, enrolment, and the four registered outcome titles with their time frames. The outcome descriptions were not printed and were not seen at that point. E-10 read the same outcome titles. The results section was not requested. Then, through the review of this map and not through any reading of the record here: that the outcome descriptions state 426 enrolled and 296 implanted; that the participant-flow table shows 198 completed and 228 not completed, of 426; and that no adverse-event term names lead migration or fracture. No posted value for outcome (a), and no breakdown of reasons for (b), has been seen. No journal publication was found by Q30. | (a) may be reported for completers only. (b) may give reasons too coarse to separate lack of benefit from other causes, and it mixes people who never had an implant with people who did. |
| P-2 | The full text of the 12-month habituation sub-study of the pivotal trial, Levy et al. 2020, PMID 31494275. Not in PMC; the publisher page was not retrievable by script. | The responder rate in the ganglion-stimulation arm at 1 month and at 12 months after implant. The abstract gives this pair for the comparator arm only. Also the per-visit figures split by CRPS type. | Q-B. Row B2 rests on a mean that "did not differ" between visits. A responder rate is a different quantity and can move when a mean does not. | The abstract, in full, including the comparator's responder rates (68.1% and 61.1%) and the ganglion arm's range of mean relief. The parent trial's full text, which gives the ganglion arm's composite success at 3 and 12 months (row B1). That second item is close to the target and must be declared in any registration. The publisher page was requested once by script and refused (HTTP 403). | The paper may report the ganglion arm's responder rate only in a figure. |
| P-3 | The full text of the sham-controlled crossover trial in established responders, Tabatabaei et al. 2026, PMID 42128597. The abstract states re-use is permitted under a CC BY licence; it was not in PMC on 2026-11-19. | (a) Median pain under sham set against the same participants' pain before implant, if reported. (b) Time since implant. (c) Whether the two participants who ended a period early did so under sham. | Q-B. Row B9 found, in one Düsseldorf trial, that pain under blinded sham equalled pre-implant pain. An independent centre either repeats that or does not, and the answer bears on whether underlying pain has shifted in long-term responders (the D candidate) and on carry-over. | The abstract, in full: active and sham medians, the difference, the design, the enrichment criterion. E-05 §6b records the same abstract and a registry note. The publisher page was requested once by script and refused (HTTP 403); nothing was received. | The paper may not report pre-implant pain at all. That would itself be worth recording, and it is not a scored outcome. |
| P-4 | The full text of the block study in row A1, Haroutounian et al. 2014, PMID 24704366. Not in PMC; the publisher address returned an abstract page only. | (a) The statistic behind "the improvement in evoked hypersensitivity was not related to the effect of the drug on spontaneous pain intensity": a correlation or a cross-table. (b) Whether any participant carried a CRPS label. (c) How completeness of the block was confirmed. | Q-C for (a): it is the one human dataset that measured both symptoms under two interventions in a lower-limb group. Q-A for (b) and (c): they decide how far S-3's parameter a can lean on it. | The abstract, in full. E-01 §5 and S-3 quote the same abstract. The publisher address was requested once by script and returned an abstract page without the article text; the page was not read and the saved copy was deleted. | (a) may be reported only as a sentence. |

**Reading, on choosing among them.** P-1 needs no access beyond a public
registry, and its quantity (a) is the only candidate here that is a
pre-specified numeric outcome. Its quantity (b) is not pre-specified, and its
totals are already known. P-2 has the most prior exposure of the three
full-text candidates. P-3 and P-4 are conditional on what the paper reports. A
registration should name one quantity, a threshold and a scoring rule before
the source is opened, and should say which rows of this map were known at the
time.

---

## Questions a treating team might consider

These are questions, at population level, that the rows above raise. They are
not steps, and none is a recommendation (ETHICS.md §3). Each names the row it
comes from. Risk, burden, cost and availability of any observation are outside
this map, and so is every individual's circumstance.

**On the generator (Q-A)**

1. When background pain is relieved by a peripheral nerve block, what does
   that establish beyond dependence on input from the limb, given that the
   block also removes ordinary touch? (A1, A2; C-009.)
2. How much weight can a single uncontrolled block carry, when the only
   saline-controlled figure found is 2 of 9 reporting some relief after
   saline, and the usual 30% comes from spinal joint blocks? (A3, A4.)
3. Has a controlled diagnostic block ever been evaluated for a suspected
   peripheral lesion in CRPS-labelled pain? These queries found none.
   Placebo-controlled trials of local anaesthetic as treatment in CRPS do
   exist, and in the two read as abstracts the placebo arm improved. (A5,
   A17.)
4. If imaging shows a focal nerve lesion, what is known about how often such
   a lesion is the source of the pain, when no specificity for neuroma was
   found in a post-surgical foot population? (A8, A9.)
5. Does a documented nerve injury change what can be expected from ganglion
   stimulation, given that the CRPS and causalgia groups responded alike in
   the one matched trial? (A14.)
6. Is there any published way to test the ganglion as generator in
   CRPS-labelled pain? The one human series is in phantom limb pain. (A6, A7.)

**On fading benefit (Q-B)**

7. When benefit fades, has lead position or integrity been looked at, and is
   there any published figure for how often that explains it? This map found
   base rates of hardware failure, one abstract in which 4 of 10 explanted
   people had a lead event first, and no figure for people with fading
   benefit as such. (B5, B6, B8, B16.)
8. What does the recorded reason "diminished pain relief" include, when the
   sources that use it do not say what was checked first? (B3, B4.)
9. Is pain with the device switched off known, and has it been compared with
   pain before implant? In one blinded trial in responders the two were equal.
   Nothing comparable exists for people whose benefit has faded. (B9, B14.)
10. Is there evidence that a pause in stimulation restores benefit for a
    ganglion stimulator? The one series is in a different device, excluded
    hardware causes by design and had no comparison group. (B10, B11.)
11. How much does the first-year record say about later years, when the
    matched trial ends at 12 months, two long-term cohorts hold 16 and 32
    devices, and the largest series (249 implants, a mean of 27 months)
    reports far fewer removals than either? (B1, B3, B4, B16.)

**On allodynia and background pain (Q-C)**

12. Are touch-evoked pain and background pain being recorded separately? In
    people with a ganglion stimulator, no source read here gives paired
    numbers for the two. (C9, C13.)
13. If one of the two changes and the other does not, what would that mean,
    given evidence that they travel on different fibres and evidence that
    they rise and fall together? (C1, C3, C4, C5.)
14. Does brush-evoked allodynia say anything about response to stimulation?
    Two studies of dorsal column stimulation in CRPS disagree, and none was
    found for ganglion stimulation. (C7.)

---

## What this map cannot say

- **It cannot say anything about a person.** Every number is a group
  proportion, mean or correlation. None is a likelihood for an individual, and
  the anchoring count shows that the group-level likelihoods themselves are
  missing.
- **It is not exhaustive.** Forty-two logged queries, screened by title.
  The review of this map found two relevant trials with one broader query
  (now Q42 and row A17), which shows the narrow queries miss things.
  Each `no data found` row is a statement about the queries named in it. A
  result reported inside a review, a surgical series or a supplement would
  not have been seen.
- **The best-matched block evidence was not read in full.** The sources for
  rows A1, A3, A6 and A8 have no PMC copy (checked through the NCBI identifier
  converter). Their publisher pages were requested by script: three refused
  the request (HTTP 403) and one returned an abstract page without the
  article text, which was not read. Europe PMC full text was not tried for
  them, and no library route was tried. For those rows "the abstract does
  not report X" is all that can be said; it is not a claim that the paper
  lacks X, and it is not a claim that no open copy exists.
- **Full text was read in part.** For most sources the methods and results
  were read and the discussion was not. Figures and supplementary files were
  not read for any source. The pivotal trial's ten tables are images in the
  open copy and were not read.
- **Europe PMC was intermittently unavailable on the day.** Three full-text
  queries completed there, one of them on a second attempt after a server
  error. The other full-text cross-checks were run on PMC through
  E-utilities instead. The two indexes overlap but are not the same.
- **One trial sits behind four rows.** The pivotal sponsor-run trial supplies
  A14, B1 and B2 and is inside the pooled analysis in B5. Those rows are not
  four independent supports.
- **"CRPS-labelled" is a loose population.** E-05 §1 records how unstable the
  label is. A source that matches on the label may still describe a different
  mix of people from the one the question has in mind.
- **The lists of candidates came with the questions.** Mixed generators are
  not mapped. For fading benefit, nothing here separates the three named
  candidates from a fourth: an early effect of expectation in unblinded care
  that wears off. The unblinded cohorts cannot exclude it, and the blinded
  trials enrolled only people still responding.
- **Several kinds of observation were not mapped at all.** Microneurography,
  skin biopsy, sympathetic blocks, bone scanning, brain imaging and
  sensory-testing predictors are covered, where they are covered, in E-01,
  E-05 and E-10, and were not re-read for this map. For sympathetic blocks
  one abstract was read after review, because Q42 returned it: a Cochrane
  review (PMID 27467116) in which "Two small studies compared LASB to
  placebo/sham (N = 32). They did not demonstrate significant short-term
  benefit". It has a PMC copy, which was not read. The 2025 mouse study on
  coincidence of touch with ongoing nociceptor firing was not re-read either.
- **Animal work gives direction only.** Two rat lineages, each from one
  group, with no value read.
- **It ranks nothing.** S-3 was not rebuilt, no observation is placed above
  another, and no prediction is registered or scored.
- **Searches are dated 2026-11-19.** Two sources are 2026 papers published
  ahead of print; their final versions may differ.

---

## Appendix

### A. Every query, verbatim

All run on 2026-11-19. PubMed and PMC through NCBI E-utilities `esearch`
(sorted by relevance, titles of the first 15 to 60 records read through
`esummary`). ClinicalTrials.gov through the v2 API (`query.term`). Europe PMC
through its REST `search` endpoint. "Hits" is the total count the service
returned. Screening was by title unless a row says an abstract or full text
was read.

| # | Database | Date | Query, verbatim | Hits |
|---|---|---|---|---|
| Q1 | PubMed | 2026-11-19 | `complex regional pain syndrome[tiab] AND nerve block[tiab] AND (spontaneous pain[tiab] OR ongoing pain[tiab])` | 1 |
| Q2 | PubMed | 2026-11-19 | `(nerve block[tiab] OR peripheral nerve block[tiab]) AND (neuropathic pain[tiab] OR postamputation pain[tiab] OR phantom[tiab]) AND (placebo-controlled[tiab] OR saline[tiab]) AND (spontaneous pain[tiab] OR afferent input[tiab])` | 2 |
| Q3 | PubMed | 2026-11-19 | `(neuroma[tiab]) AND (ultrasound[tiab] OR ultrasonography[tiab] OR neurography[tiab]) AND (sensitivity[tiab] OR specificity[tiab] OR diagnostic accuracy[tiab]) NOT Morton[tiab] NOT acoustic[tiab]` | 22 |
| Q4 | PubMed | 2026-11-19 | `(complex regional pain syndrome[tiab] OR CRPS[tiab] OR causalgia[tiab] OR reflex sympathetic dystrophy[tiab]) AND (peripheral nerve block[tiab] OR sciatic block[tiab] OR popliteal block[tiab] OR regional anesthesia[tiab] OR regional anaesthesia[tiab]) AND (pain relief[tiab] OR abolish*[tiab] OR relief[tiab])` | 18 |
| Q5 | PubMed | 2026-11-19 | `(dorsal root ganglion stimulation[tiab] OR DRG stimulation[tiab] OR DRG-S[tiab]) AND (loss of efficacy[tiab] OR habituation[tiab] OR tolerance[tiab] OR diminish*[tiab] OR explant*[tiab] OR revision[tiab] OR migration[tiab])` | 70 |
| Q6 | PubMed | 2026-11-19 | `(dorsal root ganglion stimulation[tiab] OR DRG stimulation[tiab] OR DRG-S[tiab]) AND (allodynia[tiab] OR hyperalgesia[tiab] OR evoked pain[tiab] OR quantitative sensory testing[tiab]) AND (patient*[tiab] OR human[tiab])` | 18 |
| Q7 | PubMed | 2026-11-19 | `(allodynia[tiab]) AND (spontaneous pain[tiab] OR ongoing pain[tiab]) AND (dissociat*[tiab] OR independent[tiab] OR differential[tiab] OR separate[tiab]) AND (patients[tiab]) AND (neuropathic[tiab] OR CRPS[tiab] OR complex regional[tiab])` | 22 |
| Q8 | PubMed | 2026-11-19 | `(dorsal root ganglion stimulation[tiab] OR DRG stimulation[tiab] OR DRG-S[tiab]) AND (holiday[tiab] OR intermittent[tiab] OR tapering[tiab] OR cycling[tiab] OR reprogramming[tiab] OR impedance[tiab] OR salvage[tiab] OR rescue[tiab])` | 21 |
| Q9 | PubMed | 2026-11-19 | `(spinal cord stimulation[tiab]) AND (allodynia[tiab]) AND (predict*[tiab] OR outcome[tiab]) AND (complex regional pain syndrome[tiab] OR CRPS[tiab])` | 6 |
| Q10 | PubMed | 2026-11-19 | `(neuroma[tiab]) AND (lidocaine[tiab] OR local anesthetic[tiab] OR diagnostic block[tiab] OR nerve block[tiab]) AND (pain[tiab]) AND (predict*[tiab] OR diagnos*[tiab] OR spontaneous[tiab]) AND (patients[tiab])` | 34 |
| Q11 | PubMed | 2026-11-19 | `(dynamic mechanical allodynia[tiab] OR brush-evoked allodynia[tiab] OR brush allodynia[tiab]) AND (complex regional pain syndrome[tiab] OR CRPS[tiab]) AND (prevalence[tiab] OR frequency[tiab] OR proportion[tiab] OR profile*[tiab] OR quantitative sensory testing[tiab])` | 5 |
| Q12 | PubMed | 2026-11-19 | `(spinal cord stimulation[tiab] OR neurostimulation[tiab]) AND (tolerance[tiab] OR habituation[tiab] OR loss of efficacy[tiab]) AND (mechanism*[tiab] OR cause*[tiab] OR lead migration[tiab] OR disease progression[tiab]) AND (explant*[tiab] OR revision[tiab] OR reprogram*[tiab])` | 12 |
| Q13 | PubMed | 2026-11-19 | `(dorsal root ganglion stimulation[tiab] OR DRG stimulation[tiab] OR DRG-S[tiab]) AND (long-term[tiab] OR follow-up[tiab] OR explant*[tiab] OR complication*[tiab] OR migration[tiab]) AND free full text[sb] AND (patients[tiab])` | 67 |
| Q14 | PubMed | 2026-11-19 | `(nerve block[tiab] OR diagnostic block[tiab] OR local anesthetic[tiab] OR lidocaine[tiab]) AND (neuropathic pain[tiab] OR nerve injury[tiab] OR neuroma[tiab] OR phantom[tiab] OR complex regional pain syndrome[tiab]) AND (spontaneous pain[tiab] OR ongoing pain[tiab]) AND (allodynia[tiab] OR evoked[tiab]) AND patients[tiab] AND free full text[sb]` | 7 |
| Q15 | PubMed | 2026-11-19 | `(neuroma[tiab] OR nerve injury[tiab] OR nerve entrapment[tiab]) AND (magnetic resonance neurography[tiab] OR MR neurography[tiab] OR high-resolution ultrasound[tiab] OR ultrasonography[tiab]) AND (sensitivity[tiab] OR accuracy[tiab]) AND (surgical[tiab] OR surgery[tiab] OR intraoperative[tiab]) AND free full text[sb]` | 23 |
| Q16 | PubMed | 2026-11-19 | `(complex regional pain syndrome[tiab] OR CRPS[tiab]) AND (misdiagnos*[tiab] OR alternative diagnos*[tiab] OR nerve injury[tiab] OR neuroma[tiab] OR entrapment[tiab]) AND (nerve surgery[tiab] OR neurolysis[tiab] OR decompression[tiab] OR neurectomy[tiab] OR re-evaluat*[tiab] OR reassess*[tiab])` | 16 |
| Q17 | PMC | 2026-11-19 | `("dorsal root ganglion stimulation"[Title] OR "DRG stimulation"[Title]) AND (long-term[Title] OR years[Title] OR follow-up[Title] OR outcomes[Title] OR explant*[Title] OR complications[Title])` | 7 |
| Q18 | PubMed | 2026-11-19 | `(complex regional pain syndrome[tiab] OR CRPS[tiab]) AND (allodynia[tiab]) AND (spontaneous pain[tiab] OR ongoing pain[tiab] OR pain at rest[tiab]) AND free full text[sb] AND (patients[tiab])` | 7 |
| Q19 | PubMed | 2026-11-19 | `(neuropathic pain[tiab] OR nerve injury[tiab]) AND (allodynia[tiab]) AND (A-fiber block[tiab] OR A-fibre block[tiab] OR compression block[tiab] OR ischemic block[tiab] OR differential block[tiab] OR nerve compression block[tiab])` | 4 |
| Q20 | PubMed | 2026-11-19 | `(dorsal root ganglion[tiab]) AND (stimulation[tiab] OR neurostimulation[tiab]) AND (impedance[tiab] OR perception threshold[tiab] OR paresthesia threshold[tiab] OR amplitude[tiab]) AND (loss of efficacy[tiab] OR over time[tiab] OR long-term[tiab] OR follow-up[tiab]) AND patients[tiab]` | 4 |
| Q21 | PubMed | 2026-11-19 | `dorsal root ganglion stimulation impedance loss of efficacy` | 0 |
| Q22 | PubMed | 2026-11-19 | `(dorsal root ganglion[tiab] OR DRG[tiab]) AND (lidocaine[tiab] OR local anesthetic[tiab] OR local anaesthetic[tiab] OR block[tiab]) AND (complex regional pain syndrome[tiab] OR CRPS[tiab]) AND (diagnos*[tiab] OR spontaneous pain[tiab] OR ectopi*[tiab])` | 7 |
| Q23 | PubMed | 2026-11-19 | `(selective nerve root block[tiab] OR transforaminal[tiab] OR intraforaminal[tiab] OR periradicular[tiab]) AND (complex regional pain syndrome[tiab] OR phantom[tiab] OR neuroma[tiab] OR peripheral nerve injury[tiab]) AND (pain[tiab])` | 22 |
| Q24 | PubMed | 2026-11-19 | `(comparative block*[tiab] OR controlled block*[tiab] OR placebo-controlled block*[tiab] OR double block*[tiab]) AND (peripheral nerve[tiab] OR neuroma[tiab] OR neuropathic[tiab] OR complex regional pain syndrome[tiab]) AND (diagnos*[tiab])` | 1 |
| Q25 | PubMed | 2026-11-19 | `(diagnostic nerve block[tiab] OR diagnostic block[tiab]) AND (false-positive[tiab] OR false positive[tiab] OR placebo response[tiab] OR specificity[tiab] OR predictive value[tiab]) AND (peripheral nerve[tiab] OR nerve surgery[tiab] OR neurectomy[tiab] OR neuroma[tiab] OR denervation[tiab])` | 5 |
| Q26 | ClinicalTrials.gov | 2026-11-19 | `dorsal root ganglion stimulation` | 70 |
| Q27 | ClinicalTrials.gov, single record, protocol section only | 2026-11-19 | `NCT01923285` | 1 |
| Q28 | ClinicalTrials.gov, single record, protocol section only | 2026-11-19 | `NCT02800863` | 1 |
| Q29 | ClinicalTrials.gov, single record, protocol section only | 2026-11-19 | `NCT03908476` | 1 |
| Q30 | PubMed | 2026-11-19 | `TARGET post-approval study dorsal root ganglion stimulation complex regional pain syndrome` | 0 |
| Q31 | PMC | 2026-11-19 | `"dorsal root ganglion stimulation" AND impedance AND ("loss of efficacy" OR "loss of effect" OR "diminished pain relief")` | 22 |
| Q32 | PMC | 2026-11-19 | `"dorsal root ganglion stimulation" AND (habituation OR tolerance) AND ("disease progression" OR "progression of the disease" OR "lead migration") AND "loss of efficacy"` | 37 |
| Q33 | PMC | 2026-11-19 | `"dorsal root ganglion stimulation" AND allodynia AND ("spontaneous pain" OR "ongoing pain") AND patients AND ("brush" OR "dynamic mechanical allodynia")` | 19 |
| Q34 | PubMed | 2026-11-19 | `(complex regional pain syndrome[tiab] OR CRPS[tiab]) AND allodynia[tiab] AND (long-term[tiab] OR follow-up[tiab] OR natural history[tiab] OR course[tiab]) AND (persist*[tiab] OR resol*[tiab] OR remission[tiab]) AND (spontaneous pain[tiab] OR pain at rest[tiab] OR ongoing pain[tiab])` | 1 |
| Q35 | PubMed | 2026-11-19 | `complex regional pain syndrome allodynia spontaneous pain course follow-up` | 1 |
| Q36 | PubMed | 2026-11-19 | `(dorsal root ganglion stimulation[tiab] OR DRG stimulation[tiab]) AND (disease progression[tiab] OR progression[tiab] OR spread[tiab] OR worsening[tiab]) AND (complex regional pain syndrome[tiab] OR CRPS[tiab] OR neuropathic[tiab])` | 1 |
| Q37 | ClinicalTrials.gov | 2026-11-19 | `dorsal root ganglion stimulation AND (loss of efficacy OR habituation OR tolerance OR holiday)` | 4 |
| Q38 | ClinicalTrials.gov | 2026-11-19 | `complex regional pain syndrome AND (diagnostic nerve block OR peripheral nerve block OR neuroma)` | 31 |
| Q39 | Europe PMC | 2026-11-19 | `"complex regional pain syndrome" AND ("comparative block" OR "controlled block" OR "placebo-controlled block") AND "peripheral nerve"` | 1 |
| Q40 | Europe PMC | 2026-11-19 | `"dorsal root ganglion stimulation" AND "dynamic mechanical allodynia" AND "spontaneous pain"` | 3 |
| Q41 | Europe PMC | 2026-11-19 | `"dorsal root ganglion stimulation" AND ("loss of efficacy" OR habituation) AND (impedance OR "lead position" OR "disease progression")` | 13 |
| Q42 | PubMed | 2026-11-19 | `(complex regional pain syndrome[tiab] OR CRPS[tiab] OR reflex sympathetic dystrophy[tiab]) AND (placebo[tiab] OR saline[tiab]) AND (block[tiab] OR blocks[tiab] OR local anesthetic[tiab] OR local anaesthetic[tiab] OR lidocaine[tiab] OR neuroma[tiab]) AND (randomized[tiab] OR randomised[tiab] OR controlled[tiab])` | 35 |

Q42 was added after review, as the broad cross-check the first version
lacked. All 35 titles were read. Abstracts were read for four: the two
trials in row A17, the plexus-block series named in row A16, and the
Cochrane review of sympathetic blockade named under "What this map cannot
say". The other 31 are reviews, guidance, trials and reviews of sympathetic
or intravenous regional blocks, systemic infusion studies, and records on
other conditions; none is a controlled diagnostic block of a suspected nerve
lesion by title.

**Looser cross-checks aimed at the negation.** For each `no data found` row
the table names a narrow query and a looser one: A5 (Q24 narrow; Q25, Q4,
Q39 and Q42 looser), A16 (Q1 narrow; Q4, Q14, Q38, Q42 looser), B8 (Q20 narrow; Q21, Q31,
Q41 looser), B11 (Q8 narrow; Q32, Q37 looser), B14 (Q36 narrow; Q32, Q41
looser), C12 (Q34 narrow; Q35 looser), C13 (Q6 narrow; Q33, Q40 looser). C12
has the thinnest support of the seven.

**Requests that are not searches, declared for completeness.**

- Europe PMC: a first batch of identifier look-ups timed out with no
  response, and Q41 failed once with HTTP 503 before completing. Europe PMC
  `fullTextXML` was not used for any source; every full text came from PMC.
- NCBI identifier converter: seven batches, 97 identifiers, to find which
  sources have a PMC copy.
- PubMed `efetch`: abstracts of every source named in a table.
- Registry: Q27 to Q29 requested whole records and printed only the protocol
  section (identification, status, sponsor, enrolment, outcome titles,
  references). The results sections were not printed or read.
- Publisher pages: ten requests by script. Eight were refused (HTTP 403), one
  returned an empty response, and one returned an abstract page without the
  article text, which was not read.

### B. Full texts read

All fifteen were obtained the same way: NCBI E-utilities `efetch`, `db=pmc`,
`retmode=xml`, on 2026-11-19, converted to text locally. Tables came through
as text except where noted.

| Source | Identifier | Rows | Sections read |
|---|---|---|---|
| Deer et al. 2017 (ACCURATE) | PMID 28030470, PMC5359787 | A14, B1 | Abstract; methods 2.2 in part; results 3.1, 3.2, 3.3, 3.5.5, 3.5.6 and 3.6; conflict-of-interest statement. The ten tables are images in this copy and were not read. |
| Gatzinsky et al. 2025 | PMID 39084704, PMC12703264 | B3, B13 | Abstract, methods, statistics, results with Tables 1 and 2, discussion, limitations, conclusions, funding and competing-interest notes. |
| Piedade et al. 2022 | PMID 35217898, PMC8967770 | B9 | Methods, statistics, results with Tables 1 and 2, limitations, conclusions, conflict statement. Discussion not read. |
| Piedade et al. 2023 | PMID 36705762, PMC10068636 | B9 | Methods, results with Table 1, conflict statement. Discussion not read. |
| Sievert et al. 2021 | PMID 33564905, PMC8270871 | A7, B12 | Methods, results with Table 1, limitations. Discussion not read. |
| Huygen et al. 2020 | PMID 31730273, PMC7079258 | A14, B5 | Introduction, methods, results with Tables 1 to 4, discussion, limitations, conclusions, conflict statement. |
| Chao et al. 2021 | PMID 33990112, PMC8486885 | C10 | Two results subsections only (evoked behaviour at each level; conditioned place preference). Figures and supplement not read. |
| Kinfe et al. 2020 | PMID 33087129, PMC7579938 | C9 | Passages found by term search: abstract methods, implantation paragraph, results on spontaneous pain, part of the mechanical-pain results, two discussion passages, funding, competing interests. Not read end to end. |
| Poppler et al. 2018 | PMID 29189515, PMC5997533 | A11 | Results in full. Methods and discussion not read. |
| Nischal et al. 2021 | PMID 34376930, PMC8328747 | A9 | Methods, results with Tables 1 and 2. |
| Tagliero et al. 2025 | PMID 40310559, PMC12045816 | A9 | Abstract, introduction, methods, results with Tables 1 to 3, funding and competing-interest notes. |
| Landmann et al. 2022 | PMID 35834539, PMC9282664 | A13 | Passages found by term search: abstract, patients, clinical characteristics, patch results, correlation analysis, parts of the discussion. Not read end to end. |
| Sivanesan, Bicket & Cohen 2019 | PMID 30640660, PMC6363531 | B7 | Methods, results, limitations. |
| D'Souza & Her 2022 | PMID 35985769, PMC9613866 | B10 | Study design, data extraction, outcomes, statistics, results with Tables 1 and 2. Discussion not read. |
| Chapman et al. 2023 (consensus guidance) | PMID 36942306, PMC10024474 | B8 | The section on habituation in full; passages on programming and on worsening pain found by term search. The rest of this long document was not read. |

**Opened and searched, not used for any row:** PMC7823340 (a review of nerve
ultrasound; three passages; it cites a head-to-head sensitivity figure from a
primary study that was not read) and PMC5515640 (a sensory-profile algorithm
paper; passages on how allodynia is coded).

**Fetched and not read:** PMC7669706, PMC12222022, PMC6692908, PMC9643723,
PMC12405714, PMC11363934, PMC11771605, PMC10757771. One further record,
PMC7410708, returned no body text.

### C. Sources read as abstracts only

Thirty-two, each read through PubMed `efetch` on 2026-11-19. Thirty-one have
no PMC copy, by the NCBI identifier converter. One, the Cochrane review
PMID 27467116, has a PMC copy that was not read. At least one,
PMID 42128597, states a CC BY licence in its abstract and is not in PMC, so
an open copy may exist at the publisher; its page refused the scripted
request. Europe PMC full text was not tried for any of the 32. "Abstract
only" records what this pass retrieved, not what is available.

Q-A: PMID 24704366, PMID 1484715, PMID 8032867, PMID 30817438, PMID 29913995,
PMID 24769187, PMID 31095098, PMID 21701028, PMID 40211731, PMID 29911636,
PMID 22154921, PMID 34903493, PMID 15372383, PMID 9459103, PMID 27467116.

Q-B: PMID 31494275, PMID 35302973, PMID 42439846, PMID 32539189,
PMID 39601733, PMID 34145740, PMID 35429364, PMID 42128597, PMID 33508161,
PMID 18240925, PMID 23363081.

Q-C: PMID 16508401, PMID 25599305, PMID 19942463, PMID 36050204,
PMID 25119512, PMID 20627413.

### D. Items not verified

Listed without identifiers; each refers to a row above.

- Row B9: whether the two Düsseldorf trial cohorts share participants. Not
  stated in the passages read. [UNVERIFIED]
- Rows A14 and B1: the per-visit counts and adverse-event breakdown in the
  pivotal trial's tables, which are images in the open copy. [UNVERIFIED]
- Row A9: the reading that ultrasound named some neuroma in all 11 operated
  cases is this map's count from the paper's Table 3; the paper does not
  state it. [UNVERIFIED]
- Row C5: the correlation pair that does not look self-consistent in the
  abstract. Not checked against the full text. [UNVERIFIED]
- Row C9: the size of the change in touch-evoked allodynia, shown in a figure
  that was not read. [UNVERIFIED]
- Row A6: a third paper from the same lineage on dilute anaesthetic at the
  ganglion came back in Q22 and Q23 and was seen by title only. [UNVERIFIED]
- Stop rule: its wording is as given with the brief; no repository file
  containing it was found. [UNVERIFIED]
