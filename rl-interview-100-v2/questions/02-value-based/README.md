# 第二章 Q-learning / DQN 系列

理解 value-based 方法如何在 bootstrap、off-policy 与函数逼近之间保持稳定。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q016](Q016-q-learning.md) | 简述 Q-learning：目标、更新式、为什么 model-free？ | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q017](Q017-dqn-loss-terminal-mask.md) | 写出 DQN Loss，并解释 terminal mask。 | ★★★★★ | ★★★☆☆ | 游戏/Agent |
| [Q018](Q018-dqn-two-tricks.md) | DQN 最经典的两个 trick 是什么？ | ★★★★★ | ★★☆☆☆ | 游戏/Agent |
| [Q019](Q019-experience-replay.md) | Experience Replay 为什么有效？有什么代价？ | ★★★★★ | ★★★☆☆ | 游戏/Agent |
| [Q020](Q020-target-network.md) | Target Network 为什么能稳定 DQN？ | ★★★★★ | ★★★☆☆ | 游戏/Agent |
| [Q021](Q021-deadly-triad.md) | 什么是 Deadly Triad？ | ★★★★☆ | ★★★★☆ | 研究/高级岗 |
| [Q022](Q022-double-dqn.md) | Double DQN 解决什么问题？ | ★★★★★ | ★★★☆☆ | 游戏/Agent |
| [Q023](Q023-dueling-dqn.md) | Dueling DQN 解决什么问题？ | ★★★★☆ | ★★★☆☆ | 游戏 |
| [Q024](Q024-prioritized-replay.md) | Prioritized Experience Replay 为什么使用 TD error？ | ★★★★☆ | ★★★★☆ | 游戏/Agent |
| [Q025](Q025-dqn-n-step.md) | DQN 加 n-step return 为什么有效？ | ★★★★☆ | ★★★☆☆ | 游戏 |
| [Q026](Q026-distributional-rl.md) | 什么是 Distributional RL？为什么不只学期望 Q？ | ★★★☆☆ | ★★★★☆ | 研究/游戏 |
| [Q027](Q027-rainbow-dqn.md) | Rainbow DQN 包含哪些组件？每个解决什么？ | ★★★★☆ | ★★★☆☆ | 游戏 |
| [Q028](Q028-dqn-no-ppo-is.md) | Q-learning / DQN 为什么不需要 PPO 式 Importance Sampling？ | ★★★★★ | ★★★★☆ | 游戏/PPO |

## 本章建议阅读

- [Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)
- [Human-level control through deep reinforcement learning](https://www.nature.com/articles/nature14236)
- [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)
- [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581)
- [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)
- [A Distributional Perspective on Reinforcement Learning](https://arxiv.org/abs/1707.06887)
- [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

理解 DQN 不是“Q-learning + CNN”这么简单，而是一套对 **Deadly Triad** 的工程稳定化方案。每个改进都要能映射回具体 failure mode。

### 设计 → 病灶映射

| 组件 | 主要病灶 |
|---|---|
| Replay Buffer | 样本相关、交互复用 |
| Target Network | moving bootstrap target |
| Double DQN | max overestimation |
| Dueling | state value / action advantage 表示效率 |
| PER | 非均匀学习价值 |
| n-step | reward propagation |
| Distributional RL | return representation |
| NoisyNet | exploration |

### 工程面必须会

`gather(action)`、terminal mask、target `no_grad`、hard/soft target update、buffer sampling、TD error 分布、Q-value scale 与 replay age。
