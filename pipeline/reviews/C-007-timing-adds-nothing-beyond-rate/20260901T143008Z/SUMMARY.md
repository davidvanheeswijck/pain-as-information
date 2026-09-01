# Tally: C-007-timing-adds-nothing-beyond-rate

**VERDICT: REFUTED** — only 2/5 laboratories failed to refute

Median P(substantially correct) across laboratories: **0.32** (spread 0.35)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** For a specified stimulus ensemble, does within- or across-fibre spike-train structure improve prediction of perceived pain quality or intensity beyond firing rate and recruited-unit identity? |
| `01-physical-plausibility` | `tensorx/kimi-k3` | **MINOR** the detection floor: smallest timing-information increment detectable at n=20 units × 30 repeats at 1–10 Hz, demonstrated by injection-recovery on surrogate spike trains through the identical pipeline, with the bias-corrected estimator named; the 20% threshold is meaningless until shown to lie above it. |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MINOR** The conjecture is well-posed as a measurement claim about healthy evoked nociception, but it must state explicitly that its outcome cannot bear on HC-1 or HC-2 for neuropathic pain, because the pain-relevant discrimination in that state is constructed centrally from peripherally indistinguishable traffic, and the single-unit healthy-volunteer design cannot distinguish "timing carries no information" from "timing carries information only in populations." |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MINOR** 6 citations need correction |
| `04-falsifiability` | `tensorx/glm-5.2` | **MINOR** the killer's 20% threshold permits results that contradict the conjecture as stated, and the two-ensemble, two-decoder, and two-unit requirements that would make the test discriminating are in Rivals, not in the Killer. |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `tensorx/kimi-k3` | **GATE FAILED TO RUN**  |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **NOT APPLICABLE** mechanistic conjecture with no translational claim |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.32 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.25 |
| zai | `tensorx/glm-5.2` | **NOT REFUTED** | 0.50 |
| moonshot | `tensorx/kimi-k3` | **NOT REFUTED** | 0.60 |
| google | `vertex/gemini-3.5-flash@eu` | **REFUTED** | 0.25 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
