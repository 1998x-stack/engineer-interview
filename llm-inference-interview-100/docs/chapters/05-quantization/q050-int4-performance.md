---
id: Q050
title: "为什么 INT4 模型有时候不比 FP16 快？"
chapter: "量化与低精度推理"
difficulty: "★★★★★"
tags: ["INT4", "performance"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q050｜为什么 INT4 模型有时候不比 FP16 快？

> **定位**：量化与低精度推理 · **难度**：★★★★★  
> **关键词**：`INT4` · `performance`

## 30 秒面试回答

> 容量/带宽减少并不自动等价于端到端延迟降低。若 dequant、unpack、scale load、kernel launch 或不友好的 shape 抵消收益；或工作负载已 compute/attention/communication-bound，权重压缩不会解决关键路径。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：容量/带宽减少并不自动等价于端到端延迟降低。若
dequant、unpack、scale load、kernel launch 或不友好的 shape 抵消收益；或工作负载已
compute/attention/communication-bound，权重压缩不会解决关键路径。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Speedup≈baseline_critical_path / new_critical_path；只缩短非关键项不会提速。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 容量/带宽减少并不自动等价于端到端延迟降低。若 dequant、unpack、scale load、kernel launch 或不友好的 shape
抵消收益
- 2. 或工作负载已 compute/attention/communication-bound，权重压缩不会解决关键路径。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演大 batch Prefill 已被 Tensor Core GEMM 限制，某 W4A16 kernel 需要先解码成 FP16，反而可能慢于原生
FP16/FP8。

### 建议实验

同模型用 BF16 与 INT4，在 batch=1、8、32 三档压测；同时记录 HBM、dequant kernel、GEMM 时间，解释为什么某档位有正收益、另一些没有。

### 观测指标

- 报告模型质量、VRAM、TTFT、TPOT、吞吐与长上下文结果。
- 区分 weight-only、W8A8/FP8、KV quant，各自瓶颈与硬件支持不同。
- 确认量化 kernel 是否原生高效，避免 dequant/packing 抵消收益。
- 围绕“为什么 INT4 模型有时候不比 FP16 快？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 用模型文件大小推断性能
- ✗ 不看实际 kernel backend。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 用模型文件大小推断性能
- ✗ 不看实际 kernel backend。

## 8. 追问链

- → 如何识别 dequant overhead？
- → 什么时候 FP8 比 INT4 更合适？
- → 如何做 microbenchmark 与 E2E 对照？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 06

分布式推理与通信掌握 TP/PP/DP/EP/CP，理解 NVLink/IB 拓扑与 collective 的成本模型。

本章题目 Q051 - Q060 · 共 10 题

本章学习目标
- 能从拓扑选择 TP/PP/DP/EP/CP。
- 会估 collective 与 overlap。
- 能设计多节点 MoE/长上下文部署。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

同时优化精度、内存、带宽和硬件 kernel，而不是把 bit-width 当成性能答案。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [TensorRT-LLM Quantization](https://nvidia.github.io/TensorRT-LLM/latest/features/quantization.html)

## 12. 相关题目

- [Q049 量化后的模型如何正确评估？](q049-quant-eval-quality.md)
- [Q048 为什么 KV Quantization 和 Weight Quantization 是两个问题？](q048-kv-quant-dynamic.md)
- [Q047 Per-tensor、Per-channel、Per-group quantization 怎么选？](q047-quantization-scales.md)
- [Q046 FP4 / NVFP4 为什么到 Blackwell 才更加实用？](q046-fp4-nvfp4-blackwell.md)
- [Q045 FP8 与 INT8 的工程区别是什么？](q045-fp8-int8.md)

---

[← Q049](q049-quant-eval-quality.md) · [05 量化与低精度推理](index.md) · [Q051 →](../06-distributed-inference/q051-tp-distributed.md)
