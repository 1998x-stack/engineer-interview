---
id: Q090
title: "如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？"
chapter: "vLLM / SGLang / TensorRT-LLM"
difficulty: "★★★★★"
tags: ["framework-selection", "production"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q090｜如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？

> **定位**：vLLM / SGLang / TensorRT-LLM · **难度**：★★★★★  
> **关键词**：`framework-selection` · `production`

## 30 秒面试回答

> 建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的 Goodput/成本。先排除 feature gap，再 benchmark Pareto frontier。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的
Goodput/成本。先排除 feature gap，再 benchmark Pareto frontier。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式不要只比较峰值 tokens/s；至少比较 SLO-constrained goodput 与 $/M token。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的 Goodput/成本。先排除 feature gap，再 benchmark Pareto
frontier。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 Agent/prefix-heavy workload 可能偏好强 cache/scheduler；固定 NVIDIA low-precision fleet 可能偏好 TRT-
LLM；模型迭代快则生态适配很关键。

### 建议实验

准备统一 benchmark manifest，在 vLLM/SGLang/TensorRT-LLM 中保持模型 revision、量化、TP、流量分布与 SLO 一致；按 Goodput、p99、运维复杂度评分。

### 观测指标

- 技术选型固定模型/硬件/workload/SLO 后再 benchmark。
- 核对版本：scheduler、cache、quant、spec decode、PD 能力变化很快。
- 把易用性、模型覆盖、可观测性与升级成本纳入生产决策。
- 围绕“如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 选型表里没有“升级成本/可观测性/故障恢复”。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 选型表里没有“升级成本/可观测性/故障恢复”。

## 8. 追问链

- → 如何做两周 PoC？
- → 谁负责模型新架构适配？
- → 如何避免 vendor/framework lock-in？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 10

Benchmark、生产部署与系统设计把算法优化落到 SLO、Goodput、成本、监控、故障定位与容量规划。

本章题目 Q091 - Q100 · 共 10 题

本章学习目标
- 能设计可复现 benchmark。
- 能把 SLO、Goodput、成本和容量规划串起来。
- 能系统定位线上 30% 性能回归。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

把框架理解为 scheduler + cache manager + executor + kernels + distributed runtime 的组合。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

### 版本敏感补充

三套 runtime 的 feature surface 都在快速扩张：选型文档必须记录版本/commit。建议把“模型支持、KV/prefix、quant、spec decode、P/D、MoE/MLA kernel、拓扑扩展、可观测性、升级成本”作为固定评分维度，而不是维护一张容易过期的绝对性能榜。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [TensorRT-LLM 文档](https://nvidia.github.io/TensorRT-LLM/)

## 12. 相关题目

- [Q084 TensorRT-LLM 和 vLLM 怎么选？](q084-framework-selection-trtllm-vllm.md)
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](../10-production-system-design/q100-debugging-production-systematic.md)
- [Q029 为什么生产系统应该优化 Goodput，而不是最高 Throughput？](../03-batching-scheduling/q029-goodput-production.md)
- [Q089 为什么模型刚启动时延迟明显更高？](q089-cold-start-startup.md)
- [Q088 Structured Output 为什么会影响推理性能？](q088-structured-output-fsm.md)

---

[← Q089](q089-cold-start-startup.md) · [09 vLLM / SGLang / TensorRT-LLM](index.md) · [Q091 →](../10-production-system-design/q091-benchmark-serving.md)
