# P-003. Result: UNSCORABLE (source not obtained)

**Written 2026-11-19 by the reader, a different agent from the one that
registered the prediction** (Claude Fable 5.2, a language model, working from
`REGISTRATION.md` §7 in this folder). The registration is the rule; this file
only applies it.

Intent: `intent/programme/2026-11-19-pivot-to-evidence-appraisal.md`.

The source is Tabatabaei et al., "Subperception dorsal root ganglion
stimulation versus sham stimulation in established responders: a randomized,
double-blind crossover clinical trial", *Reg Anesth Pain Med* 2026,
PMID 42128597, doi:10.1136/rapm-2026-107906 (identifiers taken from
`evidence/05-crps.md` §6b).

> **In one paragraph.** None of the four declared routes returned the full
> text. PubMed Central and Europe PMC do not hold it. The publisher refused
> the scripted request twice with HTTP 403. The paper was therefore not read,
> no number was extracted, and the claim "D ≥ 1.0" is neither supported nor
> refuted. The registration gave this outcome a probability of 0.60 and named
> it the single likeliest. This is attempt 1 under the two-unscorable stop
> rule.

Nothing here is a statement about any person, and nothing here is a
stimulation setting or advice (ETHICS.md §3).

## 1. Step 1: the registration predates the read

`F` is `predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md`.
`git fetch origin` was run first; the working branch was already at
`origin/main`.

| What | Command (from §7 step 1) | Commit | Committer time | In UTC |
|---|---|---|---|---|
| Commit that added the file | `git log --diff-filter=A --format='%H %cI' origin/main -- F` | `0da91a657b9d50bfb0e803283d26e81c938e9a3b` | 2026-11-19T21:58:00+01:00 | 20:58:00Z |
| Last commit touching the file | `git log --format='%H %cI' -1 origin/main -- F` | `54da67f743f0b169d8fbbb5100f8304fef214d46` | 2026-11-19T22:09:48+01:00 | 21:09:48Z |
| Merge commit on the first-parent line of `main` | `git log --first-parent --format='%H %cI' -1 origin/main -- F` | `6a803c73423e064fd2fb6ffc0bac739cd9fa3255` | 2026-11-19T13:11:03-08:00 | 21:11:03Z |

The merge commit has two parents, `dfd9804` and `54da67f`, so the pull request
was merged with a merge commit and not a squash, as the registration asked.

**Commits after the one that added the file** (`git log --format='%H %cI %s'
origin/main -- F`):

| Commit | Committer time | Subject | Changes rule text (§4, §5 or §7)? |
|---|---|---|---|
| `570ac46bdd80bb292e4849aeeffe380f78e44492` | 2026-11-19T22:05:36+01:00 | P-003: tighten the registration after review, before merge and before any read | **Yes.** 303 lines added, 98 removed; the commit message lists changes to the verdict rule, method C, the construct rule, the routes and the probabilities. |
| `54da67f743f0b169d8fbbb5100f8304fef214d46` | 2026-11-19T22:09:48+01:00 | P-003: close the remaining rule gaps before merge; the source is still unread | **Yes.** 105 lines added, 52 removed; borrowed SD, the REFUTED wording, the Unpaywall address, the probabilities, reader step 1. |

Neither only appends below the "Amendments" heading. Both are before the merge.

**Binding time:** the latest of the merge commit and every commit that changes
rule text, which is the merge commit: **2026-11-19T21:11:03Z**.

**Step 2 started at 2026-11-19T21:11:58Z** (the time of the first request),
55 seconds after the binding time. The reader's clock read 21:11:40Z when
step 1 was finished.

**No read before the binding time.** The reader made no request about the
paper before 21:11:58Z and has no recollection of the paper beyond what this
repository says. The brief given to the reader contained nothing from the
paper. The reader cannot check other sessions; the coordinating session's
attestation is in the registration and is not repeated here as the reader's
own. The result is not void on anything the reader can see.

## 2. Step 2: the access log

Every request was sent by one script, one request per invocation, with the
user-agent `research-reader/1.0 (scripted; one request per step)`, no cookies
and no contact details. Redirects were followed automatically inside the
request. Every request received an HTTP response, so the one permitted
identical repeat was never used. No header, client or address was altered.

| # | Route (§5) | Time (UTC) | Address requested | HTTP status | Size | What came back (kind, not content) |
|---|---|---|---|---|---|---|
| 1 | 1, PubMed Central: `elink` | 21:11:58 | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pmc&id=42128597` | 200 | 326 bytes | XML link result with an empty link set: no PMC identifier. No `efetch` request follows. |
| 2 | 2, Europe PMC: `search` | 21:12:06 | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:42128597%20AND%20SRC:MED&resultType=lite&format=json` | 200 | 1,089 bytes | JSON, one record, bibliographic fields and flags only (the `lite` result type carries no abstract). Flags: `inEPMC` "N", `inPMC` "N", `isOpenAccess` "N", `hasPDF` "N". Not flagged as having full text. No `fullTextXML` request follows. |
| 3 | 3, publisher: `doi.org` | 21:12:10 | `https://doi.org/10.1136/rapm-2026-107906` | **403** | 5,546 bytes | Redirected to `https://rapm.bmj.com/lookup/doi/10.1136/rapm-2026-107906`. An HTML refusal page from the publisher's access-control service (page title "Attention Required! \| Cloudflare"). No article content. |
| 4 | 4, Unpaywall: lookup | 21:12:15 | `https://api.unpaywall.org/v2/10.1136/rapm-2026-107906?email=reader@example.org` | 200 | 4,052 bytes | JSON metadata record. The placeholder address was accepted. `best_oa_location` is present: `url_for_pdf` is null, `url` is `https://doi.org/10.1136/rapm-2026-107906`, licence "cc-by", version "publishedVersion". |
| 5 | 4, Unpaywall: `best_oa_location.url` | 21:12:23 | `https://doi.org/10.1136/rapm-2026-107906` | **403** | 5,546 bytes | The same refusal as request 3, same redirect target, same size. No article content. |

Five requests in all. Request 5 has the same address as request 3, because the
best open-access location Unpaywall names is the publisher's own page. §5
makes it a separate step of route 4 ("one request to ... its `url` if there is
no PDF address"), so it was sent once, with the same headers as every other
request. It is not a retry with anything altered. This is recorded in the
amendment appended to the registration.

**Full text obtained, as §5 defines it: no.** No route returned the methods
and results as text. Nothing that came back contains any part of the article
body, and none of it was read in place of the full text. The abstract was not
requested and not read by the reader.

## 3. Outcome

**UNSCORABLE (source not obtained).**

Per §5: "If no route returns the full text as defined, the registration is
closed as UNSCORABLE (source not obtained). It is **not** rescued from the
abstract, from a secondary source, or from any other route."

- Steps 3 and 4 of §7 (extract the numbers, apply the rule) were not reached.
- No quotation from the paper and no arithmetic: there is nothing to score.
  D, L and U were not computed. No checking script was needed.
- The primary claim (D ≥ 1.0) is **neither supported nor refuted**. This
  outcome is not a verdict on the claim.

### Registered probabilities, beside the outcome

| Outcome | Registered probability (final version) | Occurred |
|---|---|---|
| SUPPORTED | 0.06 | no |
| REFUTED | 0.01 | no |
| INCONCLUSIVE | 0.07 | no |
| **UNSCORABLE (source not obtained)** | **0.60** | **yes** |
| UNSCORABLE (quantity not reported) | 0.26 | no |

The registered probability of the outcome that occurred is **0.60**. The
registration named it the single likeliest outcome. The step probability
"full text obtained by the declared routes" was 0.40; it was not obtained.

A correct forecast that the source could not be reached says something about
the routes. It says nothing about the paper, the trial or Q-B.

### Secondary quantities (not part of the verdict)

- **S1, time since implant** (prediction: central value at least 24 months,
  probability 0.60): **not readable.** The source was not obtained. This is
  not the registered "not reported" outcome, which needs the paper to have
  been read.
- **S2, whether pre-implant pain is reported in a usable form** (probability
  0.35 that it is, given the full text is obtained): **not readable.** The
  condition "given the full text is obtained" did not occur, so S2 is not
  scored either way.

## 4. The stop rule

"Two registrations that end unscorable for lack of a source mean the programme
cannot generate testable predictions with existing methods, and the question
of closing goes to the owner." (§5)

- **This registration is attempt 1, and it ended unscorable for lack of a
  source. It counts: the count stands at 1 of 2.**
- One more registration ending the same way sends the question of closing to
  the owner.

## 5. What scoring does not show

The limits in §6 of the registration, restated. They were written for a
scored result and hold all the more for an unscored one.

- **One blinded trial,** at one centre, with 20 participants. Whatever a
  verdict had been, it would have been one comparison.
- **Established responders only.** The participants were chosen because the
  therapy still works for them. Nothing here describes people whose benefit
  has faded, and Q-B is about those people.
- **A sham period of limited length.** Five days, after a 24-hour washout.
  Pain over a longer period without stimulation is not measured.
- **Pre-implant pain is likely to be a chart value,** recorded years earlier,
  under different conditions and possibly on a different instrument. The
  comparison is not randomised and not blinded on that side.
- **A SUPPORTED verdict would not have separated** carry-over, natural
  improvement, regression to the mean, selection and expectation. A REFUTED
  verdict would not have shown that the underlying pain is unchanged in any
  one person.
- **Not a statement about any patient.** Group summaries of 20 people say
  nothing about what an individual's pain would be with a device off.
- **Not a stimulation setting,** and not a reason for anyone to change or
  stop a therapy (ETHICS.md §3).
- **A SUPPORTED verdict would have been weak progress at best.** Half of the
  quantity was already known, and the test was not severe.

And for this outcome in particular:

- **UNSCORABLE is not evidence about the claim.** It does not make D ≥ 1.0
  more or less likely.
- **It is not progress** by the test in PROGRAMME.md. No prediction was
  confirmed or refuted.
- **It does not show the paper is unavailable to a person.** It shows that
  four scripted routes, one request each, did not return it on 2026-11-19.

## 6. Not registered: what the requests showed about access

None of this was registered, none of it is about the trial's findings, and
none of it changes the outcome. It is recorded because the stop rule turns on
"lack of a source", and the owner may want to know what kind of lack this was.

- **The metadata describes the paper as open access.** The Unpaywall record
  (request 4) has `is_oa` true, `oa_status` "hybrid", and a publisher location
  with licence "cc-by". That agrees with E-11's note that the abstract states
  a CC BY licence. Europe PMC (request 2) has `isOpenAccess` "N" for the same
  record. The two services disagree.
- **The refusal was of the scripted client, not a paywall page.** Requests 3
  and 5 were stopped by the publisher's access-control service before any
  article page was served. E-11 had already recorded one scripted
  request to the publisher page as refused with HTTP 403, before the
  registration.
- **Unpaywall lists a second location that the registration rules out.** The
  record has `has_repository_copy` true and a repository location (a
  university repository record, version "submittedVersion", licence
  "other-oa"). §5 says of the Unpaywall response: "No other location in the
  response is tried." It was not requested. Whether it holds a readable full
  text is not known.
- **Reading.** The source was not obtained because the closed list of routes
  could not reach it, not because the reader found that no open copy exists.
  A later registration that names a repository route in advance might end
  differently. That is a point about how routes are declared. It is not a
  reason to reopen this registration: its routes were fixed before the read,
  and the outcome stands.

## 7. Where the reader's brief and the registration differed

The reader's brief said that the registration wins wherever the two conflict.
Two small differences, neither affecting the outcome:

- The brief asked the log to say "what came back"; §7 step 2 says "HTTP status
  and size, not content". The log above gives status, size and the kind of
  response, and no content of the article (none was received).
- The brief asked for an arithmetic check by script "if the full text is
  obtained". It was not, so there is no arithmetic and no script.

## 8. Amendment appended to the registration

One amendment was appended under the "Amendments" heading of
`REGISTRATION.md`, after the routes were exhausted. Nothing above the heading
was changed. It records two places where §5 left a choice to the reader (which
Europe PMC flag means "full text", and the Unpaywall address being the same as
route 3's) and that every reading gives the same outcome.
