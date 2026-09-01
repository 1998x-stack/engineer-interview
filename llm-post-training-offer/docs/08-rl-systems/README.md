# 第 8 章 · RL 系统、Rollout 与分布式训练

> 数据流、吞吐、长尾、vLLM、FSDP/ZeRO、训推分离

## 本章目标

**workload 视角**：prefill、decode、forward/backward、all-gather/reduce-scatter 是完全不同的瓶颈，先 profile 再优化。

**资源视角**：峰值显存、通信量、tokens/s、GPU active ratio、queue latency、version lag 应一起监控。

**架构视角**：rollout/learner colocate 还是 disaggregate，本质是资源利用率与同步/陈旧度之间的权衡。

## 回答框架

**画数据流 → 标 workload → profile bottleneck → 资源/通信/同步 trade-off → 指标闭环**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q071 · 公开真题：一个完整 GRPO 数据流是什么？](q071-grpo-dataflow.md) | 公开真题 | L3 | 🔥 |
| [Q072 · 为什么 RL rollout 比 SFT teacher-forcing 贵？](q072-rollout-vs-teacher-forcing-cost.md) | 原理推导 | L2 |  |
| [Q073 · 公开真题：rollout 长尾为什么降低 GPU 利用率？](q073-rollout-tail-gpu-utilization.md) | 公开真题 | L3 |  |
| [Q074 · rollout 长尾有哪些工程解法？](q074-rollout-tail-solutions.md) | 系统设计 | L4 |  |
| [Q075 · vLLM 为什么适合 RL rollout？](q075-vllm-for-rollout.md) | 高频题 | L2 |  |
| [Q076 · 公开真题：FSDP 与 DDP 的核心区别？](q076-fsdp-vs-ddp.md) | 公开真题 | L3 |  |
| [Q077 · 公开真题：ZeRO-1/2/3 分别 shard 什么？](q077-zero-stages.md) | 公开真题 | L2 |  |
| [Q078 · 为什么 PPO/GRPO 系统显存比 SFT 更复杂？](q078-rl-memory-vs-sft.md) | 原理推导 | L3 |  |
| [Q079 · RL 训推分离如何设计？weight sync 的 trade-off 是什么？](q079-train-inference-disaggregation.md) | 系统设计 | L4 |  |
| [Q080 · 公开真题：TRL、verl、OpenRLHF 这类框架应该理解到什么程度？](q080-trl-verl-openrlhf.md) | 公开真题 | L3 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| GPU util 低且 p99 很高 | rollout straggler | continuous batching + length bucket + async |
| OOM 只发生在特定阶段 | KV/all-gather/activation 峰值 | 按阶段 profile peak memory |
| learner 空转等数据 | rollout throughput 不足 | 扩 rollout pool、提高 decode efficiency、平衡 placement |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：让 rollout、reward、learner 和权重同步形成高吞吐稳定闭环
- **Unit of optimization**：tokens/s、batch、model shard、version
- **主要统计偏差**：tail latency、OOM、通信瓶颈、staleness
- **系统载体**：inference engine + distributed trainer + scheduler
- **规模化变量**：GPU/节点拓扑、KV cache、network bytes/s

### 本章必须会看的指标

- `rollout tokens/s`
- `learner tokens/s`
- `GPU active ratio`
- `p95/p99 latency`
- `peak memory`
- `network bytes/s`
- `weight-sync time`
- `queue depth`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q071。

### 章节级案例

假设 64 张 GPU 上 rollout 与 learner 分池运行，生成长度重尾、权重同步昂贵；目标是提升 useful tokens/s 而不显著增加 policy lag。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

