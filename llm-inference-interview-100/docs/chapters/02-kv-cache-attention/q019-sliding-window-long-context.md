---
id: Q019
title: "Sliding Window Attention 如何降低推理复杂度？"
chapter: "KV Cache 与 Attention"
difficulty: "★★★★☆"
tags: ["sliding-window", "long-context"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q019｜Sliding Window Attention 如何降低推理复杂度？

> **定位**：KV Cache 与 Attention · **难度**：★★★★☆  
> **关键词**：`sliding-window` · `long-context`

## 30 秒面试回答

> 只保留或访问最近 W 个 token，使 Decode attention 的历史长度从 T 截断为 W，KV 占用和读取不再随无限历史增长。它属于模型语义/结构改变，不能像 serving 参数一样无损开启。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：只保留或访问最近 W 个 token，使 Decode attention 的历史长度从 T 截断为 W，KV 占用和读取不再随无限历史增长。它属于模型语义/结构改变，不能像 serving 参数一样无损开启。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Full decode attention O(T) per step；windowed O(W)，KV 从 O(T) 变 O(W)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 只保留或访问最近 W 个 token，使 Decode attention 的历史长度从 T 截断为 W，KV 占用和读取不再随无限历史增长。它属于模型语义/结构改变，不能像 serving 参数一样无损开启。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 128K 对话若模型层使用 8K sliding window，缓存与读取可大幅下降，但模型对窗口外信息的直接访问受限。

### 建议实验

构造共享 system prompt 与随机 prompt 两组流量，对比 prefix cache hit、TTFT、KV 占用与吞吐。

### 观测指标

- 先手算每 token KV bytes，再估算给定并发与上下文长度的总占用。
- 区分容量优化、带宽优化与复用优化：它们解决的瓶颈不同。
- 测 prefix hit、page waste、eviction/preemption，并观察对 TTFT/TPOT 的作用。
- 围绕“Sliding Window Attention 如何降低推理复杂度？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 在未训练支持的模型上强行截断 KV
- ✗ 忽略混合 full/sliding layers 的 hybrid cache。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 在未训练支持的模型上强行截断 KV
- ✗ 忽略混合 full/sliding layers 的 hybrid cache。

## 8. 追问链

- → Mistral 类模型为何采用 sliding window？
- → Hybrid KV manager 怎么设计？
- → 和 retrieval memory 有何区别？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

把 KV Cache 当作动态内存系统，而不仅是 Transformer 中间张量。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q055 Context Parallelism 为什么越来越重要？](../06-distributed-inference/q055-cp-long-context.md)
- [Q018 为什么 KV Cache 也值得量化？](q018-kv-quant-fp8.md)
- [Q020 MLA 为什么对推理优化特别重要？](q020-mla-deepseek.md)
- [Q017 RadixAttention 与普通 Prefix Cache 有什么不同？](q017-sglang-radixattention.md)
- [Q016 Prefix Caching 为什么有时收益巨大，有时几乎没用？](q016-prefix-cache-cache.md)

---

[← Q018](q018-kv-quant-fp8.md) · [02 KV Cache 与 Attention](index.md) · [Q020 →](q020-mla-deepseek.md)
