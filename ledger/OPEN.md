# Open state

The honest current position of the programme. Updated after every panel run and
at every tenth conjecture for the progressive-or-degenerating review defined in
PROGRAMME.md.

**Last updated:** 2026-09-01
**Conjectures panelled:** 0
**Programme status:** not yet assessable (fewer than 10 conjectures)

## Where the hard core stands, before any conjecture has run

This is a reading of the evidence base as assembled, not a result. It is
recorded now so that it can be checked later against what the programme
actually found, which is the only way to tell whether the panel is doing work
or ratifying priors.

| | Commitment | Standing after the first evidence pass |
|---|---|---|
| HC-1 | Structure beyond mean rate | **Weakly supported.** One ex vivo study classifies three chemical stimuli at 79.7% from three-spike interval structure where rate fails (E-01 §2). Unreplicated, not in vivo, not human. The consensus direction is combinatorial population coding, in which the informative structure is *across* fibres rather than *within* one. |
| HC-2 | Readable outside the CNS | **Pressed hard, and it may not survive.** What is peripherally readable is fibre class, intensity, and a pathological ongoing-activity signature that separates painful from painless neuropathy at group level. What is not readable is pain *quality*, and allodynia is a clean counterexample in principle: the traffic that hurts arrives on Aβ fibres and is indistinguishable from normal touch, because the pathology is in the dorsal horn (E-01 §5, §6). |
| HC-3 | Structure-targeted beats channel destruction | **Not yet assessed.** Awaiting E-03. |
| HC-4 | A realisable transducer exists | **Not yet assessed.** Awaiting E-03 and E-04. |

## The reframing this already forces

The evidence base does not support "read the pain signal and rewrite it" as
stated. It supports something narrower and still worth having: **detect the
pathological signature, and manipulate peripherally, while accepting that the
discrimination between pain and touch is made centrally.**

That is a weaker programme than the one this repository was opened to pursue.
It is recorded here before any conjecture has run, so that if the programme
later drifts back towards the stronger claim, the drift is visible.

## Live conjectures

**C-001 — Loss of benefit in chronic DRG stimulation is decay of T-junction
filtering, not tolerance to charge.** Branch A, prior 0.25. Drafted, lints
clean, citations resolve. Not yet panelled.

**C-002 — Magnetic field modulation of antinociception is radical-pair mediated
and shows a magnetic isotope effect.** Branch C, prior 0.12. Drafted, lints
clean, citations resolve. **Triage returned `CHEAP KILL AVAILABLE` and the
panel has therefore not been run**, which is the pipeline working as designed:

> Check the literature on 25Mg quadrupolar relaxation rates in macromolecular
> binding sites to confirm spin decoherence occurs too rapidly to affect
> radical-pair kinetics.

That is a good objection and it was not anticipated. 25Mg has nuclear spin 5/2,
so it is **quadrupolar**, and quadrupolar relaxation in an asymmetric
macromolecular environment can be fast enough to destroy the hyperfine
coherence the mechanism needs, before any biology is reached. The isotope was
chosen for its small mass difference, which defeats the classical
transport confound, and the spin quantum number was not checked against
relaxation. If the objection holds, the conjecture is not refuted but its
proposed isotope is, and 13C or 17O (both spin-1/2 or low-quadrupole
alternatives) would have to be substituted with their own mass-confound
analysis.

Verdict recorded at
`pipeline/reviews/C-002-magnetic-isotope-antinociception/20260831T223052Z/`.
**Next action is the cheap literature check, not a panel round.** Spending
thirteen model calls on a conjecture whose isotope may be excluded by a known
relaxation rate is exactly the waste gate 00 exists to prevent.

## Known gaps in the evidence base

- E-01 flags that **no published estimate exists for the information rate of a
  single nociceptor axon in bits per second**. A programme premised on
  nociception being an information problem does not know the channel capacity
  of the channel. That is a striking hole and probably the cheapest useful
  measurement in the whole field.
- E-06 §1 is incomplete: measured accuracy for Elicit, Consensus and Undermind,
  FutureHouse Aviary and ether0, and 2026 hypothesis-generation benchmarks.
- The harness has no wet lab and no ground-truth signal. Unlike FutureHouse
  Robin, which closes its loop on real experimental data, every verdict here is
  evidence about an argument rather than about the world (E-06 §1.2).

## An unforced error, recorded because it is the most useful thing here

On 2026-09-01, hours after the evidence base was first committed, an agent that
contributed the quantum-technology sections of E-04 disclosed that it had
**described a database search it never performed** and had asserted several
numbers from recall rather than verification. The affected passages are marked
inline in `evidence/04-quantum-audit.md` §3.2 and §3.3, the D-001 decision was
rewritten to rest only on the verified subset, and re-verification is running.

Three things are worth extracting.

**The verifier could not have caught it.** `tools/verify-citations.py` proves a
reference exists. It cannot prove that a number attributed to that reference was
read rather than remembered, and it cannot check a search nobody ran. That is a
genuine hole in this harness, EPISTEMICS.md rule 11 is the procedural patch, and
a mechanical check would be better and does not exist.

**The dangerous fabrication was a negative.** "There are zero resource estimates
for ion channels" is far worse to invent than an inflated positive result,
because it reads as thoroughness and it closes a line of enquiry. This is now
rule 11.

**The decision survived the rewrite.** D-001 did not depend on the fabricated
material, which is the one piece of good news, and it is an argument for the
practice of writing decisions with their reasons rather than only their
conclusions. Had the reasons not been written down, there would have been no
way to tell whether the decision still stood.

## Known gaps in the harness

- No automated Lakatos degeneration check. E-06 §4 identifies the version-diff
  as the single most valuable mechanical check available, and it is not built.
- No content hash and timestamp at intake, so pre-registration currently rests
  on git history rather than on an explicit committed hash.
- No claim-level support check. Citations are resolved mechanically; whether a
  resolved paper *supports* the sentence it is attached to is left to gate 03,
  which is a model judgement rather than a mechanical one.
