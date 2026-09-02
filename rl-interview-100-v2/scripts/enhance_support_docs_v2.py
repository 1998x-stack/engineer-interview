from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]

chapters={
'01-foundations':('第一章：MDP / Bellman / DP / MC / TD',
'''### 本章学习目标\n\n学完后应能从 **trajectory / return** 出发，自行推导到 Bellman、MC、TD、n-step 和 on/off-policy，而不是把这些概念记成互不相关的定义。\n\n### 一条因果主线\n\n```text\nSequential Decision Making\n  → Markov State\n  → Return G_t\n  → V / Q / A\n  → Bellman recursion\n  → exact expectation (DP) / sampled return (MC) / bootstrap (TD)\n  → n-step / TD(λ)\n  → behavior policy vs target policy\n  → importance sampling\n```\n\n### 面试分层\n\n- **一面**：定义准确、公式会写、能比较 MC/TD、SARSA/Q-learning。\n- **二面**：能解释 contraction、bias-variance、IS 高方差和 state 是否 Markov。\n- **项目面**：能处理 terminal/truncated、reward scale、trajectory schema 和部分可观测。\n\n### 本章手算要求\n\n至少手算一次 3-state MDP 的 V/Q、一次 MC return、一次 TD error、一次 IS 估计。'''),
'02-value-based':('第二章：Q-learning / DQN 系列',
'''### 本章学习目标\n\n理解 DQN 不是“Q-learning + CNN”这么简单，而是一套对 **Deadly Triad** 的工程稳定化方案。每个改进都要能映射回具体 failure mode。\n\n### 设计 → 病灶映射\n\n| 组件 | 主要病灶 |\n|---|---|\n| Replay Buffer | 样本相关、交互复用 |\n| Target Network | moving bootstrap target |\n| Double DQN | max overestimation |\n| Dueling | state value / action advantage 表示效率 |\n| PER | 非均匀学习价值 |\n| n-step | reward propagation |\n| Distributional RL | return representation |\n| NoisyNet | exploration |\n\n### 工程面必须会\n\n`gather(action)`、terminal mask、target `no_grad`、hard/soft target update、buffer sampling、TD error 分布、Q-value scale 与 replay age。'''),
'03-policy-gradient-ppo':('第三章：Policy Gradient / Actor-Critic / PPO',
'''### 本章学习目标\n\n能从 likelihood-ratio gradient 一路解释到 baseline、critic、GAE、TRPO、PPO，并能解释 PPO 的 ratio/clip/KL/entropy/value 如何共同作用。\n\n### 公式主线\n\n```text\nJ(θ)=E[R]\n → log-derivative trick\n → ∇logπ · Q\n → baseline → Advantage\n → learned critic\n → GAE\n → trust-region motivation\n → PPO ratio + clipped surrogate\n```\n\n### 90 分回答的观测闭环\n\n`advantage distribution → ratio tail → clipfrac → approx_KL → entropy → value explained variance → held-out return`。\n\n如果只能背 PPO loss，却解释不了这些指标之间的联动，通常只能算“会用库”，不算真正理解 PPO。'''),
'04-continuous-control':('第四章：DDPG / TD3 / SAC',
'''### 本章学习目标\n\n把连续动作问题理解成“如何优化 Q(s,a) 上的动作”，并掌握 deterministic actor、twin critic、target smoothing、maximum entropy 和 reparameterization 的关系。\n\n### 算法演化\n\n```text\nDQN 无法枚举 continuous argmax\n → DDPG：learned deterministic actor\n → actor exploit critic error\n → TD3：twin Q + delayed actor + target smoothing\n → SAC：stochastic actor + entropy objective + off-policy replay\n```\n\n### 工程高频\n\n动作缩放、tanh squash、Gaussian log-prob Jacobian、Polyak target、Q1/Q2 gap、temperature α、探索噪声与 target noise 的区别。'''),
'05-offline-model-marl-robotics':('第五章：Offline RL / Model-based / MARL / Sim2Real',
'''### 本章学习目标\n\n这一章的统一关键词是 **distribution shift**。Offline RL 是 dataset support shift，Model-based 是 learned dynamics shift，MARL 是其他 agent 造成的 non-stationarity，Sim2Real 是 simulator→real shift。\n\n### 统一分析框架\n\n1. 训练数据/模型覆盖哪里？\n2. learned policy 会走到哪里？\n3. 哪种估计会在 OOD 区域失真？\n4. 算法用 conservatism、uncertainty、factorization 还是 randomization 控制风险？\n5. 如何证明不是只在训练分布上“看起来更好”？\n\n### 项目面要求\n\n能给出 BC baseline、dataset coverage 诊断、Q/OOD 分布、model rollout horizon、opponent pool、domain randomization 范围与真实验证计划。'''),
'06-llm-post-training-rl':('第六章：RLHF / DPO / GRPO / DAPO / GSPO',
'''### 本章学习目标\n\n必须同时掌握 **算法粒度** 与 **系统粒度**：prompt/group、sequence、token 三层统计；actor/old/reference/reward/critic 五类角色；rollout、verifier、learner、weight sync 四个系统 stage。\n\n### 2026 面试主线\n\n```text\nSFT\n → preference / reward modeling\n → PPO-style online RLHF\n → DPO：offline direct preference optimization\n → GRPO：group-relative baseline, remove critic\n → DAPO：修 long-CoT GRPO pathology\n → GSPO：sequence-level importance optimization\n```\n\n### 必须能区分的三个 policy\n\n- **old / rollout policy**：ratio 的 behavior reference；\n- **current policy**：正在更新的 actor；\n- **reference policy**：长期 KL anchor。\n\n把 old 与 reference 混为一谈，是 LLM-RL 面试里非常典型的失分点。'''),
'07-debug-infra-system-design':('第七章：Debug / RL Infra / System Design',
'''### 本章学习目标\n\n从“算法能跑”升级到“训练可解释、可复现、可扩展”。系统题必须回答数据血缘、版本一致性、backpressure、长尾、故障恢复和指标联动。\n\n### Debug 顺序\n\n```text\nData / parser / mask\n → reward / verifier correctness\n → target / stop-gradient / version\n → estimator statistics\n → optimizer / gradient\n → policy distribution\n → system throughput / lag\n → only then hyperparameters\n```\n\n### 典型联动\n\n- reward↑、真实 success↓ → reward hacking\n- KL↑、entropy↓、clipfrac↑ → policy collapse / over-update\n- p99 length↑、GPU util↓ → rollout straggler\n- value loss↑、explained variance↓ → critic failure\n- queue age↑、policy lag↑ → actor/learner imbalance\n''')
}

for slug,(title,extra) in chapters.items():
    p=ROOT/'questions'/slug/'README.md'
    t=p.read_text(encoding='utf-8')
    t=re.sub(r'\n## Repo v2 章节深化.*$', '', t, flags=re.S)
    t += '\n\n## Repo v2 章节深化\n\n'+extra.strip()+'\n'
    p.write_text(t,encoding='utf-8')

# Replace small reference docs with denser professional versions, preserving repo intent.
(ROOT/'references/formula-sheet.md').write_text(r'''# 强化学习公式总表 · Interview Formula Sheet

> 目标：只保留面试中最常需要“现场写出来并解释”的公式。每个公式都附带使用条件与常见误区。

## 1. Return / Value / Advantage

\[
G_t=\sum_{k=0}^{\infty}\gamma^k r_{t+k+1}
\]

\[
V^\pi(s)=\mathbb E_\pi[G_t|s_t=s],\quad
Q^\pi(s,a)=\mathbb E_\pi[G_t|s_t=s,a_t=a]
\]

\[
A^\pi(s,a)=Q^\pi(s,a)-V^\pi(s),\qquad
\mathbb E_{a\sim\pi}[A^\pi(s,a)]=0
\]

**误区**：Advantage 不是新的价值定义，而是以状态基线中心化后的 action value。

## 2. Bellman

\[
V^\pi(s)=\mathbb E_\pi[r+\gamma V^\pi(s')]
\]

\[
Q^*(s,a)=\mathbb E[r+\gamma\max_{a'}Q^*(s',a')]
\]

terminal target：

\[
y=r+\gamma(1-d)V(s')
\]

其中 `d` 必须对应真正不可继续 bootstrap 的终止语义。

## 3. MC / TD / n-step / GAE

\[
\delta_t=r_t+\gamma V(s_{t+1})-V(s_t)
\]

\[
G_t^{(n)}=\sum_{k=0}^{n-1}\gamma^kr_{t+k}+\gamma^nV(s_{t+n})
\]

\[
\hat A_t^{GAE}=\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}
\]

`λ→0` 更接近短 bootstrap；`λ→1` 更接近长 return。

## 4. Importance Sampling

\[
\mathbb E_p[f(x)] = \mathbb E_q\left[\frac{p(x)}{q(x)}f(x)\right]
\]

PPO ratio：

\[
r_t(\theta)=\frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}
=\exp(\log\pi_\theta-\log\pi_{old})
\]

## 5. Q-learning / DQN / Double DQN

\[
Q(s,a)\leftarrow Q(s,a)+\alpha[r+\gamma\max_{a'}Q(s',a')-Q(s,a)]
\]

DQN：

\[
y=r+\gamma(1-d)\max_{a'}Q_{\theta^-}(s',a')
\]

Double DQN：

\[
a^*=\arg\max_aQ_\theta(s',a),\qquad
y=r+\gamma Q_{\theta^-}(s',a^*)
\]

## 6. Policy Gradient / Actor-Critic

\[
\nabla_\theta J(\theta)=\mathbb E[\nabla_\theta\log\pi_\theta(a|s)Q^\pi(s,a)]
\]

baseline 后：

\[
\nabla J=\mathbb E[\nabla\log\pi(a|s)A(s,a)]
\]

## 7. TRPO / PPO

TRPO：

\[
\max_\theta\;\mathbb E[r_t(\theta)A_t]
\quad s.t.\quad
\mathbb E[D_{KL}(\pi_{old}\|\pi_\theta)]\le\delta
\]

PPO：

\[
L^{CLIP}=\mathbb E\left[\min\left(r_t\hat A_t,
\operatorname{clip}(r_t,1-\epsilon,1+\epsilon)\hat A_t\right)\right]
\]

完整实现常见：

\[
L_{total}=-L^{CLIP}+c_vL_V-c_eH(\pi)+\beta KL
\]

## 8. DDPG / TD3 / SAC

DDPG critic target：

\[
y=r+\gamma Q_{\phi^-}(s',\mu_{\theta^-}(s'))
\]

TD3：

\[
y=r+\gamma\min(Q_1^-,Q_2^-)(s',\mu^-(s')+\epsilon)
\]

SAC：

\[
J(\pi)=\mathbb E\left[\sum_t\gamma^t(r_t+\alpha H(\pi(\cdot|s_t)))\right]
\]

## 9. Offline RL

CQL（离散动作直观形式）：

\[
L_{CQL}=L_{Bellman}+\alpha\left(
\mathbb E_s[\log\sum_a e^{Q(s,a)}]-\mathbb E_{(s,a)\sim D}[Q(s,a)]
\right)
\]

IQL 三步：expectile `V` → Bellman `Q` → advantage-weighted BC。

## 10. Reward Model / DPO

RM pairwise：

\[
L_{RM}=-\log\sigma(r(x,y_w)-r(x,y_l))
\]

DPO：

\[
L_{DPO}=-\log\sigma\left(\beta\left[
\log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)}-
\log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}
\right]\right)
\]

## 11. GRPO / LLM RL

组内相对 advantage 的直观形式：

\[
A_i=\frac{r_i-\bar r}{\operatorname{std}(r)+\varepsilon}
\]

要区分：

- old log-prob：用于 policy update ratio；
- reference log-prob：用于 KL anchor；
- group reward：用于相对 baseline；
- token mask：决定哪些 token 真正进入 loss。

## 12. 公式面试自查

现场写任何式子后，强制回答四个问题：

1. 期望对哪个分布取？
2. 哪些量来自 rollout，哪些来自 learned estimator？
3. 哪些项必须 stop-gradient？
4. terminal / padding / response mask 怎么处理？
''',encoding='utf-8')

(ROOT/'references/algorithm-selection.md').write_text('''# 强化学习算法选型 · Decision Guide

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
''',encoding='utf-8')

(ROOT/'references/glossary.md').write_text('''# 强化学习术语表 · Glossary

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
''',encoding='utf-8')

(ROOT/'code/README.md').write_text('''# 手撕代码骨架

这些文件不是完整训练框架，而是面试时应该能独立写出的 **最小核心**。建议顺序：先关掉自动补全自己实现，再运行 tiny test 对比。

| 文件 | 对应题 | 必须理解的 shape / stop-gradient |
|---|---|---|
| `dqn_loss.py` | Q017/Q022 | `[B,A] → gather [B]`，target no-grad，terminal mask |
| `ppo_gae.py` | Q036/Q039/Q048 | `[T,B]` 或 `[B,T]` mask，old logp detach，倒序 GAE |
| `ddpg_losses.py` | Q050/Q051 | critic target no-grad，actor 通过 critic 对 action 求梯度 |
| `td3_target.py` | Q052/Q053 | twin target Q、target action smoothing |
| `sac_losses.py` | Q054/Q055 | reparameterized action、entropy/log-prob、temperature |
| `reward_model_loss.py` | Q073 | pairwise reward difference → log-sigmoid |
| `dpo_loss.py` | Q079/Q080 | chosen/rejected policy-reference log-ratio |
| `grpo_core.py` | Q081/Q083/Q099 | `[B,G,T]`、group normalize、response mask、ratio/clip |

## 手撕代码评分标准

### 60 分：能写出主公式

但没有 shape、mask、terminal、detach 意识。

### 80 分：实现正确

- 明确 tensor shape；
- target 分支 stop-gradient；
- padding/response mask 正确；
- log-space ratio；
- 数值稳定处理 `std≈0`、`log(0)` 等边界。

### 90+ 分：可验证

为核心函数写 3 类 tiny test：

1. **手工可算样例**：2~4 个元素，结果能人工核对；
2. **边界样例**：terminal、全 padding、zero-variance group；
3. **梯度样例**：确认应该有梯度的参数有梯度，target/reference 没梯度。

## 推荐练习顺序

`DQN target → GAE → PPO clip → TD3 target → SAC actor loss → RM → DPO → GRPO`。
''',encoding='utf-8')

print('support docs enhanced')
