---
id: Q013
title: "PagedAttention 到底解决了什么？"
chapter: "KV Cache 与 Attention"
difficulty: "★★★★★"
tags: ["PagedAttention", "KV"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q013｜PagedAttention 到底解决了什么？

> **定位**：KV Cache 与 Attention · **难度**：★★★★★  
> **关键词**：`PagedAttention` · `KV`

## 30 秒面试回答

> 它主要解决动态 KV Cache 的内存管理，而非改变 attention 数学。把逻辑序列映射到固定大小的物理 block，避免要求连续显存，减少 external fragmentation，并支持更自然的共享与 copy-on-write。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：它主要解决动态 KV Cache 的内存管理，而非改变 attention
数学。把逻辑序列映射到固定大小的物理 block，避免要求连续显存，减少 external fragmentation，并支持更自然的共享与 copy-on-write。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Logical block table → physical KV blocks；请求长度增长时按需分配 block。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 它主要解决动态 KV Cache 的内存管理，而非改变 attention 数学。把逻辑序列映射到固定大小的物理 block，避免要求连续显存，减少 external fragmentation，并支持更自然的共享与 copy-on-write。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 Beam search 或共享 system prompt 可让多个序列引用相同物理块，在分叉时才复制写入。

### 建议实验

固定总 KV 容量，比较连续预分配与分页管理在随机输出长度 workload 下的可服务并发、碎片率和 OOM/抢占次数。

### 观测指标

- 先手算每 token KV bytes，再估算给定并发与上下文长度的总占用。
- 区分容量优化、带宽优化与复用优化：它们解决的瓶颈不同。
- 测 prefix hit、page waste、eviction/preemption，并观察对 TTFT/TPOT 的作用。
- 围绕“PagedAttention 到底解决了什么？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

分页减少外部碎片，但仍有最后一页内部碎片、元数据与寻址成本；page size 仍需权衡。

- ✗ 把 PagedAttention 解释成“更快的 softmax”
- ✗ 忽略 page table/last-block internal fragmentation 的代价。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 把 PagedAttention 解释成“更快的 softmax”
- ✗ 忽略 page table/last-block internal fragmentation 的代价。

## 8. 追问链

- → 它和 OS virtual memory 的类比哪里成立、哪里不成立？
- → block size 怎么选？
- → 为什么它让 continuous batching 更可行？

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

把 KV Cache 当作动态内存系统，而不仅是 Transformer 中间张量。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [PagedAttention / vLLM 论文](https://arxiv.org/abs/2309.06180)

## 12. 相关题目

- [Q014 KV block/page size 为什么不能无限小？](q014-kv-page-size.md)
- [Q015 什么叫 KV Cache 的 Internal Fragmentation？](q015-fragmentation-kv.md)
- [Q028 KV Cache 不够时应该 Swap、Recompute 还是 Reject？](../03-batching-scheduling/q028-preemption-kv.md)
- [Q076 MLA 与 GQA 谁更省 KV Cache？](../08-moe-mla-codesign/q076-mla-gqa-kv.md)
- [Q085 TensorRT-LLM 的 KV Cache system 有什么特点？](../09-serving-runtimes/q085-tensorrt-llm-kv.md)

---

[← Q012](q012-mha-gqa-mqa.md) · [02 KV Cache 与 Attention](index.md) · [Q014 →](q014-kv-page-size.md)
