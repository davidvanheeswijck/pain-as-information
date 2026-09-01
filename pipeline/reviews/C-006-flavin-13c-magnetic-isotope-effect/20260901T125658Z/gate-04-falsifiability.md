# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-006-flavin-13c-magnetic-isotope-effect.md`
> 2026-09-01T13:21:30+00:00 · tokens in=9097 out=6471
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

If the conjecture is true, it cannot happen that site-specific ¹³C substitution at flavin C4a leaves the shape or amplitude of the magnetic field effect curve on radical pair yield unchanged relative to natural-abundance flavin measured under identical conditions.

## 2. Audit the author's stated killer

- **Concrete.** Passes. The killer specifies the instrument (transient absorption spectroscopy), the outcome (B½ values), a numerical threshold (difference < 0.2 mT, 95% CI excluding 0.5 mT), and a positive control requirement.
- **Reachable.** Passes. Transient absorption spectroscopy is standard. The estimated cost (40,000–80,000 euro, 9 months) is modest and well within the reach of a physical chemistry laboratory.
- **Honest.** Passes, with a minor caveat. The author explicitly states that a null result closes Branch C, which is a strong commitment. However, the "Rivals" section introduces a dose arm (triple labelling at C4, C4a, C8α) to distinguish "no effect" from "too small to resolve". If the single-label C4a experiment fails the killer threshold but the triple-label succeeds, the author could claim the mechanism is validated while the single-site conjecture was merely misestimated. This is a narrow escape route, but the killer as written applies to the "labelled" preparation, leaving ambiguity about whether a triple-label rescue would prevent refutation.

## 3. Severity

The author estimates a false-pass probability of 0.15. This is credible. The effect is predicted to be large (1.43 mT perturbation against a ~1.89 mT system scale), the outcome is a physical measurement with a pre-registered direction, and the primary confounds (operator bias, photodegradation) are controlled by blinding and randomisation. The mass confound is negligible (0.13%). The main residual risk is that the biosynthetic labelling introduces an uncharacterised structural change that alters radical pair kinetics independently of the hyperfine coupling, but this is unlikely given established labelling chemistry. The false-pass probability is appropriately low.

## 4. The discriminating experiment

The proposed experiment is already a strong inference design. The live alternatives are:
1. ¹³C at C4a changes B½ (the conjecture).
2. The effect is real but too small to resolve at a single site.
3. The purified preparation does not sustain the radical pair.
4. The result is an artefact of measurement order.

The experiment distinguishes these by:
- Measuring the unlabelled MFE as a positive control (distinguishes 3 from 1/2).
- Randomising field order and blinding sample identity (distinguishes 4 from 1/2).
- Including a triple-label dose arm (distinguishes 1 from 2).

If the single-label shows a >0.2 mT shift, the conjecture is supported. If it shows no shift but the triple-label does, rival 2 is supported. If neither shows a shift but the positive control works, rival 1/2 is supported over the conjecture. This is a well-structured discriminating experiment.

## 5. Cost and ladder

The cheapest rung is the proposed bench experiment. The in silico prediction (identifying C4a as a high-leverage position) is already published (Pažėra et al., 2023), so the computational rung is complete. The next rung is the in vitro transient absorption measurement at an estimated cost of 40,000–80,000 euro and 9 months. This is the first hard decision point: a null result closes Branch C of the programme. The cost is trivially small relative to the animal studies it would replace.

## 6. Methodological red flags

None of the standard red flags (HARKing, post-hoc subgroup selection, composite endpoints, vague success criteria) are present. The success criterion is numerical and pre-registered. The dose arm is justified a priori by the simulation literature. The design includes blinding and randomisation.

VERDICT: PASS
