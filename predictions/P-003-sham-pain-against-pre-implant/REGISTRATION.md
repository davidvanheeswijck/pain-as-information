# P-003. Registered prediction: pain under blinded sham against pain before implant

**Written 2026-11-19 (about 21:00 UTC), before the source was read.** The
source is the full text of the sham-controlled crossover trial of ganglion
stimulation in established responders, Tabatabaei et al. 2026 (identifier in
`evidence/05-crps.md`, §6b). This file names the trial with its identifiers
removed (no PubMed number, DOI or registry number), so that no tool run over
this folder fetches its record. The quoted citation in §2 still carries the
author list, title and journal.

Intent: `intent/programme/2026-11-19-pivot-to-evidence-appraisal.md`. This is
step 2 of D-003 (`ledger/DECISIONS.md`): one prediction registered against data
not yet read, then scored. It is candidate P-3 of `evidence/11-evidence-map.md`
("Candidate predictions against unread data").

Two agents, two jobs. The registering agent (Claude Fable 5.2, a language
model) wrote this file from the repository alone and stops here. A different
agent reads the source later and writes `RESULT.md`. If the paper disagrees
with this file, the paper is right and this file is the record of the
registering agent being wrong.

Nothing here is a statement about any person, and nothing here is a stimulation
setting (ETHICS.md §3).

> **Read this first. Three limits of this registration.**
>
> 1. **It predicts one unread number.** Pain under sham in this trial is
>    already in the repository, from the abstract (median 6.0). The only
>    unread half of the quantity is the participants' pain before implant.
> 2. **The test is not severe.** A SUPPORTED verdict would mostly reflect that
>    people are implanted when their pain scores are high. REFUTED is the
>    informative outcome.
> 3. **The registered likeliest outcome is UNSCORABLE.** The registering
>    agent puts 0.86 on the registration ending unscorable (0.60 because the
>    full text is not obtained, 0.26 because pre-implant pain is not reported
>    in a usable form), and 0.14 on any verdict.

**Revised before merge.** This file was first committed at `0da91a6`. It was
revised on the same branch at `570ac46`, and once more in the commit after
that, each time after a review of the pull request, before the merge and
before any read of the source. The reviews found no leak. The revisions
tightened the scoring rule, the source routes and the verdict rule, and the
probabilities in §4 were restated to match the tighter rules. The pull request
is to be merged with a merge commit, not a squash, so that `0da91a6`,
`570ac46` and the final revision all stay in the history of `main` and the
earlier text can be read there. From the merge onwards the file is
append-only.

**Attestation by the coordinating session, recorded as relayed.** The
coordinating session attests that no session whose output it has seen had read
the paper before the merge. The registering agent cannot check this and
records it as given; its own statement is in §2.

## 1. The question, and why it bears on Q-B

Q-B is the programme's second question: why does the benefit of ganglion
stimulation fade? (PROGRAMME.md, "The three questions".)

**The quantity.** Pain under blinded sham stimulation, in people who are
established responders, set against the same participants' pain before the
stimulator was implanted. Both on the 11-point scale (0 to 10).

Write **D = pre-implant pain minus pain under sham**, in points. D is positive
when pain under sham is lower than pain before implant.

**Why it bears.** E-11 names three candidate explanations for fading:
habituation (H), lead or hardware drift (L) and disease progression (D in
E-11's lettering; called "progression" below to avoid a clash with the
quantity). Row B14 of E-11 says the measurement that progression needs is pain
with the device off, in the same people, over time, and that no study found
reports it. A blinded sham period in long-term responders is the nearest
available reading: it shows where pain goes when stimulation is withdrawn
without the participant knowing. Row B9 found one such comparison, in one
centre: pain under sham equalled pain before implant. An independent centre
either repeats that or does not.

**What each outcome would suggest, and what it would not.**

- **Sham pain at about the pre-implant level (D near 0).** The benefit in these
  responders depends on ongoing stimulation. At group level there is no sign of
  an effect carried over into the sham period, and no sign that the underlying
  pain has drifted up or down since implant. It would repeat row B9 in a second
  centre.
- **Sham pain clearly below the pre-implant level (D clearly positive).**
  Something other than ongoing stimulation accounts for part of the distance
  from pre-implant pain. The candidates cannot be separated by this number:
  an effect carried over from earlier stimulation into a sham period that is
  days long; natural improvement since implant; regression to the mean, since
  people are implanted when pain is high; selection of responders; and
  expectation under blinding, since a participant who does not know the
  allocation may still expect relief. It would not show that the underlying
  pain has improved.
- **Sham pain above the pre-implant level (D clearly negative).** That would
  suggest rebound after withdrawal, or progression of the underlying pain since
  implant. This number cannot separate those two either.
- **In every case:** the trial enrolled people in whom the therapy still works.
  No outcome is a finding about why any individual's benefit fades, and none
  describes people whose benefit has faded.

## 2. Prior exposure, verbatim

Everything the repository says about this trial, found on 2026-11-19 at commit
`dfd9804` by `grep -rIn -i` over the whole tree (outside `.git`) for the
trial's PubMed number, the DOI suffix, the first author's name, the registry
number, "Umeå", "established responder", "May 2026", "2.5 points",
"sub-perception" and "subperception", and by reading every line matching
"sham" or "crossover" in the files listed in the registering agent's brief.

In the quotations below, the trial's PubMed number, DOI and registry number are
replaced by `[PMID]`, `[DOI]` and `[registry number]`. That is the only change.
The identifiers are in `evidence/05-crps.md`.

**`evidence/05-crps.md`, §6 "The 2024-2026 frontier: thin, with three real
items", bullet "Closed-loop":**

> **[registry number], a sham-controlled sub-threshold DRG trial at Umeå, is
> COMPLETED and unpublished** and worth chasing.

**`evidence/05-crps.md`, §6b "Corrections from a registry audit, 1 September
2026", under "The important one: the sham-controlled DRG trial is published,
and it is positive":**

> This brief listed [registry number] as "COMPLETED and unpublished". **It was
> published on 13 May 2026.**
>
> > **Tabatabaei P, Wänman J, Awad A, Eriksson M, Salomonsson J, Bredemo L,
> > Sjöberg R, Hariz MI, Blomstedt P. "Subperception dorsal root ganglion
> > stimulation versus sham stimulation in established responders: a
> > randomized, double-blind crossover clinical trial." *Reg Anesth Pain Med*,
> > 2026. [PMID], [DOI].**
>
> Umeå. Enriched enrolment (at least 50% relief for at least 3 months), n=20,
> quadruple-masked, two-period crossover, two 5-day periods with a 24-hour
> washout, active at 90% of perception threshold, sham off.
>
> **Median NRS 3.0 (IQR 2.0-4.0) active against 6.0 (IQR 4.0-7.0) sham.
> Hodges-Lehmann median difference −2.5 (95% CI −3.0 to −2.0), p<0.001.** All
> patient global impression domains and satisfaction favoured active. No
> serious or device-related adverse events. `[Note a registry-versus-paper
> discrepancy: the ClinicalTrials.gov record says 80% of perception threshold,
> the paper says 90%.]`
>
> **And there are two independent centres, not one.** The frequency-dependency
> trials in §3 are **Piedade, Gillner, McPhillips, Vesper and Slotty in
> Düsseldorf**, not Umeå as this brief implied. So sham-controlled DRG evidence
> now comes from two unrelated groups.
>
> **Consequence.** The statement that sham-controlled DRG evidence is scarce is
> now substantially weaker than when written. It remains true that the *pivotal
> implantation* trial had no sham arm. It is no longer true that the technique
> lacks blinded sham-controlled support in implanted patients.

**`evidence/05-crps.md`, closing note ("Principal residual gaps"):**

> the completed but unpublished Umeå sham-controlled DRG trial
> ([registry number])

**`evidence/11-evidence-map.md`, Q-B table, row B9** (the parts about this
trial; the rest of the row is about the two Düsseldorf trials and is used in
§3):

> Tabatabaei et al. 2026, [PMID] (abstract only)

> Tabatabaei, abstract: "median NRS 3.0 (IQR 2.0-4.0) vs 6.0 (IQR 4.0-7.0)"
> active against sham, 20 established responders. Match: implanted yes;
> CRPS-labelled in about a third; limb and duration of pain not stated.

> Two centres (Düsseldorf, Umeå). Whether the two Düsseldorf cohorts overlap is
> not stated in the passages read. Authors at both centres consult for the
> manufacturer.

> These are people chosen because the therapy still works. They say nothing
> about people in whom it has faded.

**`evidence/11-evidence-map.md`, "What the Q-B table says, in plain terms":**

> In people chosen because stimulation still works, blinded switch-off brings
> the pain back, in two centres. That shows continued dependence on
> stimulation in responders. It does not describe people whose benefit has
> faded.

**`evidence/11-evidence-map.md`, "Candidate predictions against unread data",
row P-3, in full:**

> The full text of the sham-controlled crossover trial in established
> responders, Tabatabaei et al. 2026, [PMID]. The abstract states re-use is
> permitted under a CC BY licence; it was not in PMC on 2026-11-19.

> (a) Median pain under sham set against the same participants' pain before
> implant, if reported. (b) Time since implant. (c) Whether the two
> participants who ended a period early did so under sham.

> Q-B. Row B9 found, in one Düsseldorf trial, that pain under blinded sham
> equalled pre-implant pain. An independent centre either repeats that or does
> not, and the answer bears on whether underlying pain has shifted in long-term
> responders (the D candidate) and on carry-over.

> The abstract, in full: active and sham medians, the difference, the design,
> the enrichment criterion. E-05 §6b records the same abstract and a registry
> note. The publisher page was requested once by script and refused (HTTP 403);
> nothing was received.

> The paper may not report pre-implant pain at all. That would itself be worth
> recording, and it is not a scored outcome.

**`evidence/11-evidence-map.md`, same section, "Reading, on choosing among
them":**

> P-3 and P-4 are conditional on what the paper reports.

**`evidence/11-evidence-map.md`, Appendix C "Sources read as abstracts only":**

> At least one, [PMID], states a CC BY licence in its abstract and is not in
> PMC, so an open copy may exist at the publisher; its page refused the
> scripted request. Europe PMC full text was not tried for any of the 32.

The same appendix lists the trial's PubMed number among the Q-B abstract-only
sources. "The stop rule" in the same file says, without naming the trial, "at
least one such source states a CC BY licence".

**`evidence/10-descending-modulation.md`, §6.4 "Loss of efficacy":**

> And the one blinded sham-controlled DRG stimulation trial, already described
> in E-05 §6b (Tabatabaei et al., [PMID], [registry number]), enrolled only
> established responders, measured pain over days, and registered no sensory
> testing.

The table above that sentence (row R1) and the appendix entry R1 record that
the trial's registry record was read on 2026-11-18 for its outcome titles and
descriptions, with five registered outcomes and no match for sensory-testing
terms. The repository does not record what the five outcomes are.

**`README.md`, "Status", under "What the evidence pass established":**

> A blinded sham-controlled crossover trial published in May 2026 showed dorsal
> root ganglion stimulation beating sham by 2.5 points on an 11-point pain
> scale in established responders. The target is on firmer ground than the
> frequency claim.

**`ledger/OPEN.md`, "What the programme does next", candidate P-3:**

> **P-3.** The full text of the sham-controlled crossover trial in established
> responders (Tabatabaei et al. 2026): pain under sham set against the same
> participants' pain before implant, if reported.

and, in the contamination note of the same section:

> P-2, P-3 and P-4 are not affected by this note. Their prior exposure is as
> E-11 declares it.

**`ledger/OPEN.md`, "Superseded 2026-11-19: the earlier 'what the programme
should file next'", item 3.** It does not name the trial. It reads as a
reference to it, or to it together with the two Düsseldorf trials:

> **The dorsal root ganglion frequency question**, which is the only place
> HC-3 still stands, and which now has blinded sham-controlled human support
> for the target if not yet for the frequency.

**`evidence/03-writing-the-signal.md`** does not mention the trial. Its §3
still says "No sham arm exists for DRG stimulation anywhere", and
`conjectures/C-001-drg-habituation-is-filter-fatigue.md` says "no
sham-controlled DRG trial exists anywhere". The second sentence is copied in
the panel record of that conjecture,
`pipeline/reviews/C-001-drg-habituation-is-filter-fatigue/20260831T234656Z/ballot.md`
("no sham-controlled DRG trial exists anywhere"). All three were written
before the programme knew of the trial and are corrected by E-05. A search of
`pipeline/reviews/` and `conjectures/` for "sham" found no other statement
about the existence of a sham-controlled trial of ganglion stimulation, and no
mention of this trial.

### What is therefore already known

- **The design.** One centre (Umeå). 20 established responders, enrolled on at
  least 50% relief for at least 3 months. Randomised, double-blind
  ("quadruple-masked"), two-period crossover: two 5-day periods with a 24-hour
  washout. Active stimulation below the perception threshold; sham is the
  device off.
- **The result on the 11-point scale.** Median 3.0 (IQR 2.0 to 4.0) under
  active stimulation against median 6.0 (IQR 4.0 to 7.0) under sham. Median
  difference −2.5 (95% CI −3.0 to −2.0), p<0.001.
- **Other.** Global impression and satisfaction favoured active. No serious or
  device-related adverse events. About a third carry a CRPS label. Two
  participants ended a period early. Authors consult for the manufacturer. The
  abstract states a CC BY licence. Publication date 13 May 2026.
- **Consequence for this registration.** The sham value is already known. The
  only unread half of the quantity is pre-implant pain. The prediction in §4
  is therefore, in effect, a prediction about the pre-implant pain score of
  these 20 people. That limits how novel it is, and it is said here so that no
  one has to work it out later.

**Not known to the registering agent:** whether the paper reports pre-implant
pain at all, its value, time since implant, diagnoses beyond the CRPS share,
when in the sham period pain was scored, and anything in the full text beyond
the abstract as recorded above.

### What the registering agent read, and did not

- Read, in this repository only: `PROGRAMME.md`; `EPISTEMICS.md`; `ETHICS.md`;
  `ledger/DECISIONS.md` D-003; `ledger/OPEN.md` (the E-11 entry, the next
  steps, the candidates, the contamination note, the programme review);
  `evidence/11-evidence-map.md` (the Q-B table and summary, "What reading the
  full text changed", "The stop rule", "Candidate predictions", Appendix B and
  C); `evidence/05-crps.md` (the passage on DRG stimulation with its
  2026-09-01 correction, §6 and §6b, and every line matching the search terms
  above); the matching
  lines of `evidence/03-writing-the-signal.md` and
  `evidence/10-descending-modulation.md`; `README.md` lines on the trial; the
  intent file; `.github/workflows/ci.yml`; `tools/README.md`; and
  `simulations/S-001b-tjunction-retuned/PREDICTION.md` for house style.
- **Read nothing else about the trial.** No full text, abstract, PubMed,
  Crossref, publisher, preprint or registry page was fetched, opened or
  searched for. No web request of any kind was made in the registering
  session. `tools/verify-citations.py` was not run.
- **A limit that cannot be removed.** The registering agent is a language
  model whose training data may reach mid-2026, and the paper was published in
  May 2026. The agent has no recollection of the paper beyond what the
  repository says, and it cannot prove that nothing about it was in its
  training data. The typical values used in §3 are taken from the repository,
  not from memory.
- The contamination note in `ledger/OPEN.md` concerns P-1 only. The registering
  agent was given no result for P-3 by any other session.

## 3. The reasoning, by hand, from what the repository holds

**The one direct precedent says D is zero.** E-11 row B9, from the full text
of Piedade et al. 2022 (PMID 35217898, PMC8967770): "Patients reported a mean
VAS of 8.6 (SD 1.0) before the implantation of the DRG-S system and a mean
baseline VAS of 3.9 (SD 1.9)." Under sham the mean in its Table 1 is 8.57
(SD 1.26), and its Table 2 gives the difference between pre-implant and sham as
"0.000 (n.s.)". Nineteen people, implanted for a mean of 17.2 months, four-day
blinded phases with two-day washouts; the pre-implant score came from charts.
If Umeå repeats this, D is near 0 and the prediction below is refuted.

**Why I do not expect it to repeat.** Four things in the repository.

1. *The sham value is already known, and it is low for a pre-implant score.*
   Sham median 6.0 at Umeå. The two pre-implant figures the repository holds
   for ganglion-stimulation cohorts are both above 8: 8.6 in Piedade 2022, and
   "80.6 mm at baseline" in the pivotal trial (E-11 row B1). If the Umeå
   cohort was implanted at a similar level, D is about 2 to 2.6.
2. *The entry criterion bounds pre-implant pain from below.* Enrolment needed
   at least 50% relief. The active median is 3.0. A pre-implant median of 6.0
   would put the group's median relief at exactly 50%, the floor of its own
   entry criterion; 7.0 gives 57%; 8.0 gives 62%. A group sitting on the floor
   of its entry criterion is unlikely. This is loose: relief may have been
   rated by the participant as a percentage and not computed from two scores,
   and a ratio of medians is not a median of ratios.
3. *The same centre that found equality did not find it twice.* Piedade et al.
   2023 (E-11 row B9; 17 people, five-day phases) reports sham 5.3 (SD 3.0)
   against a baseline on stimulation of 3.2 (SD 2.2), with two people who
   "could not undergo the phase of sham stimulation due to unacceptable pain".
   The repository holds no pre-implant score for that trial. A sham mean of
   5.3 against the earlier trial's 8.57 says the 2022 equality is not a stable
   property even within one centre. The Umeå sham value, 6.0 over a five-day
   period, sits with the 2023 figure.
4. *Every listed bias but one pushes D upwards.* People are implanted when
   pain is high, so a later score tends to be lower (regression to the mean).
   Only responders were enrolled (selection). A sham period that follows a
   24-hour washout cannot exclude an effect that lasts days (carry-over). A
   blinded participant may expect relief (E-03 records a sham response of
   2.92 cm on a 10 cm scale in one dorsal column trial, Al-Kaisy et al. 2018).
   Only rebound pushes the other way.

**What I expect.** A pre-implant median of 7 to 8, so D between 1 and 2, most
likely 1.5 to 2. I expect sham pain to sit clearly below pre-implant pain.

**What I think is most likely overall** is that the registration ends
unscorable: the publisher refused one scripted request already (E-11), and a
crossover trial in established responders has no need to report pain before
implant. §4 gives the numbers.

**Severity (EPISTEMICS.md §7).** This is not a severe test of any mechanism. If
it comes out SUPPORTED, the likeliest reason is the base rate (people are
implanted at high pain scores), which says little about carry-over or
progression. The informative outcome would be REFUTED: a second centre in
which pain under blinded sham returns to the pre-implant level.

## 4. The prediction

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

### Probabilities, stated before the source is read

Two steps come before any verdict.

- The full text is obtained by the declared routes, as §5 defines "obtained":
  **0.40**.
- Given that, pre-implant pain is reported in a usable form: **0.35**.

So the registration is scored with probability 0.14.

| Outcome | Given that it is scored | Overall |
|---|---|---|
| SUPPORTED | 0.40 | **0.06** |
| REFUTED | 0.10 | **0.01** |
| INCONCLUSIVE | 0.50 | **0.07** |
| UNSCORABLE (source not obtained) | n/a | **0.60** |
| UNSCORABLE (quantity not reported) | n/a | **0.26** |

The single likeliest outcome is UNSCORABLE (source not obtained).

**These figures were restated twice before the merge, and the earlier ones are
kept here.** Neither change followed any new information about the paper.

| Version | Obtained | Usable, given obtained | SUPPORTED | REFUTED | INCONCLUSIVE | Not obtained | Not reported |
|---|---|---|---|---|---|---|---|
| `0da91a6` | 0.60 | 0.40 | 0.12 | 0.04 | 0.08 | 0.40 | 0.36 |
| `570ac46` | 0.45 | 0.35 | 0.06 | 0.02 | 0.08 | 0.55 | 0.29 |
| final (above) | 0.40 | 0.35 | 0.06 | 0.01 | 0.07 | 0.60 | 0.26 |

- From the first to the second: the routes were capped at one scripted
  request each, "obtained" came to need the methods and results as text, a
  differing construct became unscorable, and an unstated construct came to
  widen the interval, which moves likely outcomes from SUPPORTED to
  INCONCLUSIVE.
- From the second to the final: the Unpaywall request was fixed to a
  placeholder address on a reserved domain (§5), which the service may
  refuse. That makes the fourth route less likely to work.

## 5. Unscorable conditions and the stop rule, written now

PROGRAMME.md requires any stop rule or threshold to be in a repository file
before the work starts. These are the rules for this registration.

### The declared routes

Four routes, tried in this order. The list is closed: no other route, service,
mirror, repository search, web search, browser session, login, library proxy or
request to an author is used. The reader stops at the first route that returns
the full text as defined below.

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

**Two registrations that end unscorable for lack of a source mean the
programme cannot generate testable predictions with existing methods, and the
question of closing goes to the owner.**

- **Where it comes from.** The independent programme review of 2026-11-19, as
  relayed to the registering agent by the coordinating session in the brief
  for this registration. The registering agent has not seen the review's own
  wording of it.
- **Where it is written.** This file is the first place the rule is written
  in this repository. A search on 2026-11-19 at commit `dfd9804` for
  "unscorable" and "two registrations" found it in no file. It is written
  here before the read, as PROGRAMME.md requires.
- **This registration is attempt 1.**
- UNSCORABLE (quantity not reported) is not "for lack of a source" and does
  not count towards the two. It is still not progress by the test in
  PROGRAMME.md.

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

## 7. Instructions for the reader (the second agent)

Do these in order. Do not skip a step, and do not change the order.

1. **Confirm the registration predates the read.** Run `git fetch origin`
   first. Then record the hash and the timestamp of three commits, with `F`
   standing for
   `predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md`:
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
2. **Obtain the full text by the declared routes only** (§5), in the order
   listed there, one request per step, with the user-agent stated there. Take
   the identifiers from `evidence/05-crps.md` §6b. Log each request: the
   route, the address, the time, and what came back (HTTP status and size,
   not content). Stop at the first route that returns the full text as §5
   defines it. If none does, write `RESULT.md` with the verdict UNSCORABLE
   (source not obtained) and the log, and stop. Do not read the abstract in
   place of the full text, do not retry with altered headers, and do not try
   any other route.
3. **Extract the numbers.** Quote verbatim, with the location (section, table
   or figure, and the row or sentence): pain under sham, with the paper's
   definition of that outcome; pain before implant, with the words that show
   it was taken before implant and the words that define it, or a statement
   that no definition is given; the number of participants behind each; the
   spread of each; any paired comparison of the two; time since implant (S1).
   Say which analysis population each belongs
   to. If pre-implant pain is absent, quote what the baseline table does
   report, and say which sections you searched and for which terms.
4. **Apply the rule in §4 mechanically.** State which method (A, B or C) and
   which special cases applied. Show the arithmetic for D, L and U. State the
   verdict in one of five forms: SUPPORTED, REFUTED, INCONCLUSIVE, UNSCORABLE
   (source not obtained), UNSCORABLE (quantity not reported). Score S1 and S2
   separately and label them secondary.
5. **Write `RESULT.md`** in this folder: the commit hash and times from step
   1, the access log, the quotations, the arithmetic, the verdict, the
   registered probabilities beside the outcome, and the limits in §6. Add
   anything the paper says that bears on Q-B and was not registered, under a
   heading that says it was not registered.
6. **Do not edit `REGISTRATION.md`.** If a rule turns out to be ambiguous,
   append an amendment under the heading below, dated, saying what was
   ambiguous, that it was written after the read, and how each reading scores.
   Change nothing above the heading.
7. **Do not** update `ledger/OPEN.md` or the evidence briefs in the same
   change unless your own brief says so. Propose the ledger line in your
   report. Do not write stimulation settings or advice in any file.

---

## Amendments (appended after the registration; the text above is not edited)

None.

### Amendment 1, 2026-11-19, by the reader

"None." above is the state at the merge and is left in place. This amendment
was written after the read was attempted, by the reader (Claude Fable 5.2),
once all four routes of §5 had been tried. No text of the source was obtained
or read; see `RESULT.md`. It changes no rule. It records two places where §5
left a choice to the reader, and how each reading comes out.

**1. Route 2 does not say which Europe PMC field means "flagged as having
full text", nor which result type to request.**

- What was done: one `search` request with `resultType=lite`, chosen because
  that result type carries no abstract. The record's flags were `inEPMC` "N",
  `inPMC` "N", `isOpenAccess` "N" and `hasPDF` "N". The reader took the
  record as not flagged, and sent no `fullTextXML` request.
- Readings: taking the flag to be `inEPMC`, `inPMC`, `isOpenAccess` or
  `hasPDF`, or any combination of them, gives the same answer: not flagged,
  no further request. The record also has `hasTextMinedTerms` "Y". The reader
  does not take that as a full-text flag, since it can be set from an
  abstract alone, and the record has no PMC identifier for a `fullTextXML`
  address. Under that reading one more request would have been sent. It was
  not sent, so its result is not known; with `inEPMC` "N" the reader expects
  it would have returned no full text, and says plainly that this is an
  expectation and not an observation.
- Outcome under the readings the reader accepts: the same, route 2 returns no
  full text.

**2. Route 4's second request had the same address as route 3's request.**

- The Unpaywall response had a `best_oa_location` with no `url_for_pdf` and a
  `url` equal to `https://doi.org/` followed by the DOI, which is exactly the
  route 3 address. Route 3 had already been refused (HTTP 403). §5 forbids
  retries with altered headers and allows an identical repeat only when no
  HTTP response came back; it also makes this request a step of its own.
- What was done: the request was sent once, as route 4 states, with the same
  headers as every other request. It was refused again (HTTP 403).
- Readings: sent once as a separate step (done), or not sent because it
  repeats a refused request. Both give the same outcome: no full text from
  route 4.

**How the readings score.** Under every reading above the outcome is
UNSCORABLE (source not obtained). The readings do not disagree, so the
ambiguity rule of §4 does not turn the outcome into INCONCLUSIVE; that rule
concerns scoring, and nothing was scored.

**Observed, for whoever writes the next registration.** The Unpaywall response
also listed a repository location. §5 says "No other location in the response
is tried", and it was not requested.
