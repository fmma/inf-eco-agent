All 8 PDFs read in full. Rescoring on actual contribution and writing the bulletin.

# Inference Ecosystem — Flash News
**2026-07-21 · 269 papers scanned · 5 make the cut**

A strong week for MoE serving and KV-cache economics. The standout is a serving architecture that finally decouples the prefill/decode resource ratio from MoE weight size — plus practical wins in tiered KV storage, non-prefix reuse, MX quantization, and a sharp cautionary result on sparse attention.

## [ExpertPlex: A High-Goodput Disaggregated Serving System for MoE LLMs with Adaptive Persistent Kernels](https://arxiv.org/abs/2607.18002)
Xin Jin's group (PKU) shares massive MoE experts across prefill and decode while disaggregating the lightweight attention modules — killing >95% of duplicate weights and letting either phase fill the other's bubbles. The real advance is the Adaptive Persistent Kernel: tile-level bounded preemption (<25.3µs, GEMM intervals <10.7µs) that reallocates SMs on-GPU with no CPU intervention or kernel relaunch, preserving CUDA Graph compatibility. It adds just 8% to decode latency and slows prefill only 1.12× (vs 4.07× for Green Context, 13.79× for CUDA streams). Goodput up to 2.01× over instance-level PD-disaggregation and 1.66× over colocation, serving MiniMax-M2.7 and GLM-5.1-FP8 on H800. If you serve MoE, read this first. **Score: 96 (was 97)**

## [HyMCache: A KV Cache Framework for Multi-Turn LLM Serving with CXL-Hybrid Memory](https://arxiv.org/abs/2607.18141)
A real FPGA CXL-HM prototype (small in-device DRAM behind TB-scale SSD) turned into a KV tier by exploiting the read-dominant, append-only nature of multi-turn context. Instead of LRU, it uses request-level prefix prefetching + opportunistic write buffering to keep latency-critical reads on the fast DRAM path. Result: 3.0× over local LMCache single-node, and within 30% of 1TB distributed-DRAM Mooncake while using **16× less DRAM** (~$11K vs $30–40K per node). The clearest economic answer yet to TB-scale context caching. **Score: 91 (was 96)**

## [C²KV: Compressed and Composable KV Cache Reuse for Efficient LLM Inference](https://arxiv.org/abs/2607.17715)
Non-prefix KV reuse that finally addresses storage/bandwidth, not just recompute. A frozen-model sidecar Extractor with learnable compression tokens and a block-local "Structured Information Flow" learns a position-agnostic, 4×-compressed KV manifold you can concatenate at arbitrary positions — turning TTFT into a load-only op (no blending). Up to 17× speedup on long contexts, beating CacheBlend/EPIC/Block-Attention on both accuracy and latency, with public code. Directly deployable for RAG. **Score: 89 (was 90)**

## [MXSens: Sensitivity-Aware Mixed-Precision Quantization for Efficient LLM Inference](https://arxiv.org/abs/2607.17733)
Since rotation-based methods break MXINT's block structure, MXSens instead allocates precision: Hessian-guided 4/6/8-bit mantissas, with the 32 most sensitive columns (matching the MX block) pinned to 8-bit. Training-free, W4A4KV4 perplexity of 3.77 (LLaMA-2-70B) and 7.63 (LLaMA-3-8B), beating QuaRot/RRS/Atom/QUIK at ~3% latency overhead. Timely as MX-native hardware (Blackwell, Qualcomm AI100) ships. **Score: 87 (was 88)**

## [Lil: Less is Less When Applying Post-Training Sparse-Attention Algorithms in Long-Decode Stage](https://arxiv.org/abs/2601.03043)
The uncomfortable result: post-training sparse attention (H2O, Quest, InfLLM, StreamingLLM) can *increase* end-to-end latency on reasoning tasks — information loss inflates output length up to 90%, negating the per-step savings. Their Guardian early-stop (using LZ77 compression ratio as an information-gain proxy) cuts token consumption up to 90% with <2% accuracy drop. Essential reading before you ship sparse decode. **Score: 86 (was 88)**

*Also strong but below the cut: Talaria (session-aware serverless, 83 — headline speedup is vs an internal all-off baseline on a single server) and "Lossless but Not Free" (76 — a careful but narrow consumer-hardware speculative-decoding study).*

---

## Surge Watch

[Hierarchical Sparse Attention Done Right](https://arxiv.org/abs/2607.02980) is the breakout of the week: since landing ~July 10 it's gone 55 → 79 HF upvotes and nearly tripled GitHub stars (41 → 113). Infinite-context sparse attention is clearly hitting a nerve.

[Unlimited OCR Works](https://arxiv.org/abs/2606.23050) keeps compounding — roughly +1,700 GitHub stars in two weeks (13.6k → 15.4k) plus HF upvotes creeping 51 → 55. The optical-compression OCR wave shows no sign of cooling.

On the academic side, [DFlash](https://arxiv.org/abs/2602.06036) (block-diffusion speculative decoding) is the citation magnet: 42 → 50 citations and 17 → 21 influential ones this month, now past 5.4k stars. Diffusion drafting is becoming a citation staple.

Otherwise it's plateaus — MiniMax Sparse Attention has flattened near 153 HF upvotes, and the big model repos (Fish Audio, Qwen3-Coder) are adding stars at a mature, unremarkable clip.
