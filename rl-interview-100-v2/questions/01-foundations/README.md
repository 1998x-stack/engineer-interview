# 第一章 MDP / Bellman / DP / MC / TD

从 MDP、Bellman 与估计理论建立强化学习的坐标系。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q001](Q001-mdp-five-tuple.md) | 什么是 MDP？五元组分别代表什么？ | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q002](Q002-markov-property.md) | 一句话解释 Markov Property。 | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q003](Q003-discount-factor.md) | 为什么 Return 需要折扣因子 γ？ | ★★★★☆ | ★★☆☆☆ | 全方向 |
| [Q004](Q004-value-q-advantage.md) | V(s)、Q(s,a)、A(s,a) 有什么关系？ | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q005](Q005-bellman-expectation.md) | 推导 Bellman Expectation Equation。 | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q006](Q006-bellman-optimality.md) | Bellman Optimality 与 Bellman Expectation 有什么区别？ | ★★★★☆ | ★★★☆☆ | 全方向 |
| [Q007](Q007-dp-mc-td.md) | Dynamic Programming、Monte Carlo、TD 的区别？ | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q008](Q008-mc-vs-td.md) | MC 与 TD 各有什么优缺点？ | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q009](Q009-td-error.md) | TD Error 是什么？为什么重要？ | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q010](Q010-monte-carlo-estimation.md) | 手推一个 Monte Carlo 估计问题。 | ★★★★☆ | ★★★☆☆ | 研究/控制 |
| [Q011](Q011-n-step-return.md) | n-step Return 为什么连接了 MC 和 TD？ | ★★★★☆ | ★★★☆☆ | 全方向 |
| [Q012](Q012-on-vs-off-policy.md) | On-policy 与 Off-policy 的本质区别？ | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q013](Q013-importance-sampling.md) | Importance Sampling 是什么？RL 为什么需要它？ | ★★★★★ | ★★★★☆ | PPO/LLM-RL |
| [Q014](Q014-sarsa-vs-q-learning.md) | SARSA 与 Q-learning 有什么区别？ | ★★★★☆ | ★★★☆☆ | 全方向 |
| [Q015](Q015-exploration-exploitation.md) | Exploration 与 Exploitation 如何权衡？ | ★★★★★ | ★★★☆☆ | 游戏/机器人 |

## 本章建议阅读

- [Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

学完后应能从 **trajectory / return** 出发，自行推导到 Bellman、MC、TD、n-step 和 on/off-policy，而不是把这些概念记成互不相关的定义。

### 一条因果主线

```text
Sequential Decision Making
  → Markov State
  → Return G_t
  → V / Q / A
  → Bellman recursion
  → exact expectation (DP) / sampled return (MC) / bootstrap (TD)
  → n-step / TD(λ)
  → behavior policy vs target policy
  → importance sampling
```

### 面试分层

- **一面**：定义准确、公式会写、能比较 MC/TD、SARSA/Q-learning。
- **二面**：能解释 contraction、bias-variance、IS 高方差和 state 是否 Markov。
- **项目面**：能处理 terminal/truncated、reward scale、trajectory schema 和部分可观测。

### 本章手算要求

至少手算一次 3-state MDP 的 V/Q、一次 MC return、一次 TD error、一次 IS 估计。
