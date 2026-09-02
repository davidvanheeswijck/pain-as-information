# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-02T09:19:50+00:00 · tokens in=11418 out=6388
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

If the conjecture is true, it cannot happen that the probability of a calibrated light touch evoking a nociceptive dorsal horn response is independent of its delay after a C-fibre burst, or that its decay constant falls outside the 1 to 10 second band, or that an equivalent Aβ-burst control reproduces the same delay-dependence.

## 2. Audit the author's stated killer

- **Concrete.** **PASS.** The killer specifies the animal model, optogenetic control, stimulus delays (50–10000 ms), four control conditions, readouts (electrophysiology and behaviour), sample size (n=12), and refutation thresholds (95% CI for τ).
- **Reachable.** **PASS.** The cost (200–300k EUR, 18 months) is within reach for a well-funded lab, though the requirement for both nociceptor and low-threshold-mechanoreceptor optogenetic lines limits where it can be done.
- **Honest.** **MINOR.** The author identifies a residual risk: optogenetic burst delivery itself producing a delay-dependent change in dorsal horn excitability. The obvious rescue is that the optogenetic stimulation confounded the result, requiring a different method to activate C-fibres. This is a plausible escape hatch if the result is negative.

## 3. Severity

**False-pass probability: ~0.2.**

The author's estimate of 0.15 is reasonable but slightly optimistic. The Aβ-burst control is a major improvement and closes the adaptation false-pass route. The pre-registered τ band closes the "any decay counts" route. The main remaining risks are: (1) the optogenetic artefact identified by the author, which could produce a false positive if the opsin kinetics or light delivery create a delay-dependent effect specific to the nociceptor line; (2) multiple comparisons across models, timepoints, and readouts without explicit correction, which inflates the chance of finding a "significant" τ in at least one condition; (3) lack of blinding for the nocifensive behaviour scoring, which is subjective. However, the strict refutation criteria (any Aβ-burst reproduction kills it) keep the false-pass probability low.

## 4. The discriminating experiment

The author has already designed a strong inference experiment. The key discriminator is the Aβ-burst control.

- If delay-dependence is present in the C-burst but not the Aβ-burst, and afferents are normal, and it's present early but not late: supports the coincidence mechanism.
- If delay-dependence is present in both C-burst and Aβ-burst: supports non-specific adaptation or habituation, killing the conjecture.
- If delay-dependence is flat across delays: supports tonic disinhibition, killing the conjecture.
- If afferent responses change across delays: supports peripheral sensitisation, killing the conjecture.
- If delay-dependence is present late but not early: supports tonic disinhibition developing over time, killing the coincidence-specific claim.

The only improvement would be to replace optogenetic burst delivery with closed-loop triggering of touch based on natural C-fibre spikes, which would eliminate the optogenetic artefact risk entirely. But this is technically much harder and the current design is a good compromise.

## 5. Cost and ladder

The cheapest rung is not the full 200–300k EUR study. The first hard decision point is whether the Aβ-burst control reproduces the delay-dependence. This can be tested in an anaesthetised electrophysiology cohort alone, without the behaviour cohort and without the naive-animal control.

- **Rung 1:** In vivo electrophysiology in anaesthetised mice (neuropathic and inflammatory models) with the optogenetic lines. Test the delay series and the Aβ-burst control. Cost: ~50–80k EUR, 6–9 months.
- **Rung 2:** If Rung 1 shows a C-burst-specific delay-dependence, add the awake behaving cohort and the naive-animal control. Cost: ~150–200k EUR, 12–18 months.

The first hard decision point is Rung 1. If the Aβ-burst control reproduces the effect, the conjecture is dead and Rung 2 is not needed.

## 6. Methodological red flags

- **No blinding mentioned.** The nocifensive behaviour outcome is subjective and susceptible to experimenter bias. Blinding of the experimenter administering and scoring the behaviour is essential.
- **Multiple outcomes without correction.** The design has multiple readouts (electrophysiology, behaviour), models, and timepoints. The author should pre-register a primary outcome and a correction strategy for multiple comparisons, or specify that the refutation criteria apply to *all* conditions (which would make it very strict).

VERDICT: MINOR — The killer needs blinding for the behavioural outcome and a pre-registered primary outcome to prevent post-hoc selection between electrophysiology and behaviour.
