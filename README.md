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

There is a third reading of "quantum" that is neither of these and is entirely
defensible: **quantum technology applied to neuroscience** rather than quantum
effects inside neurons. Diamond NV-centre magnetometry and optically pumped
magnetometers as a way to *read* nerve traffic without touching it, and
quantum chemistry on a fault-tolerant machine as a way to *design* a
subtype-selective channel ligand. Those are engineering questions with real
error bars. The evidence base treats all three readings separately and says so
in every verdict.

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
| `ledger/` | What survived, what died and what killed it. |
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

Early. The evidence base is being assembled and no conjecture has yet been
through a full panel. `ledger/OPEN.md` is the honest current state.

## Licence

Code MIT, prose CC BY 4.0. Reuse for your own programme welcome. The gate
prompts and the refutation ledger are the parts worth stealing.
