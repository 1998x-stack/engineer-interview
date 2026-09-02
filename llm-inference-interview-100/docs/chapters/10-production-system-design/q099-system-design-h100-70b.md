---
id: Q099
title: "系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？"
chapter: "Benchmark、生产部署与系统设计"
difficulty: "★★★★★"
tags: ["system-design", "H100", "70B"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q099｜系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？

> **定位**：Benchmark、生产部署与系统设计 · **难度**：★★★★★  
> **关键词**：`system-design` · `H100` · `70B`

## 30 秒面试回答

> 先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡；候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace 比较 Goodput、p99 与成本。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡；候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace 比较 Goodput、p99 与成本。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 M_weights≈params×bytes；M_KV 用 Q11 公式；capacity=min(compute_capacity,KV_capacity,SLO_capacity)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡
- 2. 候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace
比较 Goodput、p99 与成本。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演高 QPS Chat 通常优先更多 replica；极低 latency 单请求可能使用更高 TP。若长 context，KV 容量可能决定
TP/replica 方案。

### 建议实验

先按权重+KV+workspace 做容量上界，再比较 TP=2×4 replicas 与 TP=4×2 replicas；最终以真实 Chat workload 的 Goodput/SLO 选型。

### 观测指标

- 使用真实 input/output/arrival 分布，报告 p50/p95/p99。
- 容量规划同时考虑 weights、KV、workspace、graph memory 与冗余。
- 性能回归先分解 queue/TTFT/TPOT，再逐层二分定位。
- 围绕“系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 直接答 TP=8
- ✗ 没有 SLO、长度分布和 dtype 就无法唯一决策。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 直接答 TP=8
- ✗ 没有 SLO、长度分布和 dtype 就无法唯一决策。

## 8. 追问链

- → 如果换 FP8 呢？
- → 如果平均 input 32K 呢？
- → 如果需要 99.9% TTFT<1s 呢？

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

把所有局部优化放到 SLO、容量、成本、可观测性与故障证据链中。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [NVIDIA H100 官方规格](https://www.nvidia.com/en-us/data-center/h100/)

## 12. 相关题目

- [Q060 一个 671B MoE 模型如何做多节点部署规划？](../06-distributed-inference/q060-moe-system-design.md)
- [Q098 生产 LLM Server 最重要的监控指标有哪些？](q098-observability-metrics.md)
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](q100-debugging-production-systematic.md)
- [Q097 线上发生 KV Cache OOM，你怎么处理？](q097-oom-kv-operations.md)
- [Q096 LLM Serving 如何做 Admission Control 和 Autoscaling？](q096-admission-control-autoscaling.md)

---

[← Q098](q098-observability-metrics.md) · [10 Benchmark、生产部署与系统设计](index.md) · [Q100 →](q100-debugging-production-systematic.md)
