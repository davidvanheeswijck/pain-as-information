# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `02-biological-plausibility.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-01T12:29:26+00:00 · tokens in=7794 out=4809
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review: C-003 — Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain

## Where the conjecture is right

The conjecture correctly identifies a genuine and under-exploited tension in the evidence base. The tonic-disinhibition account of allodynia (Coull, Duan, Lu) and the coincidence account suggested by Ghitani et al. do make opposite predictions about whether timing matters, and no published experiment has cleanly separated them by controlling C-fibre timing independently of C-fibre count while holding Aβ input constant. That is a real gap, and the proposed experiment — optogenetic control of a defined nociceptor population, calibrated mechanical stimulation, variable delays, dorsal horn readout plus behaviour — is the right shape of experiment to fill it. The conjecture also correctly recognises that the "both, at different disease stages" rival is the most likely to be true and that the design should run the delay series at two timepoints. That is the kind of self-awareness that most theoretical proposals lack. The forbidden observation is stated precisely enough to be useful, and the refutation threshold (flat response probability across delays, with a no-burst control confirming the paradigm can detect a difference) is a legitimate discriminator.

The problem is not the question. The problem is that the conjecture's framing of the mechanism, and several of its implicit assumptions about what the nervous system is doing, are not the nervous system that exists.

---

## 1. THE WIRE

The conjecture does not make detailed claims about primary afferent conduction velocity, fibre class, or extracellular signal amplitude, so it avoids the usual fatal error of proposing to "read pain from a nerve" with a sensor that cannot see C-fibres. But it inherits a subtler version of the same problem.

The mechanism requires that ongoing C-nociceptor discharge produces a **transient** facilitation of dorsal horn responses to Aβ input, decaying over hundreds of milliseconds to a few seconds. The conjecture cites windup-like facilitation as the timescale anchor. Windup is real — Mendell and Wall (1965) described it, and it is a progressive increase in dorsal horn neuron responses to repeated C-fibre stimulation at frequencies above roughly 0.3–0.5 Hz. But windup is a **cumulative, frequency-dependent** phenomenon, not a single-burst-then-decay phenomenon. A single C-fibre burst produces a short-latency excitatory postsynaptic potential lasting tens of milliseconds, not a facilitation window of hundreds of milliseconds to seconds. The long-latency, long-duration components of C-fibre-evoked responses in dorsal horn neurons are mediated by neuropeptides (substance P, CGRP) and are real, but they are **slow depolarisations lasting seconds to tens of seconds**, and they are produced by **repeated or high-frequency** stimulation, not by a single burst of the kind the conjecture proposes to deliver.

There is a further problem with the assumption that the experimenter can "set C-fibre spike count" optogenetically and thereby control the facilitation. Optogenetic activation of a defined nociceptor population does not reproduce the natural pattern of C-fibre discharge. Natural ongoing nociceptor activity in inflammatory and neuropathic states is **irregular, low-frequency, and asynchronous across fibres** (see Djouhri et al., 2006, for spontaneous activity in neuropathic nociceptors; Xiao and Bennett, 2007, for the pattern in DRG neurons). A synchronous optogenetic burst recruits the population in a way that never occurs naturally, produces a synchronous volley that maximises spatial and temporal summation at the first synapse, and therefore **maximises** the very facilitation the conjecture wants to study. This is not a fatal objection to the experiment — optogenetics is the right tool for the question — but it means the measured decay constant will be an upper bound on what natural ongoing activity produces, and the conjecture should say so.

The refractory period and activity-dependent slowing of C-fibres also matter for the interpretation. C-fibres show pronounced activity-dependent slowing of conduction velocity (Torebjörk and Hallin, 1974; Serra et al., 1999), and this slowing is itself a form of short-term plasticity that alters the **timing** of spike arrival at the dorsal horn. If the conjecture's mechanism depends on relative timing of C-fibre and Aβ input, then activity-dependent slowing is not a nuisance variable — it is part of the mechanism, and it will vary with the history of C-fibre firing in a way the optogenetic burst does not capture.

Finally, the conjecture's claim that "spike arrival on the millisecond scale" is the relevant timing precision for the coincidence is almost certainly wrong for a mechanism mediated by neuropeptide release and second-messenger cascades. Those processes operate on the scale of hundreds of milliseconds to seconds, which is why the conjecture's own proposed delays (50 ms to 3 s) are the right range. But the conjecture should not invoke millisecond spike timing as the substrate when the mechanism it proposes is a slow neuromodulatory one.

---

## 2. THE CODE

The conjecture needs a **temporal coincidence code**: the information that determines whether Aβ input is read as touch or pain is carried by the **relative timing** of C-fibre and Aβ input, not by the rate of either alone, not by the identity of the fibres alone, and not by a labelled line.

What is the evidence for temporal coincidence coding in the dorsal horn?

The strongest evidence comes from **windup** itself, which is a temporal-pattern phenomenon: the same number of C-fibre spikes produces a larger postsynaptic response when delivered at higher frequency. That is a rate code in disguise, however — windup is frequency-dependent, and the relevant variable is the **interval between successive C-fibre volleys**, not the interval between C-fibre and Aβ input.

There is also evidence for **heterosynaptic facilitation** in the dorsal horn: C-fibre input can facilitate responses to subsequent Aβ input (Woolf and King, 1990, for the original demonstration of Aβ-mediated allodynia after C-fibre conditioning; Woolf, 1983, for the central sensitisation framework). But the facilitation demonstrated in those experiments is **long-lasting** — minutes to hours — and is produced by **repeated** C-fibre stimulation, not by a single burst. The conjecture's proposed window of "a few hundred milliseconds" is not the timescale of central sensitisation as classically defined.

The evidence for a **brief, decaying** eligibility window of the kind the conjecture proposes is thin. The closest phenomenon is **paired-pulse facilitation** at the C-fibre–dorsal horn synapse, which decays over tens to hundreds of milliseconds. But paired-pulse facilitation is a homosynaptic phenomenon (C-fibre facilitating C-fibre), not a heterosynaptic one (C-fibre facilitating Aβ), and the conjecture needs the latter.

The conjecture also needs the facilitation to be **specific to the nociceptive output pathway** — Aβ input arriving during the window is routed to nociceptive projection neurons, while Aβ input arriving outside the window is not. That is a strong claim about circuit architecture. The dorsal horn circuitry that has been dissected (Duan et al., 2014; Lu et al., 2013; Peirs et al., 2015) shows that Aβ input gains access to nociceptive output through **specific interneuron populations** (PKCγ-expressing excitatory interneurons, somatostatin-expressing interneurons, and the loss of glycinergic inhibition onto those populations). Those are **structural** changes, not transient ones. The conjecture is proposing that the same routing can occur **transiently** in the absence of structural change, driven only by ongoing C-fibre activity. That is not impossible, but it is not supported by any direct evidence, and the conjecture should acknowledge that it is proposing a novel circuit mechanism rather than extending an established one.

The preparation problem is acute here. The evidence for temporal coding in dorsal horn neurons comes almost entirely from **anaesthetised or spinalised** preparations, where descending modulation is absent or blunted. In the awake animal, descending controls from the rostral ventromedial medulla and locus coeruleus tonically modulate dorsal horn excitability on a timescale of seconds to minutes, and those controls are themselves modulated by behavioural state. A facilitation window measured in an anaesthetised mouse may not exist, or may have a different time course, in an awake human with a decade-old injury. The conjecture's killer experiment is in mice, and the translation to humans is assumed, not argued.

---

## 3. WHERE IS PAIN MADE

This is the most likely fatal objection, and the conjecture walks directly into it.

The conjecture needs a **peripherally readable** difference between nociceptive and innocuous traffic — specifically, it needs the **timing** of C-fibre activity relative to Aβ activity to be the variable that determines whether touch is read as pain. If that discrimination is made centrally, then the conjecture's mechanism is a central one, and the intervention it motivates (suppressing or desynchronising ongoing nociceptor discharge) acts on the periphery to influence a central computation.

The honest answer is that the discrimination the conjecture proposes to exploit is **made in the dorsal horn**, not in the periphery. The Aβ fibres that carry the touch input in allodynia are behaving normally — the conjecture itself says so, correctly, citing the evidence. The C-fibres that carry the ongoing activity are also behaving normally for an inflamed or injured nerve — they are spontaneously active, which is what inflamed and injured nociceptors do. Neither fibre population carries a signal that says "pain." The pain is made when the two signals **coincide in the dorsal horn** and the dorsal horn is in a state that routes the Aβ input to nociceptive output.

This is not a peripheral code. It is a central computation that depends on the state of the dorsal horn network. The conjecture's proposed intervention — suppressing or desynchronising ongoing C-fibre discharge — would act peripherally, but its target is a central computation. That is not necessarily wrong: peripheral interventions can influence central computations, and that is the entire rationale for neuromodulation. But the conjecture should be honest that it is not reading a peripheral code; it is manipulating a peripheral input to a central computation, and the central computation is the thing that determines the outcome.

The deeper problem is that the conjecture's mechanism, if true, would mean that the **same** peripheral timing relationship produces pain in one dorsal horn state and touch in another. The dorsal horn state is set by the chloride gradient, the state of inhibition, the presence of microglial BDNF, and descending modulation — none of which are readable from the periphery. So even if the conjecture's timing window is real, a peripheral sensor that measures C-fibre and Aβ timing would not know whether the dorsal horn is in a state where that timing relationship produces pain. The discrimination is central, and the conjecture's programme (HC-2) requires it to be peripherally readable. This is the point where HC-2 is pressed hardest, exactly as the programme file acknowledges.

---

## 4. THE PATHOLOGY

The conjecture is about **mechanical allodynia**, and it correctly identifies that the traffic that hurts in established allodynia arrives on Aβ fibres behaving normally. That is the right starting point.

But the conjecture then proposes that the mechanism is a **transient** facilitation window opened by ongoing C-fibre activity, and that this is an alternative to the tonic-disinhibition account. The pathology literature says otherwise.

In established neuropathic pain, the changes are **structural and persistent**:

- **Ectopic spontaneous discharge** from injured axons and the DRG is present, and it is not a brief burst — it is ongoing, often for the life of the animal (Wall and Gutnick, 1974; Devor, 2009). The conjecture treats ongoing C-fibre activity as a trigger that opens a window; the pathology literature treats it as a **tonic drive** that maintains central sensitisation.

- **Altered channel expression** in the DRG and along the injured axon (Nav1.3, Nav1.7, Nav1.8 upregulation; potassium channel downregulation) changes the **pattern** of spontaneous discharge, not just its presence (Waxman et al., 1999; Dib-Hajj et al., 2010). The conjecture's optogenetic burst does not reproduce this pattern.

- **Central disinhibition** is not a transient state. The collapse of the chloride gradient in lamina I neurons, mediated by microglial BDNF acting on KCC2, is a **persistent** change in the anion reversal potential that converts GABAergic and glycinergic inhibition into excitation (Coull et al., 2003, 2005). That change is not reversed on the timescale of hundreds of milliseconds; it is reversed over days to weeks by blocking BDNF signalling or restoring KCC2 function.

- **Glial involvement** is not a passive response to C-fibre activity. Microglia and astrocytes are activated for weeks to months after nerve injury, and they release BDNF, TNF-α, IL-1β, and other mediators that maintain the disinhibited state (Ji et al., 2013; Inoue and Tsuda, 2018). The conjecture's mechanism has no place for glia, and that is a problem because the glial response is part of what makes the disinhibition tonic.

- **The PKCγ route** by which Aβ input reaches nociceptive output is a **structural** circuit change: PKCγ-expressing interneurons in lamina II receive Aβ input and, after nerve injury, transmit it to lamina I projection neurons (Lu et al., 2013; Peirs et al., 2015). That route is not opened transiently by C-fibre activity; it is opened persistently by the loss of inhibition onto those interneurons.

The conjecture's response to this is that the tonic-disinhibition account and the coincidence account "make opposite predictions about whether allodynia can be interrupted without changing anything structural." That is true, and it is the strongest part of the conjecture. But the conjecture's own "both, at different disease stages" rival is the most likely to be true, and the conjecture should reckon with what that means: in a decade-old injury, the structural changes are established, and the transient window, if it exists at all, is a minor contributor on top of a tonic disinhibition that is already routing Aβ input to nociceptive output regardless of timing.

A proposal that filters or desynchronises C-fibre activity does nothing about a system in which the Aβ-to-nociceptive route is already open. The conjecture acknowledges this in its "What it would change" section, but it does not reckon with the probability that the tonic account is correct for the clinical population it ultimately cares about.

---

## 5. PLASTICITY AND HABITUATION

The conjecture does not propose an intervention held over months or years, so this objection is less central than it would be for a neuromodulation proposal. But the conjecture's "What it would change" section proposes that an intervention that suppresses or desynchronises ongoing nociceptor discharge would close the window and reduce allodynia. That is an intervention proposal, and it inherits the plasticity problem.

Any fixed intervention that suppresses C-fibre activity will be met by the nervous system's homeostatic response. The DRG and dorsal horn are not passive: they regulate receptor expression, channel density, and synaptic strength in response to changes in input. Chronic suppression of C-fibre activity would be expected to produce **compensatory upregulation** of excitability in the very pathways being suppressed, as has been observed with chronic opioid administration (tolerance), chronic local anaesthetic block (rebound hyperexcitability), and chronic spinal cord stimulation (loss of efficacy over time, which the programme's own PB-2 acknowledges).

The conjecture's proposed intervention — desynchronising ongoing C-fibre discharge rather than suppressing it — is more interesting from a plasticity standpoint, because it does not remove the input, only changes its pattern. But the nervous system adapts to patterns too. A fixed desynchronisation pattern is a training signal, and the dorsal horn will learn it. The programme's own PB-2 says that loss of efficacy in implanted stimulation is habituation to a fixed stimulus and is addressable by pattern variation. The conjecture should acknowledge that any intervention based on its mechanism would face the same problem: the window-closing effect would habituate unless the intervention itself varied.

---

## 6. COLLATERAL TRAFFIC

The conjecture does not propose to intervene on a specific structure, so this objection is less direct than it would be for a nerve block or ablation proposal. But the conjecture's mechanism involves **ongoing C-nociceptor discharge** as the trigger, and its proposed intervention would suppress or desynchronise that discharge.

C-nociceptors are not a dedicated pain channel. They are polymodal, and their ongoing activity in inflammatory and neuropathic states is accompanied by their normal functions: **thermoregulation** (C-warm and C-cold fibres), **sudomotor and vasomotor autonomic function** (C-fibres innervating sweat glands and blood vessels), **trophic support** (C-fibres release CGRP and substance P that maintain tissue integrity and wound healing), and **nociception** itself, which is a protective function that the intervention would blunt.

An intervention that suppresses ongoing C-fibre activity would therefore suppress more than the allodynia trigger. It would impair thermoregulation, autonomic function, and trophic support in the affected limb. The conjecture's proposed alternative — desynchronisation rather than suppression — is better on this front, because it leaves the total C-fibre traffic intact and only changes its timing. But the conjecture should acknowledge that desynchronising C-fibre activity is not a free lunch: the synchrony of C-fibre discharge carries information about the intensity and quality of noxious stimuli, and desynchronising it would degrade that information.

---

## 7. SPECIES AND PREPARATION

The conjecture's supporting evidence is:

- **Ghitani et al. (2025)**: mouse, inflammatory model, in vivo imaging of DRG neurons. This is the strongest support for the coincidence framing, but it is **mouse**, **acute inflammatory**, and the readout is **DRG activity**, not dorsal horn processing or behaviour. The authors' suggestion that allodynia arises from coincidence is an **interpretation**, not a demonstrated mechanism.

- **Coull et al. (2003, 2005)**: rat, **spinal cord slices** and in vivo, neuropathic and inflammatory models. The chloride gradient collapse is demonstrated in **lamina I neurons in slices**, which is a preparation that removes descending modulation and most of the network. The in vivo confirmation is partial.

- **Duan et al. (2014)**: mouse, **optogenetic and genetic circuit dissection**, neuropathic model. This is the strongest evidence for the Aβ-to-nociceptive route, but it is **mouse**, and the circuit dissection is done in **anaesthetised** animals.

- **Lu et al. (2013)**: mouse, **genetic ablation and behavioural testing**, neuropathic model. Behavioural readout is in **awake** animals, but the circuit mechanism is inferred from **anatomical and genetic** evidence, not from direct recording of the proposed coincidence.

- **Peirs et al. (2015)**: mouse, **optogenetic and chemogenetic**, neuropathic model. Behavioural readout in awake animals, but again the circuit mechanism is inferred.

- **Mendell and Wall (1965)**: cat, **spinalised, anaesthetised**, acute. The windup phenomenon is real but was demonstrated in a preparation that is maximally different from an awake human with a decade-old injury.

- **Woolf (1983)**: rat, **anaesthetised**, acute. The central sensitisation framework was built on acute, anaesthetised preparations.

None of the conjecture's supports come from **awake, behaving humans**. The closest is the behavioural readout in awake mice, which is a long way from a human with a decade-old neuropathic injury. The conjecture's killer experiment is in mice, and the translation to humans is assumed.

The specific reasons the supports would not survive translation:

1. **Anaesthesia** removes descending inhibition, which tonically suppresses dorsal horn excitability. A facilitation window measured under anaesthesia may be larger and longer than in the awake state.

2. **Acute models** do not have the structural changes of established neuropathic pain. The chloride gradient collapse, the microglial activation, and the PKCγ circuit changes take days to weeks to develop, and they are not present in acute inflammatory models.

3. **Mouse DRG imaging** (Ghitani) measures activity in the cell body, not at the central terminals where the proposed coincidence occurs. The relationship between DRG activity and central terminal release is not one-to-one, especially in the presence of activity-dependent changes in conduction and terminal excitability.

4. **Optogenetic activation** of a defined nociceptor population does not reproduce the natural pattern of ongoing activity, as discussed above.

---

## Summary

The conjecture asks a good question and proposes a reasonable experiment to answer it. But it is built on a mechanism — a transient, C-fibre-triggered eligibility window for Aβ input — that is not supported by the physiology of the dorsal horn as it is currently understood. The facilitation that C-fibre input produces is either short (paired-pulse facilitation, tens of milliseconds) or long (central sensitisation, minutes to hours), and the conjecture's proposed window of hundreds of milliseconds to seconds sits in a gap that no direct evidence fills. The discrimination the conjecture proposes to exploit is made centrally, not peripherally, and the conjecture's programme commitment HC-2 is pressed hardest by exactly this point. The pathology of established neuropathic pain is structural and persistent, and the conjecture's own "both, at different disease stages" rival is the most likely to be true. The conjecture should be reframed as a test of a **novel circuit mechanism** rather than as a resolution of a contradiction in the evidence base, and it should acknowledge that even if the mechanism is real in an acute inflammatory mouse, it may be a minor contributor in a decade-old human injury.

VERDICT: MAJOR — The proposed transient eligibility window of hundreds of milliseconds to seconds is not supported by the physiology of C-fibre-evoked facilitation in the dorsal horn, which is either short (paired-pulse, tens of milliseconds) or long (central sensitisation, minutes to hours); the conjecture needs direct evidence for a facilitation time constant in the proposed range before the killer experiment is worth running.
