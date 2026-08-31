# Conjectures

One file per conjecture, numbered `C-0NN-slug.md`, structured by
[TEMPLATE.md](TEMPLATE.md) and enforced by `tools/lint-conjecture.py`.

## Writing one

    cp conjectures/TEMPLATE.md conjectures/C-001-your-slug.md
    $EDITOR conjectures/C-001-your-slug.md
    tools/lint-conjecture.py conjectures/C-001-your-slug.md

The linter will refuse it until it states what would refute it, gives a prior
between 0 and 1, lists at least two rivals, quantifies its killer, and cites
something that resolves. Those are not style preferences. Each one is a
countermeasure to a specific documented failure mode, and the reasons are in
[../EPISTEMICS.md](../EPISTEMICS.md).

**Read [../ledger/REFUTED.md](../ledger/REFUTED.md) before you write.** The
commonest way to waste a round here is to propose something that has already
been killed, because the priors that generated it the first time are still the
priors in play. The linter warns on textual similarity to a refuted entry, but
it only catches the obvious cases.

## The three branches

Assigned in front matter, and the assignment is load-bearing.

- **A**, classical temporal and spatial structure. Where the programme expects
  to get somewhere, and where near-term conjectures should live.
- **B**, quantum technology as instrument. Reading with quantum sensors,
  designing with quantum computation. No claim that anything quantum happens
  inside a neuron.
- **C**, quantum effects in neural tissue. Permitted, expensive, and gated on a
  quantitative decoherence and thermal-noise estimate that the conjecture
  supplies itself. The linter fails a Branch C conjecture, or any conjecture
  using quantum vocabulary, whose Mechanism section carries no timescale and no
  energy scale.

**Do not claim Branch A while the mechanism requires Branch C.** That specific
laundering is what gate 00 exists to catch and it is the failure this programme
is most at risk of.

## Lifecycle

    draft ──lint──> in-panel ──tools/panel.sh──> open | wounded | refuted
                                                   │
                                        gate 08 ───┴──> a new, strictly weaker
                                                        conjecture with its own id
                                                        and a `lineage:` pointer

`prior` is written before the panel and never edited afterwards. `posterior` is
written after. The difference between them, visible in git history, is the only
durable record of what the round actually taught anyone, and a programme where
every posterior exceeds every prior is a programme that is not learning.

A refuted conjecture keeps its file. It is closed with a reason and recorded in
the ledger, never deleted.
