---
id: Q070
title: "Speculative Decoding 在什么情况下反而变慢？"
chapter: "Speculative Decoding"
difficulty: "★★★★★"
tags: ["spec-decode", "negative-speedup"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q070｜Speculative Decoding 在什么情况下反而变慢？

> **定位**：Speculative Decoding · **难度**：★★★★★  
> **关键词**：`spec-decode` · `negative-speedup`

## 30 秒面试回答

> 高 QPS 时 target 已被大 batch 充分利用，额外 draft/verification 会争夺 compute；acceptance 低、输出很短、draft 太大或 verification kernel 不好也会负优化。它通常更适合中低并发、memory-bound、长输出。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：高 QPS 时 target 已被大 batch 充分利用，额外
draft/verification 会争夺 compute；acceptance 低、输出很短、draft 太大或 verification kernel 不好也会负优化。它通常更适合中低并发、memory-bound、长输出。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式若 T_draft+T_verify > accepted_tokens×T_target_baseline，则负收益。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 高 QPS 时 target 已被大 batch 充分利用，额外 draft/verification 会争夺 compute
- 2. acceptance 低、输出很短、draft 太大或 verification kernel 不好也会负优化。它通常更适合中低并发、memory-
bound、长输出。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演离线大 batch 生成已是高效 GEMM，spec decode 可能把大矩阵拆成更多复杂工作，吞吐不升反降。

### 建议实验

在低 QPS 与高 QPS 两种流量下开关 spec decode；如果 target 已被大 batch 充分利用，观察 draft/verify 开销是否让 TPOT/Goodput 下降。

### 观测指标

- 至少记录 acceptance length/rate、draft latency、verify latency 与最终 TPOT。
- 高 QPS 与低 QPS 分开压测；大 batch 可能减少 speculation 的相对收益。
- 验证输出分布/质量约束，区分 lossless 与近似方法。
- 围绕“Speculative Decoding 在什么情况下反而变慢？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 以单请求 latency speedup 推断 cluster throughput。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 以单请求 latency speedup 推断 cluster throughput。

## 8. 追问链

- → 如何建立自动启停策略？
- → QPS 提升时 speculative length 是否应下降？
- → 如何与 continuous batching 联动？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 08

MoE、MLA 与模型-系统协同分析 Expert Parallel、All-to-All、负载不均衡、MLA 与现代 MoE serving。

本章题目 Q071 - Q080 · 共 10 题

本章学习目标
- 能把 MoE 的瓶颈从 FLOPs 转为 all-to-all 与 load balance。
- 理解 MLA/Shared Expert 的系统意义。
- 具备模型-系统协同思维。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

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
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

## 12. 相关题目

- [Q066 Medusa 是什么？](q066-medusa-spec-decode.md)
- [Q063 Acceptance Rate 为什么是 Spec Decode 最关键指标之一？](q063-acceptance-spec-decode.md)
- [Q069 Tree Attention 为什么能加速 speculative verification？](q069-tree-attention-verification.md)
- [Q068 MTP 为什么既可以用于训练，也可以用于推理加速？](q068-mtp-deepseek.md)
- [Q067 EAGLE 与普通 Draft Model 的关键区别？](q067-eagle-speculation.md)

---

[← Q069](q069-tree-attention-verification.md) · [07 Speculative Decoding](index.md) · [Q071 →](../08-moe-mla-codesign/q071-moe-latency.md)
