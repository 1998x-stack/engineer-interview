---
id: Q028
title: "KV Cache 不够时应该 Swap、Recompute 还是 Reject？"
chapter: "Batching 与 Scheduling"
difficulty: "★★★★★"
tags: ["preemption", "KV"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q028｜KV Cache 不够时应该 Swap、Recompute 还是 Reject？

> **定位**：Batching 与 Scheduling · **难度**：★★★★★  
> **关键词**：`preemption` · `KV`

## 30 秒面试回答

> 这是“带宽换计算换排队”的选择。Swap 把 KV 移到 CPU/远端，受传输延迟影响；Recompute 丢弃 KV 后重做 Prefill，消耗 GPU compute；Reject/queue 用 admission control 保证稳定。现代框架还可用分层缓存、context parallel 或更积极的 watermark。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：这是“带宽换计算换排队”的选择。Swap 把 KV 移到 CPU/远端，受传输延迟影响；Recompute 丢弃 KV 后重做 Prefill，消耗 GPU compute；Reject/queue 用 admission control 保证稳定。现代框架还可用分层缓存、context parallel 或更积极的 watermark。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式比较 T_swap = bytes/BW_link 与 T_recompute = prefill_compute_time。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 这是“带宽换计算换排队”的选择。Swap 把 KV 移到 CPU/远端，受传输延迟影响
- 2. Recompute 丢弃 KV 后重做 Prefill，消耗 GPU compute
- 3. Reject/queue 用 admission control 保证稳定。现代框架还可用分层缓存、context parallel 或更积极的 watermark。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 PCIe 较慢、prompt 不长时 recompute 可能比 swap 更好；超长共享 prefix 则 offload/cache 可能值得。

### 建议实验

用 Poisson/突发流量分别压测，比较 FCFS、cache-aware、chunked prefill 或不同 token budget。

### 观测指标

- 记录 queue time、running/waiting requests、batched tokens 与 preemption。
- 对长短请求分桶，观察 head-of-line blocking 与 tail latency。
- 所有吞吐提升都用 Goodput/SLO 重新验收。
- 围绕“KV Cache 不够时应该 Swap、Recompute 还是 Reject？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 认为 swap 永远优于 recompute
- ✗ 忽略 vLLM V1 已移除旧式 GPU↔CPU KV swapping 路径这一版本差异。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 认为 swap 永远优于 recompute
- ✗ 忽略 vLLM V1 已移除旧式 GPU↔CPU KV swapping 路径这一版本差异。

## 8. 追问链

- → 如何做 admission control？
- → 何时预留 KV watermark？
- → HiCache 属于哪类策略？

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

把 scheduler 看作受 KV、token budget 与 SLO 约束的在线资源分配器。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 10.1 专家级深挖：把结论推到白板上

### 核心机制再抽象

Swap、recompute、reject 的选择取决于 PCIe/网络传输成本、prefill 重算成本和 SLO；现代引擎还可能采用分层 KV cache 或直接 admission control。

### 白板推导

从本题给出的基础公式出发，对关键自变量做敏感性分析：分别让 arrival rate、input/output 分布、max running requests、token budget、prefill chunk、priority/fairness policy 中一个变量变化，判断容量、带宽、计算或通信项如何变化。现场推导时重点说明数量级和主导项，而不是追求小数点精度。

### 做敏感性分析，而不是只背一个公式

面试现场建议把关键成本写成 $T=\max(T_{compute},T_{memory},T_{comm})+T_{sched/overhead}$ 或对应的容量模型，然后逐项回答：

- **哪个变量是一阶项？** 例如 context、batch、world size、bit-width 或 cache hit。
- **哪个变量只能改善局部项？** 局部加速若不在 critical path，会被 Amdahl 定律吃掉。
- **主导项何时切换？** 低并发与高并发、短上下文与长上下文、单机与跨节点经常处于不同 regime。
- **理论量与实测量如何对齐？** 用 effective bandwidth、achieved FLOP/s、exposed communication、实际 cache hit 替代理论峰值。

> **面试技巧**：写完公式后立即给一个“如果变量翻倍会怎样”的定性答案。真正懂系统的人通常能预测曲线形状，而不仅是记住一个点。

## 10.2 源码 / Runtime 视角

**典型执行路径**：Arrival queue → admission → scheduler → token budget → prefill/decode mixing → preemption。调度器优化的是多请求竞争条件下的关键路径，而不是单请求 kernel 峰值。

- 调度日志至少要能恢复每轮 selected requests、scheduled tokens、preemption 和 queue age。
- 使用 open-loop 流量测试 scheduler；closed-loop 客户端会把系统变慢自动转化为更低 offered load，掩盖过载。

### 阅读源码时建议追的对象

1. **入口对象**：请求从 API/engine 进入后，在哪里被转成内部 request / sequence / batch。
2. **状态对象**：本题相关状态由谁持有，例如 KV block table、scheduler budget、quant scales、expert routing table。
3. **关键决策点**：哪个函数真正决定分配、调度、kernel/backend 或 collective。
4. **数据结构与布局**：shape、stride、page layout、packed format、rank placement 是否与论文抽象一致。
5. **fallback 路径**：feature“支持”时是否存在慢速 fallback；生产问题经常来自意外 fallback，而不是算法本身。

- 对版本敏感的实现细节，以目标 runtime 的官方文档、release note 与源码 commit 为准。

## 10.3 Benchmark Lab：如何把本题变成可复现实验

### 实验目标

验证本题的核心判断是否在目标硬件和 workload 上成立，而不是证明某个框架宣传数字。

### 推荐实验

用 open-loop Poisson/trace-driven arrival，而不是只做 closed-loop concurrency；逐步升高 offered load 找到 SLO knee point。

### 控制变量

- 固定 checkpoint、tokenizer、sampling 参数、精度和模型 revision。
- 固定 GPU 型号、时钟/功耗策略、CUDA/driver、runtime commit 与物理拓扑。
- 预热后再采样；冷启动问题则单独建立 cold-start benchmark。
- 对随机 workload 固定 seed，并保存原始请求 trace，保证回归测试可重复。

### 自变量

arrival rate、input/output 分布、max running requests、token budget、prefill chunk、priority/fairness policy。一次实验尽量只改变一个关键变量，复杂系统再用二维 sweep 验证交互项。

### 观测量

queue time、batch tokens、running/waiting requests、preemption、TTFT/TPOT p99、Goodput。此外保存 profiler trace 与原始 per-request 数据，不只保存聚合平均值。

### 验收方式

- 先验证机制指标：例如 HBM bytes 是否下降、cache hit 是否提高、collective 是否被 overlap。
- 再验证端到端指标：TTFT/TPOT/Goodput/成本是否改善。
- 若机制指标改善但 E2E 不变，使用 Amdahl 分析剩余 critical path；不要继续盲调同一优化。

## 10.4 资深面试进阶：从“会答”到“会做系统”

高级回答应给出 throughput–latency–fairness 三方权衡，并说明过载区间的 admission/preemption 策略。

### 面试官可能改变条件

- **硬件变化**：A100/H100/B200、PCIe/SXM、单机/跨节点后，瓶颈是否迁移？
- **流量变化**：interactive chat、RAG、长 CoT、offline batch 的最优配置是否仍一样？
- **模型变化**：Dense → MoE、MHA → GQA/MLA、BF16 → FP8/INT4 后，哪个成本项被改变？
- **SLO 变化**：若从“最大吞吐”改成“p99 TPOT < X ms”，你的答案需要怎样重排优先级？
- **故障变化**：一张卡变慢、cache miss、NCCL 抖动或 cold start 时，哪些观测指标最先异常？

### 一段高质量 Senior 答案应包含

1. **Assumption**：先明确 batch/context/topology/SLO。
2. **Model**：写出一阶成本模型或数据流。
3. **Bottleneck**：指出主导资源并说明为什么。
4. **Intervention**：提出优化，同时说明它具体减少了 bytes/FLOPs/communication/queue 中哪一项。
5. **Trade-off**：说明内存、质量、公平性、复杂度或尾延迟代价。
6. **Evidence**：给出 profiler/metrics 和可证伪 A/B。
7. **Boundary**：明确何时结论失效。

### 代码审查 / 设计评审追问

- 如果让你在 runtime 源码里实现或修改这一机制，你首先会找哪个 abstraction？
- 如何写一个单元测试验证“语义正确”，再写一个 benchmark 验证“性能正确”？
- 如何避免优化只对单一 shape 有效，却让真实请求分布退化？
- 如何把本题相关指标加入线上 dashboard，并设置回归告警？

## 11. 延伸阅读

- [vLLM 官方文档](https://docs.vllm.ai/en/stable/)

## 12. 相关题目

- [Q015 什么叫 KV Cache 的 Internal Fragmentation？](../02-kv-cache-attention/q015-fragmentation-kv.md)
- [Q014 KV block/page size 为什么不能无限小？](../02-kv-cache-attention/q014-kv-page-size.md)
- [Q013 PagedAttention 到底解决了什么？](../02-kv-cache-attention/q013-pagedattention-kv.md)
- [Q076 MLA 与 GQA 谁更省 KV Cache？](../08-moe-mla-codesign/q076-mla-gqa-kv.md)
- [Q085 TensorRT-LLM 的 KV Cache system 有什么特点？](../09-serving-runtimes/q085-tensorrt-llm-kv.md)

---

[← Q027](q027-fairness-starvation.md) · [03 Batching 与 Scheduling](index.md) · [Q029 →](q029-goodput-production.md)
