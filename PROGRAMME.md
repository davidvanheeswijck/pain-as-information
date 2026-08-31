# The programme

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

There is information in the *pattern* of nociceptor firing, not only in how
much of it there is: burst structure, inter-spike interval statistics,
synchrony across fibres, or the identity of the recruited population.

**Killer.** A demonstration that perceived pain quality and intensity are
predicted by rate and recruited-fibre-class alone, with pattern adding no
information once those are controlled, across modalities and across
neuropathic and nociceptive states.

### HC-2. That structure is readable outside the CNS

Enough of the structure survives at the axon, the peripheral nerve trunk or the
dorsal root ganglion to be measured by a physically realisable sensor, without
having to record from cortex.

**Killer.** A demonstration that the pain-relevant discrimination is *created*
centrally from peripherally indistinguishable traffic, so that no peripheral
measurement, at any signal-to-noise ratio, could separate a nociceptive from an
innocuous barrage. Note that this is the commitment the evidence currently
presses hardest on, and it may well be the one that dies.

### HC-3. Structure-targeted intervention beats channel destruction

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

Frequency, pattern, closed-loop control, selective recruitment. Ordinary
electrophysiology and ordinary signal processing. This is where the programme
expects to actually get somewhere, and it is where the near-term conjectures
should live.

### Branch B. Quantum technology as instrument

Quantum sensing to *read* (NV-centre magnetometry, optically pumped
magnetometers, magnetoneurography) and quantum computation to *design*
(subtype-selective ligands for voltage-gated sodium channels). No claim that
anything quantum happens inside the neuron. Engineering feasibility questions
with real numbers attached, so they can be settled rather than argued.

### Branch C. Quantum effects in neural tissue (speculative)

Nuclear spin, radical pairs, coherence in biomolecules, as a substrate for or
a handle on neural signalling. Guarded by `pipeline/gates/01-physical-plausibility.md`,
which demands a quantitative decoherence and thermal-noise estimate before any
biological argument is heard. Two facts govern this branch and are repeated
in the gate so nobody has to remember them: thermal energy at 310 K is about
27 meV, and the published literature connecting quantum effects specifically
to nociception is, as far as this programme has found, empty.

Branch C is not banned. It is expensive, and it has to pay.

## Progressive or degenerating

The programme is reviewed against this test at every tenth conjecture, and the
verdict is written into `ledger/OPEN.md` with a date.

**Progressive** if, since the last review, the belt has produced at least one
prediction that was novel when made, was testable with existing methods, and
was then confirmed by evidence not used to construct it.

**Degenerating** if every belt change since the last review was made only to
accommodate a failure already observed, or if the number of live auxiliary
hypotheses grew while the number of forbidden observations did not.

A programme that is degenerating for two consecutive reviews is closed, and
this file records why. That is the point of writing it down in advance.
