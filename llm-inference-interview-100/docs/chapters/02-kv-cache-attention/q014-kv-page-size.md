---
id: Q014
title: "KV block/page size 为什么不能无限小？"
chapter: "KV Cache 与 Attention"
difficulty: "★★★★☆"
tags: ["KV", "page-size"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q014｜KV block/page size 为什么不能无限小？

> **定位**：KV Cache 与 Attention · **难度**：★★★★☆  
> **关键词**：`KV` · `page-size`

## 30 秒面试回答

> 小 page 减少尾块浪费、提高 prefix 匹配粒度，但会增加 block table、metadata、寻址与 kernel 调度开销，并可能降低连续访存效率。大 page 相反。最优值依赖 context 分布、prefix reuse 与 backend kernel。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：小 page 减少尾块浪费、提高 prefix 匹配粒度，但会增加
block table、metadata、寻址与 kernel 调度开销，并可能降低连续访存效率。大 page 相反。最优值依赖 context 分布、prefix reuse 与 backend kernel。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 Waste≈(page_size - last_page_used) / page_size；metadata≈O(num_pages)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 小 page 减少尾块浪费、提高 prefix 匹配粒度，但会增加 block table、metadata、寻址与 kernel 调度开销，并可能降低连续访存效率。大 page 相反。最优值依赖 context 分布、prefix reuse 与 backend kernel。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演短请求占多数时大 page 浪费明显；超长上下文中 page 太小又会让 page table 和 gather 变重。

### 建议实验

构造共享 system prompt 与随机 prompt 两组流量，对比 prefix cache hit、TTFT、KV 占用与吞吐。

### 观测指标

- 先手算每 token KV bytes，再估算给定并发与上下文长度的总占用。
- 区分容量优化、带宽优化与复用优化：它们解决的瓶颈不同。
- 测 prefix hit、page waste、eviction/preemption，并观察对 TTFT/TPOT 的作用。
- 围绕“KV block/page size 为什么不能无限小？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 只根据显存碎片选 page size
- ✗ 不进行 end-to-end TTFT/TPOT 测试。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 只根据显存碎片选 page size
- ✗ 不进行 end-to-end TTFT/TPOT 测试。

## 8. 追问链

- → Prefix cache 命中粒度如何受 page size 影响？
- → 不同 head_dim 会改变最优值吗？
- → 如何做 sweep？

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

- [Q013 PagedAttention 到底解决了什么？](q013-pagedattention-kv.md)
- [Q015 什么叫 KV Cache 的 Internal Fragmentation？](q015-fragmentation-kv.md)
- [Q028 KV Cache 不够时应该 Swap、Recompute 还是 Reject？](../03-batching-scheduling/q028-preemption-kv.md)
- [Q076 MLA 与 GQA 谁更省 KV Cache？](../08-moe-mla-codesign/q076-mla-gqa-kv.md)
- [Q085 TensorRT-LLM 的 KV Cache system 有什么特点？](../09-serving-runtimes/q085-tensorrt-llm-kv.md)

---

[← Q013](q013-pagedattention-kv.md) · [02 KV Cache 与 Attention](index.md) · [Q015 →](q015-fragmentation-kv.md)
