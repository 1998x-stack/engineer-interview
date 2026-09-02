# 第七章 Debug / RL Infra / System Design

从指标与数据流定位训练异常，并能设计可扩展的 rollout / learner 系统。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q091](Q091-reward-all-zero-one.md) | RL 训练 reward 全 0 或全 1，怎么排查？ | ★★★★★ | ★★★★☆ | 全方向 |
| [Q092](Q092-entropy-collapse.md) | 什么是 Entropy Collapse？怎么发现和缓解？ | ★★★★★ | ★★★★☆ | PPO/LLM-RL |
| [Q093](Q093-reward-hacking.md) | 什么是 Reward Hacking？举一个算法层面的例子。 | ★★★★★ | ★★★☆☆ | 全方向 |
| [Q094](Q094-long-cot-length.md) | 为什么 Long-CoT RL 容易越来越长？ | ★★★★★ | ★★★★☆ | LLM Reasoning |
| [Q095](Q095-rollout-system.md) | 设计一个大规模 PPO/GRPO Rollout 系统。 | ★★★★★ | ★★★★★ | RL Infra/LLM |
| [Q096](Q096-policy-lag.md) | Actor-Learner 架构中的 Policy Lag 是什么？ | ★★★★☆ | ★★★★☆ | 分布式RL |
| [Q097](Q097-game-rl-design.md) | 给一款 FPS/MOBA 游戏，怎么从零定义 RL 问题？ | ★★★★★ | ★★★★★ | 游戏RL |
| [Q098](Q098-llm-reasoning-rl-system.md) | System Design：设计完整 LLM Reasoning RL Pipeline。 | ★★★★★ | ★★★★★ | LLM Reasoning/Infra |
| [Q099](Q099-implement-grpo.md) | 手撕 GRPO：从 group reward 到 clipped objective 如何实现？ | ★★★★★ | ★★★★★ | LLM Reasoning |
| [Q100](Q100-rl-metrics-diagnosis.md) | 训练中应该监控哪些 RL 指标？如何联动诊断？ | ★★★★★ | ★★★★☆ | 全方向 |

## 本章建议阅读

- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)
- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

从“算法能跑”升级到“训练可解释、可复现、可扩展”。系统题必须回答数据血缘、版本一致性、backpressure、长尾、故障恢复和指标联动。

### Debug 顺序

```text
Data / parser / mask
 → reward / verifier correctness
 → target / stop-gradient / version
 → estimator statistics
 → optimizer / gradient
 → policy distribution
 → system throughput / lag
 → only then hyperparameters
```

### 典型联动

- reward↑、真实 success↓ → reward hacking
- KL↑、entropy↓、clipfrac↑ → policy collapse / over-update
- p99 length↑、GPU util↓ → rollout straggler
- value loss↑、explained variance↓ → critic failure
- queue age↑、policy lag↑ → actor/learner imbalance
