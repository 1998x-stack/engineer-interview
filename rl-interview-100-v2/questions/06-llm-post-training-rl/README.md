# 第六章 RLHF / DPO / GRPO / DAPO / GSPO

把 LLM 后训练还原成 policy、reward、sampling、KL 与系统成本问题。

## 本章面试主线

- 不把算法当作孤立名词，而是问：**它修复了哪个 failure mode？**
- 所有公式都要明确：**采样分布、目标分布、bootstrap、baseline、stop-gradient**。
- 至少准备一道“从日志发现算法实现错误”的工程题。

## 题目索引

| 题号 | 题目 | 频率 | 难度 | 典型岗位 |
|---|---|---:|---:|---|
| [Q071](Q071-rlhf-pipeline.md) | 完整讲一下 RLHF Pipeline。 | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q072](Q072-why-rl-after-sft.md) | 已经有 SFT，为什么还需要 RL？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q073](Q073-reward-model.md) | Reward Model 怎么训练？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q074](Q074-rm-distribution-shift.md) | Reward Model 准确率很高，为什么 RL 还是可能训练坏？ | ★★★★★ | ★★★★☆ | LLM Post-training |
| [Q075](Q075-reference-model.md) | RLHF 为什么需要 Reference Model？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q076](Q076-rlhf-kl.md) | KL 在 RLHF 中出现在哪里？过大和过小意味着什么？ | ★★★★★ | ★★★★☆ | LLM Post-training |
| [Q077](Q077-why-ppo-rlhf.md) | 为什么经典 RLHF 常用 PPO？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q078](Q078-critic-vs-reward-model.md) | PPO 里已经有 Critic，为什么还需要 Reward Model？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q079](Q079-dpo.md) | DPO 的核心思想与损失函数？ | ★★★★★ | ★★★★☆ | LLM Post-training |
| [Q080](Q080-dpo-vs-ppo.md) | DPO vs PPO，什么时候选哪个？ | ★★★★★ | ★★★☆☆ | LLM Post-training |
| [Q081](Q081-grpo-vs-ppo.md) | GRPO 为什么被提出？和 PPO 最核心区别？ | ★★★★★ | ★★★★☆ | LLM Reasoning |
| [Q082](Q082-grpo-memory.md) | PPO vs GRPO 为什么 GRPO 更省显存？ | ★★★★★ | ★★★☆☆ | LLM Reasoning |
| [Q083](Q083-grpo-zero-signal-group.md) | GRPO 一个 group 全对或全错会发生什么？ | ★★★★★ | ★★★★☆ | LLM Reasoning |
| [Q084](Q084-rule-vs-neural-reward.md) | Rule-based Reward 与 Neural Reward Model 各有什么优缺点？ | ★★★★★ | ★★★☆☆ | LLM Reasoning |
| [Q085](Q085-dapo.md) | DAPO 相比 GRPO 的四个核心改动？ | ★★★★★ | ★★★★★ | LLM Reasoning |
| [Q086](Q086-gspo.md) | GSPO 为什么改用 Sequence-level Importance Ratio？ | ★★★★★ | ★★★★★ | LLM Reasoning |
| [Q087](Q087-ppo-grpo-dapo-gspo.md) | PPO、GRPO、DAPO、GSPO 如何形成演化路线？ | ★★★★★ | ★★★★☆ | LLM Reasoning |
| [Q088](Q088-grpo-kl.md) | GRPO 中 KL 怎么加？与 PPO reference KL 的关系？ | ★★★★★ | ★★★★☆ | LLM Reasoning |
| [Q089](Q089-agentic-process-reward.md) | Agentic RL 的过程奖励如何设计到 token/step？ | ★★★★☆ | ★★★★★ | Agentic RL |
| [Q090](Q090-rollout-long-tail.md) | GRPO 长尾 rollout 导致 GPU 利用率低，怎么解决？ | ★★★★★ | ★★★★★ | LLM RL Infra |

## 本章建议阅读

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)
- [Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)
- [DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models](https://arxiv.org/abs/2402.03300)
- [DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)
- [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)
- [Group Sequence Policy Optimization](https://arxiv.org/abs/2507.18071)

[← 返回总目录](../../README.md)


## Repo v2 章节深化

### 本章学习目标

必须同时掌握 **算法粒度** 与 **系统粒度**：prompt/group、sequence、token 三层统计；actor/old/reference/reward/critic 五类角色；rollout、verifier、learner、weight sync 四个系统 stage。

### 2026 面试主线

```text
SFT
 → preference / reward modeling
 → PPO-style online RLHF
 → DPO：offline direct preference optimization
 → GRPO：group-relative baseline, remove critic
 → DAPO：修 long-CoT GRPO pathology
 → GSPO：sequence-level importance optimization
```

### 必须能区分的三个 policy

- **old / rollout policy**：ratio 的 behavior reference；
- **current policy**：正在更新的 actor；
- **reference policy**：长期 KL anchor。

把 old 与 reference 混为一谈，是 LLM-RL 面试里非常典型的失分点。
