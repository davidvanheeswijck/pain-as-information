# Gate verdict

> Reviewer: `vertex/gemini-3.5-flash@eu` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab google
> Gate: `03-evidence-integrity.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-02T09:17:26+00:00 · tokens in=11671 out=9727
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## Citation Classifications

### 1. Coull et al. (2003) — PMID 12931188
* **Classification:** CONTESTED
* **Dispute:** While this is a seminal study establishing that microglial BDNF shifts the neuronal chloride gradient via KCC2 downregulation in lamina I, this pathway is now known to be sex-specific. Sorge et al. (2015, PMID 26120961) demonstrated that microglia-to-neuron BDNF signaling is required for mechanical allodynia only in male mice; female mice utilize a distinct, T-cell-mediated pathway that bypasses microglia entirely. Treating this as a universal "tonic disinhibition" mechanism without sex qualification is highly contested.

### 2. Coull et al. (2005) — PMID 16355225
* **Classification:** CONTESTED
* **Dispute:** Same as Coull et al. (2003). The microglial-BDNF-KCC2 disinhibition pathway is sex-dimorphic (male-specific in rodents), which limits its generalizability as a universal baseline model for mechanical allodynia.

### 3. Duan et al. (2014) — PMID 25467445
* **Classification:** SUPPORTS
* **Evaluation:** The work is accurately cited to support the specific spinal circuit dissection of somatostatin (SST) and dynorphin (Dyn) interneurons gating mechanical allodynia.

### 4. Lu et al. (2013) — PMID 23979158
* **Classification:** SUPPORTS
* **Evaluation:** The work is accurately cited to support the role of the PKCγ-expressing excitatory interneuron pathway in gating mechanical inputs to lamina I projection neurons.

### 5. Ghitani et al. (2025) — PMID 40269164
* **Classification:** OVERSTATED
* **Evaluation:** The conjecture claims that Ghitani et al. "read [their findings] as suggesting allodynia arises from coincidence of normal touch input with ongoing nociceptor firing." While Ghitani et al. identified that inflammation induces spontaneous, touch-independent activity in specific nociceptor classes, they did not demonstrate, model, or claim a transient, sub-second "coincidence window" gating Aβ touch. The conjecture overstates the authors' discussion of spontaneous activity to manufacture an explicit endorsement of a temporal coincidence model.

### 6. Chapman, Suzuki & Dickenson (1994) — PMID 7992912
* **Classification:** SUPPORTS
* **Evaluation:** The work is accurately cited for the rate-dependence of wind-up (present at 0.5 Hz, absent at 0.1 Hz) in spinal dorsal horn neurons.

### 7. Ji et al. (2007) — PMID 17631690
* **Classification:** SUPPORTS
* **Evaluation:** The work is accurately cited for the frequency-dependent activation of ERK phosphorylation (pERK) in the dorsal horn.

### 8. Dickenson-adjacent series (1999) — PMID 9987009
* **Classification:** SUPPORTS
* **Evaluation:** The work is accurately cited for the observation of wind-up in trigeminal convergent neurons at 0.66 Hz.

### 9. Peirs C, et al. (2015) — PMID 26291162
* **Classification:** ORPHANED
* **Evaluation:** This citation is decorative. It is listed in the references but is never cited or integrated anywhere in the body text. 

### 10. Mendell LM, Wall PD. (1965) — PMID 14334366
* **Classification:** ORPHANED
* **Evaluation:** This citation is decorative. It is listed in the references but never cited in the text.

### 11. Woolf CJ. (1983) — PMID 6656869
* **Classification:** ORPHANED
* **Evaluation:** This citation is decorative. It is listed in the references but never cited in the text.

---

## Evidence Base Audit

### 1. WHAT IS MISSING
* **Sex-Specific Neuroimmune Dimorphism:** The conjecture fails to cite Sorge et al. (2015, PMID 26120961) or subsequent literature on sex differences in mechanical allodynia. Because the "tonic disinhibition" arm of the proposed contradiction relies entirely on microglial BDNF, and the "Killer" experiment proposes using "Mouse" without specifying sex, a hostile reviewer would immediately point out that the entire experimental design is blind to the fact that female mice do not use the microglial pathway.
* **Presynaptic Inhibition / Primary Afferent Depolarization (PAD):** The conjecture focuses entirely on postsynaptic/interneuronal facilitation (wind-up) to explain the temporal window. It fails to cite literature on presynaptic GABAA-mediated primary afferent depolarization (e.g., Bardoni et al., 2013, PMID 24012273), which operates on a millisecond-to-second timescale and directly gates Aβ input at the central terminal.
* **Specific Circuit Integration of Peirs et al. (2015):** Although Peirs et al. (PMID 26291162) is orphaned in the reference list, a hostile expert would ask why its findings—specifically that mechanical allodynia is gated by transient receptor potential vanilloid 1 (TRPV1)-expressing nociceptors via calretinin interneurons—were not integrated to provide a concrete anatomical pathway for the proposed C-to-Aβ coincidence.

### 2. NEGATIVE RESULTS
The conjecture is built exclusively on positive reports of wind-up and facilitation. It completely ignores the extensive literature on **Conditioned Pain Modulation (CPM)** and **Diffuse Noxious Inhibitory Controls (DNIC)** (e.g., Le Bars et al., 1979, PMID 38615), which demonstrates that conditioning C-fibre stimulation typically *inhibits* rather than facilitates subsequent mechanical and nociceptive dorsal horn responses segmentally and supraspinally ("pain inhibits pain"). The conjecture assumes C-fibre activity acts as a purely facilitatory gate without engaging with these well-established inhibitory negative results.

### 3. CHAIN LENGTH
* **Chain 1 (Tonic Disinhibition):** The claim that microglial BDNF collapses the chloride gradient is supported by Coull et al. (2003, PMID 12931188) $\rightarrow$ which cites Tsuda et al. (2003, PMID 14614170) for microglial p38 MAPK activation $\rightarrow$ which terminates in early papers on spinal microglial activation after nerve injury. This chain is short (2–3 links) and terminates in robust empirical data.
* **Chain 2 (Coincidence Model):** The claim that allodynia arises from the temporal coincidence of touch and spontaneous nociceptor activity cites Ghitani et al. (2025, PMID 40269164) $\rightarrow$ which cites Wu et al. (2001, PMID 11707497) for spontaneous activity in injured sensory neurons $\rightarrow$ which terminates in classic biophysical papers on ectopic pacemaker channels in damaged axons. This chain terminates in papers describing *peripheral ectopic generation*, none of which support or propose a *central spinal coincidence gate* operating on a seconds-long decay window. The central gating aspect of the chain is entirely unsupported.

### 4. QUANTITATIVE FIDELITY
* **Frequency-to-Interval Conversions:** The conversions are mathematically correct: $0.5\text{ Hz} = 2\text{ s}$ interval; $0.1\text{ Hz} = 10\text{ s}$ interval; $0.66\text{ Hz} \approx 1.5\text{ s}$ interval.
* **Wind-up Statistics:** The citation of PMID 9987009 for "wind-up appears in 73% of long-latency responses at 0.66 Hz" is quantitatively accurate and matches the source text.
* **Time Constant ($\tau$) Range:** The pre-registered range of $1\text{ to }10\text{ s}$ is a reasonable inference from the $0.5\text{ Hz}$ vs $0.1\text{ Hz}$ wind-up thresholds, but the assertion that it is "centred near 3 s" is stated with more precision than the cited literature (which only tests discrete steps of 2 s and 10 s) can support.

### 5. RECENCY
The "tonic disinhibition" model of Coull et al. (2003, 2005) represents the consensus of 20 years ago. The field has moved past treating this as a universal, sex-independent mechanism. By presenting the Coull et al. pathway as the sole, undisputed representative of the "tonic disinhibition" rival, the conjecture relies on an outdated consensus that ignores a decade of neuroimmunological research on sex-dimorphic pain processing.

---

VERDICT: MAJOR — Ghitani et al. (PMID 40269164) is overstated to claim it suggests a temporal coincidence window when it only reports spontaneous activity.
