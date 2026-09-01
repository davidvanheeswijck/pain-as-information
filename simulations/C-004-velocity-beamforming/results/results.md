# C-004 velocity-beamforming simulation: results

This is a forward-model simulation, not a measurement. It asks a narrow question: given a physically reasonable (documented, not tuned) model of propagating C-fibre and A-beta compound action potentials, sensor geometry, and noise, does velocity-domain matched filtering recover a coherent C-band ridge that time-domain averaging misses?

## What was simulated

- Nerve: straight, 15 cm along x. Sensor array: 8 OPMs over a 10 cm span, standoff 6.5 mm.
- C-fibres: N=1000, conduction velocity 0.4-1.4 m/s (truncated lognormal), jitter sigma 1.0 ms, AP duration 2.0 ms.
- A-beta fibres: N=200, conduction velocity 30-60 m/s (truncated normal), jitter sigma 0.1 ms, AP duration 0.5 ms.
- Source model: travelling current tripole (Ricker wavelet), net current zero, spatial width = velocity x AP duration.
- Sensor noise: 17.7 fT/sqrt(Hz) white, 2000 trials averaged, sample rate 20 kHz.

## Sanity checks

1. **Single fibre, no noise, known velocity (0.8 m/s):** beamformer recovered 0.8050 m/s (0.63% error) -> **PASS**.
2. **Amplitude calibration:** a synchronous A-beta volley carrying Bu et al.'s back-calculated 0.195 uA compound current produced a peak field of 4.524 pT at 6.5 mm (target ~1 pT) -> **PASS**.
3. **A-beta positive control:** time-domain SNR 114.76, velocity-domain SNR 250.37, ridge at 48.31 m/s -> **PASS**. If this had failed, the geometry/filter would be mis-specified and any C-band result below would be uninterpretable.
4. **Null distribution** (100 noise-only repeats of the identical pipeline): C-band peak energy mean 1.871e-25 T^2, 95th percentile 2.290e-25 T^2. Observed C-band peak energy 2.255e-25 T^2 (z=1.71) -> does NOT exceed the null.
5. **Determinism:** identical seed, run twice -> **PASS**.

## Headline numbers

- Time-domain averaging, C-fibre window: peak -192.998 fT, SNR 4.876.
- Velocity-domain matched filtering, C band: ridge at 0.423 m/s, amplitude 474.900 fT, raw SNR 4.242 (vs. theoretical per-sensor noise sigma; NOT corrected for the velocity-sweep multiple-comparisons search -- see check 4 for the corrected, null-distribution-based test), FWHM [0.423, 1.326] m/s.
- A-beta band (positive control): time-domain SNR 114.76, velocity-domain SNR 250.37 (Aβ margin is large enough that the multiple-comparisons correction does not change the conclusion here).
- Noise sweep: the C-band ridge becomes detectable above its own noise-only null distribution near 1.58 fT/sqrt(Hz) sensor noise (all else held fixed).

## Verdict

**C-004's prediction does NOT survive this simulation.** Under the documented model and parameters, the C-band velocity-domain peak does not exceed the noise-only null distribution at a signal-to-noise ratio above 3, even though the A-beta positive control confirms the array geometry and matched filter are correctly specified and working. In this model, C-fibre cross-sectional current amplitude, combined with realistic conduction-velocity dispersion and trial-to-trial jitter, produces a compound signal too small to recover at the assumed sensor noise floor, even after velocity-domain beamforming and full trial averaging. This is a negative result and should be reported as one: it does not mean the analysis method is wrong (the A-beta recovery shows it works), it means the C-fibre magnetic signal, as modelled here, may be too small at this standoff and this sensor noise floor. The noise-sweep result above (if run) states what sensitivity would be needed to change that.

No parameter in this simulation was adjusted after seeing this result; the only calibrated free parameter (overall current scale) was fixed once from Bu et al.'s back-calculated compound current, against the A-beta amplitude check, before the C-fibre band was examined.

## Full run log

```
========================================================================
C-004 velocity-beamforming simulation
n_trials=2000 sensors=8 noise=17.7 fT/rtHz c_fibres=1000 ab_fibres=200 seed=0
========================================================================
[internal] Biot-Savart kernel vs. infinite-wire formula, ratio = 1.000000 (should be ~1.0)
[check 1] single-fibre velocity recovery: true=0.8 m/s, estimated=0.8050 m/s, rel. error=0.63% -> PASS
[calibration] I_ref (A-beta, max diameter) = 1.667 nA, I_ref (C, max diameter) = 26.039 pA (ratio 64.0x, from cross-sectional-area scaling)
[check 2] amplitude calibration: 200 A-beta fibres driven by a total idealised-synchronous compound current of 0.195 uA (Bu et al. PMID 35370794) produce a peak field of 4.524 pT at 6.5 mm (target ~1.0 pT, order-of-magnitude band [0.10, 10.00] pT) -> PASS
[time-domain A] A-beta window 0.42-4.17 ms: peak 4.542 pT, SNR 114.76
[time-domain A] C-fibre window 17.9-312.5 ms: peak -192.998 fT, SNR 4.876
[velocity-domain B] A-beta band ridge: peak at 48.31 m/s, amplitude 28.027 pT, SNR 250.37, FWHM [40.91, 59.47] m/s
[velocity-domain B] C-fibre band ridge: peak at 0.423 m/s, amplitude 474.900 fT, raw SNR 4.242, FWHM [0.423, 1.326] m/s (raw SNR vs. theoretical noise sigma, NOT corrected for the velocity-sweep multiple-comparisons search; check 4's null distribution below is the corrected test and is authoritative for the C-band verdict)
[check 3] A-beta positive control (must be recovered by both methods): time-domain SNR=114.76, velocity-domain SNR=250.37, ridge inside [30.0,60.0] m/s -> PASS
[check 4] null distribution (100 noise-only repeats), C-band peak energy: mean 1.871e-25 T^2, std 2.253e-26 T^2, 95th pct 2.290e-25 T^2; observed C-band peak energy 2.255e-25 T^2 (z=1.71) -> ridge DOES NOT exceed null
[check 5] determinism (identical seed, run twice): PASS
------------------------------------------------------------------------
[validity] Checks 1-3 (velocity recovery, amplitude calibration, A-beta positive control) all passed: YES -- if NO, the model/pipeline itself is not trustworthy and the C-band result below cannot be interpreted either way.
HEADLINE: C-band ridge NOT distinguishable from the null distribution. C-004's prediction DOES NOT SURVIVE this simulation.
------------------------------------------------------------------------
[sweep] noise ASD (fT/rtHz) -> C-band detectability ratio (observed peak / null 95th percentile at that noise level; >=1 is detectable):
        0.50 fT/rtHz -> ratio 2.570
        0.85 fT/rtHz -> ratio 1.399
        1.45 fT/rtHz -> ratio 1.041
        2.46 fT/rtHz -> ratio 0.789
        4.19 fT/rtHz -> ratio 1.114
        7.13 fT/rtHz -> ratio 0.749
       12.12 fT/rtHz -> ratio 1.080
       20.62 fT/rtHz -> ratio 0.667
       35.09 fT/rtHz -> ratio 0.801
       59.69 fT/rtHz -> ratio 0.777
      101.55 fT/rtHz -> ratio 0.778
      172.76 fT/rtHz -> ratio 0.863
      293.90 fT/rtHz -> ratio 1.031
      500.00 fT/rtHz -> ratio 0.907
[sweep] C-band ridge becomes detectable above the null near noise ASD ~= 1.58 fT/rtHz
[sweep] each ratio uses a 40-repeat null distribution at that noise level, so individual points carry Monte-Carlo sampling noise (the crossing near ratio=1 is not a sharp threshold); read the crossing point as order-of-magnitude, not exact
```
