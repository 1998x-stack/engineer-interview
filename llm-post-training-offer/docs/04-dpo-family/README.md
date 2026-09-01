# 第 4 章 · DPO 与 Offline Preference Optimization

> DPO 推导、offline shift、KTO/ORPO/SimPO

## 本章目标

**推导视角**：DPO family 的共同问题是如何把 preference 直接转成 policy 的相对概率约束。

**数据视角**：offline preference 只能覆盖采样它的旧分布，必须讨论 OOD、长度偏差、hard pair 与 label noise。

**选择视角**：是否需要在线探索、是否有可靠 reward、能否承担 rollout，是 DPO vs RL 的关键分界。

## 回答框架

**从 KL-RLHF 或 preference 数据开始 → 写目标 → 解释隐式 reward → offline 边界 → 与 online RL 比较**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q031 · DPO loss 怎么写？四个 log-prob 项各在做什么？](q031-dpo-loss.md) | 高频题 | L3 | 🔥 |
| [Q032 · DPO 如何从 KL-regularized RLHF 推导出来？](q032-dpo-derivation.md) | 原理推导 | L4 | 🔥 |
| [Q033 · 为什么 DPO 比 PPO 简单很多？](q033-why-dpo-simpler-than-ppo.md) | 高频题 | L2 |  |
| [Q034 · 公开真题：PPO 与 DPO 怎么选？](q034-ppo-vs-dpo.md) | 公开真题 | L3 | 🔥 |
| [Q035 · DPO 的 offline distribution shift 问题是什么？](q035-dpo-offline-distribution-shift.md) | 原理推导 | L3 |  |
| [Q036 · DPO 为什么也可能 overfit 或出现 length bias？](q036-dpo-overfit-length-bias.md) | 原理推导 | L3 |  |
| [Q037 · DPO 中 β 应如何理解？](q037-dpo-beta.md) | 原理推导 | L3 |  |
| [Q038 · KTO 与 DPO 的数据要求有何差异？](q038-kto-vs-dpo.md) | 高频题 | L2 |  |
| [Q039 · ORPO 为什么可以 reference-free？](q039-orpo-reference-free.md) | 高频题 | L2 |  |
| [Q040 · SimPO 相比 DPO 改了什么？为什么使用平均 log probability？](q040-simpo-average-logprob.md) | 高频题 | L3 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| preference loss 降但生成质量不升 | offline overfit / metric mismatch | held-out pair + generation eval |
| 回答越来越长 | length bias | length-controlled win rate；长度归一化/数据去偏 |
| KL/reference drift 过大 | beta 或 reference mismatch | 扫 beta；检查 tokenizer/checkpoint 一致性 |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：直接从离线偏好数据调整策略相对 reference 的隐式 reward
- **Unit of optimization**：chosen/rejected sequence
- **主要统计偏差**：offline distribution shift、length bias、pair noise
- **系统载体**：policy + reference logprob + preference dataset
- **规模化变量**：训练 token、reference inference/cache、数据覆盖

### 本章必须会看的指标

- `preference margin`
- `chosen/rejected logprob`
- `implicit reward gap`
- `reference KL`
- `length-controlled win-rate`
- `offline coverage`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q031, Q032, Q034。

### 章节级案例

假设你有 50 万 preference pairs，但无法持续在线 rollout；你需要证明 offline preference optimization 的收益与边界。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

