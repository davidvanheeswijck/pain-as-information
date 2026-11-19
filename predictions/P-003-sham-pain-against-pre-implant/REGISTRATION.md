# P-003. Registered prediction: pain under blinded sham against pain before implant

**Written 2026-11-19 (about 21:00 UTC), before the source was read.** The
source is the full text of the sham-controlled crossover trial of ganglion
stimulation in established responders, Tabatabaei et al. 2026 (identifier in
`evidence/05-crps.md`, §6b). This file names the trial by author and year only,
so that no tool run over this folder fetches its record.

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

**`evidence/03-writing-the-signal.md`** does not mention the trial. Its §3
still says "No sham arm exists for DRG stimulation anywhere", and
`conjectures/C-001-drg-habituation-is-filter-fatigue.md` says "no
sham-controlled DRG trial exists anywhere". Both sentences predate the trial's
publication and are corrected by E-05.

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

Direction: sham below pre-implant. Threshold: 1.0 point. Two reference values
are used by the rule: 0 (no difference, the Piedade 2022 result) and 2.0 (the
"usual 2-point MCID" on this scale, as E-03 §1 words it). The threshold sits
midway between them.

### Verdict rule

Let D be the point estimate and [L, U] its 95% interval, both obtained as set
out under "Scoring rule".

- **SUPPORTED** if D ≥ 1.0 **and** L > 0.
  The estimate meets the threshold and "no difference" is excluded.
- **REFUTED** if D < 1.0 **and** U < 2.0.
  The estimate is under the threshold and a two-point gap is excluded.
- **INCONCLUSIVE** otherwise: D ≥ 1.0 with L ≤ 0, or D < 1.0 with U ≥ 2.0.

If the verdict is REFUTED, `RESULT.md` also says which reading of §1 the
numbers fit: "at about the pre-implant level" if the interval contains 0, and
"above the pre-implant level" if U < 0.

### All three verdicts are reachable

Three synthetic examples. None is a guess at the paper. Each uses the sham
value already known (median 6.0, IQR 4.0 to 7.0, n = 20) and the group-summary
method (C) of the scoring rule. For the sham median the standard error is
1.2533 × (3.0 / 1.35) / √20 = 0.62.

| Synthetic pre-implant score, n = 20 | D | Standard error of D | 95% interval | Verdict |
|---|---|---|---|---|
| Median 8.0 (IQR 7.0 to 9.0) | 2.0 | √(0.42² + 0.62²) = 0.75 | 0.53 to 3.47 | **SUPPORTED** (D ≥ 1.0, L > 0) |
| Median 6.0 (IQR 5.0 to 7.0) | 0.0 | 0.75 | −1.47 to 1.47 | **REFUTED** (D < 1.0, U < 2.0) |
| Median 7.0 (IQR 6.0 to 8.0) | 1.0 | 0.75 | −0.47 to 2.47 | **INCONCLUSIVE** (D ≥ 1.0, L ≤ 0) |

With spreads of this size the rule works out as: SUPPORTED from about D = 1.5
upwards, REFUTED up to about D = 0.5, INCONCLUSIVE between. A paper that
reports a paired comparison would give a narrower interval and a narrower
inconclusive band.

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
  before the permanent implant; if both are given, the earlier). The quoted
  wording must make this plain. A "baseline" taken at enrolment, with the
  stimulator already in use, is **not** pre-implant pain and is not used.
- *Scale:* 0 to 10. A 0 to 100 mm scale is divided by 10. A percentage relief
  figure is not converted into a score.
- *Which statistic:* medians if the paper gives medians for both; otherwise
  means for both; otherwise one of each (see "mixed" below).

**How D, L and U are obtained.** The first method that the paper allows:

- **(A) The paper's own paired comparison.** If the paper reports the
  difference between pre-implant and sham pain with a 95% confidence interval,
  those are D, L and U, with the sign set so that D is pre-implant minus sham.
- **(B) Per-participant values.** If the paper or its supplementary files give
  both scores for each participant, d = pre-implant minus sham is computed per
  participant; D is the mean of d, the standard error is SD(d) / √n, and
  [L, U] = D ± 1.96 × SE.
- **(C) Group summaries.** D = centre of pre-implant minus centre of sham.
  Standard error of each centre: for a mean, SD / √n; for a median,
  1.2533 × (IQR width / 1.35) / √n. If only a range (minimum to maximum) is
  given, SD is taken as range / 4. If a standard error or a confidence
  interval is given for a centre, it is used directly. If one number has no
  spread, the other number's SD is used for it. If neither has, SD = 2.2 for
  both (the sham IQR already known, divided by 1.35). The standard error of D
  is √(SE_pre² + SE_sham²), and [L, U] = D ± 1.96 × SE. n is the number of
  participants behind each number, as the paper states it.

  This treats the two scores as independent. They are paired, so the interval
  is wider than a paired one would be. That is declared and accepted: it makes
  INCONCLUSIVE more likely, not SUPPORTED. The multiplier 1.96 is used in every
  case and is approximate for 20 people.

**Special cases.**

- *Only one of the two numbers.* If the paper reports pain under sham and no
  pre-implant pain score for the trial participants, the outcome is
  UNSCORABLE (quantity not reported); see §5. The sham number cannot be
  missing, since the abstract holds it.
- *Mixed statistics* (a mean for one, a median for the other): method (C) is
  applied to the pair as given, and 0.5 is added to each side of the interval.
- *Different subsets.* If the two numbers are reported for different sets of
  participants, they are used only if one set contains the other and the
  smaller holds at least 80% of the larger (16 of 20, for example). The
  verdict then stands and the mismatch is recorded. If not, or if pre-implant
  pain is given only for a subgroup such as one diagnosis, the outcome is
  UNSCORABLE (quantity not reported).
- *Only a figure.* If a number appears only in a figure, a value printed in
  the figure is used as it stands. If none is printed, the reader reads the
  centre and the spread off the axis to the nearest 0.5, says so, and adds 0.5
  to each side of the interval. If the figure cannot be read to the nearest
  0.5, the outcome is UNSCORABLE (quantity not reported).
- *Ambiguity.* If the rule above does not decide a case, the reader does not
  choose the reading that gives a verdict. The reader appends an amendment to
  this file that states the ambiguity, scores the case under each reading, and
  reports INCONCLUSIVE if the readings disagree.

Comparisons use unrounded values. `RESULT.md` prints D, L and U to two
decimals.

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
  obtained: 0.40.

### Probabilities, stated before the source is read

Two steps come before any verdict.

- The full text is obtained by the declared routes: **0.60**.
- Given that, pre-implant pain is reported in a usable form: **0.40**.

So the registration is scored with probability 0.24.

| Outcome | Given that it is scored | Overall |
|---|---|---|
| SUPPORTED | 0.50 | **0.12** |
| REFUTED | 0.15 | **0.04** |
| INCONCLUSIVE | 0.35 | **0.08** |
| UNSCORABLE (source not obtained) | n/a | **0.40** |
| UNSCORABLE (quantity not reported) | n/a | **0.36** |

The single likeliest outcome is UNSCORABLE (source not obtained).

## 5. Unscorable conditions and the stop rule, written now

PROGRAMME.md requires any stop rule or threshold to be in a repository file
before the work starts. These are the rules for this registration.

- **UNSCORABLE (source not obtained).** The declared routes are: PubMed Central
  through NCBI E-utilities; Europe PMC full text; the publisher's open-access
  page; and one lookup of an open-access location service of the Unpaywall
  kind, following the location it returns. Supplementary files reached by the
  same routes count. If the reader cannot obtain the full text by these
  routes, the registration is closed as UNSCORABLE (source not obtained). It
  is **not** rescued from the abstract, from a secondary source, or from any
  other route.
- **UNSCORABLE (quantity not reported).** If the full text is obtained and
  does not report pre-implant pain for the trial participants in a form the
  scoring rule can use, the registration is closed as UNSCORABLE (quantity not
  reported). E-11 notes that this "would itself be worth recording"; it is
  recorded, and it is not a verdict on the claim.
- **The stop rule.** Per the programme review of 2026-11-19, as given with the
  brief for this registration: **two registrations that end unscorable for
  lack of a source mean the programme cannot generate testable predictions
  with existing methods, and the question of closing goes to the owner.** A
  search of this repository on 2026-11-19 for "unscorable" and "two
  registrations" found the rule in no file, so it is quoted as given and this
  file is where it is first written down, before the read.
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

1. **Confirm the registration predates the read.** Check that this file is on
   `main`. Record the merge commit's hash and its commit time from
   `git log --format='%H %cI' -1 origin/main -- predictions/P-003-sham-pain-against-pre-implant/REGISTRATION.md`.
   Record the time at which you start step 2. If the file is not on `main`,
   stop.
2. **Obtain the full text by the declared routes only** (§5), in the order
   listed there. Take the identifier from `evidence/05-crps.md` §6b. Log each
   attempt: the route, the request, the time, and what came back (status and
   size, not content). Stop at the first route that returns the full text. If
   none does, write `RESULT.md` with the verdict UNSCORABLE (source not
   obtained) and the log, and stop. Do not read the abstract in place of the
   full text, and do not try any other route.
3. **Extract the numbers.** Quote verbatim, with the location (section, table
   or figure, and the row or sentence): pain under sham; pain before implant,
   with the words that show it was taken before implant; the number of
   participants behind each; the spread of each; any paired comparison of the
   two; time since implant (S1). Say which analysis population each belongs
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
