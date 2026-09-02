---
id: Q008
title: "参数量和推理成本有什么关系？MoE 为什么不同？"
chapter: "推理性能基本原理"
difficulty: "★★★★★"
tags: ["MoE", "active-params"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q008｜参数量和推理成本有什么关系？MoE 为什么不同？

> **定位**：推理性能基本原理 · **难度**：★★★★★  
> **关键词**：`MoE` · `active-params`

## 30 秒面试回答

> Dense 模型每 token 激活几乎全部参数，因此总参数量与权重带宽、FLOPs 强相关；MoE 总参数决定内存容量， 但每 token 只激活少数 expert，计算量由 active params 决定。MoE 又新增 routing、dispatch 与 all-to-all，因此“参数更多但每 token FLOPs 更低”并不等于延迟一定低。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：Dense 模型每 token 激活几乎全部参数，因此总参数量与权重带宽、FLOPs 强相关；MoE 总参数决定内存容量，但每 token 只激活少数 expert，计算量由 active params 决定。MoE 又新增 routing、dispatch 与 all-to-all，因此“参数更多但每 token FLOPs 更低”并不等于延迟一定低。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Dense: active≈total；MoE: active≪total，且 T≈max(expert_compute, dispatch/AllToAll)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. Dense 模型每 token 激活几乎全部参数，因此总参数量与权重带宽、FLOPs 强相关
- 2. MoE 总参数决定内存容量，但每 token 只激活少数 expert，计算量由 active params 决定。MoE 又新增 routing、dispatch 与 all-to-all，因此“参数更多但每 token FLOPs 更低”并不等于延迟一定低。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 671B 总参数、约 37B active 的 MoE 需要容纳巨大权重池，但单 token 计算量更接近几十 B active 参数模型。

### 建议实验

做一次 input/output length × concurrency 的二维 sweep，绘制 TTFT、TPOT、Goodput 与 GPU/HBM 利用率。

### 观测指标

- 固定模型、精度、硬件与请求分布，避免“换 workload 得到假优化”。
- 同时记录 TTFT、TPOT/ITL、E2E、tokens/s、req/s 与 Goodput。
- 先看资源上限：Tensor Core、HBM、互联、CPU launch，再看框架参数。
- 围绕“参数量和推理成本有什么关系？MoE 为什么不同？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 用 active FLOPs 直接预测 MoE latency
- ✗ 忽略专家不均衡和跨节点通信。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 用 active FLOPs 直接预测 MoE latency
- ✗ 忽略专家不均衡和跨节点通信。

## 8. 追问链

- → 为什么 EP 比 TP 更自然？
- → 低并发为何让 MoE 变慢？
- → shared expert 的系统意义是什么？

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

建立统一成本模型：先区分 Prefill/Decode，再用 Roofline、排队与 SLO 判断关键路径。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q054 Expert Parallelism 是什么？](../06-distributed-inference/q054-ep-moe.md)
- [Q060 一个 671B MoE 模型如何做多节点部署规划？](../06-distributed-inference/q060-moe-system-design.md)
- [Q071 为什么 MoE 理论 FLOPs 很低，线上 latency 却未必低？](../08-moe-mla-codesign/q071-moe-latency.md)
- [Q072 Expert Parallel 和 Tensor Parallel 的本质区别？](../08-moe-mla-codesign/q072-ep-tp-moe.md)
- [Q073 MoE Expert Load Imbalance 为什么严重？](../08-moe-mla-codesign/q073-load-balance-moe.md)

---

[← Q007](q007-batching-slo.md) · [01 推理性能基本原理](index.md) · [Q009 →](q009-profiling-debugging.md)
