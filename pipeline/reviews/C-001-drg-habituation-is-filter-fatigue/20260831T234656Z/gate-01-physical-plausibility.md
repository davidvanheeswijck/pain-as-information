# Gate verdict

> Reviewer: `tensorx/kimi-k3` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab moonshot
> Gate: `01-physical-plausibility.md` · Subject: `C-001-drg-habituation-is-filter-fatigue.md`
> 2026-08-31T23:51:14+00:00 · tokens in=5811 out=13564
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

# Referee report — C-001: T-junction filtering decay under chronic DRG stimulation

First conjecture from this programme to reach my desk that invokes nothing quantum. No coherence, no entanglement, no radical pairs, no spin. The audit is therefore shortest exactly where it is usually fatal. Numbers first. Biology at the end, if the numbers earn it.

Assumptions I had to supply because the conjecture did not state them: clinical DRG pulse parameters (~1 mA, 250–300 µs biphasic, contact area ~0.12 cm²), tissue resistivity (~3–5 Ω·m), Nav steady-state inactivation slope (~6 mV per e-fold), DRG dimensions (~5 × 3.5 mm), teased-fibre signal amplitudes. The conjecture gave me frequency, threshold multiples, and the 5 mV offset, which is more than most, but a dose claim should state its own charge.

## 1. Energy scale

kT at 310 K = 4.28e-21 J = 26.7 meV (given).

The mechanism's control variable is a somatic hyperpolarising offset of ~5 mV. Per elementary charge: e·ΔV = 1.6e-19 × 5e-3 = 8.0e-22 J ≈ **0.19 kT**. Sub-kT. Flagged, per the standing rule.

The required escape from thermal averaging exists and is ordinary:

- **Rectification.** The offset acts on Nav voltage sensors. Measured steady-state inactivation slope is ~6 mV per e-fold (apparent gating charge ~4–5 e₀), so 5 mV shifts channel availability by e^(5/6) ≈ **2.3×**. Per sensor the bias is ~1 kT, not 0.19 kT, and it acts on a threshold device held near a propagation saddle-node by construction.
- **Population averaging.** DRG soma ~30 µm diameter, ~2.8e3 µm² of membrane, ~10–100 Nav channels/µm² → N ~ 3e4–3e5. Fractional channel noise ~1/√N ≤ 0.6%, equivalent to tens of µV against a 5 mV signal. Margin ~2 orders of magnitude.
- **The decision variable is macroscopic.** Capacitive energy of one spike over ~100 µm² of membrane: ½CV²·A = 0.5 × 1e-2 F/m² × (0.1 V)² × 1e-10 m² ≈ 5e-14 J ≈ **1e7 kT**. Spike failure at an impedance mismatch is not a thermal-fluctuation event.
- The Ca²⁺/SK link: SK Kd ~0.3–0.6 µM, cooperative 4 Ca²⁺/calmodulin, binding free energies many kT. No sub-kT step anywhere in the chain.

**Passes.** The escape is rectification plus averaging, both standard, neither exotic.

## 2. Timescale

No quantum degree of freedom is invoked, so the decoherence audit is vacuous. I record this explicitly because it is the first time §2 has had no work to do on a conjecture from this programme.

The classical comparison, mechanism speed vs biological need (1e-4 s spike to 1e-1 s percept):

- Spike failure at the T-junction: decided in ~1–2 ms (C-fibre spike width). In band.
- SK activation: tens of ms; decay 0.1–1 s. In band.
- Use-dependent filtering build-up: ~20 s at 20 Hz — *measured* (Chao et al.), not asserted.
- Chronic decay of the enhancement: **no time constant stated anywhere.**

The causal chain spans ~1 ms → 20 s → 28 days: nine orders of magnitude of timescale, of which the first four are measured and the last five rest on an unmeasured constant. The clinical phenomenon runs months to years (Gatzinsky: explant for diminished relief 10% at 3 y, 23% at 10 y). The protocol assumes a rat shows the decay in 28 days — i.e., that rodent homeostatic adaptation runs ~1–1.5 orders of magnitude faster than the human clinical course. Plausible on lifespan scaling; stated nowhere; load-bearing for the protocol. If filtering has not decayed by day 28, the crossover tests nothing. The weekly teased-fibre confirmation detects this failure but does not size the window.

**Passes, with the one missing estimate identified.** This is the estimate the verdict attaches to.

## 3. Field and dose

Supplied parameters (clinical DRG envelope): ~1 mA, 250–300 µs, 20 Hz default, contact ~0.12 cm².

- Charge per pulse ≈ 250–300 nC. Charge density ≈ **2–2.5 µC/cm²/phase**. Shannon (k=2) safe bound at 0.3 µC ≈ 300 µC/cm²; conservative McCreery macro-contact limit ~50 µC/cm². Margin: **1.5–2 orders of magnitude below the tissue-damage threshold.**
- Average charge rate ≈ 5–6 µC/s. Average power at ~1 kΩ lead impedance: I²R × duty = 1e-6 × 1e3 × 5e-3 ≈ **5 µW**. Heating negligible. Within all implant safety limits by orders of magnitude.
- Field at target: point-source estimate J = I/4πr² gives ~80 A/m² at 1 mm, ~9 A/m² at 3 mm; with ρ ≈ 4 Ω·m, E ~ 30–300 V/m within millimetres of the contact, order **10–100 V/m across the ganglion** (bipolar geometry reshapes but does not change the order). Myelinated-fibre thresholds at 250 µs are ~5–20 V/m, so operation at the model's required 2.8–5.5× threshold is exactly what these devices deliver. Consistent.
- Penetration depth required: 1–5 mm. The lead sits in the foramen beside the target. Nothing transcutaneous is proposed.
- Existing hardware: this parameter set *is* the approved, implanted DRG stimulator envelope (the ACCURATE device). Pattern variation within 2–50 Hz at fixed charge is a firmware change, not an instrument.

**Shortfall: zero orders of magnitude.** First time I have written that in this role.

## 4. Spatial resolution

- Volume to address: one lumbar DRG ≈ 5 × 3.5 mm ≈ **40–60 mm³**, with the functional targets (T-junctions) distributed through it.
- Field spreading: quasistatic regime, no diffraction limit applies. Bipolar guarding across a 4-contact lead confines the field to roughly the contact spacing, ~6–10 mm. Required coverage ≈ achievable confinement. **Shortfall: zero orders of magnitude.**
- Fibre selectivity is correctly *not* treated as a spatial problem. It is delegated to the anatomical impedance mismatch, which fails small fibres first — pointing the opposite way to kilohertz block, where threshold falls with diameter and large fibres block first (Bhadra et al., correctly cited). This is the right move and the conjecture makes it explicitly.
- Caveat for the record: the ganglion is not usefully somatotopic, so whether "covering the ganglion" filters the *specific* C-fibres maintaining a given patient's pain is an empirical coverage question, not a resolution shortfall.

## 5. Signal to noise

A writing conjecture with a reading test.

- **Primary readout** (teased-fibre C-spike tracking): signals 50–500 µV on hook electrodes against ~5–10 µV noise; SNR 10–50. The outcome is a per-spike binary (propagated/failed), so the budget is binomial, not thermal: 20 s × 20 Hz = 400 spikes per train, SE on a failure proportion ≈ √(p(1−p)/400) ≈ 2.5 percentage points. The 20-point refutation threshold sits at ~8σ. Resolvable with room to spare.
- **Dose control** (ECAP): cited noise floor 2.8 µV against ECAP amplitudes of 10–100 µV; margin ~4–30×.
- **Dominant noise is biological drift over 28 days**, not electronics. The conjecture's own controls — within-animal Aβ, the amplitude arm degrading identically to the pattern arm, blinded recorder — address it. The stated false-pass probability of 0.15 is argued rather than asserted and sits below the programme's 0.3 gate. n=16 in a within-animal crossover with hundreds of spikes per condition is adequately powered against the stated threshold; animal-to-animal variance is the real term and the crossover removes most of it.

**Passes.**

## Pseudoscience checklist

All seven items, checked: no coherence/resonance/entanglement invoked (§2 vacuous); every frequency carries units and is a stimulus parameter, not a claimed tissue resonance (20 Hz, 2–50 Hz, 1–10 kHz); no extra-standard-model physics; dose-response is explicit (2.8–5.5× threshold, >2 Hz, +50% amplitude arm); no suppressed research — the authors *withdrew* their own conflicted citation, which is the opposite of that pattern; venues are *Pain*, *Neuromodulation*, *J Comput Neurosci*, *Nature* — all indexed, none predatory; no homeopathic logic — the claimed effect scales with charge and pattern, and the amplitude arm is a positive control. **No hit.**

## Fairness: the strongest version I can build

The strongest version: an acute, C-fibre-selective, Ca²⁺/SK-mediated enhancement of T-junction filtering is measured in rat and reproduced in a mechanistic model with a stated dose-response; the clinical failure it would explain is large, independently documented, and grew when the conflicted citation was replaced by registry data (the correction strengthened the premise, as the authors concede); the intervention is a firmware change on an approved, implanted device; and the killer is a costed experiment (€180–250k, 18 months) inside the capability of three or four extant laboratories. This version **survives the audit**: §1–§5 pass with zero orders-of-magnitude shortfall anywhere. The honest classification is **UNDEMONSTRATED** — not IMPOSSIBLE (no conservation law or bound is touched), not INFEASIBLE (the hardware exists and is sitting in patients). My prior, formed by PROCO's finding that rate is not the active variable in spinal stimulation once charge and position are controlled, is that pattern is usually dose in disguise. The audit cannot support that prior here, and I say so. The gravest threat to this conjecture is not physics; it is the amplitude arm of its own experiment, which the authors had the discipline to make the more interesting way to die. The one genuine mechanistic soft spot — matched charge means matched mean Ca²⁺ load, so the homeostatic machinery must be sensing higher-order temporal statistics, magnitude unknown — is precisely what the experiment prices. That is what a conjecture is for.

## Biology (now permitted)

Briefly, since the numbers earned it: the rival set is well-posed, each with a distinguishing observation, and the central-compensation rival is correctly identified as the uncomfortable one. The handling of the withdrawn Levy citation is exemplary and should be the template for this programme's ledger. The 28-day window is the weak joint, as flagged in §2.

VERDICT: MINOR — supply the homeostatic decay time constant of T-junction filtering under chronic fixed-pattern stimulation, or pilot evidence that it decays within 28 days in rat; the conjecture assumes rodent decay runs ~1–1.5 orders of magnitude faster than the human clinical course (months–years), and the entire crossover is void if filtering has not decayed by day 28.
