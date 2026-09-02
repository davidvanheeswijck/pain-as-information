# Tally: C-009-peripheral-block-abolishes-crps-pain

**VERDICT: REFUTED** — 1 gate(s) returned FATAL

Median P(substantially correct) across laboratories: **0.15** (spread 0.13, suspiciously tight: check whether the panel is actually independent)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** In long-duration CRPS, does selective suppression of pathological afferent activity relieve pain more than matched nonselective sensory blockade, thereby distinguishing a peripheral generator from central reinterpretation of ordinary input? |
| `01-physical-plausibility` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **MAJOR** a 1–3 cm local block is being used to exclude generators distributed over roughly 10–30 cm of peripheral/DRG anatomy, an approximately one-order-of-magnitude spatial shortfall, and it cannot intercept DRG-origin traffic |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MINOR** Specify the block site relative to the DRG, and remove the claim that a positive result bears on HC-2; the experiment tests input-dependence, not peripheral readability. |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MINOR** 2 citations need correction |
| `04-falsifiability` | `tensorx/glm-5.2` | **MAJOR** the proposed test has false-pass probability ~0.45 and proves nothing |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **FATAL** complete sensory block makes the allodynia endpoint non-diagnostic and cannot identify a pathological peripheral generator, 97% |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **MINOR** The design is sound for its mechanistic claim, but the conjecture should state the flare risk explicitly with a pre-specified monitoring plan, and should acknowledge that the stratified analysis (lesion-identifiable vs. not) is underpowered at n=20, so the diagnostic-reallocation rival will not be fully resolved by this study alone. |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.18 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.15 |
| zai | `tensorx/glm-5.2` | **REFUTED** | 0.05 |
| google | `vertex/gemini-3.5-flash@eu` | **REFUTED** | 0.15 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
