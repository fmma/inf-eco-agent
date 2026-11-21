I've confirmed the situation from the code and the prompt. Here's the key logic in `generate_news.py`:

- `find_top_papers` only downloads PDFs for papers with `score >= 70` scored today (`SCORE_THRESHOLD = 70`).
- The PDF section is added to the prompt **only if** `pdf_paths` is non-empty.

The one new paper, "Seer," scored **42** on relevance — below 70 — so no PDF was downloaded and my prompt has no `## Full-Text PDFs` section. The list of PDF paths I'm instructed to Read is therefore empty (nothing to read), and no paper clears the minimum-70 bar for featuring.

"Seer" is categorically an agent-reasoning/decision-model paper, not an inference-systems paper, so full text wouldn't move its topicality score into range. The correct, non-fabricated output is a clean "nothing featured today" bulletin. Per the output rules, I'm emitting raw markdown only (first character `#`, no preamble, no file writes):

# Inference Ecosystem — Flash News
**2026-11-21 · 1 paper scanned · 0 featured**

Quiet day — no new paper cleared the relevance bar for inference systems.

The only paper scanned, [Seer: Guiding Small Deep-Research Agents with Shared Decision Models](https://arxiv.org/abs/2611.26423), is an agent-reasoning method: it trains an offline tool-response simulator and a value estimator to steer on-device deep-research agents at inference time, reusing both across agents without per-model retraining (GAIA accuracy jumps 13.6%→41.7% on Qwen3.5-4B and 22.3%→50.5% on Qwen3.5-9B). Genuinely useful for agent builders, but it's about *what an agent decides to do next* — not how an LLM is served or optimized, with no KV-cache, batching, quantization, or kernel angle. It scored 42/100 on relevance and isn't featured.

See Surge Watch below for movement on papers already on the board.

---

## Surge Watch

**SSD-served MoE is the GitHub story of the month.** [The Other Half of the Memory Wall](https://arxiv.org/abs/2609.18063) — serving 35B MoEs off SSD with trained routing prediction — ran 9,170→12,140 GitHub stars since Nov 9 (roughly 3k→12k since early October), with HF upvotes ticking 31→36 on Nov 21. A rare sustained real-time surge in a month where most repos have flatlined.

**The spec-decode cohort keeps compounding.** [DSpark](https://arxiv.org/abs/2607.05147) doubled from 42→91 citations (influential 19→45) in two weeks, and [DFlash](https://arxiv.org/abs/2602.06036) pushed 202→218 with influential cites now at 87 — the fastest-citing cluster on the board, and still not cooling.

**DeepSeek-V4.1-Flash finally stalled.** After the 191→234 run we flagged as "still rising," [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) sat flat at 234 citations across Nov 20–21 — its first pause since breaking out.
