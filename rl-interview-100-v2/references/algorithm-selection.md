# 强化学习算法选型 · Decision Guide

> 不按“谁更新”选算法，而按 **交互成本、动作空间、数据是否固定、是否需要探索、稳定性、系统预算** 选。

| 场景 | 首选思路 | 为什么 | 主要风险 |
|---|---|---|---|
| 小型离散、可解释 | Tabular Q / SARSA | 简单、可手算 | 状态爆炸 |
| Atari/离散高维 | DQN family | replay + value control | Deadly Triad / Q 偏差 |
| 海量并行仿真 | PPO | 稳定、易批处理 | sample efficiency |
| 昂贵连续交互 | SAC / TD3 | off-policy replay | Q extrapolation |
| 多峰随机控制 | SAC | stochastic + entropy | log-prob/squash 实现复杂 |
| 固定静态数据 | BC → IQL/CQL | 控制 OOD | 过保守/coverage |
| 学得世界模型有价值 | Model-based | imagined rollout | model bias |
| 协作 MARL | CTDE / QMIX 等 | centralized training | non-stationarity / factorization |
| 静态偏好对齐 | DPO 类 | 简单、无需 online rollout | 数据覆盖/偏好偏差 |
| 可验证 reasoning | GRPO/PPO-style RL | online exploration + verifier | rollout 成本/奖励稀疏 |
| 大规模 long-CoT RL | GRPO/DAPO/GSPO 思路 | critic cost / stability / sequence granularity | 长尾、zero-signal、KL/entropy |

## 五步选型法

1. **数据能否继续采？** 不能 → Offline RL / BC；能 → Online/off-policy 都可。
2. **动作连续还是离散？** 连续高维避免枚举式 Q argmax。
3. **交互贵不贵？** 贵 → 优先 replay/off-policy/sample reuse。
4. **是否有可靠 verifier？** 有 → online RL 的价值明显上升。
5. **系统瓶颈在哪里？** rollout、显存、learner、同步长尾会直接决定可用算法。

## 面试错误姿势

- “PPO 最稳定，所以都用 PPO”。
- “SAC sample efficient，所以真实机器人一定 SAC”。
- “DPO 比 PPO 简单，所以一定更好”。
- “GRPO 省 critic，所以总成本一定更低”。

专业回答必须给出 **约束 → tradeoff → 指标 → fallback**。
