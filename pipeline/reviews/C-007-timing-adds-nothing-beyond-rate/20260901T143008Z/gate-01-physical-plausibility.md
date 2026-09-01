# Gate verdict

> Reviewer: `tensorx/kimi-k3` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab moonshot
> Gate: `01-physical-plausibility.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T14:35:08+00:00 · tokens in=8059 out=9968
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Review of C-007 — arithmetic first

**Assumptions I had to supply because the conjecture did not:** conduction distance 0.3–0.6 m (knee-to-ankle microneurography geometry; the text says only "tens of centimetres"); activity-dependent velocity modulation of 1–5% across a naturalistic spike pattern (from the cited Serra et al.; cited but not quantified); sustained C-nociceptor rates of 1–10 Hz with peaks under 50 Hz; intraneural tungsten electrode impedance 1–5 MΩ at 1 kHz; extracellular C-fibre spike amplitude 20–50 µV.

### 1. Energy scale

Nothing sub-kT is claimed, so the thermal-averaging burden is not triggered. The mechanism is activity-dependent slowing: cumulative sodium-channel inactivation plus pump-driven hyperpolarization shifting conduction velocity. Operating energies: transmembrane ~70 mV gives e·V ≈ 70 meV ≈ 2.6 kT per elementary charge crossing the field; channel gating a few to ~13 kT; Na/K ATPase ~20 kT per cycle. All at or above kT, all dissipative. The claimed quantity is not an energy signal at all but a temporal pattern in macroscopic ionic current. No rectifier, no narrow resonance, no protected spin required. Discharged.

### 2. Timescale

No coherence, entanglement, tunnelling, radical pairs, spin, or resonance is invoked. The decoherence audit is not engaged. The classical timescales are mutually consistent: spike width ~1 ms; latency D/v = 0.4 m / 1 m/s ≈ 400 ms; ADS accumulation 0.1–1 s as stated.

The number that matters is jitter, and it is the conjecture's strong point: δT = T·(δv/v) = 400 ms × (0.01–0.05) ≈ **4–20 ms**, straddling the 5 ms threshold the conjecture sets for itself. The claim is poised at the physically interesting point, not trivially true or false.

One correction the authors should absorb: to the extent ADS is a deterministic function of spike history, it is an *invertible* time-warp — spike order is preserved in a single axon and the decoder possesses the history — so it destroys no information in principle. Only the stochastic residual of velocity fluctuation does, plausibly 0.1–1% of latency, i.e. 0.4–4 ms. That also straddles the threshold, so the empirical question survives the correction, but the mechanism paragraph should say "stochastic jitter," not "the axon destroys its own timing precision as a by-product of conducting at all."

### 3. Field and dose

No applied field. The only doses are mechanical/thermal skin stimulation within standard volunteer psychophysics and conventional surface marking pulses (~0.2 ms, <10 mA — my assumption; unspecified in the text but decades-standard practice). No shortfall to state.

### 4. Spatial resolution

Required: single-fibre isolation in a nerve fascicle. Achieved by intraneural tungsten microelectrode (tip ~1 µm), confirmed by ADS marking and receptive-field mapping. No diffraction, diffusion, or field-spreading limit applies — the sensor is in mechanical contact. Demonstrated yield is 2–6 fibres per session (Troglio et al.), which is why n=20 units costs ≥8 participants and 24 months. Shortfall: **zero orders of magnitude**. The constraint is yield, not physics.

### 5. Signal to noise

This is a reading conjecture, so here is the estimate. Electrode Johnson noise at 310 K, 1 MΩ: √(4kTR) ≈ 130 nV/√Hz, giving ~9 µV RMS over 5 kHz (~13 µV at 2 MΩ). Spike 20–50 µV against ~10 µV RMS gives amplitude SNR ≈ 2–5 — consistent with why C-fibre sorting is hard and why ADS marking exists. Timing noise: σ_t ≈ σ_v/(dV/dt) ≈ 10 µV / (30 µV per 0.3 ms) ≈ **0.1 ms** — one order of magnitude below the 1 ms decoder resolution, two below the biological jitter. The instrument is not the limit. The limit is statistical: at 1–10 Hz, 60 s × 30 repeats yields ~2×10³–2×10⁴ spikes per unit, and the conjecture nowhere shows its estimator can resolve a 20% timing-information increment at that count.

## Pseudoscience checklist

Item by item: no coherence/resonance/entanglement/"quantum information" language; every time and frequency carries units; no non-standard-model interaction; the claim has a mechanism and a quantitative threshold; no suppressed-research appeal; all venues indexed (the one Frontiers paper is flagged by the conjecture itself as single and unreplicated — appropriately non-load-bearing); no dilution logic. **No item hit.** Per the ledger's own warning from the C-005 run, I assert no citation inversion I cannot check, and none is needed.

## Fairness

Strongest version: a pre-registered comparative null, motivated by a jitter estimate that lands exactly on its own threshold, with the ensemble-dependence that killed C-005 engineered out by comparing decoders on identical data, a shuffled-timing null through the identical pipeline, two decoder families, two ensembles of differing bandwidth, a cheap kill via archived recordings before any new collection, and decision value for the hard core in both directions. It survives the audit not because the audit was lenient but because it makes no quantum, field, or dose claim for the audit to bite on; where numbers do apply — jitter, SNR, resolution — they are internally consistent and consistent with the cited physiology. Classification: **UNDEMONSTRATED** — allowed, feasible with existing technique, simply not yet shown. Nothing here is IMPOSSIBLE or INFEASIBLE. My prior is not engaged, and I note for the record that a programme filing this in Branch A with C-002 and C-004 already in the graveyard is spending its belt in the correct order. What is owed before the human study (not before the archived-data reanalysis, which should proceed now) is the detection floor: severity 0.15 is asserted, not derived. If the floor lies above 20%, the refutation threshold is untestable and the conjecture is unfalsifiable at its own killer.

VERDICT: MINOR — the detection floor: smallest timing-information increment detectable at n=20 units × 30 repeats at 1–10 Hz, demonstrated by injection-recovery on surrogate spike trains through the identical pipeline, with the bias-corrected estimator named; the 20% threshold is meaningless until shown to lie above it.
