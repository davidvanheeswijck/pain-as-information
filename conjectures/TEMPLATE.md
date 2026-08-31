---
id: C-000
title: One sentence, asserting something that could be otherwise
branch: A
status: draft
prior: 0.10
posterior:
lineage:
supersedes:
created: YYYY-MM-DD
---

<!--
  branch:  A = classical temporal or spatial structure
           B = quantum technology as instrument
           C = quantum effects in neural tissue
  status:  draft | in-panel | open | wounded | refuted | promoted
  prior:   your probability, before review, that this is substantially correct.
           Written before the panel runs. Do not edit it afterwards; that is
           what posterior is for, and the difference between them is the only
           record of what you learned.
  lineage: the conjecture this was rebuilt from, if any (e.g. C-004)
  Every section below is required. tools/lint-conjecture.py enforces it.
-->

## Claim

One paragraph. What is asserted, in the smallest number of words that still
says something. No hedging verbs. If it needs "may", "could" or "potentially"
to be defensible, it is not yet a conjecture.

## Why this, why now

What in the evidence base points here. Cite by evidence-brief identifier and by
the underlying primary source. If this came from intuition rather than from the
evidence base, say that plainly. Intuition is allowed as a source. Laundering
it through borrowed citations is not.

## Mechanism

How it would work, at the level of detail that lets someone check it. If it
invokes any quantum degree of freedom, coherence, resonance or a frequency, you
supply the energy scale, the timescale and the units here. The physical
plausibility gate will demand them, and supplying them yourself is cheaper than
a round.

## Forbidden observation

What cannot happen if this is true. One sentence, an observation, not a mood.

## Killer

The concrete experiment or observation that would refute it, with:

- the instrument or method,
- the population or preparation,
- the outcome measure and the threshold that counts as refutation,
- the approximate cost and time.

A killer that no existing method could deliver is not a killer.

## Rivals

At least two alternative explanations for the same observations, each stated as
strongly as the claim itself. For each, say what distinguishes it from the
claim observationally. If nothing does, the claim and the rival are the same
conjecture in different words, and this one should be withdrawn.

## Severity

Given this conjecture is false, what is the probability the proposed supporting
test still comes out favourable? Give a number and one line of reasoning. Above
about 0.3 and the test is not evidence.

## What it would change

If true, which experiment, treatment or theory changes. If nothing changes, say
so, and expect to be asked why the programme should spend a round on it.

## References

Every reference with a resolvable identifier: DOI, PMID, PMCID, arXiv id or
NCT number. `tools/verify-citations.py` resolves all of them in CI and a
reference that does not resolve fails the build.
