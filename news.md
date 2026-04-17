# Inference Ecosystem — Flash News
**2026-04-17 | 476 papers scanned**

## [Prefill-as-a-Service: KVCache of Next-Generation Models Could Go Cross-Datacenter](https://arxiv.org/abs/2604.15039v1)

Moonshot AI and Tsinghua introduce PrfaaS, a cross-datacenter serving architecture that selectively offloads long-context prefills to remote compute-dense clusters and ships the resulting KVCache over commodity Ethernet. The key enabler: hybrid-attention models (Kimi Linear, MiMo-V2-Flash, Qwen3.5-397B) slash KV throughput by 4-36x vs. dense models, making inter-cluster transfer feasible. On a 1T-parameter hybrid model, PrfaaS achieves 54% higher throughput and 64% lower P90 TTFT than homogeneous PD baselines, consuming only 13 Gbps of Ethernet — 13% of a 100G link. This paper redraws the deployment boundary of PD disaggregation from single-RDMA-cluster to multi-datacenter, with bandwidth-aware scheduling and a hybrid prefix cache pool built on vLLM.
Score: 96 (was 95)

## [Scepsy: Serving Agentic Workflows Using Aggregate LLM Pipelines](https://arxiv.org/abs/2604.15186v1)

Imperial College's Scepsy tackles a growing blind spot: how to efficiently schedule multi-LLM agentic workflows (beam search, RAG+reranker) onto GPU clusters. The core insight is that while individual workflow executions are wildly unpredictable, the *relative* time each LLM consumes is stable — enabling an "Aggregate LLM Pipeline" abstraction that predicts throughput/latency from per-LLM profiles. Scepsy jointly optimizes fractional GPU shares, tensor parallelism, and replica counts via topology-aware placement on Kubernetes with Nvidia MPS. On a 16-GPU cluster: 2.4x higher throughput and 27x lower latency than Kubernetes autoscaling or Aegaeon. As agentic inference becomes the default deployment pattern, this is the scheduling paper the ecosystem needs.
Score: 90 (was 92)

## [RACER: Retrieval-Augmented Contextual Rapid Speculative Decoding](https://arxiv.org/abs/2604.14885v1)

RACER unifies retrieval-based and logits-based drafting for training-free speculative decoding. An Aho-Corasick automaton with LRU eviction captures repeated n-gram patterns from context, while a "copy-logit" strategy reuses logits from prior occurrences of the same token to build a pruned draft tree. The two are merged into a single speculation budget per step. Across Vicuna, LLaMA-3.1, and Qwen3 (up to 32B), RACER consistently delivers >2x speedup over autoregressive decoding and outperforms EAGLE-3 on speedup ratio despite lower MAT — because it adds zero model parameters. Plug-and-play, code released, and robust across reasoning, code, and multilingual tasks.
Score: 82 (was 90)

## [MemoSight: Unifying Context Compression and Multi-Token Prediction for Reasoning Acceleration](https://arxiv.org/abs/2604.14889v1)

MemoSight addresses the ballooning KV cache from long Chain-of-Thought reasoning by jointly training context compression ("memory tokens") and multi-token prediction ("foresight tokens") — both implemented purely via special tokens and position ID manipulation, requiring zero architecture changes. Memory tokens compress each reasoning step at a configurable ratio; foresight tokens predict d steps ahead for speculative verification. On Qwen2.5-7B and Llama-3.1-8B across GSM8K, MMLU, GPQA, and BBH: 66% peak KV cache reduction, 1.56x inference speedup, and accuracy that matches or beats uncompressed baselines. The first framework to successfully combine MTP with CoT compression.
Score: 82 (was 85)

---

## Surge Watch

Last week's breakouts are all decelerating. [Attention Sink in Transformers](https://arxiv.org/abs/2604.10098v1) went from +11 HF/day to +3 — sitting at 72 upvotes and 49 stars. [Introspective Diffusion Language Models](https://arxiv.org/abs/2604.11035v1) same story: stars crept 94 → 102, HF barely moved. Initial bursts spent on both.

New name worth watching: [DMax](https://arxiv.org/abs/2604.08302v1) quietly ran up 17 → 50 HF upvotes and 5 → 104 GitHub stars in one week — strong traction for aggressive parallel decoding targeting discrete diffusion LLMs. Growth is now leveling, but alongside the Introspective Diffusion paper it confirms non-autoregressive inference as a real research lane, not a one-off.

[Nemotron 3 Super](https://arxiv.org/abs/2604.12374v1) continued to 26 HF (from 21 yesterday) — sustaining interest but not breaking out further.
