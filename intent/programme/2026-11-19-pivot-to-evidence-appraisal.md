# Intent: close the original hard core and continue as evidence appraisal

Author: the programme owner
Status: accepted 19/11/2026
Area: programme
Source: Claude Code session, 19/11/2026 (also answered in the owner's decision ledger)

## In the owner's words
> "yes go ahead" (19/11/2026), in reply to four options after the programme review of the same day (pivot; continue as is; narrow the core and keep simulating; close and write up), with the pivot recommended.

> "yes go ahead" (19/11/2026), in reply to the recommendation to register the sham-trial prediction (P-3) first, by an agent that has not read the paper.

> "yes go ahead" (20/11/2026), in reply to the recommendation to register a second attempt on the same unread paper with the repository route declared in advance.

## Problem
The independent review of 2026-11-19 scored the programme as degenerating under
the test in PROGRAMME.md. No prediction since the programme opened has been
novel, testable and then confirmed by evidence not used to construct it. HC-2's
killer is met for touch-evoked pain in the ledger's own words, and that was
never recorded as a decision. Four of five November simulations ended without
an informative verdict.

## Proposed outcome
1. **Close the original hard core, in writing.** Record it as decision D-003 in
   `ledger/DECISIONS.md`: HC-2 has fallen for touch-evoked pain and stands only
   for the detection of ongoing activity; "read the signal and rewrite it" is
   closed as the programme's purpose; what would reverse the decision. Add a
   dated closure note to PROGRAMME.md and bring README.md into line.
2. **New purpose.** Evidence appraisal for three questions, framed as questions
   a treating team faces, at population level:
   - which generator maintains long-standing regional neuropathic pain
     (peripheral lesion, ganglion, central);
   - why the benefit of ganglion stimulation fades;
   - whether touch-evoked allodynia and background pain are separable
     mechanisms.
3. **Simulation only under two conditions:** a published model that first
   reproduces its own results in this repository, and a verdict rule whose
   every outcome is reachable.
4. **Next steps, in order:** an evidence map for the three questions built
   from full texts; then one prediction registered against data not yet read.

## Not to do
A longer S-1b search; the ion-gradient model; an S-2c; the Branch B trade-off
surface or any sensor work; a tenth conjecture filed only to trigger a review.

## Constraints
- ETHICS.md is unchanged: no case data, no medical advice, honest failure is
  the deliverable.
- The refutation ledger, the evidence briefs and the harness are kept.
- The closure is recorded, not hidden: the original hard core stays readable in
  PROGRAMME.md with its closure note.

## Decision log
| Date | Who | Decision | Source |
|---|---|---|---|
| 19/11/2026 | owner | Pivot: close the original hard core with a written record; continue as evidence appraisal for the three questions | session, decision ledger |
| 19/11/2026 | owner | Step 2: register the sham-trial prediction (P-3) first, by an agent that has not read the paper; a different agent reads the source afterwards | session |
| 20/11/2026 | owner | Step 2, attempt 2: register a second attempt on the same unread paper, with the repository route declared in advance; the claim and the scoring rules are unchanged; it is attempt 2 of 2 under the stop rule | session |

## Implemented by
- #20 (this intent)
- #21 (D-003: close the original hard core; restate the programme as evidence appraisal; the closure record): PROGRAMME.md, README.md, ledger/DECISIONS.md, ledger/OPEN.md
- #22 (E-11: evidence map for the three questions, from full texts; step 1 of the next steps): evidence/11-evidence-map.md
- #23 (record E-11 and its stop-rule outcome; correct E-05 from full texts): ledger/OPEN.md, evidence/05-crps.md, PROGRAMME.md
- #24 (P-003 registration; step 2, the registration only, merged before the source is read): predictions/README.md, predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md
- #25, #26 (P-003 result: unscorable, source not obtained, attempt 1 of 2; and its ledger entry): predictions/P-003-sham-pain-against-pre-implant/RESULT.md, predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md (Amendment 1), ledger/OPEN.md
- #27 (P-004 registration: attempt 2 on the same unread paper, repository route declared in advance; the registration only, merged before the source is read): predictions/P-004-sham-pain-against-pre-implant-attempt-2/REGISTRATION.md, predictions/P-004-sham-pain-against-pre-implant-attempt-2/registration_checks.py
- #28, #29 (P-004 result: unscorable, source not obtained, attempt 2 of 2, the stop rule met; and its ledger entry): predictions/P-004-sham-pain-against-pre-implant-attempt-2/RESULT.md, ledger/OPEN.md

The pivot ended at the stop rule (P-004, 2026-11-20). The owner's decision that
followed is D-004 (`intent/programme/2026-11-21-evidence-resource-only.md`).
