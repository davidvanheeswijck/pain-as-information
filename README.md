# Pain as Information

A research programme on whether chronic neuropathic pain can be treated as a
**signalling** problem rather than a **tissue** problem: read what the nerve is
actually sending, and rewrite it, instead of silencing the nerve by drug,
current or knife.

Today's clinic has three moves. Damp everything systemically (opioids,
gabapentinoids, duloxetine). Destroy the wire (neurotomy, radiofrequency
denervation, in the last resort amputation). Or shout over the line
(paraesthesia-generating stimulation). All three are lossy in the same way:
they do not distinguish the signal from the channel. If nociception is carried
as information, that is a strange way to intervene on it.

This repository holds the research base, the conjectures, and the machinery
that tries to kill them.

## What this is not

It is not a treatment, a device, a protocol or medical advice. It contains no
patient data. See [ETHICS.md](ETHICS.md), which is a hard constraint on this
repository, not a disclaimer at the bottom of it.

## The hard core

Four commitments. If one of these is falsified the programme is finished, not
patched. They are stated with their killers in [PROGRAMME.md](PROGRAMME.md).

1. Nociceptive traffic carries structure beyond mean firing rate.
2. That structure is at least partly readable from outside the central nervous
   system, at the axon, the dorsal root ganglion or the cord.
3. An intervention that targets the structure can change perceived pain
   without proportionally degrading the channel's other traffic.
4. There exists a physically realisable transducer for such an intervention.

Commitments 1 to 3 are the programme. Commitment 4 is where the speculative
branches live, including the quantum branch, and it is the one under the
heaviest guard.

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

**Quantum sensing survives and is where the programme spends.** Optically
pumped magnetometers read nerve traffic without touching it, they work today,
and a superficial limb nerve gives about 1 pT at 6.5 mm, which has already been
recovered in humans. Worth noting that the benefit is *geometric*, not quantum
mechanical: a room-temperature sensor 13 times noisier than a SQUID wins
because it sits 5 mm from the skin instead of 30 mm.

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
calibration plot, the hard-core board, panel history and evidence coverage.

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
| `evidence/` | The research base. Six briefs, each separating established from contested from speculative. |
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

Early, and already pointing somewhere other than where it started.

**Eight conjectures filed. Seven refuted, one wounded, none confirmed.** Six
died in adversarial panel review, one died by simulation. That is the intended
behaviour, not a failure mode: the programme is built to kill its own ideas
cheaply, and the author's favourites went first.

### What the evidence pass established

The first evidence pass presses hard on hard-core commitment 2. What is
readable outside the central nervous system is fibre class, intensity and a
pathological ongoing-activity signature. Pain *quality* is not, and allodynia
is a counterexample in principle, because the traffic that hurts arrives on Aβ
fibres indistinguishable from normal touch and the pathology is in the dorsal
horn.

It also moves the programme off the spinal cord. Frequency specificity there is
probably dose: a double-blind crossover found 1, 4, 7 and 10 kHz equivalent
once electrode position and charge were controlled, and the same waveform is
null when blinded and large when open-label **in the same patients**. The
tuning thesis is alive one level out, at the dorsal root ganglion, where 20 Hz
field stimulation abates C-fibre trains while Aβ passes unattenuated, by a
named anatomical mechanism, in work with no industry conflict. A blinded
sham-controlled crossover trial published in May 2026 has since shown dorsal
root ganglion stimulation beating sham by 2.5 points on an 11-point pain scale
in established responders, so the target itself is now on firmer ground than
the frequency claim.

### On the quantum question, settled three times over

Quantum *information manipulation* of pain signalling is below 0.1% with an
empty literature. Two Branch C conjectures then died for the same structural
reason: a well-designed physics measurement with no demonstrated instance of
the physics in nociceptive tissue. What survives is quantum *instrumentation*,
and that has now been costed rather than argued (below).

### The one live conjecture

**C-003** is the only conjecture whose probability rose under review, from 0.30
to 0.62. It proposes that mechanical allodynia is a coincidence phenomenon in
time: ongoing C-fibre discharge opens a window during which otherwise normal
touch input is routed to nociceptive output. Its killer has been rewritten
after review, with the window's time constant now pre-registered from the
wind-up literature rather than asserted.

### The result that cost a few minutes of laptop compute

C-008 asked whether interference rejection rather than sensor sensitivity is
what blocks magnetic detection of C-fibre traffic. Simulation refuted it, and
the refutation is more useful than the conjecture would have been. Gradiometry
suppresses interference by 287,000 times in energy and still lands 17 times
short. But fix the interference and sensitivity immediately becomes binding,
which the single-axis sweeps had hidden. Three requirements together, and any
one alone fails: channel matching around 1 part in 10⁴, local myogenic
interference controlled, and a sensor near 0.2 fT/√Hz. Meet all three and the
simulated signal is recovered at nearly five times the matched null.

**So Branch B is not closed. It is costed.** The conjecture predicted its own
death would close the branch, and instead the death produced a specification a
hardware group could act on.

### What is still missing

`ledger/OPEN.md` is the honest current state and lists the gaps, including the
fact that **nobody has ever measured the information rate of a nociceptor axon
in bits per second**, which is a conspicuous hole for a programme premised on
pain being an information problem. It also records the harness defects, of
which the worst is now fixed: the hostile-referee gate produced reviewable text
in only one of its first six runs, because reasoning models were spending their
entire output budget on hidden thinking and returning nothing, and the harness
was scoring that silence as an objection no reviewer had made.

## Licence

Code MIT, prose CC BY 4.0. Reuse for your own programme welcome. The gate
prompts and the refutation ledger are the parts worth stealing.
