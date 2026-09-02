# 传统强化学习 Top 20 · 游戏 / 机器人 / 通用算法岗

> 这 20 题不是“最重要名词”，而是一条从 Bellman 到 PPO/SAC 的完整因果链。

## Level 1：基础固定点

- [Q007 DP / MC / TD](../questions/01-foundations/Q007-dp-mc-td.md)
- [Q012 On-policy vs Off-policy](../questions/01-foundations/Q012-on-vs-off-policy.md)
- [Q013 Importance Sampling](../questions/01-foundations/Q013-importance-sampling.md)

**验收**：能从数据分布解释，而不是只背定义。

## Level 2：Value-based

- [Q016 Q-learning](../questions/02-value-based/Q016-q-learning.md)
- [Q017 DQN Loss](../questions/02-value-based/Q017-dqn-loss-terminal-mask.md)
- [Q018 DQN 两个 trick](../questions/02-value-based/Q018-dqn-two-tricks.md)
- [Q019 Replay](../questions/02-value-based/Q019-experience-replay.md)
- [Q020 Target Network](../questions/02-value-based/Q020-target-network.md)
- [Q022 Double DQN](../questions/02-value-based/Q022-double-dqn.md)

**验收**：能把每个 trick 映射到 Deadly Triad / moving target / overestimation。

## Level 3：Policy Optimization

- [Q029 Value vs Policy](../questions/03-policy-gradient-ppo/Q029-value-vs-policy.md)
- [Q030 Policy Gradient Theorem](../questions/03-policy-gradient-ppo/Q030-policy-gradient-theorem.md)
- [Q033 Actor-Critic](../questions/03-policy-gradient-ppo/Q033-actor-critic.md)
- [Q036 GAE](../questions/03-policy-gradient-ppo/Q036-gae.md)
- [Q038 Why PPO](../questions/03-policy-gradient-ppo/Q038-why-ppo.md)
- [Q039 PPO Clip](../questions/03-policy-gradient-ppo/Q039-ppo-clipped-objective.md)
- [Q041 PPO IS vs DQN](../questions/03-policy-gradient-ppo/Q041-ppo-is-vs-dqn.md)
- [Q042 PPO Clip Cases](../questions/03-policy-gradient-ppo/Q042-ppo-clip-cases.md)
- [Q043 PPO Full Loss](../questions/03-policy-gradient-ppo/Q043-ppo-full-loss.md)

## Level 4：连续控制

- [Q052 TD3](../questions/04-continuous-control/Q052-td3-three-tricks.md)
- [Q054 SAC](../questions/04-continuous-control/Q054-sac-max-entropy.md)

## 传统 RL 模拟面试主线

```text
Bellman → TD → Q-learning
→ 为什么 DQN 会不稳定
→ Double / Replay / Target
→ Policy Gradient 为什么高方差
→ Critic / GAE
→ TRPO / PPO
→ 连续动作为什么 DQN 不够
→ DDPG / TD3 / SAC
```

只要这条链能闭卷讲通，传统 RL 一面的大部分基础追问都能接住。
