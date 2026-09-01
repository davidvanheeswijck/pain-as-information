# Gate verdict

> Reviewer: `vertex/gemini-3.5-flash@eu` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab google
> Gate: `03-evidence-integrity.md` · Subject: `C-005-nociceptor-information-rate.md`
> 2026-09-01T00:49:41+00:00 · tokens in=6240 out=10288
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Citation Classifications

### 1. Serra J, Campero M, Ochoa J, Bostock H. *J Physiol* 1999;515:799-811. PMID 10066906.
* **Classification:** `SUPPORTS`
* **Justification:** The cited work is the foundational study establishing that human C-nociceptor subtypes (specifically mechano-sensitive vs. mechano-insensitive/silent nociceptors) can be separated in vivo via their distinct profiles of activity-dependent conduction velocity slowing (ADS) under low-frequency electrical stimulation.

### 2. Cho A, et al. *Front Comput Neurosci* 2016;10:118. doi:10.3389/fncom.2016.00118
* **Classification:** `SUPPORTS`
* **Justification:** The citation accurately supports the text's claim. Cho et al. used an ex vivo mouse skin-nerve preparation to record nociceptive afferents under chemical stimulation, and they successfully classified three chemical stimulants with 79.7% accuracy using a pattern classifier based on three-spike inter-spike interval (ISI) motifs.

### 3. Werland F, et al. *J Physiol* 2021;599:1595-610. PMID 33369733.
* **Classification:** `MISCHARACTERISED`
* **Justification:** The conjecture claims this paper shows that "Polymodal C-nociceptors follow electrical stimulation to 100 Hz without conduction failure." The cited paper, titled *"Conduction failure in human somatosensory C-fibres,"* actually reports the exact opposite: high-frequency stimulation (such as 20 Hz, let alone 100 Hz) causes profound conduction failure and latency shifts in human C-nociceptors. Conduction failure is the primary phenomenon investigated in the paper, not an absent background effect.

### 4. Troglio A, et al. *PLOS ONE* 2025;20:e0329537. PMID 41004469.
* **Classification:** `OVERSTATED`
* **Justification:** While the paper discusses microneurography yields, claiming it supports a routine yield of "two to six tracked fibres per session" under the highly demanding conditions of the proposed protocol (30 repeats of a 60-second frozen-noise stimulus, requiring over 30 minutes of absolute electrode stability) is an overstatement. Typical yields for stable, single-unit C-fibre recordings of this duration in human subjects are closer to one or two units, with many sessions yielding zero usable units due to micro-motion.

### 5. Schmidt R, Schmelz M, Forster C, Ringkamp M, Torebjörk E, Handwerker H. *J Neurosci* 1995;15:333-41. PMID 7823139.
* **Classification:** `ORPHANED`
* **Justification:** This classic paper on the classification of responsive and unresponsive human C-nociceptors is listed in the references but is never cited anywhere in the body of the text. It is purely decorative.

### 6. Ghitani N, et al. *Nature* 2025;642:1016-23. PMID 40269164.
* **Classification:** `ORPHANED`
* **Justification:** This paper is listed in the references but is completely absent from the text. It serves no supportive function in the document.

### 7. Prescott SA, Ma Q, De Koninck Y. *Nat Neurosci* 2014;17:183-91. PMID 24473266.
* **Classification:** `ORPHANED`
* **Justification:** This paper is listed in the references but is never cited in the text. It is a decorative bibliography addition.

---

## Evidence Base Audit

### 1. WHAT IS MISSING
* **The Spinal Decoded-Information Literature:** The conjecture fails to cite Prescott et al. (2014)—which is orphaned in its own reference list—regarding how the spinal cord actually decodes peripheral input. Prescott et al. demonstrate that the spinal dorsal horn acts as a dynamical system that can transition between rate and population codes, meaning peripheral "fine timing" may be discarded centrally regardless of peripheral channel capacity.
* **Biophysical Models of Activity-Dependent Slowing (ADS):** The conjecture misses critical work modeling the biophysics of ADS (e.g., Tigerholm et al., 2014, PMID 24855043). These models show that ADS is not random "jitter" or noise that "corrupts" timing; rather, it is a highly deterministic, history-dependent filter. A hostile expert would point out that deterministic slowing does not destroy information; it merely encodes the history of the fiber's activity, which can theoretically be decoded.
* **Human Psychophysical Evidence on Rate vs. Pattern Coding:** The conjecture ignores classic human microstimulation studies (e.g., Torebjörk et al., 1984, PMID 6326179) showing that intraneural stimulation of single C-nociceptors produces pain intensity ratings that scale monotonically with mean frequency, and that irregular vs. regular stimulation patterns of the same mean rate do not alter the quality or intensity of the perceived pain.

### 2. NEGATIVE RESULTS
The conjecture is built almost entirely on a single positive report of temporal pattern coding (Cho et al., 2016) which was performed ex vivo in mice using chemical stimuli. It fails to engage with the extensive history of failed attempts to find temporal-pattern-specific pain sensations in humans. For example, clinical neuromodulation trials have repeatedly shown that "burst" or "high-frequency" stimulation patterns often fail to outperform standard tonic stimulation once total charge per second (dose) is controlled, suggesting that the central pain system operates primarily as an integrator of total nociceptive rate rather than a pattern decoder.

### 3. CHAIN LENGTH
* **Chain 1 (Information Rate Gap):** The claim *"No published estimate exists for the information rate of a nociceptor axon in bits per second"* is supported by a citation to the program's own internal ledger (`E-01 §1`). This is a self-referential chain of length 1 that terminates in an unreviewed, unpublished project document rather than an exhaustive literature search.
* **Chain 2 (Timing Degradation):** The claim that activity-dependent slowing *"degrades timing precision exactly when rate is high enough for fine timing to matter"* cites Serra et al. (1999). However, Serra et al. measured slow, cumulative conduction velocity shifts over minutes of low-frequency (0.25 Hz) stimulation. They did not measure millisecond-scale spike-to-spike jitter during high-frequency bursts. The chain terminates in a paper that does not support the micro-temporal degradation claim.

### 4. QUANTITATIVE FIDELITY
* **The 100 Hz Claim:** The claim that polymodal C-nociceptors follow electrical stimulation to 100 Hz "without conduction failure" (citing Werland et al., 2021) is biologically impossible and a direct inversion of the cited paper's data. Werland et al. show that C-nociceptors experience severe conduction block and failure at frequencies far below 100 Hz.
* **The 30 Bits/Second Ceiling:** The calculation of the 58 bits/second ceiling using $H \approx r \cdot \log_2(e / (r \cdot \Delta t))$ is mathematically consistent for a jittered Poisson process, but the assertion that the real rate "will sit well below... under 30 bits per second" is an arbitrary guess presented with false precision.

### 5. RECENCY
The conjecture relies on a 1999 paper (Serra et al.) to establish the framework for activity-dependent slowing, treating it purely as a transmission error (jitter). This ignores the last decade of axonal computational biology, which views the axon as a dynamic computational gate rather than a static cable. The consensus of the last five years has moved toward viewing axonal propagation as an active filter that performs multiplexing, rendering the "jitter degrades information" assumption obsolete.

---

VERDICT: MAJOR — Werland et al. (2021) [PMID 33369733] is cited to claim C-nociceptors follow 100 Hz without conduction failure, which is a direct inversion of the study's actual findings.
