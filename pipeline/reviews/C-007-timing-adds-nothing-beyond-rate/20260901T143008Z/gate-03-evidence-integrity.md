# Gate verdict

> Reviewer: `vertex/gemini-3.5-flash@eu` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab google
> Gate: `03-evidence-integrity.md` · Subject: `C-007-timing-adds-nothing-beyond-rate.md`
> 2026-09-01T14:36:47+00:00 · tokens in=8112 out=9846
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

As a research-integrity auditor, I have evaluated the evidence base for the draft conjecture **C-007**. Here is the audit of the individual citations and the overall shape of the evidence base.

---

### Citation Classifications

Of the 8 references listed in the document, only 3 are actually cited in the text. The remaining 5 are decorative additions to the bibliography.

1. **Serra J, Campero M, Ochoa J, Bostock H. (1999) PMID 10066906.**
   * **Classification:** `SUPPORTS`
   * **Analysis:** This is the foundational study establishing that activity-dependent slowing (ADS) of conduction velocity can be used to classify C-nociceptor subtypes (specifically distinguishing mechano-sensitive from mechano-insensitive/silent nociceptors) in human microneurography. It directly supports the mechanism described.

2. **Cho A, et al. (2016) doi:10.3389/fncom.2016.00118.**
   * **Classification:** `SUPPORTS`
   * **Analysis:** The work is accurately characterized. It is an *ex vivo* mouse skin-nerve study showing that temporal firing patterns (specifically bursting structures) in C-fibres encode chemical pain. The conjecture correctly identifies this as a single, unreplicated, non-human, chemical-stimulus study.

3. **Troglio A, et al. (2025) PMID 41004469.**
   * **Classification:** `MISCHARACTERISED`
   * **Analysis:** The conjecture cites this paper to claim that "human microneurography yields two to six tracked fibres per session." In actual microneurography practice, isolating, identifying, and tracking even a *single* C-nociceptor through a long, repeated protocol is a rare and difficult achievement; many sessions yield zero usable units. Citing a 2025 PLOS ONE paper for a highly optimistic "two to six" yield mischaracterizes the immense technical difficulty and typical attrition rates of human single-unit microneurography.

4. **Werland F, et al. (2021) PMID 33369733.**
   * **Classification:** `ORPHANED`
   * **Analysis:** This work is listed in the references but is never cited or discussed anywhere in the text of C-007. It appears to be a leftover from the refuted C-005 conjecture.

5. **Schmidt R, et al. (1995) PMID 7823139.**
   * **Classification:** `ORPHANED`
   * **Analysis:** This classic paper on human C-nociceptor classification is listed in the references but is never cited in the text.

6. **Ghitani N, et al. (2025) PMID 40269164.**
   * **Classification:** `ORPHANED`
   * **Analysis:** Listed in the references but never cited in the text.

7. **Prescott SA, Ma Q, De Koninck Y. (2014) PMID 24473266.**
   * **Classification:** `ORPHANED`
   * **Analysis:** Listed in the references but never cited in the text.

8. **Borst A, Theunissen FE. (1999) doi:10.1038/14731.**
   * **Classification:** `ORPHANED`
   * **Analysis:** This foundational review on information theory and neural coding is listed in the references but never cited in the text.

---

### Evidence Base Audit

#### 1. WHAT IS MISSING
A hostile expert would immediately ask why the following three bodies of work are absent:
* **Spinal Cord Wind-Up and Temporal Summation Literature:** The central nervous system's decoding of C-fibre input is highly sensitive to the precise temporal spacing of incoming spikes (e.g., Mendell, 1966; Herrero et al., 2000). By ignoring how the spinal cord integrates these intervals (via NMDA receptor kinetics), the conjecture assumes "information" only matters if a naive linear decoder can read it from a single axon, ignoring the biological decoder.
* **Classic Human Microneurography on Patterned Discharge:** Studies by Handwerker, Schmelz, and Torebjörk (e.g., Schmidt et al., 1995, which is listed but un-cited) show that C-nociceptors exhibit distinct adaptation and bursting profiles under sustained thermal or mechanical stimulation. These patterns are highly relevant to the quality of sensation.
* **Spike Train Metric Space Literature:** The conjecture proposes to compare decoders but fails to cite the standard mathematical frameworks for analyzing spike-timing information, such as the Victor-Purpura distance (Victor & Purpura, 1997) or the van Rossum metric (van Rossum, 2001).

#### 2. NEGATIVE RESULTS
The conjecture is itself a negative hypothesis (asserting a lack of temporal information). However, it fails to engage with existing literature where temporal coding hypotheses in other sensory modalities (like touch or olfaction) have failed to replicate or have been shown to be redundant once population rate codes are controlled for. Furthermore, it does not address whether existing open-access microneurography datasets have been subjected to similar information-theoretic analyses with null results.

#### 3. CHAIN LENGTH
* **Chain 1:** The claim that "human microneurography yields two to six tracked fibres per session" is attributed to `Troglio et al. (2025)`. If traced, this claim contradicts the foundational microneurography literature (e.g., Vallbo, 1979; Torebjörk, 1974), which establishes that single C-fibre isolation is highly volatile and frequently yields zero tracked units per session.
* **Chain 2:** The mechanism of activity-dependent slowing (ADS) as a subtype classifier is cited directly to `Serra et al. (1999)`. This is a direct, primary electrophysiological study in humans (Chain length = 1).

#### 4. QUANTITATIVE FIDELITY
* **Feasibility Numbers:** The "Killer" experiment proposes presenting "a repeated 60 second mechanical or thermal segment... at least 30 repeats per unit." This requires **30 minutes of stable, continuous recording** from a single human C-nociceptor while delivering repeated noxious stimuli. In practice, C-nociceptors will severely sensitize, fatigue, or suffer receptor damage over 30 noxious trials, violating the "frozen-noise" assumption. Additionally, keeping a microelectrode stable within a human nerve fascicle during 30 minutes of mechanical or thermal stimulation is highly unrealistic.
* **Time Constants:** The text states "slowing accumulating over 1e-1 to 1e0 seconds." In reality, activity-dependent slowing in human C-fibres accumulates over tens of seconds to minutes of continuous stimulation, meaning the lower bound of $0.1$ seconds ($10^{-1}$) is an order of magnitude too fast for the onset of stable ADS.

#### 5. RECENCY
The bibliography pads itself with 2025 citations (`Troglio et al.`, `Ghitani et al.`) to appear cutting-edge, but the core debate (rate vs. temporal coding) is framed using 1990s concepts. Modern computational neuroscience has largely moved past the binary "rate vs. 5ms timing" debate to focus on population-level manifold dynamics and state-space trajectories, which this conjecture does not address.

---

VERDICT: MINOR — 6 citations need correction
