# 100 题总索引

| 题目 | 章 | 类型 | 难度 | 高频 |
|---|---:|---|---:|:---:|
| [Q001 · 什么是 Post-Training？为什么 Pretraining 后仍需要后训练？](01-sft-data/q001-post-training-goal.md) | 1 | 高频题 | L1 |  |
| [Q002 · SFT 到底在学什么？为什么说它是 behavior cloning？](01-sft-data/q002-sft-behavior-cloning.md) | 1 | 高频题 | L1 | 🔥 |
| [Q003 · 公开真题：SFT 数据如何筛选和采样？](01-sft-data/q003-sft-data-filter-sampling.md) | 1 | 公开真题 | L2 | 🔥 |
| [Q004 · SFT 数据是越多越好吗？如何理解 data quality × diversity × difficulty？](01-sft-data/q004-sft-data-quality-diversity-difficulty.md) | 1 | 高频题 | L2 |  |
| [Q005 · 为什么 SFT 会造成 catastrophic forgetting 或 alignment tax？](01-sft-data/q005-sft-forgetting-alignment-tax.md) | 1 | 原理推导 | L2 |  |
| [Q006 · 多领域 SFT 数据应该怎么配比？](01-sft-data/q006-sft-domain-mixture.md) | 1 | 高频题 | L2 |  |
| [Q007 · 为什么 instruction data 需要 prompt diversity，而不只是 response diversity？](01-sft-data/q007-prompt-diversity.md) | 1 | 原理推导 | L1 |  |
| [Q008 · 公开真题：CoT 数据怎么构建、筛选与验证？](01-sft-data/q008-cot-data-build-filter-verify.md) | 1 | 公开真题 | L3 |  |
| [Q009 · 为什么 SFT 经常是 RL 的 cold start？DeepSeek-R1-Zero 又为什么可以跳 过？](01-sft-data/q009-sft-cold-start-pure-rl.md) | 1 | 原理推导 | L3 |  |
| [Q010 · SFT、DPO 与 Online RL 应该如何选？](01-sft-data/q010-sft-dpo-online-rl-choice.md) | 1 | 系统设计 | L3 | 🔥 |
| [Q011 · Reward Model 如何训练？Bradley-Terry 假设是什么？](02-reward-model/q011-reward-model-bradley-terry.md) | 2 | 高频题 | L2 | 🔥 |
| [Q012 · 公开真题：PPO 中的 Reward Model 数据从哪里来？](02-reward-model/q012-reward-model-data-source.md) | 2 | 公开真题 | L2 |  |
| [Q013 · Preference pair 的 margin、难度和 annotator agreement 为什么重要？](02-reward-model/q013-preference-margin-agreement.md) | 2 | 原理推导 | L2 |  |
| [Q014 · 如何处理不同标注员之间的 preference disagreement？](02-reward-model/q014-annotator-disagreement.md) | 2 | 系统设计 | L3 |  |
| [Q015 · Reward Model 为什么会被 policy exploit？](02-reward-model/q015-reward-model-exploitation.md) | 2 | 原理推导 | L3 |  |
| [Q016 · 公开真题：什么是 Reward Hacking？常见类型有哪些？](02-reward-model/q016-reward-hacking-types.md) | 2 | 公开真题 | L2 | 🔥 |
| [Q017 · 如何系统检测 Reward Hacking？](02-reward-model/q017-detect-reward-hacking.md) | 2 | 系统设计 | L3 |  |
| [Q018 · Outcome Reward 与 Process Reward 有什么本质差异？](02-reward-model/q018-outcome-vs-process-reward.md) | 2 | 高频题 | L3 |  |
| [Q019 · 多个 Reward / Judge 如何组合？](02-reward-model/q019-multi-reward-composition.md) | 2 | 系统设计 | L3 |  |
| [Q020 · 为什么 rule-based verifier 是 RLVR 的关键基础设施？](02-reward-model/q020-rule-verifier-rlvr.md) | 2 | 原理推导 | L2 |  |
| [Q021 · 公开真题：PPO 是 on-policy 还是 off-policy？为什么答案不能只说一个词？](03-ppo-gae/q021-ppo-on-vs-off-policy.md) | 3 | 公开真题 | L2 | 🔥 |
| [Q022 · 公开真题：为什么 PPO 需要 Importance Sampling？](03-ppo-gae/q022-ppo-importance-sampling.md) | 3 | 公开真题 | L2 |  |
| [Q023 · PPO clipped surrogate objective 怎么写？min 到底在做什么？](03-ppo-gae/q023-ppo-clipped-objective.md) | 3 | 高频题 | L3 | 🔥 |
| [Q024 · 公开真题：Advantage 为正/负时 clip 分别限制什么？](03-ppo-gae/q024-ppo-clip-positive-negative-advantage.md) | 3 | 公开真题 | L3 | 🔥 |
| [Q025 · PPO 为什么需要 Critic / Value Model？](03-ppo-gae/q025-ppo-critic-value-model.md) | 3 | 高频题 | L2 |  |
| [Q026 · 公开真题：GAE 如何计算？λ 控制什么？](03-ppo-gae/q026-gae-derivation-lambda.md) | 3 | 公开真题 | L3 | 🔥 |
| [Q027 · 为什么经典 PPO-RLHF 常说需要四个模型？](03-ppo-gae/q027-ppo-four-models.md) | 3 | 高频题 | L2 | 🔥 |
| [Q028 · Reference Model 与 KL penalty 的本质作用是什么？](03-ppo-gae/q028-reference-model-kl.md) | 3 | 原理推导 | L3 |  |
| [Q029 · KL 系数 β 太大或太小会怎样？如何自适应？](03-ppo-gae/q029-adaptive-kl-beta.md) | 3 | 系统设计 | L2 |  |
| [Q030 · PPO 在 LLM 后训练中最大的工程问题是什么？](03-ppo-gae/q030-ppo-engineering-cost.md) | 3 | 系统设计 | L3 |  |
| [Q031 · DPO loss 怎么写？四个 log-prob 项各在做什么？](04-dpo-family/q031-dpo-loss.md) | 4 | 高频题 | L3 | 🔥 |
| [Q032 · DPO 如何从 KL-regularized RLHF 推导出来？](04-dpo-family/q032-dpo-derivation.md) | 4 | 原理推导 | L4 | 🔥 |
| [Q033 · 为什么 DPO 比 PPO 简单很多？](04-dpo-family/q033-why-dpo-simpler-than-ppo.md) | 4 | 高频题 | L2 |  |
| [Q034 · 公开真题：PPO 与 DPO 怎么选？](04-dpo-family/q034-ppo-vs-dpo.md) | 4 | 公开真题 | L3 | 🔥 |
| [Q035 · DPO 的 offline distribution shift 问题是什么？](04-dpo-family/q035-dpo-offline-distribution-shift.md) | 4 | 原理推导 | L3 |  |
| [Q036 · DPO 为什么也可能 overfit 或出现 length bias？](04-dpo-family/q036-dpo-overfit-length-bias.md) | 4 | 原理推导 | L3 |  |
| [Q037 · DPO 中 β 应如何理解？](04-dpo-family/q037-dpo-beta.md) | 4 | 原理推导 | L3 |  |
| [Q038 · KTO 与 DPO 的数据要求有何差异？](04-dpo-family/q038-kto-vs-dpo.md) | 4 | 高频题 | L2 |  |
| [Q039 · ORPO 为什么可以 reference-free？](04-dpo-family/q039-orpo-reference-free.md) | 4 | 高频题 | L2 |  |
| [Q040 · SimPO 相比 DPO 改了什么？为什么使用平均 log probability？](04-dpo-family/q040-simpo-average-logprob.md) | 4 | 高频题 | L3 |  |
| [Q041 · 公开真题：PPO 与 GRPO 最大区别是什么？](05-grpo/q041-ppo-vs-grpo.md) | 5 | 公开真题 | L2 | 🔥 |
| [Q042 · 为什么 group-relative baseline 能替代 Critic？](05-grpo/q042-group-relative-baseline.md) | 5 | 原理推导 | L3 | 🔥 |
| [Q043 · GRPO 去掉 Critic 后，真正的成本转移到了哪里？](05-grpo/q043-grpo-cost-transfer.md) | 5 | 系统设计 | L3 |  |
| [Q044 · 公开真题：Sequence-level reward 如何传到 token？credit assignment 有什么问题？](05-grpo/q044-sequence-reward-token-credit.md) | 5 | 公开真题 | L3 | 🔥 |
| [Q045 · 为什么 group 内全对或全错时 GRPO 基本没有有效梯度？](05-grpo/q045-grpo-all-correct-all-wrong.md) | 5 | 原理推导 | L3 |  |
| [Q046 · Group size G 越大越好吗？](05-grpo/q046-grpo-group-size.md) | 5 | 系统设计 | L3 |  |
| [Q047 · 公开真题：πθ、πold、πrollout 分别是什么？为什么工程中可能不相等？](05-grpo/q047-policy-old-rollout.md) | 5 | 公开真题 | L3 |  |
| [Q048 · 公开真题：batch 很大时为什么 GRPO 会越来越 off-policy？](05-grpo/q048-grpo-large-batch-off-policy.md) | 5 | 公开真题 | L4 |  |
| [Q049 · 如何缓解 policy lag？同步 RL 与异步 RL 各自适合什么？](05-grpo/q049-policy-lag-sync-async.md) | 5 | 系统设计 | L4 |  |
| [Q050 · 为什么 GRPO 特别适合数学/代码等 verifiable tasks？](05-grpo/q050-grpo-verifiable-tasks.md) | 5 | 原理推导 | L2 |  |
| [Q051 · 公开真题：DAPO 相比 GRPO 做了哪些核心改进？](06-dapo-gspo/q051-dapo-vs-grpo.md) | 6 | 公开真题 | L3 | 🔥 |
| [Q052 · 为什么 DAPO 需要 Clip-Higher？](06-dapo-gspo/q052-dapo-clip-higher.md) | 6 | 原理推导 | L4 |  |
| [Q053 · 公开真题：Dynamic Sampling 为什么有效？](06-dapo-gspo/q053-dapo-dynamic-sampling.md) | 6 | 公开真题 | L3 |  |
| [Q054 · 长 CoT 下 sequence-level normalization 为什么可能产生长度偏差？](06-dapo-gspo/q054-long-cot-length-normalization.md) | 6 | 原理推导 | L4 |  |
| [Q055 · Token-level Policy Gradient Loss 解决什么？](06-dapo-gspo/q055-token-level-policy-gradient.md) | 6 | 原理推导 | L4 |  |
| [Q056 · Overlong Reward Shaping 为什么比硬截断惩罚更稳？](06-dapo-gspo/q056-overlong-reward-shaping.md) | 6 | 原理推导 | L3 |  |
| [Q057 · 公开真题：GSPO 与 GRPO 的核心区别是什么？](06-dapo-gspo/q057-gspo-vs-grpo.md) | 6 | 公开真题 | L4 | 🔥 |
| [Q058 · GSPO 为什么需要 1/|y| 的长度归一化？](06-dapo-gspo/q058-gspo-length-normalization.md) | 6 | 原理推导 | L4 |  |
| [Q059 · 公开真题：为什么 GSPO 对 MoE routing mismatch 更友好？](06-dapo-gspo/q059-gspo-moe-routing.md) | 6 | 公开真题 | L5 |  |
| [Q060 · DAPO 与 GSPO 应如何比较？它们不是同一层面的改进](06-dapo-gspo/q060-dapo-vs-gspo.md) | 6 | 系统设计 | L5 |  |
| [Q061 · 为什么 Online RL 可能提升 reasoning，而 SFT 不一定？](07-reasoning-verifier/q061-online-rl-reasoning.md) | 7 | 原理推导 | L3 |  |
| [Q062 · RL 是“创造能力”还是“激活已有能力”？](07-reasoning-verifier/q062-rl-create-vs-elicit.md) | 7 | 系统设计 | L4 |  |
| [Q063 · 为什么数学/代码 RL 比 open-ended chat RL 更容易？](07-reasoning-verifier/q063-verifiable-vs-open-ended-rl.md) | 7 | 原理推导 | L2 |  |
| [Q064 · Process Reward 一定比 Outcome Reward 好吗？](07-reasoning-verifier/q064-process-vs-outcome-reward.md) | 7 | 系统设计 | L3 |  |
| [Q065 · Sparse Reward 如何改善？](07-reasoning-verifier/q065-sparse-reward.md) | 7 | 系统设计 | L3 |  |
| [Q066 · 如何避免模型把“更长 CoT”误学成“更高能力”？](07-reasoning-verifier/q066-cot-length-vs-capability.md) | 7 | 系统设计 | L3 |  |
| [Q067 · Entropy collapse 是什么？为什么 GRPO/DAPO 特别关注？](07-reasoning-verifier/q067-entropy-collapse.md) | 7 | 原理推导 | L3 |  |
| [Q068 · 为什么只看训练 reward 非常危险？](07-reasoning-verifier/q068-train-reward-is-not-enough.md) | 7 | 高频题 | L2 |  |
| [Q069 · Rule-based verifier 也会被 hacking 吗？](07-reasoning-verifier/q069-verifier-hacking.md) | 7 | 系统设计 | L3 |  |
| [Q070 · 如何设计一个“好 Reward”？](07-reasoning-verifier/q070-good-reward-design.md) | 7 | 系统设计 | L4 |  |
| [Q071 · 公开真题：一个完整 GRPO 数据流是什么？](08-rl-systems/q071-grpo-dataflow.md) | 8 | 公开真题 | L3 | 🔥 |
| [Q072 · 为什么 RL rollout 比 SFT teacher-forcing 贵？](08-rl-systems/q072-rollout-vs-teacher-forcing-cost.md) | 8 | 原理推导 | L2 |  |
| [Q073 · 公开真题：rollout 长尾为什么降低 GPU 利用率？](08-rl-systems/q073-rollout-tail-gpu-utilization.md) | 8 | 公开真题 | L3 |  |
| [Q074 · rollout 长尾有哪些工程解法？](08-rl-systems/q074-rollout-tail-solutions.md) | 8 | 系统设计 | L4 |  |
| [Q075 · vLLM 为什么适合 RL rollout？](08-rl-systems/q075-vllm-for-rollout.md) | 8 | 高频题 | L2 |  |
| [Q076 · 公开真题：FSDP 与 DDP 的核心区别？](08-rl-systems/q076-fsdp-vs-ddp.md) | 8 | 公开真题 | L3 |  |
| [Q077 · 公开真题：ZeRO-1/2/3 分别 shard 什么？](08-rl-systems/q077-zero-stages.md) | 8 | 公开真题 | L2 |  |
| [Q078 · 为什么 PPO/GRPO 系统显存比 SFT 更复杂？](08-rl-systems/q078-rl-memory-vs-sft.md) | 8 | 原理推导 | L3 |  |
| [Q079 · RL 训推分离如何设计？weight sync 的 trade-off 是什么？](08-rl-systems/q079-train-inference-disaggregation.md) | 8 | 系统设计 | L4 |  |
| [Q080 · 公开真题：TRL、verl、OpenRLHF 这类框架应该理解到什么程度？](08-rl-systems/q080-trl-verl-openrlhf.md) | 8 | 公开真题 | L3 |  |
| [Q081 · 公开真题：怎么判断一次 RL 训练“质量达标”？](09-eval-debug/q081-rl-training-quality-gate.md) | 9 | 公开真题 | L3 |  |
| [Q082 · Reward 一直涨但 benchmark 不涨，怎么排查？](09-eval-debug/q082-reward-up-benchmark-flat.md) | 9 | 系统设计 | L4 |  |
| [Q083 · KL 突然暴涨通常意味着什么？](09-eval-debug/q083-kl-spike-debug.md) | 9 | 系统设计 | L3 |  |
| [Q084 · Entropy 一路下降怎么办？](09-eval-debug/q084-entropy-down-debug.md) | 9 | 系统设计 | L3 |  |
| [Q085 · Reward variance 很大怎么办？](09-eval-debug/q085-reward-variance-debug.md) | 9 | 系统设计 | L3 |  |
| [Q086 · 为什么离线 benchmark 不能完全代表线上？](09-eval-debug/q086-offline-vs-online-eval.md) | 9 | 高频题 | L2 |  |
| [Q087 · 怎么做后训练 ablation 才可信？](09-eval-debug/q087-post-training-ablation.md) | 9 | 系统设计 | L3 |  |
| [Q088 · 为什么 SFT 变好但 RL 可能变差？](09-eval-debug/q088-sft-better-rl-worse.md) | 9 | 原理推导 | L4 |  |
| [Q089 · 如何构建 hard-example data flywheel？](09-eval-debug/q089-hard-example-data-flywheel.md) | 9 | 系统设计 | L3 |  |
| [Q090 · 如何判断问题来自数据、算法还是系统实现？](09-eval-debug/q090-data-vs-algorithm-vs-system.md) | 9 | 系统设计 | L4 |  |
| [Q091 · 公开真题：什么是 Agentic RL？与单轮 reasoning RL 的状态空间有何不同？](10-agentic-rl/q091-agentic-rl-state-space.md) | 10 | 公开真题 | L3 |  |
| [Q092 · 公开真题：Agentic RL 的 credit assignment 怎么做？](10-agentic-rl/q092-agentic-credit-assignment.md) | 10 | 公开真题 | L4 |  |
| [Q093 · 公开真题：Tool Calling / Function Calling 数据怎么构造？](10-agentic-rl/q093-tool-calling-data.md) | 10 | 公开真题 | L3 |  |
| [Q094 · Agent reward 应如何设计？](10-agentic-rl/q094-agent-reward-design.md) | 10 | 系统设计 | L4 |  |
| [Q095 · 如何防止 Agent 为了 reward 无限调用工具或重复搜索？](10-agentic-rl/q095-agent-tool-loop-hacking.md) | 10 | 系统设计 | L3 |  |
| [Q096 · Multi-turn RL 与 single-turn RL 最大区别是什么？](10-agentic-rl/q096-multi-turn-vs-single-turn-rl.md) | 10 | 原理推导 | L3 |  |
| [Q097 · 公开真题：长程任务为什么可能选 GRPO 而不是 PPO？](10-agentic-rl/q097-long-horizon-grpo-vs-ppo.md) | 10 | 公开真题 | L4 |  |
| [Q098 · 如何给 Agent 过程打 reward，而不把探索路径写死？](10-agentic-rl/q098-agent-process-reward.md) | 10 | 系统设计 | L4 |  |
| [Q099 · 系统设计题：如果让你做一个 70B reasoning model 的完整 Post-Training pipeline？](10-agentic-rl/q099-70b-post-training-pipeline.md) | 10 | 系统设计 | L5 |  |
| [Q100 · 终极项目题：为什么你的项目选 GRPO/DAPO/GSPO，而不是 PPO/DPO？](10-agentic-rl/q100-algorithm-choice-project-defense.md) | 10 | 公开真题 | L5 | 🔥 |
