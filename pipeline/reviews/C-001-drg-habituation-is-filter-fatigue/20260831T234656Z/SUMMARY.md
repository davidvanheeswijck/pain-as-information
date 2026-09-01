# Tally: C-001-drg-habituation-is-filter-fatigue

**VERDICT: REFUTED** — only 2/5 laboratories failed to refute

Median P(substantially correct) across laboratories: **0.15** (spread 0.10, suspiciously tight: check whether the panel is actually independent)

## Gate verdicts

| Gate | Reviewer | Verdict |
|---|---|---|
| `00-triage` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **CHEAP KILL AVAILABLE** run a small fixed-pattern-versus-sham chronic pilot to determine whether C-fibre T-junction filtering declines at all |
| `01-physical-plausibility` | `tensorx/kimi-k3` | **MINOR** supply the homeostatic decay time constant of T-junction filtering under chronic fixed-pattern stimulation, or pilot evidence that it decays within 28 days in rat; the conjecture assumes rodent decay runs ~1–1.5 orders of magnitude faster than the human clinical course (months–years), and the entire crossover is void if filtering has not decayed by day 28. |
| `02-biological-plausibility` | `tensorx/deepseek-v4-pro-0424` | **MAJOR** The T-junction filtering mechanism is real but the conjecture treats C-fibre traffic as a labelled line for pain, which the evidence does not support; in established neuropathic pain the relevant traffic is on Aβ fibres and the relevant pathology is central, so gating C-fibre propagation at the T-junction does not address the mechanism of the disease. |
| `03-evidence-integrity` | `vertex/gemini-3.5-flash@eu` | **GATE FAILED TO RUN**  |
| `04-falsifiability` | `tensorx/glm-5.2` | **MAJOR** the proposed test has false-pass probability ~0.5 and proves nothing, because it measures an electrophysiological proxy without behavioral allodynia, failing to distinguish the conjecture from central compensation. |
| `05-prior-art` | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **PASS** genuinely open or incremental with a stated delta |
| `06-hostile-referee` | `tensorx/kimi-k3` | **GATE FAILED TO RUN**  |
| `07-clinical-translation` | `tensorx/deepseek-v4-pro-0424` | **MINOR** the translational detail to work out is the human evidence standard: the animal mechanism is testable and blindable, but the clinical claim ("vary pattern, not amplitude") cannot be tested in a fully blinded reprogramming trial, so the programme must pre-commit to an open-label design with objective activity monitoring and a pre-registered responder threshold, and must state plainly that the resulting evidence is a lower grade than the animal result. |

## Panel

| Laboratory | Reviewer | Vote | P |
|---|---|---|---|
| openai | `azure/openai-responses/gpt-5.6-sol@swedencentral` | **REFUTED** | 0.10 |
| deepseek | `tensorx/deepseek-v4-pro-0424` | **REFUTED** | 0.15 |
| zai | `tensorx/glm-5.2` | **NOT REFUTED** | 0.15 |
| moonshot | `tensorx/kimi-k3` | **NOT REFUTED** | 0.20 |
| google | `vertex/gemini-3.5-flash@eu` | **REFUTED** | 0.20 |

---

Move this conjecture's `status` to match, record the posterior in its
front matter, and append to `ledger/REFUTED.md` or `ledger/OPEN.md`.
Refuted conjectures are closed with a reason, never deleted.
