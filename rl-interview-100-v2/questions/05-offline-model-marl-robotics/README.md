# 第五章 Offline RL / Model-based / MARL / Sim2Real

处理固定数据分布、模型偏差、多智能体非平稳与真实机器人迁移。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q059](Q059-online-vs-offline-rl.md) | Online RL 与 Offline RL 有什么区别？ | ★★★★☆ | ★★★☆☆ | 推荐/机器人/研究 |
| [Q060](Q060-offline-q-failure.md) | 为什么普通 Q-learning 直接做 Offline RL 容易失败？ | ★★★★☆ | ★★★★☆ | 研究/推荐 |
| [Q061](Q061-bc-vs-offline-rl.md) | Behavior Cloning 与 Offline RL 的区别？ | ★★★★☆ | ★★★☆☆ | 机器人/推荐 |
| [Q062](Q062-cql.md) | CQL 的核心思想是什么？ | ★★★☆☆ | ★★★★☆ | Offline RL |
| [Q063](Q063-iql.md) | IQL 为什么可以避免显式 OOD action evaluation？ | ★★★☆☆ | ★★★★★ | Offline RL |
| [Q064](Q064-model-based-vs-free.md) | Model-based 与 Model-free RL 有何区别？ | ★★★★☆ | ★★★☆☆ | 研究/机器人 |
| [Q065](Q065-reward-shaping.md) | Reward Shaping 应遵循什么原则？ | ★★★★★ | ★★★★☆ | 游戏/机器人 |
| [Q066](Q066-sparse-reward.md) | Sparse Reward 怎么解决？先诊断什么？ | ★★★★★ | ★★★☆☆ | 游戏/机器人 |
| [Q067](Q067-intrinsic-motivation.md) | Intrinsic Motivation 的基本思想与 noisy-TV 问题？ | ★★★☆☆ | ★★★★☆ | 游戏/研究 |
| [Q068](Q068-self-play-curriculum.md) | Self-play 为什么能产生 Curriculum？ | ★★★★☆ | ★★★☆☆ | 游戏/MARL |
| [Q069](Q069-marl-qmix.md) | 多智能体 RL 最大难题是什么？QMIX 解决什么？ | ★★★☆☆ | ★★★★☆ | 游戏/MARL |
| [Q070](Q070-sim2real.md) | 机器人 Sim2Real 怎么做？ | ★★★★☆ | ★★★★☆ | 机器人 |

## 本章建议阅读

- [Conservative Q-Learning for Offline Reinforcement Learning](https://arxiv.org/abs/2006.04779)
- [Offline Reinforcement Learning with Implicit Q-Learning](https://arxiv.org/abs/2110.06169)
- [QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning](https://arxiv.org/abs/1803.11485)
- [Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World](https://arxiv.org/abs/1703.06907)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

这一章的统一关键词是 **distribution shift**。Offline RL 是 dataset support shift，Model-based 是 learned dynamics shift，MARL 是其他 agent 造成的 non-stationarity，Sim2Real 是 simulator→real shift。

### 统一分析框架

1. 训练数据/模型覆盖哪里？
2. learned policy 会走到哪里？
3. 哪种估计会在 OOD 区域失真？
4. 算法用 conservatism、uncertainty、factorization 还是 randomization 控制风险？
5. 如何证明不是只在训练分布上“看起来更好”？

### 项目面要求

能给出 BC baseline、dataset coverage 诊断、Q/OOD 分布、model rollout horizon、opponent pool、domain randomization 范围与真实验证计划。
