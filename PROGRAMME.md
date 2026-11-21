# The programme

> **Note, 2026-11-21.** The evidence appraisal that followed the closure below
> ended at its stop rule. [D-004](ledger/DECISIONS.md) keeps the repository open
> as an evidence resource only: no further predictions or simulations. See "The
> repository from 2026-11-21" at the end of this file.

> **Closure note, 2026-11-19.** The original hard core below is closed as the
> programme's purpose by [D-003](ledger/DECISIONS.md). The first review found
> the programme degenerating, and HC-2's killer is met for touch-evoked pain.
> The text of the hard core, the belt and the branches is left as it was written,
> so the change stays visible. The standing of each commitment is marked under its
> heading. The programme continues as evidence appraisal: see "The programme from
> 2026-11-19" at the end of this file. [Superseded 2026-11-21: that appraisal
> ended at its stop rule; see the note above and D-004.]

Written as a Lakatosian research programme rather than a hypothesis, because
the interesting failure mode here is not "the idea was wrong" but "the idea was
rescued so many times it stopped forbidding anything".

A programme has a **hard core** that is held immune from refutation by
convention, a **protective belt** of auxiliary hypotheses that absorb the
blows, and a **problemshift** that is either progressive (each rescue predicts
something new that then turns up) or degenerating (each rescue only explains
away the last failure). This file exists so that the difference stays visible.
`ledger/REFUTED.md` is the record of the belt being spent.

## Hard core

Four commitments. Each is stated with the observation that would end it. If a
core commitment falls, the programme is abandoned, not amended.

### HC-1. Nociceptive traffic carries structure beyond mean rate

*Standing, 2026-11-19: weakly supported, not falsified; one unreplicated ex vivo study, and no informative test here (S-1 gave no verdict) (ledger/OPEN.md, E-01 §2). Closed with the core.*

There is information in the *pattern* of nociceptor firing, not only in how
much of it there is: burst structure, inter-spike interval statistics,
synchrony across fibres, or the identity of the recruited population.

**Killer.** A demonstration that perceived pain quality and intensity are
predicted by rate and recruited-fibre-class alone, with pattern adding no
information once those are controlled, across modalities and across
neuropathic and nociceptive states.

### HC-2. That structure is readable outside the CNS

*Standing, 2026-11-19: fallen for touch-evoked pain; stands only for what is peripherally readable: fibre class, intensity and a group-level ongoing-activity signature (D-003, E-01 §6).*

Enough of the structure survives at the axon, the peripheral nerve trunk or the
dorsal root ganglion to be measured by a physically realisable sensor, without
having to record from cortex.

**Killer.** A demonstration that the pain-relevant discrimination is *created*
centrally from peripherally indistinguishable traffic, so that no peripheral
measurement, at any signal-to-noise ratio, could separate a nociceptive from an
innocuous barrage. Note that this is the commitment the evidence currently
presses hardest on, and it may well be the one that dies.

### HC-3. Structure-targeted intervention beats channel destruction

*Standing, 2026-11-19: not shown; the foothold at the ganglion is argued from one side (one independent model reports direct Aβ activation and does not model T-junction silencing; the other finds the route only above clinical amplitudes in one population of model neurons), and spinal frequency specificity is probably dose (E-03 §1 and §3).*

An intervention that acts on the structure can reduce perceived pain while
leaving the channel's other traffic substantially intact, and does so better
than an intervention of equivalent invasiveness that simply attenuates the
channel.

**Killer.** A head-to-head in which a structure-targeted intervention is no
better on the pain-per-unit-collateral-loss frontier than plain graded
conduction block. Also killed if fibre-selectivity turns out to be physically
inverted in a way that cannot be worked around: if every practical field
modality blocks large myelinated fibres before small unmyelinated ones, then
"spare touch, silence nociception" is not available to electrical block and the
belt has to move to a different transducer.

### HC-4. A physically realisable transducer exists

*Standing, 2026-11-19: partly; quantum information manipulation of pain signalling is below 0.1% with no literature, while quantum instrumentation survives as a costed specification (E-04, C-008). Not pursued further (D-003).*

There is at least one mechanism, buildable this century, that can apply the
intervention of HC-3 at the required spatial and temporal resolution in a human
limb or cord.

**Killer.** A resource estimate showing every candidate transducer needs energy,
field gradient, coherence time or channel count beyond physical limits. This is
the commitment the speculative branches attach to, and it is the one where
"not yet buildable" must not be allowed to masquerade as "in principle
possible".

## Protective belt

Auxiliary hypotheses. These are meant to be spent. Each one that fails should
be recorded in the ledger with what it cost.

- PB-1. Existing implanted hardware (DRG and cord stimulators) already records
  usable structure and is throwing it away.
- PB-2. Loss of efficacy over years in implanted stimulation is habituation to
  a *fixed* stimulus, and is therefore addressable by pattern variation rather
  than by more current.
- PB-3. Night-time mechanical allodynia in long-standing CRPS has a distinct
  signature from daytime background pain, and therefore a distinct handle.
- PB-4. Frequency effects in neuromodulation are mechanistic, not dose.
- PB-5. Some fraction of long-standing regional pain labelled central is
  maintained by an identifiable peripheral generator.

## Branches

Three branches, in descending order of defensibility. They are ranked
deliberately and the ranking is part of the design: work flows down the list,
not up it, and a branch may not borrow credibility from the one above it.

### Branch A. Temporal and spatial structure (classical)

*Standing, 2026-11-19: superseded. The sentence below that this is "where the programme expects to actually get somewhere" described the original hard core; Branch A conjectures C-001, C-003, C-005, C-007 and C-009 are all refuted (`ledger/REFUTED.md`). D-003 closes the purpose.*

Frequency, pattern, closed-loop control, selective recruitment. Ordinary
electrophysiology and ordinary signal processing. This is where the programme
expects to actually get somewhere, and it is where the near-term conjectures
should live.

### Branch B. Quantum technology as instrument

*Standing, 2026-11-19: parked. The branch stays as a costed specification (C-008); D-003 puts the Branch B trade-off surface and any sensor work on the not-to-do list.*

Quantum sensing to *read* (NV-centre magnetometry, optically pumped
magnetometers, magnetoneurography) and quantum computation to *design*
(subtype-selective ligands for voltage-gated sodium channels). No claim that
anything quantum happens inside the neuron. Engineering feasibility questions
with real numbers attached, so they can be settled rather than argued.

### Branch C. Quantum effects in neural tissue (speculative)

*Standing, 2026-11-19: not pursued. Both Branch C conjectures (C-002, C-006) are refuted, and D-003 does not carry the branch forward.*

Nuclear spin, radical pairs, coherence in biomolecules, as a substrate for or
a handle on neural signalling. Guarded by `pipeline/gates/01-physical-plausibility.md`,
which demands a quantitative decoherence and thermal-noise estimate before any
biological argument is heard. Two facts govern this branch and are repeated
in the gate so nobody has to remember them: thermal energy at 310 K is about
27 meV, and the published literature connecting quantum effects specifically
to nociception is, as far as this programme has found, empty.

Branch C is not banned. It is expensive, and it has to pay.

## Progressive or degenerating

The programme is reviewed against this test at every tenth conjecture [superseded 2026-11-19: every ten pieces of work, see "The programme from 2026-11-19" below], and the
verdict is written into `ledger/OPEN.md` with a date.

**Progressive** if, since the last review, the belt has produced at least one
prediction that was novel when made, was testable with existing methods, and
was then confirmed by evidence not used to construct it.

**Degenerating** if every belt change since the last review was made only to
accommodate a failure already observed, or if the number of live auxiliary
hypotheses grew while the number of forbidden observations did not.

A programme that is degenerating for two consecutive reviews is closed, and
this file records why. That is the point of writing it down in advance.

## The programme from 2026-11-19

> **Standing, 2026-11-21.** Paused at the stop rule (P-003 and P-004 both
> unscorable) and superseded by [D-004](ledger/DECISIONS.md). The text below is
> kept as written. Its promises of further predictions and of a review every ten
> pieces of work are not being carried out; see "The repository from 2026-11-21".

Decided in [D-003](ledger/DECISIONS.md) (intent:
`intent/programme/2026-11-19-pivot-to-evidence-appraisal.md`). The hard core
above is closed. This section says what the programme is now.

### Purpose

Evidence appraisal, at population level. The programme reads the published
record, says what it supports and what it does not, and registers predictions
that can fail. It does not make claims about any person's care (ETHICS.md §1
and §3). The refutation ledger, the evidence briefs and the harness are kept.

### The three questions

Framed as questions a treating team faces:

1. Which generator maintains long-standing regional neuropathic pain: a
   peripheral lesion, the ganglion, or central amplification?
2. Why does the benefit of ganglion stimulation fade?
3. Are touch-evoked allodynia and background pain separable mechanisms?

### Simulation rule

Simulation happens only on a published model that first reproduces its own
results in this repository, and only with a verdict rule whose every outcome is
reachable. A control that cannot fail, or a rule that cannot return the opposite
verdict, does not count.

### What would count as progress

The test in "Progressive or degenerating" stands as written. Applied here: a
prediction registered against data not yet read, scored afterwards, and
confirmed. An evidence map is useful work, and it is not progress by this test.
The order is fixed: first an evidence map for the three questions, built from
full texts; then one prediction registered against data not yet read, and
scored. A prediction confirmed by computation on the model it was derived from
does not count: the first review found that the hand predictions that came true
were of this kind, or forecast an instrument failure.

Any stop rule or threshold for a piece of work must be written into a file in
this repository before that work starts (the case: the E-11 stop rule, which
was in no repository file before the map was built; see
`evidence/11-evidence-map.md`, "The stop rule", and `ledger/OPEN.md`, E-11).

### Review rule going forward

The review is triggered **every ten pieces of work (conjectures, simulations or
briefs)** since the last review. The owner moved the trigger from every tenth
conjecture on 2026-11-18, so the sentence under "Progressive or degenerating"
that says "every tenth conjecture" is superseded by this one. A second consecutive degenerating
review closes the programme, and this file records why.

### Not to do

A longer S-1b search. The ion-gradient model. An S-2c. The Branch B trade-off
surface, or any sensor work. A tenth conjecture filed only to trigger a review.

## The repository from 2026-11-21

Decided in [D-004](ledger/DECISIONS.md) (intent:
`intent/programme/2026-11-21-evidence-resource-only.md`). The owner's words:
"Keep it open as an evidence resource only."

### What it is now

A public evidence base on chronic neuropathic pain as a signalling problem, with
the record of nine refuted conjectures, the simulations, the closed hard core
above and the method used. The three questions in "The programme from
2026-11-19" are the frame the briefs are read against.

### What is no longer done

No further predictions are registered and no further simulations are run. As a
consequence, and as an interpretation D-004 flags for the owner to confirm, no
further conjectures are filed and no further panels are run. The "Not to do" list
below still holds.

### How the briefs are maintained

A brief is corrected when an error is found, with a dated note, and updated when
a relevant paper appears. The existing rules apply: EPISTEMICS.md, citations
resolved, queries logged, full text where it can be read, and the source-status
tags used in E-11. The refutation ledger and the harness stay as published.
Nothing here is medical advice (ETHICS.md §1, §3).

### The review cycle is suspended (an interpretation, for the owner to confirm)

The owner did not decide this; D-004 reads it from the owner's words. A second
consecutive degenerating review closes the programme. With no predictions or
simulations there is nothing for a progressive-or-degenerating review to assess,
so the review cycle is read as suspended while D-004 stands. The every-ten-pieces
trigger is already at ten, so the suspension is the only thing that prevents a
second review. The first verdict (degenerating, 2026-11-19) stands. If work
resumes under a D-005, the next review counts as the second.

### What would reverse it (drafted, pending confirmation)

Access to full texts by a declared human or institutional route (which resembles
the option the owner did not choose, and is listed as what would be needed, not
as a plan), together with a registered prediction the owner approves; or a
published, validated model that reproduces its own results in this repository
and bears on one of the three questions, as judged by the owner in D-005. Either
needs D-005, written before any such work starts.
