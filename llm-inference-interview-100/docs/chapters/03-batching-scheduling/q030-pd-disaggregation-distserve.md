---
id: Q030
title: "什么是 Prefill–Decode Disaggregation？"
chapter: "Batching 与 Scheduling"
difficulty: "★★★★★"
tags: ["PD-disaggregation", "DistServe"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q030｜什么是 Prefill–Decode Disaggregation？

> **定位**：Batching 与 Scheduling · **难度**：★★★★★  
> **关键词**：`PD-disaggregation` · `DistServe`

## 30 秒面试回答

> 把 Prefill 和 Decode 放到不同 GPU pool，分别选择并行策略和容量，避免 compute-heavy 与 latency-sensitive memory-heavy 阶段互相干扰；关键代价是生成后的 KV 必须高效传输到 Decode 节点，因此 network/topology 与 KV transfer overlap 成为核心。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：把 Prefill 和 Decode 放到不同 GPU pool，分别选择并行策略和容量，避免 compute-heavy 与 latency-sensitive memory-heavy 阶段互相干扰；关键代价是生成后的 KV 必须高效传输到 Decode 节点，因此 network/topology 与 KV transfer overlap 成为核心。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 T_total≈T_queue_p+T_prefill+T_KV_transfer+T_queue_d+T_decode。只有 T_KV_transfer 可被隐藏/摊薄时才值得。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 把 Prefill 和 Decode 放到不同 GPU pool，分别选择并行策略和容量，避免 compute-heavy 与 latency-sensitive
memory-heavy 阶段互相干扰
- 2. 关键代价是生成后的 KV 必须高效传输到 Decode 节点，因此 network/topology 与 KV transfer overlap 成为核心。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 Prefill pool 可用高吞吐 TP/CP，Decode pool 可按更大 replication/EP 优化；两池按输入/输出负载独立扩容。

### 建议实验

测量单请求 KV 大小与网络有效带宽，估算 KV transfer 时间；再比较 colocated 与 P/D split 的 TTFT/TPOT/Goodput，验证转移是否进入关键路径。

### 观测指标

- 记录 queue time、running/waiting requests、batched tokens 与 preemption。
- 对长短请求分桶，观察 head-of-line blocking 与 tail latency。
- 所有吞吐提升都用 Goodput/SLO 重新验收。
- 围绕“什么是 Prefill–Decode Disaggregation？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

P/D 分离消除资源干扰但新增 KV 网络传输、跨池排队与部署复杂度；不是所有规模都值得。

- ✗ 只看到“分离就更快”
- ✗ 若网络慢或 prompt 很短，KV transfer 可能吞掉全部收益。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 只看到“分离就更快”
- ✗ 若网络慢或 prompt 很短，KV transfer 可能吞掉全部收益。

## 8. 追问链

- → KV 如何跨节点传？
- → P/D pool 比例如何容量规划？
- → 什么 workload 不适合 disaggregation？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 04

CUDA、Attention Kernel 与 Runtime
从 IO-aware Attention、Kernel Fusion 到 CUDA Graph，用 profiler 定位真正瓶颈。

本章题目 Q031 - Q040 · 共 10 题

本章学习目标
- 能区分 IO、compute、launch 与 runtime overhead。
- 会用 Nsight 设计证据链。
- 理解 Attention/GEMM kernel 的硬件适配。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

### 高分答案的额外特征

- 能把“机制正确”与“线上收益”分开讨论；
- 会主动声明假设，而不是用绝对句式；
- 能现场估算数量级，并说明误差来源；
- 能提出可复现实验和可观测指标；
- 能指出当前框架版本可能改变实现细节。

## 10. 2026 工程扩展（外部资料）

> 本节是基于 2026 年公开框架/论文的补充，不属于 PDF 原始正文；具体 feature/status 应以目标版本文档为准。

把 scheduler 看作受 KV、token budget 与 SLO 约束的在线资源分配器。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

### 版本敏感补充

当前 TensorRT-LLM 的 disaggregated serving 文档已经把 context/prefill 与 generation/decode 实例分开，并专门提供 KV Cache Exchange/Transmission 机制；这说明 P/D 分离已从论文概念进入主流 runtime 的实际部署能力，但网络拓扑和 KV transfer overlap 仍是成败关键。

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)
- [DistServe / Goodput 与 P/D](https://www.usenix.org/conference/osdi24/presentation/zhong-yinmin)
- [TensorRT-LLM 文档](https://nvidia.github.io/TensorRT-LLM/)
- [TensorRT-LLM Disaggregated Serving](https://nvidia.github.io/TensorRT-LLM/features/disagg-serving.html)

## 12. 相关题目

- [Q029 为什么生产系统应该优化 Goodput，而不是最高 Throughput？](q029-goodput-production.md)
- [Q028 KV Cache 不够时应该 Swap、Recompute 还是 Reject？](q028-preemption-kv.md)
- [Q027 如何解决调度中的 Starvation？](q027-fairness-starvation.md)
- [Q026 FCFS 和 Cache-aware Scheduling 怎么选？](q026-scheduling-cache-aware.md)
- [Q025 Scheduler 中的 max_num_batched_tokens 本质是什么？](q025-vllm-token-budget.md)

---

[← Q029](q029-goodput-production.md) · [03 Batching 与 Scheduling](index.md) · [Q031 →](../04-kernel-runtime/q031-flashattention-io.md)
