---
id: Q060
title: "一个 671B MoE 模型如何做多节点部署规划？"
chapter: "分布式推理与通信"
difficulty: "★★★★★"
tags: ["MoE", "system-design"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q060｜一个 671B MoE 模型如何做多节点部署规划？

> **定位**：分布式推理与通信 · **难度**：★★★★★  
> **关键词**：`MoE` · `system-design`

## 30 秒面试回答

> 先算权重/量化容量与 KV，再按 expert 数设计 EP，使大多数 expert 通信尽量落在高速域；根据每 expert GEMM 尺寸决定是否再 TP；评估 all-to-all、shared expert、routing balance、DP replica 与 P/D 分离。最后用真实输入/输出分布做 capacity test。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：先算权重/量化容量与 KV，再按 expert 数设计 EP，使大多数
expert 通信尽量落在高速域；根据每 expert GEMM 尺寸决定是否再 TP；评估 all-to-all、shared expert、routing
balance、DP replica 与 P/D 分离。最后用真实输入/输出分布做 capacity test。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Memory = local_expert_weights + shared/dense_weights + KV + runtime；Latency=max(compute, A2A, TP
collectives)+overheads。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 先算权重/量化容量与 KV，再按 expert 数设计 EP，使大多数 expert 通信尽量落在高速域
- 2. 根据每 expert GEMM 尺寸决定是否再 TP
- 3. 评估 all-to-all、shared expert、routing balance、DP replica 与 P/D 分离。最后用真实输入/输出分布做 capacity
test。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演大 EP 能把权重摊开，但如果跨节点 A2A 太慢，需要 expert replication、node-limited routing 或更合理
placement。

### 建议实验

运行 `nvidia-smi topo -m`，对比单机 TP 与跨节点 TP 的延迟/吞吐，并关联 NCCL timeline。

### 观测指标

- 先画物理拓扑：GPU/NVLink/PCIe/NIC/节点，再选 TP/PP/EP/CP。
- 记录 collective bytes、时间、overlap 与 straggler。
- 把单卡 compute 提升和跨卡通信放在同一个 critical path 中评估。
- 围绕“一个 671B MoE 模型如何做多节点部署规划？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 只按总参数/显存算“能放下”就结束
- ✗ MoE 性能通常死在通信和小 GEMM。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 只按总参数/显存算“能放下”就结束
- ✗ MoE 性能通常死在通信和小 GEMM。

## 8. 追问链

- → EP size 怎么选？
- → 专家热度不均如何处理？
- → P/D 分离后两侧并行策略是否相同？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 07

Speculative Decoding
理解 draft-verify、acceptance、Medusa/EAGLE/MTP，以及何时加速、何时负优化。

本章题目 Q061 - Q070 · 共 10 题

本章学习目标
- 理解 lossless speculative sampling。
- 会根据 acceptance 与 draft cost 判断收益。
- 能比较 N-gram/Medusa/EAGLE/MTP。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

从模型切分上升到拓扑感知的通信成本模型。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q054 Expert Parallelism 是什么？](q054-ep-moe.md)
- [Q071 为什么 MoE 理论 FLOPs 很低，线上 latency 却未必低？](../08-moe-mla-codesign/q071-moe-latency.md)
- [Q072 Expert Parallel 和 Tensor Parallel 的本质区别？](../08-moe-mla-codesign/q072-ep-tp-moe.md)
- [Q073 MoE Expert Load Imbalance 为什么严重？](../08-moe-mla-codesign/q073-load-balance-moe.md)
- [Q074 All-to-All 为什么是 MoE 推理的关键瓶颈？](../08-moe-mla-codesign/q074-alltoall-moe.md)

---

[← Q059](q059-overlap-communication.md) · [06 分布式推理与通信](index.md) · [Q061 →](../07-speculative-decoding/q061-speculative-decoding-draft.md)
