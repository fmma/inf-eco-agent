# Inference Ecosystem — Flash News
**2026-04-16 | 426 papers scanned**

### [Event Tensor: A Unified Abstraction for Compiling Dynamic Megakernel](https://arxiv.org/abs/2604.13327v1)

CMU and NVIDIA introduce Event Tensor Compiler (ETC), a compiler abstraction that fuses entire LLM decoding pipelines — attention, RoPE, KV-cache, MLP, MoE — into a single persistent megakernel. On B200 GPUs, ETC beats vLLM by 1.48x and SGLang by 1.20x at batch-1 on Qwen3-30B-A3B, while cutting engine warmup from 583s (SGLang) to 35s via true ahead-of-time compilation that eliminates CUDA Graph recapture entirely. The MoE megakernel outperforms FlashInfer by 1.23x through on-GPU dynamic scheduling of data-dependent expert routing — something no prior megakernel could handle. Already merged into a major open-source system. This is the new bar for low-batch serving latency.
Score: 97 (was 95)

### [ToolSpec: Accelerating Tool Calling via Schema-Aware and Retrieval-Augmented Speculative Decoding](https://arxiv.org/abs/2604.13519v1)

ToolSpec observes that tool-call generation — not tool execution — is the latency bottleneck (80-96% of end-to-end time at scale). It uses a finite-state machine to deterministically fill schema tokens (JSON keys, tool names, parameter names) while speculatively decoding only variable fields, plus retrieves similar historical tool calls as draft candidates. The result: 3.5-4.2x speedup across Qwen2.5, LLaMA-3.1, and ToolLLaMA, with 61% relative improvement over the best training-free speculative decoding baseline. Training-free, plug-and-play, and increasingly relevant as agentic multi-tool workflows scale.
Score: 90 (was 93)

### [KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs](https://arxiv.org/abs/2604.13226v1)

KV Packet wraps each document's precomputed KV cache in lightweight trainable Header/Trailer soft-token adapters (just 8 tokens each), enabling zero-recomputation cache concatenation for RAG. The adapters absorb attention-sink boundary artifacts that cause naive concatenation to fail. On Llama-3.1-8B, TTFT drops 19.45x on Needle-in-a-Haystack and inference FLOPs fall 5-6 orders of magnitude versus CacheBlend/EPIC, while F1 stays competitive with full recomputation. Universal adapters trained on mixed domains generalize across tasks — a practical drop-in for any RAG serving stack running repeat-document workloads.
Score: 88 (was 95)

### [DASH-Q: Robust Ultra Low-Bit Post-Training Quantization via Stable Diagonal Curvature Estimate](https://arxiv.org/abs/2604.13806v1)

DASH-Q makes an elegant argument: at 2-bit precision, off-diagonal Hessian entries are pure noise from limited calibration data, so GPTQ-style cross-channel compensation overfits. By discarding off-diagonal terms entirely and solving independent weighted least-squares per channel, DASH-Q improves 2-bit zero-shot accuracy by 7% average (up to 14%) over the strongest PTQ baseline across Llama-3.1-8B, Qwen3-14B, DeepSeek-MoE-16B, Phi-3.5-MoE, and Mixtral-8x7B — while quantizing 74.5x faster. Stable even with just 2 calibration samples. Deploys on standard inference engines with no custom kernels.
Score: 85 (was 88)

### [YOCO++: Enhancing YOCO with KV Residual Connections for Efficient LLM Inference](https://arxiv.org/abs/2604.13556v1)

YOCO++ adds weighted KV residual connections from layer 1 to each bottom-half layer in the YOCO decoder-decoder architecture, enriching the shared global KV cache at zero additional decoding I/O cost. With a learnable scaling factor (lambda=35) to stabilize training, it achieves SOTA among cross-layer KV compression methods at 50% cache compression — outperforming the standard Transformer on commonsense benchmarks at 1.1B scale. Prefilling latency halves and decoding throughput jumps, unlike FusedKV which regresses on throughput due to extra I/O.
Score: 80 (was 90)

---

## Surge Watch

[Attention Sink in Transformers](https://arxiv.org/abs/2604.10098v1) refuses to plateau — 58 → 69 HF upvotes and 34 → 47 GitHub stars in the latest 24 hours. Three-day arc of 26 → 69 upvotes makes this the fastest-moving survey paper we've tracked. Clearly tapped a nerve.

[Introspective Diffusion Language Models](https://arxiv.org/abs/2604.11035v1) is accelerating, not cooling — GitHub stars surged 69 → 94 overnight (HF 15 → 19). The builder-first pattern is intensifying as diffusion LLMs compete for the non-autoregressive slot.

[Nemotron 3 Super](https://arxiv.org/abs/2604.12374v1) is the fresh entry — NVIDIA's MoE Mamba-Transformer hybrid leapt from 4 → 21 HF upvotes in a single day. The Mamba-meets-MoE-for-agentic-reasoning pitch is resonating; first-day signal strength mirrors TriAttention's early trajectory.

TriAttention has now fully settled (107 HF / 534 stars, +2/+30 over 2 days). First citation appeared, marking the transition from community buzz to academic uptake.
