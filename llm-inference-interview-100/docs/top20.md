# Top 20 高频优先题

如果只有 3 天，先吃透这些题。要求不是背答案，而是每题能连续回答 3 个追问。

- [Q001 为什么 LLM 的 Prefill 和 Decode 是两种完全不同的计算？](chapters/01-performance-fundamentals/q001-prefill-decode-roofline.md) - `prefill, decode, roofline`
- [Q003 为什么 batch=1 的 Decode 经常是 Memory Bound？](chapters/01-performance-fundamentals/q003-decode-memory-bandwidth.md) - `decode, memory-bandwidth`
- [Q004 什么是 Roofline Model？如何用于分析 LLM inference？](chapters/01-performance-fundamentals/q004-roofline-profiling.md) - `roofline, profiling`
- [Q005 如何估算一个模型 Decode 的理论 token/s？](chapters/01-performance-fundamentals/q005-estimation-bandwidth.md) - `estimation, bandwidth`
- [Q011 KV Cache 显存怎么计算？](chapters/02-kv-cache-attention/q011-kv-cache-memory.md) - `KV-cache, memory`
- [Q013 PagedAttention 到底解决了什么？](chapters/02-kv-cache-attention/q013-pagedattention-kv.md) - `PagedAttention, KV`
- [Q016 Prefix Caching 为什么有时收益巨大，有时几乎没用？](chapters/02-kv-cache-attention/q016-prefix-cache-cache.md) - `prefix-cache, cache`
- [Q021 Static Batching 和 Continuous Batching 有什么区别？](chapters/03-batching-scheduling/q021-continuous-batching-scheduler.md) - `continuous-batching, scheduler`
- [Q024 Chunked Prefill 为什么能解决这个问题？](chapters/03-batching-scheduling/q024-chunked-prefill-sarathi.md) - `chunked-prefill, Sarathi`
- [Q030 什么是 Prefill–Decode Disaggregation？](chapters/03-batching-scheduling/q030-pd-disaggregation-distserve.md) - `PD-disaggregation, DistServe`
- [Q031 FlashAttention 为什么更快？](chapters/04-kernel-runtime/q031-flashattention-io.md) - `FlashAttention, IO`
- [Q041 Weight-only Quantization 与 W8A8 有什么区别？](chapters/05-quantization/q041-quantization-w4a16-w8a8.md) - `quantization, W4A16, W8A8`
- [Q050 为什么 INT4 模型有时候不比 FP16 快？](chapters/05-quantization/q050-int4-performance.md) - `INT4, performance`
- [Q051 Tensor Parallelism 是什么？](chapters/06-distributed-inference/q051-tp-distributed.md) - `TP, distributed`
- [Q054 Expert Parallelism 是什么？](chapters/06-distributed-inference/q054-ep-moe.md) - `EP, MoE`
- [Q061 Speculative Decoding 的基本原理是什么？](chapters/07-speculative-decoding/q061-speculative-decoding-draft.md) - `speculative-decoding, draft`
- [Q071 为什么 MoE 理论 FLOPs 很低，线上 latency 却未必低？](chapters/08-moe-mla-codesign/q071-moe-latency.md) - `MoE, latency`
- [Q081 请描述 vLLM 的核心架构思想。](chapters/09-serving-runtimes/q081-vllm-architecture.md) - `vLLM, architecture`
- [Q099 系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？](chapters/10-production-system-design/q099-system-design-h100-70b.md) - `system-design, H100, 70B`
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](chapters/10-production-system-design/q100-debugging-production-systematic.md) - `debugging, production, systematic`
