# Tally: C-005-nociceptor-information-rate

**VERDICT: REFUTED** — only 2/5 laboratories failed to refute

Median P(substantially correct) across laboratories: **0.25** (spread 0.21)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** For a specified stimulus ensemble, does sub-5-millisecond spike timing add information about pain-relevant stimulus features or perception beyond firing rate and unit identity? |
| `01-physical-plausibility` | `tensorx/kimi-k3` | **MINOR** the response-drift (sensitisation/fatigue) time constant of human C-nociceptors under repeated noxious frozen-noise stimulation, set against the 1,800 s per-unit acquisition, with a pre-committed block-interleaving or detrending rule if the two are comparable. |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MINOR** The measurement is worth doing, but the conjecture must state explicitly that a low single-axon information rate in healthy volunteers under natural stimulation does not test HC-2 (peripheral readability of pain-relevant discrimination), does not generalise to neuropathic pain (where the relevant traffic is ectopic, Aβ-mediated, or centrally amplified), and does not constrain the population code that the CNS actually reads. |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MAJOR** Werland et al. (2021) [PMID 33369733] is cited to claim C-nociceptors follow 100 Hz without conduction failure, which is a direct inversion of the study's actual findings. |
| `04-falsifiability` | `tensorx/glm-5.2` | **MAJOR** the proposed test has false-pass probability ~0.6 and proves nothing, because the direct method of information estimation on a 60-second continuous stimulus with only 30 repeats is statistically biased toward underestimation, guaranteeing a favourable result even if the true rate is high. |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `nebius/kimi-k3` | **MAJOR** the refutation rule is unreachable as specified: every estimator bias runs toward confirmation, no estimator or power analysis is named, and the preparation's non-stationarity points the same way (70%) |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **NOT APPLICABLE** mechanistic conjecture with no translational claim |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.14 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.25 |
| zai | `tensorx/glm-5.2` | **NOT REFUTED** | 0.35 |
| moonshot | `tensorx/kimi-k3` | **NOT REFUTED** | 0.25 |
| google | `vertex/gemini-3.5-flash@eu` | **REFUTED** | 0.20 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
