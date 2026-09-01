# Gate verdict

> Reviewer: `tensorx/deepseek-v4-pro-0424` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab deepseek
> Gate: `07-clinical-translation.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T15:27:22+00:00 · tokens in=7741 out=869
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Translational Review — C-007

## 1. Patient population

**Not applicable as posed.** This is a mechanistic measurement conjecture in healthy volunteers using microneurography. There is no patient population, no disease phenotype, and no enrichment strategy to assess. The "subjects" are healthy human volunteers with identifiable C-nociceptors accessible to microneurography — a technical feasibility population, not a clinical one.

This is not a criticism. The conjecture does not claim to be a treatment. It is a foundational measurement question about whether single-fibre temporal structure carries information beyond rate. Asking it in patients first would be methodologically wrong: the stimulus ensemble must be controlled, and disease states would confound the very question being asked.

## 2. Endpoint and the placebo problem

**Not applicable.** The endpoint is information-theoretic (recovered information about a stimulus ensemble, in bits), measured from electrophysiological recordings. It is not self-reported, not subject to placebo or expectation effects, and not subject to regression to the mean in the clinical sense. The measurement is objective in the strongest sense available in neuroscience: a comparison of decoder performance on identical recorded data.

Blinding is irrelevant here — there is no intervention and no subjective outcome. The relevant methodological threats are decoder bias, estimator bias, and ensemble under-sampling, all of which the conjecture addresses explicitly (bias-corrected estimator, shuffled-timing null through identical pipeline, two decoder families, two ensembles of different temporal bandwidth).

## 3. Risk

**Minimal and procedural.** Microneurography in healthy volunteers carries small but real risks: transient paraesthesia during nerve localisation, small risk of nerve irritation, bruising, and rare vasovagal episodes. No implanted device, no ablation, no drug. The risk profile is that of a research procedure, not a therapeutic intervention.

The one risk worth naming in a translational review is **opportunity cost to the programme**: if this conjecture is confirmed, it redirects Branch A away from single-fibre temporal coding. That is a scientific risk, not a patient risk, and the conjecture states it plainly in "What it would change."

## 4. Regulatory path

**Not applicable.** This is not a drug, device, combination, or software as a medical device. It is a human physiology experiment requiring research ethics approval, not regulatory clearance. No EU MDR or FDA classification applies. The cost and timeline stated (€150,000–250,000, 24 months) are research costs, not regulatory costs.

The only regulatory-adjacent consideration is that microneurography in healthy volunteers is an established research procedure with standard ethics committee oversight. No breakthrough designation, no orphan route, no predicate device.

## 5. Comparator

**Not applicable in the clinical sense.** The comparator is not "best available care" but the rate-plus-identity decoder itself — the conjecture is inherently comparative. The "minimum clinically important difference" has no meaning here; the relevant threshold is the pre-specified 20% information gain with confidence interval excluding zero, which is a statistical and scientific threshold, not a clinical one.

This is the correct framing for a measurement claim. The conjecture's severity estimate (0.15 probability of a false favourable result) is honest and the reformulation from C-005 genuinely improves the design: comparing decoders on identical data cancels the ensemble and most estimator bias.

## 6. Deliverability

**Deliverable as science, not as treatment.** The archived-recording reanalysis path is the right first move and could settle the question for a fraction of the cost. The full prospective study is feasible within existing microneurography laboratory capacity — this is not a superconducting-magnet problem. The main deliverability constraint is the scarcity of investigators skilled in human microneurography and the session time required for 20 tracked units across 8 participants.

The conjecture is honest about its own limitation: if confirmed, it tells us single-fibre timing is not the carrier, but it does not tell us whether population-level synchrony is. That is the next question, and the conjecture says so.

---

VERDICT: NOT APPLICABLE — mechanistic conjecture with no translational claim
