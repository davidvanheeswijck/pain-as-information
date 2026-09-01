# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `05-prior-art.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T00:51:56+00:00 · tokens in=6025 out=6019
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Ledger check

C-005 is **not a restatement** of either graveyard entry.

The closest is C-001, because both concern information conveyed by C-fibre traffic. C-001 was killed by:

> “The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease.”

C-005 does not re-propose T-junction filtering or assume that C-fibre traffic is sufficient for pain. It asks a narrower encoding question. It therefore avoids, rather than answers, C-001’s disease-mechanism objection. A low or high information rate in healthy C-nociceptors would not show that those fibres maintain neuropathic pain or allodynia.

C-002 is unrelated.

## Established field and established terminology

This belongs to **neural coding and sensory information theory**. The measurement proposed is usually called:

- **stimulus-specific mutual-information rate**, or **transmitted information rate**;
- estimated using the **repeated-stimulus/direct entropy method** or “direct method”;
- followed by a **temporal precision** or **jitter analysis**.

It should not be called the axon’s **channel capacity**. Channel capacity is the supremum of mutual information over admissible input distributions. This experiment measures information achieved under one investigator-selected stimulus ensemble. Different stimulus bandwidths, amplitudes and priors can produce different bits-per-second values for the same neuron.

A more accurate title would be:

> *Transmitted information rate and temporal precision of identified human C-nociceptors under a specified repeated naturalistic stimulus ensemble.*

## Canonical prior work

The general idea is old and well established.

- **Shannon (1948)** supplied the distinction among entropy, mutual information and channel capacity.
- **MacKay and McCulloch (1952), “The limiting information capacity of a neuronal link,” Bulletin of Mathematical Biophysics 14:127–135**, made one of the earliest explicit information-capacity calculations for neurons.
- **de Ruyter van Steveninck and Bialek (1988)** applied information-theoretic analysis to repeated naturalistic stimulation of a sensory neuron. They found that short spike sequences and precise timing conveyed substantial information in the blowfly H1 system.
- **Strong et al. (1998), Physical Review Letters 80:197–200**, formalized direct entropy estimation from repeated stimuli, including extrapolation for finite sampling. They demonstrated that millisecond-scale spike patterns can transmit information not captured by coarse rate alone.
- **Borst and Theunissen (1999), Nature Neuroscience 2:947–957**, reviewed the resulting rate-versus-timing literature and emphasized that the answer depends on stimulus statistics, response timescale and the definition of “rate.”

The application to peripheral nociceptors also has substantial antecedents. Classical work by Zotterman, Handwerker, Torebjörk, Ochoa, Schmelz and colleagues established C-nociceptor classes, broad tuning, stimulus-response relations and activity-dependent conduction slowing. Cho et al. (2016) went beyond rate and reported chemical-stimulus discrimination from interspike-interval structure.

Thus neither “measure neural information in bits per second” nor “compare rate with temporal pattern” is new. What may be new is doing it **directly in identified human C-nociceptors during a repeated naturalistic stimulus**.

## What the prior work does—and does not—establish

I do not find a canonical published number that can simply replace the proposed human experiment. Published information rates for other sensory neurons cannot be transferred to human C-nociceptors, and Cho et al. did not provide the proposed human, in-vivo, frozen-noise estimate.

Nevertheless, the document overstates the evidential gap in three ways.

### 1. There is no ensemble-independent “information rate of the axon”

“Under natural stimulation” is not a sufficient specification. Information rate depends on:

- the stimulus variable being decoded;
- its amplitude distribution and temporal bandwidth;
- whether onset, intensity, modality, location or chemical identity is the target;
- the analysis word length and time resolution;
- adaptation and nonstationarity;
- whether fibre identity is available to the decoder.

The experiment can establish a rate for its stimulus ensemble, not a universal value below 30 bits/s.

### 2. The experiment does not estimate channel capacity

A repeated frozen stimulus estimates transmitted information about that stimulus. To estimate capacity, one would need to define physically admissible stimuli and optimize the stimulus distribution, likely iteratively. The present proposal instead gives a lower bound on capacity and an achieved rate under one ensemble.

### 3. Fine timing is not synonymous with structure beyond rate

HC-1 includes bursts, interspike-interval statistics and synchrony. Those can exist on tens-to-hundreds-of-milliseconds scales. Failure to find information below 5 ms would not reduce HC-1 to fibre identity plus mean rate. Cho et al.’s three-spike interval result is especially not equivalent to a claim for sub-5-ms precision.

## Problems with the proposed mechanism

Activity-dependent slowing is real, but “slowing corrupts timing” is not yet established.

A history-dependent propagation delay can:

- introduce apparently noisy arrival-time variability;
- deterministically transform intervals while preserving information;
- itself encode recent firing history;
- be partly invertible by a decoder familiar with the transformation.

The experiment should separately estimate stimulus-to-generation and generation-to-recording transformations if possible. Otherwise, variability introduced at transduction, spike initiation and conduction will be conflated.

The proposed natural thermal stimulus is also unlikely to possess useful power at 200 Hz, given actuator and tissue thermal filtering. A 5-ms jitter test is uninformative if the stimulus cannot carry features on that timescale. Mechanical stimulation may have greater bandwidth, but receptor mechanics and safety still require measurement rather than assumption.

Finally, subtype identity is fixed for a particular recorded unit. It is not a time-varying code measurable within that unit. Quantifying information in “which subtype fired” requires simultaneous or pooled population decoding with an explicit prior over fibres.

## Failed and limiting approaches

Several recurrent failures in this field bear directly on the design:

1. **Treating information rate as an intrinsic neuronal constant.** Rates changed when investigators changed the stimulus ensemble or decoding target.
2. **Naive direct entropy estimation.** Long binary words with millisecond bins have an enormous response space. Plug-in estimates are badly biased with limited repeats; thirty repeats of a 60-second segment will not, by itself, cure this.
3. **Equating jitter sensitivity with a unique temporal code.** Jitter can alter counts near analysis-bin boundaries and disrupt bursts or rate transients, depending on implementation.
4. **Using an input with inadequate temporal bandwidth.** Failure to observe fine timing then reflects the stimulus or transducer rather than the neuron.
5. **Assuming stationarity in adapting nociceptors.** Repetition, sensitization, fatigue and activity-dependent slowing can make nominally identical trials nonexchangeable.
6. **Extrapolating from electrically evoked following rates to natural coding.** Following 100-Hz electrical stimulation does not show that natural transduction uses or supports a 100-Hz information-bearing regime.
7. **Inferring a population or pain code from single fibres.** Peripheral single-unit information does not establish which information reaches perception or remains relevant after central convergence.

The proposed sample is also asymmetric logically. One unit reliably exceeding 30 bits/s can refute a universal upper bound, but 20 units cannot confirm that *all* human C-nociceptors are below it. The claim should specify a population quantity, such as the median or 95th percentile within named subtypes and stimulus conditions.

## Adjacent fields with the same structure

This methodological problem has already been solved, or at least encountered, elsewhere:

- **Cochlear implants:** competing strategies encode envelopes, channel identity and timing; performance is limited by neural survival, channel interaction and the mismatch between available engineering bandwidth and usable biological information.
- **Tactile afferent coding:** first-spike latency, population identity and millisecond timing have been compared directly with rate codes.
- **Retinal and insect visual coding:** repeated naturalistic stimuli, direct information estimates and finite-sampling corrections were developed here.
- **Cardiac pacing:** rate-responsive and closed-loop systems distinguish measured physiological state from merely varying stimulation patterns.
- **NeuroPace responsive neurostimulation:** detects pathological temporal structure and intervenes conditionally, although it does not estimate a universal neuronal bitrate.
- **Adaptive DBS:** Medtronic’s Percept/adaptive programmes use biomarkers such as beta power rather than trying to decode all information in individual axons.
- **Closed-loop spinal-cord stimulation:** Saluda Medical’s Evoke system regulates stimulation using evoked compound action potentials. This is feedback control of recruitment, not decoding of spontaneous nociceptive traffic.

The general lesson is that clinically useful feedback often requires a robust low-dimensional biomarker, not reconstruction of the complete information carried by individual axons.

## Patents and industry

The broad patent territory is already crowded. Saluda Medical, Medtronic, Abbott, Boston Scientific, Nevro, NeuroPace, Cochlear and peripheral-interface companies have extensive portfolios covering:

- neural-signal recording;
- spike and compound-action-potential feature extraction;
- closed-loop stimulation;
- stimulus-pattern selection;
- ECAP-controlled spinal stimulation;
- adaptive stimulation based on measured biomarkers.

Those portfolios make a broad downstream claim such as “measure neural patterns and adjust stimulation according to information content” unlikely to be novel.

I find no industry programme known for publishing a direct, single-human-C-nociceptor bits-per-second estimate. Commercial spinal systems generally record compound responses or stimulation-evoked signals, not spontaneous identified C-nociceptor spike trains. The closest successful programme, Saluda’s ECAP-controlled SCS, does not answer C-005. Nor do Nevro’s high-frequency SCS, Abbott’s burst/DRG systems, or Medtronic’s closed-loop SCS programmes: they compare therapeutic waveforms and feedback variables rather than measuring peripheral sensory information capacity.

There is therefore no directly relevant pilot-to-pivotal clinical failure to cite. The industry failures are informative mainly because waveform novelty and physiological feedback have repeatedly failed to prove that a particular temporal code is causal. Therapeutic efficacy cannot substitute for the proposed encoding measurement.

## Necessary redesign before testing

The proposed experiment is useful only after the estimand is narrowed.

1. Define the stimulus variable and ensemble mathematically.
2. Replace “channel capacity” with “transmitted information rate under ensemble E.”
3. Predefine subtype-specific population quantities rather than a universal statement about “a human C-nociceptor.”
4. Measure the delivered stimulus spectrum at the receptor and ensure it supports the tested temporal precision.
5. Use several estimators: bias-corrected direct estimation, model-based encoding/decoding, and held-out predictive likelihood.
6. Include convergence tests over repeat number, word length and bin size.
7. Separate coarse time-varying rate from finer spike-pattern information using an explicit conditional-information analysis.
8. Compare recorded-arrival timing with a model of activity-dependent propagation delay.
9. Treat 30 bits/s as a preregistered condition-specific prediction, not a biological constant.
10. Do not claim consequences for pain perception without a perceptual or behavioural measurement.

## Novelty verdict

**INCREMENTAL.**

The established subject is **stimulus-specific neural information-rate estimation and temporal-code analysis**.

The precise delta is:

> **application of repeated-stimulus information-rate and temporal-precision estimation to subtype-identified human C-nociceptors in vivo.**

That delta appears worth testing, but the current universal “under 30 bits/s” and “channel capacity” language is not supportable. Confirmation would establish a conditional empirical bound for the chosen ensemble, not a general capacity limit and not the weakness of HC-1 as a whole.

## Five works to read next

1. **MacKay DM, McCulloch WS. “The limiting information capacity of a neuronal link.” Bulletin of Mathematical Biophysics. 1952;14:127–135.**  
   The early neuronal information-capacity treatment and the place to learn why a capacity claim requires explicit channel assumptions.

2. **de Ruyter van Steveninck RR, Bialek W. “Real-time performance of a movement-sensitive neuron in the blowfly visual system.” Proceedings of the Royal Society B. 1988;234:379–414.**  
   Canonical repeated-naturalistic-stimulus work showing how short spike sequences and timing are related to information transmission.

3. **Strong SP, Koberle R, de Ruyter van Steveninck RR, Bialek W. “Entropy and information in neural spike trains.” Physical Review Letters. 1998;80:197–200.**  
   The direct-method foundation, including the extrapolations needed before calling a finite-data entropy estimate reliable.

4. **Panzeri S, Senatore R, Montemurro MA, Petersen RS. “Correcting for the sampling bias problem in spike train information measures.” Journal of Neurophysiology. 2007;98:1064–1072.**  
   Essential for evaluating whether thirty repeats can support the proposed bins, word lengths and confidence bounds.

5. **Borst A, Theunissen FE. “Information theory and neural coding.” Nature Neuroscience. 1999;2:947–957.**  
   The clearest corrective to treating rate and timing as absolute alternatives independent of stimulus statistics and decoding timescale.

VERDICT: PASS — genuinely open or incremental with a stated delta
