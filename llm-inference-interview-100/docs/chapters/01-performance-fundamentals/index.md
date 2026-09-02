# 01 推理性能基本原理

建立统一成本模型：先区分 Prefill/Decode，再用 Roofline、排队与 SLO 判断关键路径。

## 本章学习方法

- **问题范围**：Q001 - Q010
- **核心实验**：做一次 input/output length × concurrency 的二维 sweep，绘制 TTFT、TPOT、Goodput 与 GPU/HBM 利用率。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q001 为什么 LLM 的 Prefill 和 Decode 是两种完全不同的计算？](q001-prefill-decode-roofline.md) - ★★★★★ - `prefill, decode, roofline`
- [Q002 TTFT、TPOT、ITL、E2E Latency、Throughput、Goodput 分别是什么？](q002-metrics-slo-goodput.md) - ★★★★☆ - `metrics, SLO, goodput`
- [Q003 为什么 batch=1 的 Decode 经常是 Memory Bound？](q003-decode-memory-bandwidth.md) - ★★★★★ - `decode, memory-bandwidth`
- [Q004 什么是 Roofline Model？如何用于分析 LLM inference？](q004-roofline-profiling.md) - ★★★★★ - `roofline, profiling`
- [Q005 如何估算一个模型 Decode 的理论 token/s？](q005-estimation-bandwidth.md) - ★★★★★ - `estimation, bandwidth`
- [Q006 输入长度和输出长度分别怎样影响成本？](q006-sequence-length-cost.md) - ★★★★☆ - `sequence-length, cost`
- [Q007 为什么 Batch Size 不是越大越好？](q007-batching-slo.md) - ★★★★☆ - `batching, SLO`
- [Q008 参数量和推理成本有什么关系？MoE 为什么不同？](q008-moe-active-params.md) - ★★★★★ - `MoE, active-params`
- [Q009 推理慢，你如何判断是 Compute、HBM、Network 还是 CPUBottleneck？](q009-profiling-debugging.md) - ★★★★★ - `profiling, debugging`
- [Q010 给你一个推理服务，正确的优化顺序是什么？](q010-methodology-benchmark.md) - ★★★★★ - `methodology, benchmark`
