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

## What the shipped files show (read from the data files, not simulated)

- **The A-fibre feature lumps Aβ and Aδ.** The A-fibre-inhibition input drives Aβ (rows 0 to 44) and Aδ (rows 45 to 89) together. The shipped weight of Aδ onto the local inhibitory interneuron (SG75, rows 45 to 59) is [0.0] while Aδ drives the WDR neuron directly (rows 60 to 89, weights [6.6667e-05, 0.0016]). Aδ therefore adds WDR spikes and cannot inhibit through SG75; Aβ is the fibre class that inhibits. The pre-registered criterion counted both together, so the criterion cannot isolate Aβ inhibition.
- **The shipped SCS pulses are on the surround fibres, not on Aβ.** In the shipped `Foreman SCS` input the pulses are on fibres 30 to 44 (the surround input to SG76, whose outputs are GABA-A onto the WDR and EX neurons, rows 288 to 290; target cell index [76]), identical on all 15, 25 pulses, first at 16101 ms, median interval 1000 ms (1 Hz). The Aβ fibres in that file carry a background of about 8.9 Hz per fibre. The pre-registered driver instead pulsed Aβ fibres 0 to 14, which excite the WDR directly. This comes from the input file; it was not simulated here.
- **Wind-up weights.** The wind-up control used the `Foreman SCS` weight table, in which the surround outputs (rows 288 to 290) are [0.007315]; the original `WindUp` folder has them at 0 (`PROVENANCE.md`). This does not affect the wind-up pass (the surround fibres are silent in that input) but it is a difference from the original wind-up run.

- **Successor guidance (needs a fresh pre-registration).** Register an Aβ-only versus Aδ-only decomposition of the A-fibre control, an SCS driver on the surround fibres 30 to 44 as the shipped data show, and a drive grid of about 0.5 to 2 Hz per C fibre.

## NO VERDICT

P0 to P3 are **NO VERDICT**. Reasons: G1: the unmodified starting model does not pass the pre-registered control, so nothing else was run beyond the control record above.

Conditional reading, not a verdict: candidate 0 at dt 0.025: A failed (mean 19.40 spikes per cycle with A fibres, 11.30 without). This describes the pre-registered control (its lumping of Aβ and Aδ and its SCS driver, see the section above) against the tolerances fixed in `PREDICTION.md`; it does not show the port or the published model to be wrong.

