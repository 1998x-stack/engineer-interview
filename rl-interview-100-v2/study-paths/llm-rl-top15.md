# LLM Post-training / Reasoning RL Top 15 · 2026

> 重点不是背“PPO→GRPO→DAPO→GSPO”名字，而是回答：**每一步到底修了哪个 failure mode，换来了什么新成本？**

## A. PPO 基础层

- [Q039 PPO Clipped Objective](../questions/03-policy-gradient-ppo/Q039-ppo-clipped-objective.md)
- [Q041 PPO Importance Sampling](../questions/03-policy-gradient-ppo/Q041-ppo-is-vs-dqn.md)
- [Q042 PPO Clip Cases](../questions/03-policy-gradient-ppo/Q042-ppo-clip-cases.md)
- [Q043 PPO Full Loss](../questions/03-policy-gradient-ppo/Q043-ppo-full-loss.md)
- [Q045 PPO KL Monitoring](../questions/03-policy-gradient-ppo/Q045-ppo-kl-monitoring.md)

**验收**：能区分 ratio clip 与 reference KL；能解释 old/current/reference 三种 policy。

## B. RLHF / Preference 层

- [Q071 RLHF Pipeline](../questions/06-llm-post-training-rl/Q071-rlhf-pipeline.md)
- [Q073 Reward Model](../questions/06-llm-post-training-rl/Q073-reward-model.md)
- [Q075 Reference Model](../questions/06-llm-post-training-rl/Q075-reference-model.md)
- [Q076 RLHF KL](../questions/06-llm-post-training-rl/Q076-rlhf-kl.md)
- [Q079 DPO](../questions/06-llm-post-training-rl/Q079-dpo.md)

**验收**：能说明 RM、Critic、Reference 各自解决什么，不混用。

## C. Reasoning RL 层

- [Q081 GRPO vs PPO](../questions/06-llm-post-training-rl/Q081-grpo-vs-ppo.md)
- [Q085 DAPO](../questions/06-llm-post-training-rl/Q085-dapo.md)
- [Q086 GSPO](../questions/06-llm-post-training-rl/Q086-gspo.md)
- [Q090 Long-tail Rollout](../questions/06-llm-post-training-rl/Q090-rollout-long-tail.md)
- [Q099 手撕 GRPO](../questions/07-debug-infra-system-design/Q099-implement-grpo.md)

## 2026 必会比较表

| 维度 | PPO | GRPO | DAPO | GSPO |
|---|---|---|---|---|
| Critic | 通常有 | 去掉独立 critic | 通常沿 GRPO | 通常沿 group-relative 思路 |
| Advantage | GAE/value | group-relative reward | group-relative + sampling 改进 | group-relative |
| Ratio 粒度 | action/token | token | token + 特殊 loss/clip | sequence |
| 主要关注 | trust-region-like update | critic memory | long-CoT pathology | sequence-level stability |
| 系统关键 | actor/critic rollout | G-way rollout | dynamic sampling/length | sequence ratio / MoE stability |

> 表格用于建立主线，不表示这些算法只能采用一种固定实现。

## 模拟面试 5 连问

1. GRPO 为什么能去 critic？
2. group 全对为什么没梯度？
3. DAPO Dynamic Sampling 怎么修？
4. GSPO 为什么认为 token ratio 粒度不理想？
5. 如果 p99 response length 是 p50 的 5 倍，你的 rollout 系统怎么避免 GPU 等待？
