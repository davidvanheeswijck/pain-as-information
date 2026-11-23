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
| [E-10](10-descending-modulation.md) | The pain brake: descending modulation, what the CPM test measures and predicts | HC-2, HC-3, PB-2, PB-3, S-2 |
| [E-11](11-evidence-map.md) | Evidence map for the three questions, from full texts: which generator, why ganglion-stimulation benefit fades, whether allodynia and background pain separate | D-003, S-3 |
| [E-12](12-lumbar-root-compression.md) | Lumbar stenosis and nerve-root compression in CRPS-labelled lower-limb pain: mimic or contributor, tests that separate them, the foramen and the stimulation lead, imaging with an implant | D-004, E-05 §1 and §8a, E-11 Q-A and Q-B |

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

> **Superseded 2026-11-21.** The sentence above, that a correction is stated
> plainly "rather than annotated as a change", is no longer the convention. E-05
> already marks corrections with dated notes, and D-004 adopts that. The current
> convention: a dated "Correction, <date>" note, with the original text left
> readable. The older sentence is left visible.

## Maintenance

From 2026-11-21 the briefs are maintained, not extended (D-004,
`../ledger/DECISIONS.md`).

**Updating a brief.** When a relevant paper appears, add it under the rules
above: the identifier resolves, the queries are logged, the full text is read
where it can be, and every number carries its source. Do not write a number from
recall.

**Marking a correction.** Where an error is found in a brief, mark it where it
sits with a dated "Correction, <date>" note giving the reason, as E-05 does, and
leave the original text readable. This replaces the older sentence under "Rules"
(see the note there).

**Source-status tags.** Rows in E-11 carry exactly one of `number read in full
text`, `number from abstract only`, `direction only` or `no data found`. They are
defined in E-11 ("How to read the tables"). New rows use the same tags.

## Known gaps

Tracked in [../ledger/OPEN.md](../ledger/OPEN.md) so they stay visible rather
than being quietly forgotten. The largest at present: no published estimate
exists for the information rate of a single nociceptor axon in bits per second,
which is a striking hole for a programme premised on nociception being an
information problem.
