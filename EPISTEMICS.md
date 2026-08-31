# Epistemics

The rules the harness enforces, and why each one exists. Every rule here is
either machine-checked by `tools/` or written into a gate prompt. A rule that
is neither is a wish, and does not belong in this file.

## 1. Refutation is the default verdict

A conjecture does not accumulate support until it passes. It is presumed dead,
and survives only if a quorum of independent reviewers **fails** to kill it.

    SURVIVES   >= 4 of 5 panel labs return NOT REFUTED, and no gate returns FATAL
    WOUNDED    3 of 5, or any gate returns MAJOR
    REFUTED    <= 2 of 5, or any gate returns FATAL

Why. Language models are agreeable. Measured sycophancy, where a model shifts
its assessment towards the position the user appears to hold, is a documented
failure of RLHF-trained assistants, and it is exactly the failure that would
destroy this project: the author has a pet theory and a strong personal motive
to believe it. Asking a model "is this good?" is therefore a broken question.
The gates ask "kill this", and the scoring treats survival as the surprising
outcome.

## 2. No two panellists from the same laboratory

`tools/panel.sh` selects reviewers under a hard constraint of distinct
`model_lab` values as reported by the router. A panel of five is five
laboratories.

Why. Models from one lab share pretraining data, post-training recipe and
failure modes, so their agreement is correlated and reads as consensus without
being independent. Self-preference bias, where a model rates its own or a
sibling's output more highly, is documented. Heterogeneous panels of smaller
models have been found competitive with a single large judge at lower cost.
Diversity here is a correctness requirement, not a hedge.

## 3. Citations are resolved, not trusted

`tools/verify-citations.py` extracts every DOI, PMID, PMCID, arXiv identifier
and NCT number from a document and resolves each against Crossref, PubMed,
OpenAlex, arXiv or ClinicalTrials.gov. Unresolvable identifiers fail CI.

Why. Fabricated references are the signature defect of language models used for
science, and they are worse than useless because they are *checkable* and
therefore convert a reader's diligence into wasted time. Resolution is cheap
and mechanical, so there is no excuse for shipping an unresolved reference.

Resolution proves existence, not support. A gate still has to ask whether the
paper says what the conjecture claims it says, and
`pipeline/gates/03-evidence-integrity.md` is the gate that does it.

## 4. Every conjecture states what would kill it, before review

`tools/lint-conjecture.py` rejects any conjecture file without a non-empty
`## Killer` section containing a concrete observation, and without a stated
prior. Popper's demarcation is not decoration here: it is a lint rule.

Why. The characteristic output of a language model asked to generate a
hypothesis is a claim that is plausible, unfalsifiable and vacuous. Requiring
the falsifier up front is the cheapest available filter, and requiring it
*before* the panel runs prevents the killer being retrofitted to whatever the
panel happened not to attack.

## 5. Priors are numbers, and they are recorded before the evidence

Each conjecture states a prior probability that it is substantially correct,
with one sentence of justification. After the panel, a posterior is recorded.
Both are in the file, both are in git history.

Why. It makes overconfidence visible over time, and it makes the difference
between "I was persuaded" and "I persuaded myself" auditable. A programme where
every posterior exceeds every prior is a programme that is not learning.

## 6. The refuted ledger is append-only and is read before proposing

`ledger/REFUTED.md` records every dead conjecture with the argument that killed
it. `tools/lint-conjecture.py` warns when a new conjecture's claim is close to a
refuted one, and the generative gate is given the ledger as context.

Why. Without it, the loop rediscovers the same dead idea indefinitely, because
each round starts from the same priors that produced it the first time. A
research programme without a graveyard is a random walk.

## 7. Severity, not confirmation

A test that a conjecture would very probably pass even if it were false counts
for nothing. Gates are instructed to assess *severity*: given this conjecture is
false, what is the probability the proposed test would still come out
favourable? Only tests with low probability of a false pass are recorded as
evidence.

Why. Confirmations are cheap and are the currency of bad science. Platt's
strong inference asks for the experiment that discriminates between live
alternatives, and that is the only experiment worth designing.

## 8. Alternatives are mandatory

Every conjecture carries at least two rival explanations for the same
observations, stated as strongly as the conjecture itself. A conjecture with no
rivals fails lint.

Why. A single hypothesis with supporting evidence is compatible with almost any
world. The question that matters is which of several accounts the evidence
prefers, and that question cannot be asked if only one account is written down.

## 9. Provenance is verified and stamped, not asserted

The runner reads the router's own model metadata and refuses to run unless the
model reports EU hosting, zero retention and no training use. What the router
actually reported is written into every verdict header, so a relaxed run is
visible in the artefact it produced.

Why. This is inherited from the sibling legislation project, and it applies for
a stronger reason here: material derived from a real clinical history motivates
this work even though none of it enters this repository, and a claim about
where data went should be evidence rather than intention.

## 10. The harness must be able to say the premise is wrong

At least one gate is instructed that "the author's framing is mistaken" is an
available and creditable verdict, and the triage gate can return
`VERDICT: WRONG QUESTION` with a reformulation.

Why. Every other rule here polices the answer. This one polices the question,
which is where a motivated programme actually goes wrong.

## Pseudoscience tells

`pipeline/gates/01-physical-plausibility.md` carries an explicit checklist,
because this subject area is unusually well populated with confident nonsense
and the failure is embarrassing rather than merely wrong. Automatic FATAL on:
a mechanism invoking coherence, resonance or entanglement with no timescale or
energy estimate; "frequency" used without units; appeal to unnamed suppressed
research; a claimed effect with no dose-response and no mechanism; energy
sources not in the standard model; and any citation that resolves to a
predatory or non-indexed venue and is load-bearing.

## What this file does not do

It does not make the output true. A harness of this kind raises the floor on
rigour and lowers the rate of embarrassing error. It does not substitute for an
experiment, and no verdict produced by it is evidence about the world. It is
evidence about the argument.
