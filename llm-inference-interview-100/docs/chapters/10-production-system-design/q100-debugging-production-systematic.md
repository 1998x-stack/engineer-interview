---
id: Q100
title: "终极综合题：线上模型突然慢了 30%，你如何定位？"
chapter: "Benchmark、生产部署与系统设计"
difficulty: "★★★★★"
tags: ["debugging", "production", "systematic"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q100｜终极综合题：线上模型突然慢了 30%，你如何定位？

> **定位**：Benchmark、生产部署与系统设计 · **难度**：★★★★★  
> **关键词**：`debugging` · `production` · `systematic`

## 30 秒面试回答

> 先确认变更与流量是否变化；将退化拆为 queue/TTFT/TPOT，按请求长度和 tenant 分桶。再看 scheduler/KV 指标、GPU timeline、kernel/HBM、NCCL 与 CPU。做 fixed-input controlled experiment 并逐项关闭 cache/spec/compile/parallel features，最终用 A/B 或回滚验证根因。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：先确认变更与流量是否变化；将退化拆为
queue/TTFT/TPOT，按请求长度和 tenant 分桶。再看 scheduler/KV 指标、GPU timeline、kernel/HBM、NCCL 与 CPU。做 fixed-input controlled experiment 并逐项关闭 cache/spec/compile/parallel features，最终用 A/B 或回滚验证根因。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式诊断树：Regression scope → TTFT/TPOT split → Scheduler/KV → GPU/Kernel → Network/CPU → Controlled
isolation → Root-cause proof。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 先确认变更与流量是否变化
- 2. 将退化拆为 queue/TTFT/TPOT，按请求长度和 tenant 分桶。再看 scheduler/KV 指标、GPU timeline、kernel/HBM、NCCL 与 CPU。做 fixed-input controlled experiment 并逐项关闭 cache/spec/compile/parallel features，最终用 A/B 或回滚验证根因。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演若 TTFT 升而 TPOT 不变，优先查 Prefill/queue/cache；若 TPOT 升，查 Decode batch、HBM、KV、NCCL、spec acceptance。

### 建议实验

冻结一组 fixed-input 回放流量，做版本二分和 feature flag 二分；每次只改一个变量，把“相关性”升级为可重复的因果证据。

### 观测指标

- 使用真实 input/output/arrival 分布，报告 p50/p95/p99。
- 容量规划同时考虑 weights、KV、workspace、graph memory 与冗余。
- 性能回归先分解 queue/TTFT/TPOT，再逐层二分定位。
- 围绕“终极综合题：线上模型突然慢了 30%，你如何定位？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 直接猜“驱动问题”
- ✗ 没有时间线、没有对照、一次改多个变量。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 直接猜“驱动问题”
- ✗ 没有时间线、没有对照、一次改多个变量。

## 8. 追问链

- → 如何确认是 workload drift？
- → 如何做 performance bisect？
- → 怎么防止同类回归再次发生？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确诊断路径，并能把 TTFT/TPOT 分开。
- 优秀：能用 controlled experiment、profile 与回滚/A-B 建立可证伪的根因证据链。

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
- [Nsight Systems Analysis Guide](https://docs.nvidia.com/nsight-systems/AnalysisGuide/index.html)

## 12. 相关题目

- [Q090 如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？](../09-serving-runtimes/q090-framework-selection-production.md)
- [Q029 为什么生产系统应该优化 Goodput，而不是最高 Throughput？](../03-batching-scheduling/q029-goodput-production.md)
- [Q009 推理慢，你如何判断是 Compute、HBM、Network 还是 CPUBottleneck？](../01-performance-fundamentals/q009-profiling-debugging.md)
- [Q099 系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？](q099-system-design-h100-70b.md)
- [Q098 生产 LLM Server 最重要的监控指标有哪些？](q098-observability-metrics.md)

---

[← Q099](q099-system-design-h100-70b.md) · [10 Benchmark、生产部署与系统设计](index.md)
