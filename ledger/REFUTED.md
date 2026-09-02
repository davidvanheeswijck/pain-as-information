# The graveyard

Append-only. A refuted conjecture is closed with a reason, never deleted.

This file exists because a research programme without a graveyard is a random
walk: without it the loop rediscovers the same dead idea indefinitely, since
each round starts from the same priors that produced it the first time. It is
also read by gate 05 and gate 09 as context, so an entry here actively prevents
the next round from wasting itself.

It is public, and it includes the author's favourites. A programme built around
a family member's illness has an obvious incentive to report progress that is
not there, and this file is the counterweight. See ETHICS.md, clause 6.

## Format

Each entry:

```
### C-0NN — Title

**Refuted** YYYY-MM-DD by <gate or panel> · run `pipeline/reviews/C-0NN/<stamp>/`
**Prior** 0.NN → **Posterior** 0.NN

The killing argument, in the reviewer's own words where possible, with the
citation that carries it. Long enough that someone can tell whether a later
conjecture answers it or merely rephrases around it.

**Do not re-propose unless:** the specific condition that would revive it.
```

That last line is the useful part. Most refutations are contingent on something
being true of the world today. Saying what would have to change turns a dead
end into a standing bet.

---

### C-001 — Loss of benefit in chronic DRG stimulation is decay of T-junction filtering, not tolerance to charge

**Refuted** 2026-09-01 by five-laboratory panel · run `pipeline/reviews/C-001-drg-habituation-is-filter-fatigue/20260831T234656Z/`
**Prior** 0.25 → **Posterior** 0.15
Vote: 2 of 5 laboratories failed to refute. Median P across laboratories 0.15.

Two independent gates landed the same blow from different directions, and the
author had written the objection into the conjecture himself without noticing
it was fatal.

**The mechanism does not address the disease.** From the biological
plausibility gate, verbatim:

> The T-junction filtering mechanism is real but the conjecture treats C-fibre
> traffic as a labelled line for pain, which the evidence does not support; in
> established neuropathic pain the relevant traffic is on Aβ fibres and the
> relevant pathology is central, so gating C-fibre propagation at the
> T-junction does not address the mechanism of the disease.

This is HC-2's weak point arriving exactly where E-01 §5 said it would. Gating
nociceptor traffic is beside the point if the traffic that hurts is touch.

**The proposed experiment could not have distinguished the conjecture from its
own listed rival.** From the falsifiability gate: false-pass probability **0.5**
against the author's stated 0.15, because the killer measured C-fibre
conduction failure and never measured behavioural allodynia. The Rivals section
had said central compensation would be distinguished by "behavioural allodynia
returns while propagation failure holds steady" — a discriminator the Killer
section never actually measured. **The conjecture proposed a test it did not
specify.**

Not everything failed. Prior art returned PASS, genuinely open with a stated
delta: the idea is novel, the design was wrong. Physical plausibility returned
MINOR, asking for the homeostatic decay time constant and noting that the
entire 28-day crossover is void if filtering has not decayed by then in rat.
Clinical translation returned MINOR, noting that "vary pattern, not amplitude"
cannot be tested in a fully blinded reprogramming trial and would need a
pre-committed open-label design.

**Do not re-propose unless:** a design measures behavioural allodynia and
C-fibre propagation failure **in the same animals**, and a pilot first
establishes that T-junction filtering decays at all under chronic fixed-pattern
stimulation. The premise was never demonstrated; it was assumed. Both gates
that mattered said so independently.

**Caveat on this run, recorded because it affects how much weight the verdict
carries.** Two of eight gates failed on infrastructure (a 900 s timeout with a
retry loop that turned out to be dead for network failures), and the tally's
own gate parser was broken, so the FATAL/MAJOR logic never fired and the
verdict rests on the vote alone. All three bugs are fixed and the tally above
was regenerated with the corrected parser. The vote of 2 of 5 is unaffected.

---

### C-004 — Velocity-domain matched filtering can recover an evoked C-fibre magnetic component from a superficial nerve

**Refuted** 2026-09-01 by forward simulation · `simulations/C-004-velocity-beamforming/`
**Prior** 0.20 → **Posterior** 0.07

**The programme's first generated result rather than reviewed one, and it is
negative.** The conjecture proposed a EUR 250,000 to 400,000 human experiment.
The simulation that killed it cost about a day of compute, which is the entire
argument for insisting on a cheap kill before hardware.

**The result.** The velocity-domain ridge in the C band sits at **z = 1.71**
against a noise-only null distribution computed through the identical pipeline:
observed peak energy 2.255e-25 T², null 95th percentile 2.290e-25 T². It sits
on the null, not above it.

**The positive control passed, so this is a real negative and not a broken
pipeline.** The Aβ ridge was recovered at 48.3 m/s with velocity-domain SNR
250, single-fibre velocity recovery was accurate to 0.63%, and amplitude
calibration produced 4.5 pT at 6.5 mm against Bu et al.'s measured ~1 pT, which
is the expected direction and magnitude of error for a model that ignores
volume-conductor return currents.

**The number that matters for anyone reading this later.** The noise sweep puts
the detectability threshold at about **1.58 fT/√Hz**. Helium-4 magnetometers,
the only class with the bandwidth the conjecture assumed it needed, sit near
43 fT/√Hz, roughly 27 times too noisy. The best research alkali OPMs reach
about 1 fT/√Hz and would clear the sensitivity bar but are specified to
150-350 Hz.

**The prediction was pre-registered.** `PREDICTION.md` in the simulation
directory was written before any output existed. It called the noise threshold
at "1 to 5 fT/√Hz" against a measured 1.58, and called the Aβ control and the
hardware conclusion correctly. It was **wrong** that time-domain averaging
would show nothing: the model gives SNR 4.9 for the C band, which is an
artefact of modelling only white sensor noise.

**Do not re-propose unless** one of these changes:

1. ~~**The bandwidth premise is wrong**, which is the live escape route.~~
   **RESOLVED 2026-09-01, same day. The escape route was correct and it did not
   save the conjecture.** C-band signal energy is 90% below 29.7 Hz and 99%
   below 106 Hz, against Aβ at 90% below 557 Hz, so the kilohertz requirement
   is real for myelinated volleys and was wrongly carried over to C-fibres. A
   350 Hz alkali magnetometer has ample bandwidth. **The stated reason for this
   refutation was therefore false: the quiet sensors are fast enough.**
   But an 18-seed ensemble shows the conjecture still fails, for a different
   reason: detectable against sensor noise alone (mean ratio 1.246, CI
   [1.178, 1.314], 18/18 seeds), **not detectable against realistic
   interference** (mean 0.731, CI [0.649, 0.814], 1/18 seeds; with mains notch
   0.783, 2/18). See `simulations/C-004-velocity-beamforming/results/sensor-realism/ENSEMBLE.md`.
   **The barrier is interference rejection, not sensitivity and not bandwidth**,
   which is what E-04 §3.1 warned and this simulation independently reproduced.
   Note also that the single-seed run printed "OVERTURNED" on the strength of
   what turned out to be a 1-in-18 outlier.
2. A sensor appears that is simultaneously below about 1.6 fT/√Hz and fast
   enough for the true C-band spectral content.
3. Someone models the volume-conductor return currents and finds the external
   field is larger than this model's idealisation suggests, which would be
   surprising, since ignoring return currents should over-estimate rather than
   under-estimate the external field.

**One honest limitation, disclosed in the simulation's own approximation 7.**
Only white sensor noise is modelled. Real magnetoneurography is limited by
cardiac, muscular and environmental interference, which the evidence base
states explicitly. That makes this negative **conservative**: if beamforming
fails against pure sensor noise it fails harder against real interference. It
also means the apparent time-domain detection at SNR 4.9 is not real.

---

### C-005 — A human C-nociceptor carries under 30 bits per second, with little information in fine timing beyond rate

**Refuted** 2026-09-01 by five-laboratory panel · run `pipeline/reviews/C-005-nociceptor-information-rate/20260901T004323Z/` · superseded by [C-007](../conjectures/C-007-timing-adds-nothing-beyond-rate.md)
**Prior** 0.45 → **Posterior** 0.25
Triage returned FATAL (`WRONG QUESTION`), which is dispositive under the
scoring rule regardless of the vote. The vote was 2 of 5 failing to refute.

**Refuted as posed, not as motivated.** The gap it identified is real and the
reformulation is now C-007.

**The objection, and it is correct.** An information rate is only defined
relative to a stimulus ensemble. "A C-nociceptor carries 30 bits per second" is
not a property of the axon, it is a property of the axon together with the
distribution of stimuli presented, so two honest laboratories could report
different numbers without either being wrong. Worse, the absolute figure was
never what the programme needed: HC-1 asserts structure **beyond mean rate**,
which is a comparative claim. Triage's reformulation, verbatim:

> For a specified stimulus ensemble, does sub-5-millisecond spike timing add
> information about pain-relevant stimulus features or perception beyond firing
> rate and unit identity?

That is better posed and cheaper to answer, because comparing two decoders on
identical data cancels the ensemble and most of the estimator bias.

**Do not re-propose unless:** the claim is comparative rather than absolute, and
the stimulus ensemble is specified.

---

#### A scored false positive from gate 03, recorded because panel reliability is data

The evidence-integrity gate returned **MAJOR**, asserting that Werland et al.
(PMID 33369733) "is cited to claim C-nociceptors follow 100 Hz without
conduction failure, which is a direct inversion of the study's actual
findings."

**The accusation is false.** The abstract states, verbatim: *"polymodal
C-nociceptors in the pig follow stimulation at up to 100 Hz without conduction
failure"*, and the results give *"untreated polymodal nociceptors with moderate
ADS (15.2% ± 10.2%) followed stimulation frequencies of 100 Hz without
conduction failure (98.5% ± 6%)"*. E-01 §1 and C-005 both state this
accurately. There is no inversion. Checked by fetching the abstract from
PubMed rather than by argument.

There is a weaker legitimate criticism available, that this is *electrical*
stimulation in *pig* and does not license an inference about natural
stimulation in humans. The gate did not make that argument; it asserted a
factual inversion that does not exist.

**Why this is in the ledger rather than quietly discounted.** A MAJOR verdict
is a claim, not a finding, and this one would have corrupted a correct passage
in the evidence base had it been obeyed. The harness has no mechanism for
scoring its own reviewers, which is now recorded as a known gap in
[OPEN.md](OPEN.md). Until it does, **every FATAL and MAJOR gets checked against
the source before it is acted on**, and the check is cheap: this one took a
single API call.

---

### C-002 — Magnetic field modulation of antinociception is radical-pair mediated and shows a magnetic isotope effect

**Refuted** 2026-09-01 by a cheap-kill literature check ordered at triage · superseded by [C-006](../conjectures/C-006-flavin-13c-magnetic-isotope-effect.md)
**Prior** 0.12 → **Posterior** 0.05

Refuted **as written**. The underlying radical-pair question survives and is
carried forward; the ²⁵Mg implementation is dead.

**The objection that was raised was wrong.** Triage argued that ²⁵Mg is
quadrupolar and that fast relaxation in a distorted site would average the
hyperfine away. On the numbers it does not. The worst measured protein-bound
²⁵Mg relaxation in the literature is T₂ ≈ 31 µs in an enzyme ternary complex
with a deliberately strained coordination sphere, and 472 µs in the binary
complex (Ehrlich & Colman, PMID 7819280), against a radical-pair window of
about 1 µs. That is 30 to 470 times too slow to matter.

**Two better reasons killed it, and the gate missed both.**

*Magnesium has no unpaired spin density, so no hyperfine, so no magnetic
isotope effect is possible in principle.* Closed-shell Mg²⁺ cannot carry the
effect, so the design silently presupposed a Mg⁺• radical. That is precisely
the contested step: the magnesium isotope literature failed independent
replication (Crotty et al., PMID 22198842), with Hore's adjudication noting
"scant evidence that Mg has any biologically relevant redox chemistry"
(PMID 22307585). A null would therefore have been uninformative, which
**destroyed the conjecture's own claim to be decisive in both directions** —
the sole justification for filing a Branch C conjecture at all.

*The field range and the isotope were physically incompatible.* The ²⁵Mg⁺
hyperfine constant is −596.254376(54) MHz, about 21.3 mT, giving an effective
hyperfine field of order 63 mT. The conjecture proposed 10 µT to 1 mT: two to
four orders of magnitude apart. Every claimed magnesium effect in the
literature sits at 3 to 80 mT and none at microtesla, which should have been
the tell.

**Do not re-propose unless:** the isotope carries unpaired electron spin
density at a radical centre, the applied field range matches that isotope's own
hyperfine scale, and a null result would be interpretable. C-006 satisfies all
three by moving to ¹³C on flavin.

**Worth keeping for the method, not just the result.** The gate's objection was
wrong and the check it triggered was still worth running, because it surfaced
two fatal problems nobody had raised. A cheap kill is valuable even when its
stated reason is mistaken.

### C-006 — A carbon-13 magnetic isotope effect is detectable on a purified flavin radical pair at the bench

**Refuted** 2026-09-01 by panel · superseded C-002 · branch C
**Prior** 0.35 → **Posterior** 0.55

**The posterior rose while the conjecture died, and both are correct.** The
panel judged the bench experiment *more* likely to detect a real effect than
filed. It killed the conjecture on a different axis entirely.

**What killed it.** Gate 02, biological plausibility, returned **FATAL**: the
flavin-tryptophan radical pair requires **photoexcitation** and is validated
only in avian cryptochrome magnetoreception. No mechanism was proposed or
evidenced by which such a radical pair forms in mammalian nociceptive neurons.
The conjecture was filed as the calibration step for a biological magnetic
isotope claim, and it cannot calibrate anything if the pair it calibrates
does not occur in the tissue of interest.

The physics was sound. The quantitative audit stands: a single ¹³C at flavin
C4a gives a hyperfine of about 1.43 mT against a pair B½ of 1.89 to 2.46 mT, a
perturbation of the same order as the system's entire field scale, with a 0.13%
mass change that cannot carry a classical kinetic isotope effect. Gates 04, 05
and 07 all returned PASS. **The bridge to the nervous system was simply never
built**, and C-002 had the identical defect in a different place.

**This is the second consecutive Branch C conjecture killed for the same
structural reason:** a well-designed physics measurement with no demonstrated
instance of the physics in nociceptive tissue.

**Do not re-propose unless:** a radical pair is demonstrated to form in
mammalian sensory neurons **without** exogenous photoexcitation, at a
concentration and lifetime compatible with a magnetic field effect. Absent
that, Branch C has no biological anchor and further bench conjectures in it
are premature regardless of how good the bench design is.

**Caveat on this verdict:** the hostile-referee gate did not run (see D-H1 in
[OPEN.md](OPEN.md)). A gate-02 FATAL is decisive on its own, so re-running is
optional, but the record should show the panel was incomplete.

---

### C-007 — For a specified stimulus ensemble, sub-5-millisecond spike timing adds no information beyond rate and unit identity

**Refuted** 2026-09-01 at triage · superseded C-005 · branch A
**Prior** 0.40 → **Posterior** 0.32

**Refuted as posed, for the second time in a row, and the reformulation is
again worth more than the conjecture.** C-005 was killed at triage as the wrong
question and reformulated into C-007. Triage then judged **C-007 still the
wrong question** and supplied another:

> "For a specified stimulus ensemble, does within- or **across-fibre**
> spike-train structure improve prediction of **perceived pain quality or
> intensity** beyond firing rate and recruited-unit identity?"

Two changes, both material. The outcome moves from *information about the
stimulus* to *prediction of the percept*, which is what the programme actually
cares about and what HC-1 actually asserts. And it admits **across-fibre**
structure, which the single-unit design excluded by construction.

**Gate 02 made the point that matters most for the whole programme**, and it
should be read as a constraint on Branch A rather than only on this conjecture:
the conjecture's outcome **cannot bear on HC-1 or HC-2 for neuropathic pain**,
because in that state the pain-relevant discrimination is constructed centrally
from peripherally indistinguishable traffic. A healthy-volunteer single-unit
design cannot distinguish "timing carries no information" from "timing carries
information only in populations". So the experiment as designed could not have
answered the question it was filed to answer, whichever way it came out.

Gate 01 added a hard methodological requirement the design lacked: an
injection-recovery demonstration of the **detection floor** at n=20 units by
30 repeats, through the identical pipeline, before the 20% threshold means
anything. Gate 04 noted the discriminating requirements sit in Rivals rather
than in the Killer.

**Do not re-propose unless:** the design records **simultaneously from two or
more identified units**, predicts a **perceptual** report rather than stimulus
identity, and carries a pre-registered detection floor established by
injection-recovery. A single-unit stimulus-decoding study should not be filed
in this programme again; that is now three conjectures killed on variants of
the same error.

**Caveat on this verdict:** the hostile-referee gate did not run (see D-H1 in
[OPEN.md](OPEN.md)).

---

---

### C-008 — Gradiometric interference rejection, not sensor sensitivity, is what blocks magnetic detection of C-fibre traffic

**Refuted** 2026-09-01 by simulation, 18 seeds · lineage C-004 · branch B
**Prior** 0.35 → **Posterior** 0.18

**Refuted, and it is the most productive refutation in the programme so far,
because it replaced a false dichotomy with a costed specification.**

First- and second-order gradiometry leave the C-band detectability ratio at
**0.638 [0.516, 0.759]** and **0.663 [0.524, 0.801]**, both excluding 1.0,
while the Aβ positive control passes **18/18** at ratios of 15,731 and 3,321.
Reference regression lost the positive control and is inconclusive.

**The conjecture's premise was right in the regime it measured and wrong as a
general claim.** Sweeping sensor noise from 1.0 to 0.05 fT/√Hz moved
detectability not at all, which is exactly what C-008 predicted. But that flat
sweep is an artefact of the interference-limited regime: gradiometry suppresses
interference by 287,000× in energy and still lands **17× short** of the
C-fibre signal, so the sensor floor was never what the measurement was
touching.

**Fix the interference and sensitivity immediately becomes binding.** At gain
matching of 1:33,000, with the local muscle term removed, improving the sensor
from 1.0 to **0.2 fT/√Hz** takes detectability from 0.948 to **4.718, 8/8
seeds**. "Sensitivity buys nothing" is true before you fix the interference and
false after. The conjecture measured the first and legislated for the second.

**Rival 2 was wrong, and building it was how we found out.** C-008 named local
muscular interference as the most likely failure route and noted the simulation
did not model muscle at all. It was added, at an amplitude consistent with the
one relevant measurement (PMID 40542043). Zeroing it leaves the C-band at
0.578, slightly *worse*. Muscle is not the blocker.

**Do not re-propose unless** the design carries all three requirements
together, because any one of them alone fails: channel matching **better than
about 1:3,000**, local myogenic interference controlled, and a sensor at
**0.5 fT/√Hz or better**. A conjecture proposing any single one of these has
already been tested and refuted here.

**The joint sweep gives the exchange rate**, which is the practically useful
output: 1:3,333 matching with a 0.2 fT/√Hz sensor gives 1.79 [1.34, 2.24], and
1:10,000 matching with a 0.5 fT/√Hz sensor gives 1.42 [1.15, 1.70]. The two are
exchangeable. **A 1 fT/√Hz sensor never suffices at any matching tested**, best
cell 0.967 [0.896, 1.038], which is the cleanest negative available and rules
out ordinary commercial OPMs regardless of array engineering.

**Branch B is not closed.** C-008 predicted its own refutation would close it.
Instead the refutation costed it. The remaining question is a trade-off surface
between sensitivity and array balancing, not a yes or no.

**Method note worth keeping.** Three anti-rigging measures decided this result,
and without any one of them the simulation would have confirmed the conjecture:
interference was given real spatial structure rather than C-004's uniform
field; per-sensor gain mismatch was added, and its omission in the first draft
produced an Aβ ratio of 7,991, the signature of a null collapsed to machine
precision; and the muscle source was modelled even though it turned out not to
matter.

---

### C-003 — Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain

**Refuted** 2026-09-02 by panel, second review · branch A
**Prior** 0.30 → **Posterior after first panel** 0.62 → **Posterior** 0.15

**The only conjecture in this programme whose probability ever rose under
review, and it did not survive the rematch.** Five of five laboratories voted
REFUTED, median P(substantially correct) 0.15.

**The killing argument is not the panel's. It is two papers the panel's own
triage gate told us to go and find**, at a cost of two PubMed queries against
the 200,000 to 300,000 euro study the conjecture proposed.

*The mechanism was measured in 1993.* Thompson, Woolf & Sivilotti,
*J Neurophysiol* 1993;69:2116-28, PMID 8350135. Conditioning one dorsal root
while testing another: "conditioning at A beta-fiber strength had no effect,
whereas A delta- and C-fiber strength conditioning were equally effective", and
"Heterosynaptic facilitation of only A beta- or A delta-fiber-evoked Test EPSPs
was observed, no enhancement of C-fiber strength Test EPSPs could be
demonstrated." **That is the conjecture's mechanism and its selectivity. It is
also the Aβ-burst control that the rewritten Killer offered as its single
largest innovation, and it was run and passed thirty-three years ago.**

*The timing was measured too, and the conjecture had it wrong twice.* Single
Aδ/C-strength slow EPSPs "lasted for 4-6 s" and the cumulative depolarisation
"slowly decayed back to the control Vm over tens of seconds", with facilitation
decaying in parallel. C-003 v1 proposed "a few hundred milliseconds", wrong by
one to two orders of magnitude. The v2 rewrite proposed 1 to 10 seconds, which
is the low end of the measured range and was derived by a bad inference anyway
(see below).

*And the necessity question was answered before triage could ask it.* Ghitani
et al., *Nature* 2025;642:1016-23, PMID 40269164, states verbatim: "suggesting
that tactile allodynia results from the continuing firing of nociceptors
**coincident with touch**. Indeed, we have demonstrated that **nociceptor
activity is both necessary and sufficient** for inflammatory tactile
allodynia." Triage's reformulated question was whether spontaneous C-nociceptor
activity is necessary. For the inflammatory model, that is published.

**So the space C-003 occupied is closed from both sides**: the facilitation
mechanism and its time course from 1993, necessity and sufficiency from 2025.
What was left was a specific decay constant, and the conjecture got it wrong.

### Three findings about the harness, recorded because they are the reusable part

**1. An internal contradiction survived a rewrite and only a gate caught it.**
The v2 Killer explicitly withdrew "a few hundred milliseconds" as unevidenced
and pre-registered 1 to 10 seconds. **The title and the Claim were never
updated** and still asserted a few hundred milliseconds. Triage found it. This
is the derived-text failure mode: the reasoning was fixed and the thing derived
from it was not.

**2. The inference from wind-up was unsound, and the gate said so precisely.**
The v2 rewrite derived a decay constant from wind-up's induction-frequency
threshold, arguing that facilitation present at 0.5 Hz and absent at 0.1 Hz
brackets it to seconds. Triage: "induction-frequency thresholds do not
determine relaxation time." That is correct. A threshold for cumulative
summation is not a relaxation constant, and the honest source for the timing
was a direct measurement, which existed.

**3. Gate 03 produced the same false positive twice, with two different
models.** In the first panel it claimed Ghitani et al. "does not propose
coincidence"; in the second, that it "only reports spontaneous activity". The
abstract says "coincident with touch" verbatim and asserts necessity and
sufficiency. **Both objections are wrong, and the conjecture's citation of that
paper was accurate on both occasions.** Two independent laboratories generating
the same wrong reading of the same source is a property of the gate prompt or
of the source's phrasing, not of one model, and it should be treated as a
standing caution when gate 03 fires on a *Nature* abstract.

**Do not re-propose unless** the claim is about something Thompson 1993 and
Ghitani 2025 jointly leave open. Candidly, that is narrow: the trial-by-trial
*timing* coupling under natural unstimulated conditions in an **established
neuropathic** model, as opposed to acute inflammatory, in adult rather than
neonatal tissue. A conjecture proposing to demonstrate coincidence, or
necessity, or the fibre selectivity, is re-running published work.

---

### C-009 — An ultrasound-guided peripheral nerve block abolishes pain in long-duration CRPS, as it does in peripheral nerve injury

**Refuted** 2026-09-02 by panel · branch A
**Prior** 0.45 → **Posterior** 0.15

**Killed by a FATAL from the hostile-referee gate, which was the first verdict
that gate has ever successfully returned** (see D-H1 in [OPEN.md](OPEN.md)). It
earned its keep on its first working run.

**The core defect: the design cannot do what the claim requires.** A complete
sensory block removes *all* afferent traffic, ordinary touch included.
Abolition of pain is therefore equally consistent with a pathological
peripheral generator and with central reinterpretation of entirely normal
input. Triage said this first and the hostile referee sharpened it to a FATAL
at 97% confidence: "complete sensory block makes the allodynia endpoint
non-diagnostic and cannot identify a pathological peripheral generator."

**Four further hits, each correcting a specific overreach:**

- **The "gain versus generator" dichotomy is not exhaustive.** Verbatim: "A
  recurrent central network can be both pathologically altered and
  input-dependent; 'gain' versus 'generator' is not an experimentally
  exhaustive distinction." The conjecture was built on a false binary.
- **The spatial mismatch, from gate 01.** "a 1-3 cm local block is being used to
  exclude generators distributed over roughly 10-30 cm of peripheral/DRG
  anatomy, an approximately one-order-of-magnitude spatial shortfall, and **it
  cannot intercept DRG-origin traffic**." This is decisive for the population
  the programme cares about, since the dorsal root ganglion is precisely where
  its own evidence points. A negative result would have been uninterpretable.
- **Wrong hard-core attribution.** Gate 02: "remove the claim that a positive
  result bears on HC-2; the experiment tests **input-dependence, not peripheral
  readability**." Correct. HC-2 is about decoding a signal, not about whether
  a signal is required. The `bears_on` field was wrong.
- **Overreach in the consequences section.** The conjecture claimed a positive
  result would mean "every peripheral intervention this programme has
  considered is aimed at a real target". Verbatim reply: "Blocking an entire
  mixed nerve does not validate every peripheral intervention, any more than
  general anaesthesia validates every cortical drug target." Confidence that
  this alone sinks credibility: 94%.

Gate 04 independently put the false-pass probability at **0.45** against the
stated 0.2, which the severity section had already under-argued.

**What survives, and it is worth more than the conjecture was.** The hostile
referee's required counterweight names the defensible version explicitly:

> "**spontaneous**, not stimulus-evoked, pain in rigorously adjudicated
> long-duration CRPS remains acutely dependent on peripheral nerve transmission
> in a substantial and reproducible **subgroup**. That is clinically and
> biologically plausible, and the Haroutounian result makes it worth testing."

With the conditions it also names: preregistered multicentre crossover, a
credible expectancy control, anatomical coverage established **independently of
pain response**, spontaneous pain as the sole mechanistically interpretable
acute endpoint, explicit responder-mixture modelling, and prospective evidence
that the acute response predicts durable benefit from a predefined peripheral
treatment.

And the limit on what even that would buy: "It still would not establish
pathological nociceptor discharge, validate HC-2, or prove that central
sensitisation is merely 'gain'."

**Do not re-propose unless** the claim is a **stratification biomarker** claim
rather than a mechanism claim: that acute input-dependence of spontaneous pain
identifies a subgroup who benefit durably from a predefined peripheral
treatment. That is a prediction about treatment response, it is falsifiable
against outcomes rather than against interpretation, and it does not require
the gain-versus-generator dichotomy to be true.

**Clinical note.** The patient-facing summary derived from this conjecture was
corrected on the same day to remove the peripheral-versus-central framing, to
state that a negative result is weakly interpretable if the generator is at the
dorsal root ganglion, and to record that the allodynia endpoint is
uninformative under complete block because numb skin cannot be brushed. The
derived document had inherited the conjecture's overreach, which is the failure
mode this programme has now seen three times.
