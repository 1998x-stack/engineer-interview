# 白板训练：后训练算法岗 12 组必画图 / 必推公式

## 使用方法

每组控制在 8–12 分钟：2 分钟画、4 分钟推、4 分钟接受反例追问。目标不是公式漂亮，而是每个符号都能解释数据来源和系统位置。

1. **Pretrain vs SFT objective**：解释分布拟合与行为塑形的差异。
2. **Bradley–Terry RM**：从 pair preference 到 reward difference。
3. **Importance Sampling**：从换测度推 PPO ratio。
4. **PPO Clip**：分 A>0/A<0 画 piecewise 行为。
5. **GAE**：从 TD residual 到指数加权并解释 lambda。
6. **KL-regularized RLHF → DPO**：推最优 policy 与 implicit reward。
7. **GRPO group baseline**：解释 std=0 退化。
8. **Sequence reward → token gradient**：指出 credit assignment 粗粒度。
9. **DAPO failure map**：四个 trick 分别修什么。
10. **GSPO sequence ratio**：从 token log-ratio 平均到 geometric mean。
11. **RL system dataflow**：rollout→reward→learner→weight sync，标 version。
12. **Agentic RL trajectory**：state/action/observation/reward 与长程 credit。

## 评分标准

- 公式正确只是 30%。
- 能解释假设、边界和数值实现再加 30%。
- 能给 failure mode、指标和 ablation 再加 30%。
- 能把公式映射到自己项目的 tensor/服务/版本，再加最后 10%。


<!-- PROFESSIONAL_FOOTER -->
## 使用建议

把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。
