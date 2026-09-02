# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-009-peripheral-block-abolishes-crps-pain.md`
> 2026-09-02T12:54:02+00:00 · tokens in=11914 out=4246
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

In a patient with long-duration CRPS and a technically confirmed peripheral nerve block, spontaneous pain will not persist at more than half its pre-block intensity while sensory block is demonstrably complete in the painful territory.

## 2. Audit the author's stated killer

- **Concrete.** PASS. It specifies a population (n=20, CRPS >5 yrs), an intervention (US-guided block vs IV infusion), an outcome (11-point NRS at 30 mins), and a threshold (median reduction <50% with 95% CI excluding 80%).
- **Reachable.** PASS. Ultrasound-guided regional blocks and quantitative sensory testing are standard clinical procedures. The cost (60k–120k EUR) and timeline (12 months) are realistic.
- **Honest.** FAIL. The author explicitly builds in an auxiliary rescue. In the Rivals section, he states that if the block only works on patients with discrete focal lesions (diagnostic reallocation), the design "should be read as measuring how much of CRPS it accounts for rather than as refuting it." If the block succeeds only in misdiagnosed patients, the core conjecture—that *established CRPS* is maintained by peripheral input—is false, but the author frames this as a successful measurement of a fraction. The belt absorbs the blow by design.

## 3. Severity

Given the conjecture is false, the probability the proposed test still comes out favourable is **~0.45**.

The dominant route to a false pass is the complete absence of blinding for a subjective, self-reported outcome in a field with high placebo responses. The author acknowledges a block cannot be blinded, but the proposed IV lidocaine control is a weak comparator: it does not reproduce the profound, undeniable sensory loss of a regional block, which maximises expectancy effects. Furthermore, the known 26–33% misdiagnosis rate guarantees a subset of true peripheral nerve injury patients will be enrolled. If these patients experience >80% pain relief, they can easily pull the cohort median above the 50% threshold, generating a "favorable" result for the CRPS intervention even if true CRPS patients experience no relief.

## 4. The discriminating experiment

The live alternative explanations for pain abolition under block are:
1. **Peripheral maintenance:** Removing afferent input removes the central gain's driver.
2. **Expectancy/Non-specific relief:** The dramatic sensory loss triggers descending inhibition or reporting bias independent of the CRPS mechanism.
3. **Diagnostic reallocation:** The patients who respond never had CRPS.

To distinguish these, measure **temporal summation (wind-up)** of second pain during the block. 
- If pain drops but temporal summation remains exaggerated, the block is acting via expectancy or non-specific inhibition (Alternative 2), because the central sensitization machinery is still running.
- If temporal summation normalizes in parallel with pain reduction, peripheral input is actively maintaining the central gain (Conjecture).
- If only a distinct subgroup normalizes, those patients likely have focal nerve lesions (Alternative 3).

## 5. Cost and ladder

1. **Existing-data reanalysis:** Retrospective chart review of CRPS patients who received incidental nerve blocks for surgery or trauma. Cost: ~5,000 EUR, 2 months. Establishes baseline response rates.
2. **Human volunteer psychophysics:** N/A (requires the disease state).
3. **Patient study:** The proposed crossover. First hard decision point is whether the median reduction in the retrospective review exceeds 50%. If it does not, the prospective trial is likely capturing expectancy and should be redesigned with a sham control.

## 6. Methodological red flags

- **Subgroup with no prior justification:** The author pre-emptively defines a subgroup (discrete lesion vs. no lesion) to absorb a null result.
- **Success criterion vague enough to be met by any result:** The explicit framing that the study "measures how much of CRPS it accounts for" means a mixed or negative result is reclassified as a successful quantification, forbidding nothing.
- **No blinding:** In a field where the outcome is a self-reported rating and placebo responses are routinely above 30%.

VERDICT: MAJOR — the proposed test has false-pass probability ~0.45 and proves nothing
