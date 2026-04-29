Now let me rescore and write the bulletin based on all PDFs read.

**Rescoring notes:**
- CacheFlow: Strong systems paper, practical TTFT improvements on real workloads, implemented atop vLLM/LMCache. Score up to 96.
- Pythia: Comprehensive agent-native serving system from UCLA/Alibaba with production traces, up to 2.9x JCT reduction. Score up to 95.
- Scaling Multi-Node MoE (no PDF but abstract is detailed): Up to 20x all-to-all reduction. Keep 95.
- SAW-INT4 (no PDF but co-authored by Tri Dao): Keep 95.
- Salca: Impressive ASIC accelerator for long-context decoding, 3.82x speedup over A100, first to target 64K contexts. Score stays 90 — academic hardware, no production path.
- NVLLM, AHASD, FusionCIM, PolyKV: Hardware research papers, interesting but niche. Scores 70-80 range.
- Scalable Inference (Salesforce): Production deployment study, good operational lessons but incremental. Score down to 82.

Top 5 selected: CacheFlow (96), Pythia (95), MoE Scaling (95), SAW-INT4 (95), Salca (90).

# Inference Ecosystem — Flash News
**2026-04-29 | 496 papers scanned**

### [CacheFlow: Efficient LLM Serving with 3D-Parallel KV Cache Restoration](https://arxiv.org/abs/2604.25080v1)

KV cache restoration is the new TTFT killer for long-context workloads, and CacheFlow treats it as a multi-dimensional scheduling problem. It introduces a two-pointer strategy that overlaps recomputation (forward from chunk 0) with I/O loading (backward from the last chunk) across tokens, layers, and GPUs simultaneously, hitting the harmonic-mean optimum of compute and I/O. Evaluated on Qwen3-8B, Qwen3-30B-A3B, and Llama-3.1-8B atop vLLM+LMCache, it cuts TTFT by 10–62% over baselines including SGLang and Cake, with 88% GPU + 78% I/O utilization during restoration. This is the paper to read if you run multi-turn chatbots, RAG, or agentic pipelines on long contexts.
Score: 96 (was 95)

### [Pythia: Toward Predictability-Driven Agent-Native LLM Serving](https://arxiv.org/abs/2604.25899v1)

Pythia argues that multi-agent workflows are predictable programs, not random traffic — and builds a serving system to exploit that. Built on SGLang, it synthesizes workflow graphs from traces into regular expressions, then uses them for Belady-like speculative cache management (25.5x TTFT reduction for recurring agents), graph-driven priority scheduling, and phase-adaptive autoscaling that pre-provisions replicas before fan-out bursts hit. On an 8xA100 cluster with coding assistant and deep-research workloads, Pythia delivers up to 2.9x JCT reduction and 1.96x throughput over vLLM, SGLang, and Autellix. A strong signal that agent-native serving is the next systems frontier.
Score: 95 (was 92)

### [Scaling Multi-Node MoE Inference Using Expert Activation Patterns](https://arxiv.org/abs/2604.23150v1)

Georgia Tech + Meta profile 100K+ expert activation traces from Llama 4 Maverick, DeepSeek V3-671B, and Qwen3-230B, revealing that expert load is persistently imbalanced and domain-specific (code vs. math vs. chat). They propose workload-aware micro-batch grouping and expert placement that maximizes token locality, cutting inter-node all-to-all communication by up to 20x. The finding that prefill expert activations strongly predict decode patterns is directly actionable for anyone deploying MoE models across nodes.
Score: 95 (was 95)

### [SAW-INT4: System-Aware 4-Bit KV-Cache Quantization for Real-World LLM Serving](https://arxiv.org/abs/2604.19157v1)

Co-authored by Tri Dao, this paper identifies the minimal viable KV-cache quantization under real serving constraints (paged layouts, fused attention, no dequantize-requantize overhead). The winner: token-wise INT4 with block-diagonal Hadamard rotation. Their fused rotation-quantization kernel introduces zero measurable end-to-end overhead, matching plain INT4 throughput while recovering nearly all accuracy lost by naive quantization. A pragmatic systems co-design result that should become the default KV-cache compression baseline.
Score: 93 (was 95)

### [Salca: A Sparsity-Aware Hardware Accelerator for Efficient Long-Context Attention Decoding](https://arxiv.org/abs/2604.24820v1)

The first ASIC accelerator purpose-built for long-context (up to 64K) attention decoding. Salca combines dual-compression sparse attention (2-bit asymmetric keys + 3-bit symmetric queries + heavy-channel feature pruning = 8x data reduction over 4-bit baselines) with an O(n) approximate histogram-based Top-K filter. The five-stage pipelined architecture with HBM conflict elimination delivers 3.82x speedup and 74.19x energy efficiency over A100, with at least 3.5x throughput over prior sparse attention accelerators. Academic hardware without a production path, but it maps out where custom silicon for long-context inference needs to go.
Score: 90 (was 95)

---

## Surge Watch

[Act While Thinking](https://arxiv.org/abs/2603.18897) woke up after two months of absolute silence: 0→3 citations (2 influential) in the last 8 days. A paper about speculatively executing tools while the LLM is still generating — the pattern-aware approach to parallelizing agent tool calls is now being picked up as foundational reference in new agentic inference work.

Otherwise, the landscape is quiet. Previous surges (TriAttention, IceCache, Block Diffusion Draft Trees) have all stabilized as expected. Most papers tracked this week show flat or single-digit incremental growth across all signals.
