# Tally: C-006-flavin-13c-magnetic-isotope-effect

**VERDICT: REFUTED** — 1 gate(s) returned FATAL

Median P(substantially correct) across laboratories: **0.55** (spread 0.75)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** Does a radical-pair process exist in nociceptive tissue and causally alter pain-relevant signalling under fields compatible with a physically realizable intervention? |
| `01-physical-plausibility` | `tensorx/kimi-k3` | **MINOR** supply the pre-registered simulated B½ shift and yield-change amplitude for a single ¹³C at C4a (anchoring the 0.5 mT threshold to a prediction), and one paragraph demonstrating that the Schleicher route labels C4a site-specifically rather than uniformly. |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **FATAL** the flavin-tryptophan radical pair requires photoexcitation and is validated only in avian cryptochrome magnetoreception; no mechanism is proposed or evidenced by which such a radical pair forms in mammalian nociceptive neurons, and the conjecture's implicit biological claim therefore has no connection to the nervous system it purports to calibrate. |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MINOR** 2 citations need correction |
| `04-falsifiability` | `tensorx/glm-5.2` | **PASS**  |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `tensorx/kimi-k3` | **GATE FAILED TO RUN**  |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **PASS**  |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.10 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.55 |
| zai | `tensorx/glm-5.2` | **NOT REFUTED** | 0.50 |
| moonshot | `tensorx/kimi-k3` | **NOT REFUTED** | 0.65 |
| google | `vertex/gemini-3.5-flash@eu` | **NOT REFUTED** | 0.85 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
