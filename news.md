Writing to the repo is denied too. Let me confirm that's a blanket permission state and not just one path, so I can tell you exactly what's blocking.

The situation is clear now, so let me report it rather than keep probing.

## I can't read the PDFs in this environment

Here's what I tried and what happened:

| Approach | Result |
|---|---|
| **Read tool** on each PDF | ❌ `pdftoppm is not installed` — the Read tool renders PDF pages to images, which needs **poppler** |
| **Ghostscript** (`gs`, which *is* installed) → text | ❌ blocked by permission mode ("requires approval") |
| **`python3`** stdlib extractor (zlib/FlateDecode) | ❌ `python3` blocked by permission mode |
| **Write** a scratch script (repo or `/tmp`) | ❌ Write blocked by permission mode |

Only read-only commands (`ls`, `which`) and `Read` on text files are permitted here, and `Read` can't decode PDFs without poppler. So I **cannot** do the full-text read + rescore that `news-prompt.md` requires. I won't fake it — any bulletin I produce right now is **abstract-only**, and the "(was X)" rescores the prompt asks for would be meaningless without the actual papers.

## How to unblock (pick one)

1. **Install poppler** (best — makes the `Read` tool work exactly as the pipeline expects). On NixOS: add `pkgs.poppler_utils` to `environment.systemPackages` in `fmma/nixos-webserver:configuration.nix`, or for a one-off `nix-shell -p poppler_utils` and launch `claude` from that shell. Then re-run.
2. **Approve a fallback** — allow `gs` (already installed) or `python3` for this session and I'll extract the text myself and do the real full-text rescore.
3. **Accept an abstract-only draft** — I write the bulletin from the (detailed) abstracts now, clearly labeled, no full-text rescore.

## ⚠️ This probably affects the production pipeline too

`generate_news.py` invokes `claude --print --allowedTools "Read"` to read these same PDFs. If the host running the daily scan is missing poppler, that step **silently degrades** — Claude falls back to the abstracts embedded in the prompt and still emits a bulletin, so `scan.sh`'s `ERR` trap never fires and you'd never see it fail. Worth confirming `pdftoppm` exists on whatever host runs the cron scan (`which pdftoppm`), not just here.

---

Since you clearly want the bulletin, here's an **abstract-based draft** so you're not empty-handed. **This is NOT the full-text rescore** — scores are the existing abstract-pass scores, and I've picked the 5 strongest for inference engineers. Don't ship this as the full-text edition:

```markdown
# Inference Ecosystem — Flash News
**2026-11-20 · 301 papers scanned · 5 featured** _(abstract-only draft — PDFs could not be opened)_

[TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming](https://arxiv.org/abs/2611.26619)
Song Han's group tackles the KV-cache heterogeneity of hybrid (global-attention + bounded-state) models on CPU–GPU superchips: a Transparent Cache Pool reshuffles physical pages behind fixed virtual addresses, and a Cache Streamer prefetches the next global-attention layer's prefix during bounded-state compute. Built on SGLang, evaluated on GB300/GH200 across 7 configs — up to 2.04× agent turns, 20–59% lower P50 per-token latency, and 1.40–3.05× better agent TTFT vs SGLang+HiCache. Relevance: 96 (abstract-based).

[FrontierReplay: Split-Free Exact Prefix Caching for Hybrid Language Models](https://arxiv.org/abs/2611.26020)
Exact prefix reuse in hybrid models normally forces the prefill pass to be cut at each checkpoint; FrontierReplay instead materializes exact checkpoints at structural boundaries (turn ends, branch points) without cutting prefill, using a state-only replay kernel that rebuilds state 6–37× cheaper per token than recomputation. Result: 16–89% lower median TTFT (up to 8.9×), up to 1.73× SLO capacity, 4.26× goodput — and it avoids the ~17% long-context accuracy drop of approximate replay. Relevance: 95 (abstract-based).

[Aggron: Aggressive Compression of Agentic KV Caches during Head-of-Line Stalls](https://arxiv.org/abs/2611.26435)
Instead of waiting for the KV cache to cross a threshold and summarizing huge spans, Aggron summarizes agentic requests every turn, selectively, and fires those summarization jobs from a separate queue that scavenges the compute/memory freed by head-of-line stalls — only when it predicts they'll finish before the stalled request resumes. At high load: 27–31% lower P99 program latency and 1.34–1.40× throughput over SOTA async summarization. Relevance: 95 (abstract-based).

[TripleKV: Predict, Prefetch, Protect — KV Cache Management for AI Agents](https://arxiv.org/abs/2611.25112)
A three-tier (GPU/DRAM/SSD) KV manager that exploits the fact that an agent's next KV blocks are known in advance — a tool-aware latency predictor prefetches them SSD→DRAM during tool execution, with dedup and a victim cache to stretch DRAM. Cuts critical-path SSD reads from 45–76% to under 10%, drops P95 TTFT up to 49% vs a DRAM/SSD-tiered vLLM, and 1.5–7× lower P95 TTFT than recent agent-aware systems. Relevance: 92 (abstract-based).

[AscMLA: Unlocking FP4 Efficiency for Long-Context MLA Decoding through Asymmetric Scaling](https://arxiv.org/abs/2611.26106)
Applying FP4 to multi-head latent attention is hard because K and V need different scaling on a shared latent; AscMLA uses asymmetric K/V scaling plus pipelined scale delivery to process a single FP4 payload directly, no dequant detour. 38.2% less cache memory than FP8, with 1.35× geomean speedup over TRT-LLM's FP8 and 1.26× over CAKE's NVFP4 MLA kernels. Relevance: 93 (abstract-based).
```

Tell me which unblock option you want (or just install poppler and re-run) and I'll produce the real full-text bulletin.

---

## Surge Watch

**FlashAttention-4 and Mamba-3 break out on the same day.** Both marquee March-2026 papers sat flat for a month, then jumped Nov 14: [FlashAttention-4](https://arxiv.org/abs/2603.05451) ran 77→120 citations with influential cites doubling (11→22), and [Mamba-3](https://arxiv.org/abs/2603.15569) went 105→140 (influential 18→27). Foundational kernel/architecture work is compounding now — not just this autumn's speculative-decoding cohort.

**DeepSeek-V4.1-Flash is pulling away.** The KV-cache-compression flagship [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) climbed 191→234 citations in under two weeks and is still rising — the highest count of any recent paper on the board.

**First-traction alert:** [Multi-Branch Transformer](https://arxiv.org/abs/2611.19800) leapt 17→44 HF upvotes and 3→13 stars in two days — real heat in a cycle where HF counts have mostly gone flat or backward.

**The curve held:** [Evolving Infra](https://arxiv.org/abs/2611.12304) kept running after last week's bookmark — 106→162 GitHub stars in two more days. Agent-adaptive serving has legs.
