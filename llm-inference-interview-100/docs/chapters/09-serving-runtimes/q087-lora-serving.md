---
id: Q087
title: "Multi-LoRA Serving 怎么优化？"
chapter: "vLLM / SGLang / TensorRT-LLM"
difficulty: "★★★★☆"
tags: ["LoRA", "serving"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q087｜Multi-LoRA Serving 怎么优化？

> **定位**：vLLM / SGLang / TensorRT-LLM · **难度**：★★★★☆  
> **关键词**：`LoRA` · `serving`

## 30 秒面试回答

> Base weights 在所有请求间共享，仅 adapter A/B 小矩阵随请求不同。关键是避免按 adapter 把 batch 切碎：把同一 batch 中不同 LoRA 的低秩增量用 batched/grouped kernel 计算，同时缓存热门 adapter，减少切换和加载。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：Base weights 在所有请求间共享，仅 adapter A/B 小矩阵随请求不同。关键是避免按 adapter 把 batch 切碎：把同一 batch 中不同 LoRA 的低秩增量用 batched/grouped kernel 计算，同时缓存热门 adapter，减少切换和加载。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 y = xW_base + xA_iB_i；W_base 共享，A_i/B_i 按 request 选择。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. Base weights 在所有请求间共享，仅 adapter A/B 小矩阵随请求不同。关键是避免按 adapter 把 batch 切碎：把同一
batch 中不同 LoRA 的低秩增量用 batched/grouped kernel 计算，同时缓存热门 adapter，减少切换和加载。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 100 个租户各有 LoRA，如果逐租户独立 batch，GPU 利用率会崩；fused multi-LoRA kernel 可保留主 batch。

### 建议实验

同一模型同一 workload 在两个 runtime 上跑统一 benchmark schema，比较 Goodput 与 p99，而非只看峰值 tokens/s。

### 观测指标

- 技术选型固定模型/硬件/workload/SLO 后再 benchmark。
- 核对版本：scheduler、cache、quant、spec decode、PD 能力变化很快。
- 把易用性、模型覆盖、可观测性与升级成本纳入生产决策。
- 围绕“Multi-LoRA Serving 怎么优化？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 只关注 adapter 显存很小，忽略 adapter diversity 对 batching 的破坏。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 只关注 adapter 显存很小，忽略 adapter diversity 对 batching 的破坏。

## 8. 追问链

- → LoRA rank 如何影响 kernel？
- → adapter cache 怎么做？
- → 不同 TP rank 如何切 LoRA？

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

把框架理解为 scheduler + cache manager + executor + kernels + distributed runtime 的组合。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q091 你会如何 Benchmark 一个 LLM Serving Engine？](../10-production-system-design/q091-benchmark-serving.md)
- [Q086 SGLang HiCache 是什么？](q086-hicache-sglang.md)
- [Q088 Structured Output 为什么会影响推理性能？](q088-structured-output-fsm.md)
- [Q085 TensorRT-LLM 的 KV Cache system 有什么特点？](q085-tensorrt-llm-kv.md)
- [Q089 为什么模型刚启动时延迟明显更高？](q089-cold-start-startup.md)

---

[← Q086](q086-hicache-sglang.md) · [09 vLLM / SGLang / TensorRT-LLM](index.md) · [Q088 →](q088-structured-output-fsm.md)
