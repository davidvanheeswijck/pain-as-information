# C-004 sensor-realism follow-up: does the bandwidth premise save it?

**C-004's refutation is OVERTURNED by this analysis: the Research alkali OPM clears both the sensitivity and bandwidth bar for the C-band ridge (detectability ratio 1.07 with no interference), and this survives cardiac, 1/f-drift and mains interference once a 50 Hz notch is applied (ratio 1.04), under the stated, explicitly guessed interference amplitudes (see Part 3).**

**This crossing is marginal, not decisive.** Every ratio above sits within about 25% of 1 -- the threshold itself, not a wide margin either side of it. With 200 null repeats the 95th-percentile estimate that these ratios are divided by still carries several percent of Monte-Carlo noise, and an independent check at a different seed (not written to this file, since it is not the pre-registered run) flipped the with-interference verdict to the opposite side of 1. Read the headline above as 'right on the boundary', in the direction PREDICTION.md itself expected ('marginal, within roughly an order of magnitude of the noise floor either way'), not as a robust result in either direction.

This is a forward-model simulation, not a measurement. It extends `simulate.py`'s default pipeline (see `../results.md`) to ask a narrower follow-up question: was the original 'no sensor is both quiet enough and fast enough' conclusion an artefact of assuming the full 10 kHz bandwidth used elsewhere in the evidence base, when that requirement was derived from myelinated (fast, narrow) compound action potentials rather than the slower, broader C-fibre volley?

## Part 1 -- spectral content of the noiseless compound signal

- **C-fibre population:** 50% of energy below **2.8 Hz**, 90% below **29.7 Hz**, 99% below **106.0 Hz**.
- **A-beta population:** 50% of energy below **373.6 Hz**, 90% below **556.9 Hz**, 99% below **720.5 Hz**.

See `psd.png`.

## Part 2 -- three realistic sensors, full pipeline

| Sensor | Noise ASD (fT/√Hz) | Bandwidth (Hz) | Aβ control | C-band ratio |
|---|---|---|---|---|
| Research alkali OPM | 1 | 350 | PASS | 1.075 |
| Commercial alkali OPM | 10 | 350 | PASS | 0.751 |
| Helium-4 OPM | 43 | 2000 | PASS | 0.726 |

"C-band ratio" is observed C-band beamformer peak energy divided by the 95th percentile of a noise-only null generated through the identical, band-limited pipeline (same definition as the default run's sweep, here with 200 null repeats per row). >= 1 means detectable at that sensor's noise+bandwidth. The A-beta control must pass for a row's C-band result to be interpretable at all.

See `sensor-comparison.png`.

## Part 3 -- interference, on the best-case sensor

Best-case sensor carried forward: **Research alkali OPM**.

- Cardiac interference: **43.4 fT**, from a GUESSED (not measured) attenuation factor of 5.79e-04 applied to a 75 pT torso-MCG midpoint of the stated 50-100 pT range; change `--cardiac-amplitude-fT` to test other assumptions.
- 1/f drift below 10 Hz: **50.0 fT rms**, added after trial averaging.
- Mains: **20.0 fT** at 50 Hz plus two harmonics.

- Detectability ratio with no interference: **1.075**.
- Detectability ratio with interference: **1.029**.
- Detectability ratio with interference and a 50/100/150 Hz notch: **1.036**. No notch is applied at the ~1 Hz cardiac fundamental, since Part 1 shows that frequency overlaps the C-band signal's own dominant content -- notching it would remove signal along with interference.

## Discipline

No calibrated constant from the default run (in particular the overall current scale) was touched here. Every new assumption specific to this follow-up -- the filter type/order, the noise-vs-bandwidth split, the interference amplitudes -- is listed in `simulate.py`'s module docstring as approximations 8-13, with the same explicitness as the original seven. The cardiac amplitude in particular is a stated guess, not a measurement; the headline above should not be read as insensitive to it without rerunning with `--cardiac-amplitude-fT` set to other plausible values.

## Full run log

```
========================================================================
C-004 sensor-realism follow-up
Does the C-band signal fit inside a realistic alkali OPM's bandwidth, and does that survive realistic interference?
========================================================================
[part 1] C-band noiseless compound signal, mid-array sensor: energy below 50%=2.8 Hz, 90%=29.7 Hz, 99%=106.0 Hz
[part 1] A-beta noiseless compound signal, mid-array sensor: energy below 50%=373.6 Hz, 90%=556.9 Hz, 99%=720.5 Hz
[part 2] Research alkali OPM (1 fT/rtHz, 350 Hz bandwidth): A-beta positive control PASS (ridge 47.32 m/s, SNR 2195.64); C-band ridge 1.220 m/s, detectability ratio 1.075 (observed 7.806e-28 T^2 vs. null p95 7.264e-28 T^2, 200 repeats)
[part 2] Commercial alkali OPM (10 fT/rtHz, 350 Hz bandwidth): A-beta positive control PASS (ridge 46.35 m/s, SNR 218.43); C-band ridge 1.298 m/s, detectability ratio 0.751 (observed 5.528e-26 T^2 vs. null p95 7.361e-26 T^2, 200 repeats)
[part 2] Helium-4 OPM (43 fT/rtHz, 2000 Hz bandwidth): A-beta positive control PASS (ridge 49.33 m/s, SNR 102.21); C-band ridge 1.298 m/s, detectability ratio 0.726 (observed 1.001e-24 T^2 vs. null p95 1.379e-24 T^2, 200 repeats)
[part 3] best-case sensor carried forward for interference testing: Research alkali OPM
[part 3] interference assumptions: cardiac 43.4 fT (attenuation 5.79e-04 from a GUESSED, not measured, 75 pT torso MCG midpoint), 1/f drift 50.0 fT rms below 10 Hz (added after trial averaging), mains 20.0 fT at 50 Hz plus two harmonics (all with independent per-trial phase)
[part 3] Research alkali OPM WITHOUT interference: detectability ratio 1.075
[part 3] Research alkali OPM WITH interference: detectability ratio 1.029 (observed 3.895e-25 T^2 vs. null p95 3.787e-25 T^2)
[part 3] Research alkali OPM WITH interference AND a 50/100/150 Hz notch: detectability ratio 1.036 (observed 3.972e-25 T^2 vs. null p95 3.836e-25 T^2); no notch is applied at the ~1 Hz cardiac fundamental, since that frequency overlaps the C-band signal's own dominant content (Part 1) and notching it would remove signal along with interference
------------------------------------------------------------------------
HEADLINE: the bandwidth premise is wrong for Research alkali OPM, and this survives realistic interference with a 50 Hz notch applied. C-004's refutation is OVERTURNED under this analysis.
------------------------------------------------------------------------
```
