---
id: Q049
title: "量化后的模型如何正确评估？"
chapter: "量化与低精度推理"
difficulty: "★★★★☆"
tags: ["quant-eval", "quality"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q049｜量化后的模型如何正确评估？

> **定位**：量化与低精度推理 · **难度**：★★★★☆  
> **关键词**：`quant-eval` · `quality`

## 30 秒面试回答

> 必须同时评估质量与系统收益：perplexity/任务准确率、reasoning/code/multilingual、长上下文；系统侧测 TTFT/TPOT/throughput/VRAM/cost。量化方案只有在目标 workload 的速度-质量 Pareto 上占优才算成功。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：必须同时评估质量与系统收益：perplexity/任务准确率、reasoning/code/multilingual、长上下文；系统侧测 TTFT/TPOT/throughput/VRAM/cost。量化方案只有在目标
workload 的速度-质量 Pareto 上占优才算成功。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Compare Δquality 与 speedup、memory_saved、goodput_gain，而非单一指标。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 必须同时评估质量与系统收益：perplexity/任务准确率、reasoning/code/multilingual、长上下文
- 2. 系统侧测 TTFT/TPOT/throughput/VRAM/cost。量化方案只有在目标 workload 的速度-质量 Pareto 上占优才算成功。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演某 INT4 在 WikiText perplexity 几乎不变，却可能在数学推理和长 context 上明显退化。

### 建议实验

同一模型比较 BF16、FP8、W4A16；在 batch=1 与高并发下分别测速度，解释 Roofline 变化。

### 观测指标

- 报告模型质量、VRAM、TTFT、TPOT、吞吐与长上下文结果。
- 区分 weight-only、W8A8/FP8、KV quant，各自瓶颈与硬件支持不同。
- 确认量化 kernel 是否原生高效，避免 dequant/packing 抵消收益。
- 围绕“量化后的模型如何正确评估？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 只测短文本 perplexity
- ✗ benchmark 使用与线上不同 kernel/框架。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 只测短文本 perplexity
- ✗ benchmark 使用与线上不同 kernel/框架。

## 8. 追问链

- → 如何设回归阈值？
- → 采样随机性如何控制？
- → 为什么 structured output 也应测试？

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

同时优化精度、内存、带宽和硬件 kernel，而不是把 bit-width 当成性能答案。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [TensorRT-LLM Quantization](https://nvidia.github.io/TensorRT-LLM/latest/features/quantization.html)

## 12. 相关题目

- [Q048 为什么 KV Quantization 和 Weight Quantization 是两个问题？](q048-kv-quant-dynamic.md)
- [Q050 为什么 INT4 模型有时候不比 FP16 快？](q050-int4-performance.md)
- [Q047 Per-tensor、Per-channel、Per-group quantization 怎么选？](q047-quantization-scales.md)
- [Q046 FP4 / NVFP4 为什么到 Blackwell 才更加实用？](q046-fp4-nvfp4-blackwell.md)
- [Q045 FP8 与 INT8 的工程区别是什么？](q045-fp8-int8.md)

---

[← Q048](q048-kv-quant-dynamic.md) · [05 量化与低精度推理](index.md) · [Q050 →](q050-int4-performance.md)
