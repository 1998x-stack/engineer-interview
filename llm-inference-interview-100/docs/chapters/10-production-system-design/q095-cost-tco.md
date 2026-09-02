---
id: Q095
title: "如何计算每百万输出 token 成本？"
chapter: "Benchmark、生产部署与系统设计"
difficulty: "★★★★☆"
tags: ["cost", "TCO"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q095｜如何计算每百万输出 token 成本？

> **定位**：Benchmark、生产部署与系统设计 · **难度**：★★★★☆  
> **关键词**：`cost` · `TCO`

## 30 秒面试回答

> 先用集群小时成本除以稳定输出 token/hour，再乘一百万；生产还要折算 GPU 利用率、冗余、CPU/网络/存储、 失败与 idle capacity。输入与输出 token 应分别核算，因为 Prefill 与 Decode 的成本结构不同。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：先用集群小时成本除以稳定输出 token/hour，再乘一百万；生产还要折算 GPU 利用率、冗余、CPU/网络/存储、失败与 idle capacity。输入与输出 token 应分别核算，因为 Prefill 与
Decode 的成本结构不同。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Cost/Mout = (GPU$/h×GPU_count + infra$/h) / output_tokens_per_h × 10^6。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 先用集群小时成本除以稳定输出 token/hour，再乘一百万
- 2. 生产还要折算 GPU 利用率、冗余、CPU/网络/存储、失败与 idle capacity。输入与输出 token 应分别核算，因为 Prefill
与 Decode 的成本结构不同。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演同一硬件在低 QPS 夜间利用率 20%，实际 $/M token 可能远高于满载 benchmark。

### 建议实验

建立可重复的 benchmark manifest：模型 revision、runtime commit、driver/CUDA、拓扑、参数、流量分布与结果。

### 观测指标

- 使用真实 input/output/arrival 分布，报告 p50/p95/p99。
- 容量规划同时考虑 weights、KV、workspace、graph memory 与冗余。
- 性能回归先分解 queue/TTFT/TPOT，再逐层二分定位。
- 围绕“如何计算每百万输出 token 成本？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

$/M token 不能只除 GPU 标价，还应明确利用率、冗余、输入/输出 token、网络与 idle capacity 的口径。

- ✗ 用云 GPU 标价/理论 tokens/s 得出成本
- ✗ 忽略 goodput 与闲置。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 用云 GPU 标价/理论 tokens/s 得出成本
- ✗ 忽略 goodput 与闲置。

## 8. 追问链

- → 怎么把 P/D 两池成本合并？
- → 量化节省显存但质量下降如何折算？
- → reserved capacity 怎么计？

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

## 12. 相关题目

- [Q006 输入长度和输出长度分别怎样影响成本？](../01-performance-fundamentals/q006-sequence-length-cost.md)
- [Q094 Throughput 和 Goodput 的区别是什么？](q094-goodput-slo.md)
- [Q096 LLM Serving 如何做 Admission Control 和 Autoscaling？](q096-admission-control-autoscaling.md)
- [Q093 为什么 p99 比平均 latency 更重要？](q093-p99-tail-latency.md)
- [Q097 线上发生 KV Cache OOM，你怎么处理？](q097-oom-kv-operations.md)

---

[← Q094](q094-goodput-slo.md) · [10 Benchmark、生产部署与系统设计](index.md) · [Q096 →](q096-admission-control-autoscaling.md)
