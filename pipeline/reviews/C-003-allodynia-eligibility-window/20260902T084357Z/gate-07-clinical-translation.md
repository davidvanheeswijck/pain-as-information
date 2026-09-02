# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `07-clinical-translation.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-02T09:54:24+00:00 · tokens in=11091 out=2613
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Translational Medicine Review — C-003

**Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain**

---

## 1. The patient population

**Phenotype.** The conjecture targets mechanical allodynia — pain evoked by light touch — in the context of established neuropathic or inflammatory pain. The mechanistic claim is specific: touch-evoked pain that depends on the *temporal proximity* of ongoing C-nociceptor discharge to Aβ input, with a decay constant τ in the 1–10 second range.

**Who exactly, in a human trial.** This is where the conjecture first meets reality. The human phenotype that would correspond to the mouse model is not "chronic pain" or even "neuropathic pain" — it is a patient whose mechanical allodynia is *fluctuating on a seconds-to-tens-of-seconds timescale*, and whose touch-evoked pain is modulated by what happened in the preceding seconds. That is not a diagnosis. It is not even a standard clinical observation. Most clinical allodynia is assessed as a static property: brush the skin, ask for a rating. The temporal structure the conjecture predicts — that a touch 1 second after a spontaneous nociceptor burst hurts more than a touch 8 seconds after — is not something any routine clinical assessment captures.

**Enrichment strategy.** There is no validated human biomarker for "ongoing C-fibre discharge" that could be measured at the bedside. Microneurography can record spontaneous C-fibre activity in humans, but it is a research procedure available in perhaps a dozen centres worldwide, requires specialist operators, and is not feasible as a screening tool for a trial of any meaningful size. Quantitative sensory testing (QST) can measure dynamic mechanical allodynia, but it does not measure the *temporal dependence* the conjecture predicts. Without a measurable criterion to select patients whose allodynia is coincidence-dependent, a human trial would enrol a mixture of patients whose allodynia is tonic-disinhibition-driven, coincidence-driven, and peripherally-driven — and the conjecture itself says those are different mechanisms with different responses to intervention.

**This is a major translational gap, not a minor one.** The conjecture is a mouse electrophysiology conjecture. It is not yet a human-trial conjecture. I will assess it as such, but the enrichment problem is the first place this dies on the way to the clinic.

---

## 2. Endpoint and the placebo problem

**What is measured.** In the mouse experiment: dorsal horn projection neuron responses and nocifensive behaviour, with direct afferent recording. These are objective, measurable, and blindable in principle (the experimenter delivering the touch can be blinded to the delay condition; the electrophysiology is read out by machine).

**In a human translation, the endpoint would be self-reported pain.** That is the only endpoint that matters for a pain intervention, and it is subjective. The placebo problem is severe for any intervention that acts on timing of neural activity, because the intervention itself would be an implanted or applied device — the maximum-placebo scenario.

**Sham control.** For an implanted device that delivers patterned stimulation, sham is possible in principle (implant but don't stimulate, or stimulate at a sub-threshold level), but the patient can often feel the stimulation, which unblinds them. For a device that *desynchronises* ongoing nociceptor traffic — the intervention the conjecture suggests — the patient may feel nothing at all, which is both a blessing (sham is easier) and a curse (the patient cannot tell whether the device is working, which affects expectation and adherence).

**Regression to the mean.** If patients are enrolled during a flare of allodynia — which is when they would present — regression to the mean is severe. A trial that enrols patients at their worst and measures them 3 months later will show improvement in the sham arm too, regardless of mechanism.

**The honest statement.** The mouse experiment is blindable and objective. The human translation is not, and the evidential standard achievable is lower: open-label or single-blind, with self-reported endpoints, and all the inflation that entails.

---

## 3. Risk

**Direct harm from the modality.** The conjecture itself is a mechanism, not an intervention. But the intervention it implies — suppressing or desynchronising ongoing C-nociceptor discharge — would be delivered by electrical neuromodulation (DRG stimulation, peripheral nerve stimulation, or spinal cord stimulation) or by pharmacological means. The risks are those of the modality:

- **Implanted device:** surgical risk (infection 2–10%, lead migration 5–15%, revision 10–30% over 5 years, explant 5–20%), plus the specific risk of placing hardware near the DRG or peripheral nerve.
- **Electrical stimulation:** charge injection, tissue heating, off-target neural effects. If the intervention desynchronises nociceptor traffic, it may also desynchronise *other* traffic — including the Aβ touch input that the conjecture says is normal and should be preserved.
- **Pharmacological suppression of C-fibre activity:** if achieved by sodium channel blockade, the risk is loss of protective sensation, numbness, and in the worst case a Charcot-like joint if the patient loses the protective pain that prevents overuse injury.

**Loss of function.** The conjecture's own logic says that touch is normal and should be preserved. An intervention that suppresses C-fibre activity broadly would also suppress the *protective* nociception that warns of tissue damage. In a patient with established neuropathic pain, the baseline protective sensation may already be compromised; further suppression is a live risk.

**Making the disease worse.** This is the risk that matters most and is most often omitted. Intervening on a limb with central sensitisation can spread or worsen the condition. The literature on operating on affected limbs in CRPS is a warning: surgical intervention on the affected limb can trigger spread, worsening, or new symptoms. An implanted device in the affected limb or its innervation carries the same risk. The conjecture's own mechanism — that ongoing C-fibre activity opens a window for touch to be read as pain — implies that *increasing* C-fibre activity (e.g., by the surgical trauma of implantation) could *worsen* allodynia in the short term. That is a real, mechanism-predicted risk, not a formality.

**Opportunity cost.** For a patient with established neuropathic pain and mechanical allodynia, the established options are: pharmacological (gabapentinoids, SNRIs, tricyclics, topical agents), psychological (CBT, ACT), physical therapy, and in selected cases existing neuromodulation (SCS, DRG stimulation). A patient spending a year in a trial of a novel timing-based intervention is not receiving those, or is receiving them in a constrained protocol. The window of treatable disease is not infinite; neuropathic pain becomes more treatment-resistant over time.

---

## 4. Regulatory path

**This is a mechanism, not a product.** There is no device, drug, or software to regulate yet. The regulatory path would depend on the intervention that emerges from the mechanism:

- **If electrical neuromodulation:** a Class III device in the FDA framework (implanted, life-sustaining or life-supporting, or presents potential unreasonable risk of illness or injury), Class III under EU MDR (implantable active device). There are predicate devices (SCS, DRG stimulators), so a 510(k) or De Novo pathway is conceivable if the intervention is a modification of existing hardware with new stimulation patterns. But a *new* stimulation pattern on existing hardware is a software change, which may be a new indication requiring clinical data.
- **If pharmacological:** a new drug or a repurposed existing drug. The regulatory path is standard but long: Phase I (safety), Phase II (dose-finding and proof of concept), Phase III (efficacy). For a drug that acts on C-fibre discharge, the safety bar is high because of the protective sensation concern.
- **If software as a medical device:** if the intervention is a closed-loop algorithm that detects ongoing C-fibre activity and delivers stimulation in response, that is SaMD, Class II or III depending on the risk, and the regulatory path is newer and less settled.

**Realistic first-in-human timeline.** The mouse experiment is 18 months and €200–300k. If it confirms the mechanism, the next step is a human microneurography study to demonstrate that the coincidence phenomenon exists in humans — that is another 2–3 years and €500k–1M, and it requires a centre with microneurography capability. Only then would a device or drug development programme begin. Realistic first-in-human for an intervention: **5–8 years from now, at a cost of €5–20M to reach a first-in-human safety study**, dominated by the need to demonstrate the mechanism in humans first, then develop and validate the intervention, then run the regulatory studies.

**The dominant cost driver is the human mechanism demonstration.** If the coincidence phenomenon cannot be demonstrated in humans — and it may not be, because human neuropathic pain is more heterogeneous and more chronic than the mouse models — then the entire translational path collapses regardless of how good the mouse data are.

---

## 5. Comparator

**The honest comparator is best available current care for mechanical allodynia in neuropathic pain.**

For a patient with established neuropathic pain and mechanical allodynia, the current standard is:

- **Pharmacological:** gabapentinoids (NNT ~7 for 50% pain relief in neuropathic pain), SNRIs (NNT ~6–7), tricyclics (NNT ~3–4), topical lidocaine or capsaicin for localised allodynia.
- **Neuromodulation:** SCS achieves ~50% pain reduction in ~50–60% of selected patients at 12 months; DRG stimulation achieves similar or better in CRPS and focal neuropathic pain.
- **Combined rehabilitation:** graded motor imagery, desensitisation, physical therapy.

**What improvement would be clinically meaningful.** The minimum clinically important difference (MCID) for pain intensity is typically 30% reduction on a 0–10 NRS, or 2 points. For a novel mechanism to justify its risk and cost, it would need to achieve *at least* that in a population enriched for the coincidence phenotype — and ideally to achieve it in patients who have *failed* existing options, since those are the patients who would be enrolled in an early trial.

**The conjecture's plausible effect size is unknown.** The mouse experiment does not estimate an effect size in humans. It estimates a time constant. Until the human mechanism demonstration is done, there is no basis to estimate whether a timing-based intervention would achieve a clinically meaningful effect. **This is not fatal — it is simply unknown — but it means the translational path is long and the probability of success at each step is multiplicative.**

---

## 6. Deliverability

**Would this be affordable, available, and acceptable?**

- **Affordable:** An implanted neuromodulation device costs €20,000–50,000 for hardware and implantation. A pharmacological intervention would be cheaper. The cost is not the primary barrier.
- **Available:** The intervention would require either a neuromodulation implant (available in most tertiary centres) or a drug (available everywhere). The *screening* to identify patients with the coincidence phenotype is the bottleneck: microneurography is available in perhaps a dozen centres worldwide, and it is not a screening tool.
- **Acceptable:** Patients with neuropathic pain are often desperate for relief and willing to accept significant risk. But an intervention that requires a research-grade microneurography assessment before treatment is not acceptable as a routine clinical pathway.

**What it would take to make this a treatment.** A bedside or clinic-based method to identify patients whose allodynia is coincidence-dependent. That method does not exist. Without it, the intervention cannot be targeted, and an untargeted intervention will show no effect overall because the population is mechanistically heterogeneous — exactly the failure mode described in the prompt.

---

VERDICT: MAJOR — no enrichable human population without a bedside measure of the coincidence phenotype; the human mechanism demonstration is a prerequisite that may not be feasible, and the intervention's effect size in humans is unknown. The mouse experiment is worth doing, but it is a mechanism experiment, not a translational one.
