# Intent: act on the November 2026 gap review, simulation first

Author: the programme owner
Status: accepted 16/11/2026
Area: simulation, harness
Source: Claude Code session, 16/11/2026 (an independent review of the programme at 798701b by a Fable 5.2 reviewer, then the owner's go)

## In the owner's words
> "can you resume this project and evaluate with fable 5.2 what are the gaps and were could we really make progress by running simulations ourselves" (16/11/2026)

> "is there a way to run this in a visual physics simulation these experiments ? If usefull of course" (16/11/2026)

> "yes go ahead" (16/11/2026), approving: housekeeping fixes, pre-register and build the DRG T-junction rate-versus-pattern simulation, then an interactive visual driven by the same model.

> "S-3, the diagnostic decision model -> yes go ahead and S-1 visual" (17/11/2026)

> "you can try with fable 5.2" (17/11/2026)

## Problem
All nine conjectures are refuted and none is live. Both simulations so far went to
Branch B (magnetic detection of evoked C-fibre volleys), which bears on none of the
clinical questions that motivate the programme: which generator (neuroma, ganglion,
central), why ganglion-stimulation benefit fades, and whether touch-evoked allodynia
and background pain are separable. The HC-3 foothold (T-junction filtering at the
ganglion) is argued from one side of a contested literature. Several derived files
(README status, a 2-seed results file at the canonical C-008 path, a single-seed
"OVERTURNED" path in the C-004 code) disagree with their sources.

## Proposed outcome
1. Housekeeping: README and OPEN.md agree with the ledger; the stale C-008 smoke
   result no longer sits at the canonical path; simulation verdict code refuses to
   declare a result with too few seeds or with a CI spanning its threshold; the
   independent counter-evidence on ganglion stimulation (Graham/Lempka 2019, 2022;
   Gemes 2013; Chao 2021) is in the evidence base.
2. Simulation S-1: a NEURON population model of the ganglion T-junction that asks
   whether stimulation *pattern* matters beyond mean rate, and whether the
   T-junction account can retrodict the blinded human frequency ordering.
   Prediction committed before any run.
3. A browser visual of S-1, driven by the same model and parameters, labelled as an
   illustration. The verdict comes from the ensemble, never from the visual.

## Constraints
- ETHICS.md: no case data in this repository; nothing here is a stimulation setting.
- EPISTEMICS.md: pre-registration before results; absence claims carry verbatim queries.
- Simulation verdicts require an ensemble; INCONCLUSIVE when a CI spans a threshold.

## Decision log
| Date | Who | Decision | Source |
|---|---|---|---|
| 16/11/2026 | owner | Go on housekeeping, S-1 and its visual | session |
| 16/11/2026 | owner | Systematic scan of AI in pain research, kept in a private folder outside this repository until the owner decides | session |
| 17/11/2026 | owner | Build S-3 (generator-discrimination decision model) and the S-1 visual | session |

## Open questions
- After S-1: build the dorsal-horn gate model (S-2) or the generator-discrimination decision model (S-3) next: owner David

## Implemented by
- #1 this intent record
- #2 housekeeping: status counts, seed-ensemble verdict guard, DRG counter-evidence
- #3 S-1 simulation: NO VERDICT, positive control failed (see ledger/OPEN.md "Simulations")
- Outstanding: the S-1 visual (item 3 above) is not built yet
