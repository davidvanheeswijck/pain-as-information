# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-001-drg-habituation-is-filter-fatigue.md`
> 2026-09-01T00:09:25+00:00 · tokens in=5671 out=5527
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation

If the conjecture is true, it is forbidden that, in a preparation where DRG stimulation has lost its C-fibre filtering effect, raising the amplitude (charge) restores the filtering effect while varying the temporal pattern at constant charge does not.

## 2. Audit the author's stated killer

- **Concrete.** Passes. It specifies a chronic single-fibre preparation in a rat tibial nerve injury model, n=16 per arm, a within-animal crossover, a blinded recorder, and a specific outcome (proportion of C-fibre spikes failing to propagate) with a numerical threshold (20 percentage points).
- **Reachable.** Passes. It uses existing electrophysiology methods, costs 180k-250k euro, and takes 18 months, which is well within the reach of existing neural engineering laboratories.
- **Honest.** Passes. The author explicitly accepts that if the amplitude arm restores filtering at least as well as pattern variation, the conjecture is dead. The listed rivals are clearly distinguished by their own observable consequences, and no obvious auxiliary rescue is waiting to absorb the killer without cost.

## 3. Severity

Given the conjecture is false, the probability the proposed test still comes out favourable is **~0.5**.

The proposed test measures C-fibre conduction failure in a rat over 28 days, but the conjecture is about loss of clinical pain benefit in humans over months to years. The test does not measure behavioral allodynia. If loss of benefit is actually due to central compensation (a rival the author explicitly acknowledges), peripheral filtering might still decay and be restored by pattern variation, yielding a false pass on the electrophysiological outcome while the clinical conjecture remains false. Furthermore, any non-specific change in stimulation could transiently alter conduction, and the amplitude control may not perfectly isolate this because amplitude and pattern are fundamentally different perturbations with different dose-response curves. Because the proxy outcome is decoupled from the clinical phenomenon, the false-pass probability is well above 0.3, meaning the test is not evidence for the clinical conjecture.

## 4. The discriminating experiment

Live alternatives:
1. **T-junction filtering decay (conjecture):** Pattern variation restores filtering and pain relief; amplitude does not.
2. **Tolerance to charge:** Amplitude restores filtering and pain relief; pattern does not.
3. **Central compensation:** Neither restores pain relief, even if peripheral filtering is restored.
4. **Mechanical drift:** Neither restores filtering; impedance rises.

**Experiment:** Chronic DRG stimulation in a rat nerve injury model, measuring BOTH teased-fibre C-fibre conduction failure AND behavioral allodynia over 28 days. Once allodynia returns, perform the within-animal crossover (fixed 20 Hz, varied pattern, increased amplitude).
- If pattern restores both C-fibre failure and allodynia, but amplitude does not: supports the conjecture.
- If amplitude restores both, but pattern does not: supports tolerance to charge.
- If neither restores allodynia, but pattern restores C-fibre failure: supports central compensation.
- If neither restores C-fibre failure and impedance rises: supports mechanical drift.

Without the behavioral measure, the electrophysiology alone cannot distinguish the conjecture from central compensation.

## 5. Cost and ladder

1. **Existing-data reanalysis:** Retrospective analysis of clinical DRG reprogramming logs. Do patients who receive pattern variation (frequency/program changes) at constant charge report better restoration of relief than those who receive amplitude increases? Cost: minimal, 1-2 months.
2. **In silico:** Extend the Kent et al. (2018) computational model of DRG filtering to include chronic homeostatic adaptation (e.g., SK channel expression changes) to see if pattern variation restores filtering in silico. Cost: low, 2-3 months.
3. **Ex vivo or animal:** The proposed rat experiment, modified to include behavioral allodynia. Cost: 180k-250k euro, 18 months.

The first hard decision point is the animal experiment, which is expensive and slow. The cheaper rungs should be exhausted first.

## 6. Methodological red flags

- **Proxy outcome without behavioral correlate:** The design uses an electrophysiological proxy (C-fibre conduction failure) for a clinical phenomenon (loss of pain benefit) without measuring the behavioral equivalent (allodynia) in the animal, making it impossible to distinguish peripheral mechanisms from central compensation.

VERDICT: MAJOR — the proposed test has false-pass probability ~0.5 and proves nothing, because it measures an electrophysiological proxy without behavioral allodynia, failing to distinguish the conjecture from central compensation.
