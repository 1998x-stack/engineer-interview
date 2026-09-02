# 7 天强化学习面试冲刺计划 · Professional Edition

> 目标不是 7 天“看完 100 题”，而是完成 **主动回忆 → 白板推导 → 最小代码 → Failure Mode → 模拟面试** 五个闭环。

## 总规则

每天只做四类产出：

1. **口述**：每题 30 秒 + 90 秒两个版本；
2. **白板**：当天至少 3 个公式从定义推导，不看笔记；
3. **代码**：至少 1 个核心函数从空文件手写；
4. **诊断**：至少分析 1 个“训练看似正常但其实错”的案例。

## Day 1 — MDP / Bellman / MC / TD

范围：Q001–Q015。

### 必须输出

- 手推一个 3-state MDP 的 `Vπ`；
- 写出 Bellman expectation / optimality 的区别；
- 从 return 推出 TD error；
- 解释 MC↔TD↔n-step 的 bias/variance；
- 解释 on/off-policy 与 importance sampling。

### 当日验收

随机抽 Q005/Q007/Q012/Q013，任何一题 90 秒内不能完整回答，就不进入 Day 2。

## Day 2 — Q-learning / DQN

范围：Q016–Q028。

### 必须输出

- 手写 DQN target + terminal mask；
- 画 online/target/replay 数据流；
- 用一句 failure mode 对应 Double/Dueling/PER/n-step/Distributional；
- 解释 Deadly Triad。

### 当日验收

能指出以下三种 bug 的日志表现：target 未 `detach`、terminal mask 错、Q overestimation。

## Day 3 — Policy Gradient / GAE / PPO

范围：Q029–Q048。

### 必须输出

- 从 log-derivative trick 推到 policy gradient；
- 证明 action-independent baseline 不改期望；
- 手推 GAE；
- 分 `A>0/A<0` 画 PPO clipped objective；
- 从零写 `ratio = exp(new_logp-old_logp)` 与 clipped loss。

### 当日验收

能解释 `KL↑ + entropy↓ + clipfrac↑` 为什么是危险组合。

## Day 4 — DDPG / TD3 / SAC / Offline RL

范围：Q049–Q070。

### 必须输出

- 画 DDPG→TD3→SAC 演化；
- 写 TD3 target；
- 解释 SAC entropy / temperature；
- 解释 Offline Q-learning OOD failure；
- 对比 BC / CQL / IQL。

### 当日验收

必须回答：**为什么一个“Q 很高”的动作在 Offline RL 中反而值得怀疑？**

## Day 5 — RLHF / Reward / DPO

范围：Q071–Q080。

### 必须输出

- 画 SFT→Preference→RM→PPO 的经典 RLHF；
- 区分 Reward Model 与 Critic；
- 区分 old policy 与 reference policy；
- 写 RM pairwise loss；
- 写 DPO loss 并解释每个 log-ratio。

### 当日验收

能解释：**RM validation accuracy 很高，为什么 policy 仍能把 RM 优化坏？**

## Day 6 — GRPO / DAPO / GSPO / LLM Rollout

范围：Q081–Q090。

### 必须输出

- 手写 `[B,G,T]` 的 group advantage；
- 解释 zero-signal group；
- 比较 PPO / GRPO 的显存与 rollout 成本；
- 讲清 DAPO 四个技术点分别处理什么 pathology；
- 解释 GSPO 为什么把 ratio 提到 sequence-level；
- 画长尾 rollout 的同步等待问题。

### 当日验收

能独立回答：**GRPO 省 critic，为什么总 wall-clock 不一定更便宜？**

## Day 7 — Debug / Infra / System Design

范围：Q091–Q100。

### 必须输出

- 完成两次 45 分钟模拟面试；
- 设计一张 RL dashboard；
- 画 PPO/GRPO 大规模 rollout system；
- 手撕 GRPO；
- 分析 reward 全 0、entropy collapse、reward hacking、policy lag、p99 length 五个事故。

## 每日 2 小时最小安排

| 时间 | 任务 |
|---|---|
| 0–25 min | 闭卷口述昨日内容 |
| 25–60 min | 今日核心题深读 |
| 60–90 min | 白板推导 / 手撕 |
| 90–110 min | failure mode / debug |
| 110–120 min | 记录错题与明日复习 |

## 错题记录格式

```text
题号：
我答错/漏掉：
真正的 failure mode：
核心公式：
我会看哪 3 个指标：
下次 30 秒回答：
```
