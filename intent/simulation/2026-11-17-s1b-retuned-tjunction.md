# Intent: S-1b, a re-tuned T-junction model that blocks progressively

Author: the programme owner
Status: accepted 17/11/2026
Area: simulation
Source: Claude Code session, 17/11/2026 (answer to a choice between three follow-up models; also recorded in the owner's decision ledger)

## In the owner's words
> "yes go ahead" (17/11/2026), then, asked which model: "Re-tuned T-junction (Recommended)" and, asked whether the AI-in-pain-research brief goes public: "Keep private".

## Problem
S-1 (PR #3) returned NO VERDICT: its model reproduced Sundt 2015's following
frequencies but blocked C-type traffic within about half a second at every rate
of 4 Hz and above, so it failed the Chao 2020 progressive-block control. The
run's own diagnosis named the tuning amendment (Ca decay and SK set against
Sundt's 6 Hz following frequency) as the likely cause, untested.

## Proposed outcome
S-1b: the same question as S-1 (does stimulation pattern matter beyond rate at
the T-junction; can the T-junction account retrodict the blinded human
frequency ordering), on a model re-tuned under a new pre-registration so that
it can pass both controls: Sundt's following frequencies *and* a block that
builds over tens of seconds. If no parameter set in the declared search space
passes both, that is itself the result and is reported as such.

## Constraints
- Pre-register before any run, including the tuning search space and the
  criterion for choosing parameters, which may use the controls only, never P1
  or P2 quantities.
- Reuse S-1's corrected recording sites, site-geometry test, scored-probe
  reporting and gated conditional readings.
- ETHICS.md: no case data; nothing is a stimulation setting.

## Out of scope
- The AI-in-pain-research brief stays private, outside this repository.
- The ion-gradient run-down mechanism and the S-2 dorsal-horn model are not
  built now.

## Decision log
| Date | Who | Decision | Source |
|---|---|---|---|
| 17/11/2026 | owner | Build S-1b (re-tuned T-junction); keep the AI brief private | session, decision ledger |

## Implemented by
- #8 this intent record
- #9 S-1b: no tuning met the calibration targets within the pre-registered budget; P1 and P2 not run (see ledger/OPEN.md "Simulations")
