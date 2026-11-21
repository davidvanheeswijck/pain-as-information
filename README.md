# Pain as Information

This repository is now a **public evidence base on chronic neuropathic pain as a
signalling problem**. It holds ten evidence briefs, a record of nine refuted
conjectures, seven simulations (two closed conjectures, C-004 and C-008; five
later ones, S-1 to S-3, S-1b and S-2b, tested published models), a closed
research programme, and the method that was used. It is kept open as an evidence
resource only ([D-004](ledger/DECISIONS.md), 2026-11-21): no further predictions
or simulations are run, and the briefs are corrected and updated when relevant
papers appear. No prediction was scored against unread data.

**What it set out to do.** It began as a research programme asking whether
chronic neuropathic pain can be treated as a **signalling** problem rather than
a **tissue** problem: read what the nerve is actually sending, and rewrite it,
instead of silencing the nerve by drug, current or knife.

**What happened.** The conjectures were all refuted. On 2026-11-19 the first
programme review found the programme degenerating, and the owner closed the
original hard core in writing ([D-003](ledger/DECISIONS.md)). The programme
continued for two days as evidence appraisal on three questions a treating team
faces. Its one prediction, registered against a paper not yet read, was registered
twice (P-003, P-004) and neither could be scored, because scripted access to the
paper failed both times. The stop rule was met.

**What it is now.** An evidence resource. The record of what failed is the
useful part, and it is public.

Today's clinic has three moves. Damp everything systemically (opioids,
gabapentinoids, duloxetine). Destroy the wire (neurotomy, radiofrequency
denervation, in the last resort amputation). Or shout over the line
(paraesthesia-generating stimulation). All three are lossy in the same way:
they do not distinguish the signal from the channel. That was the motivation.

This repository holds the research base, the conjectures, and the machinery
that tried to kill them.

## How to use this

- **The briefs** are in [evidence/](evidence/README.md), one file per subject.
  Each separates established from contested from speculative, and each
  identifier resolves. Start with the table in `evidence/README.md`. E-11 maps
  the three questions below to what the literature offers.
- **Source-status tags.** In E-11 every row carries exactly one tag.
  `number read in full text` means the number was read in the open full text.
  `number from abstract only` means it was read in an abstract and no further.
  `direction only` means the source gives a direction and no usable number.
  `no data found` means the logged queries returned nothing on point, which is
  a statement about those queries and not about the literature.
- **Corrections** are marked in the brief as "Correction, <date>", with the
  original claim readable beside it. E-05 has several.
- **The refuted ideas** are in [ledger/REFUTED.md](ledger/REFUTED.md): nine
  conjectures, each with the reason it died and the condition for re-proposing
  it. The numbered files are in [conjectures/](conjectures/).
- **What was tried and what failed** is in [ledger/OPEN.md](ledger/OPEN.md),
  and the decisions with their reasons are in
  [ledger/DECISIONS.md](ledger/DECISIONS.md).
- **Nothing here is medical advice.** It is population-level reading of the
  published record, with no patient data, and it says nothing about any
  person's care. See [ETHICS.md](ETHICS.md).

## What this is not

It is not a treatment, a device, a protocol or medical advice. It contains no
patient data. See [ETHICS.md](ETHICS.md), which is a hard constraint on this
repository, not a disclaimer at the bottom of it.

## The original hard core, closed 2026-11-19

The programme was opened on four commitments. It was written down that if one
fell, the programme was finished, not patched. Each is stated with its killer in
[PROGRAMME.md](PROGRAMME.md), which keeps the original text. Their standing now:

1. Nociceptive traffic carries structure beyond mean firing rate. *Weakly
   supported, not falsified; no informative test here (S-1 gave no verdict).*
2. That structure is readable outside the central nervous system, at the axon,
   the peripheral nerve trunk or the dorsal root ganglion. *Fallen for
   touch-evoked pain. It stands only for what is peripherally readable: fibre
   class, intensity and a group-level ongoing-activity signature.* (An earlier version of this file said "at least partly readable" and
   named the cord. PROGRAMME.md never said either, and this is now the same
   wording.)
3. An intervention that targets the structure can change perceived pain without
   proportionally degrading the channel's other traffic. *Not shown. The
   foothold at the ganglion is argued from one side (one independent model
   reports direct Aβ activation and does not model T-junction silencing; the
   other finds the route only above clinical amplitudes, in one population of
   model neurons), and frequency specificity at the spinal cord is probably
   dose.*
4. There exists a physically realisable transducer for such an intervention.
   *Partly: quantum instrumentation survives as a costed specification, quantum
   manipulation of pain signalling does not. Not pursued further.*

HC-2's killer is a demonstration that the discrimination is made centrally from
traffic that is peripherally indistinguishable. The ledger's own evidence meets
that for touch-evoked pain: the traffic that hurts arrives on Aβ fibres and is
indistinguishable from normal touch. "Read the signal and rewrite it" is
therefore closed as this programme's purpose.

## What the repository is now

An evidence resource. From 2026-11-19 to 2026-11-20 the programme appraised the
evidence for three questions framed as ones a treating team faces:

1. Which generator maintains long-standing regional neuropathic pain: a
   peripheral lesion, the ganglion, or central amplification?
2. Why does the benefit of ganglion stimulation fade?
3. Are touch-evoked allodynia and background pain separable mechanisms?

Step 1 was an evidence map built from full texts (E-11). Step 2 was one
prediction registered against data not yet read. It was registered twice
(P-003, P-004) and neither registration could be scored, which met the stop
rule. The owner then
decided, in [D-004](ledger/DECISIONS.md), to keep the repository open as an
evidence resource only.

What is no longer done: no further predictions or simulations, which is what the
owner decided. Conjectures and panels are also paused, and the review cycle is
read as suspended while D-004 stands. Both are interpretations of the owner's
words that D-004 flags for the owner to confirm. What is maintained: the briefs
are corrected when an error is found and updated when a relevant paper appears,
and the refutation ledger and the harness stay as published. Reversing D-004
needs a new decision, D-005, written before any work starts. See "The repository from 2026-11-21" in
[PROGRAMME.md](PROGRAMME.md).

## On the quantum question

This programme was started partly on the intuition that if nerves carry
information, information-level and possibly quantum-level manipulation should
beat brute force. Half of that intuition is well founded and half of it is a
trap, and the repository is built to keep the two apart.

The well founded half is **temporal structure**. Frequency and pattern already
do mechanistically different things in the spinal cord and in peripheral nerve,
and closed-loop devices that measure evoked responses already beat open-loop
ones in randomised trials. That is ordinary physics and live clinical science,
and it is under-exploited.

The trap is **quantum coherence in warm neural tissue**. Thermal energy at body
temperature is roughly 27 meV and decoherence in a wet 310 K environment is
brutally fast, which is why the strongest published proposals in this space
remain contested after two decades. There is, further, essentially no published
work connecting quantum effects specifically to nociception. Anything entering
this repository through that door has to pass a quantitative decoherence gate
before anyone spends another sentence on it.

There is a third reading of "quantum" that is neither of these: **quantum
technology applied to neuroscience** rather than quantum effects inside
neurons. That reading splits, and the evidence base has now split it.

**Quantum sensing survives as an instrument.** Optically
pumped magnetometers read nerve traffic without touching it, they work today,
and a superficial limb nerve gives about 1 pT at 6.5 mm, which has already been
recovered in humans. Worth noting that the benefit is *geometric*, not quantum
mechanical: a room-temperature sensor 13 times noisier than a SQUID wins
because it sits 5 mm from the skin instead of 30 mm. Under D-003 the sensor
work is not being pursued.

**Quantum computation for ligand design does not survive.** The two rigorous
resource estimates in this space, both metalloenzyme active sites, call for
111 and about 2,158 logical qubits and 10⁸ and 5 × 10⁶ physical qubits
respectively. The current hardware milestone is a surface code below threshold
with, in headline terms, one logical qubit. And the deeper problem does not
improve with hardware: phase estimation prices one energy at one geometry,
while the quantities that matter pharmacologically are conformational, which is
a sampling problem where quantum computers have no known advantage. Written up
as a decision, with the evidence that would reverse it, in
[ledger/DECISIONS.md](ledger/DECISIONS.md).

The evidence base treats all these readings separately and says which one it is
talking about in every verdict.

## Watching it

**[davidvanheeswijck.github.io/pain-as-information](https://davidvanheeswijck.github.io/pain-as-information/)**

A dashboard showing the conjecture lineage graph, the prior-against-posterior
calibration plot, the original hard-core board (closed, with each commitment's standing), panel history and evidence coverage.

It is **generated from this repository** by `tools/build-dashboard.py`, and CI
fails the build if it is stale. That is deliberate. A hand-maintained summary
goes quietly out of date and then misleads the people relying on it, which has
already happened twice in this repository's first day: once when the README
described a route the briefs behind it had closed, and once when material was
asserted rather than derived and had to be retracted. Anything on that page can
be traced back to a file here.

The calibration plot is the part worth looking at first. If every posterior sits
above its prior, the programme is not learning, it is agreeing with itself.

## The method, and how it ran

Conjecture in, adversarial panel, verdict, ledger. Repeat. This is the loop the
programme ran while it was filing conjectures. It is kept as published and is
paused under D-004; the tools are still here and the record is what they produced.

```
conjectures/C-0NN-*.md            a numbered conjecture, with its own killer
    |
    +-- tools/lint-conjecture.py  structure: does it state what would refute it?
    +-- tools/verify-citations.py mechanically resolve every DOI, PMID, arXiv id
    |
    +-- tools/panel.sh            N gates x heterogeneous model labs, EU-hosted
    |
    v
pipeline/reviews/                 every verdict committed, refutations included
    |
    v
ledger/REFUTED.md or ledger/OPEN.md
```

The design commitments behind that loop are in
[EPISTEMICS.md](EPISTEMICS.md). Three of them matter more than the rest:

- **Refutation is the default.** A conjecture does not need votes to die. It
  needs a quorum of independent labs *failing* to kill it in order to survive.
- **No two panellists from the same laboratory.** Panel selection enforces
  model-lab diversity, because a panel of one lab's models agreeing with itself
  is not independent evidence.
- **Citations are resolved, not trusted.** Every reference in a conjecture or
  an evidence brief is checked against Crossref, PubMed, OpenAlex, arXiv or
  ClinicalTrials.gov by a script that runs in CI. A fabricated reference fails
  the build.

## Layout

| Path | What lives there |
|---|---|
| `evidence/` | The research base. Ten briefs (E-01 to E-08, E-10, E-11), each separating established from contested from speculative. |
| `predictions/` | Two registrations of one prediction (P-003, P-004) and their unscorable results. No further predictions are registered (D-004). |
| `conjectures/` | Numbered hypotheses. One file each, template enforced. |
| `pipeline/gates/` | The adversarial prompts. The interesting part. |
| `pipeline/reviews/` | Verbatim model verdicts, committed, failures included. |
| `ledger/` | What survived, what died and what killed it, and the programme's spend decisions with the evidence that would reverse them. |
| `tools/` | The runner, the panel selector, the linter, the citation verifier. |

## Use

To read, see "How to use this" above. The commands below run the tools; the
panel step is paused under D-004, and the linter and verifier are what keep the
briefs honest.

    cp .env.example .env && $EDITOR .env      # REQUESTY_API_KEY; .env is gitignored
    tools/lint-conjecture.py conjectures/C-001-*.md
    tools/verify-citations.py evidence/*.md
    tools/panel.sh conjectures/C-001-*.md

Review runs are routed through an EU-hosted, zero-retention endpoint by
default, and the runner reads the router's own model metadata and refuses to
start unless the model it is about to use reports `geolocation: eu`,
`data_retention_days: 0` and `data_used_for_training: false`. What the router
actually said is stamped into every verdict. See [tools/README.md](tools/README.md).

## Status

**Degenerating at the first review (2026-11-19). The original hard core was
closed by D-003. The repository is kept open as an evidence resource only by
D-004 (2026-11-21).** The current position is kept in
[ledger/OPEN.md](ledger/OPEN.md).

### What happened

**Nine conjectures filed. Nine refuted, none live, none confirmed.** Five died
in adversarial panel review, two were closed at triage (one by a cheap
literature check, one as the wrong question), and two died by simulation. The
programme was built to kill its own ideas cheaply, and the author's favourites
went first. Reasons and re-proposal conditions are in
[ledger/REFUTED.md](ledger/REFUTED.md).

**Five simulations in November, four without an informative verdict.**

- S-1, DRG T-junction rate versus pattern: no verdict, the positive control failed.
- S-1b, a re-tuned version of the same model: no tuning found within the
  budget, so the predictions were not run.
- S-2, a dorsal-horn model of touch-evoked pain: no verdict, the positive
  control failed by its own design.
- S-2b, the corrected run: onset inconclusive, the reduced-C test not
  informative, the stimulation questions no verdict.
- S-3, generator discrimination: the pre-registered kill was triggered, and the
  positive control passed. The available observations do not localise the
  generator within the modelled ranges.

**One evidence brief since the independent review.** E-10, on descending
modulation (the "pain brake"), found a weak handle: the test is a difference
between two pain ratings with poor between-session reliability, the founding
predictive claims have not replicated cleanly, and two small CRPS cohorts found
the brake not reduced. It is the only thing the programme learned about the
world in that period, and it is negative.

**The review of 2026-11-19** applied the test in PROGRAMME.md. No prediction
since the programme opened was novel, testable and then confirmed by evidence
not used to construct it. The owner then closed the original hard core and
chose evidence appraisal over continuing as before, narrowing the core and
simulating on, or closing and writing up.

**The stop rule, 2026-11-20.** Two registrations of one prediction
against one unread paper (P-003, P-004) were both unscorable, because scripted
routes could not obtain it. Two registrations, neither scored. That is a statement about
access, not about the claim or the paper. The owner chose to keep the repository
open as an evidence resource only (D-004, 2026-11-21).

### What the evidence pass established

The first evidence pass pressed hard on commitment 2, and it did not survive for
touch-evoked pain. What is readable outside the central nervous system is fibre
class, intensity and a pathological ongoing-activity signature. Pain *quality*
is not, and allodynia is a counterexample in principle, because the traffic that
hurts arrives on Aβ fibres indistinguishable from normal touch and the
pathology is in the dorsal horn.

It also moved the programme off the spinal cord. Frequency specificity there is
probably dose: a double-blind crossover found 1, 4, 7 and 10 kHz equivalent
once electrode position and charge were controlled, and the same waveform is
null when blinded and large when open-label **in the same patients**. At the
dorsal root ganglion, 20 Hz field stimulation abates C-fibre trains while Aβ
passes unattenuated in rat work from one lineage, but two models from an
independent group do not find it at clinical amplitude (one reports direct Aβ
activation and does not model T-junction silencing; the other finds the route
only above clinical amplitudes, in one population of model neurons), so that
foothold is argued from one side. A blinded sham-controlled crossover trial
published in May 2026 showed dorsal root ganglion stimulation beating sham by
2.5 points on an 11-point pain scale in established responders. The target is on
firmer ground than the frequency claim.

### On the quantum question

Quantum *information manipulation* of pain signalling is below 0.1% with an
empty literature. Two Branch C conjectures died for the same structural reason:
a well-designed physics measurement with no demonstrated instance of the
physics in nociceptive tissue. Quantum *instrumentation* survives and was costed
rather than argued. C-008 asked whether interference rejection rather than
sensor sensitivity blocks magnetic detection of C-fibre traffic. Simulation
refuted it, and showed that three requirements together are needed, each
failing alone: channel matching around 1 part in 10⁴, local myogenic
interference controlled, and a sensor near 0.2 fT/√Hz. That is a specification,
and under D-003 it is parked, not pursued.

### What is still missing

`ledger/OPEN.md` is the honest current state and lists the gaps, including the
fact that **nobody has ever measured the information rate of a nociceptor axon
in bits per second**, which is a conspicuous hole for a programme premised on
pain being an information problem. It also records the harness defects.

## Licence

Code MIT, prose CC BY 4.0. Reuse for your own programme welcome. The gate
prompts and the refutation ledger are the parts worth stealing.
