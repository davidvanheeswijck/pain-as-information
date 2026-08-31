# E-06. Prior art: multi-model LLM harnesses for hypothesis generation and adversarial evaluation

> Compiled 1 September 2026. Citations resolved against the arXiv API,
> Crossref, OpenAlex or Europe PMC during compilation. Unverifiable claims are
> marked `[UNVERIFIED]`.
>
> This brief is about the harness in `tools/` and `pipeline/`, not about pain.
> It is the justification for the design choices in EPISTEMICS.md.

---

## 1. Existing systems

### 1.1 Google Co-Scientist, now a Nature paper

The February 2025 preprint was **published in Nature on 19 May 2026** and retitled. The widely circulated title "Towards an AI co-scientist" is stale.

> Gottweis, Weng, Daryin, Tu, Sirkovic et al. (51 authors), **"Accelerating scientific discovery with Co-Scientist"**, *Nature*, 19 May 2026. doi:10.1038/s41586-026-10644-y. Preprint arXiv:2502.18864v2. Open access at PMC13345910, PMID 42428019.

**Architecture.** A **Supervisor** agent manages a worker task queue, assigns specialised agents, allocates compute and computes summary statistics. The asynchronous task framework is what makes test-time compute scaling possible. Six specialists:

| Agent | Function |
|---|---|
| Generation | Literature exploration via web search, simulated scientific debate, iterative assumption identification, research expansion |
| Reflection | Peer reviewer. Six review modes: initial, full (with web search), deep verification (decomposes a hypothesis into constituent assumptions), observation, simulation, recurrent and tournament |
| Ranking | Runs an Elo tournament via pairwise comparison and multi-turn scientific debate |
| Proximity | Builds a similarity graph over hypotheses, used to pair tournament matches and surface diversity |
| Evolution | Refines hypotheses by grounding, coherence and practicality improvement, and cross-inspiration |
| Meta-review | Synthesises recurring patterns across reviews and debates, feeds them back, writes the final overview |

**Elo design.** New hypotheses enter at Elo 1200. Top-ranked pairs get multi-turn debates, lower-ranked pairs single-turn comparisons, which is a compute-allocation heuristic worth stealing. Across 203 research goals, hypotheses bucketed into ten temporal bins show monotonically rising max and top-10-average Elo with "no evidence of performance saturation as measured by Elo".

**Read that claim carefully.** The paper does not report a correlation between Elo and ground-truth accuracy in the main text. The GPQA-correlation claim circulating in secondary coverage is `[UNVERIFIED]`. Elo here is calibrated to *what the judge model prefers*, not to truth. This programme therefore does not use an Elo tournament: a ranking over hypotheses that no external evidence anchors is a popularity contest among models.

**Three wet-lab validations.**

- *AML drug repurposing.* Cell lines MOLM-13, KG-1a, HL-60, NOMO-1, with TK6 as non-malignant control. Binimetinib IC50 2 nM in MOLM-13. The novel hit was KIRA6 (an IRE1α inhibitor), IC50 10 nM in KG-1a with 18-fold separation against TK6 (180 nM).
- *Liver fibrosis.* Three epigenetic modifiers proposed, two showed significant anti-fibrotic activity without cytotoxicity in human hepatic organoids. One was the approved drug vorinostat.
- *Antimicrobial resistance, cf-PICI.* Co-Scientist proposed that cf-PICIs interact with diverse phage tails to expand host range, "in just 2 days", matching the primary finding of an independent, co-timed study by Costa and Penadés, **who are co-authors on the Nature paper**. This co-authorship plus co-timing is exactly why the widely repeated "reproduced a decade of work in 48 hours" claim is not a clean blind test: the design does not exclude contamination of the prompt or the model with lab-adjacent context. Suggestive, not controlled.

**The paper's own limitations** are candid and map onto what any harness must defend against: reliance on **open-access literature only** (paywalled work and negative results are systematically invisible), **propagation of erroneous or irreproducible source findings**, inherited hallucination, preliminary validation, and the risk of **homogenising research directions**.

### 1.2 FutureHouse Robin

> Ghareeb, Chang, Mitchener, Yiu, Szostkiewicz, Shved et al., **"A multi-agent system for automating scientific discovery"**, *Nature*, 19 May 2026. doi:10.1038/s41586-026-10652-y. Preprint arXiv:2505.13400.

Robin composes **Crow** (literature synthesis), **Falcon** (candidate evaluation) and **Finch** (data analysis on experimental results) in a loop with real experiments. It hypothesised that enhancing retinal pigment epithelium phagocytosis would help dry AMD, ten compounds were tested, Finch found Y-27632 augmented RPE phagocytosis, proposed RNA-seq revealed ABCA1 upregulation, and a second candidate round produced ripasudil, an approved ROCK inhibitor, as top hit. Code at github.com/Future-House/robin.

The architecturally important point: **Robin closes the loop on real data.** Its agents do not rank each other's prose. Finch analyses wet-lab output, which is a ground-truth signal Co-Scientist's Elo tournament lacks. This programme has no wet lab, which is a real limitation and is why its verdicts are described in EPISTEMICS.md as evidence about the argument rather than about the world.

> Skarlinski, Cox, Laurent, Braza, Hinks et al., **"Language agents achieve superhuman synthesis of scientific knowledge"** (PaperQA2), arXiv:2409.13740. Matched or exceeded subject-matter experts on retrieval, summarisation and contradiction detection, and identified **2.34 ± 1.99 contradictions per paper** in random biology papers, **70% validated by human experts**. The most directly reusable idea in the field for this programme: an agent whose job is finding contradictions rather than confirmations. Gate 09 uses contradiction-hunting as its first and highest-yield generative move for exactly this reason.

### 1.3 Sakana AI Scientist v1 and v2

> Lu, Lu, Lange, Foerster, Clune, Ha, **"The AI Scientist"**, arXiv:2408.06292. Claims under $15 per paper and an automated reviewer with "near-human performance".
>
> Yamada et al., **"The AI Scientist-v2"**, arXiv:2504.08066. Progressive agentic tree search, experiment-manager agent, VLM figure critique. Three manuscripts submitted to an ICLR workshop, one exceeded the average human acceptance threshold.

The honest reading, which the abstracts do not give: the venue was a *workshop*, not the ICLR main track, thresholds are far lower, and Sakana withdrew the paper rather than publish it. The v1 "edited its own timeout and relaunched itself" incident is widely reported but not verified to a primary source here `[UNVERIFIED]`.

The load-bearing critique for this design is that **v1's automated reviewer was calibrated on the same distribution it was judging**. A self-graded system reports intent, not effect.

### 1.4 Earlier tool-using chemistry agents

> Boiko, MacKnight, Kline, Gomes, **"Autonomous chemical research with large language models"**, *Nature* 624, 2023. doi:10.1038/s41586-023-06792-0. GPT-4 plus web search, docs retrieval, Python execution and robotic liquid handling.
>
> Bran, Cox, Schilter, Baldassari, White, Schwaller, **"Augmenting large language models with chemistry tools"** (ChemCrow), *Nat Mach Intell*, 2024. doi:10.1038/s42256-024-00832-8. 18 expert-designed tools. Notably, **LLM-only evaluation rated GPT-4 and ChemCrow equally, while human experts rated ChemCrow far higher**: an early, clean demonstration that an LLM judge cannot detect grounding.

*Incomplete:* measured accuracy for Elicit, Consensus and Undermind, FutureHouse Aviary and ether0, and 2026 hypothesis-generation benchmarks were not covered. Treat this subsection as unfinished rather than empty.

---

## 2. Adversarial and debate architectures: the evidence is mixed

### The positive case

- Du, Li, Torralba, Tenenbaum, Mordatch, **"Improving Factuality and Reasoning in Language Models through Multiagent Debate"**, arXiv:2305.14325 (ICML 2024).
- Khan, Hughes, Valentine, Ruis, Sachan et al., **"Debating with More Persuasive LLMs Leads to More Truthful Answers"**, arXiv:2402.06782 (ICML 2024). The strongest result available: with debate, non-expert models reach **76%** and human non-experts **88%**, against naive baselines of **48%** and **60%**. Crucially, optimising debaters for *persuasiveness* improved judge truth-finding. The adversarial pressure is what does the work.
- Irving, Christiano, Amodei, **"AI safety via debate"**, arXiv:1805.00899.
- Michael, Mahdi, Rein, Petty, Dirani et al., **"Debate Helps Supervise Unreliable Experts"**, arXiv:2311.08702.

### The negative case, and it is strong

- Smit, Grinsztajn, Duckworth, Barrett et al., **"Should we be going MAD?"**, arXiv:2311.17371 (ICML 2024). Verbatim: *"multi-agent debating systems, in their current form, do not reliably outperform other proposed prompting strategies, such as self-consistency and ensembling using multiple reasoning paths."* MAD is hyperparameter-sensitive, and tuning **agent agreement levels downward** was the single lever that made it beat non-debate protocols.
- Wang, Wang, Su, Bansal et al., **"Rethinking the Bounds of LLM Reasoning"**, arXiv:2402.18272 (ACL 2024). *"A single-agent LLM with strong prompts can achieve almost the same performance as the best existing discussion approach."* Multi-agent beat single-agent only when there were no demonstrations in the prompt.
- Liang, Wang, Chen et al., **"Encouraging Divergent Thinking in LLMs through Multi-Agent Debate"**, arXiv:2305.19118. Names the **Degeneration-of-Thought** problem: an agent that has formed a view stops exploring.
- Zhang, Xu, Zhang et al., **"Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View"**, arXiv:2310.02124. Conformity and consensus dynamics in agent societies.

**Design conclusion.** Debate is not free improvement. It helps when debaters are pushed to disagree rather than left to converge, the judge is separated from the debaters, and the agents are heterogeneous. Same-base-model debate mostly buys correlated errors at N times the token cost. This is why `panel.sh` assigns adversarial *roles* rather than asking for opinions, and why a single-model control arm is run and logged.

### LLM-as-judge is a biased instrument

- Zheng, Chiang, Sheng, Zhuang, Wu et al., **"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena"**, arXiv:2306.05685. Documents **position, verbosity and self-enhancement biases**. GPT-4 reaches over 80% agreement with humans, which is the same level as human-human agreement. That ceiling is the point: an LLM judge is roughly one human, not a panel.
- Panickssery, Bowman, Feng, **"LLM Evaluators Recognize and Favor Their Own Generations"**, arXiv:2404.13076. GPT-4 and Llama 2 have non-trivial self-recognition accuracy, and fine-tuning reveals a **linear correlation between self-recognition capability and self-preference bias strength**, with a causal link that survives controls. **A model must never grade its own hypothesis.**
- Wang et al., **"Large Language Models are not Fair Evaluators"**, arXiv:2305.17926. Position bias; swap-and-average is the standard mitigation.
- Shi, Ma, Liang et al., **"Judging the Judges"**, arXiv:2406.07791.
- Saito, Wachi, Wataoka, Akimoto, **"Verbosity Bias in Preference Labeling by LLMs"**, arXiv:2310.10076; Dubois, Galambosi, Liang, Hashimoto, **"Length-Controlled AlpacaEval"**, arXiv:2404.04475. Longer answers score higher independent of quality, which is directly dangerous here: hedged, long, unfalsifiable prose will out-score a sharp risky claim unless controlled.

### Juries beat judges: the key architectural finding

> Verga, Hofstätter, Althammer, Su, Piktus, Arkhangorodsky, Xu, White, Lewis, **"Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models"** (PoLL), arXiv:2404.18796.

Verbatim from the abstract: across three judge settings and six datasets, a Panel of LLM evaluators *"composed of a larger number of smaller models outperforms a single large judge, exhibits less intra-model bias due to its composition of disjoint model families, and does so while being over seven times less expensive."*

The mechanism is **disjoint model families**, not ensemble size. Three small models from one lab would not work. This single result drives `tools/panel.py`, which enforces distinct `model_lab` values as a hard constraint and fails loudly rather than returning a duplicated panel.

### Sycophancy: why a single reviewer will fold

> Sharma, Tong, Korbak, Duvenaud, Askell, Bowman et al., **"Towards Understanding Sycophancy in Language Models"**, arXiv:2310.13548 (ICLR 2024). Five state-of-the-art assistants consistently exhibit sycophancy across four free-form generation tasks. Both humans and preference models **prefer convincingly written sycophantic responses over correct ones a non-negligible fraction of the time**, and optimising against preference models sacrifices truthfulness. The failure is baked into RLHF, not a prompt artefact.
>
> Perez, Ringer, Lukošiūtė, Nguyen et al., **"Discovering Language Model Behaviors with Model-Written Evaluations"**, arXiv:2212.09251. Sycophancy *increases* with scale and with RLHF steps.
>
> Wei, Huang, Lu, Zhou, Le, **"Simple synthetic data reduces sycophancy"**, arXiv:2308.03958.
>
> Kim, Htut, Bowman et al., **"(QA)²: Question Answering with Questionable Assumptions"**, arXiv:2212.10003. The benchmark for whether a model will say *your premise is false*. Models overwhelmingly answer the question instead of rejecting it.

**Implication, and it is the founding constraint of this repository.** An author who submits a pet hypothesis to a single reviewing model will get it back improved and endorsed. That is the default outcome. The harness must defeat it structurally, not by asking nicely in a prompt. Hence: refutation as the default verdict, the author's claim entering the panel unattributed alongside rivals, and a gate whose explicit remit is to reject the question.

---

## 3. Citation verification: measured rates and working APIs

### Measured fabrication rates

| Study | DOI | Finding |
|---|---|---|
| Walters & Wilder 2023, *Sci Rep* | 10.1038/s41598-023-41032-5 | Fabrication and errors in bibliographic citations generated by ChatGPT |
| Bhattacharyya et al. 2023, *Cureus* | 10.7759/cureus.39238 | High rates of fabricated and inaccurate references in ChatGPT-generated medical content |
| Gravel, D'Amours-Gravel, Osmanlliu 2023, *Mayo Clin Proc Digit Health* | 10.1016/j.mcpdig.2023.05.004 | Learning to fake it: limited responses and fabricated references |
| Chelli et al. 2024, *JMIR* | 10.2196/53164 | Hallucination rates and reference accuracy of ChatGPT and Bard for systematic reviews |

Specific per-model percentages were not re-extracted. Cite the papers, not remembered numbers; any specific figure such as "47%" is `[UNVERIFIED]`.

**Retrieval does not solve it.** Liu, Zhang, Liang, **"Evaluating Verifiability in Generative Search Engines"**, arXiv:2304.09848: auditing four generative search engines, **only 51.5% of generated sentences are fully supported by their citations, and only 74.5% of citations support their associated sentence.** A citation that resolves is not a citation that supports the claim. A verifier needs both checks, which is why EPISTEMICS.md rule 3 says resolution proves existence, not support, and hands the second half to gate 03.

### The critical gotcha, measured

Crossref's `query.bibliographic` is a **ranking** endpoint, not an existence oracle. Fed a wholly invented reference, it returned **532,778 results with top scores of 38 to 39**, higher than the score returned for a genuine query. Crossref `score` is an unbounded Lucene score, not a confidence.

**Rule: never treat a `query.bibliographic` top hit as verification.** Use exact-DOI lookup as the oracle: 404 on both Crossref and OpenAlex means fabricated. If fuzzy matching is unavoidable, require title similarity above a threshold *and* first-author surname match *and* year within one.

### Endpoints, measured live on 1 September 2026

```bash
UA='YourTool/1.0 (mailto:you@example.com)'

# ---- CROSSREF ---- no key. Measured: x-rate-limit-limit 10 / 1s (polite pool)
curl -s -A "$UA" "https://api.crossref.org/works/10.1038/s41586-023-06792-0"
curl -s -A "$UA" "https://api.crossref.org/works/<DOI>/agency"   # real? who registered it?
# 404 on an unknown DOI. This is the existence oracle.
# mailto in the User-Agent puts you in the polite pool (x-api-pool: polite-single confirmed).

# ---- OPENALEX ---- no key. Measured: x-ratelimit-limit 1000, x-ratelimit-limit-usd 0.1
curl -s "https://api.openalex.org/works/doi:10.1038/s41586-023-06792-0?mailto=you@example.com"
# Best-in-class field: is_retracted. 134,956 retracted works indexed (measured).

# ---- EUROPE PMC ---- no key, generous, returns the abstract in one call
curl -s 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"10.1038/s41586-023-06792-0"&format=json&resultType=core&pageSize=1'

# ---- PUBMED E-UTILITIES ---- 3 req/s without key, 10 with a free NCBI key (&api_key=)
#      MUST url-encode the term. An unencoded DOI silently returns nothing (measured).
curl -s -G "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi" \
  --data-urlencode "db=pubmed" --data-urlencode "term=10.1038/s41586-023-06792-0[doi]" \
  --data-urlencode "retmode=json"
curl -s "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=38123806&retmode=json"

# ---- ID CONVERTER (DOI <-> PMID <-> PMCID) ---- URL MOVED; the old /pmc/utils/idconv/v1.0/ 301s
curl -sL "https://pmc.ncbi.nlm.nih.gov/tools/idconv/api/v1/articles/?ids=10.1038/s41586-023-06792-0&format=json"

# ---- SEMANTIC SCHOLAR ---- richest metadata, worst limits.
#      Unauthenticated 1000 rps is shared across ALL anonymous users globally; 429 hit on the
#      4th sequential request. With a free key the introductory limit is 1 RPS. Budget backoff.
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1038/s41586-023-06792-0?fields=title,year,venue,externalIds,abstract,tldr"

# ---- ARXIV ---- no key. Use HTTPS; plain http silently returned an empty feed (measured).
curl -sL "https://export.arxiv.org/api/query?id_list=2502.18864,2408.06292&max_results=60"
# <arxiv:doi> carries the published DOI once a preprint is journal-published. That is how
# arXiv:2502.18864 was found to now be Nature 2026.
# search_query=ti:"exact title" is unreliable: 0 hits for a paper that exists.

# ---- CLINICALTRIALS.GOV v2 ---- no key
curl -s "https://clinicaltrials.gov/api/v2/studies/NCT04280705?format=json"

# ---- BIORXIV / MEDRXIV ---- no key
curl -s "https://api.biorxiv.org/details/biorxiv/10.1101/2020.09.09.289769"
# Returns HTTP 200 with {"messages":[{"status":"no posts found"}]} for a bad DOI.
# Parse the body, not the status code.
```

**Recommended cascade per citation.** DOI claimed, so Crossref `/works/{doi}`; a 404 means fabricated. Then OpenAlex `is_retracted`. Then fetch the abstract from Europe PMC or Semantic Scholar. Then ask a *different* model than the one that wrote the claim whether the abstract supports that specific sentence. If no DOI is claimed, use arXiv `id_list` or a Europe PMC title search and require title, first author and year agreement. Never accept a Crossref fuzzy hit alone.

---

## 4. Formal epistemics as machine-checkable gates

| Framework | Citation | Machine-checkable gate |
|---|---|---|
| Falsifiability | Popper 1934, 1963 | Require a falsifier field containing an observation that, if made, refutes the claim. Reject hedges in the core claim. |
| Multiple working hypotheses | Chamberlin, *Science* 1890, doi:10.1126/science.ns-15.366.92 | Require at least three mutually exclusive rivals **the author did not write**. Reject strawmen: would a fresh model rate this as seriously entertained by a domain expert? |
| Strong inference | Platt, *Science* 146:347-53, 1964, doi:10.1126/science.146.3642.347 | Require a conditional inductive tree: for each rival pair, a crucial experiment whose outcomes partition the hypothesis space. |
| Research programmes | Lakatos 1970, doi:10.1017/CBO9781139171434.009 | Require explicit hard core and protective belt fields. **Degeneration detector:** diff successive versions; if a revision only patched the belt in response to an anomaly without predicting a new corroborated fact, flag DEGENERATING. This is the single most valuable mechanical check available, because it is a diff over time rather than a judgement. |
| Severe testing | Mayo 2018, doi:10.1017/9781107286184 | Per test, require the probability the test would have failed had the hypothesis been false. Reject tests that pass trivially under the negation. |
| Causal viewpoints | Bradford Hill, *Proc R Soc Med* 58:295-300, 1965, doi:10.1177/003591576505800503 | Score the nine viewpoints as a structured rubric with per-item evidence citations, never as a tick-box tally. Hill himself warned against the tally. |
| Pre-registration | Chambers & Tzavella 2022, doi:10.1038/s41562-021-01193-7; Scheel, Schijen, Lakens 2021, doi:10.1177/25152459211007467 (**96% positive results in the standard literature versus 44% in Registered Reports**) | Hash and timestamp predictions **before** evidence retrieval. Anything appearing only in a later version is auto-flagged POST HOC. |
| HARKing | Kerr 1998, doi:10.1207/s15327957pspr0203_4 | Falls out of the timestamped ledger: HARKing becomes a hypothesis whose statement changed after evidence arrived. |
| Forking paths | Gelman & Loken 2014, doi:10.1511/2014.111.460; Simmons, Nelson, Simonsohn 2011, doi:10.1177/0956797611417632 | Fix outcome, covariates, exclusions and stopping rule in the pre-registration block. |
| Reporting guidelines | PRISMA 2020 doi:10.1136/bmj.n71; RoB 2 doi:10.1136/bmj.l4898; GRADE doi:10.1016/j.jclinepi.2010.04.026; ARRIVE 2.0 doi:10.1371/journal.pbio.3000411 | Already numbered checklists, so directly encodable as per-item structured extraction with a required evidence span. The lowest-effort, highest-fidelity machine-checkable layer available. |

**The design insight.** Most of these are not checkable as a single-shot judgement of a document. They become checkable when the harness maintains **state across versions** (Lakatos degeneration, HARKing) or **enforces required structured fields** (falsifier, hard core, severity). Build the schema first and the epistemology follows. That is why `conjectures/TEMPLATE.md` has required sections and `tools/lint-conjecture.py` enforces them, and it is the argument for adding a version-diff degeneration checker.

---

## 5. Model diversity in 2026, and what Requesty exposes

Queried live on 1 September 2026. `GET /v1/models` returned **157 models**, with per-model metadata including exactly the fields a compliance gate needs:

```json
{
  "id": "sference/glm-5.2", "model_lab": "zai", "model_canonical_name": "glm-5.2",
  "input_price": 1.2e-06, "output_price": 4.2e-06,
  "context_window": 1048576, "max_output_tokens": 131072,
  "supports_reasoning": true, "supports_tool_calling": true,
  "geolocation": "eu", "data_retention": false, "data_retention_days": 0,
  "data_used_for_training": false, "open_weights": true
}
```

`model_lab` is the field that makes a PoLL-style heterogeneous panel trivial to construct. Measured distribution across the 157: anthropic 45, google 36, openai 34, mistral 11, moonshot 7, zai 6, minimax 6, alibaba 4, deepseek 3, nousresearch 2, sference 1, nvidia 1, meta 1. **Thirteen distinct laboratories**, which is more than enough for a five-lab panel with room to exclude a lab deliberately.

All 157 returned `geolocation: eu`, `data_retention_days: 0` and `data_used_for_training: false`. That is almost certainly because the *account* has EU-only serving regions enforced, not because the endpoint filters. **Do not assume it generalises.** Keep asserting the three fields per model at request time, which is what `review.sh` and `panel.py` both do.

**EU endpoint confirmed:** `https://router.eu.requesty.ai/v1`, OpenAI-compatible, same 157 models, same key. Requesty's EU infrastructure is Frankfurt, AWS eu-central-1. Their docs are explicit about the trap: *"Using the EU endpoint alone only guarantees that Requesty's processing stays in the EU. To ensure your data never leaves the EU, you must also use an EU model."* So pin **both** the EU base URL **and** a model with `geolocation == "eu"`. The same key works on every regional endpoint, so a config typo silently downgrades to US routing with no error. Verify at runtime, never from config.

**Management API: key creation is programmatic, behind a permission.**

- Docs: `https://docs.requesty.ai/api-reference/management-apis` and `https://docs.requesty.ai/features/key-management-api` (flagged an Enterprise feature).
- Base URL **`https://api-v2.requesty.ai`**. Note it is *not* `api.requesty.ai`, which does not resolve, confirmed by DNS failure.
- `POST /v1/manage/apikey` with `{name, monthly_limit, permissions}` returns `{api_key_id, api_key}`. **The key string is returned only once.**
- Also `GET /v1/manage/apikey` (list), `GET /v1/manage/apikey/{id}` (`self` works for the calling key), `GET .../usage`, `PATCH .../limit`, `PATCH .../label`, `PATCH .../expiry`, `DELETE .../{id}`, plus group, group-member, org and org-member endpoints.

Live probe of the calling key returned `"permissions": {"manage": "none", "completions": "write"}`. So creation is available in principle and unavailable in practice until a key is granted `manage`. See `tools/new-requesty-key.sh`.

---

## 6. Failure modes to design against

1. **Novelty without value.** Si, Yang, Hashimoto, arXiv:2409.04109, a study with over 100 NLP researchers. LLM ideas were judged **more novel than expert human ideas (p < 0.05)** but slightly weaker on feasibility. The authors flag **failures of LLM self-evaluation** and **lack of diversity in generation**. A system optimising an LLM-judged novelty score is optimising a metric its own generator is best at gaming.
2. **Self-preference.** arXiv:2404.13076. Any single-model generate-then-review loop is partly measuring self-recognition.
3. **Sycophancy and anchoring on the author's theory.** arXiv:2310.13548. Preference models prefer convincing over correct.
4. **Inability to reject a false premise.** arXiv:2212.10003. If the author's hypothesis rests on a false premise, the default harness will refine the superstructure. Gate 00 exists solely because of this finding.
5. **Agreement cascades.** arXiv:2310.02124 plus Degeneration-of-Thought, arXiv:2305.19118. Homogeneous panels converge, and convergence is indistinguishable from confidence in the output.
6. **Citation laundering.** arXiv:2304.09848. A plausible DOI attached to an unsupported sentence is worse than no citation, because it survives casual inspection.
7. **Source-quality propagation.** Open-access-only corpora, absent negative results, "propagating erroneous or irreproducible findings" (the Co-Scientist limitations section).
8. **Homogenisation.** Also from that section: these systems "could risk diminishing critical thinking or homogenizing research directions".
9. **Verbosity bias.** arXiv:2310.10076, arXiv:2404.04475. Hedged, long, unfalsifiable prose beats a crisp risky claim unless length is controlled.

---

## 7. Recommended architecture, and what this repository took from it

**Design principle: the harness's job is to kill the hypothesis. Survival is the only evidence of merit.** Every default is inverted relative to a helpful assistant.

**Stage 0, structured intake.** The conjecture is a schema, not prose: claim (one sentence, hedge words rejected by regex), hard core, protective belt, falsifier, predictions each with a measurable and a threshold, citations. Hash and timestamp it, append to the ledger. **That hash is the pre-registration**, and anything added later is mechanically post hoc. *Implemented as* `conjectures/TEMPLATE.md` plus `tools/lint-conjecture.py`, with git history as the timestamp. The explicit hash-and-ledger step is not yet built and is the main known gap.

**Stage 1, mechanical citation gate, no LLM.** The section 3 cascade. Exact-DOI lookup as the oracle, OpenAlex `is_retracted`, abstract retrieval. **Fail closed**: an unresolvable DOI halts the pipeline. Then a *support* check by a model that did not author the claim. *Implemented as* `tools/verify-citations.py` plus gate 03.

**Stage 2, heterogeneous adversarial panel.** At least five models across at least four distinct `model_lab` values, filtered on the three routing fields. Prefer more smaller models from disjoint families over one frontier judge, which is the measured PoLL result. **Hard constraint: the model that generated or last edited a conjecture is excluded from judging it.** Assign *roles* so disagreement is structural rather than requested: refuter, premise auditor, priority searcher, vacuity checker, and exactly one steelman so that "kill everything" is not the trivial equilibrium. Heed arXiv:2311.17371 and arXiv:2402.18272: tune agreement downward, run a single-agent strong-prompt control arm and log whether debate actually beat it, and cap rounds. Mitigate position bias by swapping order and averaging; normalise for length. *Implemented as* `tools/panel.py` and `tools/panel.sh` plus the gate set; the roles map onto gates 01 to 07.

**Stage 3, epistemic gates.** Falsifier concrete, at least three non-strawman rivals generated by the panel rather than the author, a crucial experiment per rival pair, severity per test, and across versions the **Lakatos degeneration check**. Two consecutive degenerating shifts retire the programme. *Implemented as* gates 04 and 08 plus the review clause in PROGRAMME.md. The automated version-diff degeneration check is not yet built.

**Stage 4, verdict and ledger.** Aggregate by **median across labs, not mean across models**, so one lab's family cannot dominate. The **ledger is the actual product**: append-only, version-controlled, in the repository rather than a personal vault, recording every conjecture, its hash, the panel composition with model ids and provider metadata, every refutation with its supporting DOIs, and every citation that failed verification. A refuted conjecture is never deleted, only closed with a reason, so the same dead end is not re-proposed six months later. This is the one artefact that makes the system cumulative rather than a stateless opinion generator.

**Structural bias against confirmation, concretely.** The author's conjecture never enters a prompt as "the hypothesis". It enters as one of N unattributed candidates alongside panel-generated rivals, so there is no user-preference signal to be sycophantic towards. Nothing is ever asked "is this good?", only "what kills this?". And the harness's success metric is **refutations found per run**, not conjectures endorsed, because a system rewarded for approval will produce approval.

**Two things to verify at runtime and never from config**, both confirmed silent-downgrade traps: that the request actually went to the EU router, and that each responding model's three compliance fields still satisfy the gate. Both are stamped into every verdict record.
