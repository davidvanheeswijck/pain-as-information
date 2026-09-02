# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `02-biological-plausibility.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-02T09:16:21+00:00 · tokens in=11049 out=3128
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review of C-003: "Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain"

## Where the conjecture is right

The conjecture correctly identifies a genuine and under-exploited feature of the spinal physiology: **wind-up has a rate dependence that brackets a facilitation time constant in the seconds range**, and this is distinct from both paired-pulse facilitation (tens of milliseconds) and classical central sensitisation (minutes to hours). The pre-registration of τ in the 1–10 s band, derived from the 0.5 Hz/0.1 Hz boundary in Chapman, Suzuki & Dickenson (1994) and the 0.66 Hz trigeminal data, is a legitimate and testable prediction. The Aβ-burst control is the right control, and the reverse-order control is the right control for directional specificity. The conjecture also correctly recognises that the tonic-disinhibition account and the coincidence account make opposite predictions about whether allodynia can be interrupted without structural change, and that this is worth testing early. The design's inclusion of direct afferent recording to rule out peripheral sensitisation is methodologically sound and addresses the most likely confound.

Now the objections.

---

## 1. THE WIRE

The conjecture does not propose to *read* pain from a nerve, so it escapes the usual wire objections. It proposes an optogenetic experiment in mouse, where the primary afferents are stimulated directly by channelrhodopsin expression rather than recorded from. That is the right way to do it, and the wire objection does not apply to the design as written.

However, the conjecture's **clinical translation claim** — that an intervention suppressing or desynchronising ongoing nociceptor discharge would close the window — implicitly requires that ongoing C-fibre discharge be measurable and targetable in a human limb or cord. That is where the wire objection returns. The fibres carrying the ongoing discharge are unmyelinated C-fibres, 0.2–1.5 μm diameter, conducting at 0.5–2 m/s, with extracellular action currents in the tens of microvolts at the nerve trunk and sub-picotesla magnetic fields at the skin surface (Wikswo et al., 1980; Wijesinghe, 2012). They are outnumbered by Aβ fibres by roughly an order of magnitude in a mixed nerve, and the Aβ compound action potential is two to three orders of magnitude larger. The programme's own C-004 and C-008 refutations have already established that detecting C-fibre traffic against realistic interference is not currently possible with available sensors. The conjecture's clinical promise therefore rests on a measurement that the programme has already shown it cannot make. This is not fatal to the *experiment* — the experiment uses optogenetics and does not need to read anything — but it is fatal to the *translation* claim, and the conjecture should say so.

**Objection 1:** The clinical translation claim assumes peripheral readout of C-fibre ongoing discharge that the programme's own simulations (C-004, C-008) have refuted as currently feasible.

---

## 2. THE CODE

The conjecture needs a **temporal coincidence code**: the relative timing of two afferent populations determines the postsynaptic outcome. This is not rate coding, not labelled line, not population coding in the usual sense. It is a specific form of **temporal pattern coding** at the level of two convergent inputs.

What is the evidence for temporal coincidence coding in the dorsal horn? The strongest is **wind-up itself**, which is a rate-dependent facilitation requiring repetitive C-fibre input above a threshold frequency (Mendell & Wall, 1965; Woolf, 1983). Wind-up is a temporal phenomenon: the same number of spikes delivered at 0.5 Hz produces facilitation that the same number delivered at 0.1 Hz does not. That is a genuine temporal code, and the conjecture is right to anchor to it.

But the conjecture extends wind-up in a specific direction: it claims that a *burst* of C-fibre activity opens a window during which *subsequent Aβ input* is routed to nociceptive output. Wind-up as classically described is about the *C-fibre-evoked response itself* being facilitated by prior C-fibre input — it is homosynaptic or at least C-fibre-specific. The conjecture requires **heterosynaptic facilitation**: C-fibre activity facilitating the Aβ-evoked response. That is a different claim.

The evidence for heterosynaptic facilitation of Aβ input by C-fibre activity is much thinner. The PKCγ interneuron circuit (Lu et al., 2013; Peirs et al., 2015) shows that Aβ input can reach lamina I output neurons through a polysynaptic route that is normally gated by inhibitory interneurons, and that this gate is opened by disinhibition. But that is the *tonic* account the conjecture is arguing against. The specific claim that C-fibre activity opens a *transient* window for Aβ routing, decaying over seconds, is not established by any of the cited literature. The Ghitani et al. (2025) finding is about ongoing nociceptor activity in inflammation, but it does not test the timing dependence the conjecture proposes.

**Objection 2:** The conjecture needs heterosynaptic, time-decaying facilitation of Aβ input by C-fibre activity. Wind-up is homosynaptic C-fibre facilitation. The heterosynaptic version is not established by the cited evidence, and the conjecture should acknowledge this gap explicitly.

---

## 3. WHERE IS PAIN MADE

The conjecture is refreshingly honest here, and it is the first conjecture in this programme to get this right. It explicitly states that the discrimination is constructed centrally — in the dorsal horn — and that the peripheral inputs are each individually normal. The mechanism is a central gating phenomenon.

But this honesty creates a problem for the programme's hard core. HC-2 states that pain-relevant structure is readable outside the CNS. The conjecture's mechanism is *defined* by a central computation: the coincidence of two peripherally normal inputs. The information that distinguishes "touch" from "pain" in this account does not exist in either afferent population alone; it exists only in their relative timing at the dorsal horn. That means **no peripheral measurement of either population can distinguish the pain state from the non-pain state**, because the relevant variable is the *coincidence*, which is only computed centrally.

This is not a refutation of the conjecture — the conjecture is a central mechanism, and it is right to be one. But it is a direct challenge to HC-2, and the programme should record that this conjecture, if confirmed, would be evidence *against* the hard core rather than for it. The conjecture bears on HC-1 and HC-3, but it bears *against* HC-2.

**Objection 3:** The conjecture's mechanism is centrally constructed by definition. If confirmed, it strengthens the case that the pain-relevant discrimination is *not* peripherally readable, which is the killer condition for HC-2. The programme should record this tension explicitly rather than listing HC-2 as untouched.

---

## 4. THE PATHOLOGY

The conjecture is about **mechanical allodynia in inflammatory and neuropathic models**, and it correctly identifies that the traffic that hurts arrives on Aβ fibres behaving normally. That is the right framing, and it is a significant improvement over C-001, which was killed for treating C-fibre traffic as a labelled line for pain.

But the conjecture does not fully reckon with the following:

**Ectopic spontaneous discharge.** In neuropathic models, ongoing C-fibre activity is not the only source of spontaneous input. Injured axons and DRG neurons generate ectopic discharge that can be rhythmic, bursting, or irregular (Devor, 2009; Liu et al., 2000). The conjecture's optogenetic design controls C-fibre spike count, which is the right way to isolate the timing question. But the clinical translation claim — suppress ongoing nociceptor discharge and the window closes — assumes that the ongoing discharge is the *only* source of the facilitation. In established neuropathic pain, ectopic discharge from injured Aβ fibres, sympathetic-sensory coupling, and central disinhibition all contribute. Suppressing one population's ongoing activity may not close the window if other sources maintain the facilitated state.

**Central disinhibition.** The conjecture acknowledges the tonic-disinhibition account as its main rival, and the design is set up to distinguish them. But the two mechanisms are not mutually exclusive. A collapsed chloride gradient (Coull et al., 2003, 2005) could lower the threshold for the coincidence mechanism to operate, meaning the window exists but is only behaviourally relevant in the disinhibited state. The design's two-timepoint arm partially addresses this, but the interaction between the two mechanisms is not cleanly separable by the proposed experiment.

**Glial involvement.** Microglial BDNF is the mechanism of the chloride collapse (Coull et al., 2005). The conjecture does not address whether the transient facilitation it proposes is glial-dependent or purely synaptic. If it is glial-dependent, the time constant may be much longer than the wind-up bracket suggests, because glial signalling operates on a slower timescale than synaptic facilitation.

**Objection 4:** The conjecture's clinical translation assumes that ongoing C-fibre discharge is the sole maintainer of the facilitated state. In established neuropathic pain, ectopic discharge from multiple sources, central disinhibition, and glial signalling all contribute, and the design does not test whether suppressing one source closes the window.

---

## 5. PLASTICITY AND HABITUATION

The conjecture is an acute experiment, not a chronic intervention, so the habituation objection does not apply to the design as written. However, the clinical translation claim — an intervention that suppresses or desynchronises ongoing nociceptor discharge — would be a chronic intervention, and the programme's own PB-2 and C-001 have already established that fixed interventions lose efficacy over time.

The specific concern here is that **the nervous system adapts to any fixed pattern of suppression**. If an intervention suppresses ongoing C-fibre discharge, the dorsal horn will upregulate its sensitivity to the remaining input, or the ectopic generators will shift frequency, or the disinhibitory mechanisms will strengthen. The conjecture's own logic implies this: if the window is opened by ongoing discharge, and the system is plastic, then removing the discharge will trigger compensatory changes that reopen the window through a different route. The conjecture should acknowledge that its clinical translation is subject to the same habituation problem that killed C-001.

**Objection 5:** The clinical translation claim is a chronic intervention and is subject to the same plasticity and habituation problems that the programme has already documented in C-001 and PB-2. The conjecture does not address this.

---

## 6. COLLATERAL TRAFFIC

The experiment uses optogenetic control of defined populations, so collateral traffic is not a concern for the design. The clinical translation claim — suppressing ongoing nociceptor discharge — would affect C-fibres, which carry not only nociceptive traffic but also thermoregulatory, sudomotor, and vasomotor autonomic traffic, and provide trophic support to the skin. Suppressing C-fibre activity chronically would impair thermoregulation, sweating, and wound healing in the affected limb. This is a known problem with any C-fibre-targeted intervention, and the conjecture does not address it.

**Objection 6:** The clinical translation claim would require chronic suppression of C-fibre activity, which carries autonomic and trophic functions that would be lost. The conjecture does not reckon with this collateral damage.

---

## 7. SPECIES AND PREPARATION

The conjecture is a mouse experiment, and the evidence it cites is:

- **Wind-up rate dependence:** rat, anaesthetised, acute (Chapman et al., 1994); rat, in vitro spinal slice (Ji et al., 2007); rat, anaesthetised, acute (trigeminal, 1999).
- **Tonic disinhibition:** rat, in vitro and in vivo, neuropathic model (Coull et al., 2003, 2005); mouse, optogenetic and genetic dissection (Duan et al., 2014; Lu et al., 2013; Peirs et al., 2015).
- **Ongoing nociceptor activity in inflammation:** mouse, in vivo calcium imaging (Ghitani et al., 2025).

None of this is human, none is awake, and none is chronic in the sense of a decade-old injury. The wind-up time constant is measured in anaesthetised rat spinal cord, where descending inhibition is attenuated by anaesthesia. In awake humans, descending modulation is intact and may alter the facilitation time constant substantially. The conjecture's τ band of 1–10 s is derived from anaesthetised preparations and may not generalise.

The optogenetic design is the right way to test the mechanism in mouse, but the translation to human allodynia — where the ongoing discharge is not under experimental control, the Aβ input is not calibrated, and the dorsal horn has been remodelled by years of injury — is a large leap. The conjecture should state plainly that its τ band is derived from anaesthetised rodent preparations and may not survive contact with awake human physiology.

**Objection 7:** The τ band is derived from anaesthetised rodent preparations. Descending modulation in awake humans may alter the facilitation time constant, and the conjecture does not address this.

---

## Summary

The conjecture is a well-designed experiment that would distinguish a timing-dependent coincidence mechanism from tonic disinhibition. The Aβ-burst control is the right control, the reverse-order control is the right control, and the pre-registered τ band is a genuine improvement over the first version. The conjecture correctly identifies that the pain-relevant discrimination is central, and it correctly anchors to wind-up as the source of the time constant.

But the clinical translation claim is premature. It assumes that ongoing C-fibre discharge is the sole maintainer of the facilitated state, that peripheral readout of that discharge is feasible, that chronic suppression would not trigger compensatory plasticity, and that the anaesthetised rodent time constant generalises to awake humans. The programme's own refutations (C-001, C-004, C-008) have already established that the first two assumptions are false or unproven.

The conjecture is worth running as an experiment. It is not yet a basis for intervention.

VERDICT: MINOR — The experiment is well-designed and worth running, but the clinical translation claim should be removed or explicitly flagged as contingent on peripheral readout of C-fibre discharge (refuted by C-004/C-008), on C-fibre discharge being the sole maintainer of the facilitated state (not tested by the design), and on the anaesthetised rodent τ band generalising to awake humans (not established).
