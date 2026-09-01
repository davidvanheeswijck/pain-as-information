# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `02-biological-plausibility.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T00:48:35+00:00 · tokens in=5965 out=3460
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review of C-005: "A human C-nociceptor carries under 30 bits per second, with little information in fine timing beyond rate"

## Where the conjecture is right

The conjecture correctly identifies a genuine and embarrassing hole in the literature: no direct information-rate measurement exists for human C-nociceptors, and the programme has been reasoning with entropy-rate ceilings as though they were measurements. That is a real gap, and the proposed frozen-noise microneurography design is the right shape of experiment to fill it. The conjecture also correctly identifies activity-dependent slowing as both a subtype classifier and a source of timing jitter—this is a real physiological phenomenon (Serra et al., 1999), and the reasoning that timing precision degrades exactly when rate is high is sound. The severity estimate is honest: the false-pass route through under-sampling is real and the jitter analysis is a sensible internal control. The cost estimate is plausible. This is a measurement conjecture that deserves to be done, and the programme is right to fund it first.

Now the objections.

---

## 1. THE WIRE

The conjecture's account of the primary afferent is broadly accurate for the fibre class it names, but it understates the heterogeneity problem and overstates what a single "identified C-nociceptor" is.

**Conduction velocity and fibre class.** Human C-fibres conduct at 0.4–1.4 m/s, unmyelinated, 0.2–1.5 µm diameter. Correct. But the conjecture treats "C-nociceptor" as a coherent category. It is not. Human microneurography distinguishes mechano-insensitive (CMi) and mechano-heat (CMH) nociceptors, and these differ in conduction velocity, activity-dependent slowing, spontaneous rate, and—critically—in what they signal. CMi units are silent at rest, have pronounced activity-dependent slowing, and are thought to be the dominant input to central sensitisation in some pathological states; CMH units have higher spontaneous rates and less slowing (Schmidt et al., 1995; Serra et al., 1999). A single information-rate figure averaged across these subtypes would be a category error. The conjecture's own cited classifier (Serra) exists precisely because these are different populations.

**Spontaneous rate.** The conjecture does not mention spontaneous discharge. Human C-nociceptors have low but nonzero spontaneous rates (typically <0.1 Hz in healthy skin, but elevated in neuropathy). For information-rate estimation under natural stimulation, spontaneous activity is noise that must be subtracted, and in neuropathic states it is the signal. The conjecture's healthy-volunteer design sidesteps this, which is fine for the measurement as stated, but the programme's HC-2 (readable outside the CNS) will eventually need the neuropathic case, where the spontaneous rate is not negligible.

**Refractory period and activity-dependent slowing.** The conjecture correctly identifies activity-dependent slowing as a timing-corrupting mechanism. But it does not mention the refractory period explicitly. C-fibre refractory periods are of order 2–5 ms, which sets a hard ceiling on instantaneous rate and interacts with slowing to produce complex interval statistics. The entropy-rate ceiling formula H ≈ r·log₂(e/(r·Δt)) assumes a renewal-like process with a fixed dead time; real C-fibre trains with activity-dependent slowing are non-renewal, and the formula is an upper bound, not an estimate. The conjecture acknowledges this ("real spike trains are not maximum entropy"), but the 30 bits/s figure is then a guess dressed as a prediction.

**Extracellular signal size.** This is where the wire objection bites hardest for the programme's larger ambitions, though not for this specific conjecture. A single C-fibre action potential recorded extracellularly at the nerve trunk is of order 1–10 µV, buried under the 50–200 µV compound activity of Aβ fibres and the electromyogram. Microneurography works because the electrode tip is *inside* the fascicle, within tens of micrometres of the axon. The conjecture's killer experiment is feasible precisely because it uses microneurography, not a nerve-trunk electrode. But the programme's HC-2—readable outside the CNS by a physically realisable sensor—is not addressed by this experiment. A 30 bits/s channel that requires an intraneural microelectrode to read is not a channel that a wearable or implantable trunk-level device can access. The conjecture is honest about this, but the programme should not mistake a successful microneurography measurement for evidence that the structure is readable by anything else.

---

## 2. THE CODE

The conjecture needs a rate-plus-fibre-class code to be sufficient, with fine timing contributing little. The evidence for that in mammals is mixed, and the strongest contrary evidence comes from a preparation the conjecture itself dismisses.

**Rate coding.** There is solid evidence that perceived pain intensity correlates with C-fibre discharge rate in human microneurography, particularly for heat pain (e.g., the classic LaMotte and Campbell work, and later microneurography studies showing that perceived intensity tracks CMH discharge). But the correlation is not identity: the same rate produced by different stimulus modalities does not produce the same percept, and the same rate in different fibre classes does not produce the same percept. That is fibre-class coding, which the conjecture accepts.

**Temporal pattern coding.** The conjecture cites the single ex vivo study (Cho et al., 2016) showing 79.7% classification of three chemicals from three-spike interval structure, and dismisses it as unreplicated and chemical. That dismissal is fair as far as it goes, but it ignores a larger literature. Temporal patterning in nociceptors has been shown to matter in: (a) the distinction between first and second pain (Aδ vs C, which is fibre class, but also the *pattern* of C-fibre bursts); (b) wind-up in the dorsal horn, where the *frequency* of C-fibre input, not just the total count, determines the central response (Prescott, Ma & De Koninck, 2014, cited by the conjecture itself); (c) the encoding of itch vs pain, where the *pattern* of C-fibre firing (bursting vs tonic) has been argued to distinguish pruritic from nociceptive traffic in some preparations, though this is contested. The conjecture's own citation of Prescott et al. is a problem for it: Prescott's work shows that the dorsal horn is exquisitely sensitive to the *temporal pattern* of primary afferent input, which means that even if the information in fine timing is small in bits, it may be large in *effect*. A channel carrying 5 bits/s of timing information can still drive a qualitatively different central response if the decoder is a coincidence detector.

**Population and combinatorial coding.** The conjecture's third rival—that the question is ill-posed for a single axon—is the one the evidence most strongly supports. Nociceptive information in mammals is population-coded. The same stimulus recruits multiple classes (CMH, CMi, Aδ mechano-heat, peptidergic and non-peptidergic populations) with overlapping but distinct tuning. The percept is a function of the *pattern of co-activation across classes*, not of any single axon's rate. The conjecture acknowledges this rival honestly, and the proposed experiment would produce data relevant to it, but the single-axon information rate is then a lower bound on the population rate, not an estimate of the channel the CNS actually reads.

**Preparation generalisability.** The Cho et al. study is ex vivo, chemical, and unreplicated. The human microneurography literature is awake, natural-stimulus, but small-n and technically demanding. The conjecture's proposed experiment is the right preparation for the question it asks. But the programme should be clear that a low single-axon information rate in healthy volunteers under natural stimulation does not refute the strong form of HC-1; it only refutes the strong form *for single axons in healthy skin*. The strong form of HC-1 could still be true at the population level, or in neuropathic states where ectopic burst patterns are the signal.

---

## 3. WHERE IS PAIN MADE

This is the fatal objection to the programme's larger ambitions, and the conjecture does not escape it.

The discrimination between nociceptive and innocuous traffic is **not made in the periphery**. It is made in the dorsal horn and above. The primary afferent does not know it is a "pain fibre"; it is a transducer with a particular threshold and adaptation profile. The same C-fibre that responds to a noxious heat also responds to a firm but innocuous mechanical stimulus, and the CNS decides whether that traffic is painful based on context, co-activation, and descending modulation.

The conjecture's measurement is of a single C-nociceptor's information rate about a *stimulus*. That is a legitimate measurement, but it does not measure "pain information". It measures the information a particular axon carries about a physical variable. Whether that information contributes to pain, itch, touch, or nothing depends on central processing. The conjecture is careful to say "about a natural stimulus", not "about pain", and that care is appropriate. But the programme's HC-2—that pain-relevant discrimination is readable outside the CNS—is not tested by this experiment. A 30 bits/s channel carrying stimulus information is not a 30 bits/s pain channel.

The most likely fatal objection to the whole programme, as the review instructions put it, is that the difference between nociceptive and innocuous traffic is made centrally. This conjecture does not address that objection. It measures the wrong thing for HC-2, even though it measures the right thing for HC-1.

---

## 4. THE PATHOLOGY

The conjecture is explicitly about healthy volunteers under natural stimulation. That is the right choice for a first measurement, but it means the conjecture has nothing to say about neuropathic pain, which is the programme's stated target.

Neuropathic pain is not intense nociception. It is a disease of the system, not of the transducer. The relevant features:

**Ectopic spontaneous discharge.** Injured axons and their cell bodies in the DRG generate spontaneous activity that is not stimulus-locked. This activity has a *pattern*—bursting, irregular, sometimes rhythmic—that is not captured by a rate measurement under natural stimulation. The information rate of a spontaneously active neuropathic C-fibre is not the same as the information rate of a healthy C-fibre responding to a stimulus.

**Altered channel expression.** After nerve injury, DRG neurons upregulate Nav1.3, Nav1.7, Nav1.8, and downregulate potassium channels, changing the relationship between stimulus and firing. The "channel" the conjecture measures in healthy volunteers is not the channel that exists in a decade-old injury.

**Central disinhibition.** The dorsal horn loses inhibitory tone after nerve injury, so the same peripheral input produces a larger central response. The information in the periphery is unchanged; the gain is changed centrally. A peripheral measurement cannot see this.

**Allodynia on Aβ fibres.** In established allodynia, the traffic that hurts arrives on low-threshold mechanoreceptors that are behaving normally. The Aβ fibre is carrying the same information it always carried; the CNS has rewired it into a pain percept. No measurement of C-fibre information rate, however precise, will detect this, because the C-fibre is not the problem.

The conjecture's healthy-volunteer design is defensible as a first measurement, but the programme must not extrapolate from it to the pathological case. A proposal that filters "pain fibres" does nothing about a system in which touch fibres have been rewired into a pain percept. This conjecture does not propose filtering, but its results will be used to argue about filtering, and the programme should be clear that the argument does not transfer.

---

## 5. PLASTICITY AND HABITUATION

The conjecture is a measurement, not an intervention, so this objection applies less directly. But the programme's PB-2 (loss of efficacy in implanted stimulation is habituation to a fixed stimulus) is relevant to how the results would be used.

If the measurement confirms low single-axon information rates, the programme will argue that high-bandwidth transducers are solving an assumed requirement. That argument is sound only if the channel is stationary. It is not. The information rate of a C-nociceptor changes with:

**Receptor regulation.** Repeated stimulation changes the transducer. Heat sensitisation, desensitisation, and fatigue all alter the rate and pattern of firing. A frozen-noise design with 30 repeats assumes stationarity over the recording session; if the fibre sensitises or desensitises, the information estimate is biased.

**Central habituation.** The perceived intensity of a repeated stimulus declines over time even when the peripheral firing rate does not. This is central habituation, and it means that the information rate measured peripherally is not the information rate perceived centrally.

**Long-term plasticity.** Over months and years, the nervous system changes in response to any fixed input. The conjecture's measurement is a snapshot; the programme's interventions are chronic. The two are not the same problem.

---

## 6. COLLATERAL TRAFFIC

The conjecture is a measurement, not an intervention, so collateral damage is not directly at issue. But the programme's HC-3 (structure-targeted intervention beats channel destruction) depends on being able to act on the structure without collateral damage. The measurement proposed here does not address that.

The nerve trunk carrying the C-nociceptor also carries:

- **Aβ fibres** for touch and proprioception
- **Aδ fibres** for fast nociception and cold
- **C-fibres** for warmth, itch, and autonomic function (sudomotor, vasomotor)
- **Motor fibres** in mixed nerves

A sensor that reads C-nociceptor activity from the trunk must contend with all of these. A transducer that acts on C-nociceptors must avoid all of these. The conjecture's microneurography measurement is selective because the electrode is inside the fascicle, within micrometres of the axon. No practical intervention has that selectivity. The programme's HC-4 (a physically realisable transducer exists) is not advanced by this measurement.

---

## 7. SPECIES AND PREPARATION

The conjecture's evidence base is:

- **Human microneurography** (Serra, Schmidt): awake, natural stimulus, small-n. This is the gold standard for the question asked, and the conjecture's proposed experiment is in this tradition.
- **Ex vivo rodent** (Cho): chemical stimulus, unreplicated. The conjecture correctly dismisses this as weak evidence for human natural-stimulus coding.
- **Rodent slice and in vivo** (Prescott): the dorsal horn, not the primary afferent. Relevant to the *decoder*, not the *channel*.
- **Human microneurography** (Werland): electrical stimulation, not natural. Relevant to the rate ceiling, not the information rate.

The conjecture's proposed experiment is the right preparation for the question it asks. The weakness is not the preparation but the extrapolation: a healthy-volunteer, natural-stimulus, single-axon measurement does not generalise to the neuropathic, spontaneous-activity, population-coded case that the programme ultimately cares about.

---

## Summary

The conjecture is a good measurement proposal for a real gap in the literature. It is honest about its limitations, its severity estimate is credible, and its refutation threshold is well-specified. The objections above are not objections to the measurement; they are objections to the programme's likely use of the measurement. The single-axon information rate of a healthy human C-nociceptor under natural stimulation is a number worth knowing. It is not a number that settles HC-1, HC-2, or HC-3. The programme should fund the measurement, but it should not mistake the result for an answer to the programme's central questions.

VERDICT: MINOR — The measurement is worth doing, but the conjecture must state explicitly that a low single-axon information rate in healthy volunteers under natural stimulation does not test HC-2 (peripheral readability of pain-relevant discrimination), does not generalise to neuropathic pain (where the relevant traffic is ectopic, Aβ-mediated, or centrally amplified), and does not constrain the population code that the CNS actually reads.
