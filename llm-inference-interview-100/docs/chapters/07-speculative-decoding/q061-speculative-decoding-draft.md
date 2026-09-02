---
id: Q061
title: "Speculative Decoding 的基本原理是什么？"
chapter: "Speculative Decoding"
difficulty: "★★★★★"
tags: ["speculative-decoding", "draft"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q061｜Speculative Decoding 的基本原理是什么？

> **定位**：Speculative Decoding · **难度**：★★★★★  
> **关键词**：`speculative-decoding` · `draft`

## 30 秒面试回答

> 用更便宜的 proposer/draft 一次猜多个 token，再让 target 用一次或少数 forward 并行验证；若平均接受多个 token，就减少 target 的串行 decode step。核心不是“少算 target FLOPs”，而是用一次较大的验证替代多次小的 memory-bound decode。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：用更便宜的 proposer/draft 一次猜多个 token，再让 target
用一次或少数 forward 并行验证；若平均接受多个 token，就减少 target 的串行 decode step。核心不是“少算 target
FLOPs”，而是用一次较大的验证替代多次小的 memory-bound decode。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Speedup 取决于 accepted_tokens / (draft_cost + verify_cost)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 用更便宜的 proposer/draft 一次猜多个 token，再让 target 用一次或少数 forward 并行验证
- 2. 若平均接受多个 token，就减少 target 的串行 decode step。核心不是“少算 target FLOPs”，而是用一次较大的验证替代多次小的 memory-bound decode。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 draft 每轮提 5 个 token，target 平均接受 4 个，则一次 target 验证推进约 4 token，而非 1 token。

### 建议实验

对不同 draft 长度/温度做 sweep，画 accepted tokens 与实际 speedup 曲线。

### 观测指标

- 至少记录 acceptance length/rate、draft latency、verify latency 与最终 TPOT。
- 高 QPS 与低 QPS 分开压测；大 batch 可能减少 speculation 的相对收益。
- 验证输出分布/质量约束，区分 lossless 与近似方法。
- 围绕“Speculative Decoding 的基本原理是什么？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

Speculative decoding 的“lossless”依赖正确的接受/校正算法；工程实现还需考虑采样参数与并行验证。

- ✗ 把 draft 输出直接当最终答案
- ✗ 标准 speculative sampling 需要正确接受/拒绝规则。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 把 draft 输出直接当最终答案
- ✗ 标准 speculative sampling 需要正确接受/拒绝规则。

## 8. 追问链

- → 为什么它特别适合 memory-bound decode？
- → 验证为什么可以并行多个 token？
- → 采样分布如何保持一致？

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

用“proposal 成本 + verification 成本 + acceptance”而不是宣传 speedup 判断价值。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q062 为什么标准 speculative sampling 可以保持输出分布不变？](q062-speculative-sampling-correctness.md)
- [Q063 Acceptance Rate 为什么是 Spec Decode 最关键指标之一？](q063-acceptance-spec-decode.md)
- [Q064 Draft Model 为什么不能越小越好？](q064-draft-model-tradeoff.md)
- [Q065 N-gram / Suffix speculation 为什么不需要 Draft Model？](q065-ngram-speculation.md)
- [Q066 Medusa 是什么？](q066-medusa-spec-decode.md)

---

[← Q060](../06-distributed-inference/q060-moe-system-design.md) · [07 Speculative Decoding](index.md) · [Q062 →](q062-speculative-sampling-correctness.md)
