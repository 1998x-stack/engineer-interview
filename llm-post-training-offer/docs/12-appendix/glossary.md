# Glossary：LLM Post-Training 核心术语

| 术语 | 精确定义 | 面试中容易混淆的点 |
|---|---|---|
| Policy | 给定 state/context 的动作/token 分布 | current / old / rollout / reference 不是一个角色 |
| Reference Model | KL 或隐式 reward 的行为锚点 | 不等于 old policy |
| Reward Model | 从 response/pair 估计偏好的模型 | proxy，不代表真实目标本身 |
| Verifier | 根据可验证条件判定结果/过程 | rule-based 也有漏洞与 false positive |
| Advantage | action/trajectory 相对 baseline 的超额收益 | sequence advantage 广播到 token 不等于 token credit |
| On-policy | 数据分布与当前优化 policy 足够接近 | PPO 可有限复用旧数据，但不等于任意 off-policy |
| Policy lag | rollout 数据与 learner 当前 policy 的版本差 | 异步系统必须量化而非口头描述 |
| RLVR | Reinforcement Learning with Verifiable Rewards | 成功前提是 verifier 可靠、低成本、可扩展 |
| GRPO | Group Relative Policy Optimization | 以 group-relative baseline 替代 critic 的核心思想 |
| DAPO | failure-driven 的大规模 long-CoT RL recipe | 不是“GRPO 的简单新版本号” |
| GSPO | Group Sequence Policy Optimization | sequence-level importance ratio/clipping 是关键粒度变化 |
| Entropy Collapse | policy 多样性过快消失 | entropy 下降不总是坏，要与性能/多样性联合看 |
| Reward Hacking | 优化 proxy 而偏离 true objective | optimizer 越强越会主动搜索 proxy 漏洞 |
| Process Reward | 对中间步骤提供信号 | dense 不等于更正确；错误 PRM 可更危险 |
| Outcome Reward | 对终局结果提供信号 | 简洁、探索自由，但 credit 稀疏 |


<!-- PROFESSIONAL_FOOTER -->
## 使用建议

把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。
