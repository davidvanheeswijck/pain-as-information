# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `02-biological-plausibility.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T14:35:40+00:00 · tokens in=7699 out=4234
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review of C-007: "Sub-5-millisecond spike timing adds no information beyond rate and unit identity"

## Where the conjecture is right

The reformulation from C-005 is a genuine improvement and the programme deserves credit for accepting it. The original question—"how many bits per second does a nociceptor carry"—was indeed ill-posed, and the comparative framing here is the correct one. The mechanistic argument from activity-dependent slowing (ADS) is also physiologically sound in its broad outline: unmyelinated axons do accumulate conduction slowing with repetitive discharge, and this does degrade the temporal fidelity of spike arrival at a distant recording site. The prediction that timing information degrades precisely when rate coding saturates is a testable, mechanistically motivated claim rather than a hand-wave. The proposed reanalysis of archived microneurography recordings before new collection is exactly the right order of operations, and the severity estimate of 0.15 is honest. The two-decoder-family requirement is a necessary control that many proposals in this space omit.

That said, the conjecture as written contains several biological assumptions that do not survive contact with what is actually known about primary afferent physiology. I will take them in the order requested.

---

## 1. THE WIRE

The conjecture's experimental design is built on human microneurography of single identified C-nociceptors. This is the right preparation for the question, but the conjecture under-specifies what "a single human C-nociceptor" actually is, and this matters for the claim.

**Fibre class and conduction velocity.** Human C-nociceptors conduct at 0.4–1.4 m/s, as the conjecture states. But the population is heterogeneous in a way that directly affects the timing claim. Mechano-insensitive C-nociceptors (CMi, also called "silent" nociceptors) have conduction velocities at the low end of this range and are only recruited after sensitisation or inflammation (Schmidt et al., 1995, which the conjecture cites). Mechano-heat-sensitive C-nociceptors (CMH) conduct faster and are the units most commonly captured in microneurography of healthy volunteers. If the conjecture's stimulus ensemble is mechanical or thermal in healthy skin, it will preferentially recruit CMH units. The timing statistics of CMH units may not generalise to CMi units, which are the ones that become relevant in pathological states. This is not fatal to the conjecture as posed—it specifies healthy volunteers—but it limits the inference the programme wants to draw about neuropathic pain, where the relevant population shifts.

**Spontaneous rate.** Healthy human C-nociceptors have very low or absent spontaneous discharge. This is actually an advantage for the proposed experiment: the noise floor for timing analysis is low. But it also means the conjecture is testing timing information in a regime—evoked, healthy, acute—that is maximally favourable to rate coding. In injured or sensitised fibres, spontaneous ectopic discharge adds a background that changes the inter-spike interval statistics entirely. The conjecture's own HC-1 is motivated by neuropathic pain, but the killer experiment as specified cannot speak to that condition.

**Refractory period and activity-dependent slowing.** The conjecture correctly identifies ADS as the mechanism that degrades timing. But it understates the magnitude of the effect. In human C-nociceptors, ADS accumulates over seconds of repetitive discharge and can reach 20–30% of conduction velocity (Serra et al., 1999, cited). For a 1 m/s fibre conducting over 50 cm, that is a latency shift of 150–200 ms. This is not a subtle jitter; it is a first-order effect that swamps any sub-5-ms timing structure. The conjecture's own mechanism section says "timescales are ordinary: spikes on the millisecond scale, slowing accumulating over 1e-1 to 1e0 seconds." But the slowing is not merely accumulating over those timescales—it is *imposing* a low-frequency modulation on spike timing that is orders of magnitude larger than the fine timing the conjecture proposes to test. If the conjecture is right, it is right for a trivial reason: the axon's own conduction dynamics act as a low-pass filter on timing information. That is a real finding, but it is not the same as demonstrating that fine timing carries no information in principle.

**Extracellular signal size.** The conjecture does not propose to read the signal from the nerve trunk; it proposes microneurography, which records from within the nerve fascicle. This is the correct choice. Any proposal to read C-fibre timing from the surface or from the trunk would fail on signal-to-noise grounds, as C-004 already established. The conjecture is not making that mistake.

---

## 2. THE CODE

The conjecture needs a specific coding scheme to be true: it needs **rate-plus-identity** to be sufficient, with **temporal pattern** adding nothing. This is a labelled-line-plus-rate code. The conjecture does not need population coding, combinatorial coding, or synchrony coding to be false—it only needs them to be absent from the single-unit comparison. But the rivals section acknowledges this: the population-coding rival predicts exactly the null the conjecture expects, and the conjecture's own design cannot distinguish "timing carries no information" from "timing carries information only in populations."

What does the mammalian evidence actually support?

**Rate coding.** There is solid evidence that nociceptor discharge rate encodes stimulus intensity in a monotonic, saturating fashion. This is true across species and preparations, from rat skin-nerve to human microneurography. No one disputes this.

**Temporal pattern coding.** The evidence is thinner than the conjecture implies, but it is not absent. The conjecture cites Cho et al. (2016) as "the only direct temporal-pattern result" and dismisses it as "a single unreplicated ex vivo study using chemical stimuli." That is accurate as far as it goes, but it omits the broader literature on temporal coding in nociceptive pathways. First, there is the well-established phenomenon of **first-spike latency** coding in dorsal horn neurons, where the latency of the first spike after stimulus onset carries information about stimulus location and intensity that is not captured by rate (Prescott, Ma & De Koninck, 2014, cited). This is a central phenomenon, but it demonstrates that the nervous system *does* use timing information downstream of the primary afferent, which weakens the claim that timing is irrelevant at the periphery. Second, there is the literature on **burst firing** in nociceptors, particularly in the context of sensitisation and ectopic discharge. Injured nociceptors do not simply fire faster; they fire in bursts with characteristic inter-spike interval structure (e.g., Amir et al., 2002; Liu et al., 2000). If the programme's ultimate target is neuropathic pain, the relevant question is not whether healthy evoked timing carries information, but whether pathological spontaneous timing does. The conjecture as posed cannot answer that.

**Labelled line coding.** The conjecture assumes that "unit identity, established by activity-dependent slowing" is a stable, meaningful classifier. This is true for the broad distinction between mechano-sensitive and mechano-insensitive C-nociceptors in healthy human skin (Serra et al., 1999). But it is not true in the pathological state. After nerve injury, ADS profiles change, fibres that were mechano-insensitive become mechano-sensitive, and the identity of a unit as "nociceptive" becomes less stable. The conjecture's reliance on ADS as a classifier is sound for the healthy-volunteer experiment it proposes, but it does not generalise to the condition the programme cares about.

**Preparation generalisability.** The evidence for rate coding in nociceptors comes from a mix of anaesthetised rodent, ex vivo skin-nerve, and awake human microneurography. The human microneurography literature is the most relevant and is robust. But the temporal-pattern literature is dominated by ex vivo and anaesthetised preparations, where the absence of descending modulation and the altered chemical environment change the statistics of discharge. The conjecture's proposed experiment in awake humans is exactly the right preparation to settle the question for healthy evoked pain. It cannot settle it for neuropathic pain.

---

## 3. WHERE IS PAIN MADE

This is the most serious objection, and the conjecture does not address it.

The conjecture asks whether fine timing in a single C-nociceptor carries information about a stimulus ensemble. But **pain is not a property of the stimulus ensemble**. Pain is a percept constructed in the CNS from a pattern of afferent traffic that has already been transformed by the dorsal horn. The discrimination between "nociceptive" and "innocuous" traffic is not made in the periphery; it is made centrally.

This matters for the conjecture in two ways.

First, the conjecture's killer experiment measures information about a *stimulus ensemble*, not about *pain*. A decoder that recovers stimulus features from spike timing is answering a sensory-coding question, not a pain question. The relationship between stimulus features and pain percept is itself a central transformation, and it is nonlinear, state-dependent, and plastic. Even if the conjecture is confirmed—even if timing adds nothing to rate-plus-identity for stimulus decoding—that tells us nothing about whether timing carries information relevant to the pain percept. The percept could be constructed entirely from rate and identity, or it could be constructed from timing features that are not stimulus-related but are still perceptually relevant (e.g., synchrony across fibres, which the single-unit design cannot detect).

Second, and more fundamentally, the conjecture's framing assumes that the relevant information is in the primary afferent at all. For acute, healthy, evoked pain, this is defensible. For the chronic neuropathic pain that motivates the programme, it is not. In established allodynia, the traffic that hurts arrives on Aβ fibres—low-threshold mechanoreceptors that are behaving normally. The pathology is central: disinhibition, altered descending modulation, and rewiring of Aβ input onto nociceptive projection neurons (Prescott et al., 2014, cited). A single-unit C-nociceptor recording in a healthy volunteer cannot speak to this, and the conjecture does not claim it can. But the programme's HC-1 and HC-2 are about nociceptive traffic carrying structure that is readable outside the CNS. If the pain-relevant discrimination is made centrally from peripherally indistinguishable traffic, then no amount of peripheral timing analysis—at any resolution—will recover it. The conjecture's own HC-2 killer is exactly this, and the conjecture does not engage with it.

The honest statement is: **the discrimination this conjecture proposes to test exists in the periphery only for acute, evoked, healthy nociception. For the chronic pain states that motivate the programme, the discrimination is constructed centrally, and no peripheral measurement can recover it.** This is not a reason to reject the conjecture as posed—it is a well-posed question about healthy sensory coding—but it is a reason to reject any inference from the conjecture's outcome to the programme's core commitments about pain.

---

## 4. THE PATHOLOGY

The conjecture is explicitly about healthy volunteers and acute evoked nociception. It does not claim to address neuropathic pain. But the programme's hard core is motivated by neuropathic pain, and the conjecture's "What it would change" section draws implications for HC-1 and HC-2 that are not limited to healthy states. So the pathology objection must be stated.

Neuropathic pain is not intense nociception. It is a different state of the system. The features that matter are:

**Ectopic spontaneous discharge.** Injured axons and their cell bodies in the DRG generate spontaneous action potentials that are not stimulus-evoked. This discharge has its own temporal structure—bursts, irregular intervals, and in some cases high-frequency trains—that is not captured by the stimulus-ensemble framework of the conjecture. The conjecture's killer experiment, by design, cannot measure this.

**Altered channel expression.** After nerve injury, voltage-gated sodium channel expression changes: Nav1.3, Nav1.7, and Nav1.8 are upregulated or redistributed, and this changes the intrinsic firing properties of the axon and soma. The ADS profile that the conjecture uses as a classifier is itself altered. A unit that was classified as a CMH nociceptor before injury may have a different ADS profile after injury, and a unit that was mechano-insensitive may become mechano-sensitive.

**Central disinhibition.** The dorsal horn undergoes loss of inhibitory tone after nerve injury, so that the same afferent input produces a larger postsynaptic response. This is a central change that no peripheral recording can detect.

**Glial involvement.** Microglia and astrocytes in the dorsal horn are activated after nerve injury and contribute to central sensitisation. This is entirely invisible to a peripheral recording.

**Allodynia on Aβ fibres.** In established allodynia, the traffic that hurts arrives on low-threshold mechanoreceptors that are behaving normally. The Aβ fibres are not nociceptors; they are touch fibres. Their discharge is stimulus-locked, regular, and high-rate. A proposal that filters "pain fibres" does nothing about a system in which touch fibres have been rewired into a pain percept. The conjecture does not propose to filter anything, but its framing—that nociceptor timing is the relevant question—inherits the same assumption that C-001 was refuted for.

The conjecture's defenders might say: "This is a measurement claim about healthy coding, not a claim about pathology." That is true as far as it goes. But the "What it would change" section says that if the conjecture is confirmed, "every conjecture about reading or writing a temporal pattern on a single axon is attacking a channel that does not carry one." That is a general claim about the channel, and it is being used to redirect the programme. The channel in neuropathic pain is not the same channel as in healthy skin.

---

## 5. PLASTICITY AND HABITUATION

The conjecture is a measurement study, not an intervention. It does not propose to hold a fixed input over months or years. So the habituation objection does not apply directly.

However, the conjecture's framing—that rate-plus-identity is sufficient—has implications for the programme's intervention branch. If fine timing carries no information, then the programme's PB-2 (loss of efficacy is habituation to a fixed stimulus, addressable by pattern variation) loses its mechanistic basis. If the nervous system does not read fine timing, then varying the fine timing of a stimulation pattern cannot be the mechanism by which habituation is avoided. The conjecture's own "What it would change" section acknowledges this: if confirmed, "the case for pattern-based intervention becomes an evidential case rather than a plausibility argument." That is a polite way of saying the plausibility argument dies.

This is not an objection to the conjecture; it is a consequence. But it is a consequence the programme should weigh carefully before committing to the experiment. A null result on this conjecture would not merely be a null result; it would remove the mechanistic rationale for a substantial part of the programme's intervention strategy.

---

## 6. COLLATERAL TRAFFIC

The conjecture is a recording study, not an intervention. It does not propose to block, stimulate, or otherwise interfere with any structure. So the collateral-traffic objection does not apply.

The only structure being "intervened on" is the microneurography needle, which is inserted into the peroneal or radial nerve. This carries a small risk of transient paraesthesia and a very small risk of nerve injury, but it is a standard research procedure with an established safety record. No touch, proprioception, thermoregulation, sudomotor, vasomotor, trophic, or motor function is lost.

---

## 7. SPECIES AND PREPARATION

The conjecture's killer experiment is human, awake, healthy volunteers. This is the right preparation for the question as posed. The evidence base it draws on is mixed:

- **Serra et al. (1999):** Human microneurography, awake. This is the gold standard for ADS-based classification of C-nociceptors. Generalises directly.
- **Schmidt et al. (1995):** Human microneurography, awake. The classic demonstration of mechano-insensitive C-nociceptors. Generalises directly.
- **Cho et al. (2016):** Ex vivo, chemical stimuli. Does not generalise to awake human evoked pain. The conjecture acknowledges this.
- **Werland et al. (2021):** Pig, electrical stimulation. Does not generalise to natural stimulation in humans. The conjecture cites it only for the 100 Hz following claim, which is not central to the argument.
- **Prescott et al. (2014):** Review, central mechanisms. Generalises conceptually but is not a primary data source for the peripheral claim.
- **Ghitani et al. (2025):** This is a central study (dorsal horn, optogenetics, mouse). It is cited but not used in the mechanism. Its relevance to the peripheral timing claim is indirect.
- **Troglio et al. (2025):** Human microneurography, methodological. Generalises directly.
- **Borst & Theunissen (1999):** Review of information theory in neural coding. Generalises conceptually.

The conjecture's supports that would not survive translation are the ex vivo and anaesthetised ones, but the conjecture does not rely on them for its central claim. The central claim rests on human microneurography and the ADS mechanism, both of which are solid.

The one preparation issue worth flagging: **the conjecture's killer experiment uses healthy volunteers, but the programme's hard core is about pain.** The translation gap is not from anaesthetised to awake, or from rodent to human; it is from healthy to pathological. That gap is not addressed by the conjecture and cannot be closed by the proposed experiment.

---

## Summary of objections

1. **The wire is right, but the population is heterogeneous.** The conjecture's healthy-volunteer design preferentially recruits CMH units and cannot speak to the CMi units that dominate in pathological states.

2. **The code is under-specified.** The conjecture needs rate-plus-identity to be sufficient, but the evidence for temporal coding in nociceptive pathways is not absent—it is thin and mostly from preparations that do not generalise. The conjecture's own design cannot distinguish "timing carries no information" from "timing carries information only in populations."

3. **Where pain is made is the fatal objection to the programme's inference, not to the conjecture as posed.** The discrimination the conjecture tests exists in the periphery only for acute, healthy, evoked nociception. For chronic pain, the discrimination is central, and no peripheral measurement can recover it. The conjecture does not claim otherwise, but the programme's HC-1 and HC-2 do.

4. **The pathology is not addressed.** Neuropathic pain is not intense nociception, and the conjecture's healthy-volunteer design cannot speak to ectopic discharge, altered channel expression, central disinhibition, glial involvement, or Aβ-mediated allodynia.

5. **Plasticity and habituation are not directly relevant**, but a null result would remove the mechanistic rationale for the programme's pattern-variation intervention strategy.

6. **Collateral traffic is not relevant** to a recording study.

7. **Species and preparation are mostly right**, with the caveat that the healthy-to-pathological translation gap is the one that matters and is not addressed.

---

VERDICT: MINOR — The conjecture is well-posed as a measurement claim about healthy evoked nociception, but it must state explicitly that its outcome cannot bear on HC-1 or HC-2 for neuropathic pain, because the pain-relevant discrimination in that state is constructed centrally from peripherally indistinguishable traffic, and the single-unit healthy-volunteer design cannot distinguish "timing carries no information" from "timing carries information only in populations."
