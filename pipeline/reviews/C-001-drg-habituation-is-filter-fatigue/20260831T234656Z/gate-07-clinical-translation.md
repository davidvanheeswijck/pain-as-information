# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `07-clinical-translation.md` · Subject: `C-001-drg-habituation-is-filter-fatigue.md`
> 2026-09-01T00:26:48+00:00 · tokens in=5474 out=1610
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Translational Assessment — C-001

### 1. Patient population

The conjecture is fundamentally a mechanistic claim about a device-tissue interaction, not a proposal for a new patient-facing intervention. The relevant population is the existing DRG stimulation cohort: patients with chronic neuropathic pain in a focal dermatomal distribution (typically CRPS of the foot/knee, post-surgical neuropathic pain, or mononeuropathy) who have already received an implanted DRG stimulator and are experiencing declining benefit.

The enrichment problem is real but not the primary barrier here. The phenotype — "loss of benefit after initially successful DRG stimulation" — is operationally definable: documented ≥50% pain relief at 3 months post-implant, followed by decline to <30% relief at ≥12 months without lead migration on imaging or impedance change. This is a retrospective-identifiable, prospectively-enrollable subgroup. The measurable criterion is the trajectory of pain scores against a stable device check, not clinical impression.

However, the conjecture as written is an animal-mechanism claim first. It does not propose a human trial. The translational question is whether the mechanistic distinction (filtering decay vs. charge tolerance) can be established in a way that changes clinical practice.

### 2. Endpoint and the placebo problem

The proposed killer experiment is an animal electrophysiology study with a blinded recorder and a within-animal control (Aβ propagation). This is the correct level of evidence for the mechanistic claim, and it is blindable in the sense that matters: the person scoring conduction failure does not know the stimulation condition.

But the translational endpoint — the thing that would matter to a patient — is not C-fibre propagation failure. It is pain relief durability. And here the conjecture inherits the full placebo problem of neuromodulation:

- Pain is self-reported. No objective endpoint exists in routine use.
- The intervention being proposed (pattern variation) is a reprogramming session, which is a high-expectation encounter: the patient returns to clinic, the programmer does something novel, the patient expects improvement. This is the maximum-placebo scenario short of implantation itself.
- Sham control for reprogramming is theoretically possible (the programmer performs an identical session but does not actually change the pattern) but practically difficult: patients can often feel changes in stimulation paresthesia when patterns change, and the programmer cannot be blinded to what they are doing.
- Regression to the mean is severe: patients present for reprogramming when their pain is at its worst, so any intervention will appear to help.

The honest statement is this: the animal experiment can be rigorous, but the human translation of "pattern variation beats amplitude increase" would require a sham-controlled reprogramming trial, and that trial cannot be adequately blinded. The achievable evidential standard is a lower one: an open-label crossover with objective activity monitoring and a pre-registered responder threshold, accepting that the effect size will be inflated by expectation.

### 3. Risk

The conjecture itself proposes no new device and no new surgical procedure. The intervention — varying stimulation pattern within 2–50 Hz at constant charge — uses existing implanted hardware and existing programming software. The direct risks are therefore minimal:

- No new surgical risk, no infection, no migration risk beyond what the patient already carries from the existing implant.
- No tissue heating or charge injection concern: total charge is held constant.
- The main risk is therapeutic failure: the patient spends 3–6 months trying pattern variation when amplitude increase or explantation would have served them better. In a population with progressive disease, that delay is not trivial but it is also not catastrophic — amplitude increase remains available at any point.

The more serious risk is interpretive. If pattern variation is adopted based on an unblinded or weakly controlled trial, patients will be exposed to an ineffective intervention dressed as innovation, and the 12–23% explantation rate for insufficient relief will not improve. The opportunity cost is real: every reprogramming visit spent on pattern variation is a visit not spent on honest discussion of explantation or alternative therapy.

There is also a subtle risk in the framing. The conjecture says the 12% explantation rate is "partly iatrogenic." If that claim is made publicly before the mechanism is established, it could discourage appropriate explantation and prolong suffering in patients for whom the device has genuinely failed.

### 4. Regulatory path

No new regulatory path is required for the animal experiment. For the human translation:

- The intervention is a change in programming practice for an already-approved device (DRG stimulation systems are FDA-approved and CE-marked). No new device approval is needed.
- A clinical trial of reprogramming strategy would be a post-market study, not a pre-market approval. In the EU, this falls under the clinical investigation provisions of MDR Article 62 only if it is a systematic investigation of safety or performance; a practice-pattern comparison could be conducted as a pragmatic trial under existing approval.
- The realistic first-in-human timeline is short: 12–18 months from animal result to a pilot reprogramming protocol, because the hardware exists and the intervention is a software setting.
- Cost is dominated not by regulatory fees but by trial design: a sham-controlled reprogramming trial with adequate blinding infrastructure would cost €1–3 million. An open-label crossover would cost €300,000–500,000. The difference is the cost of honesty.

### 5. Comparator

The honest comparator is current practice: when a DRG patient reports declining benefit, the programmer increases amplitude (or pulse width, or frequency) within the same fixed pattern. This is what the conjecture calls "turning it up."

What does current practice achieve? The explantation data tell the story: 10–23% of patients are explanted specifically for diminished pain relief over 3–10 years, and only 50% are still using the device at 5–7 years. Current practice is not working well for this subgroup.

What improvement would be clinically meaningful? For a reprogramming intervention in a patient already implanted, the minimum clinically important difference on a 0–10 NRS is approximately 2 points or 30% reduction sustained for 3 months. The conjecture's plausible effect size is unknown — it has not been tested in humans — but the animal mechanism suggests a restoration of the original filtering effect, which in the original ACCURATE trial corresponded to roughly 2.5–3 points of pain relief. If pattern variation could recapture even half of that in the declining subgroup, it would clear the MCID bar.

The fatal scenario is not that the effect is below MCID. It is that the effect cannot be measured without the placebo problem inflating it past MCID in an unblinded trial.

### 6. Deliverability

This is the conjecture's strongest translational feature. Pattern variation requires:

- No new hardware. Existing DRG stimulators already support multiple programs and frequency ranges.
- No new surgical procedure. Reprogramming is a clinic visit.
- No new infrastructure. Any centre that implants DRG stimulators can deliver this.
- No new cost. The intervention is a software setting change.

If the animal experiment confirms the mechanism, the human translation is immediately deliverable in any of the hundreds of centres worldwide that already manage DRG implants. The barrier is not deliverability but evidence quality: can the claim survive contact with the placebo problem?

---

**VERDICT: MINOR — the translational detail to work out is the human evidence standard: the animal mechanism is testable and blindable, but the clinical claim ("vary pattern, not amplitude") cannot be tested in a fully blinded reprogramming trial, so the programme must pre-commit to an open-label design with objective activity monitoring and a pre-registered responder threshold, and must state plainly that the resulting evidence is a lower grade than the animal result.**
