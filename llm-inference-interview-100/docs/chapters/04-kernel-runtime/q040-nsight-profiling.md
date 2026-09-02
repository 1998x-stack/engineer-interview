---
id: Q040
title: "Nsight 里看到 GPU Util=100%，为什么模型仍可能很慢？"
chapter: "CUDA、Attention Kernel 与 Runtime"
difficulty: "★★★★★"
tags: ["Nsight", "profiling"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q040｜Nsight 里看到 GPU Util=100%，为什么模型仍可能很慢？

> **定位**：CUDA、Attention Kernel 与 Runtime · **难度**：★★★★★  
> **关键词**：`Nsight` · `profiling`

## 30 秒面试回答

> “GPU active”只说明设备有工作，不代表 Tensor Core 或 HBM 达到有效峰值。可能是单个低效率 kernel、 memcpy、串行 NCCL 或大量 stall。必须继续看 SM throughput、Tensor pipe、DRAM throughput、occupancy、stall reasons 与时间线重叠。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：“GPU active”只说明设备有工作，不代表 Tensor Core 或
HBM 达到有效峰值。可能是单个低效率 kernel、memcpy、串行 NCCL 或大量 stall。必须继续看 SM throughput、Tensor
pipe、DRAM throughput、occupancy、stall reasons 与时间线重叠。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Utilization 是“是否忙”的指标，不是“忙得有效”的指标。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. “GPU active”只说明设备有工作，不代表 Tensor Core 或 HBM 达到有效峰值。可能是单个低效率 kernel、memcpy、串行 NCCL 或大量 stall。必须继续看 SM throughput、Tensor pipe、DRAM throughput、occupancy、stall reasons 与时间线重叠。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演一个 memory copy 持续占 GPU 时间也可能让利用率显示很高，但模型 FLOP/s 很低。

### 建议实验

从 Nsight Systems 的 timeline 确认 GPU active 后，再用 Nsight Compute 检查 SM/Tensor/HBM；构造一个 memcpy-heavy 对照说明“100% active”并不等于高有效算力。

### 观测指标

- 用 Nsight Systems 看 timeline/空洞，用 Nsight Compute 看 kernel 级吞吐与 stall。
- 分别 benchmark prefill/decode，不用单一平均值掩盖 shape 差异。
- 核对 kernel backend、dtype、page layout、CUDA Graph/compile 是否真的命中。
- 围绕“Nsight 里看到 GPU Util=100%，为什么模型仍可能很慢？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 用 nvidia-smi GPU-Util 作为优化终点。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 用 nvidia-smi GPU-Util 作为优化终点。

## 8. 追问链

- → Nsight Systems 与 Compute 各看哪些 counter？
- → 如何识别 memory throttling？
- → 如何找 NCCL overlap？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 05

量化与低精度推理比较 GPTQ、AWQ、SmoothQuant、FP8/FP4、KV Quantization 及其硬件约束。

本章题目 Q041 - Q050 · 共 10 题

本章学习目标
- 能比较主流 PTQ/低精度路线。
- 能解释为何 bit 更低不一定更快。
- 会做量化后的质量-性能联合回归。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

从“GPU 很忙”深入到 IO、tile、launch、shape 与 kernel critical path。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [Nsight Systems Analysis Guide](https://docs.nvidia.com/nsight-systems/AnalysisGuide/index.html)

## 12. 相关题目

- [Q009 推理慢，你如何判断是 Compute、HBM、Network 还是 CPUBottleneck？](../01-performance-fundamentals/q009-profiling-debugging.md)
- [Q004 什么是 Roofline Model？如何用于分析 LLM inference？](../01-performance-fundamentals/q004-roofline-profiling.md)
- [Q039 为什么 Tensor Core 对矩阵 Shape 很敏感？](q039-tensor-core-shape.md)
- [Q038 为什么 Prefill GEMM 和 Decode GEMM 优化完全不同？](q038-gemm-prefill-decode.md)
- [Q037 什么情况下 Kernel Launch Overhead 会成为瓶颈？](q037-launch-overhead-cuda.md)

---

[← Q039](q039-tensor-core-shape.md) · [04 CUDA、Attention Kernel 与 Runtime](index.md) · [Q041 →](../05-quantization/q041-quantization-w4a16-w8a8.md)
