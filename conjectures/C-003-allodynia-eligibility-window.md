---
id: C-003
title: Ongoing C-fibre activity opens a brief eligibility window during which touch is read as pain
branch: A
status: wounded
prior: 0.30
posterior: 0.62
lineage:
supersedes:
created: 2026-09-01
bears_on: HC-1, HC-3, PB-3
---

## Claim

Mechanical allodynia is a coincidence phenomenon in time. Ongoing,
touch-independent C-nociceptor discharge opens a window of a few hundred
milliseconds during which Aβ input reaching the dorsal horn is routed to the
nociceptive output pathway. Aβ input arriving outside that window is felt as
touch. The percept therefore depends on the **relative timing** of two inputs
that are each individually normal, and not on either input being abnormal.

## Why this, why now

This resolves a sharp contradiction sitting inside the evidence base, which is
the highest-yield place to look for a conjecture.

**The contradiction.** E-01 §5 records that in established allodynia the
traffic that hurts arrives on Aβ fibres **whose own behaviour is normal**, and
that the pathology is central: microglial BDNF collapses the chloride gradient
in lamina I, disinhibiting a circuit that lets Aβ input reach nociceptive
output (Coull et al., PMID 12931188 and PMID 16355225; circuit dissection in
Duan et al., PMID 25467445; PKCγ route in Lu et al., PMID 23979158).

But E-01 §5 also records the 2025 finding that inflammation leaves nociceptor
**mechanical** responses minimally affected while inducing long-lasting
touch-independent spontaneous activity in specific classes, which the authors
themselves read as suggesting allodynia arises from **coincidence** of normal
touch input with ongoing nociceptor firing (Ghitani et al., PMID 40269164).

Those are two different stories. In the first, the gate is held open
tonically by a structural change in inhibition, and timing is irrelevant. In
the second, the gate is opened transiently by ongoing nociceptor traffic, and
timing is everything. **Both are supported, and they make opposite predictions
about whether allodynia can be interrupted without changing anything
structural.**

**Why not already done.** The peripheral imaging work and the spinal circuit
manipulations come from different groups using different preparations, and no
published experiment has independently controlled the *timing* of C-fibre
activity while holding C-fibre spike count and Aβ input constant. Doing so
requires optogenetic control of one population and calibrated mechanical
stimulation of the other in the same animal, which is a combination rather than
an invention.

## Mechanism

Ongoing C-nociceptor discharge produces sustained release of glutamate and
neuropeptides onto dorsal horn interneurons. Where the tonic-disinhibition
account has this raise excitability permanently, the coincidence account has it
raise excitability **transiently**, decaying over the timescale of the
underlying synaptic and second-messenger processes, which for windup-like
facilitation is of order hundreds of milliseconds to a few seconds.

Aβ input arriving while the network is in that facilitated state crosses
threshold onto the nociceptive projection pathway. Aβ input arriving after it
has decayed does not.

The prediction that separates this from tonic disinhibition is therefore a
**decaying function of inter-stimulus interval**: pair a burst of C-fibre
activity with a light touch at varying delays and the probability of a
nociceptive response should fall as the delay grows, rather than being flat.

Timescales and magnitudes are ordinary: spike arrival on the millisecond scale,
facilitation decaying over 1e-1 to 1e0 seconds, membrane potential offsets of a
few millivolts. No exotic physics is invoked.

## Forbidden observation

The probability that a calibrated light touch evokes a nociceptive dorsal horn
response will not depend on its delay after a burst of C-fibre activity, once
total C-fibre spike count and touch intensity are held constant.

## Killer

Mouse, neuropathic or inflammatory model with established mechanical allodynia,
using optogenetic control of a defined nociceptor population so that C-fibre
spike count is set by the experimenter rather than inferred.

### The time constant is now pre-registered, and it comes from wind-up

The first version of this conjecture proposed a window of "a few hundred
milliseconds" and was correctly criticised for placing it in a gap between
paired-pulse facilitation (tens of milliseconds) and central sensitisation
(minutes to hours), with no direct evidence for a facilitation constant in
between. **That gap is not empty, and the evidence was already in the wind-up
literature.**

Wind-up is a dorsal-horn facilitation that requires repetitive C-fibre input
above a threshold *rate*, and the published rate dependence brackets the
constant directly:

- **Present at 0.5 Hz, absent at 0.1 Hz.** Chapman, Suzuki & Dickenson,
  *Anesthesiology* 1994;81:1429-35 (PMID 7992912): "At 0.5 Hz but not at 0.1
  Hz, there was an enhanced C-fiber evoked response of dorsal horn neurons
  elicited by repetitive C-fiber stimulation (wind-up), which is mediated by
  the NMDA receptor."
- Corroborated at the molecular level by frequency-dependent ERK
  phosphorylation: "high frequency (0.5 Hz and 10 Hz) but not low frequent
  (0.05 Hz) stimulus-evoked pERK" (Ji et al., *Mol Pain* 2007;3:18,
  PMID 17631690).
- And in trigeminal convergent neurons, wind-up appears in 73% of
  long-latency responses at **0.66 Hz** (Dickenson-adjacent series,
  *Eur J Neurosci* 1999;11:31-40, PMID 9987009).

**0.5 Hz is a 2-second interval. 0.1 Hz is a 10-second interval.** A
facilitation that survives 2 s and has decayed by 10 s has a time constant on
the order of **seconds**, not hundreds of milliseconds and not minutes.

**The conjecture is therefore amended rather than defended.** The claim is now
that the eligibility window has a decay constant **τ in the range 1 to 10
seconds**, centred near 3 s, and this is pre-registered as the prediction. The
original "few hundred milliseconds" is withdrawn as unevidenced. If the window
turns out to be tens of milliseconds it is paired-pulse facilitation and not a
distinct phenomenon; if it is minutes it is classical central sensitisation and
also not distinct. **The conjecture only says something new if τ lands in the
seconds band**, which is precisely why that band is now the prediction.

### Design

Deliver a fixed-count C-fibre burst, then a calibrated von Frey touch at
delays of **50, 200, 500, 1000, 2000, 5000 and 10000 milliseconds**,
randomised within animal, spanning the bracketed range with two points below it
and one above.

**Four control conditions, not one.** Gate 04 judged the single no-burst
control insufficient and put the false-pass probability at about 0.6. These
close the identified routes:

1. **No-burst control.** Establishes the baseline response probability.
2. **Aβ-burst control — the critical addition.** A matched-count optogenetic
   burst in a *low-threshold mechanoreceptor* population instead of
   nociceptors, at the same delays. This delivers an equivalent afferent
   barrage and equivalent sensory adaptation, without the nociceptive content.
   **If the delay-dependence is identical in this arm, the effect is adaptation
   or habituation and the conjecture is dead.** This is the control the first
   version lacked and it is the single largest contributor to the false-pass
   rate.
3. **Reverse-order control.** Touch first, burst second, at matched intervals.
   The conjecture predicts no effect; a symmetric effect indicates a
   non-specific arousal or state change rather than a directional window.
4. **Naive-animal control.** The same delay series in animals without
   established allodynia. The conjecture predicts a much weaker or absent
   window, since it claims the window is what allodynia *is*.

**Two timepoints after model induction**, early and late, run from the start
rather than as a follow-up. This is imported from the third rival, which
predicts coincidence dominates early and tonic disinhibition late, and which
the previous design could not have detected.

**Direct afferent recording in the same preparation**, confirming that Aβ and
C-fibre responses to the calibrated stimuli are themselves unchanged across
delays. This is imported from the second rival. If the afferents are changing,
the coincidence framing is misattributing a peripheral effect.

Read out dorsal horn projection neuron responses electrophysiologically **and**
nocifensive behaviour, in separate cohorts. **Target n=12 per group**, with the
detection floor established before collection by injection-recovery on
simulated response series through the identical fitting pipeline, reporting the
smallest τ-difference resolvable at that n.

**Refutation threshold, tightened.** The conjecture is refuted if **any** of
the following holds, with the no-burst control confirming the paradigm can
detect a difference at all:

- response probability is flat across delays, that is the fitted τ has a 95%
  confidence interval including infinity; **or**
- the fitted τ falls outside the pre-registered 1 to 10 second band with a
  confidence interval excluding it; **or**
- **the Aβ-burst control reproduces the same delay-dependence** within the
  resolvable difference established by injection-recovery; **or**
- the reverse-order control produces a symmetric effect.

Approximate cost 200,000 to 300,000 euro and 18 months, now somewhat higher
than the first version because of the added control arms, in a laboratory that
already has both the nociceptor and the low-threshold-mechanoreceptor
optogenetic lines. That pair of lines is the real constraint on where this can
run.

## Rivals

- **Tonic disinhibition, timing irrelevant.** The chloride gradient has
  collapsed, the gate is open, and any Aβ input is read as pain regardless of
  what preceded it. This is the mainstream account and it has strong support.
  *Distinguished by:* flat response probability across delays.
- **Peripheral sensitisation after all.** The Aβ fibres or the nociceptors are
  not behaving normally in the neuropathic state even if they are in the
  inflammatory one, so the coincidence framing imports a finding from the wrong
  model. *Distinguished by:* direct recording of Aβ and C-fibre responses to
  the calibrated stimuli, which this design produces anyway.
- **Both, at different disease stages.** Coincidence dominates early while
  disinhibition is incomplete, and tonic disinhibition dominates late. This is
  the most likely rival to be true and the least convenient, because it means
  the answer depends on when you look. *Distinguished by:* running the delay
  series at two timepoints after model induction, which this design should
  therefore do from the start rather than as a follow-up.

## Severity

Given the conjecture is false, the probability the proposed test still comes out
favourable is about **0.15**.

**The previous estimate of 0.2 was judged optimistic by the panel, which put it
near 0.6, and the panel was right about the design as it then stood.** The
single no-burst control could not separate the proposed mechanism from ordinary
sensory adaptation, because any burst-then-touch paradigm produces some decay
for reasons that have nothing to do with nociceptive coincidence. That is the
dominant false-pass route and it was essentially uncontrolled.

The Aβ-burst control closes it directly: it produces the same afferent load and
the same adaptation with no nociceptive content, so a decay that appears in
both arms is definitionally not the proposed mechanism. The reverse-order
control removes non-specific arousal. The pre-registered τ band removes the
freedom to read any decay whatsoever as confirmation, which was the second
largest route to a false pass and the one gate 04 named. The naive-animal arm
tests the claim that the window is specific to the allodynic state.

What remains is the possibility that optogenetic burst delivery itself produces
a delay-dependent change in dorsal-horn excitability through a route unrelated
to natural C-fibre traffic. That is not fully controlled and should be stated
as the residual risk.

## What it would change

If confirmed, allodynia becomes a **timing** problem rather than a purely
structural one, and that is the first thing in this programme that would make
temporal-pattern intervention clinically relevant rather than merely
mechanistically interesting. An intervention that suppressed ongoing
nociceptor discharge would close the window without needing to restore
inhibition, and, more usefully, an intervention that merely **desynchronised**
it might do the same.

It also bears directly on PB-3, the programme's hypothesis that night-time
mechanical allodynia has a distinct signature and therefore a distinct handle.
A coincidence mechanism would give it one.

If refuted, the tonic-disinhibition account stands alone, allodynia is
structural, and the programme should stop proposing to treat it by anything
acting on peripheral timing. That would remove the most clinically motivating
target in Branch A, which is a good reason to test it early rather than late.

## References

- Ghitani N, et al. *Nature* 2025;642:1016-23. PMID 40269164. doi:10.1038/s41586-025-08875-6
- Coull JAM, Boudreau D, Bachand K, et al., De Koninck Y. *Nature* 2003;424:938-42. PMID 12931188. doi:10.1038/nature01868
- Coull JAM, Beggs S, Boudreau D, et al., De Koninck Y. *Nature* 2005;438:1017-21. PMID 16355225. doi:10.1038/nature04223
- Duan B, et al. *Cell* 2014;159:1417-32. PMID 25467445. doi:10.1016/j.cell.2014.11.003
- Lu Y, et al. *J Clin Invest* 2013;123:4050-62. PMID 23979158. doi:10.1172/JCI70026
- Peirs C, et al. *Neuron* 2015;87:797-812. PMID 26291162. doi:10.1016/j.neuron.2015.07.029
- Mendell LM, Wall PD. *Nature* 1965;206:97-9. PMID 14334366. doi:10.1038/206097a0
- Woolf CJ. *Nature* 1983;306:686-8. PMID 6656869. doi:10.1038/306686a0
