# 强化学习术语表 · Glossary

## A

- **Advantage**：`A(s,a)=Q(s,a)-V(s)`，衡量动作相对该状态平均策略行为的增益。
- **Actor**：显式参数化策略的网络/模块。
- **Approx KL**：用 rollout action/token 的 log-prob 差近似监控策略漂移。

## B

- **Behavior Policy**：真正产生训练数据的策略 `μ`。
- **Bootstrap**：target 中使用当前/目标网络对未来价值的估计，而不是等待真实完整 return。

## C

- **Critic**：学习 `V/Q` 等价值估计，为 actor 提供 advantage/gradient signal。
- **Clip Fraction**：PPO 中 ratio 落到 clipping 区域的样本比例。
- **Credit Assignment**：把最终结果归因到之前哪些动作/token/step。

## D

- **Deadly Triad**：function approximation + bootstrapping + off-policy 的不稳定组合。
- **Distribution Shift**：训练数据分布与 learned policy / deployment 分布不一致。

## E

- **Entropy Collapse**：策略分布过早变尖，探索和输出多样性快速消失。
- **Explained Variance**：value prediction 解释 return 方差的程度，critic 诊断常用。

## G

- **GAE**：对未来 TD residual 按 `(γλ)^l` 加权形成的 advantage estimator。
- **GRPO**：Group Relative Policy Optimization，通过同 prompt 的组内相对 reward 构造 baseline/advantage，避免独立 critic。
- **GSPO**：Group Sequence Policy Optimization，以 sequence-level importance ratio/clipping 为核心。

## I

- **Importance Sampling**：用 likelihood ratio 校正采样分布与目标分布差异。
- **IQL**：Implicit Q-Learning，offline RL 中通过 expectile value + advantage-weighted BC 避免显式查询 OOD action。

## K

- **KL Anchor**：用 reference policy 的 KL regularization 控制策略长期漂移。

## O

- **Off-policy**：behavior policy 与 target policy 可不同。
- **On-policy**：数据主要由当前要优化的策略产生，旧数据复用受限。

## P

- **Policy Lag**：actor rollout policy 落后于 learner 当前 policy 的程度。
- **PPO Ratio**：`π_new(a|s)/π_old(a|s)`，不是 reward ratio。

## R

- **Reference Model**：LLM post-training 中冻结的先验/锚点策略。
- **Reward Hacking**：优化器利用 proxy reward 与真实目标之间的漏洞。
- **Rollout**：用当前/指定 policy 与环境或生成过程交互得到 trajectory/response。

## T

- **Target Network**：用于构造相对慢变化 bootstrap target 的网络副本。
- **Truncation**：外部时间/长度限制导致结束，不一定等价于 MDP terminal。

## Z

- **Zero-signal Group**：GRPO 类方法中组内 reward 无差异、相对 advantage 近零的 prompt group。
