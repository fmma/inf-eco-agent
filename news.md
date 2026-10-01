I hit a wall that's worth surfacing before I produce anything, because the output would otherwise misrepresent what I actually did.

**I can't read the PDFs in this environment.** The Read tool renders PDF pages to images via `pdftoppm` (poppler-utils), which isn't installed on this host:

```
pdftoppm is not installed. Install poppler-utils ... to enable PDF page rendering.
```

My fallback — extracting text with Python (`pymupdf`/`pypdf`) via Bash — is also blocked: every Bash call here returns "requires approval" and isn't being granted (consistent with the `--allowedTools "Read"` invocation the news step uses). So I have no working path to the full text of the 8 PDFs. Reporting that honestly rather than fabricating a full-text rescore.

**Two ways forward:**

1. **Quick fix (this host):** `sudo apt-get install poppler-utils`, then re-run — Read will work.
2. **Robust fix (recommended):** decouple `generate_news.py` from the Read tool's image rendering. Extract text server-side with `pymupdf`/`pypdf` and either inline it into the prompt or write `.txt` siblings for Claude to `Read`. This removes the poppler system dependency entirely and still works under `--allowedTools "Read"`. It also sidesteps the cost/fragility of image-rendering every PDF page.

If you'd rather I just do it now: **approve one Bash call** and I'll extract the text with Python and produce a genuine full-text rescore.

---

Meanwhile, so you're not blocked, here's a bulletin built **from the abstracts only** (they already carry the key numbers). I've kept the scores at their abstract-based values rather than faking a `(was X)` full-text delta:

```markdown
# Inference Ecosystem — Flash News
**2026-10-01 · 543 papers scanned · 5 picks**

[Working Around the Compute Ceiling: Byte-Exact Memory in Galahad](https://arxiv.org/abs/2609.39358)
A memory layer for vLLM, SGLang and llama.cpp that turns document "reading" into a one-time cost: it saves byte-exact KV state per text block and reloads it on any later request containing the same bytes, then serves the model only the section a question needs. On a 100-fact/97K-token recall test (Gemma 4 31B), it reports 98/100 at 3.0s & 572J vs 10/100, 9.3s & 2,754J without — 100/100 at ~0.6s with section routing — and bit-identical restored logits, failing closed on any check miss. Stateful serving across all three major runtimes is a big deal; bold single-author claims, so verify before betting on it. Score: 95

[Vosti: Specifying, Implementing, and Verifying Deterministic LLM Inference](https://arxiv.org/abs/2609.38981)
First formal system-level spec of deterministic inference plus an engine verified against it — and it shows vLLM's batch-invariant and SGLang's deterministic modes still diverge under some execution variations. Vosti selects kernels independently of runtime state, ties KV to logical token prefixes, and splits its proof across engine (Verus) and kernel (Triton analyzer) for bitwise-identical logits at perf comparable to vLLM batch-invariant on decode-heavy loads. The determinism topic is white-hot post-Thinking-Machines, and "verified" raises the bar. Score: 95

[SparseEngine: Sparse-First Inference Engine](https://arxiv.org/abs/2609.39068)
A ground-up sparse-first serving engine whose shared lifecycle contract lets 15 sparse-attention methods each control their own KV layout; Chain Cache resumes KV-eviction from retained history and Prefix-Cache Pruning drops selected regions while preserving prefix matching. Reports >10x throughput with KV eviction, >2.5x decode at matched concurrency vs vLLM, and >2x end-to-end on agent benchmarks — open source. If it holds, it's a serious option for long-context agent serving. Score: 95

[Efficient Expert-Parallel Communication on PCIe-Connected Consumer GPUs](https://arxiv.org/abs/2609.40093)
ThunderEP rethinks MoE expert-parallel comms for PCIe consumer boxes: it removes the relay hops of ring all-to-all, moves data through DMA engines to dodge compute contention, and cuts completion-flag polling overhead. Integrated into vLLM, it hits 2.00x/1.53x over NCCL for dispatch/combine and up to 1.66x end-to-end on RTX 4090/5090 systems. Directly actionable for anyone serving MoE models without NVLink. Score: 94

[UBTree: Parallel Tree Drafting via Unigram and Bigram Models for Speculative Decoding](https://arxiv.org/abs/2609.39972)
Pairs a unigram proposer with a bigram selector (trained with a renormalized KL objective on high-temp data) so tree drafts stay diverse even under high-entropy targets. Reports 5.84–6.94x over autoregressive decoding on Qwen3-4B/8B across 7 benchmarks, beats DARTree in all 28 comparisons, and tops the frontier production baseline DSpark. Spec decoding remains the highest-leverage latency win, and the production eval is the selling point. Score: 93
```

Want me to go the Bash route for a real full-text rescore, or are you set with the abstract-based draft?

---

## Surge Watch

[Fast KV Compaction via Attention Matching](https://arxiv.org/abs/2602.16284) is the clearest new mover: after sitting flat at ~17 citations for a month, it broke out to **17→23 with a sharp 20→23 burst across 09-30→10-01, and influential citations doubling 4→8** in the same two days — a sudden, concentrated pickup for a KV-compaction method that had shown no prior momentum.

[REAP the Experts](https://arxiv.org/abs/2510.13999) keeps compounding on the MoE-pruning side: **40→47 citations (09-23→10-01) with influentials climbing 16→20** — a notably high influential ratio and a steeper, still-accelerating ramp than most of its one-shot-compression peers.

Last cycle's sprinters have settled: [DeepSeek-V4.1-Flash](https://arxiv.org/abs/2609.19969) held at 23 citations (09-30) with no fresh jump, and [Continuum](https://arxiv.org/abs/2511.02230) edged just 63→64 into 10-01 — both cooling from the fast climbs flagged last week rather than extending them.
