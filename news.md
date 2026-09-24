# Inference Ecosystem — Flash News

**2026-09-24 · 580 scanned · 5 picks**

Long-context attention, KV provisioning, and reliability dominate this batch — the scarce resource in serving keeps shifting from raw FLOPs toward managed state and ready capacity.

### [Fast Recovery for LLM Serving via Decoupled Device Memory Lifetime in Dynamo](https://arxiv.org/abs/2609.25451)
NVIDIA mines 18 weeks of Dynamo production failures and finds most are *device-preserving*: the engine process dies but GPU-resident weights stay intact. A GPU Memory Service (read-only weight sharing via CUDA VMM) plus parked Shadow Engines cut replica recovery from minutes to under 7s — 13–29× faster than a warm restart — for just 4–8 GiB/GPU, reclaiming an estimated 79% of GPU-hours lost to recovery. Open-source, already in production on vLLM and SGLang: the rare reliability paper you can adopt today. Score: 91 (was 90)

### [Block-Sparse Attention with Semantic-Geometric Decoupled Routing](https://arxiv.org/abs/2609.22884)
SGDR pinpoints why training-free block routers degrade — pooling *post*-RoPE tokens cancels high-frequency positional cues. Shifting semantic pooling to pre-RoPE space and reconstructing geometry from an offline prior yields a closed-form, near-O(1) block score with custom Triton kernels: 5.03× over FlashAttn at 128K (451→90ms) at sub-3.4ms routing overhead, beating MInference and Prism while holding full-attention accuracy. A clean, deployable long-context win. Score: 90 (was 90)

### [The KV Cache Working Set: Online Capacity Planning for LLM Inference Systems](https://arxiv.org/abs/2609.27746)
KVSET answers a question every agentic-serving operator hits: how much prefix-cache storage do you actually need? It applies the classic Mattson stack algorithm (plus a Fenwick tree) to derive the entire capacity-to-hit-rate curve in a single trace pass — no capacity-by-capacity simulation. Validated on production coding-agent traces (GLM-5.2 / SGLang / Mooncake), giving ~1 TiB for 95% coverage and ~5 TiB for 99%, and shipped as the first open-source online KV capacity analyzer. Score: 88 (was 92)

### [Adapting Tree-Structured Speculative Decoding to DeepSeek-V4](https://arxiv.org/abs/2609.24698)
The hard part of tree speculation on DeepSeek-V4 isn't the tree — it's keeping CSA/HCA compressed attention consistent as branches diverge from a shared prefix. Branch-aware verification, scratch-pad state isolation, and accepted-path refresh (all landed in SGLang) push accepted length above matched linear in every setting and add up to ~18.5% throughput. The transferable lesson: verify-side overhead now dominates and grows with compressed/sparse context formats — exactly where models are heading. Score: 87 (was 95)

### [PAGE: Partition-Aware Gated KV-Cache Eviction](https://arxiv.org/abs/2609.22157)
PAGE reframes eviction as an admission decision — *whether* to evict, not just what — from one label-free prefill signal (the early-to-late head-agreement drop). As a wrapper over any SnapKV-style evictor it cuts catastrophic harm 29× (Mistral NIAH-MK3: plain SnapKV's 99%→0% collapse becomes a flat 89%). Refreshingly honest about limits: it's a safety net, not a compressor — realized savings are 1.8–3.4× and fade by batch 16 — but a worthwhile guardrail for retrieval-critical traffic. Score: 81 (was 90)

---

## Surge Watch

Community reception flipped this cycle: after last time's "upvotes stayed flat," HF is where the action is. [Random Attention](https://arxiv.org/abs/2609.03430) (RL-guided KV eviction for reasoning) climbed 161→187 HF upvotes since early September — 170→187 in the last two weeks, the cleanest sustained upvote accrual in the set — with GitHub stars 29→69 alongside.

Diffusion-speculation drew a fresh crowd hit too: [Unlocking Lossless Speedups in LLMs via Discrete Diffusion](https://arxiv.org/abs/2609.04010) spiked from single digits to a ~119 peak (holding ~112) with GitHub stars running 50→88 — the newest entrant to that hot line.

On code adoption, [GSQ](https://arxiv.org/abs/2604.18556) (Gumbel-Softmax low-precision quantization) roughly doubled its GitHub stars, 38→71 since early September (HF 14→19) — the fastest repo accretor here.

Citations cooled versus last cycle — DFlash, DSpark, and FlashAttention-4 keep ticking but nothing re-accelerated. The quiet exception is Kimi's [Attention Residuals](https://arxiv.org/abs/2603.15031), 49→53 citations while HF crept 193→196.
