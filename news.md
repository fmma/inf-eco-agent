# Inference Ecosystem — Flash News
**2026-05-21 | 303 papers scanned, 5 selected**

## [NanoCP: Request-Level Dynamic Context Parallelism for Data-Expert Parallel Decoding](https://arxiv.org/abs/2605.21100)

NanoCP decouples MoE communication from KV cache placement by assigning each request its own context-parallel degree — long requests spread attention across multiple DP instances while short ones stay local. An AOT graph engine and a custom routing-based communication backend make this dynamic parallelism compatible with CUDA Graphs and DeepEP's static-shape decode kernels. Evaluated on DeepSeek-V3 and Kimi-K2 across 32 H200 GPUs, NanoCP sustains 1.88--3.27x higher request rates under strict TPOT SLOs and cuts P99 tail latency by up to 2.12x versus vLLM baselines. This is the first system to make per-request CP practical for variable-length MoE decoding — directly relevant to anyone deploying DeepSeek-class models at scale.
Score: 95 (was 95)

## [Understanding and Improving Communication Performance in Multi-node LLM Inference](https://arxiv.org/abs/2511.09557)

NVRAR is a hierarchical all-reduce built on NVSHMEM that replaces NCCL's ring/tree algorithms with recursive doubling tuned for the 128KB--2MB message regime that dominates decode-phase tensor parallelism. It achieves 1.9--3.6x lower latency than NCCL on Slingshot and InfiniBand, translating to a 1.72x end-to-end batch latency reduction on Llama 3.1 405B across multi-node decode workloads. The paper also provides the most thorough public performance study of TP vs. hybrid parallelism at scale (up to 128 GPUs). If you run 405B-class models across nodes, this is immediately actionable — NVRAR is open-sourced and integrates into both YALIS and vLLM.
Score: 95 (was 95)

## [OCTOPUS: Optimized KV Cache via Octahedral Parametrization Under Optimal Squared Error Quantization](https://arxiv.org/abs/2605.21226)

OCTOPUS quantizes the rotated KV cache in coordinate triplets using an octahedral map from computer graphics, splitting each triplet into direction (two scalars on [-1,1]^2) and norm, then applying Lloyd-Max quantizers with a non-uniform (b+1, b-1) bit allocation derived from a Lagrangian optimum. At 2-bit KV, it is the only rotation codec that does not collapse on 128K needle-in-a-haystack recall (0.81 vs. SnapKV 0.42) and retains usable video quality where competitors degrade to noise. A fused Triton kernel reconstructs keys on the fly without materializing the full tensor. The first KV codec validated across text, video, and audio modalities — fills a real gap for anyone pushing sub-4-bit KV budgets.
Score: 93 (was 95)

## [Frontier: Towards Comprehensive and Accurate LLM Inference Simulation](https://arxiv.org/abs/2605.21312)

Frontier is a discrete-event simulator that models co-located, prefill-decode disaggregated (PDD), and attention-FFN disaggregated (AFD) serving with role-specific cluster workers, CUDA Graph padding, speculative decoding, and prefix caching as first-class runtime adapters. On a 16-H800 testbed, it achieves <4% throughput error and reduces end-to-end latency error from 44.9% to 6.4% under co-location and from 51.7% to 2.6% under PDD versus prior simulators. It scales to 1K+ GPUs on commodity CPUs, enabling Pareto-frontier searches across serving architectures, heterogeneous GPU placement, and RL rollout reconfiguration. If you are sizing disaggregated deployments or evaluating MoE parallelism plans without burning GPU-hours, this is the tool.
Score: 90 (was 95)

## [Mix-Quant: Quantized Prefilling, Precise Decoding for Agentic LLMs](https://arxiv.org/abs/2605.20315)

Mix-Quant applies NVFP4 W4A4 quantization exclusively to the compute-bound prefill phase while keeping autoregressive decoding in BF16, exploiting the insight that prefill errors stay local while decode errors snowball across agentic trajectories. On Blackwell GPUs, it delivers up to 3x prefill speedup with negligible accuracy loss across BFCL v4, LongMemEval, and tau^2-bench — whereas uniform FP4 drops Qwen3.5-9B's agentic average from 77.3 to 70.4, Mix-Quant recovers it to 74.7. Naturally pairs with prefill-decode disaggregated serving via NIXL-based KV transfer. A straightforward win for anyone serving agentic workloads on Blackwell hardware where prefill is the bottleneck.
Score: 88 (was 92)

---

## Surge Watch

Nothing noteworthy in signal trends today.
