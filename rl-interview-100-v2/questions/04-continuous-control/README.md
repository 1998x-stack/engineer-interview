# 第四章 DDPG / TD3 / SAC 连续控制

理解连续动作空间中的 actor-critic、Q 过估计、双 critic 与最大熵。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q049](Q049-continuous-action-dqn.md) | 为什么 DQN 不适合连续动作空间？ | ★★★★★ | ★★☆☆☆ | 机器人/控制 |
| [Q050](Q050-ddpg-updates.md) | DDPG 的 Actor 和 Critic 如何更新？ | ★★★★☆ | ★★★★☆ | 机器人/控制 |
| [Q051](Q051-ddpg-instability.md) | DDPG 为什么容易不稳定？ | ★★★★☆ | ★★★★☆ | 机器人/控制 |
| [Q052](Q052-td3-three-tricks.md) | TD3 相比 DDPG 的三个关键改进？ | ★★★★★ | ★★★☆☆ | 机器人/控制 |
| [Q053](Q053-td3-min-double-q.md) | TD3 为什么取 min(Q1,Q2)，而不是平均？ | ★★★★☆ | ★★★★☆ | 机器人/控制 |
| [Q054](Q054-sac-max-entropy.md) | SAC 的核心思想是什么？ | ★★★★★ | ★★★☆☆ | 机器人/控制 |
| [Q055](Q055-sac-temperature.md) | SAC 的 temperature α 是什么？ | ★★★★☆ | ★★★☆☆ | 机器人/控制 |
| [Q056](Q056-ppo-td3-sac-selection.md) | PPO、TD3、SAC 如何选？ | ★★★★★ | ★★★☆☆ | 机器人/控制 |
| [Q057](Q057-continuous-action-discretization.md) | 连续动作为什么不能简单 discretize？ | ★★★★☆ | ★★☆☆☆ | 机器人/控制 |
| [Q058](Q058-topk-vs-sac.md) | LLM top-k sampling 与 SAC stochastic policy 的本质区别？ | ★★★☆☆ | ★★★☆☆ | LLM/控制 |

## 本章建议阅读

- [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)
- [Addressing Function Approximation Error in Actor-Critic Methods](https://proceedings.mlr.press/v80/fujimoto18a.html)
- [Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor](https://proceedings.mlr.press/v80/haarnoja18b.html)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

把连续动作问题理解成“如何优化 Q(s,a) 上的动作”，并掌握 deterministic actor、twin critic、target smoothing、maximum entropy 和 reparameterization 的关系。

### 算法演化

```text
DQN 无法枚举 continuous argmax
 → DDPG：learned deterministic actor
 → actor exploit critic error
 → TD3：twin Q + delayed actor + target smoothing
 → SAC：stochastic actor + entropy objective + off-policy replay
```

### 工程高频

动作缩放、tanh squash、Gaussian log-prob Jacobian、Polyak target、Q1/Q2 gap、temperature α、探索噪声与 target noise 的区别。
