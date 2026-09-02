---
id: Q099
title: "系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？"
chapter: "Benchmark、生产部署与系统设计"
difficulty: "★★★★★"
tags: ["system-design", "H100", "70B"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q099｜系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？

> **定位**：Benchmark、生产部署与系统设计 · **难度**：★★★★★  
> **关键词**：`system-design` · `H100` · `70B`

## 30 秒面试回答

> 先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡；候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace 比较 Goodput、p99 与成本。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡；候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace 比较 Goodput、p99 与成本。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式 M_weights≈params×bytes；M_KV 用 Q11 公式；capacity=min(compute_capacity,KV_capacity,SLO_capacity)。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 先定义模型 dtype、输入/输出分布和 SLO，再算权重+KV。BF16 70B 仅权重约 140GB，需要至少跨卡
- 2. 候选可比较 TP=2×4 replicas、TP=4×2 replicas、FP8/INT4 后更小 TP 等。节点内 NVLink 适合 TP，最终用真实 trace
比较 Goodput、p99 与成本。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演高 QPS Chat 通常优先更多 replica；极低 latency 单请求可能使用更高 TP。若长 context，KV 容量可能决定
TP/replica 方案。

### 建议实验

先按权重+KV+workspace 做容量上界，再比较 TP=2×4 replicas 与 TP=4×2 replicas；最终以真实 Chat workload 的 Goodput/SLO 选型。

### 观测指标

- 使用真实 input/output/arrival 分布，报告 p50/p95/p99。
- 容量规划同时考虑 weights、KV、workspace、graph memory 与冗余。
- 性能回归先分解 queue/TTFT/TPOT，再逐层二分定位。
- 围绕“系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 直接答 TP=8
- ✗ 没有 SLO、长度分布和 dtype 就无法唯一决策。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 直接答 TP=8
- ✗ 没有 SLO、长度分布和 dtype 就无法唯一决策。

## 8. 追问链

- → 如果换 FP8 呢？
- → 如果平均 input 32K 呢？
- → 如果需要 99.9% TTFT<1s 呢？

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

把所有局部优化放到 SLO、容量、成本、可观测性与故障证据链中。

- **框架视角**：把本题放回 scheduler、KV manager、executor、kernel 与 distributed runtime 的完整路径，而不是孤立理解单个开关。
- **评估视角**：统一比较 latency distribution、Goodput 与资源成本；对长上下文和高并发单独建 workload bucket。
- **维护视角**：记录 runtime commit 和 feature flags。像 scheduler、KV swapping、quant backend 这类细节可能在大版本间变化。

## 10.1 专家级深挖：把结论推到白板上

### 核心机制再抽象

8×H100 70B 设计先列 SLO、长度/并发、dtype、是否量化，再算权重+KV+workspace；然后比较 TP2×4 replica、TP4×2 replica 等候选，以 Goodput 与容错做选择。

### 白板推导

BF16 70B 权重约 140GB；如果 TP=2，每 rank 仅权重约 70GB，80GB H100 留给 KV/workspace 的空间很紧。FP8/4-bit 会显著改变候选拓扑。

### 做敏感性分析，而不是只背一个公式

面试现场建议把关键成本写成 $T=\max(T_{compute},T_{memory},T_{comm})+T_{sched/overhead}$ 或对应的容量模型，然后逐项回答：

- **哪个变量是一阶项？** 例如 context、batch、world size、bit-width 或 cache hit。
- **哪个变量只能改善局部项？** 局部加速若不在 critical path，会被 Amdahl 定律吃掉。
- **主导项何时切换？** 低并发与高并发、短上下文与长上下文、单机与跨节点经常处于不同 regime。
- **理论量与实测量如何对齐？** 用 effective bandwidth、achieved FLOP/s、exposed communication、实际 cache hit 替代理论峰值。

> **面试技巧**：写完公式后立即给一个“如果变量翻倍会怎样”的定性答案。真正懂系统的人通常能预测曲线形状，而不仅是记住一个点。

## 10.2 源码 / Runtime 视角

**典型执行路径**：Traffic → gateway → queue/admission → replica/router → engine → GPU → telemetry。生产问题必须沿请求级、调度级、GPU/网络级证据链定位。

- 所有监控统一到 request_id、model_revision、engine_revision 与 worker/rank，便于跨层 RCA。
- 容量实验必须包含 burst、长尾长度和故障注入，不只测稳态均匀流量。

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

把 TP2×4 replicas、TP4×2、TP8×1 三套候选都跑真实 trace；比较单请求 TPOT、总 Goodput、故障域和空闲显存。

### 控制变量

- 固定 checkpoint、tokenizer、sampling 参数、精度和模型 revision。
- 固定 GPU 型号、时钟/功耗策略、CUDA/driver、runtime commit 与物理拓扑。
- 预热后再采样；冷启动问题则单独建立 cold-start benchmark。
- 对随机 workload 固定 seed，并保存原始请求 trace，保证回归测试可重复。

### 自变量

traffic trace、SLO、replica count、parallelism、autoscaling、admission、cache、failure mode。一次实验尽量只改变一个关键变量，复杂系统再用二维 sweep 验证交互项。

### 观测量

p50/p95/p99、Goodput、queue、GPU/KV utilization、errors/retries、cost/token、availability。此外保存 profiler trace 与原始 per-request 数据，不只保存聚合平均值。

### 验收方式

- 先验证机制指标：例如 HBM bytes 是否下降、cache hit 是否提高、collective 是否被 overlap。
- 再验证端到端指标：TTFT/TPOT/Goodput/成本是否改善。
- 若机制指标改善但 E2E 不变，使用 Amdahl 分析剩余 critical path；不要继续盲调同一优化。

## 10.4 资深面试进阶：从“会答”到“会做系统”

高级回答以 SLO、真实 trace、故障域和单位成本为约束，所有局部优化最终回到 Goodput/成本。

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
- [NVIDIA H100 官方规格](https://www.nvidia.com/en-us/data-center/h100/)

## 12. 相关题目

- [Q060 一个 671B MoE 模型如何做多节点部署规划？](../06-distributed-inference/q060-moe-system-design.md)
- [Q098 生产 LLM Server 最重要的监控指标有哪些？](q098-observability-metrics.md)
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](q100-debugging-production-systematic.md)
- [Q097 线上发生 KV Cache OOM，你怎么处理？](q097-oom-kv-operations.md)
- [Q096 LLM Serving 如何做 Admission Control 和 Autoscaling？](q096-admission-control-autoscaling.md)

---

[← Q098](q098-observability-metrics.md) · [10 Benchmark、生产部署与系统设计](index.md) · [Q100 →](q100-debugging-production-systematic.md)
