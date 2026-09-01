# Gate verdict

> Reviewer: `tensorx/kimi-k3` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab moonshot
> Gate: `01-physical-plausibility.md` · Subject: `C-006-flavin-13c-magnetic-isotope-effect.md`
> 2026-09-01T13:17:21+00:00 · tokens in=9180 out=11279
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Referee report: C-006 — ¹³C magnetic isotope effect on a purified flavin radical pair

This is a Branch C filing, so the numbers come first. Unusually, the conjecture brought most of its own. I checked them.

### 1. Energy scale

The conjecture states the interaction energy as ~40 MHz and converts: h·40 MHz = 2.65e-26 J = 1.65e-7 eV, against kT = 26.7 meV at 310 K. Ratio 6.2e-6. **Arithmetic verified.** It explicitly disclaims any Boltzmann-population mechanism and rests the effect on kinetics: spin-selective recombination rectifies a sub-kT interaction into a chemical yield difference. That is two of the three sanctioned escapes from thermal averaging — a rectifying mechanism, and a spin degree of freedom weakly coupled to the lattice. Any future version of this conjecture argued from populations should be refused on sight; this version is not. **Pass.** No assumptions needed from me.

### 2. Timescale

Required: ~1 µs of spin evolution for hyperfine-driven singlet–triplet interconversion to compete with recombination. Thermal decoherence benchmark ħ/kT = 2.5e-14 s. The conjecture calls this a nine-order gap; it is 4e7, i.e. **10^7.6, not 10^9** — correct the text, though the argument is unaffected. The long-lived degree of freedom is named correctly: electron spins on FAD•−/TrpH•+ and the ¹³C nuclear spin (I = ½, no quadrupole — the trap that was wrongly invoked against C-002 is genuinely absent here). Microsecond radical-pair lifetimes in purified cryptochrome are measured, not assumed (Xu et al. 2021 is the existence proof, in vitro, on protein). Assumption I had to supply: the electron T₂ for this specific labelled construct at measurement temperature is borrowed from cryptochrome measurements rather than stated; the mandatory positive control covers it. **Pass.**

### 3. Field and dose

0–20 mT static, swept, at the cuvette. Field scale verified: 40 MHz / (gμ_B) = 1.43 mT, matching the conjecture; B½ of 1.89 mT (solution) and 2.46 mT (cryptochrome) means the sweep reaches ~8× B½ and saturates the curve. Penetration depth is irrelevant (optical sample). Safety: 20 mT static is below MRI fringe field. Hardware exists in every transient-absorption laboratory that does spin chemistry. **Shortfall: zero orders of magnitude. Pass.**

### 4. Spatial resolution

Not applicable as posed, and I say so explicitly rather than letting it pass silently. This is ensemble spectroscopy on a cuvette; the targeting is molecular — one isotope at one atom — which no field gradient could match. The spatial-resolution demand arrives only if a later conjecture tries to move this signature into tissue, and it will be brutal when it does. For C-006: **pass by construction.**

### 5. Signal to noise

Here the conjecture states a threshold but not an amplitude, so I supply the estimate. Magnetic field effects on purified cryptochrome-class FAD–Trp pairs are percent-scale changes in yield over 0–20 mT (Xu et al.; Maeda et al. 2012). The observable is a B½ shift of ≥0.5 mT on a ~2 mT B½ — a 20–25% change in the half-saturation field of a percent-scale curve. With 1e3–1e4 laser shots averaged per field point, ΔA precision of 1e-4–1e-3 OD is routine; B½ per preparation extracts to ≪0.1 mT. Dominant noise is not the detector but inter-preparation variation and photodegradation ordering, both addressed in the design (≥5 preparations, interleaving, randomised field order, blinded operator). Integration: minutes per curve, hours per preparation; 9 months for the full design is consistent. **Pass on feasibility** — but the one number that is genuinely missing is the **simulated B½ shift and yield-change amplitude for a single ¹³C at C4a from the Pažėra/Hore machinery**. The 0.5 mT refutation threshold is currently a round number; it must be anchored to a pre-registered prediction, or the "too small to resolve" rival cannot be cleanly separated from refutation.

### Pseudoscience checklist

No item hit. Every frequency carries units and is a measured hyperfine coupling, not a "characteristic frequency" of a tissue. No non-standard-model interaction. Dose-response is present twice over (field sweep; single- versus triple-site labelling arm). Venues are indexed; *Magnetic Resonance* (Copernicus/AMPERE) is a legitimate EPR journal. No suppressed-research appeal; no dilution logic. The Zadeh-Haghighi reference is listed but never cited in the text — cite it where it bears or remove it.

### Minor errata

(i) "Nine-order gap" → 10^7.6. (ii) My recollection is that uniform ¹³C/¹⁵N isotope substitution in a cryptochrome MFE assay has already appeared (Sheppard et al., *Sci Rep* 2017); verify and distinguish — "never been done" is defensible only for *site-specific* labelling, and the uniform-labelling result, if it exists, constrains the expected single-site effect size. (iii) The Schleicher citation must be shown to deliver ¹³C at C4a specifically, not uniform labelling; the entire effect size hangs on spin density at that one atom, and if the route is chemical synthesis rather than biosynthesis, say so and cost it.

### Strongest version, per the fairness requirement

The strongest construction: a magnetic isotope effect measured on the one radical pair with a validated biological instance, in vitro, with the relevant hyperfine tensor already measured (Martínez et al.), predictive simulations published (Pažėra et al.), labelling chemistry established in principle, a pre-registered direction and threshold, a mandatory positive control, and — the part this programme got right — a null that is interpretable and terminates Branch C for €40–80k instead of €200k of animal work. That version survives every item of the audit. Nothing violates a conservation law or a proven bound, so it is not IMPOSSIBLE. Every required capability — field, sensor, coherence time, labelling, effect size — exists or has a demonstrated route, so it is not INFEASIBLE. It is **UNDEMONSTRATED**: allowed, feasible, simply not yet shown. I have rejected a great many quantum-biology manuscripts, and I note for the record that the difference between this one and those is not the topic but the arithmetic: the numbers were supplied before they were demanded, the thermal objection is answered with the correct escape rather than with adjectives, and the conjecture is designed to be killed cheaply. Against my prior, it passes the gate. The shortfall is not nine orders of magnitude; it is zero, plus one missing simulation output.

VERDICT: MINOR — supply the pre-registered simulated B½ shift and yield-change amplitude for a single ¹³C at C4a (anchoring the 0.5 mT threshold to a prediction), and one paragraph demonstrating that the Schleicher route labels C4a site-specifically rather than uniformly.
