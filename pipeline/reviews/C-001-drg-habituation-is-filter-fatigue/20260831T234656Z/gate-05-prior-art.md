# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `05-prior-art.md` · Subject: `C-001-drg-habituation-is-filter-fatigue.md`
> 2026-09-01T00:11:34+00:00 · tokens in=5498 out=7215
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Ledger check

`ledger/REFUTED.md` contains no entries. C-001 is therefore not a restatement of a conjecture already killed by this programme, and there is no ledger argument to quote.

## What this is already called

This conjecture combines three established subjects:

1. **Afferent filtering at the dorsal-root-ganglion T-junction**, also called **T-junction filtering** or **ganglionic filtering**.
2. **Loss of efficacy**, **habituation**, or **stimulation tolerance** during chronic neuromodulation.
3. **Temporal pattern modulation**, including **cycling**, **intermittent stimulation**, **stimulation holidays**, and **variable- or pseudorandom-frequency stimulation**, as attempts to prevent or reverse habituation.

“Novelty of the stimulus pattern” is not yet an established DRG mechanism. If retained, it needs an operational definition—predictability, entropy, sequence repetition, or inter-pulse-interval distribution—not the ordinary-language sense of novelty.

## Canonical prior work

The conjecture’s first mechanistic step is substantially known.

- **Amir and Devor, 2003**, showed that sensory spikes can conduct through the pseudounipolar stem without invading the soma and analysed how soma/T-junction excitability controls transmission. This is important antecedent physiology for the impedance-mismatch account.  
  *Biophysical Journal* 84:2181–2191.

- **Gemes et al., 2013**, directly studied action-potential propagation failure in sensory neurons and described the DRG as an afferent filter, particularly in C-type units. They also found that painful nerve injury can reduce this filtering.  
  *Journal of Physiology* 591:1111–1131. DOI: 10.1113/jphysiol.2012.242750.

- **Kent et al., 2018**, modelled DRG stimulation and T-junction propagation, including the dependence on membrane state and stimulation parameters.  
  PMID 29377442.

- **Chao et al., 2020**, supplied the acute experimental result closest to the present proposal: DRG field stimulation progressively suppressed C-fibre propagation while sparing Aβ traffic, with calcium-activated potassium conductances implicated.  
  PMID 32658148.

Thus, “DRG stimulation can enhance T-junction filtering preferentially in nociceptive fibres” is not novel. What has not been established is the chain:

> chronic fixed stimulation → homeostatic loss of SK-mediated filtering → restoration by an unpredictable pattern at matched charge.

Each arrow remains evidentially open.

The modern clinical programme is also old enough to have an industrial history. Spinal Modulation developed the Axium DRG system in the late 2000s; early prospective clinical reports appeared by 2013. St Jude Medical acquired Spinal Modulation in 2015, and Abbott inherited the programme when it acquired St Jude. Axium/Proclaim DRG culminated in the successful ACCURATE regulatory trial and FDA approval in 2016. The underlying therapy has therefore been under commercial development for well over a decade.

## What has already been tried

### Chronic loss of benefit

Loss of benefit is well recognized across SCS and DRG stimulation. The literature calls it **loss of efficacy** or **habituation**, but those labels do not establish a cellular mechanism. Explantation for diminished relief is compatible with:

- physiological accommodation;
- lead migration or contact geometry changes;
- fibrosis and altered thresholds;
- hardware failure;
- disease progression;
- central compensation;
- inadequate initial response subsequently classified as loss of benefit;
- battery replacement or revision decisions.

The Gatzinsky and Vanloon data establish attrition, not decay of T-junction filtering. The conjecture currently moves too quickly from a clinical administrative endpoint—“explant for diminished relief”—to a particular ion-channel mechanism.

The Levy analysis of ACCURATE suggested less habituation with DRG than SCS at 12 months, but its duration, sponsorship, and conflict structure limit it. The longer independent data cited in C-001 appropriately prevent the programme from treating that result as settled.

### Pattern changes and holidays

Neuromodulation practice does not respond to loss of benefit solely by increasing charge. Clinicians also change:

- active contacts;
- pulse width;
- frequency;
- waveform;
- duty cycle;
- stimulation schedule;
- anatomical targeting;
- and, in some centres, use a temporary **stimulation holiday**.

Retrospective SCS reports describe recovery of benefit after stimulation holidays or waveform conversion, but these are vulnerable to regression to the mean, expectation, washout, and changed recruitment. They do not demonstrate SK-channel “novelty” or DRG T-junction restoration.

Commercial waveform programmes—burst stimulation, high-frequency SCS, cycling, multiplexed stimulation, and closed-loop stimulation—show that varying temporal delivery is not itself new. Results have been mixed. In particular:

- **PROCO** found no independent analgesic advantage of frequencies between 1 and 10 kHz once other dosing considerations were controlled. This is adjacent rather than directly refuting because it studied SCS, not DRG T-junction conduction.
- A rigorous placebo-controlled crossover trial of **burst SCS** by **Hara et al.** found no clinically important advantage over placebo for chronic radicular pain after lumbar surgery, despite encouraging uncontrolled experience. This is a warning that waveform preference and open-label rescue do not establish a waveform-specific mechanism.
- Salvage by waveform switching is reported, but there is no convincing evidence that random or changing patterns reverse a measured chronic decline in C-fibre T-junction filtering.

I find no published chronic DRG experiment that first demonstrates loss of the Chao filtering effect and then tests charge-matched stochastic rescue. Nor is there an identified DRG pilot of that exact intervention that subsequently failed a pivotal trial.

## Patents and industry

The broad engineering idea is heavily occupied.

Spinal Modulation/St Jude/Abbott DRG patent families, including families titled along the lines of **“Selective stimulation systems and signal parameters for medical conditions,”** disclose stimulation at or near the DRG with selectable frequency, amplitude, pulse width, electrode configuration, and temporal delivery. More general Medtronic, Boston Scientific, Abbott, and Nevro portfolios disclose cycling among programmes, varying stimulation parameters, and changing waveforms to address accommodation or preserve efficacy.

Consequently:

- “vary DRG stimulation parameters to reduce accommodation” is not likely to be patent-novel;
- “use pseudorandom stimulation” is also old in the broader stimulation art;
- a potentially narrower claim would require the specific physiological feedback variable—measured T-junction propagation failure—and a defined charge-matched adaptation protocol.

A formal patentability opinion would require claim charts against the Abbott/Spinal Modulation continuations and the broader anti-habituation portfolios. Patents are also only evidence that somebody proposed the intervention, not that it worked.

Industry status matters here:

- **Spinal Modulation → St Jude Medical → Abbott:** commercialized DRG stimulation successfully; no demonstrated chronic T-junction biomarker or random-pattern rescue programme is publicly established.
- **Saluda Medical/Evoke:** commercialized ECAP-controlled SCS. This establishes closed-loop measurement of large-fibre spinal recruitment, not measurement of C-fibre traffic at the DRG.
- **Nevro, Boston Scientific, Abbott and Medtronic:** have commercialized or investigated alternative SCS waveforms and programme switching. Their mixed clinical record is prior information against assuming that temporal complexity itself prevents habituation.

The document’s ECAP argument is therefore overstated. Cord ECAPs are dominated by synchronous, myelinated-fibre activity. A reported microvolt measurement floor does not imply that existing DRG hardware can record sparse, asynchronous C-fibre propagation or quantify T-junction failure. The proposed experiment still requires specialized peripheral and central recordings; it is not made “cheap” by current clinical ECAP systems.

## Adjacent fields

The structural problem is familiar elsewhere:

- **Cochlear implants:** interleaved and temporally varied pulse trains are used to manage channel interaction and neural adaptation. The key lesson is that equal charge is not equal neural dose when timing changes.
- **Cardiac pacing:** rate adaptation and pacing algorithms vary timing, but physiological feedback—not novelty by itself—is what justifies the variation.
- **Deep-brain stimulation:** cycling, interleaving, adaptive DBS, and coordinated-reset stimulation have all been proposed to reduce adaptation or pathological synchrony. Acute promise has not consistently translated into durable superiority.
- **Responsive neurostimulation for epilepsy:** stimulation is event-triggered rather than continuously repeated. This is the mature analogue of replacing an open-loop fixed train with feedback control.
- **Telecommunications:** pseudorandom and spread-spectrum sequences separate effects of total power, spectral content, predictability, and interference. The conjecture presently confounds these dimensions.

The closest transferable lesson is that randomizing a sequence changes its spectrum, peak intervals, calcium accumulation, and recruitment statistics even when total charge is unchanged. A positive stochastic-pattern result would not, by itself, show a biological response to “novelty.”

## Does the proposed experiment identify the claimed mechanism?

Not as currently written.

1. **Failure to develop chronic decay must itself be a refutation.**  
   The protocol presupposes that fixed 20 Hz stimulation loses its filtering effect. If it does not, the proposed explanation for clinical loss of benefit fails in this model.

2. **The amplitude arm cannot simultaneously be “50% higher” and charge-matched** unless pulse width, pulse count, or duration is reduced. That compensating alteration introduces another temporal variable. There should be separate charge-matched and clinically realistic dose-escalation contrasts.

3. **Random 2–50 Hz stimulation changes more than novelty.**  
   It changes inter-spike intervals, burst peaks, spectral content, calcium accumulation, and SK activation. At minimum, use:
   - fixed 20 Hz;
   - periodic variable-frequency stimulation;
   - a repeated irregular sequence;
   - a continuously regenerated irregular sequence;
   - sequences with matched pulse count and matched inter-pulse-interval histograms but different ordering;
   - a stimulation-holiday arm.

   The repeated-irregular versus regenerated-irregular comparison is the one that can isolate sequence familiarity from ordinary nonlinear kinetics.

4. **Charge is not neural dose.**  
   Recruitment, ECAP amplitude where measurable, peak current, charge per phase, pulse count, and spectral distribution should be reported separately.

5. **Teased-fibre recordings are unlikely to be longitudinal recordings from the same fibre.**  
   Weekly measurements may introduce sampling and preparation changes. Aβ preservation does not fully control selective deterioration of C-fibre recordings.

6. **The mechanism needs direct corroboration.**  
   Measure somatic membrane potential, calcium handling, and SK responsiveness, and include an SK-channel intervention such as apamin where ethically and technically appropriate. Otherwise the result remains a waveform effect rather than evidence of homeostatic SK adaptation.

7. **Conduction rescue is not clinical rescue.**  
   A second stage must connect restored filtering to blinded behavioural outcomes. Central compensation could leave the cellular mechanism correct but therapeutically irrelevant.

## Novelty verdict

**INCREMENTAL.**

The established content is DRG **T-junction afferent filtering**, its acute enhancement by DRG field stimulation, and the general use of temporal variation to address neuromodulation habituation.

The precise delta is:

> **Testing whether chronic fixed-pattern DRG stimulation causes loss of measured C-fibre T-junction filtering that is reversed more effectively by sequence variation than by charge escalation.**

That experiment appears open. The stronger claim that clinical loss of benefit *is* decay of this filtering is premature and should not be in the title until the chronic physiological decline has been demonstrated.

## Five works to read next

1. **Amir R, Devor M. *Biophysical Journal*. 2003;84:2181–2191.**  
   Foundational account of soma and T-junction excitability in pseudounipolar sensory-neuron conduction.

2. **Gemes G, et al. *Journal of Physiology*. 2013;591:1111–1131.**  
   The essential pre-DRGS paper on C-neuron afferent filtering, propagation failure, and its alteration after painful injury.

3. **Chapman KB, et al. “Best Practices for Dorsal Root Ganglion Stimulation for Chronic Pain.” *Journal of Pain Research*. 2023.**  
   Establishes what clinicians actually change during DRG reprogramming and corrects the claim that current practice merely increases charge.

4. **Hara S, et al. “Effect of Spinal Cord Burst Stimulation vs Placebo Stimulation…” *JAMA*. 2022.**  
   A useful negative control showing how promising waveform-specific effects can disappear under blinded placebo comparison.

5. **The published “stimulation holiday” salvage literature for habituated SCS patients.**  
   This is the closest clinical precedent for recovery after temporal interruption and should determine the washout, regression, and rechallenge controls.

VERDICT: PASS — genuinely open or incremental with a stated delta
