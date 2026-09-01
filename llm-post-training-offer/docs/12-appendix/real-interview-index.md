# 公开真题索引

| 题号 | 题目 | PDF 标注来源 |
|---|---|---|
| [Q003](../01-sft-data/q003-sft-data-filter-sampling.md) | 公开真题：SFT 数据如何筛选和采样？ | I7 |
| [Q008](../01-sft-data/q008-cot-data-build-filter-verify.md) | 公开真题：CoT 数据怎么构建、筛选与验证？ | I3, I7 |
| [Q012](../02-reward-model/q012-reward-model-data-source.md) | 公开真题：PPO 中的 Reward Model 数据从哪里来？ | I6 |
| [Q016](../02-reward-model/q016-reward-hacking-types.md) | 公开真题：什么是 Reward Hacking？常见类型有哪些？ | I7 |
| [Q021](../03-ppo-gae/q021-ppo-on-vs-off-policy.md) | 公开真题：PPO 是 on-policy 还是 off-policy？为什么答案不能只说一个词？ | I1 |
| [Q022](../03-ppo-gae/q022-ppo-importance-sampling.md) | 公开真题：为什么 PPO 需要 Importance Sampling？ | I1, I11 |
| [Q024](../03-ppo-gae/q024-ppo-clip-positive-negative-advantage.md) | 公开真题：Advantage 为正/负时 clip 分别限制什么？ | I1 |
| [Q026](../03-ppo-gae/q026-gae-derivation-lambda.md) | 公开真题：GAE 如何计算？λ 控制什么？ | I1, I6, P3 |
| [Q034](../04-dpo-family/q034-ppo-vs-dpo.md) | 公开真题：PPO 与 DPO 怎么选？ | I6, I10 |
| [Q041](../05-grpo/q041-ppo-vs-grpo.md) | 公开真题：PPO 与 GRPO 最大区别是什么？ | I3, I11, P2 |
| [Q044](../05-grpo/q044-sequence-reward-token-credit.md) | 公开真题：Sequence-level reward 如何传到 token？credit assignment 有什么问题？ | I1, I8 |
| [Q047](../05-grpo/q047-policy-old-rollout.md) | 公开真题：πθ、πold、πrollout 分别是什么？为什么工程中可能不相等？ | I6 |
| [Q048](../05-grpo/q048-grpo-large-batch-off-policy.md) | 公开真题：batch 很大时为什么 GRPO 会越来越 off-policy？ | I6 |
| [Q051](../06-dapo-gspo/q051-dapo-vs-grpo.md) | 公开真题：DAPO 相比 GRPO 做了哪些核心改进？ | I3, I7, P9 |
| [Q053](../06-dapo-gspo/q053-dapo-dynamic-sampling.md) | 公开真题：Dynamic Sampling 为什么有效？ | I7, P9 |
| [Q057](../06-dapo-gspo/q057-gspo-vs-grpo.md) | 公开真题：GSPO 与 GRPO 的核心区别是什么？ | I3, I11, P10 |
| [Q059](../06-dapo-gspo/q059-gspo-moe-routing.md) | 公开真题：为什么 GSPO 对 MoE routing mismatch 更友好？ | I8, P10 |
| [Q071](../08-rl-systems/q071-grpo-dataflow.md) | 公开真题：一个完整 GRPO 数据流是什么？ | I6 |
| [Q073](../08-rl-systems/q073-rollout-tail-gpu-utilization.md) | 公开真题：rollout 长尾为什么降低 GPU 利用率？ | I7, I8 |
| [Q076](../08-rl-systems/q076-fsdp-vs-ddp.md) | 公开真题：FSDP 与 DDP 的核心区别？ | I1, I7, P12 |
| [Q077](../08-rl-systems/q077-zero-stages.md) | 公开真题：ZeRO-1/2/3 分别 shard 什么？ | I1, P11 |
| [Q080](../08-rl-systems/q080-trl-verl-openrlhf.md) | 公开真题：TRL、verl、OpenRLHF 这类框架应该理解到什么程度？ | I6 |
| [Q081](../09-eval-debug/q081-rl-training-quality-gate.md) | 公开真题：怎么判断一次 RL 训练“质量达标”？ | I7 |
| [Q091](../10-agentic-rl/q091-agentic-rl-state-space.md) | 公开真题：什么是 Agentic RL？与单轮 reasoning RL 的状态空间有何不同？ | I1, I7 |
| [Q092](../10-agentic-rl/q092-agentic-credit-assignment.md) | 公开真题：Agentic RL 的 credit assignment 怎么做？ | I7, I8 |
| [Q093](../10-agentic-rl/q093-tool-calling-data.md) | 公开真题：Tool Calling / Function Calling 数据怎么构造？ | - |
| [Q097](../10-agentic-rl/q097-long-horizon-grpo-vs-ppo.md) | 公开真题：长程任务为什么可能选 GRPO 而不是 PPO？ | I12 |
| [Q100](../10-agentic-rl/q100-algorithm-choice-project-defense.md) | 终极项目题：为什么你的项目选 GRPO/DAPO/GSPO，而不是 PPO/DPO？ | I3, I7, I11 |

**使用方式**：不要追求“押中逐字原题”。真实面试会沿项目继续追公式、反例、failure 和系统实现。真题的价值是校准考察深度。


<!-- PROFESSIONAL_FOOTER -->
## 使用建议

把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。
