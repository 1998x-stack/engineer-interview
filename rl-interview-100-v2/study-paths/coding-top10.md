# 手撕实现 Top 10 · Coding Interview Path

> 目标：不是写完整框架，而是能在 15–25 分钟内写对 **shape、mask、detach、target、数值稳定**。

## Top 10

1. [Q016 Q-learning](../questions/02-value-based/Q016-q-learning.md)
2. [Q017 DQN Loss + terminal mask](../questions/02-value-based/Q017-dqn-loss-terminal-mask.md)
3. [Q019 Replay Buffer](../questions/02-value-based/Q019-experience-replay.md)
4. [Q022 Double DQN target](../questions/02-value-based/Q022-double-dqn.md)
5. [Q031 REINFORCE](../questions/03-policy-gradient-ppo/Q031-reinforce.md)
6. [Q033 Actor-Critic](../questions/03-policy-gradient-ppo/Q033-actor-critic.md)
7. [Q036 GAE](../questions/03-policy-gradient-ppo/Q036-gae.md)
8. [Q048 PPO + GAE](../questions/03-policy-gradient-ppo/Q048-implement-ppo-gae.md)
9. [Q054 SAC core loss](../questions/04-continuous-control/Q054-sac-max-entropy.md)
10. [Q099 GRPO](../questions/07-debug-infra-system-design/Q099-implement-grpo.md)

## 每题统一手撕模板

### 1. 先写 shape

例如 GRPO：

```text
rewards        [B, G]
old_logp       [B, G, T]
new_logp       [B, G, T]
response_mask  [B, G, T]
advantage      [B, G] -> broadcast [B, G, T]
```

### 2. 再写 stop-gradient 边界

- target network / old policy / reference policy 默认不回传；
- advantage 是否 detach 要明确；
- critic 与 actor 是否共享 backbone 要明确。

### 3. 再写 mask

优先检查：

- terminal；
- truncation；
- padding；
- prompt vs response token；
- multi-env episode boundary。

### 4. 最后做数值稳定

- `exp(new_logp-old_logp)`；
- `std + eps`；
- `logsumexp`；
- gradient clipping；
- Huber loss（适用时）。

## Tiny Test 必做

每个函数至少三个测试：

1. **人工可算**：两三个数，结果手工对齐；
2. **边界**：全 terminal / zero-variance / 全 padding；
3. **梯度**：检查 target/reference 无梯度，actor 有梯度。

## 配套最小代码

见 [`../code/README.md`](../code/README.md)。
