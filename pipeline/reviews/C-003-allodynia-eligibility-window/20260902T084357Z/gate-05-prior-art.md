# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `05-prior-art.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-02T09:22:29+00:00 · tokens in=11212 out=8024
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Ledger check

C-003 is **not a literal restatement** of a ledgered conjecture, but it approaches the failure that killed C-001.

C-001 was killed by this argument:

> “The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease.”

C-003 materially answers part of that objection: Aβ traffic is the test input, and the proposed interaction occurs in a central dorsal-horn circuit. It does not simply rename peripheral C-fibre blockade.

It does **not**, however, establish that ongoing C-fibre activity is required in established neuropathic allodynia. That remains model-dependent. The nerve-injury literature includes mechanical hypersensitivity maintained by disinhibited Aβ circuits despite loss or silencing of substantial nociceptor populations. The inflammatory result of Ghitani et al. therefore cannot automatically be generalized to chronic neuropathic allodynia.

C-007 also imposed the relevant methodological constraint:

> “For a specified stimulus ensemble, does within- or across-fibre spike-train structure improve prediction of perceived pain quality or intensity beyond firing rate and recruited-unit identity?”

C-003 does include a behavioural outcome and a cross-fibre manipulation, so it advances beyond C-007. But recording afferents and measuring behaviour in separate cohorts weakens the promised trial-level linkage between the two inputs and the percept.

## Established field and established name

This belongs to **spinal nociceptive plasticity**, specifically:

- **C-fibre-conditioned heterosynaptic facilitation of A-fibre responses**
- **central sensitization**
- **wind-up/temporal summation**, if repeated C-fibre input is required
- **disinhibition-mediated recruitment of low-threshold mechanoreceptor input**, for the injury-state circuit
- a **conditioning–test stimulus paradigm**, experimentally

“Eligibility window” is not the conventional term here. In neuroscience, an eligibility trace usually denotes a transient synaptic record subsequently converted into plasticity by a third signal, as in reinforcement learning or three-factor learning rules. C-003 instead proposes transient state-dependent excitability or heterosynaptic facilitation. Calling it an eligibility window risks hiding the applicable literature.

## Canonical prior work

### The broad phenomenon is old

Mendell and Wall introduced **wind-up** in 1965: repeated C-fibre volleys progressively increased dorsal-horn neuronal responses. The critical property was dependence on inter-volley timing.

Woolf demonstrated in 1983 that peripheral injury produces a central increase in spinal excitability capable of amplifying subsequent input. Wall and Woolf subsequently showed that C-afferent conditioning could produce prolonged facilitation of spinal reflex responses, with important dependence on the tissue and afferents stimulated.

Cook, Woolf, Wall and McMahon showed in 1987 that C-primary-afferent input could dynamically enlarge dorsal-horn mechanoreceptive fields. In operational terms, nociceptive conditioning made previously ineffective low-threshold inputs effective.

The especially close prior art is the work commonly described as **small-calibre-afferent-induced heterosynaptic facilitation of A-fibre-evoked responses** in spinal preparations during the late 1980s and early 1990s. That is substantially the physiological interaction asserted by C-003.

Human capsaicin experiments then showed that normal mechanoreceptive A-fibre input can acquire a painful percept after nociceptive conditioning. Torebjörk and colleagues’ 1992 work on capsaicin-induced secondary hyperalgesia is a canonical example.

Finally, Torsney and MacDermott in 2006 directly demonstrated that removing spinal inhibition opens a route by which innocuous primary-afferent input reaches nociceptive lamina-I output neurons. That provides a competing mechanism in which no immediately preceding C-fibre burst is necessary.

### What is actually new

The literature has already established all the following separately:

1. C-fibre conditioning can transiently facilitate subsequent spinal responses.
2. Facilitation depends on stimulus frequency and interval.
3. Low-threshold A-fibre input can recruit nociceptive output after conditioning or disinhibition.
4. Aβ-mediated touch can be perceived as painful in sensitized tissue.
5. Spontaneous nociceptor activity can maintain some inflammatory pain states.

The defensible delta is:

> **Mapping the fixed-spike-count C-to-Aβ conditioning interval in an identified allodynic state while comparing nociceptor and low-threshold-mechanoreceptor conditioning and measuring both projection-neuron and behavioural outputs.**

That is a useful experiment, but it is an incremental combination of established conditioning–test methods, not a new mechanism class.

## Important technical problem with the claimed time constant

The 0.1-Hz versus 0.5-Hz wind-up threshold does **not** identify an exponential decay constant of 1–10 seconds.

Wind-up is a nonlinear accumulation process involving repeated volleys, NMDA-receptor recruitment, membrane depolarization, after-discharges and threshold crossing. Failure at 0.1 Hz and success at 0.5 Hz can result from any combination of:

- decay between volleys;
- number of repetitions;
- nonlinear NMDA conductance;
- stimulus intensity;
- afterhyperpolarization;
- peptide release;
- response saturation or floor effects.

It therefore brackets a useful **conditioning interval**, but not necessarily a single latent τ. Pre-registering a seconds-scale effect is reasonable; claiming that the cited frequency results directly estimate τ≈3 s is not.

There is also a conceptual contradiction: if a seconds-scale result is said to be predicted from wind-up, then observing it cannot simultaneously establish a phenomenon distinct from wind-up. Novelty would have to come from the **heterosynaptic C-to-Aβ interaction in the specified disease state**, not merely from the timescale.

## Failed or limiting precedents

### 1. Wind-up is not equivalent to chronic pain

Repeated C-fibre stimulation reliably produces wind-up experimentally, but wind-up is neither necessary nor sufficient for chronic allodynia. Reviews such as Herrero, Laird and López-García distinguish short-term wind-up from the longer-lived plasticity grouped under central sensitization. Many interventions abolish wind-up without eliminating established pain hypersensitivity.

**Consequence:** a seconds-scale conditioning curve could be real while explaining little about chronic allodynia.

### 2. A single conditioning burst may produce post-discharge, not gating

A C-fibre burst can leave dorsal-horn projection neurons firing or depolarized for seconds. A touch delivered during that tail can appear to increase “nociceptive response probability” through simple superposition or thresholding.

The current controls do not close this route. An Aβ burst is not a valid control for C-evoked post-discharge because it is not expected to activate the same central conductances or peptides.

A necessary additional condition is **C-burst alone**, with the expected post-burst response measured at every proposed touch delay. The primary endpoint should be an interaction term:

\[
R(C+\text{touch},t)-R(C\text{ alone},t)-R(\text{touch alone}),
\]

or an equivalent nonlinear model, rather than the unadjusted response after burst-plus-touch.

### 3. Peripheral drive is important in some models but dispensable in others

Inflammatory allodynia, traumatic nerve injury, chemotherapy neuropathy and microglial disinhibition are not interchangeable. Nav1.8-lineage ablation and related nociceptor-manipulation studies have found strong effects on inflammatory pain but preservation of important components of neuropathic mechanical hypersensitivity.

**Consequence:** inflammatory and neuropathic animals should not be treated as alternative implementations of one experiment. They are a pre-registered effect-modification test.

### 4. Conditioning identity cannot be reduced to matched spike count

A matched-count Aβ burst does not match:

- central projection pattern;
- glutamate release probability;
- neuropeptide release;
- conduction dispersion;
- postsynaptic receptor recruitment;
- spatial distribution within the dorsal horn.

It is still a valuable negative control, but “the same afferent load” is too strong. A more convincing specificity series would compare multiple nociceptor classes, naturalistic replay versus synchronous optogenetic bursts, and direct dorsal-root stimulation with optogenetic stimulation.

### 5. Peripheral interruption has repeatedly failed to cure centrally maintained allodynia

Local anaesthetic blocks, nociceptor silencing and peripheral interventions can reduce pain in selected patients and models, especially early in disease, but established allodynia can persist or recur because central disinhibition and plasticity have become sufficient. That practical history is why the field distinguishes **induction** from **maintenance** of central sensitization.

The proposed early-versus-late comparison is therefore essential rather than optional.

## Design implications

Before spending €200,000–300,000, the experiment should add or alter the following:

1. **Add C-burst-only trials at every delay.** Otherwise lingering burst responses can masquerade as touch conversion.
2. **Define the endpoint as a C-by-touch interaction**, not merely an elevated response after paired stimulation.
3. **Separate inflammatory and neuropathic models prospectively.** Do not pool them or substitute one after seeing results.
4. **Use sufficient washout and model carry-over.** Randomized short-delay trials can themselves accumulate wind-up and alter later trials.
5. **Replay natural spontaneous firing statistics.** A synchronous optogenetic burst is likely to be more effective than the asynchronous activity invoked by the conjecture.
6. **Measure touch-alone pain in the established allodynic state.** If touch is already painful without a recent burst, the strong claim that the window is “what allodynia is” has failed even if further facilitation occurs.
7. **Do not infer desynchronization therapy from a positive timing curve.** If total C-fibre activity maintains tonic depolarization, desynchronizing it may reduce peaks without closing the facilitated state.
8. **Prefer within-animal linkage where feasible.** The programme’s own ledger has already identified separate physiological and behavioural cohorts as a route to mechanistic overinterpretation.

A positive result would support “ongoing nociceptor activity transiently modulates the gain of touch-evoked pain.” It would not by itself establish that two individually normal inputs are jointly sufficient, that the touch is literally rerouted, or that coincidence is the primary maintenance mechanism of chronic allodynia.

## Adjacent fields with the same structure

- **Paired-pulse and conditioning–test neurophysiology:** the direct methodological precedent; estimate recovery or facilitation functions while varying the conditioning–probe interval.
- **Cochlear implants and auditory psychophysics:** forward masking uses almost the same conditioning–probe design and explicitly separates residual neural activity, adaptation and true probe-response changes.
- **Cardiac electrophysiology:** refractory-period and strength–interval curves provide a mature framework for distinguishing a recovery process from accumulation across repeated stimuli.
- **Spike-timing-dependent and paired associative stimulation:** relevant to interval-controlled experiments, although C-003 does not yet demonstrate synaptic plasticity and should not borrow “eligibility trace” terminology from this field.
- **Responsive neurostimulation and closed-loop DBS/SCS:** demonstrate state-dependent intervention and biomarker-triggered stimulation, but not the proposed C-to-Aβ mechanism.

## Patents and industry

Broad patent territory is already occupied around:

- patterned and burst spinal-cord stimulation;
- stimulation conditional on recorded neural activity;
- evoked-compound-action-potential feedback;
- adaptive adjustment of frequency, pulse width and timing;
- selective peripheral-nerve stimulation or block.

Relevant industrial programmes include Abbott’s BurstDR, Nevro’s high-frequency SCS, Saluda Medical’s Evoke ECAP-controlled closed-loop SCS, Medtronic’s adaptive/closed-loop platforms, and multiplexed-waveform programmes associated with differential-target stimulation. These programmes establish that varying temporal patterns and controlling stimulation from neural responses are mature industrial concepts.

None of those programmes, however, validates the specific claim that spontaneous C-fibre discharge creates a seconds-long window in which Aβ touch becomes painful. Nor is there a known pivotal clinical trial that isolated C-to-Aβ relative timing while holding C-fibre count constant. The experimental delta therefore remains potentially protectable only at a narrow implementation level; broad claims to “timing-based treatment of allodynia” would face extensive prior art.

The industrial history also gives a warning: patterned SCS modalities often perform well in uncontrolled pilots, while comparative trials show smaller or nonspecific advantages once paresthesia, programming attention, charge delivery and regression to the mean are controlled. No commercial waveform should be cited as indirect evidence for this mechanism.

## Novelty verdict

**INCREMENTAL.**

The central content is already known as **C-fibre-conditioned heterosynaptic facilitation of A-fibre responses within central sensitization**. The conjecture’s narrow new contribution is the controlled interval-response experiment in an identified allodynic state, particularly the nociceptor-versus-mechanoreceptor conditioning comparison and early-versus-late disease test.

The manuscript should replace “allodynia is a coincidence phenomenon” with a testable, less totalizing formulation: “ongoing nociceptor activity contributes a seconds-scale, heterosynaptic facilitation of touch-evoked nociceptive output in specified allodynia models.”

## Five works to read next

1. **Wall PD, Woolf CJ. “Muscle but not cutaneous C-afferent input produces prolonged increases in the excitability of the flexion reflex in the rat.” J Physiol. 1984;356:443–458.** Shows that prolonged C-conditioned facilitation is old and strongly dependent on afferent source.

2. **Cook AJ, Woolf CJ, Wall PD, McMahon SB. “Dynamic receptive field plasticity in rat spinal cord dorsal horn following C-primary afferent input.” Nature. 1987;325:151–153.** Close prior art for C input making previously ineffective mechanical inputs recruit dorsal-horn output.

3. **Torebjörk HE et al. “Central changes in processing of mechanoreceptive input in capsaicin-induced secondary hyperalgesia in humans.” J Physiol. 1992;448:765–780.** Human evidence that ordinary mechanoreceptive input becomes painful after nociceptive conditioning.

4. **Torsney C, MacDermott AB. “Disinhibition opens the gate between pain and touch in the spinal cord.” J Neurosci. 2006;26:1833–1843.** Establishes the principal rival: Aβ access to nociceptive output can arise from tonic disinhibition without a recent C-fibre burst.

5. **Herrero JF, Laird JMA, López-García JA. “Wind-up of spinal cord neurones and pain sensation: much ado about something?” Prog Neurobiol. 2000;61:169–203.** Essential for avoiding the invalid inference from wind-up frequency thresholds to a chronic-pain mechanism or a unique exponential τ.

VERDICT: PASS — genuinely open or incremental with a stated delta
