# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `05-prior-art.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-01T12:34:14+00:00 · tokens in=7887 out=6796
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Ledger check

C-003 is not a literal restatement of a ledger entry, but it encounters the central objection that killed **C-001**:

> “The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease.”

C-003 partly answers this: Aβ remains the test channel, while C-fibre activity is proposed as a conditioning input to a central circuit. It also includes both spinal and behavioural outcomes, correcting C-001’s failure to measure allodynia.

It does **not**, however, answer the disease-maintenance objection. Showing that an artificial C-fibre burst can transiently enhance an Aβ response establishes **sufficiency for facilitation**, not that spontaneous C-fibre firing is necessary for established allodynia. A tonically disinhibited spinal cord can still exhibit additional C-conditioned facilitation. Thus a decaying delay curve would not distinguish the conjecture from its stated tonic-disinhibition rival.

The ledger’s same-animal requirement is also not met: C-003 proposes electrophysiology and behaviour “in separate cohorts,” and does not actually specify simultaneous measurement of spontaneous peripheral C activity.

## Established field and established name

This belongs to **spinal central sensitization**, specifically:

- **C-fibre-conditioned heterosynaptic facilitation**
- **conditioning–test stimulation**
- **wind-up / post-tetanic facilitation of dorsal-horn responses**
- **unmasking of low-threshold mechanoreceptive input**

“Eligibility window” is borrowed terminology and is potentially misleading. In neuroscience, an eligibility trace usually denotes a temporary synaptic state that determines subsequent plasticity or reinforcement. The immediate response-gating phenomenon proposed here is conventionally described as **heterosynaptic facilitation after C-afferent conditioning**.

## Canonical prior work

The broad experiment and mechanism considerably predate optogenetics.

1. **Mendell and Wall, 1965** showed frequency-dependent “wind-up” of dorsal-horn neurons during repeated activation of unmyelinated afferents. This established that identical peripheral volleys can produce progressively different spinal output because of recent C-fibre history.

2. **Woolf, 1983** demonstrated a central component of post-injury hypersensitivity: innocuous input could produce enhanced responses after injury-induced spinal sensitization.

3. **Woolf and Wall, 1986**, *Relative effectiveness of C primary afferent fibers of different origins in evoking a prolonged facilitation of the flexor reflex in the rat*, directly used afferent conditioning to induce prolonged facilitation. The important word is **prolonged**: the literature does not generally support a uniquely sub-second gate.

4. **Cook, Woolf, Wall and McMahon, 1987**, *Dynamic receptive field plasticity in rat spinal cord dorsal horn following C-primary afferent input*, showed that C-afferent input changes subsequent dorsal-horn responsiveness and recruits previously ineffective mechanoreceptive inputs.

5. Human capsaicin studies, especially **Torebjörk, Lundberg and LaMotte, 1992**, showed that ongoing nociceptor activation can induce central changes under which input carried by myelinated mechanoreceptors becomes painful.

Accordingly, the proposition “recent C-fibre activity changes whether subsequent mechanoreceptive input reaches nociceptive output” is established prior art. Ghitani et al. 2025 apply this general structure to identified inflammatory nociceptor populations and spontaneous activity; they did not originate the conditioning/facilitation concept.

## What is actually new

The defensible delta is:

> **Cell-type-specific optogenetic C-afferent conditioning with fixed spike count, followed by a randomized Aβ/touch delay sweep and both projection-neuron and behavioural readouts in established allodynia.**

That is an incremental experimental refinement. It is not a new theory of allodynia.

The proposed disease-stage comparison could also be valuable, but only if inflammatory and neuropathic models are treated as separate hypotheses rather than pooled alternatives.

## Important prior negative and limiting evidence

### 1. The expected facilitation often lasts much longer than proposed

Classic central-sensitization effects can persist for seconds, minutes, or longer after C-afferent conditioning. A fitted decay between 50 and 3,000 ms may therefore characterize ordinary short-term synaptic summation while missing the state responsible for allodynia.

A negative result in that interval would not refute a longer-lived C-driven sensitization mechanism.

### 2. A delay effect does not discriminate tonic disinhibition

The proposed alternatives are not exclusive:

\[
\text{response} =
\text{tonic disinhibition}
+
\text{transient C-conditioned facilitation}.
\]

A neuropathic animal with collapsed chloride inhibition can still show a declining response after an added C burst. Therefore:

- a declining curve does not establish that allodynia is a coincidence phenomenon;
- a flat curve does not establish tonic disinhibition unless the conditioning stimulus is independently shown to engage the relevant circuit;
- neither result tests whether endogenous spontaneous C activity maintains baseline allodynia.

The decisive experiment requires **necessity**, for example selective silencing of spontaneous C activity while preserving mechanically evoked Aβ input, followed by restoration using replayed spike trains.

### 3. The conditioning input is not “individually normal”

A synchronous optogenetic burst is not equivalent to naturally distributed spontaneous firing across nociceptors. Synchrony itself can produce nonlinear transmitter release, peptide release, NMDA recruitment, and dendritic summation.

At minimum, the study needs:

- synchronous burst versus asynchronous/Poisson replay;
- identical cell count and total spike count;
- C-burst-only trials at each response-measurement latency;
- opsin-negative controls;
- measurement of the naturally occurring spontaneous trains used to construct the replay.

Without those conditions, a positive result may simply rediscover the known potency of synchronous C-afferent conditioning.

### 4. Inflammatory and neuropathic allodynia cannot be treated interchangeably

Ghitani et al. concern inflammatory spontaneous nociceptor activity. Coull, Duan, Lu and related circuit work concerns neuropathic disinhibition and altered spinal routing. A result in an inflammatory model does not settle established neuropathic allodynia, and vice versa.

The conjecture should be narrowed to one model initially. The inflammatory version is better motivated by the cited 2025 evidence.

### 5. Human secondary allodynia is not normally trial-locked to individual C spikes

Capsaicin and injury paradigms produce secondary mechanical allodynia that outlasts individual nociceptor discharges by far more than hundreds of milliseconds. This does not exclude maintenance by continuing peripheral activity, but it argues against presenting the phenomenon as a brief, isolated coincidence window without first separating:

- immediate heterosynaptic facilitation;
- wind-up;
- induction of central sensitization;
- maintenance of central sensitization.

## Patents and industry

The relevant patent landscape is crowded for **temporally patterned and closed-loop neurostimulation**, but not for the specific biological claim.

- **Abbott BurstDR / Proclaim** commercialized burst-pattern spinal stimulation derived from Dirk De Ridder’s work. It varies temporal pattern but does not measure endogenous C-fibre activity or time intervention to C–Aβ coincidence.
- **Nevro HFX/Senza** commercialized high-frequency spinal stimulation. Its large waveform patent portfolio, including litigation with Boston Scientific, shows that frequency and pattern are mature commercial territory.
- **Saluda Medical Evoke** uses evoked compound action potentials for closed-loop spinal-cord stimulation. It regulates recruitment despite posture and electrode changes; it does not decode nociceptor timing.
- **Medtronic RestoreSensor/Intellis/Inceptiv** developed adaptive or closed-loop stimulation using posture or evoked responses.
- **Boston Scientific and SPR Therapeutics** have extensive programmable-pattern and peripheral-stimulation portfolios, again without the proposed endogenous C-conditioning mechanism.

These programmes mean that “vary stimulation in time” and “closed-loop stimulation based on neural responses” are not patentably novel at a high level. The possible novelty lies in the biomarker and control rule: detecting or suppressing a defined C-conditioned period during which Aβ input is converted into pain.

No directly relevant device appears to have reached a pivotal trial using that rule. It would therefore be wrong to cite commercial SCS success as evidence for this mechanism.

A useful caution is **Hara et al., JAMA 2022**, a sham-controlled trial in which burst spinal-cord stimulation did not significantly improve disability over placebo stimulation in chronic radicular pain after lumbar surgery. That trial does not refute C-003, but it does refute the loose inference that a biologically plausible temporal waveform necessarily confers clinical benefit. Saluda’s ECAP-controlled stimulation has stronger clinical evidence, but it solves dose stability, not temporal nociceptive routing.

I found no directly relevant “approved and subsequently withdrawn” device whose withdrawal tested this coincidence hypothesis. Device withdrawals and company failures in this area have generally involved hardware, battery, financing, or broad efficacy issues rather than C–Aβ timing.

## Assessment of the proposed killer

The current experiment would probably reproduce known C-conditioned facilitation, but it would not kill or confirm the disease-level conjecture.

A more discriminating sequence would be:

1. Record spontaneous activity from the nominated C-nociceptor population in the allodynic state.
2. Selectively silence that activity without blocking Aβ transmission.
3. Test whether calibrated touch ceases to evoke projection-neuron activity and behaviour.
4. Replay the measured C trains optogenetically, comparing naturalistic asynchronous replay with synchronous spike-count-matched bursts.
5. Vary touch phase relative to the replay.
6. Run tonic-disinhibition measurements or manipulations in the same preparation.
7. Test induction and maintenance separately.

The key comparison is not merely finite versus infinite fitted decay constant. It is whether timing explains touch responses **beyond baseline sensitization, total C spike count, and tonic inhibitory state**.

## Novelty classification

**INCREMENTAL.**

The central claim is old under the name **C-fibre-conditioned heterosynaptic facilitation in central sensitization**. The incremental contribution is the cell-type-specific, spike-count-controlled delay experiment motivated by Ghitani et al.’s identified spontaneous nociceptor populations.

The manuscript should stop saying that timing control has not been done without qualifying that statement. Electrical conditioning–test experiments did it in broad form decades ago. What apparently remains less explored is the stated cell-type-specific and naturalistic-replay version in established inflammatory allodynia.

## Five works to read next

1. **Cook AJ, Woolf CJ, Wall PD, McMahon SB. Nature. 1987;325:151–153. “Dynamic receptive field plasticity in rat spinal cord dorsal horn following C-primary afferent input.”**  
   The closest classical antecedent: C-afferent conditioning changes how subsequent mechanoreceptive input is represented.

2. **Woolf CJ, Wall PD. J Neurosci. 1986;6:1433–1442. “Relative effectiveness of C primary afferent fibers of different origins in evoking a prolonged facilitation of the flexor reflex in the rat.”**  
   Establishes the conditioning–test paradigm and warns that the relevant facilitation may be prolonged rather than a sub-second window.

3. **Torebjörk HE, Lundberg LER, LaMotte RH. J Physiol. 1992;448:765–780. “Central changes in processing of mechanoreceptive input in capsaicin-induced secondary hyperalgesia in humans.”**  
   Human evidence that nociceptor conditioning changes the perceptual meaning of later myelinated mechanoreceptor input.

4. **Sandkühler J. Physiol Rev. 2009;89:707–758. “Models and mechanisms of hyperalgesia and allodynia.”**  
   Separates wind-up, short-term facilitation, long-term potentiation, disinhibition, induction, and maintenance—the distinctions C-003 currently conflates.

5. **Ghitani N, et al. Nature. 2025;642:1016–1023. PMID 40269164.**  
   The direct modern motivation; it must be read as proposing a disease-specific role for spontaneous inflammatory nociceptor activity, not as erasing sixty years of C-afferent conditioning literature.

VERDICT: PASS — genuinely open or incremental with a stated delta
