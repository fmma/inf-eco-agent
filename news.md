I've now traced the full flow, and here's what's actually happening this cycle:

**Both of today's papers are off-topic for LLM inference, and there are no PDFs to read.** `generate_news.py:65-73` only downloads PDFs for papers scoring ≥70 today. Today's two papers scored **25** ([PrefReward](https://arxiv.org/abs/2607.21067) — personalized text generation) and **5** ([SPORD](https://arxiv.org/abs/2607.21354) — JD.com supply-chain planning), so zero PDFs were downloaded — which is why the prompt I received has no "Full-Text PDFs" section. The pipeline is behaving correctly; there's simply nothing relevant.

Neither paper clears the minimum-70 bar the prompt requires, and both are plainly outside "LLM inference systems." I won't fabricate features for them, and I won't claim to have read PDFs that don't exist. The honest bulletin for this cycle is:

---

# Inference Ecosystem — Flash News
**2026-07-25 · 2 papers scanned · 0 clear the bar**

Quiet cycle for inference systems — neither of today's two papers is on-topic, so nothing makes the bulletin. [PrefReward](https://arxiv.org/abs/2607.21067) does personalized text generation via a user-preference matrix and a KL-based decoding reward (relevance 25 — touches decoding, but it's a personalization method, not a serving/inference contribution). [SPORD](https://arxiv.org/abs/2607.21354) is JD.com's NetSim supply-chain planning platform — simulation-proposes, integer-program-disposes, with real deployment wins — but it's operations research with no LLM-inference connection (relevance 5). No full-text rescore ran; the PDF-download step correctly skipped both below the 70 threshold. Surge Watch below carries this cycle's real signal.

---

A couple of things worth flagging on the pipeline itself:

- **This is the expected "new papers, but none relevant" path.** `scan.sh:176` invokes `generate_news.py` whenever *any* paper was scored, regardless of relevance, so the news step always runs and Surge Watch gets appended. The output above is the honest thing to emit; scan.sh will append the Surge Watch section and post to Discord.
- **The prompt has no explicit "nothing qualifies" branch.** `news-prompt.md` says "select top 3–5 (minimum 70)" but doesn't say what to do when zero qualify — so the model is left to improvise. If you want deterministic behavior for low-relevance cycles, consider adding a line to `news-prompt.md` like: *"If no paper reaches 70, output only the heading + date + a one-sentence 'no relevant papers this cycle' note."* That would prevent a future run from padding the bulletin with off-topic papers just to fill space.

Want me to add that fallback instruction to `news-prompt.md`?

---

## Surge Watch

The breakout this cycle is [Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980): GitHub stars tripled from 41 (July 10) to 122 (July 24) while HF upvotes climbed 55 → 80 — a genuine two-week ramp behind its "infinite context" sparse-attention pitch. It cleared 100 stars mid-week and is still compounding; easily the strongest fresh momentum in the set. Worth watching whether it holds past 150.

Quieter but real: [OSCAR](https://arxiv.org/abs/2605.17757) (offline 2-bit KV-cache quantization) resurfaced at 552 GitHub stars — nearly double its ~295 from early June — though flat HF upvotes (63 → 66) mark this as steady adoption rather than new buzz.

On the citation front, [DFlash](https://arxiv.org/abs/2602.06036) (block-diffusion speculative decoding) keeps grinding: 42 → 51 citations in under three weeks with 21 influential — the best academic-impact velocity here, even as its HF (89) and ~5.5k stars plateau. The mid-July drafting/quant cohort, by contrast, is still frozen.
