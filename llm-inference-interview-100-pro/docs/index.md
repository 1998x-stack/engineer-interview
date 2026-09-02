# LLM 部署与推理优化面试 100 题

这是一份问题驱动的 LLM Inference / Serving 面试手册。目标不是记住框架参数，而是建立可估算、可诊断、可验证的系统思维。

## 章节

- [01 推理性能基本原理](chapters/01-performance-fundamentals/index.md) - 建立统一成本模型：先区分 Prefill/Decode，再用 Roofline、排队与 SLO 判断关键路径。
- [02 KV Cache 与 Attention](chapters/02-kv-cache-attention/index.md) - 把 KV Cache 当作动态内存系统，而不仅是 Transformer 中间张量。
- [03 Batching 与 Scheduling](chapters/03-batching-scheduling/index.md) - 把 scheduler 看作受 KV、token budget 与 SLO 约束的在线资源分配器。
- [04 CUDA、Attention Kernel 与 Runtime](chapters/04-kernel-runtime/index.md) - 从“GPU 很忙”深入到 IO、tile、launch、shape 与 kernel critical path。
- [05 量化与低精度推理](chapters/05-quantization/index.md) - 同时优化精度、内存、带宽和硬件 kernel，而不是把 bit-width 当成性能答案。
- [06 分布式推理与通信](chapters/06-distributed-inference/index.md) - 从模型切分上升到拓扑感知的通信成本模型。
- [07 Speculative Decoding](chapters/07-speculative-decoding/index.md) - 用“proposal 成本 + verification 成本 + acceptance”而不是宣传 speedup 判断价值。
- [08 MoE、MLA 与模型-系统协同](chapters/08-moe-mla-codesign/index.md) - 理解现代模型结构如何重写 KV、GEMM、routing 与通信的性能模型。
- [09 vLLM / SGLang / TensorRT-LLM](chapters/09-serving-runtimes/index.md) - 把框架理解为 scheduler + cache manager + executor + kernels + distributed runtime 的组合。
- [10 Benchmark、生产部署与系统设计](chapters/10-production-system-design/index.md) - 把所有局部优化放到 SLO、容量、成本、可观测性与故障证据链中。

## 使用建议

- 面试前：先看 [Top 20](top20.md) 和 [公式速查](formula-cheatsheet.md)。
- 深挖：按章节逐题阅读并完成建议实验。
- 系统设计：阅读 [Benchmark Playbook](benchmark-playbook.md) 与 [框架选型矩阵](framework-matrix.md)。

> 原始成书版位于 [`assets/pdf/`](../assets/pdf/LLM_Inference_Interview_100_2026.pdf)。
