# Gate verdict

> Reviewer: `nebius/kimi-k3` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab moonshot
> Gate: `06-hostile-referee.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T02:20:06+00:00 · tokens in=5954 out=20412
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Review of C-005 — "A human C-nociceptor carries under 30 bits per second"

Read on a plane, as instructed. The document is more literate than most of what crosses my desk from this genre, which makes its failures more specific, not fewer.

---

## 1. Desk-reject kills

**None that holds, and I checked.** The author has read the field. Serra et al. 1999 is cited for what it actually showed; Schmidt et al. 1995 is the right lineage; the Cho et al. 2016 characterization (ex vivo, chemical stimuli, one preparation, unreplicated) is accurate and appropriately dismissive. The flat claim —

> "No published estimate exists for the information rate of a nociceptor axon in bits per second"

— is, to my knowledge, true for nociceptors. But it is one fibre class away from embarrassment: Saal, Vijayakumar & Johansson (*J Neurosci* 2009;29:8022–31) did exactly this measurement — single human afferents, microneurography, mutual information — for tactile afferents. The method exists, in the same preparation, one receptor class over. The "conspicuous hole for fifty years" framing survives, but barely, and only because nociception specifically went unmeasured. Confidence a desk-reject sticks: **10%**, and the editor who issued it would be wrong.

---

## 2. Method kills

**MK-1 (lead kill): the decision rule cannot refute the conjecture.**

> "the conjecture is refuted if the point estimate exceeds 30 bits per second with a lower confidence bound above 30"

Every known bias in direct-method information estimation at 30 repeats runs *downward*: limited-repeat bias, word-length truncation, non-stationarity inflating noise entropy. No estimator is named. No bias correction (Panzeri & Treves 1996, *Network* 7:87; Panzeri et al. 2007) is mentioned. No surrogate-data validation. No power analysis — in a conjecture whose entire content is a number. Refutation requires a lower confidence bound to clear 30 bits/s under biases that all push down; confirmation requires only that a downward-biased estimate stay under 30. The stated severity is 0.2; honest severity is 0.4–0.5. Strong et al. 1998 (*Phys Rev Lett* 80:197) used order 10² repeats for a reason. A test that can only confirm is not a test. **Confidence this alone sinks the work as specified: 70%.**

**MK-2: the preparation will not hold still for the estimator.**

> "at least 30 repeats of a 60 second frozen segment per unit"

The direct method assumes stationarity across repeats. Repeated noxious heat produces fatigue and cross-modal sensitization on exactly this timescale (Peng, Ringkamp, Meyer & Campbell, *J Neurosci* 2003;23:4766; LaMotte & Campbell, *J Neurophysiol* 1978;41:509). Drift inflates noise entropy, biasing the estimate down — the confound and the decision rule point the same way, which is why this is one kill with MK-1, not two. The fix is long inter-stimulus intervals; 30 × (60 s + 8 min rest) is a five-hour hold on a single C-unit, at the edge of what microneurography has ever done. Why no design fixes it: the estimator's stationarity demand, the fibre's plasticity, and electrode stability cannot be jointly satisfied at the required repeat count in an awake human. **Confidence: 60%.**

**MK-3: the refutation criterion is set at the wrong timescale by the conjecture's own arithmetic.**

> "jittering within 5 milliseconds destroys more than 30% of the transmitted information"

By the document's own formula, the ceiling at 10 Hz and 20 ms resolution is ≈ 38 bits/s. So "under 30 bits/s" implicitly assumes effective precision no finer than ~20 ms — which makes the 20 ms shuffle the decisive condition, while refutation is tied to the 5 ms shuffle. Information living at 10–20 ms precision passes the stated criterion while the motivating story is wrong. Alone: **30%**. As an addendum to MK-1, damning.

---

## 3. Inference kills

**IK-1 — the mechanism conflates a deterministic recoding with noise.**

> "timing jitter grows with discharge rate"

Jitter is noise. Activity-dependent slowing is a deterministic, history-dependent latency modulation — which is *exactly why it works as a subtype classifier* (Serra et al. 1999, cited in this manuscript; modeled in Tigerholm et al., *J Neurophysiol* 2019). A deterministic, order-preserving, invertible recoding destroys no mutual information (Cover & Thomas, data processing). Only the *stochastic* component of latency at fixed interval history destroys timing information, and that component is unmeasured — and is not measured by this protocol. The conjecture cites as its noise source the most reliable deterministic phenomenon in the C-fibre literature. Confidence this sinks the Mechanism section: **80%**. The measurement claim survives it, which is the only reason this is not the verdict.

**IK-2 — "If confirmed, the programme's HC-1 survives only in its weak form."** A single-axon timing null says nothing about synchrony across fibres, which HC-1 explicitly includes. And n=20, CMH-dominated, one or two stimulus classes, healthy volunteers, acute stimuli — generalized to "a human C-nociceptor" across modalities and states, in a programme whose disease target is chronic and neuropathic. The mouse-to-man move is absent (credit where due); the acute-to-chronic move is present.

**IK-3 — "If refuted, HC-1 is confirmed in its strong form."** Information about the *stimulus* in the axon is not information *read by the cord*. Available-information versus used-information is the oldest conflation in this literature (deCharms & Zador, *Annu Rev Neurosci* 2000;23:613). Refutation would show the structure exists; it would not show perception uses it.

**IK-4 — bears_on: HC-2.** A single-fibre microneurography estimate does not test whether structure survives at the nerve trunk at realisable sensor SNR. That is a population, geometry and noise question. The claimed bearing is borrowed from work not proposed here.

---

## 4. Priority kills

No clinical decision changes. The decision that changes is internal to the programme (Branch B transducer specifications). The strong-form rival this experiment discriminates against has, by the document's own account, one unreplicated ex vivo study behind it; the rival the field actually holds — population and identity coding, listed here as rival 3 — is explicitly deferred to a "multi-unit follow-up." You do not need €250,000 and two years to decline to believe one unreplicated study. The Saal et al. 2009 contrast is instructive: single-afferent information was measured in touch because there was reason to think single afferents matter there. The nociceptor gap is a judgment, not an oversight. **Confidence this alone sinks: 25%.** It caps impact; it does not kill.

---

## 5. Ridicule kills

**RK-1.** Quote, verbatim, side by side:

> "Human C-fibre subtypes are separable on the wire by activity-dependent slowing"

> "timing jitter grows with discharge rate"

The conference version writes itself: *"The author's noise source is the field's gold-standard classifier. If the slowing were jitter, Serra would have classified nothing."* **45% this follows the work permanently.**

**RK-2.**

> "the transmitted rate will sit well below the ceiling because real spike trains are not maximum entropy. Under 30 bits per second is the prediction."

"Well below" is the entire quantitative derivation. The distance from 58 to 30 is the whole conjecture, asserted in one clause, and the 0.45 prior inherits it. **35%.**

**RK-3.**

> "Reduced substantially if run as a secondary analysis on existing archived recordings, which should be attempted first."

The archive does not contain frozen-noise repeats. That is why the experiment was designed. This sentence tells the room the author has not run the direct method. **40%.**

---

## Counterweight

Yes, there is something here I would be embarrassed to have rejected in ten years: the measurement itself. If someone holds human C-nociceptors through frozen-noise repeats and reports a bias-controlled number with a named estimator, that number gets cited for thirty years whichever side of 30 it lands on — every peripheral-coding argument in pain currently calibrates against tactile afferents and ex vivo rodent preparations, and a human nociceptor datum would anchor them. The design skeleton is the right skeleton and nobody has run it. What would change my mind: a pilot demonstrating response stability across the repeat count or a validated drift-robust estimator; surrogate-data validation that the chosen estimator at the achievable repeat count resolves 30 versus 60 bits/s with symmetric error; and a measurement of the stochastic component of latency at fixed interval history — which would also settle whether the Mechanism section's story is true, since if latency variability at fixed history is large, my recoding argument fails and the slowing story stands. I would rather fund a repaired version of this than half of what I sign. But this version's decision rule is a machine for confirming itself, and I will not sign a machine for confirming itself.

VERDICT: MAJOR — the refutation rule is unreachable as specified: every estimator bias runs toward confirmation, no estimator or power analysis is named, and the preparation's non-stationarity points the same way (70%)
