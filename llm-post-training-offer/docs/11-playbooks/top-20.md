# 高频 20 题

目标：这 20 题达到 **可讲 5-10 分钟**：定义 -> 公式 -> why -> failure -> 工程 -> 追问。

1. [Q002 · SFT 到底在学什么？为什么说它是 behavior cloning？](../01-sft-data/q002-sft-behavior-cloning.md)
2. [Q003 · 公开真题：SFT 数据如何筛选和采样？](../01-sft-data/q003-sft-data-filter-sampling.md)
3. [Q010 · SFT、DPO 与 Online RL 应该如何选？](../01-sft-data/q010-sft-dpo-online-rl-choice.md)
4. [Q011 · Reward Model 如何训练？Bradley-Terry 假设是什么？](../02-reward-model/q011-reward-model-bradley-terry.md)
5. [Q016 · 公开真题：什么是 Reward Hacking？常见类型有哪些？](../02-reward-model/q016-reward-hacking-types.md)
6. [Q021 · 公开真题：PPO 是 on-policy 还是 off-policy？为什么答案不能只说一个词？](../03-ppo-gae/q021-ppo-on-vs-off-policy.md)
7. [Q023 · PPO clipped surrogate objective 怎么写？min 到底在做什么？](../03-ppo-gae/q023-ppo-clipped-objective.md)
8. [Q024 · 公开真题：Advantage 为正/负时 clip 分别限制什么？](../03-ppo-gae/q024-ppo-clip-positive-negative-advantage.md)
9. [Q026 · 公开真题：GAE 如何计算？λ 控制什么？](../03-ppo-gae/q026-gae-derivation-lambda.md)
10. [Q027 · 为什么经典 PPO-RLHF 常说需要四个模型？](../03-ppo-gae/q027-ppo-four-models.md)
11. [Q031 · DPO loss 怎么写？四个 log-prob 项各在做什么？](../04-dpo-family/q031-dpo-loss.md)
12. [Q032 · DPO 如何从 KL-regularized RLHF 推导出来？](../04-dpo-family/q032-dpo-derivation.md)
13. [Q034 · 公开真题：PPO 与 DPO 怎么选？](../04-dpo-family/q034-ppo-vs-dpo.md)
14. [Q041 · 公开真题：PPO 与 GRPO 最大区别是什么？](../05-grpo/q041-ppo-vs-grpo.md)
15. [Q042 · 为什么 group-relative baseline 能替代 Critic？](../05-grpo/q042-group-relative-baseline.md)
16. [Q044 · 公开真题：Sequence-level reward 如何传到 token？credit assignment 有什么问题？](../05-grpo/q044-sequence-reward-token-credit.md)
17. [Q051 · 公开真题：DAPO 相比 GRPO 做了哪些核心改进？](../06-dapo-gspo/q051-dapo-vs-grpo.md)
18. [Q057 · 公开真题：GSPO 与 GRPO 的核心区别是什么？](../06-dapo-gspo/q057-gspo-vs-grpo.md)
19. [Q071 · 公开真题：一个完整 GRPO 数据流是什么？](../08-rl-systems/q071-grpo-dataflow.md)
20. [Q100 · 终极项目题：为什么你的项目选 GRPO/DAPO/GSPO，而不是 PPO/DPO？](../10-agentic-rl/q100-algorithm-choice-project-defense.md)


<!-- PROFESSIONAL_FOOTER -->
## 使用建议

把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。
