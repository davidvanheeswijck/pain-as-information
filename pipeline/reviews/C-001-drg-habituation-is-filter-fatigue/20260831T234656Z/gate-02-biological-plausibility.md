# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `02-biological-plausibility.md` · Subject: `C-001-drg-habituation-is-filter-fatigue.md`
> 2026-08-31T23:51:39+00:00 · tokens in=5432 out=4357
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review of C-001: Loss of benefit in chronic DRG stimulation is decay of T-junction filtering, not tolerance to charge

## Where the conjecture is right

The conjecture correctly identifies a genuine and under-exploited feature of sensory neuron physiology: the T-junction of pseudounipolar neurons is indeed a site of impedance mismatch where propagation is marginal and state-dependent. The observation that C-fibre spikes have the lowest safety factor at this junction, and that somatic membrane potential shifts can gate propagation, is real and has been demonstrated in careful preparations. The conjecture also correctly identifies that the clinical literature on DRG stimulation lacks mechanistic endpoints, that explantation rates for loss of benefit are substantial and under-characterised, and that "loss of benefit" and "tolerance to charge" are currently conflated in clinical practice without evidence distinguishing them. The proposed experiment is well-designed, appropriately powered, and would genuinely discriminate between the rival hypotheses. The willingness to record that a supporting citation was withdrawn, and to note that this strengthens rather than weakens the premise, is exactly the kind of epistemic hygiene the programme's design intends.

Now the objections.

---

## 1. THE WIRE

The conjecture's account of the primary afferent does not match reality in several respects.

**Conduction velocity and fibre class.** The conjecture treats "C-fibre trains" as the relevant nociceptive signal and Aβ as the innocuous control. But the Chao et al. preparation the conjecture leans on is a rat preparation, and the relevant human anatomy differs in ways that matter. In human dorsal roots, C-fibre conduction velocities are 0.5–2 m/s, Aδ 2–30 m/s, and Aβ 30–70 m/s. The T-junction filtering mechanism proposed depends on the safety factor for propagation, which is a function of the impedance mismatch at the branch point. The magnitude of that mismatch scales with the ratio of the soma/dendritic capacitance to the axonal capacitance, and that ratio is not identical across species. More importantly, the conjecture assumes that the C-fibre population is homogeneous in its susceptibility to T-junction failure. It is not. Unmyelinated fibres in human nerve include not only nociceptors but also C-low-threshold mechanoreceptors (C-LTMRs), C-thermoreceptors, C-sympathetic efferents, and C-fibres innervating viscera. A mechanism that "fails C-fibre propagation" fails all of these, and the conjecture offers no account of what happens to thermoregulation, sudomotor function, or the pleasant-touch system when their C-fibres are silenced.

**Spontaneous rate and refractory period.** The conjecture's proposed mechanism requires that the filtering enhancement builds over ~20 seconds of stimulation and that it is maintained by continued stimulation. But the spontaneous discharge rate of human C-nociceptors is typically <0.1 Hz, and their refractory period is 1–2 seconds. A 20 Hz stimulus is therefore not "riding on" ongoing C-fibre traffic; it is a massive, non-physiological drive. The conjecture treats the C-fibre as a passive cable whose propagation can be gated by a somatic offset, but a C-fibre driven at 20 Hz for 20 seconds is not in a physiological state. It is in a state of profound activity-dependent slowing (see below), and the "filtering" observed may be an artefact of that non-physiological drive rather than a mechanism that operates on naturally occurring nociceptive traffic.

**Activity-dependent slowing.** This is the most serious wire-level objection. Unmyelinated fibres exhibit pronounced activity-dependent slowing of conduction velocity: after a train of impulses, conduction velocity falls by 10–30%, and recovery takes minutes. This is a well-established property of C-fibres in every species examined, including human (Serra et al., 1999, *J Physiol* 515:799–811; Weidner et al., 2000, *Brain* 123:1716–27). The Chao et al. observation that C-fibre activity "abates" during 20 Hz ganglion stimulation is entirely consistent with the known phenomenon of activity-dependent conduction block in unmyelinated fibres driven at non-physiological rates. The conjecture interprets this as "enhanced T-junction filtering" caused by Ca2+-SK activation. But the simpler explanation—that 20 Hz is simply beyond the sustainable firing rate of most C-fibres, and that they fail due to the biophysics of unmyelinated conduction itself—is not excluded by the data cited. The Kent et al. model the conjecture relies on is a computational model, not a measurement, and it was constructed to reproduce the Chao et al. observation. It is not independent evidence for the mechanism.

**Extracellular signal size.** The conjecture proposes to distinguish C-fibre propagation failure from Aβ propagation using "teased-fibre recording" in rat. This is feasible in an acute preparation. But the conjecture also gestures toward the clinical relevance of this distinction, and here the wire problem is fatal. The extracellular action potential of a single C-fibre at the dorsal root ganglion is on the order of 1–10 µV at the recording electrode, while Aβ fibres produce signals of 50–500 µV. The C-fibre signal is not merely smaller; it is buried in the noise floor of any chronically implanted electrode system, and it is outnumbered by Aβ and Aδ fibres by roughly 10:1 in the dorsal root. The conjecture's own citation of ECAP measurement in the cord (2.8 µV resolution) is for compound potentials dominated by large myelinated fibres. There is no existing implanted hardware that can resolve single C-fibre propagation failure in a human dorsal root ganglion, and the conjecture does not propose one. This is a problem for the *testability* of the conjecture in humans, not for the rat experiment, but it matters for the programme's HC-2.

---

## 2. THE CODE

The conjecture needs a **labelled-line** code: C-fibre traffic is nociceptive, Aβ traffic is innocuous, and the therapeutic effect comes from selectively gating the former while sparing the latter. This is the simplest possible coding scheme, and it is the one the evidence has been least kind to.

The labelled-line theory of pain was dominant in the 1960s and 1970s, and it survives in attenuated form in the distinction between nociceptive and non-nociceptive primary afferents. But the evidence from awake human microneurography, from dorsal horn recordings, and from the neuropathic pain literature is that the relationship between peripheral fibre class and pain percept is not a labelled line. It is combinatorial and state-dependent.

Specifically:

- **Rate coding** is well established for nociceptors: perceived intensity of heat pain correlates with C-fibre and Aδ discharge rate (LaMotte and Campbell, 1978, *J Neurophysiol* 41:509–28). But rate coding alone does not explain allodynia, where Aβ traffic produces pain, or the phenomenon of "second pain" where C-fibre input produces a delayed, diffuse percept distinct from the sharp Aδ percept.
- **Population coding** is required to explain spatial and temporal summation, and the fact that the same C-fibre can contribute to pain, itch, or warmth depending on the population context (Schmelz et al., 1997, *J Neurosci* 17:8003–8).
- **Temporal pattern coding** is supported by the observation that the same mean rate produces different percepts depending on burst structure (Handwerker and Kobal, 1993, *Physiol Rev* 73:639–71), but the effect size is modest and the evidence comes largely from cutaneous C-fibres in acute preparations.

The conjecture's mechanism requires that the *only* thing that matters is whether C-fibre spikes propagate past the T-junction. It does not engage with the possibility that the dorsal horn reads the *pattern* of surviving spikes, or that the therapeutic effect of DRG stimulation is not "fewer C-fibre spikes" but "different C-fibre spike pattern." This is not a fatal objection to the rat experiment, which measures propagation failure directly. But it is a fatal objection to the clinical interpretation, because the human dorsal horn is not a simple relay.

The evidence for labelled-line coding in mammals comes overwhelmingly from anaesthetised or decerebrate preparations, where the dorsal horn is in a state that does not generalise to awake humans. In awake humans, the same peripheral input can produce different percepts depending on attention, expectation, and descending modulation (Tracey and Mantyh, 2007, *Neuron* 55:377–91). A mechanism that operates entirely at the T-junction is blind to all of this.

---

## 3. WHERE IS PAIN MADE

The discrimination the conjecture proposes to exploit—nociceptive versus innocuous traffic—is **not made in the periphery**. It is made in the dorsal horn, and it is made there by a network whose state is set by descending projections, local inhibitory tone, and glial signalling.

The primary afferent does not "know" whether it is a nociceptor. It is a transducer with a threshold and a dynamic range. The same C-fibre that signals noxious heat at 45°C also signals warmth at 38°C, and the difference between "warm" and "painful" is made centrally, by the pattern of dorsal horn neurons recruited and by the state of the network (Craig, 2003, *Annu Rev Neurosci* 26:1–30).

The conjecture's mechanism operates at the T-junction, which is peripheral to the dorsal horn. It proposes to gate C-fibre propagation based on fibre class. But the fibre class is not the code for pain. The code for pain is the *interpretation* of the arriving traffic by the dorsal horn, and that interpretation is not fixed. In a human with a decade-old injury, the dorsal horn has undergone substantial plasticity: loss of inhibitory interneurons, sprouting of Aβ terminals into lamina II, changes in chloride gradient that convert GABAergic inhibition to excitation, and microglial activation (Coull et al., 2005, *Nature* 438:1017–21; the conjecture cites this paper but does not reckon with its implication). In that state, the same C-fibre traffic that was innocuous before the injury is now painful, and the same Aβ traffic that was innocuous is now painful. Gating C-fibre propagation at the T-junction does not address the Aβ contribution, and it does not address the central amplification that makes the surviving C-fibre traffic sufficient to drive the percept.

This is the most likely fatal objection to the programme's HC-2, and the conjecture does not engage with it. The conjecture's own "most uncomfortable rival"—central compensation—is not a rival to the mechanism; it is the default explanation for why the mechanism, even if it works as described, would not produce lasting clinical benefit.

---

## 4. THE PATHOLOGY

The conjecture treats neuropathic pain as if it were intense nociception: C-fibres firing too much, and the therapeutic goal is to reduce C-fibre traffic. This is not what neuropathic pain is.

In established neuropathic pain, the relevant phenomena include:

- **Ectopic spontaneous discharge from injured axons and the DRG.** After nerve injury, injured A-fibres and C-fibres develop spontaneous activity originating at the neuroma and the ganglion (Wall and Gutnick, 1974, *Exp Neurol* 43:580–93; Devor, 2009, *Exp Neurol* 217:226–38). This activity is not "traffic from the periphery" in the normal sense; it is generated at the site of injury and propagates centrally. The T-junction filtering mechanism proposed by the conjecture would gate this traffic, but only if the ectopic focus is distal to the T-junction. In many cases, the ectopic focus is *at* the ganglion, and the T-junction is not in the path.

- **Altered channel expression.** Injured sensory neurons upregulate Nav1.3, Nav1.7, and Nav1.8, and downregulate potassium channels, producing hyperexcitability that is not dependent on peripheral input (Waxman et al., 1999, *Proc Natl Acad Sci* 96:7635–9). The conjecture's mechanism—Ca2+-SK-mediated hyperpolarisation—would be opposed by these changes, and the conjecture does not account for the possibility that the same chronic stimulation that enhances SK conductance also drives compensatory upregulation of the very channels that produce ectopic discharge.

- **Central disinhibition.** The Coull et al. paper the conjecture cites demonstrates that after nerve injury, the chloride gradient in lamina I neurons collapses, converting GABAergic inhibition to excitation. This means that the dorsal horn is not merely receiving too much C-fibre traffic; it is amplifying whatever traffic arrives. Gating C-fibre propagation at the T-junction reduces the input, but it does not address the amplifier.

- **Allodynia on Aβ fibres.** In established allodynia, the traffic that hurts is arriving on low-threshold mechanoreceptors that are behaving normally. The Aβ fibres are not injured, not ectopic, and not hyperexcitable. They are doing exactly what they always did. The pathology is that the dorsal horn now interprets their normal activity as pain. The conjecture's mechanism explicitly spares Aβ fibres—that is its claimed selectivity—but in allodynia, sparing Aβ fibres means sparing the very traffic that produces the pain.

A proposal that filters "pain fibres" does nothing about a system in which touch fibres have been rewired into a pain percept. This is not a peripheral problem, and it cannot be fixed at the T-junction.

---

## 5. PLASTICITY AND HABITUATION

The conjecture proposes that the decline in benefit is "decay of filtering enhancement under an unvarying stimulus," and that varying the pattern will restore it. This is a hypothesis about plasticity, and it is testable in the rat preparation proposed. But the conjecture does not reckon with what is known about plasticity in the relevant systems.

**Accommodation to sustained depolarisation.** Neurons accommodate to sustained depolarising or hyperpolarising inputs by adjusting their channel populations. A chronic SK-mediated hyperpolarisation will, over days to weeks, be opposed by downregulation of SK channels, upregulation of depolarising conductances, or shifts in the voltage dependence of existing channels. This is not a speculative mechanism; it is the standard homeostatic response of excitable cells to sustained perturbation (Turrigiano, 1999, *Nature* 391:892–6). The conjecture's own proposed decay mechanism is an instance of this, but the conjecture treats it as specific to the *pattern* of stimulation rather than to the *presence* of stimulation. The evidence for pattern-specific habituation in sensory systems is weak, and the evidence for amplitude-dependent accommodation is strong.

**Receptor regulation.** Chronic electrical stimulation of neural tissue produces changes in the tissue surrounding the electrode: glial encapsulation, changes in extracellular ion concentrations, and altered expression of ion channels in the neurons nearest the electrode. These changes are not pattern-dependent; they are charge-dependent. The conjecture's rival "mechanical and anatomical drift" is not a rival to the neural adaptation story; it is a parallel process that occurs on the same timescale and produces the same clinical picture.

**Decline of implanted stimulation benefit over time.** The clinical literature on spinal cord stimulation, deep brain stimulation, and vagus nerve stimulation all show the same pattern: initial benefit, then decline over months to years, with partial recovery after reprogramming. The conjecture proposes that this is pattern habituation, but the simpler explanation—that the nervous system adapts to any fixed input, regardless of pattern, and that the adaptation is proportional to the total charge delivered—is not excluded by any evidence the conjecture cites.

---

## 6. COLLATERAL TRAFFIC

The dorsal root ganglion is not a pain structure. It contains the cell bodies of all primary afferents: proprioceptive, tactile, thermoreceptive, nociceptive, and visceral. An intervention that gates C-fibre propagation at the T-junction gates:

- **C-thermoreceptors.** Warm and cold fibres are unmyelinated. Silencing them produces loss of thermal sensation and impaired thermoregulation. The conjecture does not mention this.
- **C-low-threshold mechanoreceptors.** These are the "pleasant touch" fibres, and they are unmyelinated. Silencing them produces loss of affective touch, which is already impaired in many neuropathic pain patients.
- **C-sympathetic efferents.** Postganglionic sympathetic fibres are unmyelinated and pass through the DRG in some species (though not in humans, where sympathetic efferents join the spinal nerve distal to the DRG). In humans, the DRG does not contain sympathetic efferents, but it does contain the cell bodies of visceral afferents, and gating those has consequences for visceral sensation and autonomic reflexes.
- **Aδ fibres.** The conjecture claims Aδ is "intermediate" in its susceptibility. Aδ fibres include cold nociceptors, mechano-nociceptors, and some visceral afferents. Partial gating of Aδ traffic would produce partial loss of sharp pain, cold pain, and visceral pain.

The conjecture's claimed selectivity—C-fibres fail, Aβ fibres pass—is not a clean separation of nociceptive from innocuous traffic. It is a separation of unmyelinated from myelinated traffic, and those are not the same thing. The clinical literature on DRG stimulation does not report loss of thermal sensation or affective touch as a common side effect, which suggests either that the stimulation is not actually gating C-fibre propagation in humans, or that the gating is incomplete and the surviving traffic is sufficient to maintain these functions. Either way, the conjecture's mechanism does not match the clinical observation.

---

## 7. SPECIES AND PREPARATION

The evidence the conjecture relies on is:

- **Rat, anaesthetised, acute.** Chao et al. is a rat preparation, and the recordings are from an acute ganglion preparation. The T-junction filtering mechanism is demonstrated in a preparation where the dorsal root is cut, the ganglion is exposed, and the stimulation is applied directly to the ganglion. This is not the same as a chronically implanted human DRG stimulator, where the electrode is outside the ganglion, the stimulation field is shaped by the dura and the surrounding tissue, and the neurons are in a chronically injured state.
- **Computational model.** Kent et al. is a model, not a measurement. It reproduces the Chao et al. observation, but it does not provide independent evidence for the mechanism.
- **Human clinical data.** The explantation rates the conjecture cites are real, but they are not evidence for the mechanism. They are evidence that the therapy fails in a substantial fraction of patients, which is consistent with many mechanisms, including the rivals the conjecture lists.

The conjecture's proposed test is a rat experiment, and it is a good rat experiment. But the translation from rat to human is not straightforward. The rat DRG is smaller, the stimulation field is more uniform, the T-junction geometry is different, and the chronic injury state is different. A mechanism demonstrated in an acute rat preparation may not survive contact with a chronically implanted human DRG stimulator.

---

## Summary

The conjecture is a well-formed, testable hypothesis about a real and under-exploited feature of sensory neuron physiology. The proposed experiment would genuinely discriminate between the conjecture and its rivals, and the willingness to record the withdrawal of a supporting citation is commendable.

But the conjecture's clinical relevance depends on a series of assumptions that the evidence does not support: that C-fibre traffic is a labelled line for pain, that the T-junction filtering mechanism operates on physiologically relevant traffic in chronically injured humans, that the decline in benefit is pattern habituation rather than charge-dependent accommodation, and that gating C-fibre propagation addresses the pathology of neuropathic pain. The most serious objection is that the discrimination the conjecture proposes to exploit is made centrally, not peripherally, and that in established allodynia the traffic that hurts is arriving on Aβ fibres that the conjecture explicitly spares.

VERDICT: MAJOR — The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease.
