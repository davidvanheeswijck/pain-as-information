# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `05-prior-art.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T14:40:41+00:00 · tokens in=7781 out=5387
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Ledger check

C-007 descends directly from **C-005**, which was refuted because an absolute information rate is undefined without a stimulus distribution:

> “An information rate is only defined relative to a stimulus ensemble. ‘A C-nociceptor carries 30 bits per second’ is not a property of the axon, it is a property of the axon together with the distribution of stimuli presented…”

The ledger required:

> “For a specified stimulus ensemble, does sub-5-millisecond spike timing add information about pain-relevant stimulus features or perception beyond firing rate and unit identity?”

C-007 **substantively answers that objection** by fixing the ensemble and comparing representations on the same recordings. It is not merely verbal evasion.

However, it only partially adopts the prescribed endpoint. It decodes the **stimulus**, not pain perception, and therefore cannot determine whether timing carries information specifically relevant to pain. It also substitutes “rate in 50 ms bins” for mean rate; a 50-ms count sequence is already a temporal code.

## Established field and terminology

The established field is **neural coding**, specifically:

- **Rate coding versus temporal coding**
- **Spike-train information analysis**
- **Temporal precision of a neural code**
- **Conditional information in spike timing given spike count**
- For identity across fibres: **labelled-line coding** or **labeled population coding**

The clean formulation is not “does timing add information beyond rate?” but:

> Does spike timing carry conditional information about the stimulus, \(I(S;T\mid N,U)\), after controlling for spike count \(N\), unit class \(U\), and any time-varying rate envelope?

That distinction matters because 50-ms bin counts retain stimulus-locked temporal structure. Comparing 50-ms and 1-ms bins primarily measures the value of **finer temporal resolution**, not timing beyond a rate code.

Activity-dependent slowing establishes a C-fibre’s physiological class; it is not ordinarily called “unit identity.” If the intended feature is CMH, CMi, sympathetic, or another ADS-defined phenotype, call it **unit class**.

## Canonical prior work

This question is much older than the conjecture.

- **Adrian (1920s)** established frequency/rate coding as a principal sensory representation.
- **MacKay and McCulloch (1952), “The limiting information capacity of a neuronal link”**, treated neuronal signalling as an information channel.
- **Bialek et al. (1991), “Reading a neural code,” Science**, demonstrated reconstruction and information analysis from spike trains.
- **Victor and Purpura (1996)** introduced spike-train metrics explicitly designed to determine the temporal precision at which spike timing matters.
- **Strong et al. (1998), “Entropy and information in neural spike trains,” Physical Review Letters**, developed the direct method for estimating information as temporal resolution is varied.
- **Borst and Theunissen (1999)** reviewed the rate/temporal-code distinction and the dependence of coding conclusions on stimulus ensemble and decoder.
- In somatosensation, **Johansson and Birznieks (2004)** showed that first-spike timing in tactile afferent populations can carry substantial information, demonstrating that millisecond timing is biologically usable in peripheral sensory systems—although not necessarily in C fibres.

The closest pain-specific prior art identified in the supplied record is **Cho et al. (2016), Frontiers in Computational Neuroscience 10:118**, which examined temporal structure in nociceptor responses to chemical stimulation. That work means the broad proposition “nociceptor temporal patterns may encode stimulus information” has already been asked experimentally. Its ex-vivo preparation, chemical ensemble, non-human material, and lack of replication leave the proposed human microneurographic comparison open.

Thus, the broad idea is known; the human C-nociceptor implementation is the delta.

## What earlier work found

Across sensory systems, the general answer is not universally “rate” or “timing.” It depends on:

1. the stimulus ensemble;
2. whether timing is measured relative to a repeated external event;
3. the observation window;
4. whether the comparator is total spike count, a time-varying rate, or coarse binned counts;
5. trial-to-trial stationarity;
6. the amount of data available to fit the richer representation.

Fast auditory, visual, tactile, and electrosensory systems often exhibit useful millisecond timing. Slowly conducting nociceptors have lower firing rates, activity-dependent conduction changes, and slower natural stimuli, making sub-5-ms information less plausible—but not already disproved.

The proposed mechanism is also not one-way. Activity-dependent slowing can create arrival-time variability, but because slowing depends systematically on spike history, it can itself carry decodable information. A history-aware receiver may infer or compensate for it. “Conduction changes timing” does not by itself imply “conduction destroys timing information.”

## Failed attempts and known methodological failures

There is no identified pivotal clinical trial that directly tested this single-unit information claim. The important failures are methodological:

- **Limited-sample information estimates:** increasing resolution from 50 ms to 1 ms greatly expands the response space and preferentially harms the fine-timing arm. Under-sampling therefore does **not** degrade both arms equally; it tends to create false support for the null.
- **Stimulus-locked rate masquerading as precision:** information can rise at finer bins merely because the peristimulus rate changes inside a 50-ms interval, without any trial-specific precise timing code.
- **Frozen-noise pseudoreplication:** repeated samples within one 60-second waveform are correlated and are not equivalent to independent stimuli or independent trials.
- **Decoder failure interpreted as biological absence:** failure of two chosen decoders is not proof that the response contains no additional information.
- **Nonstationarity:** sensitization, fatigue, receptor adaptation, skin temperature, electrode drift, and activity-dependent slowing can make repeats nonexchangeable.
- **Null-hypothesis mismatch:** failure to detect an improvement is not evidence of equivalence. A pre-specified equivalence or noninferiority margin is required.

The conjecture’s current criterion also does not match its wording. The claim says timing “adds no information,” but the experiment only calls it refuted above a **20%** increase. A reproducible 10% gain would falsify the literal claim but survive the stated killer. Either change the claim to “adds less than 20%” or make any reliably positive conditional-information increment refuting.

## Adjacent fields

### Cochlear implants

This is the closest engineering analogy. Modern cochlear implants largely transmit channelized amplitude envelopes rather than complete acoustic fine structure. Fine-structure strategies, including MED-EL’s FSP/FS4 family, have produced mixed and often modest benefits, especially for pitch and speech in noise. The practical limitations are electrode–neuron interface, channel interaction, neural survival, and inability to reproduce natural spatiotemporal firing—not proof that timing is intrinsically uninformative.

### Tactile afferents

Rapidly conducting mechanoreceptors use first-spike latency and population timing. This is a direct warning against extrapolating from C-fibre conduction properties to peripheral sensory axons generally.

### Retina and auditory neuroscience

These fields developed the relevant controls: information-versus-bin-width curves, repeated frozen stimuli, trial shuffling, count-preserving timing surrogates, and analyses separating stimulus-locked rate modulation from precise repeatable spike timing.

### Responsive neurostimulation and cardiac pacing

NeuroPace RNS and modern cardiac devices use temporal event detection and closed-loop response. They establish that temporal pattern recognition can be implemented in implantable hardware, but they operate on population field signals or cardiac events, not isolated C-nociceptor spike trains.

### Spinal cord stimulation

Closed-loop SCS systems use evoked compound action potentials as feedback. This is amplitude/homeostasis control, not decoding of natural nociceptor fine timing.

## Patents and industry

No identified patent or commercial programme directly anticipates the proposed experiment or establishes the negative result.

Relevant industrial activity includes:

- **Saluda Medical, Evoke:** closed-loop SCS using ECAP amplitude to maintain recruitment within a therapeutic window.
- **Medtronic, Inceptiv:** ECAP-responsive SCS compensating for posture and electrode–cord distance.
- **Nevro, Senza:** high-frequency stimulation intended to avoid paresthesia, but without single-unit C-fibre decoding.
- **Abbott and Boston Scientific:** waveform programming, sensing, and adaptive neuromodulation patent portfolios.
- **NeuroPace:** detection of pathological temporal patterns in intracranial population activity.
- **Cochlear, MED-EL, and Advanced Bionics:** decades of patents concerning envelope extraction, pulse timing, interleaving, and fine-structure representation.

These portfolios establish that adaptive waveform control, temporal feature extraction, and neural-response feedback are heavily patented fields. They do **not** show that sub-5-ms timing in a human C-nociceptor has been measured against a count- and class-controlled comparator.

I find no relevant “successful pilot followed by failed pivotal trial” because this is a basic measurement conjecture rather than a therapeutic device claim. Cochlear fine-structure strategies provide the nearest history of plausible temporal coding producing weaker-than-expected clinical gains, but they are not a direct refutation.

## Design corrections required before testing

1. **State the established question:** conditional information in spike timing beyond spike count and unit class.
2. **Define the rate comparator correctly:** total count, a cross-validated smooth conditional intensity model, or both—not only 50-ms bins.
3. **Use count- and rate-preserving surrogates:** jitter spikes within windows while preserving trial count and the peristimulus rate envelope.
4. **Pre-register an information-versus-jitter curve:** for example 1, 2, 5, 10, 20, 50, and 100 ms, rather than canonizing 5 ms without prior justification.
5. **Use nested cross-validation:** all preprocessing, bandwidth selection, and decoder hyperparameters must be fit inside training folds.
6. **Test equivalence:** if “less than 20%” is the scientific claim, require the upper confidence bound to fall below 20%.
7. **Validate power by injection:** add synthetic timing information of known magnitude to real spike trains and demonstrate that the pipeline recovers it.
8. **Separate stimulus information from pain information:** include trial-wise psychophysics if the result is intended to bear directly on HC-1.
9. **Clarify unit identity:** ADS-defined class is not individual identity; identity contributes nothing within a single-unit analysis unless data are pooled across units.
10. **Address stimulus bandwidth:** use at least two independently generated ensembles, not merely repeated copies of one frozen waveform.

## Novelty assessment

**INCREMENTAL.**

The established subject is **rate coding versus temporal coding in neural spike trains**. The broad method—vary temporal resolution and compare information or decoding performance on repeated stimuli—is canonical. Nociceptor temporal coding has also been investigated by Cho et al.

The precise delta is:

> **A within-recording, human microneurographic estimate of conditional stimulus information in sub-5-ms timing of ADS-classified single C-nociceptors.**

That is a legitimate and potentially valuable increment. It should not be presented as the first test of temporal neural coding, the first information-theoretic study of spike timing, or the first suggestion that nociceptor patterns encode stimulus identity.

The proposed archived-data reanalysis is the correct next step, but only if the recordings contain repeated stimuli with sufficiently precise stimulus timestamps and enough trials to validate sensitivity to an injected timing effect.

## Five works to read next

1. **Victor JD, Purpura KP. “Nature and precision of temporal coding in visual cortex: a metric-space analysis.” Journal of Neurophysiology, 1996.**  
   Provides an established, bin-free way to ask at what temporal precision spike trains discriminate stimuli.

2. **Strong SP, Koberle R, de Ruyter van Steveninck RR, Bialek W. “Entropy and information in neural spike trains.” Physical Review Letters, 1998.**  
   Canonical information-versus-temporal-resolution framework and essential background for the proposed analysis.

3. **Panzeri S, Senatore R, Montemurro MA, Petersen RS. “Correcting for the sampling bias problem in spike train information measures.” Journal of Neurophysiology, 2007.**  
   Explains why sparse sampling can preferentially erase apparent fine-timing information and how to diagnose the bias.

4. **Cho A et al. Frontiers in Computational Neuroscience 10:118, 2016, doi:10.3389/fncom.2016.00118.**  
   Closest nociceptor-specific temporal-pattern precedent; its exact comparator and reported temporal scale should determine the honest novelty claim.

5. **Johansson RS, Birznieks I. “First spikes in ensembles of human tactile afferents code complex spatial fingertip events.” Nature Neuroscience, 2004.**  
   Demonstrates millisecond-scale peripheral somatosensory coding in humans and supplies the strongest adjacent-field counterexample to a general rate-only assumption.

VERDICT: PASS — genuinely open or incremental with a stated delta
