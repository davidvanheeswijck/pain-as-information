These results are not stimulation settings.

# S-2 results: dorsal-horn model of touch-evoked pain

**These results are not stimulation settings.**

Pre-registration: `PREDICTION.md` (commit 007f633). Every number below is generated from the per-model files by `aggregate_s002.py`. Shifts are model millivolts; frequencies are those of a synthetic Aβ pulse train in a four-cell model.

## Positive control (candidate 0, the unmodified starting model)

| dt (ms) | W: wind-up (stimuli 1-5 to 16-20) | A: A-fibre inhibition | Drive match | F: SCS frequency effect | Accepted |
|---|---|---|---|---|---|
| 0.025 | 20.60 to 37.20 spikes/stim: pass | with A 19.40, without A 11.30: FAIL | not run | not run | NO |
| 0.0125 | 20.80 to 38.20 spikes/stim: pass | with A 15.80, without A 11.20: FAIL | not run | not run | NO |

The control runs in the order W, A, drive match, F and stops at the first failing feature, so a feature after it reads "not run". Features are defined in `PREDICTION.md`: W needs the mean of stimuli 16 to 20 to be at least 1.5 times that of stimuli 1 to 5 and at least 1 spike more; A needs the mean with A-fibre events to be at most 0.80 of the mean without them (and the latter at least 1 spike per cycle).

## Gates

- G1, candidate 0 passes W, A and F at both dt: FAIL
- G2, 200 accepted within the cap: not reached
- G3, dt-halving convergence: no convergence files
- G4, wiring test passed at the start of the run: pass

## NO VERDICT

P0 to P3 are **NO VERDICT**. Reasons: G1: the unmodified starting model does not pass the pre-registered control in this re-implementation, so nothing else was run beyond the control record above.

Conditional reading, not a verdict: candidate 0 at dt 0.025: A failed (mean 19.40 spikes per cycle with A fibres, 11.30 without). This describes this re-implementation and driver against the tolerances fixed in `PREDICTION.md`; it does not say the published model is wrong.

