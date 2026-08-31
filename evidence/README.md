# Evidence base

The research base the programme argues from. Each brief separates
**ESTABLISHED** from **CONTESTED** from **SPECULATIVE**, gives identifiers that
resolve, and marks what it could not verify.

| Brief | Subject | Bears on |
|---|---|---|
| [E-01](01-nociceptive-coding.md) | How pain information is encoded on nerves | HC-1, HC-2 |
| [E-02](02-reading-the-signal.md) | Reading neural signals from nerve and cord in humans | HC-2, HC-4 |
| [E-03](03-writing-the-signal.md) | Writing to, tuning and selectively blocking nerve signals | HC-1, HC-3, HC-4, PB-4 |
| [E-04](04-quantum-audit.md) | Quantum effects in biology, and quantum technology for neuroscience | Branch B, Branch C |
| [E-05](05-crps.md) | CRPS: mechanism, natural history, and why treatment fails | PB-2, PB-3, PB-5 |
| [E-06](06-prior-art-ai-harness.md) | Prior art on multi-model harnesses for hypothesis evaluation | the harness itself |

## Rules

**Every identifier resolves.** `tools/verify-citations.py` runs over this
directory in CI. A DOI, PMID, PMCID, arXiv id or NCT number that does not
resolve fails the build. Anything deliberately unresolvable carries
`[UNVERIFIED]` in the same sentence, which the verifier honours.

**Resolution is not support.** A citation that exists may still not say what it
is cited for. Only 51.5% of sentences in generative search output are fully
supported by their citations (arXiv:2304.09848). Gate 03 asks the second
question; the verifier only answers the first.

**Negative results are in scope and are wanted.** A brief that reports only
what worked is not an evidence base, it is advocacy. The most valuable single
items in this directory are the failed trials: PROCO, the Hara and Gulisano
sham-controlled nulls, the unpublished Grünenthal Phase 3 results, the
magnetogenetics refutation.

**Industry funding and blinding are always stated.** In this field the
correlation between "unblinded, industry-sponsored" and "large effect" is
strong enough that omitting it changes the conclusion.

**A brief that is wrong gets corrected in place, not appended to.** A stale
summary sitting next to a corrected sub-finding misleads the people using it,
and derived documents are where errors hide. Where a correction has been
applied, the corrected claim is stated plainly rather than annotated as a
change, and git history holds the diff.

## Known gaps

Tracked in [../ledger/OPEN.md](../ledger/OPEN.md) so they stay visible rather
than being quietly forgotten. The largest at present: no published estimate
exists for the information rate of a single nociceptor axon in bits per second,
which is a striking hole for a programme premised on nociception being an
information problem.
