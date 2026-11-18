# Intent: S-2, a dorsal-horn model of touch-evoked pain

Author: the programme owner
Status: accepted 17/11/2026
Area: simulation
Source: Claude Code session, 17/11/2026

## In the owner's words
> "i follow your recommendation" (17/11/2026), in reply to three options after S-1b. The recommendation, given in the same session before work started, was S-2, the dorsal-horn model, because two T-junction runs had ended without a verdict and touch-evoked allodynia had never been modelled separately from background pain.

## Problem
The programme's motivating phenotype has touch-evoked allodynia and a separate
background pain. The evidence base (E-01 §5 and §6) says allodynia is carried on
normal Aβ input and produced by loss of inhibition in the dorsal horn, which no
peripheral decoder can see and which a ganglion-level intervention may not
reach. Nothing in the programme models that, and the independent review of
2026-11-16 ranked it as a main gap.

## Proposed outcome
S-2: a pre-registered dorsal-horn microcircuit model, started from a published
and validated model, that asks:
1. As inhibition collapses (anion reversal shifted upward, the KCC2/BDNF route),
   at what point does touch (Aβ) input start to drive the pain-projection
   output?
2. Can stimulation that recruits Aβ fibres (the reading of clinical-amplitude
   ganglion stimulation in Graham 2019), or reduced C-fibre input (the
   T-junction reading), still reduce touch-evoked output once inhibition has
   collapsed, separately from C-driven ongoing output?
3. What pattern of change over time would distinguish progressive
   disinhibition from habituation or lead drift, as an observation a treating
   team could make?

Because the network's weights are under-constrained, the output is a set of
discriminating hypotheses tested across an ensemble, not a verdict about any
patient.

## Constraints
- Pre-register before any run, including the positive control taken from the
  starting model's own published results, the ensemble rule and a kill condition.
- Record the prior-art search (ModelDB and PubMed queries, verbatim).
- ETHICS.md: no case data; nothing is a stimulation setting or advice.

## Out of scope
- Further T-junction work (a longer S-1b search, the ion-gradient mechanism).
- The private AI-in-pain-research brief stays private.

## Decision log
| Date | Who | Decision | Source |
|---|---|---|---|
| 17/11/2026 | owner | Build S-2 (dorsal-horn model), following the session's recommendation | session |

## Implemented by
- #11 this intent record
- #12 S-2: NO VERDICT, the A-fibre control lumped Aβ with Aδ and the stimulation driver used the wrong input (see ledger/OPEN.md "Simulations")
