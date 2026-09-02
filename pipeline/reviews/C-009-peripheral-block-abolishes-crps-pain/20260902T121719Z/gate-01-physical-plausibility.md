# Gate verdict

> Reviewer: `azure/openai-responses/gpt-5.6-sol@swedencentral` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab openai
> Gate: `01-physical-plausibility.md` · Subject: `C-009-peripheral-block-abolishes-crps-pain.md`
> 2026-09-02T12:51:35+00:00 · tokens in=11841 out=6146
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Mandatory quantitative audit

### Assumptions the conjecture failed to supply

I have had to assume:

- A lidocaine-like agent, because neither drug nor formulation is specified.
- A representative peripheral block of **10 mL of 1% lidocaine**, i.e. **100 mg** or approximately **43 mmol/L** at injection.
- A 70 kg adult, baseline pain **6/10**, and within-patient pain-score standard deviation of approximately **1.5 points**.
- A target nerve diameter of **2–10 mm**, depth **1–5 cm**, and injectate volume **5–20 mL**.
- Diagnostic ultrasound at **5–15 MHz**.
- That “complete block” means loss of pinprick, cold and light-touch sensation throughout the entire painful territory—not merely numbness in one named nerve distribution.

These parameters must be specified prospectively; different local anaesthetics have materially different potency, duration and toxicity.

### 1. Energy scale

This is an ordinary pharmacological mechanism, not a thermally fragile quantum proposal.

For a local anaesthetic with an effective channel dissociation constant \(K_d\sim10\)–\(100\,\mu\text{M}\),

\[
|\Delta G^\circ|\simeq kT\ln(1\text{ M}/K_d)
\]

gives approximately:

\[
|\Delta G^\circ|\simeq (9.2\text{–}11.5)kT
  \simeq 0.25\text{–}0.31\ \text{eV}
  \simeq (4.0\text{–}5.0)\times10^{-20}\ \text{J}.
\]

At 310 K, \(kT\simeq26.7\) meV or \(4.3\times10^{-21}\) J. Thus channel binding is roughly **one order of magnitude above \(kT\)** in free-energy terms. A nominal 1% lidocaine solution is approximately 43 mM, initially **\(4\times10^2\) to \(4\times10^3\) times \(K_d\)**, so even allowing a tenfold dilution gives high channel occupancy.

The membrane energy for moving one monovalent ion through 70 mV is

\[
qV\simeq 1.1\times10^{-20}\ \text{J}\simeq 2.6kT.
\]

Reliability does not depend on preserving one such event against thermal noise: action-potential generation is a collective, nonlinear process involving many channels and ions. There is no thermal-energy objection.

### 2. Timescale

No coherence, entanglement, radical pair, tunnelling or spin mechanism is invoked. Electronic decoherence in the femtosecond-to-picosecond range is therefore irrelevant.

The relevant hierarchy is approximately:

- Channel conformational and use-dependent blocking events: milliseconds to seconds.
- Action potential: approximately \(10^{-3}\) s.
- Block onset: **600–1800 s**.
- Proposed primary endpoint: **1800 s**.
- Block duration: roughly **\(7\times10^3\) to \(3\times10^4\) s**.

The molecular mechanism is therefore at least **three orders of magnitude faster** than block onset and five to seven orders faster than block duration. No protected long-lived quantum degree of freedom is required.

A single 30-minute endpoint is nevertheless poor pharmacology. A time series through onset, plateau and recovery is needed to establish that pain follows the approximately 2–8 hour conduction-block window rather than an injection or expectation response.

### 3. Field and dose

There is no therapeutic applied field. Ultrasound is used only for guidance.

For a conventional block:

- Ultrasound frequency: approximately **5–15 MHz**.
- Wavelength in tissue:  
  \[
  \lambda=c/f\simeq 1540/(5\text{–}15)\times10^6
  \simeq0.10\text{–}0.31\ \text{mm}.
  \]
- Useful penetration: approximately **3–8 cm**, depending on frequency and body habitus.
- Regulatory diagnostic intensity ceiling is of order **0.7 W/cm² ISPTA**; for a 1–5 cm² active aperture, that corresponds to an upper-bound acoustic output of order **1 W**, already achieved by standard clinical hardware.
- No hardware shortfall exists.

For the drug, the assumed 10 mL of 1% lidocaine gives **100 mg**, versus a customary maximum without epinephrine of about **4.5 mg/kg**, commonly capped near 300 mg. For a 70 kg adult this is a safety margin of approximately **threefold**. That margin can disappear if several nerves require separate injections, or if bupivacaine is substituted. The protocol must specify agent, concentration, volume, total dose, injection site, free plasma concentration and stopping rule. “Comparable plasma concentration” is not an executable dose specification.

### 4. Spatial resolution

A 5–20 mL injectate has a spherical-equivalent radius

\[
r=(3V/4\pi)^{1/3}\simeq1.1\text{–}1.7\ \text{cm},
\]

although actual spread follows fascial planes. Ultrasound resolves approximately **0.1–1 mm** structures at the proposed depth, while the target nerve is several millimetres across. Imaging resolution is therefore adequate by roughly one order of magnitude.

The limitation is not diffraction but anatomical coverage. A hand or foot may involve several named nerves, while a single injection typically produces a drug cloud only a few centimetres across. Depending on block location, the distance between all relevant trunks or between the injection and a possible DRG generator is approximately **10–30 cm**, versus **1–3 cm** local spread: potentially a **one-order-of-magnitude spatial mismatch**.

Most importantly, a block distal to the DRG cannot interrupt ectopic impulses originating in the DRG and propagating centrally. The mechanism explicitly includes DRG activity, but the proposed intervention does not test it. Persistence of pain would therefore not distinguish a DRG primary-afferent generator from an autonomous central generator.

### 5. Signal to noise

The principal readout is a subjective 0–10 pain score, not a physical sensor.

Assuming baseline pain 6/10:

- Complete abolition gives \(\Delta=6\) points.
- An 80% reduction gives \(\Delta=4.8\).
- A 50% reduction gives \(\Delta=3.0\).
- The separation between the proposed 80% and 50% effects is therefore **1.8 points**.

With within-patient standard deviation \(\sigma\simeq1.5\),

\[
\mathrm{SE}\simeq \sigma/\sqrt{20}\simeq0.34
\]

and the 1.8-point contrast is about **5 standard errors** under independent, approximately Gaussian measurement noise. Random score noise is therefore not the limiting factor.

The dominant noise is systematic: an effective block produces unmistakable numbness, so neither participant nor operator is blinded. Expectancy effects of order **1–2 NRS points** are comparable to the entire 1.8-point separation between the 50% and 80% hypotheses and do not average away with longer integration. Repeated measurements during onset and recovery would reduce random noise but not this bias. Mechanical allodynia is still less interpretable: once touch transmission is blocked, failure to report touch-evoked pain is partly tautological.

No magnetic sensing is proposed, so femtotesla amplitudes and sensor noise floors are inapplicable.

## Pseudoscience checklist

No checklist item is triggered. The conjecture supplies an ordinary mechanism and pharmacological timescale, uses frequencies only with a conventional anticipated meaning, invokes no non-standard interaction, and cites indexed clinical literature.

## Physical classification

The mechanism is not **IMPOSSIBLE**: it violates no conservation law or proven bound.

It is not **INFEASIBLE**: standard regional-anaesthesia hardware already supplies the required spatial resolution, dose and timing.

The restricted claim is **UNDEMONSTRATED**: it is physically allowed and experimentally feasible but has not been established in the specified long-duration CRPS population.

## Scientific assessment after the arithmetic

The physics passes. The causal interpretation does not yet.

First, “complete sensory block” must be anatomically defined before recruitment. A single named-nerve block is not evidence that all primary afferent input from a hand or foot has been removed. Block completeness requires a pre-specified map of the painful territory against pinprick, cold, touch and preferably an objective evoked-potential or neurographic measure. Patients whose painful territory cannot be covered safely must not be treated as informative nulls.

Second, the conjecture’s mechanism includes ectopic DRG activity, but a distal peripheral block leaves that source connected to the spinal cord. If pain persists, the experiment cannot conclude that central changes are autonomous. It can conclude only that pain was not maintained by activity originating distal to the block. This is a major mismatch between mechanism and intervention.

Third, spontaneous pain and allodynia must not carry equal inferential weight. Abolition of spontaneous pain after a verified block is informative. Abolition of mechanical allodynia is expected whenever the test stimulus itself can no longer reach the CNS; it does not establish selective removal of a pain-maintaining signal.

Fourth, the universal Claim does not match the median-based test. “Abolishes … regardless of phenotype” predicts something close to an all-patient response. A median reduction above 50% permits nearly half the patients to fail. The manuscript must choose between a population-average claim and an individual-level universal claim and pre-register a corresponding confirmation criterion.

Fifth, a transient block response is not yet a validated diagnostic for benefit from a durable peripheral intervention. That requires a prospective predictive-validity study. The proposed experiment can test whether distal peripheral traffic acutely contributes to pain; it cannot by itself establish that surgery, ablation or chronic stimulation will help.

Finally, this bears directly on PB-5 but only indirectly on HC-2. Demonstrating that peripheral input is necessary does not demonstrate that pain-relevant structure is externally readable. A wire can be necessary while its relevant code remains unobservable with any practical sensor.

## Strongest fair version

The strongest defensible version is: in independently adjudicated patients with long-duration CRPS whose spontaneous pain is confined to a territory that can be completely covered by specified proximal nerve or plexus blocks, verified interruption of distal afferent conduction will reduce spontaneous pain substantially more than a randomized matched-plasma intravenous local-anaesthetic control, with pain tracking block onset and recovery. That version survives the quantitative audit: it is conventional, safe within standard dose limits, spatially achievable in selected patients, and has a large nominal signal. It remains **UNDEMONSTRATED**, principally because obvious numbness prevents full blinding and because a negative result cannot exclude a DRG generator proximal to the block.

VERDICT: MAJOR — a 1–3 cm local block is being used to exclude generators distributed over roughly 10–30 cm of peripheral/DRG anatomy, an approximately one-order-of-magnitude spatial shortfall, and it cannot intercept DRG-origin traffic
