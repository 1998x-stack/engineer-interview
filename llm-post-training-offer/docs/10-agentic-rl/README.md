# 第 10 章 · Agentic RL 与系统设计

> 长程 MDP、tool calling、credit、reward、项目答辩

## 本章目标

**MDP 视角**：Agent 的 state/action/observation/horizon 比单轮文本任务复杂，环境本身是训练系统的一部分。

**reward 视角**：终局成功、过程进展、工具成本、无效动作与安全约束要分层，而不是堆成一个随意加权的标量。

**项目答辩视角**：高级回答必须能把算法、环境、系统和 ablation 串成一条研究决策链。

## 回答框架

**定义 state/action/observation/reward → horizon/credit → tool/environment → 系统 → 评测与安全约束**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q091 · 公开真题：什么是 Agentic RL？与单轮 reasoning RL 的状态空间有何不同？](q091-agentic-rl-state-space.md) | 公开真题 | L3 |  |
| [Q092 · 公开真题：Agentic RL 的 credit assignment 怎么做？](q092-agentic-credit-assignment.md) | 公开真题 | L4 |  |
| [Q093 · 公开真题：Tool Calling / Function Calling 数据怎么构造？](q093-tool-calling-data.md) | 公开真题 | L3 |  |
| [Q094 · Agent reward 应如何设计？](q094-agent-reward-design.md) | 系统设计 | L4 |  |
| [Q095 · 如何防止 Agent 为了 reward 无限调用工具或重复搜索？](q095-agent-tool-loop-hacking.md) | 系统设计 | L3 |  |
| [Q096 · Multi-turn RL 与 single-turn RL 最大区别是什么？](q096-multi-turn-vs-single-turn-rl.md) | 原理推导 | L3 |  |
| [Q097 · 公开真题：长程任务为什么可能选 GRPO 而不是 PPO？](q097-long-horizon-grpo-vs-ppo.md) | 公开真题 | L4 |  |
| [Q098 · 如何给 Agent 过程打 reward，而不把探索路径写死？](q098-agent-process-reward.md) | 系统设计 | L4 |  |
| [Q099 · 系统设计题：如果让你做一个 70B reasoning model 的完整 Post-Training pipeline？](q099-70b-post-training-pipeline.md) | 系统设计 | L5 |  |
| [Q100 · 终极项目题：为什么你的项目选 GRPO/DAPO/GSPO，而不是 PPO/DPO？](q100-algorithm-choice-project-defense.md) | 公开真题 | L5 | 🔥 |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| 成功率高但工具调用次数暴涨 | cost hacking | step cost + duplicate detection + budget |
| 长程任务失败集中在早期步骤 | credit/plan failure | trajectory slicing + intermediate progress verifier |
| tool error 后循环 | termination/recovery policy 缺失 | 明确 retry budget、fallback 与 stop condition |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：在环境交互中优化长程任务成功、效率与安全
- **Unit of optimization**：state-action-observation trajectory
- **主要统计偏差**：long-horizon credit、environment noise、tool hacking
- **系统载体**：agent runtime + tools + environment + RL trainer
- **规模化变量**：environment latency、steps/trajectory、tool budget

### 本章必须会看的指标

- `task success`
- `steps/trajectory`
- `tool calls`
- `invalid-action rate`
- `retry rate`
- `latency/cost`
- `environment failure rate`
- `long-horizon success`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q100。

### 章节级案例

假设 agent 需要搜索、代码执行和结构化 API，多轮最长 30 steps；最终成功率稀疏且工具调用有真实成本。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

