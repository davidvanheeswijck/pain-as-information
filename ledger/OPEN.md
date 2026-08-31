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

*None yet.*

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

## Known gaps in the harness

- No automated Lakatos degeneration check. E-06 §4 identifies the version-diff
  as the single most valuable mechanical check available, and it is not built.
- No content hash and timestamp at intake, so pre-registration currently rests
  on git history rather than on an explicit committed hash.
- No claim-level support check. Citations are resolved mechanically; whether a
  resolved paper *supports* the sentence it is attached to is left to gate 03,
  which is a model judgement rather than a mechanical one.
