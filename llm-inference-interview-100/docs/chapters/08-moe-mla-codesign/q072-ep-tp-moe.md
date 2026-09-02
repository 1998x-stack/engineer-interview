---
id: Q072
title: "Expert Parallel 和 Tensor Parallel 的本质区别？"
chapter: "MoE、MLA 与模型-系统协同"
difficulty: "★★★★★"
tags: ["EP", "TP", "MoE"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q072｜Expert Parallel 和 Tensor Parallel 的本质区别？

> **定位**：MoE、MLA 与模型-系统协同 · **难度**：★★★★★  
> **关键词**：`EP` · `TP` · `MoE`

## 30 秒面试回答

> TP 切一个矩阵本身，所有 token 通常参与同步 collective；EP 切不同 experts，只有被路由到某 expert 的 token  发送到对应 rank，通信是数据依赖的 all-to-all。两者可叠加：expert 内部做 TP，experts 之间做 EP。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：TP 切一个矩阵本身，所有 token 通常参与同步 collective；EP 切不同 experts，只有被路由到某 expert 的 token 发送到对应 rank，通信是数据依赖的 all-to-all。两者可叠加：expert
内部做 TP，experts 之间做 EP。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 TP communication 与 layer structure 固定；EP traffic 由 routing distribution 决定。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. TP 切一个矩阵本身，所有 token 通常参与同步 collective
- 2. EP 切不同 experts，只有被路由到某 expert 的 token 发送到对应 rank，通信是数据依赖的 all-to-all。两者可叠加：expert 内部做 TP，experts 之间做 EP。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演如果一个 expert 太大单卡放不下，可 EP 分 expert、再对单 expert TP。

### 建议实验

对 MoE workload 记录每 expert token histogram、All-to-All 时间和 grouped GEMM shape，随并发变化分析。

### 观测指标

- MoE 关注 tokens/expert 分布、All-to-All、grouped GEMM 与 load imbalance。
- MLA/GQA 关注 KV bytes/token 和 attention backend 支持。
- 模型架构变化后重新做 profile，不套 Dense Llama 的经验公式。
- 围绕“Expert Parallel 和 Tensor Parallel 的本质区别？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 把 EP size 直接等价于 expert 数
- ✗ 一个 rank 可放多个 expert，也可复制 expert。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 把 EP size 直接等价于 expert 数
- ✗ 一个 rank 可放多个 expert，也可复制 expert。

## 8. 追问链

- → EP×TP rank 怎么布局？
- → 何时 expert replication 优于更大 EP？
- → shared expert 属于哪一层？

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

理解现代模型结构如何重写 KV、GEMM、routing 与通信的性能模型。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)

## 12. 相关题目

- [Q054 Expert Parallelism 是什么？](../06-distributed-inference/q054-ep-moe.md)
- [Q071 为什么 MoE 理论 FLOPs 很低，线上 latency 却未必低？](q071-moe-latency.md)
- [Q073 MoE Expert Load Imbalance 为什么严重？](q073-load-balance-moe.md)
- [Q074 All-to-All 为什么是 MoE 推理的关键瓶颈？](q074-alltoall-moe.md)
- [Q075 Shared Expert 有什么意义？](q075-shared-expert-moe.md)

---

[← Q071](q071-moe-latency.md) · [08 MoE、MLA 与模型-系统协同](index.md) · [Q073 →](q073-load-balance-moe.md)
