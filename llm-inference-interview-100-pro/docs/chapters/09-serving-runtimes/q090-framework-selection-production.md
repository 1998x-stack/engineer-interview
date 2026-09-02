---
id: Q090
title: "如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？"
chapter: "vLLM / SGLang / TensorRT-LLM"
difficulty: "★★★★★"
tags: ["framework-selection", "production"]
source: "LLM_Inference_Interview_100_2026.pdf"
edition: "2026.09"
---

# Q090｜如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？

> **定位**：vLLM / SGLang / TensorRT-LLM · **难度**：★★★★★  
> **关键词**：`framework-selection` · `production`

## 30 秒面试回答

> 建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的 Goodput/成本。先排除 feature gap，再 benchmark Pareto frontier。

## 1. 面试官到底在考什么

- 这道题不是考名词定义，而是看你能否从系统资源出发解释：建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的
Goodput/成本。先排除 feature gap，再 benchmark Pareto frontier。
- 面试中应先给结论，再给成本模型/瓶颈，再给适用边界。只背框架参数通常拿不到高分。

### 回答结构建议

1. **先下结论**：20-30 秒说清核心瓶颈或机制。
2. **给成本模型**：至少写一个与显存、带宽、计算或通信相关的量化表达。
3. **说边界**：明确在什么 batch/context/topology/SLO 条件下成立。
4. **给证据**：说明会看哪些 metrics、profiler 或 controlled experiment。
5. **给反例**：解释何时这个优化可能没有收益甚至负优化。

## 2. 关键公式 / 成本模型

公式不要只比较峰值 tokens/s；至少比较 SLO-constrained goodput 与 $/M token。

> **使用公式的原则**：先做一阶上界/下界估算，再用 profiler 校正有效带宽、kernel efficiency、通信 overlap 与排队时间。不要把理论峰值直接当线上值。

## 3. 深入原理：Know-Why

- 1. 建立决策矩阵：模型结构(Dense/MoE/MLA/VLM)、GPU/加速器、quant、prefix reuse、P/D、structured output、LoRA、运维成熟度、社区/模型支持，以及真实 workload 的 Goodput/成本。先排除 feature gap，再 benchmark Pareto
frontier。
- 把这一结论放进 Roofline / 内存容量 / 调度 / 通信四类模型中检查，确认瓶颈是否真的位于关键路径，而不是只优化了一个非关键算子。

### 进一步推导

- 将结论分别放进 **计算（FLOPs/Tensor Core）**、**内存（HBM/KV）**、**通信（NCCL/网络）**、**调度（queue/batch）** 四个视角检查。
- 问自己：优化前后究竟减少的是 **bytes、FLOPs、collective、kernel launch、排队还是重复计算**？如果没有减少关键路径上的成本，端到端加速通常有限。
- 对线上系统，最终验收应回到 **TTFT/TPOT/p99/Goodput/成本**，而不是只看单 kernel speedup。

## 4. 工程场景 / 现场推演

现场推演 Agent/prefix-heavy workload 可能偏好强 cache/scheduler；固定 NVIDIA low-precision fleet 可能偏好 TRT-
LLM；模型迭代快则生态适配很关键。

### 建议实验

准备统一 benchmark manifest，在 vLLM/SGLang/TensorRT-LLM 中保持模型 revision、量化、TP、流量分布与 SLO 一致；按 Goodput、p99、运维复杂度评分。

### 观测指标

- 技术选型固定模型/硬件/workload/SLO 后再 benchmark。
- 核对版本：scheduler、cache、quant、spec decode、PD 能力变化很快。
- 把易用性、模型覆盖、可观测性与升级成本纳入生产决策。
- 围绕“如果 vLLM、SGLang、TensorRT-LLM 三选一，你怎么做技术选型？”至少设计一个可证伪的 A/B 实验，明确控制变量与验收指标。

## 5. 边界条件与反例

避免把局部规律绝对化；必须说明 workload、并发、上下文长度、硬件拓扑、精度和 SLO，才能判断该结论是否成立。

- ✗ 选型表里没有“升级成本/可观测性/故障恢复”。

## 6. 生产排障 / 落地 Checklist

- [ ] 明确模型 revision、dtype/quantization 与 attention/backend。
- [ ] 固定硬件与物理拓扑，记录 driver/CUDA/runtime commit。
- [ ] 固定或记录 input/output length 与 arrival/concurrency 分布。
- [ ] 同时报 TTFT、TPOT/ITL、E2E、Throughput、Goodput、p95/p99。
- [ ] 将 GPU 指标与 scheduler/KV/queue 指标对齐到同一时间线。
- [ ] 对任何“优化”做 on/off A/B，且一次只改变一个关键变量。
- [ ] 检查收益是否只是从一种 SLO 转移到另一种 SLO。

## 7. 常见错误 / Gotchas

- ✗ 选型表里没有“升级成本/可观测性/故障恢复”。

## 8. 追问链

- → 如何做两周 PoC？
- → 谁负责模型新架构适配？
- → 如何避免 vendor/framework lock-in？

### 自我加压追问

- 如果硬件从 H100 换成 B200/A100，结论中哪些部分会变化？
- 如果 workload 从低并发 Chat 变成高并发 batch inference，最优点会怎么移动？
- 如果上下文长度增加 8 倍，容量瓶颈和带宽瓶颈分别怎样变化？
- 如何设计一个实验来证伪你自己的判断？

## 9. 面试官评分标准

- 及格：能给出正确概念和基本方向。
- 良好：能写出成本/显存/通信公式，能解释为什么。
- 优秀：能指出反例、适用边界，并能把问题落到 profiler、SLO 或真实系统配置。

CHAPTER 10

Benchmark、生产部署与系统设计把算法优化落到 SLO、Goodput、成本、监控、故障定位与容量规划。

本章题目 Q091 - Q100 · 共 10 题

本章学习目标
- 能设计可复现 benchmark。
- 能把 SLO、Goodput、成本和容量规划串起来。
- 能系统定位线上 30% 性能回归。

建议刷题方法：先用 30 秒回答自测，再遮住正文推导公式，最后只看“追问链”进行模拟面试。

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

### 版本敏感补充

三套 runtime 的 feature surface 都在快速扩张：选型文档必须记录版本/commit。建议把“模型支持、KV/prefix、quant、spec decode、P/D、MoE/MLA kernel、拓扑扩展、可观测性、升级成本”作为固定评分维度，而不是维护一张容易过期的绝对性能榜。

## 10.1 专家级深挖：把结论推到白板上

### 核心机制再抽象

三选一应先写 workload matrix，再给候选框架；对 Dense、MoE/MLA、长上下文、NVIDIA-only 优化、prefix-heavy agent 等 workload，最优选项可能不同。

### 白板推导

从本题给出的基础公式出发，对关键自变量做敏感性分析：分别让 runtime/version、scheduler policy、KV config、attention backend、quant backend、parallelism、compile/graph、spec decode 中一个变量变化，判断容量、带宽、计算或通信项如何变化。现场推导时重点说明数量级和主导项，而不是追求小数点精度。

### 做敏感性分析，而不是只背一个公式

面试现场建议把关键成本写成 $T=\max(T_{compute},T_{memory},T_{comm})+T_{sched/overhead}$ 或对应的容量模型，然后逐项回答：

- **哪个变量是一阶项？** 例如 context、batch、world size、bit-width 或 cache hit。
- **哪个变量只能改善局部项？** 局部加速若不在 critical path，会被 Amdahl 定律吃掉。
- **主导项何时切换？** 低并发与高并发、短上下文与长上下文、单机与跨节点经常处于不同 regime。
- **理论量与实测量如何对齐？** 用 effective bandwidth、achieved FLOP/s、exposed communication、实际 cache hit 替代理论峰值。

> **面试技巧**：写完公式后立即给一个“如果变量翻倍会怎样”的定性答案。真正懂系统的人通常能预测曲线形状，而不仅是记住一个点。

## 10.2 源码 / Runtime 视角

**典型执行路径**：API server → scheduler → KV manager → model runner → attention/GEMM backend → distributed executor。框架差异通常落在 scheduler/cache abstraction、kernel coverage、模型适配与运维能力。

- 所有结论绑定框架版本/commit；scheduler、KV、backend 的默认值可能跨版本变化。
- 把 feature support 与实际 fast path 区分：能运行不代表已命中最优 kernel/并行路径。

### 阅读源码时建议追的对象

1. **入口对象**：请求从 API/engine 进入后，在哪里被转成内部 request / sequence / batch。
2. **状态对象**：本题相关状态由谁持有，例如 KV block table、scheduler budget、quant scales、expert routing table。
3. **关键决策点**：哪个函数真正决定分配、调度、kernel/backend 或 collective。
4. **数据结构与布局**：shape、stride、page layout、packed format、rank placement 是否与论文抽象一致。
5. **fallback 路径**：feature“支持”时是否存在慢速 fallback；生产问题经常来自意外 fallback，而不是算法本身。

- 官方/上游实现参考：<https://docs.vllm.ai/en/stable/>
- 官方/上游实现参考：<https://nvidia.github.io/TensorRT-LLM/>
- 官方/上游实现参考：<https://github.com/sgl-project/sglang>

## 10.3 Benchmark Lab：如何把本题变成可复现实验

### 实验目标

验证本题的核心判断是否在目标硬件和 workload 上成立，而不是证明某个框架宣传数字。

### 推荐实验

同一 checkpoint、同一硬件、同一 tokenizer/sampling、同一 trace 做 apples-to-apples benchmark，并固定框架 commit。

### 控制变量

- 固定 checkpoint、tokenizer、sampling 参数、精度和模型 revision。
- 固定 GPU 型号、时钟/功耗策略、CUDA/driver、runtime commit 与物理拓扑。
- 预热后再采样；冷启动问题则单独建立 cold-start benchmark。
- 对随机 workload 固定 seed，并保存原始请求 trace，保证回归测试可重复。

### 自变量

runtime/version、scheduler policy、KV config、attention backend、quant backend、parallelism、compile/graph、spec decode。一次实验尽量只改变一个关键变量，复杂系统再用二维 sweep 验证交互项。

### 观测量

版本/commit、feature flags、TTFT/TPOT/Goodput、KV hit、compile/cold-start、GPU/CPU overhead。此外保存 profiler trace 与原始 per-request 数据，不只保存聚合平均值。

### 验收方式

- 先验证机制指标：例如 HBM bytes 是否下降、cache hit 是否提高、collective 是否被 overlap。
- 再验证端到端指标：TTFT/TPOT/Goodput/成本是否改善。
- 若机制指标改善但 E2E 不变，使用 Amdahl 分析剩余 critical path；不要继续盲调同一优化。

## 10.4 资深面试进阶：从“会答”到“会做系统”

高级回答以版本化架构与 workload matrix 为中心，能区分“feature support”“fast path”“运维成熟度”。

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
- [TensorRT-LLM 文档](https://nvidia.github.io/TensorRT-LLM/)

## 12. 相关题目

- [Q084 TensorRT-LLM 和 vLLM 怎么选？](q084-framework-selection-trtllm-vllm.md)
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](../10-production-system-design/q100-debugging-production-systematic.md)
- [Q029 为什么生产系统应该优化 Goodput，而不是最高 Throughput？](../03-batching-scheduling/q029-goodput-production.md)
- [Q089 为什么模型刚启动时延迟明显更高？](q089-cold-start-startup.md)
- [Q088 Structured Output 为什么会影响推理性能？](q088-structured-output-fsm.md)

---

[← Q089](q089-cold-start-startup.md) · [09 vLLM / SGLang / TensorRT-LLM](index.md) · [Q091 →](../10-production-system-design/q091-benchmark-serving.md)
