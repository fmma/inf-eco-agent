Now I have all 8 PDFs read. Here are my rescored assessments and the bulletin.

**Rescored relevance (full-text based):**

| Paper | Initial | Rescored | Notes |
|---|---|---|---|
| Tutti (2605.03375) | 88 | 92 | GPU-centric SSD KV cache, vLLM integration, strong H100 results |
| OServe (2602.12151) | 85 | 90 | ICML 2026, spatial-temporal heterogeneous serving, 2x improvement |
| Kairos (2605.02329) | 90 | 93 | PD-disaggregated SLO scheduling, 229B MoE on H200, production-grade |
| Coral (2605.04357) | 82 | 88 | Multi-LLM ILP placement on heterogeneous GPUs, CMU/Princeton |
| ContextPilot (2511.03475) | 86 | 89 | MLSys 2026, context reuse for long-context prefill, DeepSeek-R1 |
| eLLM (2506.15155) | 78 | 80 | Virtual tensor abstraction unifying activation/KV memory, DAC 2026, solid but narrower scope |
| Nitsum (2605.05467) | 80 | 87 | Adaptive TP as runtime control surface for tiered SLOs, up to 5.3x goodput, UCSD |
| TokenStack (2605.05639) | 75 | 68 | HBM-PIM architecture paper, simulation-only, hardware proposal — less directly applicable |

**Top 5 selected** (rescored >= 70, ranked): Kairos (93), Tutti (92), OServe (90), ContextPilot (89), Coral (88). Nitsum (87) makes it 6 — I'll include the top 5.

# Inference Ecosystem — Flash News

**1000 papers scanned, 20 shortlisted, 8 read in full.**

---

### [Kairos: SLO-Aware Scheduling for Disaggregated LLM Serving](https://arxiv.org/abs/2605.02329)

Kairos tackles SLO violations in prefill-decode disaggregated architectures with two mechanisms: urgency-based priority scheduling on the prefill side to eliminate head-of-line blocking, and slack-guided adaptive decode batching that exploits the gap between per-step latency and TPOT SLO targets. Evaluated on MiniMax-M2.5 (229B MoE) across 8x H200 GPUs, it improves TTFT SLO attainment by 23.9%, TPOT SLO by 27.1%, and end-to-end SLO by 33.8% over DistServe. Decode throughput rises 19.3% by dynamically growing batch sizes when slack permits.
Score: 93 (was 90)

### [Tutti: GPU-Centric SSD-Backed KV Cache for LLM Serving](https://arxiv.org/abs/2605.03375)

Tutti introduces a GPU-native object abstraction for SSD-backed KV cache, bypassing the CPU entirely with GPU io_uring for asynchronous direct I/O and slack-aware I/O scheduling that hides SSD latency within decode step budgets. Integrated into vLLM and evaluated on H100 GPUs with Solidigm D7 SSDs running Llama3-8B and GLM-4-9B-1M, Tutti cuts TTFT by 78.3% versus GDS-enabled LMCache, doubles sustainable request rate, and reduces serving cost by 27%.
Score: 92 (was 88)

### [OServe: Spatial-Temporal Workload Orchestration for LLM Serving](https://arxiv.org/abs/2602.12151)

Accepted at ICML 2026, OServe addresses both spatial heterogeneity (different request patterns across model replicas) and temporal heterogeneity (load shifts over time) via a two-level scheduling framework: a flow-network formulation for workload assignment and flow-guided generation for flexible model deployment across GPUs. An LSTM predictor triggers temporal reconfigurations. On OPT-66B and Llama2-70B with 8–32 GPUs, OServe achieves up to 2x improvement in P99 latency and throughput over vLLM.
Score: 90 (was 85)

### [ContextPilot: Context Reuse for Long-Context Prefill Acceleration](https://arxiv.org/abs/2511.03475)

Published at MLSys 2026, ContextPilot accelerates long-context prefill through three complementary mechanisms: hierarchical clustering for context indexing, prefix-cache-aware context alignment, and multi-turn overlap deduplication. It achieves up to 3x prefill speedup, works across scales from edge devices to DeepSeek-R1 (671B), and is open-sourced. The system is orthogonal to attention kernel optimizations and composable with existing serving stacks.
Score: 89 (was 86)

### [Coral: Multi-LLM Serving on Heterogeneous Cloud GPUs](https://arxiv.org/abs/2605.04357)

From CMU and Princeton, Coral jointly optimizes resource allocation and model placement when serving multiple LLMs on heterogeneous GPU types. A two-stage design uses offline ILP to generate Serving Templates (model-to-GPU-type mappings) and online ILP for resource allocation under shifting demand. Evaluated across 6 models, 5 GPU types, and 20 configurations, Coral delivers up to 2.79x cost reduction over baselines and 2.39x higher goodput under scarce resources, with online solve times in tens of seconds.
Score: 88 (was 82)

---

## Surge Watch

Nothing noteworthy in signal trends today.
