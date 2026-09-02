# 第三章 Policy Gradient / Actor-Critic / PPO

从 score-function estimator 走到 GAE、TRPO 与 PPO，掌握现代 policy optimization 主线。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q029](Q029-value-vs-policy.md) | Value-based 与 Policy-based 的本质区别？ | ★★★★★ | ★★☆☆☆ | 全方向 |
| [Q030](Q030-policy-gradient-theorem.md) | 写出 Policy Gradient Theorem，并解释 log-derivative trick。 | ★★★★★ | ★★★★☆ | 全方向 |
| [Q031](Q031-reinforce.md) | REINFORCE 怎么来？最大缺点是什么？ | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q032](Q032-baseline-unbiasedness.md) | 为什么加 baseline 不改变 Policy Gradient 的期望？ | ★★★★★ | ★★★★☆ | 全方向 |
| [Q033](Q033-actor-critic.md) | Actor-Critic 为什么比 REINFORCE 更实用？ | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q034](Q034-a2c-vs-a3c.md) | A2C 与 A3C 有什么区别？ | ★★★★☆ | ★★★☆☆ | 游戏/分布式RL |
| [Q035](Q035-a3c-staleness.md) | A3C 异步训练为什么可能不收敛？ | ★★★★☆ | ★★★★☆ | 分布式RL |
| [Q036](Q036-gae.md) | GAE 是什么？λ 控制什么？ | ★★★★★ | ★★★★☆ | PPO/机器人/LLM-RL |
| [Q037](Q037-trpo-trust-region.md) | TRPO 为什么需要 Trust Region？ | ★★★★☆ | ★★★★☆ | PPO/研究 |
| [Q038](Q038-why-ppo.md) | 为什么提出 PPO？相比 TRPO 好在哪里？ | ★★★★★ | ★★★☆☆ | PPO/LLM-RL |
| [Q039](Q039-ppo-clipped-objective.md) | 写出 PPO Clipped Objective，并解释每一项。 | ★★★★★ | ★★★★☆ | PPO/LLM-RL |
| [Q040](Q040-ppo-ratio.md) | PPO 中 ratio 到底表示什么？ | ★★★★★ | ★★★☆☆ | PPO/LLM-RL |
| [Q041](Q041-ppo-is-vs-dqn.md) | 为什么 PPO 需要 Importance Sampling，而 DQN 不需要？ | ★★★★★ | ★★★★☆ | PPO/游戏 |
| [Q042](Q042-ppo-clip-cases.md) | PPO clip 到底 clip 什么？分 A>0 与 A<0 解释。 | ★★★★★ | ★★★★☆ | PPO/LLM-RL |
| [Q043](Q043-ppo-full-loss.md) | PPO 的完整 Loss 有哪几部分？ | ★★★★★ | ★★★☆☆ | PPO/机器人 |
| [Q044](Q044-shared-backward.md) | Policy loss 和 Value loss 能否一次 backward？ | ★★★★☆ | ★★★☆☆ | PPO/LLM-RL |
| [Q045](Q045-ppo-kl-monitoring.md) | PPO 已经 clip，为什么还要监控 KL？ | ★★★★★ | ★★★☆☆ | PPO/LLM-RL |
| [Q046](Q046-ppo-multi-epoch.md) | PPO 是 On-policy，为什么 rollout 能训练多个 epoch？ | ★★★★★ | ★★★★☆ | PPO/LLM-RL |
| [Q047](Q047-ppo-limitations.md) | PPO 有哪些缺点？ | ★★★★★ | ★★★☆☆ | PPO/LLM-RL |
| [Q048](Q048-implement-ppo-gae.md) | 手撕 PPO/GAE：代码顺序与最常见 bug？ | ★★★★★ | ★★★★★ | PPO/LLM-RL |

## 本章建议阅读

- [Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)
- [Asynchronous Methods for Deep Reinforcement Learning](https://arxiv.org/abs/1602.01783)
- [High-Dimensional Continuous Control Using Generalized Advantage Estimation](https://arxiv.org/abs/1506.02438)
- [Trust Region Policy Optimization](https://arxiv.org/abs/1502.05477)
- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

能从 likelihood-ratio gradient 一路解释到 baseline、critic、GAE、TRPO、PPO，并能解释 PPO 的 ratio/clip/KL/entropy/value 如何共同作用。

### 公式主线

```text
J(θ)=E[R]
 → log-derivative trick
 → ∇logπ · Q
 → baseline → Advantage
 → learned critic
 → GAE
 → trust-region motivation
 → PPO ratio + clipped surrogate
```

### 90 分回答的观测闭环

`advantage distribution → ratio tail → clipfrac → approx_KL → entropy → value explained variance → held-out return`。

如果只能背 PPO loss，却解释不了这些指标之间的联动，通常只能算“会用库”，不算真正理解 PPO。
