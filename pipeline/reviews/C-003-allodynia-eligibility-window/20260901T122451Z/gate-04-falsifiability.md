# Gate verdict

> Reviewer: `tensorx/glm-5.2` · router router.eu.requesty.ai · geolocation eu · retention 0d · trained-on false · lab zai
> Gate: `04-falsifiability.md` · Subject: `C-003-allodynia-eligibility-window.md`
> 2026-09-01T12:31:59+00:00 · tokens in=8067 out=6296
> Verbatim model output below. Do not edit it. If it is wrong, that is
> a fact about the panel and belongs in the record.

## 1. The forbidden observation
The probability that a calibrated light touch evokes a nociceptive dorsal horn response will not depend on its delay after a burst of C-fibre activity, once total C-fibre spike count and touch intensity are held constant.

## 2. Audit the author's stated killer
- **Concrete.** Passes. It specifies the animal model, optogenetic control, fixed delays, von Frey touch, readouts (dorsal horn electrophysiology and behaviour), n=12 per group, and a statistical threshold (95% CI of decay constant includes infinity).
- **Reachable.** Passes. Optogenetics in mice with von Frey testing and electrophysiology is standard. The cost (200k-300k EUR) and timeframe (18 months) are realistic.
- **Honest.** Fails. The author lists the rival "Both, at different disease stages" and notes that "the answer depends on when you look." If the killer fires (flat response), the obvious rescue is that the experiment was conducted at the wrong disease stage. The author even suggests running at two timepoints, but does not specify how a failure at one timepoint would be interpreted, leaving the door open to post-hoc selection of the "correct" stage.

## 3. Severity
Given the conjecture is false, the probability the proposed test still comes out favourable is about **0.6**.

The proposed test only requires a decaying function of inter-stimulus interval. This is the exact signature of central sensitization/wind-up, a robust phenomenon in these circuits (Mendell & Wall, 1965, cited by the author). The test cannot distinguish the proposed "coincidence routing" from generic temporal summation/wind-up, where a C-fibre burst simply depolarizes the projection neuron, bringing it closer to threshold for the subsequent Aβ input. Therefore, even if the specific routing conjecture is false, the test will likely show a decay and falsely pass.

## 4. The discriminating experiment
Live alternatives:
1. **Tonic disinhibition** (timing irrelevant).
2. **Generic central sensitization/wind-up** (C-fibre burst depolarizes projection neurons, bringing them closer to threshold for Aβ input; this is summation, not routing).
3. **Coincidence routing** (Aβ input is specifically routed to the nociceptive pathway during the window).

**Experiment:** Ex vivo spinal cord preparation with dorsal root attached. Record intracellularly from lamina I projection neurons. Stimulate dorsal root with Aβ-threshold and C-threshold pulses. Deliver Aβ alone, C alone, and Aβ at varying delays after C.

- **Outcome A (supports routing):** Aβ alone produces no EPSP in projection neurons. C alone produces a subthreshold EPSP. Paired stimulus produces a suprathreshold response only at short delays. This would show Aβ is being routed to a pathway it doesn't normally activate.
- **Outcome B (supports summation):** Aβ alone produces a subthreshold EPSP. C alone produces a subthreshold EPSP. Paired stimulus produces a suprathreshold response due to temporal summation. This supports wind-up, not routing, and would refute the conjecture while the proposed in vivo test would have falsely passed.

## 5. Cost and ladder
1. **Existing data:** Unlikely to have paired optogenetic/mechanical data with this temporal resolution.
2. **In silico:** Could model the circuit, but won't settle the biological question of routing vs. summation.
3. **Ex vivo:** Spinal cord slice with dorsal root attached. Electrical stimulation at Aβ and C thresholds. Intracellular recording from lamina I neurons. Cost: ~30k EUR, 3-6 months. This is the first hard decision point. If it's summation, the conjecture is dead.
4. **In vivo animal:** The proposed optogenetic study.
5. **Human:** Not applicable.

## 6. Methodological red flags
- **No blinding** mentioned for behavioural scoring.
- **Multiple outcomes** (electrophysiology and behaviour) with no correction.
- **Subgroup with no prior justification:** "neuropathic or inflammatory model" and "two timepoints" without a pre-specified interaction.
- **Success criterion too loose:** "decay constant's 95% CI includes infinity". A decay constant of 5 seconds would pass, but contradicts the "few hundred milliseconds" claim in the mechanism.

VERDICT: MAJOR — the proposed test has false-pass probability ~0.6 and proves nothing
