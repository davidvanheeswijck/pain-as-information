# P-004. Result of attempt 2: UNSCORABLE (source not obtained)

**Written 2026-11-20 by the reader** (Claude Fable 5.2, a language model; a
different session from the one that wrote `REGISTRATION.md`). The reader
followed `REGISTRATION.md` §7, with §4 and §5, in the order written there.

**Outcome: UNSCORABLE (source not obtained).**

**In one paragraph.** None of the five declared routes returned the full
text. PubMed Central and Europe PMC do not hold it. The publisher refused the
scripted request with HTTP 403, as before. The open-access lookup again
listed one repository copy, labelled as the submitted version. The one
request to that copy was answered with HTTP 200 and an HTML page that is an
automated "not a bot" challenge. It holds no link to a file, so the rule
allowed no second request. The paper was not read, no number was extracted,
and the claim "D ≥ 1.0" is neither supported nor refuted. The registration
gave this outcome a probability of 0.48 and named it the single likeliest.
**This is attempt 2 of 2. The stop rule is met, and the question of closing
goes to the owner.**

Nothing here is a statement about any person, and nothing here is a
stimulation setting (ETHICS.md §3).

**On identifiers.** As in the registration, the trial's PubMed number and DOI
are written `[PMID]` and `[DOI]`, and the publisher's host name is written
`[publisher host]`, so that no tool run over this folder fetches the record.
The values are in `evidence/05-crps.md` §6b. The repository address in
request 5 is given as requested; it is not a PubMed number, a DOI or a
registry number.

## 1. Step 1: the registration predates the read

`F` is `predictions/P-004-sham-pain-against-pre-implant-attempt-2/REGISTRATION.md`.
`git fetch origin` was run first; the worktree was already at `origin/main`.

| Commit | Hash | Committer time |
|---|---|---|
| Added `F` | `df9380f18add47f521532d069c6002515dbab0c7` | 2026-11-20T22:06:52+01:00 |
| Last to touch `F` | `2b65ba7c0796304bb8e6a68fa88b9d8dfbafd979` | 2026-11-20T22:15:53+01:00 |
| First-parent commit on `main` that brought it in (merge of pull request 27) | `9ddf580a3ca4322624cc064cac8725cfa4c101a7` | 2026-11-20T22:17:54+01:00 |

The merge commit has two parents (`10e0cfa` and `2b65ba7`): it is a merge
commit, not a squash, and all three branch commits are in the history of
`main`.

**Every commit that touches `F`, oldest first:**

| Hash | Time | Subject | Changes rule text (§4, §5, §7)? |
|---|---|---|---|
| `df9380f` | 22:06:52+01:00 | register attempt 2 of the sham-pain prediction before the source is read | It adds the file. |
| `af1a963` | 22:08:40+01:00 | add the relayed attestation before merge | **No.** One hunk, in the header before §1: the "no attestation was relayed" paragraph is replaced by "Revised before merge" and the attestation. Checked with `git diff df9380f af1a963 -- F`. |
| `2b65ba7` | 22:15:53+01:00 | make route 5 step (b) deterministic after review | **Yes.** Rule text in §5 (route 5 step (b), the kind-of-failure record, the PDF text rule), the restated probabilities in §4, and the logging in §7 step 2. It also changed `registration_checks.py`. |

No commit touches `F` after the merge. The "Amendments" section reads "None."

**Binding time:** the latest of the merge commit and every commit that
changes rule text, which is the merge commit:
**2026-11-20T22:17:54+01:00, that is 21:17:54Z.**

**Start of step 2:** the reader's clock read 21:18:36Z after step 1's
commands. The first request about the paper was sent at **21:19:38Z**, 1
minute 44 seconds after the binding time. The read started after the binding
time.

**Exposure.** The reader made no request about the paper before 21:19:38Z
and has no recollection of the paper beyond what this repository says. The
brief given to the reader contained nothing from the paper. Before the first
request the reader read `REGISTRATION.md` in full, `registration_checks.py`,
and the citation line of `evidence/05-crps.md` §6b with the heading above it
(for the identifiers). The reader did not open P-003's `RESULT.md`. The same
limit as in the registration applies and cannot be removed: the reader is a
language model whose training data reach mid-2026, and the paper was
published in May 2026.

**`python3 registration_checks.py carried`** (exit status 0):

```
ok    the quantity: 6 lines, 347 bytes, identical
ok    primary claim and verdict rule: 60 lines, 2925 bytes, identical
ok    verdict rule alone: 37 lines, 1755 bytes, identical
ok    reachability, as in P-003: 32 lines, 1791 bytes, identical
ok    scoring rule (methods A, B, C; construct; widenings; special cases): 140 lines, 8197 bytes, identical
ok    secondary quantities: 15 lines, 831 bytes, identical
ok    request conditions and routes 1 to 4: 32 lines, 2033 bytes, identical
ok    what full text obtained means: 10 lines, 613 bytes, identical
ok    the outcomes: 11 lines, 619 bytes, identical
ok    the stop rule sentence: 3 lines, 188 bytes, identical
ok    what scoring does not show: 23 lines, 1444 bytes, identical
```

**`python3 registration_checks.py selftest`** (exit status 0):

```
caught  the quantity: byte 174 of the block changed 'B' -> 'X'; inner check exit 1
caught  primary claim and verdict rule: byte 1464 of the block changed 'i' -> 'X'; inner check exit 1
caught  verdict rule alone: byte 878 of the block changed '0' -> 'X'; inner check exit 1
caught  reachability, as in P-003: byte 896 of the block changed '0' -> 'X'; inner check exit 1
caught  scoring rule (methods A, B, C; construct; widenings; special cases): byte 4101 of the block changed '1' -> 'X'; inner check exit 1
caught  secondary quantities: byte 415 of the block changed 'n' -> 'X'; inner check exit 1
caught  request conditions and routes 1 to 4: byte 1016 of the block changed 'e' -> 'X'; inner check exit 1
caught  what full text obtained means: byte 306 of the block changed 't' -> 'X'; inner check exit 1
caught  the outcomes: byte 310 of the block changed 't' -> 'X'; inner check exit 1
caught  the stop rule sentence: byte 94 of the block changed 'e' -> 'X'; inner check exit 1
caught  what scoring does not show: byte 723 of the block changed 's' -> 'X'; inner check exit 1
file on disk unchanged: True
PASS  11 of 11 one-character mutations caught
```

The carried blocks are identical to P-003's, and the check that says so can
fail.

## 2. Step 2: the access log

**How the requests were made.** Each request was sent by
`reader_routes.py get` in this folder (Python 3.15.2, `urllib`, standard
library only): the user-agent `research-reader/1.0 (scripted; one request per
step)`, no cookie handling, no other header chosen by the reader, redirects
followed inside the request, a 60-second timeout. Every request got an HTTP
response, so the identical-repeat rule was never used. Nothing was retried.
**Five requests were sent in all.** Times are UTC, 2026-11-20.

| # | Route and step (§5) | Time | Address requested | HTTP status | Content-Type | Final address | Size | What came back (kind, not content) |
|---|---|---|---|---|---|---|---|---|
| 1 | 1, PubMed Central: `elink` | 21:19:38Z | `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&db=pmc&id=[PMID]` | 200 | `text/xml; charset=UTF-8` | same | 326 bytes | XML link result with an empty link set: no PMC identifier. |
| – | 1: `efetch` | – | – | – | – | – | – | **Not sent.** Its condition (a PMC identifier) was not met. |
| 2 | 2, Europe PMC: `search` | 21:19:43Z | `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A[PMID]%20AND%20SRC%3AMED&resultType=lite&format=json` | 200 | `application/json;charset=UTF-8` | same | 1,089 bytes | JSON, one record. Flags: `inEPMC` "N", `inPMC` "N", `isOpenAccess` "N", `hasPDF` "N". None of the four is "Y": not flagged as having full text. `pmcid` absent. (`hasTextMinedTerms` "Y", ignored as §5 says.) |
| – | 2: `fullTextXML` | – | – | – | – | – | – | **Not sent.** The record is not flagged. |
| 3 | 3, publisher: `doi.org` | 21:19:54Z | `https://doi.org/[DOI]` | **403** | `text/html; charset=UTF-8` | `https://[publisher host]/lookup/doi/[DOI]` (one 302 hop) | 5,546 bytes | An HTML refusal page from the publisher's access-control service (page title "Attention Required! \| Cloudflare"). No article content. |
| 4 | 4, Unpaywall: lookup | 21:19:58Z | `https://api.unpaywall.org/v2/[DOI]?email=reader@example.org` | 200 | `application/json` | same | 4,070 bytes | JSON metadata record. The placeholder address was accepted. `best_oa_location`: `url_for_pdf` null, `url` `https://doi.org/[DOI]`, `license` "cc-by", `version` "publishedVersion". |
| – | 4: best location | – | `https://doi.org/[DOI]` | – | – | – | – | **Skipped.** `url_for_pdf` is null, so the address is `url`. It is the same string as the address requested in route 3 (compared character by character: equal). By the clarification to route 4 the step is skipped, not repeated. Route 4 ends with no full text. |
| 5 | 5, repository entry 1 of 1: step (a) | 21:20:04Z | `http://urn.kb.se/resolve?urn=urn:nbn:se:umu:diva-253252` | 200 | `text/html; charset=utf-8` | `https://umu.diva-portal.org/smash/record.jsf?pid=diva2:2060352` (one 302 hop) | 7,092 bytes | An HTML page. By §5 it is treated as a landing page. See below. |
| – | 5, entry 1: step (b) | – | – | – | – | – | – | **Not sent.** No candidate link remained. The entry ends with no second request. |

### Route 5 in detail

- **The lookup response used:** request 4, and no other. No new lookup was
  made.
- **Repository entries in `oa_locations`:** the list has 2 entries. Entry 0
  has `host_type` "publisher" (it is the best location). **One** entry has
  `host_type` "repository".
- **That entry:** position 1 in `oa_locations` (the second of two, counting
  from 0). `version`: **"submittedVersion"**. `license`: "other-oa".
  `repository_institution`: "Umeå University". `url_for_pdf`: null.
  **Address field used: `url`.**
- **Step (a):** the address was not one already requested in this attempt.
  Response: HTTP 200, `Content-Type` `text/html; charset=utf-8`, final address
  as in the table. The page is not the full text: it holds no part of any
  article. It is therefore "an HTML landing page" as §5 defines one, and step
  (b) was applied to it.
- **Step (b), the selection,** run with `reader_routes.py select` on the saved
  body (`html.parser`, start tags only, body decoded as UTF-8 as the header
  names, links resolved against the final address of (a)):
  - links found, in document order: **5** (one `link` element, a stylesheet;
    four `a` elements, all to other sites);
  - links that qualify as pointing to a PDF or full-text file: **0** (no path
    ends in `.pdf`, none contains `fulltext`, no element declares
    `type="application/pdf"`, and there is no `citation_pdf_url` element);
  - links excluded: **0**, since none qualified;
  - **no candidate remained. No second request was sent. The entry ended.**
- **Entries exhausted.** Route 5 ended with no full text.

**Reader's note on the page. It changes no record.** The page returned in
request 5 is an automated challenge, not the repository's record page. Its
title is "Making sure you're not a bot!". It asks the client to run a script
(a proof-of-work calculation) before the site is shown. The registration
foresaw this case (§5, "A limit of that definition") and says what to do: the
page is treated as a landing page, step (b) is applied, and the kind of
failure is recorded from the HTTP status alone. One `a` element on the page
sits inside a `script` element; by the parser rule it is not a link, and it
would not have qualified in any case. The page echoes request metadata of
the client; none of it is copied here.

### Full text obtained, as §5 defines it: no

No route returned the methods and results as text. Nothing that came back
contains any part of the article body, and nothing was read in place of the
full text. The abstract was not requested and not read. The lookup records
(requests 2 and 4) carry bibliographic fields; the reader printed only the
access fields listed above.

## 3. Steps 3 to 5: not reached

- **Version label and extraction tool (step 3):** no copy was obtained. The
  lookup labels the listed repository copy "submittedVersion"; that label was
  never applied to a text. No PDF was downloaded. `pdftotext` and `pypdf`
  were not run and not installed. There are no word counts.
- **Numbers (step 4):** none extracted. There are no quotations.
- **Scoring (step 5):** not applied. No method (A, B or C), no widening and
  no special case was reached. There is no D, L or U and no arithmetic.
- **Secondary quantities:** S1 (time since implant): **not readable**, the
  source was not obtained. S2 (whether pre-implant pain is reported in a
  usable form): **not readable**, for the same reason. Neither is scored.

## 4. The verdict, beside the registered probabilities

**UNSCORABLE (source not obtained).** By §5 it is not rescued from the
abstract, from a secondary source or from any other route.

| Outcome | Registered probability, overall (§4) | Occurred |
|---|---|---|
| SUPPORTED | 0.05 | no |
| REFUTED | 0.01 | no |
| INCONCLUSIVE | 0.12 | no |
| **UNSCORABLE (source not obtained)** | **0.48** | **yes** |
| UNSCORABLE (quantity not reported) | 0.34 | no |

- **Registered probability of the outcome that occurred: 0.48.** It was the
  single likeliest outcome in the registration.
- The registration put 0.52 on the full text being obtained. It was not.
- **Where the chain broke, against the registered factors for route 5**
  (§4, step 1): the lookup answered the placeholder address again (registered
  at 0.95: it did); the response still listed the repository entry (0.98: it
  did); **the repository answers a scripted client and does not block it
  (0.85): it did not.** The two later factors were never tested.
- One case says little about calibration, as the registration says of P-003.

## 5. The kind of failure (§5, "recorded separately")

The record rests on the HTTP status alone, as §5 requires.

| Route and step | Record |
|---|---|
| 1, `elink` | "no full text in any response" (the service answered; no identifier) |
| 1, `efetch` | skipped (not sent: no PMC identifier) |
| 2, `search` | "no full text in any response" (the service answered; not flagged) |
| 2, `fullTextXML` | skipped (not sent: not flagged) |
| 3, `doi.org` | **"a route was refused by a bot block"** (HTTP 403) |
| 4, lookup | "no full text in any response" (a metadata record) |
| 4, best location | skipped (same address as route 3) |
| 5, entry 1, step (a) | "no full text in any response" (HTTP 200; a landing page by §5, with no candidate link) |
| 5, entry 1, step (b) | skipped (not sent: no candidate remained) |

**Overall record: "a route was refused by a bot block" (route 3).** At least
one step was of that kind.

**What the record undercounts, as §5 says it can.** Route 5's entry is
recorded as "no full text in any response" because its status was 200 and no
non-200 refusal was received for that entry. In substance the response was an
automated challenge to the scripted client (the note in §2). §5 declares this
limit in advance: "A bot block served with status 200 is therefore recorded
as the wrong kind." The record above is the mechanical one. This paragraph is
the reader's note, and it changes no record.

Read with that note: routes 1 and 2 show that two open archives do not hold
the paper; routes 3, 4 and 5 show that both places listed as holding a copy
turned the scripted client away, one with a 403 and one with a challenge
page.

## 6. The stop rule

The rule (§5, carried from P-003): "Two registrations that end unscorable for
lack of a source mean the programme cannot generate testable predictions with
existing methods, and the question of closing goes to the owner."

- P-003 was attempt 1 and ended UNSCORABLE (source not obtained).
- This registration is attempt 2 and ends UNSCORABLE (source not obtained).
- **The count stands at 2 of 2. The stop rule is met. The question of
  closing the programme goes to the owner.**
- The reader does nothing further about it. Closing is the owner's decision,
  not the reader's.

## 7. Caveats, restated

From §6 of the registration, as they bear on this outcome:

- **No verdict was reached.** "D ≥ 1.0" is neither supported nor refuted.
  Nothing in this file is evidence for or against the claim.
- **Failing again does not show that the paper cannot be had.** It shows
  that five scripted routes, with at most two requests per repository entry,
  did not return it. The lookup still describes the paper as open access
  (`is_oa` true, `oa_status` "hybrid", a publisher location with licence
  "cc-by") and still lists a repository copy.
- **The stop rule does not distinguish kinds of failure** (§8, item 1). "No
  open copy exists" and "the declared routes could not reach one" count the
  same. This outcome is of the second kind, and §5 above records it.
- **Had a verdict been reached, it would have been limited** in the ways §6
  lists: one blinded trial at one centre with 20 participants; established
  responders only; a five-day sham period after a 24-hour washout; a
  pre-implant score that is likely a chart value; a test that is not severe,
  with half of the quantity already known; and a copy labelled as the
  submitted version, with a wider interval for that reason.
- **Not a statement about any patient,** not a stimulation setting, and not
  a reason for anyone to change or stop a therapy (ETHICS.md §3).
- **By the test in PROGRAMME.md this is not progress.** No prediction has
  yet been scored against unread data.

## 8. Rules that left the reader a choice

No amendment was appended to `REGISTRATION.md`. No rule was ambiguous in a
way that could change the outcome. Three places left the reader a small
choice, recorded here so that they are not lost. Every reading gives
UNSCORABLE (source not obtained).

1. **The exact addresses of routes 1 and 2.** §5 names the services and the
   parameters (`elink` to `db=pmc`; `search` with `resultType=lite` and
   `format=json`) and not the full query strings. The reader used the forms
   in the table. Both responses have the same sizes as the registration
   quotes for attempt 1 (326 and 1,089 bytes).
2. **`type="application/pdf"`, letter case.** §5 says letter case is ignored
   for the path tests and does not say so for this attribute.
   `reader_routes.py` compares it exactly. No link on the page had a `type`
   attribute, so both readings give the same selection.
3. **"Position in `oa_locations`".** Counted from 0 here (position 1, the
   second of two entries). There is one repository entry, so the order rule
   had nothing to decide.

## 9. Not registered: what the requests showed about access

None of this was registered, none of it is about the trial's findings, and
none of it changes the outcome.

- **The lookup record is as attempt 1 reported it,** 18 bytes longer (4,070
  against 4,052). Open-access status, best location, licence and the
  repository entry's version label are unchanged.
- **The repository entry has no PDF address.** Its `url_for_pdf` is null and
  its `url` is a national resolver address that redirects to the record page
  of a university publication portal. The lookup therefore does not itself
  say that a file is attached to the record. Whether one is, was not learned.
- **The portal put a script challenge in front of its record page.** A
  client that does not run scripts gets the challenge with status 200 and
  nothing else. No declared route could pass it, and the registration forbids
  any other client.
- **Reading.** For the second time the source was not obtained because the
  declared routes could not reach it, not because the reader found that no
  open copy exists. Both failures turn on scripted access being turned away.
  That is a point about the method of access. It is not a reason to reopen
  this registration: its routes were fixed before the read, and the outcome
  stands.

## 10. Files

- `reader_routes.py`, in this folder: the one-request tool and the route 5
  step (b) selection, with a self-test (`python3 -I reader_routes.py
  selftest`, 7 of 7 pass). It holds no identifier of the paper.
- The five saved responses and the machine-readable log are in the reader's
  scratch folder and are not committed. No PDF and no text of the paper
  exists there, since none was obtained.
- `ledger/OPEN.md` and the evidence briefs are not changed in this pull
  request. A ledger line is proposed in the reader's report.
