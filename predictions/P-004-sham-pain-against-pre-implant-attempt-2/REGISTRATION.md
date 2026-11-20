# P-004. Registered prediction, attempt 2: pain under blinded sham against pain before implant

**Written 2026-11-20, before the source was read.** The source is the same
paper as in P-003: the sham-controlled crossover trial of ganglion stimulation
in established responders, Tabatabaei et al. 2026 (identifiers in
`evidence/05-crps.md`, §6b, and in
`predictions/P-003-sham-pain-against-pre-implant/RESULT.md`). This file names
the trial by pointer only. It carries no PubMed number, no DOI and no registry
number, so that no tool run over this folder fetches its record.

Intent: `intent/programme/2026-11-19-pivot-to-evidence-appraisal.md`. This is
still step 2 of D-003 (`ledger/DECISIONS.md`): one prediction registered
against data not yet read, then scored. The owner approved a second attempt on
the same unread paper, with the repository route declared in advance, on
2026-11-20 (recorded in the intent file).

**On the number.** "P-004" continues the folder numbering after P-003. It is
**not** candidate P-4 of `evidence/11-evidence-map.md` and `ledger/OPEN.md`
(the block study). It is candidate P-3 again.

Two agents, two jobs. The registering agent (Claude Fable 5.2, a language
model) wrote this file from the repository alone and stops here. A different
agent reads the source later and writes `RESULT.md`. If the paper disagrees
with this file, the paper is right and this file is the record of the
registering agent being wrong.

Nothing here is a statement about any person, and nothing here is a stimulation
setting (ETHICS.md §3).

> **Read this first. Five limits of this registration.**
>
> 1. **It predicts one unread number.** Pain under sham in this trial is
>    already in the repository, from the abstract (median 6.0). The only
>    unread half of the quantity is the participants' pain before implant.
> 2. **The test is not severe.** A SUPPORTED verdict would mostly reflect that
>    people are implanted when their pain scores are high. REFUTED is the
>    informative outcome.
> 3. **The informative outcome is harder to reach in this attempt than in
>    P-003.** A copy obtained by the new route is expected to be the submitted
>    version, which widens the interval by 0.5 on each side. At that likely
>    total widening of 0.5, with the synthetic spreads of §4 and method (C),
>    REFUTED needs D below about 0.03 (0.033 before rounding), that is,
>    pre-implant pain at or below the sham level. In P-003, with no widening,
>    it needed D ≤ 0.5. SUPPORTED needs D above 1.97 (1.967), against 1.47
>    (1.467) in P-003. **At the maximum total widening of 2.0 the rule is
>    close to uninformative:** SUPPORTED needs D above 3.47 (3.467) and
>    REFUTED needs D below −1.47 (−1.467), so nearly every plausible paper
>    would be INCONCLUSIVE. These thresholds are rounded to two decimals; the
>    figures in brackets are the same values to three.
> 4. **The registered likeliest outcome is still UNSCORABLE.** The
>    registering agent puts 0.82 on the registration ending unscorable (0.48
>    because the full text is not obtained, 0.34 because pre-implant pain is
>    not reported in a usable form), and 0.18 on any verdict. The single
>    likeliest outcome is UNSCORABLE (source not obtained), at 0.48. If a
>    verdict is reached, the likeliest is INCONCLUSIVE (0.12 overall).
> 5. **This is attempt 2 of 2 under the stop rule.** If it ends UNSCORABLE
>    (source not obtained), the stop rule is met and the question of closing
>    the programme goes to the owner (§5).

**What is new here, in one sentence.** The claim, the quantity and every
scoring rule are those of P-003, copied below word for word; the only
substantive change is the list of routes by which the source may be obtained
(§5), with the version rule and the PDF text rule that a repository route
needs.

**Merge.** The pull request that adds this file is to be merged with a merge
commit, not a squash, so that every commit on its branch stays in the history
of `main`. From the merge onwards the file is append-only.

**Revised before merge.** This file was first committed at `df9380f`. It was
revised twice on the same branch, each time before the merge and before any
read of the source. Neither revision followed any information about the
paper.

- *First revision, `af1a963`.* The first version said that no attestation had
  been relayed; the attestation below was then relayed and added. Two limits
  listed in §8 (items 4 and 5) were put to the coordinating session, which
  decided to leave them as written. No rule text in §4, §5 or §7 changed.
- *Second revision, the commit after `af1a963`, after a review of the pull
  request.* The review found no leak and confirmed the carried rules
  identical. **Rule text in §5 changed before merge:**
  - route 5, step (b), was rewritten so that it is deterministic (which
    links are candidates, which are excluded, the parser, how addresses are
    resolved and compared, and what counts as an HTML landing page);
  - the kind-of-failure record now rests on the HTTP status alone;
  - the PDF text rule gained a word-count method, a note on column order,
    and a second extraction with the fallback tool when the first yields too
    little text.

  Outside §5: the box above gained limit 3; the band thresholds are said to
  be rounded; the publisher's host name is masked in one quotation in §2;
  `registration_checks.py` gained a self-test; reader step 2 logs more; and
  the probabilities in §4 were restated (the earlier figures are kept
  there). The carried P-003 blocks were not touched.

**Attestation by the coordinating session, recorded as relayed.** "The
coordinating session attests that, up to the merge of this registration, no
session whose output it has seen has read the paper's
abstract-beyond-what-the-repository-quotes or its full text; the P-003
reader's requests returned no full text and its report shows none." The
registering agent cannot check this and records it as given. What the P-003
reader reports about its own exposure is quoted in §1. The registering
agent's own statement is in §2.

## 1. Relation to P-003, and the question

### The same paper, the same quantity, the same claim

- **Paper:** the one P-003 registered against. It has still not been read.
- **Quantity:** D, as P-003 defines it. The definition is copied here
  unchanged:

**The quantity.** Pain under blinded sham stimulation, in people who are
established responders, set against the same participants' pain before the
stimulator was implanted. Both on the 11-point scale (0 to 10).

Write **D = pre-implant pain minus pain under sham**, in points. D is positive
when pain under sham is lower than pain before implant.

- **Claim:** D ≥ 1.0 (§4, copied unchanged).
- **Rules:** the verdict rule, methods (A), (B) and (C), the construct rule,
  the widenings and the order of precedence among them are those of P-003.
  They are carried into §4 and §5 of this file **verbatim**, so that this
  file stands alone. **Nothing in those rules is changed.**
- **Proof of that.** `registration_checks.py carried`, in this folder, takes
  each carried block from
  `predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md` and
  checks that it is present in this file byte for byte. A reader who finds a
  difference between a carried block here and P-003's text should treat
  P-003's text as the rule and record the difference.
- **Section numbers are kept** (§2 prior exposure, §3 reasoning, §4 the
  prediction, §5 unscorable conditions, §6 limits, §7 reader), so that every
  cross-reference inside a carried block points to the right place in this
  file.
- **Why the question bears on Q-B, and what each outcome would and would not
  suggest:** P-003 §1, unchanged, and not repeated here.

### What is added, all of it in §5

- A fifth route (repository copies), with two clarifications to routes 2 and
  4 taken from P-003's Amendment 1.
- A version rule, because a repository copy may not be the published version.
  It adds one widening to the interval. That is the only place where the new
  material touches scoring, and it can only make the interval wider.
- A PDF text rule.
- A record, with no effect on any rule, of what kind of failure it was if the
  source is again not obtained.

### Why a second registration against the same paper is legitimate

**The paper was not read in attempt 1.** The outcome of P-003 was about
routes, not about the paper. P-003's `RESULT.md` summarises its request log
like this (quoted in full; the block holds no PubMed number, DOI, registry
number or host name):

> **In one paragraph.** None of the four declared routes returned the full
> text. PubMed Central and Europe PMC do not hold it. The publisher refused
> the scripted request twice with HTTP 403. The paper was therefore not read,
> no number was extracted, and the claim "D ≥ 1.0" is neither supported nor
> refuted. The registration gave this outcome a probability of 0.60 and named
> it the single likeliest. This is attempt 1 under the two-unscorable stop
> rule.

and, under its access log:

> **Full text obtained, as §5 defines it: no.** No route returned the methods
> and results as text. Nothing that came back contains any part of the article
> body, and none of it was read in place of the full text. The abstract was not
> requested and not read by the reader.

and, in its §1:

> The reader made no request about the
> paper before 21:11:58Z and has no recollection of the paper beyond what this
> repository says. The brief given to the reader contained nothing from the
> paper.

**So, per the P-003 reader's own report, no result, no abstract and no full
text of the paper was seen by that reader.** The registering agent of this
file cannot check that report and records it as given.

**What attempt 1 exposed.** Access metadata only: which services hold the
paper, what the publisher's access-control service did to a scripted request,
and what the open-access lookup says about where copies are and under which
licence and version label. All of it is listed in §2. P-003's `RESULT.md` §6,
quoted in full:

> ## 6. Not registered: what the requests showed about access
>
> None of this was registered, none of it is about the trial's findings, and
> none of it changes the outcome. It is recorded because the stop rule turns on
> "lack of a source", and the owner may want to know what kind of lack this was.
>
> - **The metadata describes the paper as open access.** The Unpaywall record
>   (request 4) has `is_oa` true, `oa_status` "hybrid", and a publisher location
>   with licence "cc-by". That agrees with E-11's note that the abstract states
>   a CC BY licence. Europe PMC (request 2) has `isOpenAccess` "N" for the same
>   record. The two services disagree.
> - **The refusal was of the scripted client, not a paywall page.** Requests 3
>   and 5 were stopped by the publisher's access-control service before any
>   article page was served. E-11 had already recorded one scripted
>   request to the publisher page as refused with HTTP 403, before the
>   registration.
> - **Unpaywall lists a second location that the registration rules out.** The
>   record has `has_repository_copy` true and a repository location (a
>   university repository record, version "submittedVersion", licence
>   "other-oa"). §5 says of the Unpaywall response: "No other location in the
>   response is tried." It was not requested. Whether it holds a readable full
>   text is not known.
> - **Reading.** The source was not obtained because the closed list of routes
>   could not reach it, not because the reader found that no open copy exists.
>   A later registration that names a repository route in advance might end
>   differently. That is a point about how routes are declared. It is not a
>   reason to reopen this registration: its routes were fixed before the read,
>   and the outcome stands.

**What attempt 1 did not expose.** Any number, table, sentence or figure of
the paper; whether the paper reports pre-implant pain; its value; time since
implant. The prediction in §4 is therefore made with the same knowledge of
the trial's findings as in P-003, which is the abstract-level record in P-003
§2.

**What a second attempt costs in credibility, said plainly.**

- The route list is being widened after a failure, and with knowledge of
  which extra route is likely to exist. That is why the routes are fixed here
  before any further request, why the claim and the rules are not touched, and
  why the stop rule counts this as attempt 2 and not as a fresh attempt 1.
- P-003's outcome stands as recorded. This registration does not reopen it
  and does not rescue it.
- Widening the routes cannot make any verdict on D more likely than another.
  It only changes whether a verdict is reached, and the version rule makes a
  verdict reached this way less sharp, not more.

## 2. Prior exposure

**P-003 §2 stands unchanged and is the prior exposure of this registration
too.** It quotes everything the repository said about the trial at commit
`dfd9804`. It is not copied here, because it is not rule text and because its
quotations sit beside the identifiers this file leaves out. The summary under
"What is therefore already known" in P-003 §2 is what §3 and §4 below rely
on: one centre; 20 established responders; two 5-day periods with a 24-hour
washout; median 3.0 (IQR 2.0 to 4.0) under active stimulation against median
6.0 (IQR 4.0 to 7.0) under sham; pre-implant pain not known.

### What the repository has gained since, found at commit `10e0cfa`

`git diff --stat dfd9804 10e0cfa` lists six files: the P-003 registration
(with its Amendment 1) and result, `predictions/README.md`, `ledger/OPEN.md`,
the intent file and the generated `docs/index.html`. `predictions/README.md`
and `docs/index.html` say nothing about the trial. The intent file gained the
owner's approval of P-003 and a pointer to it. Everything else that is new is
below.

In the quotations, the trial's PubMed number and DOI are replaced by `[PMID]`
and `[DOI]`, and the publisher's host name in one redirect address is
replaced by `[publisher host]`. Those are the only changes. What remains
unmasked, here and in the rest of this file: the first author's name and the
year, the name of the centre, the names of the lookup services and their
public addresses, and the title of the publisher's refusal page. None of
these is an identifier of the paper that a tool could resolve. The masked
values are in P-003's `RESULT.md`.

**P-003 `RESULT.md`, §2, the access log.** The columns "Time" and "Address
requested" are left out here because the addresses carry the identifiers. The
other cells are quoted as they stand:

> | # | Route (§5) | HTTP status | Size | What came back (kind, not content) |
> |---|---|---|---|---|
> | 1 | 1, PubMed Central: `elink` | 200 | 326 bytes | XML link result with an empty link set: no PMC identifier. No `efetch` request follows. |
> | 2 | 2, Europe PMC: `search` | 200 | 1,089 bytes | JSON, one record, bibliographic fields and flags only (the `lite` result type carries no abstract). Flags: `inEPMC` "N", `inPMC` "N", `isOpenAccess` "N", `hasPDF` "N". Not flagged as having full text. No `fullTextXML` request follows. |
> | 3 | 3, publisher: `doi.org` | **403** | 5,546 bytes | Redirected to `https://[publisher host]/lookup/doi/[DOI]`. An HTML refusal page from the publisher's access-control service (page title "Attention Required! \| Cloudflare"). No article content. |
> | 4 | 4, Unpaywall: lookup | 200 | 4,052 bytes | JSON metadata record. The placeholder address was accepted. `best_oa_location` is present: `url_for_pdf` is null, `url` is `https://doi.org/[DOI]`, licence "cc-by", version "publishedVersion". |
> | 5 | 4, Unpaywall: `best_oa_location.url` | **403** | 5,546 bytes | The same refusal as request 3, same redirect target, same size. No article content. |

**The lookup metadata fields, as P-003 `RESULT.md` reports them.** These are
the new facts this registration uses. Each is quoted from the passages above
or from §6 of that file (quoted in full in §1):

| Field | Reported value, verbatim |
|---|---|
| Open-access status | "`is_oa` true, `oa_status` "hybrid"" |
| Licence, publisher location | "a publisher location with licence "cc-by"" |
| Best location | "`url_for_pdf` is null, `url` is `https://doi.org/[DOI]`, licence "cc-by", version "publishedVersion"" |
| That a repository copy exists | "`has_repository_copy` true and a repository location" |
| The repository copy | "a university repository record, version "submittedVersion", licence "other-oa"" |
| Whether it was requested | "It was not requested. Whether it holds a readable full text is not known." |
| The lookup's treatment of the placeholder address | "The placeholder address was accepted." |
| Europe PMC flags | "`inEPMC` "N", `inPMC` "N", `isOpenAccess` "N", `hasPDF` "N"" |

**P-003 `REGISTRATION.md`, Amendment 1** (written by the reader after the
routes were exhausted), the parts that add anything:

> The record also has `hasTextMinedTerms` "Y". The reader
> does not take that as a full-text flag, since it can be set from an
> abstract alone, and the record has no PMC identifier for a `fullTextXML`
> address.

> **Observed, for whoever writes the next registration.** The Unpaywall response
> also listed a repository location. §5 says "No other location in the response
> is tried", and it was not requested.

**`ledger/OPEN.md`, "What the programme does next", the P-003 entry:**

> - **What the outcome does not show.** It is a statement about the declared routes, not about availability. The open-access lookup lists a repository copy of the paper, which the registration's closed route list did not allow. The stop rule does not distinguish "no open copy exists" from "the declared routes could not reach one".
> - **Standing.** No prediction has yet been scored against unread data.

### What is therefore known about access, and what is not

- **Known.** The paper is not in PubMed Central. Europe PMC does not flag it
  as full text. The publisher's page refuses this scripted client (three
  times now: once before P-003, twice in it). The open-access lookup accepted
  the placeholder address once, describes the paper as open access, and lists
  a repository copy at a university repository, labelled as the submitted
  version, licence "other-oa".
- **Not known to the registering agent.** The repository's name, host or
  address (the repository does not record them). Whether the lookup entry has
  a `url_for_pdf` or only a landing-page `url`. How many repository entries
  the response lists. Whether a file is attached to the repository record,
  whether it is under embargo, and in what format it is. Whether the
  repository answers a scripted client. Whether the submitted version reports
  pre-implant pain, or differs in any number from the published paper.
- **Still not known:** everything P-003 §2 lists as not known, starting with
  whether the paper reports pre-implant pain at all.

### What the registering agent read, and did not

- Read, in this repository only, on 2026-11-20 at commit `10e0cfa`:
  `predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md` in full,
  including Amendment 1; `predictions/P-003-sham-pain-against-pre-implant/RESULT.md`
  in full; `ledger/OPEN.md` in full; `PROGRAMME.md`, "Progressive or
  degenerating" and "The programme from 2026-11-19"; the intent file;
  `predictions/README.md`; `.github/workflows/ci.yml`; `.gitignore`; and the
  argument lists of `tools/build-dashboard.py` and `tools/lint-privacy.py`.
- **Read nothing else about the trial.** No full text, abstract, PubMed,
  Crossref, publisher, repository, preprint or registry page was fetched,
  opened or searched for. The university repository copy was not opened and
  its address is not known to the registering agent. The only network
  requests in the registering session were `git` and `gh` against this
  repository. `tools/verify-citations.py` was not run.
- **The evidence briefs were not re-read.** The registering agent relies on
  P-003 §2 for what they say about the trial.
- **A limit that cannot be removed,** as in P-003. The registering agent is a
  language model whose training data reach mid-2026, and the paper was
  published in May 2026. The agent has no recollection of the paper beyond
  what the repository says, and it cannot prove that nothing about it was in
  its training data.
- The registering agent was given no result of the paper by any other
  session. Its brief contained nothing from the paper.

## 3. The reasoning

**P-003 §3 stands unchanged and is the reasoning for this claim.** Nothing
about the trial has been learned since it was written, so there is nothing to
add to it. In brief, from what the repository holds:

- The one direct precedent (the first Düsseldorf trial, E-11 row B9) found
  pain under sham equal to pain before implant: D of zero. If Umeå repeats
  that, the claim is refuted.
- Four things argue against a repeat: the known sham median of 6.0 is low for
  a pre-implant score in the cohorts the repository records (both above 8);
  the entry criterion of at least 50% relief, with an active median of 3.0,
  bounds pre-implant pain from below; the second Düsseldorf trial did not
  find the equality again; and every listed bias but rebound pushes D
  upwards.
- **What is expected, unchanged:** a pre-implant median of 7 to 8, so D
  between 1 and 2, most likely 1.5 to 2.
- **Severity (EPISTEMICS.md §7), unchanged:** this is not a severe test of any
  mechanism. If it comes out SUPPORTED, the likeliest reason is the base rate.
  The informative outcome would be REFUTED.

**What is most likely overall** is again that the registration ends
unscorable. §4 gives the numbers and the reasons.

## 4. The prediction

Everything from "Primary claim" to the end of "Secondary quantities" is P-003
§4, carried verbatim, with two insertions that are marked as new: "Reachability
with the version widening" and "The version widening". The probabilities at the
end are restated.

### Primary claim

**In the Umeå trial, the participants' pain under blinded sham is at least 1.0
point below their pain before implant, on the 11-point scale: D ≥ 1.0.**

Direction: sham below pre-implant. Threshold: 1.0 point.

**The threshold is chosen, not derived.** Nothing in the repository yields
1.0. It was picked by the registering agent as the smallest gap it would call
"clearly below", midway between two reference values that the rule also uses:

- 0, no difference, which is the Piedade 2022 result (E-11 row B9);
- 2.0, the figure the repository uses as the usual minimum clinically
  important difference on this scale: "below the usual 2-point MCID"
  (`evidence/03-writing-the-signal.md` §1, "The systematic reviews", on a
  10-point scale) and "the usual 2-point or 30% minimum clinically important
  difference" (same file, §5, "Botulinum toxin A").

The threshold is lower than what §3 expects (D of 1.5 to 2). The claim is
therefore easier to meet than the registering agent's own expectation, and
that is declared. With the interval rule below and the spreads expected, the
claim is in practice supported only from about D = 1.5 upwards.

### Verdict rule

Let D be the point estimate and [L, U] its 95% interval, both obtained as set
out under "Scoring rule". Checked in this order:

1. **SUPPORTED** if D ≥ 1.0 **and** L > 0.
   The estimate meets the threshold and "no difference" is excluded.
2. **REFUTED** if U < 1.0, **or** if D ≤ 0.5 **and** U < 2.0.
   Either the whole interval is below the threshold, or the estimate is at
   most half a point and a two-point gap is excluded.
3. **INCONCLUSIVE** otherwise.

**The boundaries, stated plainly.**

- An estimate of 1.0 or more is SUPPORTED or INCONCLUSIVE. It is never
  REFUTED.
- An estimate above 0.5 and below 1.0 is REFUTED only if U < 1.0. Otherwise
  it is INCONCLUSIVE. It is never SUPPORTED.
- An estimate of 0.5 or less is REFUTED if U < 2.0, and INCONCLUSIVE
  otherwise.
- REFUTED can hold with L > 0 (for example D = 0.4 with an interval of 0.1 to
  0.7). Sham pain is then reliably below pre-implant pain, and by less than
  the claimed point. That is a refutation of "at least 1.0".
- The cut-offs are still sharp at D = 1.0 against INCONCLUSIVE, at D = 0.5,
  and at the interval bounds. A sharp rule is the price of a mechanical one.

**The wording that goes with REFUTED.** If the verdict is REFUTED,
`RESULT.md` adds exactly one of these four phrases, the first that applies:

1. U < 0: "above the pre-implant level".
2. U < 1.0 and L > 0: "below the pre-implant level, by less than a point".
3. U < 1.0 and L ≤ 0: "at about the pre-implant level".
4. Otherwise (the verdict rests on D ≤ 0.5 with U < 2.0, and U is 1.0 or
   more): "not shown to be a point or more below the pre-implant level".

The phrase "below the pre-implant level, by less than a point" is used only
under 2, that is, only when U < 1.0.

### All three verdicts are reachable

Synthetic examples. None is a guess at the paper. Each uses the sham value
already known (median 6.0, IQR 4.0 to 7.0, n = 20) and method (C) of the
scoring rule, with no widening unless stated.

- Sham: SD = 3.0 / 1.35 = 2.2222; SE = 1.2533 × 2.2222 / √20 = 0.6228.
- Pre-implant with an IQR two points wide: SD = 2.0 / 1.35 = 1.4815;
  SE = 1.2533 × 1.4815 / √20 = 0.4152.
- SE of D = √(0.4152² + 0.6228²) = 0.7485. Half-width = 1.96 × 0.7485 = 1.467.

| Synthetic pre-implant score, n = 20 | Widening | D | 95% interval | Verdict |
|---|---|---|---|---|
| Median 8.0 (IQR 7.0 to 9.0) | none | 2.0 | 0.53 to 3.47 | **SUPPORTED** (D ≥ 1.0, L > 0) |
| Median 6.0 (IQR 5.0 to 7.0) | none | 0.0 | −1.47 to 1.47 | **REFUTED** (D ≤ 0.5, U < 2.0) |
| Median 7.0 (IQR 6.0 to 8.0) | none | 1.0 | −0.47 to 2.47 | **INCONCLUSIVE** (D ≥ 1.0, L ≤ 0) |
| Median 6.5 (IQR 5.5 to 7.5) | none | 0.5 | −0.97 to 1.97 | **REFUTED** (D ≤ 0.5, U < 2.0) |
| Median 8.0 (IQR 7.0 to 9.0) | 0.5 (construct unstated) | 2.0 | 0.03 to 3.97 | **SUPPORTED** |
| Median 7.5 (IQR 6.5 to 8.5) | 0.5 (construct unstated) | 1.5 | −0.47 to 3.47 | **INCONCLUSIVE** |
| Median 6.0 (IQR 5.0 to 7.0) | 0.5 (construct unstated) | 0.0 | −1.97 to 1.97 | **REFUTED** |

**Reachability bands with these spreads** (half-width 1.467 plus widening):

| Total widening | SUPPORTED when | REFUTED when | INCONCLUSIVE between |
|---|---|---|---|
| none | D > 1.47 | D ≤ 0.50 | 0.50 < D ≤ 1.47 |
| 0.5 | D > 1.97 | D < 0.03 | 0.03 ≤ D ≤ 1.97 |
| 1.0 | D > 2.47 | D < −0.47 | −0.47 ≤ D ≤ 2.47 |
| 1.5 | D > 2.97 | D < −0.97 | −0.97 ≤ D ≤ 2.97 |

A paper that reports a paired comparison would give a narrower interval and a
narrower inconclusive band.

### Reachability with the version widening (new in this registration)

The block above is P-003's and stops at a total widening of 1.5. §5 of this
file adds one more widening of 0.5 (the version rule), so the largest possible
total is now **2.0**. The examples and bands are recomputed by
`registration_checks.py reachability` in this folder, with the same synthetic
spreads (half-width 1.467 before any widening). The first seven rows of its
output repeat P-003's table exactly. The rows it adds:

| Synthetic pre-implant score, n = 20 | Total widening | D | 95% interval | Verdict |
|---|---|---|---|---|
| Median 8.5 (IQR 7.5 to 9.5) | 1.0 | 2.5 | 0.03 to 4.97 | **SUPPORTED** |
| Median 8.0 (IQR 7.0 to 9.0) | 1.0 | 2.0 | −0.47 to 4.47 | **INCONCLUSIVE** |
| Median 5.5 (IQR 4.5 to 6.5) | 1.0 | −0.5 | −2.97 to 1.97 | **REFUTED** |
| Median 9.5 (IQR 8.0 to 10.0) | 2.0 | 3.5 | 0.03 to 6.97 | **SUPPORTED** |
| Median 8.0 (IQR 7.0 to 9.0) | 2.0 | 2.0 | −1.47 to 5.47 | **INCONCLUSIVE** |
| Median 4.5 (IQR 3.5 to 5.5) | 2.0 | −1.5 | −4.97 to 1.97 | **REFUTED** |

**Reachability bands, recomputed up to the new maximum:**

| Total widening | SUPPORTED when | REFUTED when | INCONCLUSIVE between |
|---|---|---|---|
| none | D > 1.47 | D ≤ 0.50 | 0.50 < D ≤ 1.47 |
| 0.5 | D > 1.97 | D < 0.03 | 0.03 ≤ D ≤ 1.97 |
| 1.0 | D > 2.47 | D < −0.47 | −0.47 ≤ D ≤ 2.47 |
| 1.5 | D > 2.97 | D < −0.97 | −0.97 ≤ D ≤ 2.97 |
| 2.0 | D > 3.47 | D < −1.47 | −1.47 ≤ D ≤ 3.47 |

**The thresholds are rounded.** They are printed to two decimals, as P-003
printed them. As computed, the half-width before widening is 1.4670, so the
SUPPORTED thresholds are 1.467, 1.967, 2.467, 2.967 and 3.467, and the
REFUTED thresholds from a widening of 0.5 upwards are 0.033, −0.467, −0.967
and −1.467. The script prints both forms. Scoring uses unrounded values, as
the carried rule says.

**What this means, said plainly.**

- **REFUTED, the informative outcome, is harder to reach here than in
  P-003.** With no widening it needs D ≤ 0.5. At the likely total of 0.5 it
  needs D below 0.033: pre-implant pain at or below the sham level.

- All three verdicts stay reachable at every total, including 2.0. The table
  shows one example of each.
- With the known sham median of 6.0, a SUPPORTED verdict at a total of 2.0
  under method (C) needs a pre-implant median of 9.5 or more, and a REFUTED
  verdict needs one below 4.53. Neither is likely. At a total of 2.0 the rule
  returns INCONCLUSIVE for nearly every plausible paper.
- The total that matters most is 0.5: a copy that is not the published
  version, with nothing else widened. Under method (C), SUPPORTED then needs
  D above 1.97, which is a pre-implant median of 8.0 or more. That is the top
  of what §3 expects.
- If the copy is also silent on the construct, the total is 1.0 and SUPPORTED
  needs D above 2.47.
- The version widening is the price of accepting a copy that may differ from
  the published paper. It makes INCONCLUSIVE more likely, not SUPPORTED.

### Scoring rule

Applied mechanically by the reader, in this order. Every number used is quoted
verbatim in `RESULT.md` with its location in the paper.

**Which numbers.**

- *Pain under sham:* the paper's summary of pain intensity for the sham period
  on its primary pain outcome, in its primary analysis population, at the time
  point or window the paper defines for that outcome. This is expected to be
  the median already known. If the full text gives a different figure from the
  abstract for the same outcome, the full text's figure is used and the
  difference is recorded.
- *Pain before implant:* a pain intensity score that the paper states was
  taken before the stimulator was implanted (before trial stimulation or
  before the permanent implant). The quoted wording must make this plain. A
  "baseline" taken at enrolment, with the stimulator already in use, is
  **not** pre-implant pain and is not used.
- *Scale:* 0 to 10. A 0 to 100 mm scale is divided by 10. A percentage relief
  figure is not converted into a score.
- *Construct.* Pre-implant pain must be the same pain construct as the sham
  outcome: pain intensity, with the same definition (average, worst, least or
  current pain, and the same body region if the paper distinguishes regions).
  One rule, in three cases:
  - the paper states the definition of both and they are the same: scored,
    no widening;
  - the paper states the definition of both and they differ (for example
    average pain under sham and worst pain before implant), or the
    pre-implant number is not a pain intensity score: UNSCORABLE (quantity
    not reported);
  - the definition of the pre-implant score is not stated, or that of the
    sham outcome is not: scored, and 0.5 is added to each side of the
    interval.
- *If the paper gives more than one pre-implant pain score,* the reader does
  not choose. The order is: first, the one whose stated definition matches the
  sham outcome; among those that match, or if none states a definition, the
  earliest in time; if that still leaves more than one, the one reported in
  the baseline table before any reported only in text.
- *Which statistic:* medians if the paper gives medians for both; otherwise
  means for both; otherwise one of each (see "mixed" below). If medians and
  means are both given for both, medians.

**Constants and conversions, used wherever they apply.** There is no other
source of a standard error.

- The multiplier for every 95% interval built by the reader is z = 1.96. A
  t multiplier is never used. This is approximate for 20 people and declared.
- Standard deviation from a median with an interquartile range:
  SD = (Q3 − Q1) / 1.35.
- Standard deviation from a range only: SD = (maximum − minimum) / 4.
- Standard error of a mean: SE = SD / √n.
- Standard error of a median: SE = 1.2533 × SD / √n.
- Standard error from a reported standard error: used as given.
- Standard error from a reported confidence interval for a mean, a median or
  a difference: SE = (upper − lower) / (2 × z), with z = 1.645 for a 90%
  interval, 1.960 for 95% and 2.576 for 99%. An interval whose level is not
  stated is taken as 95%. An interval at any other stated level is not used,
  and the number is treated as having no reported spread. No further factor
  is applied to a standard error obtained this way.
- A p-value is never converted into a standard error.
- *An unlabelled "x ± y".* If the paper gives a value as "x ± y" and nowhere
  says whether y is a standard deviation, a standard error or half a
  confidence interval, y is treated as a standard deviation, and `RESULT.md`
  says that this was done.
- *Borrowed SD.* If one of the two numbers has no reported spread, it takes
  the SD of the other. If the other's spread is an SD, an interquartile range
  or a range, that SD is the one given by the conversions above. If the
  other's spread is a standard error, or a confidence interval converted to
  one, it is converted back with the other number's own n: SD = SE × √n if
  the other number is a mean, and SD = SE × √n / 1.2533 if it is a median. If
  no conversion is possible (for example the other number's spread is an
  interval at an unusable level, or belongs to a difference and not to the
  number), the other number counts as having no reported spread and the
  fallback SD applies to both.
- *Fallback SD.* If neither number has a usable spread, both take
  SD = 3.0 / 1.35 = 2.2222 (the sham IQR already known).
- With a borrowed or fallback SD, the standard-error formula is that of the
  number receiving it: 1.2533 × SD / √n if that number is a median, SD / √n if
  it is a mean.
- n is the number of participants behind each number, as the paper states it.
  If it is not stated for a number, the n of the primary analysis population
  is used; if that is not stated, 20.

**How D, L and U are obtained.** The first method that the paper allows:

- **(A) The paper's own paired comparison.** The paper reports the difference
  between pre-implant and sham pain in the same participants (a mean
  difference, a median difference or a Hodges-Lehmann estimate) with a
  confidence interval. The sign is set so that D is pre-implant minus sham.
  With a 95% interval, or one of unstated level, those are D, L and U as
  reported. With a 90% or 99% interval, SE is obtained by the conversion above
  and [L, U] = D ± 1.96 × SE. With an interval at any other level, with a
  p-value only, or with "not significant" only, method (A) is not available
  and the reader goes to (B), then (C).
- **(B) Per-participant values.** The paper or its supplementary files give
  both scores for each participant. d = pre-implant minus sham is computed per
  participant, over the participants who have both. D is the mean of d, SD(d)
  is the sample standard deviation (n − 1 in the denominator),
  SE = SD(d) / √n, and [L, U] = D ± 1.96 × SE.
- **(C) Group summaries.** D = centre of pre-implant minus centre of sham.
  Each centre gets a standard error by the conversions above.
  SE of D = √(SE_pre² + SE_sham²), and [L, U] = D ± 1.96 × SE of D.

  Method (C) treats the two scores as independent. They are paired, so the
  interval is wider than a paired one would be. That is declared and
  accepted: it makes INCONCLUSIVE more likely, not SUPPORTED.

**Widenings.** Each adds 0.5 to each side of the interval, under any method.
They **stack by addition**, each counted at most once, so the total is 0, 0.5,
1.0 or 1.5:

- construct not stated (above);
- mixed statistics: a mean for one number and a median for the other, under
  method (C);
- a value read off a figure axis (below), whether one of the numbers or both.

**Special cases.**

- *Only one of the two numbers.* If the paper reports pain under sham and no
  pre-implant pain score for the trial participants, the outcome is
  UNSCORABLE (quantity not reported); see §5. The sham number cannot be
  missing, since the abstract holds it.
- *Different subsets.* If the two numbers are reported for different sets of
  participants, they are used only if one set contains the other and the
  smaller holds at least 80% of the larger (16 of 20, for example). The
  verdict then stands and the mismatch is recorded. If not, or if pre-implant
  pain is given only for a subgroup such as one diagnosis, the outcome is
  UNSCORABLE (quantity not reported).
- *Only a figure.* If a number appears only in a figure, a value printed in
  the figure is used as it stands, with no widening. If none is printed, the
  reader reads the centre and the spread off the axis to the nearest 0.5,
  says so, and the figure widening applies. If the figure cannot be read to
  the nearest 0.5, the outcome is UNSCORABLE (quantity not reported).
- *Ambiguity.* If the rule above does not decide a case, the reader does not
  choose the reading that gives a verdict. The reader appends an amendment to
  this file that states the ambiguity, scores the case under each reading, and
  reports INCONCLUSIVE if the readings disagree.

Comparisons use unrounded values. `RESULT.md` prints D, L and U to two
decimals, and each intermediate standard error to four.

### The version widening (new in this registration; the only addition to scoring)

The "Widenings" paragraph above is P-003's and lists three widenings. This
registration adds a fourth, defined by the version rule in §5:

- **the copy scored is not the published version.**

It adds 0.5 to each side of the interval, under any method, is counted at most
once, and stacks by addition with the other three. With four widenings the
total is 0, 0.5, 1.0, 1.5 or 2.0. Where the carried paragraph says "so the
total is 0, 0.5, 1.0 or 1.5", that holds for a published-version copy; for any
other copy the total is one step higher. Nothing else in the scoring rule is
affected: the methods, the conversions, the construct rule, the special cases
and the verdict rule apply to a repository copy exactly as written.

### Secondary quantities (not part of the verdict)

Both are **secondary**. They are scored as stated and reported beside the
primary verdict. Neither can change it.

- **S1, time since implant.** Prediction: the central value the paper reports
  for time since implant among the participants (median, or mean if no median)
  is at least 24 months. My probability: 0.60. Basis: the two Düsseldorf
  cohorts had means of 17.2 and 32.8 months (E-11 row B9), and one centre needs
  years of implanting to assemble 20 established responders. If the paper does
  not report it: "not reported".
- **S2, whether pre-implant pain is reported for the same individuals.**
  Prediction: it is **not** reported in a form the scoring rule can use. My
  probability that it is reported in a usable form, given the full text is
  obtained: 0.35.

**Unchanged in this registration.** S1 and S2 are scored as stated, on
whichever copy is obtained, and labelled with its version. Nothing learned
since P-003 bears on either probability.

### Probabilities, restated before the source is read

Taken from what is in the repository only. Three facts carry the change: a
repository copy is listed by the lookup; its version label is the submitted
one; and whether pre-implant pain is reported is as unknown as it was.

**Step 1. The full text is obtained by the declared routes, as §5 defines
"obtained": 0.52** (P-003: 0.40, and it was not obtained; the first version
of this file: 0.55, see "Restated once before the merge" below).

- Routes 1 to 4 failed a day ago and are expected to fail again. Together
  they add about 0.01 (a deposit in PubMed Central in the meantime).
- Nearly all of the 0.52 is route 5. It needs five things in a row, and the
  registering agent's rough figures for each are: the lookup answers the
  placeholder address again (0.95); the response still lists the repository
  entry (0.98); the repository answers a scripted client with an unusual
  user-agent and does not block it (0.85); a file holding the full text is
  reached within two requests under the first-link rule (0.70); and the file
  gives methods and results as text under the PDF text rule (0.92). The
  product is 0.51, and with routes 1 to 4 the total is 0.52.
- The fourth factor fails if the record has no file, the file is under
  embargo, the file sits on another host, the page builds its links by
  script, or **the first candidate in document order is the wrong file**: a
  site-wide document such as a policy or a guide linked in the page header,
  or a navigation link whose path happens to contain "fulltext". The rule
  requests that one and the entry ends. The exclusions in step (b) remove
  one way to fail (a link back to the page itself) and leave this one.
- For: a lookup service that labels a repository entry with a version has
  usually found a file there, and university repositories exist to be
  harvested by scripts.
- Against: the rule is deliberately narrow (at most two requests per entry,
  same host only, no retries), and nothing in the repository says what the
  entry's address looks like.

**Step 2. Given that, pre-implant pain is reported in a usable form: 0.35**
(P-003: 0.35). Unchanged. Nothing learned since bears on it. A submitted
version could report more or less than the published one, and the registering
agent has no reason to lean either way.

So the registration is scored with probability 0.52 × 0.35 = 0.18.

**Step 3. Given that it is scored.** If the full text is obtained, it is
almost certainly the submitted version, so the version widening applies and
the smallest total widening is 0.5. That moves likely outcomes from SUPPORTED
to INCONCLUSIVE: under method (C), a D of 1.5 to 2, which §3 expects, is
INCONCLUSIVE at that widening. A paired comparison in the paper (method A)
would be narrower, and is the main way SUPPORTED stays possible.

| Outcome | Given that it is scored | Overall | P-003, final: given scored | P-003, final: overall |
|---|---|---|---|---|
| SUPPORTED | 0.25 | **0.05** | 0.40 | 0.06 |
| REFUTED | 0.07 | **0.01** | 0.10 | 0.01 |
| INCONCLUSIVE | 0.68 | **0.12** | 0.50 | 0.07 |
| UNSCORABLE (source not obtained) | n/a | **0.48** | n/a | 0.60 |
| UNSCORABLE (quantity not reported) | n/a | **0.34** | n/a | 0.26 |
| Sum | 1.00 | **1.00** | 1.00 | 1.00 |

| | Obtained | Usable, given obtained | Scored |
|---|---|---|---|
| P-003, final | 0.40 | 0.35 | 0.14 |
| This registration | 0.52 | 0.35 | 0.18 |

Arithmetic, unrounded: scored 0.1820; SUPPORTED 0.0455; REFUTED 0.0127;
INCONCLUSIVE 0.1238; not obtained 0.4800; not reported 0.3380. These sum to
1.0000. The overall column is rounded to two decimals and sums to 1.00.

**The single likeliest outcome is UNSCORABLE (source not obtained), at 0.48.**
The second is UNSCORABLE (quantity not reported), at 0.34. A verdict of any
kind has 0.18, and the likeliest verdict is INCONCLUSIVE.

**Restated once before the merge, and the earlier figures are kept here.**
The change followed no information about the paper.

| Version | Obtained | Usable, given obtained | SUPPORTED | REFUTED | INCONCLUSIVE | Not obtained | Not reported |
|---|---|---|---|---|---|---|---|
| `df9380f` and `af1a963` | 0.55 | 0.35 | 0.05 | 0.01 | 0.13 | 0.45 | 0.36 |
| final (above) | 0.52 | 0.35 | 0.05 | 0.01 | 0.12 | 0.48 | 0.34 |

- What changed: the factor for "a file is reached within two requests under
  the first-link rule" went from 0.75 to 0.70. Making step (b) deterministic
  after review made one failure plain that the first figure had not priced:
  the rule takes the first candidate in document order, and that can be the
  wrong file.
- What did not change: the other four factors. The second extraction with
  the fallback tool can only help the fifth factor, by a little; it stays at
  0.92. The figures given that the registration is scored are unchanged.

**What these figures are not.** They are one agent's judgement, stated so that
it can be checked against the outcome. The P-003 figure for "obtained" (0.40)
was followed by a failure, which is what a 0.60 chance of failure looks like
and says little about calibration from one case. The rise from 0.40 to 0.52
follows from access metadata recorded in P-003's `RESULT.md`, not from any
information about the paper's content.

## 5. Unscorable conditions and the stop rule, written now

PROGRAMME.md requires any stop rule or threshold to be in a repository file
before the work starts. These are the rules for this registration.

### The declared routes

**Five routes, tried in this order. The list is closed.** Routes 1 to 4 are
P-003's, exactly as written there. Route 5 is new. No other route, service,
mirror, repository search, web search, browser session, login, library proxy or
request to an author is used. The reader stops at the first route that returns
the full text as defined below.

The paragraph on how requests are made, and routes 1 to 4, carried verbatim
from P-003 §5:

Every request is scripted, sends the user-agent string
`research-reader/1.0 (scripted; one request per step)` and carries no cookies
and no contact details of the owner. Each step below is **one request**.
Redirects followed automatically within a request are not counted. There are
no retries with altered headers, a different user-agent, a different client or
a different address. If a request gets no HTTP response at all (a timeout or a
dropped connection), the identical request may be sent once more, after at
least 60 seconds. Any HTTP response, including a refusal, ends that step.

1. **PubMed Central through NCBI E-utilities.** One `elink` request from the
   PubMed record to `db=pmc`. If it returns a PMC identifier, one `efetch`
   request with `db=pmc` and `retmode=xml`.
2. **Europe PMC full text.** One request to the Europe PMC REST `search`
   endpoint for the PubMed number. If the record is flagged as having full
   text, one request to its `fullTextXML` endpoint.
3. **The publisher's open-access page.** One request to `https://doi.org/`
   followed by the DOI.
4. **Unpaywall.** One request to `https://api.unpaywall.org/v2/` followed by
   the DOI, with `email=reader@example.org`. Every reader uses exactly that
   address. It is a non-personal placeholder on a domain reserved for
   examples; no real address, and never the owner's, is sent. If the response
   has a `best_oa_location`, one request to its `url_for_pdf`, or to its `url`
   if there is no PDF address. No other location in the response is tried.

   A declared weakness of this step, from the registering agent's memory of
   the service's documentation and not from any lookup: the service asks
   callers to give their own email address, and it may refuse a placeholder.
   If it does, that refusal is an HTTP response and ends the step like any
   other. The address is not changed and the request is not repeated.

Supplementary files count if the obtained full text links to them, with one
request per file under the same conditions.

### Clarifications to routes 2 and 4, binding here

P-003's Amendment 1 recorded two places where the text above left a choice to
the reader. Every reading gave the same outcome there. They are fixed here in
advance, so that the reader of this registration has no choice to make.

- **Route 2, the fields and the result type.** The `search` request uses
  `resultType=lite` and `format=json`. The record is "flagged as having full
  text" if, and only if, at least one of the four fields `inEPMC`, `inPMC`,
  `isOpenAccess` and `hasPDF` has the value "Y". `hasTextMinedTerms` is not a
  full-text flag and is ignored. If the record is flagged, the one
  `fullTextXML` request is addressed with the record's `pmcid` if it has one,
  and otherwise with `MED/` followed by the PubMed number. Whatever HTTP
  response comes back ends the step. If the record is not flagged, no
  `fullTextXML` request is sent. The form of that address is from the
  registering agent's memory of the service and not from any lookup; if the
  service rejects it, that response ends the step.
- **Route 4, when the best location is the route-3 address.** If the address
  that route 4's second step would request (the `url_for_pdf` of
  `best_oa_location`, or its `url` if there is no PDF address) is the same
  string as the address requested in route 3, **that step is skipped, not
  repeated.** It is logged as skipped, with the address comparison. Route 4
  then ends with no full text, and the reader goes on to route 5. If the
  address differs from the route-3 address in any character, the step is
  sent as route 4 states.

The second clarification differs from what the P-003 reader did (it sent the
request once and was refused again). Amendment 1 shows that both readings give
the same outcome. Skipping is chosen here because a request already refused,
sent again unchanged, cannot return anything new.

### Route 5, repository copies (new in this registration)

5. **Repository copies.** No new lookup is made. From the same single lookup
   response already received in route 4 (the one request to
   `https://api.unpaywall.org/v2/`), take every entry of `oa_locations` whose
   `host_type` is `repository`, in the order the response lists them. For
   each such entry, in turn:

   a. **One scripted request** to its `url_for_pdf` if that field is present
      and not null, else to its `url`.

   b. **If that returns an HTML landing page, one further request** to the
      first link on that page that points to a PDF or full-text file on the
      same host. "First" means the first candidate in document order **after
      the exclusions below**. If no candidate remains, the entry ends with no
      second request. Every term in this step is defined below.

   Each of (a) and (b) is one request, under the conditions carried above:
   **the same user-agent**, no cookies, no contact details, redirects inside
   a request not counted. **No retries with altered headers**, a different
   user-agent, a different client or a different address. **The
   identical-repeat rule is as in P-003:** only if a request gets no HTTP
   response at all may the identical request be sent once more, after at
   least 60 seconds; any HTTP response, including a refusal, ends that step.

   Fixed in advance, so that the reader does not choose:

   - *At most two requests per entry.* If (b) returns another HTML page that
     is not the full text, the entry ends there. No third request.
   - *"An HTML landing page".* A response to (a) with HTTP status 200 whose
     `Content-Type` header starts with `text/html` (ignoring letter case),
     and which is not itself the full text as defined below. If such a page
     is itself the full text, the entry has returned the full text and (b)
     is not needed.
   - *A limit of that definition, said plainly.* A page served with status
     200 and `text/html` that is in fact a bot challenge or an access-denied
     page cannot be told apart from a landing page mechanically. **It is
     treated as a landing page.** Step (b) is applied to it like any other.
     If the entry then ends without full text, the kind of failure recorded
     for it is "no full text in any response", unless a non-200 refusal was
     received for that entry (see "The kind of failure" below). A bot block
     served with status 200 is therefore recorded as the wrong kind. The
     reader may describe the page in a note; the note changes no record.
   - *The parser.* The landing page is parsed with Python's standard-library
     `html.parser` (`HTMLParser`), and only start tags of elements are used.
     Text inside comments and inside `script` elements is ignored, so a link
     that exists only in a comment or in script is not a link. The body is
     decoded with the character set named in the `Content-Type` header, or
     as UTF-8 if none is named, with undecodable bytes replaced.
   - *The links, in document order.* The links are, in the order their start
     tags appear in the source: the `href` of each `a` element and of each
     `link` element, and the `content` of each `meta` element whose `name`
     is `citation_pdf_url` (ignoring letter case). An element without that
     attribute, or with an empty one, is not a link.
   - *Resolving.* Each link is resolved against **the final address of (a)**,
     that is, the address (a) ended at after its redirects, with
     `urllib.parse.urljoin`. **A `<base href>` in the page is ignored.** Any
     fragment is then stripped (`urllib.parse.urldefrag`). **Path parameters
     such as `;jsessionid=…` and query strings are kept as they are**, both
     in the address compared and in the address requested.
   - *"Points to a PDF or full-text file".* A link qualifies if at least one
     of these holds: its path ends in `.pdf`; its path contains `fulltext`;
     its element declares `type="application/pdf"`; or its element is the
     `citation_pdf_url` one. **For the `.pdf` and `fulltext` tests only the
     path component is examined, ignoring letter case**: the `path` given by
     `urllib.parse.urlparse` for the resolved address, which leaves out the
     query string, the fragment and the parameters of the last path segment.
   - *Exclusions.* A qualifying link is **not a candidate** if any of these
     holds for its resolved, fragment-stripped address:
     - it equals the address requested in (a), or the final address (a)
       ended at;
     - it is on a different host;
     - it is the same string as an address already requested in this attempt
       that received an HTTP response.
   - *"The same host".* The host name of the link's address equals, ignoring
     letter case, the host name of the final address of (a). A file on any
     other host, including a subdomain, is on a different host. A link with
     no host name after resolving (for example a `mailto:` or `javascript:`
     address) is on a different host.
   - *Which one is requested.* **The first candidate in document order after
     those exclusions.** An excluded link does not use up the step: the
     reader passes over it and takes the next. The reader does not pick a
     later candidate because it looks more promising. **If no candidate
     remains, the entry ends with no second request.**
   - *An address already answered, for (a).* If the address for (a) is the
     same string as one already requested in this attempt that received an
     HTTP response, (a) is skipped and logged as skipped, and the entry
     ends.
   - *Any other response to (a)* (a refusal, an error status, a 200 response
     that is neither `text/html` nor readable full text): the entry ends.
   - *The response to (b)* either is the full text as defined below, or it
     is not, and the entry ends either way.
   - *Order and stopping.* The reader goes on to the next repository entry
     only if the current one did not return the full text as defined below,
     and stops at the first that does. When the entries are exhausted, route
     5 ends.
   - *No lookup response to work from.* If route 4's lookup was refused,
     returned no JSON record, or lists no entry with `host_type`
     `repository`, route 5 makes no request and ends.
   - *Route 5 does not depend on route 4's second step.* It is tried whether
     that step was sent, skipped or refused.

   **How this sits with route 4's last sentence.** Route 4, carried above,
   says "No other location in the response is tried." That sentence bounds
   route 4, and it is left as written. Route 5 is a separate, declared route
   that reads the same response. Between them, the locations that may be
   requested are the best location (route 4) and the repository entries
   (route 5). No other entry of `oa_locations`, and no other field of the
   response, is used to make a request.

**No other route exists. The list of five is closed.** In particular the
reader does not search any repository, does not look the paper up in any
other index, and does not use an address that comes from anywhere but the
steps above.

### The version rule (new in this registration)

A repository copy may be the submitted version and not the published one.
P-003's `RESULT.md` reports the label of the listed copy as "submittedVersion".

- **Any version is accepted**: submitted, accepted or published. A copy is
  not turned down for its version.
- **The version label is recorded.** For a copy obtained by route 5 or by
  route 4's second step, the label is the `version` field of the lookup entry
  the copy came from, quoted verbatim. If that field is absent or null, the
  label is "unlabelled". If the document itself states a version (for example
  a cover page or a header), that wording is quoted beside the label; the
  lookup's label is the one the rule uses. A copy obtained by routes 1 to 3
  is taken as the published version, label "publishedVersion", unless the
  document itself says it is an author manuscript, in which case that wording
  is the label.
- **If the copy is not the published version** (its label is anything other
  than "publishedVersion", including "unlabelled"), the result is scored, and
  it is labelled **"scored on the <label> version"** wherever the verdict is
  stated. **The interval gets one further widening of 0.5 on each side,
  stacking with the others** (§4, "The version widening"). **The stated
  maximum total widening becomes 2.0.** The reachability bands for that total
  are in §4.
- **If a number in the repository copy conflicts with the abstract-level
  numbers already in this repository** (the sham median of 6.0 and its IQR of
  4.0 to 7.0, and likewise the active median and the difference), **the
  repository copy's numbers are used for scoring and the conflict is noted**
  in `RESULT.md`, with both versions of the number quoted. This is the same
  precedence as the carried scoring rule gives the full text over the
  abstract.
- **What the label does not license.** The reader does not go looking for
  the published version to compare, and does not correct the copy from any
  other source. A verdict labelled with a version is a verdict on that copy.

### The PDF text rule (new in this registration)

The carried definition below counts "text extracted locally from a PDF". This
rule says how.

- **The tool.** `pdftotext` from Poppler, run as `pdftotext -layout` on the
  downloaded file. **The fallback:** the Python library `pypdf`, taking
  `extract_text()` of each page in order. No other extraction tool is used.
  No optical character recognition is used, by any tool.
- **When the fallback is used.** In two cases, and once per file:
  - `pdftotext` is absent, or fails to run on the file;
  - `pdftotext` runs and its output has fewer than 1,500 words. The fallback
    is then **also** tried, once, **and its result decides**: if the
    fallback's output meets the test below, the full text is obtained and
    the fallback's output is the text that is read; if it does not, the copy
    does not count.

  If `pdftotext` yields 1,500 words or more, the fallback is not run.
- **The tool is recorded:** the name and version of each tool run, the
  command or call, and the word count each gave. Installing either named
  tool is not a request for the source; if the reader installs one, that is
  logged.
- **"Full text obtained" from a PDF needs the methods and the results
  readable as text after extraction:** the extracted text holds the passages
  that describe the trial's methods and report its results, as running
  words, and at least 1,500 words in all. The figure of 1,500 is chosen, not
  derived; it stands for "more than an abstract and a cover page".
- **How words are counted.** Whitespace-separated tokens of the whole
  extracted text: the length of Python's `text.split()`. Nothing is removed
  first, so headers, reference lists and table cells count.
- **Column order.** `-layout` keeps the page layout, and on a two-column
  page it may interleave the columns line by line. **That does not
  disqualify the text.** The test is whether the methods and results are
  there as words, not whether they come out in reading order. If interleaved
  columns make a needed number impossible to attribute, that is a matter
  for the scoring rule (its "Ambiguity" case), not for this one.
- **A scanned or image-only PDF does not count.** If extraction, by the
  tool whose result decides, gives no text or less than the above, the copy
  is not the full text, and the reader goes on as if the request had
  returned nothing usable.
- A PDF that is readable but in which a needed table is an image is handled
  as the carried definition says: the full text is obtained, and the missing
  table goes to the scoring rule.

### What "full text obtained" means

The methods and the results sections are readable as text (XML, HTML, or text
extracted locally from a PDF), including whichever table or passage reports
the participants' baseline characteristics and pain scores. A page that shows
only the abstract does not count. Neither does a page that shows the abstract
with a preview, a first page, or tables that are images with no text. If the
results are readable and a needed table is an image only, the full text is
obtained and the missing table is handled by the scoring rule (it may lead to
UNSCORABLE (quantity not reported)).

### The outcomes

- **UNSCORABLE (source not obtained).** If no route returns the full text as
  defined, the registration is closed as UNSCORABLE (source not obtained). It
  is **not** rescued from the abstract, from a secondary source, or from any
  other route.
- **UNSCORABLE (quantity not reported).** If the full text is obtained and
  does not report pre-implant pain for the trial participants in a form the
  scoring rule can use, the registration is closed as UNSCORABLE (quantity not
  reported). E-11 notes that this "would itself be worth recording"; it is
  recorded, and it is not a verdict on the claim.

### The stop rule

The rule, in P-003's words, unchanged:

**Two registrations that end unscorable for lack of a source mean the
programme cannot generate testable predictions with existing methods, and the
question of closing goes to the owner.**

- **Where it comes from, and where it is written.** It was first written in
  P-003's registration (§5), before that read, from the independent programme
  review of 2026-11-19 as relayed. It is carried here unchanged. This
  registration does not alter it.
- **This registration is attempt 2 of 2.** P-003 was attempt 1, ended
  UNSCORABLE (source not obtained), and counted. Its `RESULT.md` §4 says: "the
  count stands at 1 of 2."
- **If this registration ends UNSCORABLE (source not obtained), the stop rule
  is met, and the question of closing goes to the owner.** The reader writes
  that in `RESULT.md` and does nothing further about it. Closing is the
  owner's decision, not the reader's.
- If this registration ends with any verdict, or as UNSCORABLE (quantity not
  reported), the count stays at 1 of 2.
- UNSCORABLE (quantity not reported) is not "for lack of a source" and does
  not count towards the two. It is still not progress by the test in
  PROGRAMME.md.

### The kind of failure, recorded separately

P-003's `RESULT.md` §6 and the ledger raised a distinction that the stop rule
does not make. **This registration does not change the rule. It only records
the distinction.**

If the outcome is UNSCORABLE (source not obtained), `RESULT.md` states, for
each route and each step, exactly one of:

- **"no route returned a response containing full text"** kind (in short,
  "no full text in any response"): the service answered and what it returned
  held no full text (no identifier, not flagged, a landing page with no
  candidate link, a file that fails the PDF text rule, an entry not listed,
  an error status other than those below);
- **"a route was refused by a bot block"** kind: a non-200 refusal, that is,
  a response with HTTP status 401, 403 or 429;
- "skipped", or "no HTTP response", where those apply.

**The record rests on the HTTP status alone, and that is a limit.** A bot
challenge or access-denied page served with status 200 cannot be told apart
mechanically from an ordinary page (see route 5, "A limit of that
definition"). It is recorded as the "no full text in any response" kind
unless a non-200 refusal was also received for the same step or entry. The
record can therefore undercount bot blocks. It cannot overcount them.

and then one overall line, by this rule: if at least one step was of the
bot-block kind, the overall record is **"a route was refused by a bot
block"**, naming the routes; otherwise it is **"no route returned a response
containing full text"**.

Either way the outcome is UNSCORABLE (source not obtained), it counts as
attempt 2, and the stop rule is met. The record is there so that the owner,
deciding, can see which kind of lack it was. In attempt 1 both kinds
occurred: routes 1 and 2 held no full text, and routes 3 and 4 were refused.

## 6. What scoring does not show

- **One blinded trial**, at one centre, with 20 participants. Whatever the
  verdict, it is one comparison.
- **Established responders only.** The participants were chosen because the
  therapy still works for them. Nothing here describes people whose benefit
  has faded, and Q-B is about those people.
- **A sham period of limited length.** Five days, after a 24-hour washout.
  Pain over a longer period without stimulation is not measured.
- **Pre-implant pain is likely to be a chart value**, recorded years earlier,
  under different conditions and possibly on a different instrument. The
  comparison is not randomised and not blinded on that side.
- **A SUPPORTED verdict does not separate** carry-over, natural improvement,
  regression to the mean, selection and expectation. A REFUTED verdict does
  not show that the underlying pain is unchanged in any one person.
- **Not a statement about any patient.** Group summaries of 20 people say
  nothing about what an individual's pain would be with a device off.
- **Not a stimulation setting,** and not a reason for anyone to change or stop
  a therapy (ETHICS.md §3).
- **A SUPPORTED verdict would be weak progress at best.** PROGRAMME.md counts a
  prediction as progress when it was novel, testable and then confirmed by
  evidence not used to construct it. Here half of the quantity was already
  known (§2), and §3 says the test is not severe.

And for this attempt in particular:

- **A verdict on a submitted version is a verdict on that copy.** Numbers can
  change between submission and publication. The version widening allows for
  that crudely; it does not measure it.
- **Obtaining the source on the second attempt would show that the declared
  routes were the obstacle in the first.** It would say nothing more about
  the paper than one read says.
- **Failing again would not show that the paper cannot be had.** It would
  show that five scripted routes, with at most two requests per repository
  entry, did not return it.

## 7. Instructions for the reader (the second agent)

P-003 §7, adapted to this file. Do these in order. Do not skip a step, and do
not change the order.

1. **Confirm the registration predates the read.** Run `git fetch origin`
   first. Then record the hash and the timestamp of three commits, with `F`
   standing for
   `predictions/P-004-sham-pain-against-pre-implant-attempt-2/REGISTRATION.md`:
   - the commit that **added** the file:
     `git log --diff-filter=A --format='%H %cI' origin/main -- F`;
   - the **last** commit that touches it:
     `git log --format='%H %cI' -1 origin/main -- F`;
   - the commit on the first-parent line of `main` that brought it in (the
     merge commit): `git log --first-parent --format='%H %cI' -1 origin/main -- F`.

   If the first command prints nothing, the file is not on `main`: stop. Run
   `git log --format='%H %cI %s' origin/main -- F` and, for each commit after
   the one that added the file, say whether it changes any rule text (anything
   in §4, §5 or §7) or only appends below the "Amendments" heading. The
   **binding time** is the latest timestamp among: the merge commit, and every
   commit that changes rule text. Record the time at which you start step 2.
   **The read must start after the binding time. If any read of the source
   began before it, by you or by any session whose output you have seen, the
   result is void:** write that in `RESULT.md` and stop.

   Also run `python3 registration_checks.py carried` and
   `python3 registration_checks.py selftest` in this folder and record their
   output. The second shows that the first can fail. If `carried` reports a
   difference, say so in `RESULT.md` and apply P-003's wording for that
   block.
2. **Obtain the full text by the declared routes only** (§5), in the order
   listed there, one request per step, with the user-agent stated there. Take
   the identifiers from `evidence/05-crps.md` §6b. **Log every request**: the
   route and step, the address, the time, and what came back (HTTP status and
   size, and the kind of response, not content). Log every skipped step too,
   with the reason. For route 5, log the number of repository entries in the
   lookup response, and for each: its position in `oa_locations`, its
   `version` and `license` fields, which address field was used, the
   `Content-Type` and the final address of the response to (a), and, for a
   landing page: how many links qualified, which were excluded and under
   which exclusion, and which element supplied the link requested (or that
   no candidate remained). Stop at the first route that returns the full
   text as §5 defines it.
   If none does, write `RESULT.md` with the verdict UNSCORABLE (source not
   obtained), the log and the kind-of-failure record of §5, state that the
   stop rule is met, and stop. Do not read the abstract in place of the full
   text, do not retry with altered headers, and do not try any other route.
3. **Record the version label and the extraction tool.** State which route
   and which lookup entry the copy came from, its version label by the
   version rule, any version wording in the document itself, the file type
   and size, and, for a PDF, each extraction tool run, its version, the
   command, and the word count it gave (whitespace-separated tokens), and
   which tool's result decided. Say whether the version widening applies.
4. **Extract the numbers.** Quote verbatim, with the location (section, table
   or figure, and the row or sentence): pain under sham, with the paper's
   definition of that outcome; pain before implant, with the words that show
   it was taken before implant and the words that define it, or a statement
   that no definition is given; the number of participants behind each; the
   spread of each; any paired comparison of the two; time since implant (S1).
   Say which analysis population each belongs to. If pre-implant pain is
   absent, quote what the baseline table does report, and say which sections
   you searched and for which terms. If any number in the copy conflicts with
   the abstract-level numbers in this repository, quote both and score with
   the copy's.
5. **Apply the rule in §4 mechanically.** State which method (A, B or C),
   which widenings and which special cases applied, and the total widening.
   Show the arithmetic for D, L and U. State the verdict in one of five
   forms: SUPPORTED, REFUTED, INCONCLUSIVE, UNSCORABLE (source not obtained),
   UNSCORABLE (quantity not reported). If the copy is not the published
   version, add "scored on the <label> version" to the verdict wherever it is
   stated. Score S1 and S2 separately and label them secondary.
6. **Write `RESULT.md` in this folder**: the commit hashes and times from
   step 1, the access log, the version label and the extraction tool, the
   quotations, the arithmetic, the verdict, the registered probabilities of
   this file beside the outcome, where the count under the stop rule now
   stands, and the limits in §6. Add anything the paper says that bears on
   Q-B and was not registered, under a heading that says it was not
   registered.
7. **Do not edit `REGISTRATION.md`. Amendments are append-only.** If a rule
   turns out to be ambiguous, append an amendment under the heading below,
   dated, saying what was ambiguous, that it was written after the read, and
   how each reading scores. Change nothing above the heading. Do not edit
   P-003's files.
8. **Do not** update `ledger/OPEN.md` or the evidence briefs in the same
   change unless your own brief says so. Propose the ledger line in your
   report. Do not write stimulation settings or advice in any file.

## 8. Not changed, though noted

Things the registering agent noticed and left as they are. None is a rule of
this registration. Each is here so that it is not lost, and so that no one
has to wonder whether it was seen.

1. **The stop rule does not distinguish kinds of failure.** "No open copy
   exists" and "the declared routes could not reach one" count the same. The
   rule is carried unchanged; §5 only records which it was.
2. **Whether two attempts at one paper are "two registrations" in the sense
   the review meant** is not something this file can settle. It follows its
   brief and the owner's approval: this is attempt 2 of 2.
3. **The carried "Widenings" paragraph says the total is "0, 0.5, 1.0 or
   1.5".** It is left as written, and the version widening is stated beside
   it. A reader could find the two sentences at odds; §4 says how they fit.
4. **The carried definition of "full text obtained" names XML, HTML and text
   extracted from a PDF.** A submitted manuscript may be a word-processor
   file. By the carried wording such a file does not count, and the entry
   would end without full text. The definition is not widened here.
5. **Route 5 follows links on the same host only, and makes at most two
   requests per entry.** A repository that serves its files from another
   host, or behind a second landing page, or through links built by script,
   will not be reached. This is new text, kept narrow on purpose, and it is
   the likeliest way for this attempt to fail for a reason that has nothing
   to do with the paper.
6. **Route 3 has been refused three times** and will very probably be
   refused again. It is kept, as P-003 wrote it; it costs one request.
7. **The lookup's placeholder address** was accepted in attempt 1. P-003's
   declared weakness about it is carried unchanged and may still bite.
8. **The multiplier z = 1.96 for 20 people,** the independence assumption of
   method (C), and the chosen threshold of 1.0 are P-003's declared
   approximations and are unchanged.
9. **At a total widening of 2.0 the rule is close to uninformative** (§4). A
   smaller version widening, or none with a label only, would keep more
   resolution. The size was fixed by the brief for this registration at 0.5,
   the same as every other widening.
10. **The version label comes from the lookup service,** not from the
    document. The service can be wrong: a copy labelled as submitted may be
    the accepted or published text, and the reverse. The rule uses the label
    as given and quotes what the document says beside it.
11. **Half of the quantity is already known, and the test is not severe.**
    That was true of P-003 and is true here. A second attempt does not make
    the prediction more novel.
12. **The stop rule's original wording in the programme review has still not
    been seen** by a registering agent. It is carried from P-003, which had
    it as relayed.
13. **The folder number P-004 collides with candidate P-4** in E-11 and the
    ledger, which is a different paper. The top of this file says so. The
    numbering is not changed here.
14. **Route 5 takes the first candidate link, even if it is the wrong
    file,** and it records a bot block served with status 200 as "no full
    text in any response". Both follow from keeping step (b) mechanical.
    Both are stated in §5, and the first is priced in §4.

---

## Amendments (appended after the registration; the text above is not edited)

None.
