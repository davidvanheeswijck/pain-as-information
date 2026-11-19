# Pain as Information

A research programme that began by asking whether chronic neuropathic pain can
be treated as a **signalling** problem rather than a **tissue** problem: read
what the nerve is actually sending, and rewrite it, instead of silencing the
nerve by drug, current or knife.

**That original aim is closed.** On 2026-11-19 the first programme review found
the programme degenerating, and the owner closed the original hard core in
writing ([D-003](ledger/DECISIONS.md)). The programme continues as **evidence
appraisal**: reading the published record on three questions a treating team
faces, at population level, and registering predictions that can fail. What it
set out to do, what happened and what it is now are all below.

Today's clinic has three moves. Damp everything systemically (opioids,
gabapentinoids, duloxetine). Destroy the wire (neurotomy, radiofrequency
denervation, in the last resort amputation). Or shout over the line
(paraesthesia-generating stimulation). All three are lossy in the same way:
they do not distinguish the signal from the channel. That was the motivation.

This repository holds the research base, the conjectures, and the machinery
that tries to kill them.

## What this is not

It is not a treatment, a device, a protocol or medical advice. It contains no
patient data. See [ETHICS.md](ETHICS.md), which is a hard constraint on this
repository, not a disclaimer at the bottom of it.

## The original hard core, closed 2026-11-19

The programme was opened on four commitments. It was written down that if one
fell, the programme was finished, not patched. Each is stated with its killer in
[PROGRAMME.md](PROGRAMME.md), which keeps the original text. Their standing now:

1. Nociceptive traffic carries structure beyond mean firing rate. *Weakly
   supported, not falsified; never tested here.*
2. That structure is readable outside the central nervous system, at the axon,
   the peripheral nerve trunk or the dorsal root ganglion. *Fallen for
   touch-evoked pain. It stands only for detecting ongoing activity, at group
   level.* (An earlier version of this file said "at least partly readable" and
   named the cord. PROGRAMME.md never said either, and this is now the same
   wording.)
3. An intervention that targets the structure can change perceived pain without
   proportionally degrading the channel's other traffic. *Not shown. The
   foothold at the ganglion is argued from one side, and frequency specificity
   at the spinal cord is probably dose.*
4. There exists a physically realisable transducer for such an intervention.
   *Partly: quantum instrumentation survives as a costed specification, quantum
   manipulation of pain signalling does not. Not pursued further.*

HC-2's killer is a demonstration that the discrimination is made centrally from
traffic that is peripherally indistinguishable. The ledger's own evidence meets
that for touch-evoked pain: the traffic that hurts arrives on Aβ fibres and is
indistinguishable from normal touch. "Read the signal and rewrite it" is
therefore closed as this programme's purpose.

## What the programme is now

Evidence appraisal, for three questions framed as ones a treating team faces:

1. Which generator maintains long-standing regional neuropathic pain: a
   peripheral lesion, the ganglion, or central amplification?
2. Why does the benefit of ganglion stimulation fade?
3. Are touch-evoked allodynia and background pain separable mechanisms?

Next, in order: an evidence map for the three questions built from full texts,
then one prediction registered against data not yet read. Simulation happens
only on a published model that first reproduces its own results here, with a
verdict rule whose every outcome is reachable. The refutation ledger, the
evidence briefs and the harness stay. The review now falls every ten pieces of
work, and a second consecutive degenerating review closes the programme. See
"The programme from 2026-11-19" in [PROGRAMME.md](PROGRAMME.md).

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

## How the programme runs

Conjecture in, adversarial panel, verdict, ledger. Repeat.

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
| `evidence/` | The research base. Nine briefs, each separating established from contested from speculative. |
| `conjectures/` | Numbered hypotheses. One file each, template enforced. |
| `pipeline/gates/` | The adversarial prompts. The interesting part. |
| `pipeline/reviews/` | Verbatim model verdicts, committed, failures included. |
| `ledger/` | What survived, what died and what killed it, and the programme's spend decisions with the evidence that would reverse them. |
| `tools/` | The runner, the panel selector, the linter, the citation verifier. |

## Use

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

**Degenerating at the first review (2026-11-19). The original hard core is
closed by D-003, and the programme continues as evidence appraisal.** The
current position is kept in [ledger/OPEN.md](ledger/OPEN.md).

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
independent group do not find that mechanism at clinical amplitude, so that
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
