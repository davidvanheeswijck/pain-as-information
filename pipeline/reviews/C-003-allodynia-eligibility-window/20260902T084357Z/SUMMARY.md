# Tally: C-003-allodynia-eligibility-window

**VERDICT: REFUTED** — only 0/5 laboratories failed to refute

Median P(substantially correct) across laboratories: **0.15** (spread 0.07, suspiciously tight: check whether the panel is actually independent)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** Is spontaneous C-nociceptor activity necessary and trial-by-trial temporally coupled to touch-evoked pain in established allodynia beyond the effects of tonic central disinhibition? |
| `01-physical-plausibility` | `nebius/kimi-k3` | **GATE FAILED TO RUN**  |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MINOR** The experiment is well-designed and worth running, but the clinical translation claim should be removed or explicitly flagged as contingent on peripheral readout of C-fibre discharge (refuted by C-004/C-008), on C-fibre discharge being the sole maintainer of the facilitated state (not tested by the design), and on the anaesthetised rodent τ band generalising to awake humans (not established). |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MAJOR** Ghitani et al. (PMID 40269164) is overstated to claim it suggests a temporal coincidence window when it only reports spontaneous activity. |
| `04-falsifiability` | `tensorx/glm-5.2` | **MINOR** The killer needs blinding for the behavioural outcome and a pre-registered primary outcome to prevent post-hoc selection between electrophysiology and behaviour. |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `nebius/kimi-k3` | **GATE FAILED TO RUN**  |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **MAJOR** no enrichable human population without a bedside measure of the coincidence phenotype; the human mechanism demonstration is a prerequisite that may not be feasible, and the intervention's effect size in humans is unknown. The mouse experiment is worth doing, but it is a mechanism experiment, not a translational one. |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.18 |
| moonshot | `nebius/kimi-k3` | **REFUTED** | 0.15 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.22 |
| zai | `tensorx/glm-5.2` | **REFUTED** | 0.15 |
| google | `vertex/gemini-3.5-flash@eu` | **REFUTED** | 0.15 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
