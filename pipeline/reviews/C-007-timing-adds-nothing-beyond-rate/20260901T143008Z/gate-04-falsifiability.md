# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T14:38:51+00:00 · tokens in=7981 out=10540
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

If the conjecture is true, a decoder given spike times at 1 ms resolution cannot recover more information about the stimulus ensemble than one given only rate in 50 ms bins plus unit identity.

That sentence is statable. The conjecture is falsifiable as stated.

## 2. Audit the author's stated killer

**Concrete.** Passes. Instrument is microneurography, outcome is the difference in recovered information between two decoders on the same recordings, threshold is >20% with CI excluding zero, sample is n≥20 units across ≥8 participants with ≥30 repeats per unit. This is an observation, not a mood.

**Reachable.** Passes. Microneurography is practiced in dozens of laboratories. The cost (150–250k EUR, 24 months) is within the range someone would pay. The author correctly identifies the archived-recording reanalysis as a cheaper first rung.

**Honest.** Fails, for two reasons.

*The 20% threshold contradicts the conjecture.* The conjecture forbids any increase. The killer only fires above 20%. A result showing that 1 ms timing adds 12% information is incompatible with the conjecture as stated but does not trigger the killer. The author survives a result that contradicts his own claim. The available rescue is: "twelve per cent is within estimator noise" — plausible, uncheckable after the fact, and exactly the kind of belt-absorption the programme was designed to catch.

*The Rivals' requirements are not in the Killer.* The Rivals section says the design "should include" two ensembles of different temporal bandwidth and "at least two decoder families, including one that does not assume a fixed bin." The Killer section mentions neither. If the killer fires with one ensemble and one decoder, the author can say: "try a wider-bandwidth ensemble" or "try a non-binned decoder." If it does not fire, the author can say the same things in reverse. These rescues are cheap, available, and not foreclosed by the Killer as written.

## 3. Severity

False-pass probability: **~0.25**.

The comparative design is genuinely strong — two decoders on identical data cancels the stimulus ensemble and most estimator bias, as the author argues. Two factors raise the rate above the stated 0.15:

1. **The threshold gap.** If timing carries a modest amount of information (5–15%), the conjecture is false but the killer does not fire. Given the author's own mechanism — jitter grows with discharge rate, degrading timing precisely where it would matter — a modest effect is the most likely form a false conjecture would take. I estimate P(1–20% increase | timing carries any information) ≈ 0.35.

2. **Power.** n=20 units is small for information-theoretic estimation, which is high-variance even with bias correction. A real >20% effect could produce a CI that includes zero. I estimate P(underpowered | real effect >20%) ≈ 0.20.

Combined: roughly 0.25. Below 0.3, so the test is evidence — but weaker than claimed, and the threshold gap accounts for most of the difference.

## 4. The discriminating experiment

Four live alternatives:

1. **Timing adds nothing** (the conjecture)
2. **Timing adds information but only across fibres, not within one** (Rival 2)
3. **Timing adds information but only with high-bandwidth stimuli** (Rival 1)
4. **Timing adds information but requires a non-binned decoder** (Rival 3)

The single experiment: a 2×2×2 design. Two stimulus ensembles (narrow and wide temporal bandwidth) × two decoder families (binned and non-binned, e.g. a point-process GLM) × single-unit vs. simultaneous two-unit recording with cross-fibre synchrony features.

| Outcome | Means |
|---|---|
| Null across all cells | Supports conjecture |
| Single-unit timing significant only with wide ensemble | Rival 1 — ensemble was the limit |
| Single-unit timing significant only with non-binned decoder | Rival 3 — decoder was the limit |
| Single-unit null, two-unit synchrony significant | Rival 2 — population code |
| Single-unit timing significant across all cells | Conjecture refuted |

The critical missing piece is the simultaneous two-unit recording. Without it, alternatives 1 and 2 are observationally equivalent for single-unit data: a null result cannot distinguish "timing carries no information" from "timing carries information but only at the population level." The author acknowledges this in Rivals but does not build the two-unit recording into the Killer. This is the gap that makes the proposed test less discriminating than it appears.

## 5. Cost and ladder

1. **Existing-data reanalysis.** ~5–20k EUR, 3–6 months. Several laboratories hold marked C-fibre recordings with known stimuli. The decoder comparison is computational and runs on whatever is already captured. **First hard decision point:** if timing adds information in archived data, the conjecture is refuted for a fraction of the cost. If null, the question is whether archived stimuli had sufficient temporal bandwidth and repeat counts — if not, new collection is justified.
2. **In silico.** ~1–5k EUR, 1–2 months. Simulate C-nociceptor spike trains with known injected timing structure and test whether the proposed decoders recover it. Calibrates the pipeline and bounds the detectable effect size before touching human data.
3. **Ex vivo / animal.** ~50–100k EUR, 12 months. Nerve-skin preparations with controlled mechanical and thermal stimuli. Allows simultaneous multi-fibre recording that human microneurography rarely achieves.
4. **Human volunteer psychophysics.** The proposed microneurography study. 150–250k EUR, 24 months.

The archived reanalysis is the right first step and is cheap enough to run now. The in silico calibration should precede or run alongside it, because it establishes what effect size the pipeline can detect — which is exactly the number needed to judge whether the 20% threshold is appropriate.

## 6. Methodological red flags

- **Success criterion mismatched to the claim.** The conjecture forbids any increase; the killer permits up to 20%. This is a success criterion loose enough to be met by a result that contradicts the conjecture.
- **Rivals' requirements not pre-registered in the Killer.** The two-ensemble and two-decoder-family requirements are stated as things the design "should include" but are not part of the refutation criteria. This creates a post-hoc rescue channel: the author can invoke them selectively depending on which way the result goes.
- **No pre-registration of decoder implementations.** Decoder design choices (bin size, feature extraction, model class, regularisation) are degrees of freedom that could be tuned after seeing the data. Without a pre-committed decoder specification, the comparison is vulnerable to garden-of-forking-paths analysis even with only two decoder families.

---

VERDICT: MINOR — the killer's 20% threshold permits results that contradict the conjecture as stated, and the two-ensemble, two-decoder, and two-unit requirements that would make the test discriminating are in Rivals, not in the Killer.
