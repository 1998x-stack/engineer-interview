# 第 6 章 · DAPO / GSPO

> 长 CoT RL 的 failure modes、sequence-level optimization、MoE

## 本章目标

**failure-driven 视角**：DAPO/GSPO 不应背成名词列表；每个修改都要对应 entropy、无效 group、长度 weighting、ratio 噪声或 MoE mismatch。

**粒度视角**：token、sequence、group 是不同 normalization / importance / loss aggregation 粒度，改变粒度会改变估计量性质。

**规模化视角**：前沿 RL 算法必须与 rollout 系统、MoE routing、policy freshness 一起理解。

## 回答框架

**先说 GRPO failure → 对应 DAPO/GSPO 修改 → 粒度与公式 → 训练现象 → 何时值得使用**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q051 · 公开真题：DAPO 相比 GRPO 做了哪些核心改进？](q051-dapo-vs-grpo.md) | 公开真题 | L3 | 🔥 |
| [Q052 · 为什么 DAPO 需要 Clip-Higher？](q052-dapo-clip-higher.md) | 原理推导 | L4 |  |
| [Q053 · 公开真题：Dynamic Sampling 为什么有效？](q053-dapo-dynamic-sampling.md) | 公开真题 | L3 |  |
| [Q054 · 长 CoT 下 sequence-level normalization 为什么可能产生长度偏差？](q054-long-cot-length-normalization.md) | 原理推导 | L4 |  |
| [Q055 · Token-level Policy Gradient Loss 解决什么？](q055-token-level-policy-gradient.md) | 原理推导 | L4 |  |
| [Q056 · Overlong Reward Shaping 为什么比硬截断惩罚更稳？](q056-overlong-reward-shaping.md) | 原理推导 | L3 |  |
| [Q057 · 公开真题：GSPO 与 GRPO 的核心区别是什么？](q057-gspo-vs-grpo.md) | 公开真题 | L4 | 🔥 |
| [Q058 · GSPO 为什么需要 1/|y| 的长度归一化？](q058-gspo-length-normalization.md) | 原理推导 | L4 |  |
| [Q059 · 公开真题：为什么 GSPO 对 MoE routing mismatch 更友好？](q059-gspo-moe-routing.md) | 公开真题 | L5 |  |
| [Q060 · DAPO 与 GSPO 应如何比较？它们不是同一层面的改进](q060-dapo-vs-gspo.md) | 系统设计 | L5 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| entropy 快速塌缩 | 正向探索受限 | Clip-Higher/采样温度/难度调度 |
| 有效 group 比例低 | 全对/全错过多 | Dynamic Sampling |
| 长序列训练不稳定 | length weighting / ratio noise | 检查 token-vs-sequence normalization，考虑 GSPO |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：修复 long-CoT/大规模 RL 中的稳定性与粒度失配
- **Unit of optimization**：token aggregation 或 sequence ratio
- **主要统计偏差**：length weighting、entropy collapse、MoE mismatch
- **系统载体**：高吞吐 rollout + sequence/token statistics
- **规模化变量**：长序列 KV cache、有效样本、路由/后端一致性

### 本章必须会看的指标

- `entropy`
- `positive/negative clip fraction`
- `effective sample rate`
- `response length p50/p95`
- `sequence ratio`
- `routing mismatch`
- `training stability`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q051, Q057。

### 章节级案例

假设模型平均 CoT 从 1k 增长到 8k tokens，并且是 MoE；原先 GRPO 训练开始出现 entropy 下降、ratio 尾部异常与吞吐恶化。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

