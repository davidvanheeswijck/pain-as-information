# Gate verdict

> Reviewer: `tensorx/kimi-k3` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab moonshot
> Gate: `01-physical-plausibility.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T00:48:16+00:00 · tokens in=6320 out=13549
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

**Referee report — C-005: information rate of a single human C-nociceptor**

This is a Branch A filing: a classical measurement claim about a classical channel. My audit apparatus is calibrated for Branch C, and most of it finds nothing to bite on here. I say so section by section, because a short section is a finding, not a courtesy. Numbers first; biology after.

## 1. Energy scale

No interaction is proposed. The conjecture asks to *record* an existing signal and to deliver physiological stimuli. The carrier is the action potential, so the relevant estimate is the energy of one spike.

Supplied by me — the conjecture gives none of these numbers: unmyelinated fibre diameter ~1 µm, specific membrane capacitance ~1 µF/cm², giving ~3×10⁻¹⁰ F per cm of axon; voltage swing ~100 mV. Minimum energy to charge the membrane: ½CV² ≈ 1.6×10⁻¹² J per cm per spike; with Hodgkin–Huxley ionic overlap, order 10⁻¹¹ J/cm. Against kT = 4.3×10⁻²¹ J at 310 K, that is **~10⁸–10⁹ kT per spike per centimetre**.

The escape-from-thermal-averaging question that kills Branch C filings does not arise. Nothing here operates below kT; nothing needs a rectifier, a sub-thermal-linewidth resonance, or a protected spin. The stimulus side is equally unremarkable: thermal steps to ~43–48 °C and mechanical forces in the mN–100 mN range (supplied by me; the conjecture says only "mechanical or thermal") are transduced by channel gating at a few kT per event — standard ion-channel biophysics — and read out by a regenerative event eight orders of magnitude above the thermal floor.

## 2. Timescale

No coherence, entanglement, tunnelling, radical pair, spin, or resonance is invoked. The decoherence subsection of my standing audit is vacuous, and I record that explicitly rather than letting it pass silently.

The conjecture's one calculation, checked: H ≈ r·log₂(e/(r·Δt)) at r = 10 Hz, Δt = 5 ms gives r·Δt = 0.05, e/0.05 ≈ 54.4, log₂ ≈ 5.77, **H ≈ 58 bits/s**. The conjecture says "near 58." Correct.

What the conjecture does not state, and I supply: 30 bits/s at 10 Hz is **3 bits per spike**. Primary afferents elsewhere in the literature deliver ~1–3 bits/spike. The prediction is therefore "nociceptors are ordinary or worse," and the ceiling does not force it — at 50 Hz the same formula gives ~172 bits/s. The claim is a biological prediction, not a physics bound. The audit can certify the test, not the outcome.

The mechanism claim, quantified with numbers the conjecture cites but does not state: electrode-to-receptive-field distance ~0.3–0.6 m (supplied) at 0.4–1.4 m/s gives latencies of 0.2–1.5 s; activity-dependent slowing of tens of percent under sustained firing (the phenomenon is Serra et al.; the magnitude is mine) produces arrival-time wander of order **10¹–10² ms — one to two orders of magnitude above the 5 ms window** the conjecture nominates as the informative limit. Internally consistent. Two caveats: the wander is history-dependent and therefore partly decodable in principle, which the jitter-shuffle control handles empirically; and the spinal terminal sits farther along the axon than the electrode, so dispersion at the CNS-relevant site is *greater* than at the recording site — which cuts in the conjecture's favour.

## 3. Field and dose

No applied field. Dose is the stimulus, within established human microneurography and psychophysics practice. Shortfall: **zero orders of magnitude**. No hardware is required that does not exist. This is the only correct entry for this section, and it is the first time in a long run of this programme's filings that I have had occasion to write it.

## 4. Spatial resolution

Target volume: one unmyelinated axon, ~1 µm diameter, inside a nerve fascicle. Electrical recording has no diffraction limit; the selectivity limit is the electrode's extracellular pickup radius, of order tens of µm, with unit identity established by the activity-dependent-slowing fingerprint — the same physical effect the conjecture invokes as its mechanism. Required versus achievable resolution: **zero orders of magnitude gap**; demonstrated for decades. The yield (2–6 fibres per session, per the conjecture's own Troglio citation) is a cost and stamina problem, not a physics one. Twenty units each held for 30 repeats of a 60 s segment is ambitious but precedented.

## 5. Signal to noise

This is a reading conjecture, so here is the estimate. Supplied by me: extracellular C-fibre spike amplitude at an intrafascicular electrode, order 20–200 µV; electrode impedance ~2 MΩ. Johnson noise: √(4kTR) = √(4 × 1.38×10⁻²³ × 310 × 2×10⁶) ≈ 0.19 µV/√Hz, which over a 5 kHz spike bandwidth gives **~13 µV RMS**. Amplifier noise is negligible against this; physiological background is comparable. Single-unit SNR of order 2–15: the demonstrated, difficult, routine regime for this technique. Integration: 30 × 60 s = 1,800 s per unit, ~1.8×10⁴ spikes at 10 Hz — a workable scale for the direct method with standard bias correction.

One conversion the conjecture should have done itself: its lone rival result, Cho et al.'s 79.7% classification of three chemicals, is ~0.65 bits per three-spike event (stimulus entropy 1.585 bits minus confusion entropy ~0.93 bits). At event rates of order one per few seconds, that is **≲1 bit/s from fine-interval structure** — inside the conjecture's own bound. The cited opposition, expressed in bits, is not opposition.

The missing estimate, and the reason this is not a clean PASS: repeated noxious stimulation sensitises or fatigues C-nociceptors on minute timescales. If the stimulus-response function drifts across the 30 repeats, noise entropy is inflated and the information estimate is biased **downward — the direction that falsely confirms this particular conjecture**. The severity section names under-sampling as the false-pass route but never names drift. What must be on the table before the killer runs: the drift time constant of human C-nociceptor responses under the proposed frozen-noise protocol, set against the 1,800 s acquisition, with a pre-committed block-interleaving or detrending rule if the two are comparable.

## Pseudoscience checklist

Nothing triggered. "Information" is Shannon's, with units (bits/s) and a named estimator. Every frequency carries units and refers to discharge rate, not to any characteristic frequency of a tissue or disease. No interaction outside the standard model. The jitter-window sweep — information destroyed versus shuffle window at 1, 5, 20 ms — is a dose-response curve. All load-bearing citations resolve to indexed venues (*J Physiol* ×2, *J Neurosci*, *Nature*, *Nat Neurosci*, *PLOS ONE*, *Front Comput Neurosci*). No dilution logic, no suppressed research.

## Strongest version, per the fairness requirement

The strongest construction: the peripheral spike train is the most robustly classical signal in the body — ~10⁸–10⁹ kT, millisecond duration, metre-scale propagation — and this conjecture proposes only to measure one with a fifty-year-old technique and a twenty-five-year-old estimator, using one arithmetically correct ceiling calculation, a mechanism whose documented magnitude exceeds the proposed informative window by one to two orders of magnitude, a pre-committed refutation threshold with confidence bounds, and a stated severity. The number it seeks has, by the programme's own ledger and my knowledge of the literature, genuinely never been measured. It survives every applicable section of the audit. It is not IMPOSSIBLE — no conservation law or proven bound is engaged. It is not INFEASIBLE — every required capability exists and is routine. It is UNDEMONSTRATED, which is the correct classification for a conjecture and the correct reason to fund the experiment. My prior disposes me against programmes like this one; that prior is not threatened by saying plainly that this filing pays its way, and that the two assumptions I had to supply — the bits-per-spike prior implicit in the 30 bits/s threshold, and the drift budget — are the only arithmetic it left undone.

VERDICT: MINOR — the response-drift (sensitisation/fatigue) time constant of human C-nociceptors under repeated noxious frozen-noise stimulation, set against the 1,800 s per-unit acquisition, with a pre-committed block-interleaving or detrending rule if the two are comparable.
