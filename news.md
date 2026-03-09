# Inference Ecosystem — Flash News
**2026-03-09 | 117 papers scanned**

### [FlashPrefill: Instantaneous Pattern Discovery and Thresholding for Ultra-Fast Long-Context Prefilling](https://arxiv.org/abs/2603.06199v1)

The standout paper this week. FlashPrefill from WeChat/CASIA simultaneously discovers vertical, slash, and block-sparse attention patterns using a block-approximation kernel that avoids explicit attention score materialization, then applies a Max-based Dynamic Thresholding that replaces expensive Top-k/Top-p sorting with a single max-reduction pass. On Qwen3-30B with 256K context, it achieves **27.78x** operator speedup over FlashAttention and **7.22x** end-to-end TTFT speedup in vLLM — and critically, unlike competing methods, it still delivers **1.71x** speedup even at 4K context. Needle-in-a-Haystack accuracy is preserved. Already integrated with vLLM with code available. This is immediately deployable for anyone hitting prefill bottlenecks on long contexts.
Score: 95 (was 90)

### [MoEless: Efficient MoE LLM Serving via Serverless Computing](https://arxiv.org/abs/2603.06350v1)

First serverless MoE serving framework. MoEless decouples experts from MoE models into independent serverless functions, predicts expert load distributions using lightweight layer-aware predictors (fine-tuned replicas of the gate networks), and dynamically scales expert replicas to eliminate stragglers. Tested on Mixtral-8x7B, Phi-3.5-MoE, and Llama-4-Scout on 8x A6000 GPUs with real Azure LLM traces, achieving **43% lower latency** and **84% lower cost** vs. Megatron-LM and EPLB baselines. The speculative load prediction using hidden-state similarity across layers is clever — prediction distance of 3-4 layers gives >90% accuracy. A practical blueprint for elastic MoE deployment.
Score: 90 (was 92)

### [A Persistent-State Dataflow Accelerator for Memory-Bound Linear Attention Decode on FPGA](https://arxiv.org/abs/2603.05931v1)

Makes a compelling case that subquadratic sequence models (GDN, Mamba, etc.) are *more* memory-bound than standard Transformers at decode time — all exhibit arithmetic intensities below 1 FLOP/B. The solution: hold the full 2 MB Gated DeltaNet recurrent state persistently in FPGA BRAM, converting the workload from memory-bound to compute-bound. A fused five-phase pipelined datapath on AMD Alveo U55C achieves **63 µs/token** (4.5x faster than H100 GPU) at **9.96 W** on-chip — that's **60x better energy efficiency**. With Qwen3-Next using 75% GDN layers, this is directly relevant to production hybrid architectures. The architectural insight that on-chip persistence beats HBM bandwidth is the real takeaway.
Score: 92 (was 93)

### [Stem: Rethinking Causal Information Flow in Sparse Attention](https://arxiv.org/abs/2603.06274v1)

A training-free sparse attention framework grounded in a clean theoretical insight: early tokens in causal attention are recursive anchors whose pruning propagates errors across all subsequent layers. Stem's Token Position-Decay allocates higher top-k budgets to initial positions and decays toward sequence end, while its Output-Aware Metric combines QK routing scores with value vector magnitudes (not just attention scores). On Llama-3.1-8B at 128K context, Stem achieves **3.7x prefill speedup** with only 25% compute budget while nearly matching dense accuracy on LongBench. Plug-and-play compatible with DeepSeek-V3.2's DSA and MiniCPM-4.1, further compressing their already-sparse budgets by 15-18%.
Score: 85 (was 82)

### [MoEless Parallelization Strategies for Dense LLM Deployment](https://arxiv.org/abs/2603.05692v1)

Thorough empirical study of TP, PP, and hybrid TP+PP for Llama-3.1-70B/405B inference on AMD MI325x/MI355x GPUs. Key finding: TP8 consistently delivers best latency (1.87x-3.61x faster prefill/decode than TP4), while PP shines for throughput via larger KV cache capacity (2.89x more at PP=4). The simulator achieves >86% accuracy vs. silicon. Useful reference for anyone deploying dense models, though the conclusions (TP for latency, PP for throughput) are expected — the value is in the quantified tradeoffs at scale.
Score: 78 (was 92)

---

## Surge Watch

Nothing noteworthy in signal trends today.
