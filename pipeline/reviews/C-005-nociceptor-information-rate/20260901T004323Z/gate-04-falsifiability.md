# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T00:50:05+00:00 · tokens in=6203 out=4669
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

If the conjecture is true, a human C-nociceptor cannot transmit more than 30 bits per second about a natural stimulus, nor can shuffling its spike times within a 5-millisecond window destroy more than 30% of that transmitted information.

## 2. Audit the author's stated killer

**Concrete.** Pass. The killer specifies the instrument (human microneurography), the sample (n=20 units, 8 participants), the stimulus paradigm (frozen-noise, 30 repeats of 60s), and the exact numerical thresholds for refutation (>30 bits/s lower confidence bound, or >30% information loss under 5ms jitter).

**Reachable.** Pass. Microneurography is an established, if difficult, technique. The estimated cost (150k–250k EUR) and timeline (24 months) are realistic for a focused psychophysics/neurophysiology study. The suggestion to mine existing archives first is practically sound.

**Honest.** Marginal pass. The author pre-commits to the numerical thresholds. However, the "Rivals" section contains an obvious auxiliary rescue: if the measured rate is low, the author can claim the stimulus was not "natural" or "rich" enough, or defer to the rival that the single-axon question is "ill-posed" and low information is "true and irrelevant." The killer forbids the specific observation, but the protective belt allows the programme to survive the result.

## 3. Severity

Given the conjecture is false (i.e., the true transmission rate is >30 bits/s or fine timing is crucial), the probability the proposed test still comes out favourable is **~0.6**.

The author estimates a false-pass probability of 0.2, attributing it to under-sampling. This misses a fatal statistical property of the proposed design. The killer relies on the "direct method" of information estimation on a 60-second continuous frozen-noise segment. A 60-second spike train binned at 5 milliseconds has 12,000 time bins. Estimating the entropy rate of a 12,000-dimensional response distribution from only 30 repeats is mathematically intractable; the sampling bias (the "curse of dimensionality") is astronomical. Standard bias corrections (e.g., Panzeri-Treves, Strong et al.) will either fail entirely or over-subtract massively, systematically crushing the estimated information rate toward zero regardless of the true underlying rate. If the true rate is 50 bits/s, this experiment will almost certainly output a number below 30 bits/s. The test is structurally biased toward a false pass.

## 4. The discriminating experiment

The live alternatives are: (1) fine timing carries substantial information; (2) the rate is far higher than 30 bits/s under natural stimulation; (3) the single-axon rate is low, but population co-firing carries the information.

To distinguish these, abandon the 60-second frozen-noise paradigm, which cannot be sampled sufficiently. Instead, use discrete, brief stimuli (e.g., 1-second mechanical or thermal pulses of varying intensities and textures) repeated 200–500 times per unit. 

- **Outcome A:** Decoding stimulus identity from spike counts (rate) yields >30 bits/s. *Meaning:* Alternative 2 is true; the conjecture is false.
- **Outcome B:** Rate yields <30 bits/s, but adding fine temporal structure (e.g., 5ms bins) to the decoder improves decoding accuracy by >30%. *Meaning:* Alternative 1 is true; the conjecture is false.
- **Outcome C:** Rate yields <30 bits/s, and adding temporal structure does not improve decoding. *Meaning:* The conjecture is true for single axons. (To address Alternative 3, a follow-up measuring multi-unit coherence would be required, but this experiment cleanly settles the single-axon claim).

## 5. Cost and ladder

1.  **In silico (cheapest):** Simulate C-fibre conduction with activity-dependent slowing. Feed it known high-rate spike trains and measure the arrival-time jitter. Cost: ~0 EUR, 1-2 months. *Decision point:* Does jitter actually degrade 5ms timing at 10Hz? If not, the mechanism is wrong.
2.  **Existing-data reanalysis:** Search for archived human microneurography data using repeated discrete stimuli (e.g., standard heat ramps). Apply the discrete decoding approach. Cost: ~5k EUR, 3-6 months. *Decision point:* Can we get a lower-bound estimate of single-axon info rate from existing data?
3.  **Ex vivo / animal:** Record from rodent C-fibres with rich, repeated discrete stimuli. Cost: ~20k EUR, 6 months. *Decision point:* Is the rate >30 bits/s in a mammalian C-fibre under controlled conditions?
4.  **Human volunteer psychophysics:** The author's proposed microneurography study, but redesigned for discrete stimuli. Cost: 150k-250k EUR, 24 months.

## 6. Methodological red flags

- **Success criterion vague enough to be met by any result:** The 60-second frozen-noise design guarantees a low information estimate due to statistical bias, meaning the design itself fulfills the conjecture's success criteria regardless of biology.
- **Arbitrary thresholds:** The 30% jitter-loss threshold and the 5ms window are not derived from psychophysical just-noticeable-differences or downstream CNS integration windows; they are convenient round numbers that could be shifted post-hoc to absorb a result.
- **Subgroup with no prior justification:** Classifying units by activity-dependent slowing allows for post-hoc subgroup analysis ("the low rate was driven by CMi fibres, not polymodal").

VERDICT: MAJOR — the proposed test has false-pass probability ~0.6 and proves nothing, because the direct method of information estimation on a 60-second continuous stimulus with only 30 repeats is statistically biased toward underestimation, guaranteeing a favourable result even if the true rate is high.
