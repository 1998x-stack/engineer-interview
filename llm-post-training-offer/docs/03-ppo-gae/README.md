# 第 3 章 · PPO / GAE / 经典 RLHF

> importance sampling、clip、critic、KL、GAE

## 本章目标

**策略梯度视角**：PPO 的每个部件都对应一个问题：ratio 处理采样分布、advantage 降方差、clip 控制更新、KL 锚定语言先验。

**LLM 映射**：state 是 prompt+prefix，action 是 token，episode 是 response；终局 reward 如何变成 token gradient 是核心 credit 问题。

**系统视角**：不要把 PPO 只看成 loss；critic/RM/ref、rollout 和 learner 的资源布局决定它是否能实际跑起来。

## 回答框架

**先写公式 → 逐项解释 → 正/负 advantage 或 bias/variance 情况 → 映射 LLM token → 系统代价**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q021 · 公开真题：PPO 是 on-policy 还是 off-policy？为什么答案不能只说一个词？](q021-ppo-on-vs-off-policy.md) | 公开真题 | L2 | 🔥 |
| [Q022 · 公开真题：为什么 PPO 需要 Importance Sampling？](q022-ppo-importance-sampling.md) | 公开真题 | L2 |  |
| [Q023 · PPO clipped surrogate objective 怎么写？min 到底在做什么？](q023-ppo-clipped-objective.md) | 高频题 | L3 | 🔥 |
| [Q024 · 公开真题：Advantage 为正/负时 clip 分别限制什么？](q024-ppo-clip-positive-negative-advantage.md) | 公开真题 | L3 | 🔥 |
| [Q025 · PPO 为什么需要 Critic / Value Model？](q025-ppo-critic-value-model.md) | 高频题 | L2 |  |
| [Q026 · 公开真题：GAE 如何计算？λ 控制什么？](q026-gae-derivation-lambda.md) | 公开真题 | L3 | 🔥 |
| [Q027 · 为什么经典 PPO-RLHF 常说需要四个模型？](q027-ppo-four-models.md) | 高频题 | L2 | 🔥 |
| [Q028 · Reference Model 与 KL penalty 的本质作用是什么？](q028-reference-model-kl.md) | 原理推导 | L3 |  |
| [Q029 · KL 系数 β 太大或太小会怎样？如何自适应？](q029-adaptive-kl-beta.md) | 系统设计 | L2 |  |
| [Q030 · PPO 在 LLM 后训练中最大的工程问题是什么？](q030-ppo-engineering-cost.md) | 系统设计 | L3 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| KL 突增 | 步长、ratio、staleness 或 reward scale 异常 | 联查 LR/clip fraction/ratio tail/version |
| clip fraction 长期极高 | 更新过猛 | 减 LR/epoch，检查 advantage scale |
| critic loss 发散 | value target/scale/训练不稳 | 检查 reward normalization、value clip、mask |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：在 KL/信赖约束下做稳定的在线策略改进
- **Unit of optimization**：token/action + trajectory return
- **主要统计偏差**：advantage variance、critic bias、policy lag
- **系统载体**：actor/critic/RM/ref + rollout/learner
- **规模化变量**：rollout tokens、四角色显存、通信与同步

### 本章必须会看的指标

- `approx KL`
- `clip fraction`
- `ratio quantiles`
- `entropy`
- `value loss/explained variance`
- `grad norm`
- `data age`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q021, Q023, Q024, Q026, Q027。

### 章节级案例

假设 32B 模型使用 PPO 做 RLHF，训练出现 KL 抖动和 GPU 利用率不足；需要同时从目标函数与系统数据流定位。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

