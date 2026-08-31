# tools

Standard library Python and bash. No pip dependencies, so this runs on a bare
CI runner and on a laptop with no virtualenv.

| Tool | What it does |
|---|---|
| `review.sh` | One gate, one model, one verdict. Verifies routing before spending a token and stamps what the router said into the output. |
| `panel.py` | Selects a review panel under a hard lab-diversity constraint. |
| `panel.sh` | Runs a conjecture through all gates then a panel vote, then tallies. |
| `tally.py` | Applies the scoring rules in EPISTEMICS.md to a panel run. |
| `verify-citations.py` | Resolves every DOI, PMID, PMCID, arXiv id and NCT number against a real registry. |
| `lint-conjecture.py` | Structural linter. Rejects a conjecture that does not say what would refute it. |
| `lint-privacy.py` | Backstop for the privacy firewall in ETHICS.md. |
| `new-requesty-key.sh` | Mints a project-scoped router key with its own monthly budget. |

## Setup

    cp .env.example .env && $EDITOR .env

`REQUESTY_API_KEY` is the only required value. `.env` is gitignored and every
tool reads it the same way, so the two never disagree about which key is in
play.

For a project-scoped key with its own spending cap:

    tools/new-requesty-key.sh "pain-as-information" 25

That needs a key with `manage` permission, which is separate from a key that
can call completions. If yours cannot, the script says so and gives the one
manual step. See the note at the top of the script.

## Running a conjecture

    tools/panel.sh conjectures/C-001-whatever.md

That lints, verifies citations, assembles a panel, runs eight gates rotated
across five laboratories, runs a five-lab vote, and writes everything to
`pipeline/reviews/<id>/<timestamp>/`. Roughly thirteen model calls.

Useful flags:

    --dry-run                 assemble the panel and stop, spending nothing
    --size 3                  smaller and cheaper panel
    --exclude-lab anthropic   drop a laboratory entirely
    --gates "00-triage"       run one gate
    --rivals conjectures/C-002-other.md    add a candidate to the ballot

`--exclude-lab` is how you avoid self-review. A model must never grade its own
hypothesis, and self-preference bias is measured rather than theoretical
(arXiv:2404.13076). If a conjecture was drafted with help from a model, exclude
that model's laboratory from its panel.

`--rivals` is the mechanism behind the anti-sycophancy design. The ballot
presents every candidate unattributed, ordered by a content hash rather than by
authorship, so there is no user-preference signal for a panellist to be
agreeable towards. A run with no rivals still works, but the protection is
weaker, so add rivals when you have them.

## Routing

Reviews run on an EU-hosted, zero-retention endpoint by default. The runner
reads the router's own model metadata and refuses to start unless the model
reports `geolocation: eu`, `data_retention_days: 0` and
`data_used_for_training: false`. What the router actually reported goes into
every verdict header, so a relaxed run is visible in every artefact it
produced.

Three separate guarantees, three separate switches, so that relaxing one does
not silently drop the other two:

    REVIEW_REQUIRE_EU           1
    REVIEW_REQUIRE_NO_TRAINING  1
    REVIEW_REQUIRE_ZDR          1

Unknown counts as failure: a router that does not report a field is refused
rather than read as a quiet yes. `REVIEW_VERIFY=0` skips the check entirely,
and the provenance line then names the router and claims nothing about
jurisdiction, because nothing was checked.

**Pinning the EU base URL is not sufficient on its own.** Requesty's own
documentation is explicit that the EU endpoint guarantees only that their
processing stays in the EU, and that the model must also be an EU model. The
same key works on every regional endpoint, so a typo in the base URL silently
downgrades the routing with no error. This is why the check is per model and at
request time rather than read from config.

**EU-hosted is not EU-made.** Most models on this endpoint are built by
American and Chinese laboratories and run on European infrastructure under
zero retention. Of those offered, only Mistral's are from a European
laboratory. Both facts belong in the record.

## Citation verification

    tools/verify-citations.py evidence/ conjectures/

Resolves identifiers against Crossref, DataCite, PubMed, arXiv and
ClinicalTrials.gov, caches successes permanently and failures for a week, and
fails the build on anything that does not resolve.

Two things it deliberately does not do. It does not use Crossref's
`query.bibliographic` fuzzy search as an existence check, because that endpoint
returns high-scoring hits for entirely invented references and its `score` is
an unbounded Lucene score rather than a confidence. And it does not claim that
a resolved citation *supports* the sentence it is attached to: only 51.5% of
sentences in generative search output are fully supported by their citations
(arXiv:2304.09848), so support is a separate question and gate 03 asks it.

Set `CROSSREF_MAILTO` and, if you have one, `NCBI_API_KEY`. Both registries
give politer service to clients that identify themselves, and the NCBI key
raises the rate limit from 3 to 10 requests per second.

## Privacy backstop

    tools/lint-privacy.py

Runs in CI over every tracked file. It is a safety net, not the primary
control: the primary control is not writing case material into a public
repository in the first place. It redacts its own output, because a privacy
linter that prints the private data into a CI log has defeated itself.

To have it check for specific names, create `tools/.privacy-names`, one
lowercase token per line. That file is gitignored by design, since a list of
the names that must not appear is itself something you would not publish.
