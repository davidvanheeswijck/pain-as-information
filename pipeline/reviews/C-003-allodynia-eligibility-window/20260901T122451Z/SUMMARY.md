# Tally: C-003-allodynia-eligibility-window

**VERDICT: WOUNDED** — only 3/5 laboratories failed to refute; triage returned WRONG QUESTION, so reformulate rather than rebuild; 1 vote(s) could not be parsed and were counted as refutations, because an unreadable vote is not a passing one

Median P(substantially correct) across laboratories: **0.62** (spread 0.67)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **WRONG QUESTION** Is endogenous ongoing C-nociceptor activity necessary for Aβ-evoked pain in established allodynia, rather than merely capable of transiently facilitating an already disinhibited dorsal-horn circuit? |
| `01-physical-plausibility` | `nebius/kimi-k3` | **NO VERDICT LINE**  |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MAJOR** The proposed transient eligibility window of hundreds of milliseconds to seconds is not supported by the physiology of C-fibre-evoked facilitation in the dorsal horn, which is either short (paired-pulse, tens of milliseconds) or long (central sensitisation, minutes to hours); the conjecture needs direct evidence for a facilitation time constant in the proposed range before the killer experiment is worth running. |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **MAJOR** Ghitani et al., 2025 (PMID 40269164) does not support the claim that the authors proposed a temporal-coincidence mechanism for mechanical allodynia. |
| `04-falsifiability` | `tensorx/glm-5.2` | **MAJOR** the proposed test has false-pass probability ~0.6 and proves nothing |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `nebius/kimi-k3` | **NO VERDICT LINE**  |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **NOT APPLICABLE** mechanistic conjecture with no translational claim |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.18 |
| moonshot | `nebius/kimi-k3` | **UNPARSED** | - |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **NOT REFUTED** | 0.55 |
| zai | `tensorx/glm-5.2` | **NOT REFUTED** | 0.70 |
| google | `vertex/gemini-3.5-flash@eu` | **NOT REFUTED** | 0.85 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
