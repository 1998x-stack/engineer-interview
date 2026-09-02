from pathlib import Path
import json, re, textwrap

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT/'data/questions.json').read_text(encoding='utf-8'))

# Primary-source map. Kept deliberately small and authoritative.
PAPERS = {
    'dqn': ('Human-level control through deep reinforcement learning', 'https://www.nature.com/articles/nature14236'),
    'double-dqn': ('Deep Reinforcement Learning with Double Q-learning', 'https://arxiv.org/abs/1509.06461'),
    'dueling': ('Dueling Network Architectures for Deep Reinforcement Learning', 'https://arxiv.org/abs/1511.06581'),
    'per': ('Prioritized Experience Replay', 'https://arxiv.org/abs/1511.05952'),
    'distributional': ('A Distributional Perspective on Reinforcement Learning', 'https://arxiv.org/abs/1707.06887'),
    'rainbow': ('Rainbow: Combining Improvements in Deep Reinforcement Learning', 'https://arxiv.org/abs/1710.02298'),
    'gae': ('High-Dimensional Continuous Control Using Generalized Advantage Estimation', 'https://arxiv.org/abs/1506.02438'),
    'trpo': ('Trust Region Policy Optimization', 'https://arxiv.org/abs/1502.05477'),
    'ppo': ('Proximal Policy Optimization Algorithms', 'https://arxiv.org/abs/1707.06347'),
    'ddpg': ('Continuous control with deep reinforcement learning', 'https://arxiv.org/abs/1509.02971'),
    'td3': ('Addressing Function Approximation Error in Actor-Critic Methods', 'https://arxiv.org/abs/1802.09477'),
    'sac': ('Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor', 'https://arxiv.org/abs/1801.01290'),
    'cql': ('Conservative Q-Learning for Offline Reinforcement Learning', 'https://arxiv.org/abs/2006.04779'),
    'iql': ('Offline Reinforcement Learning with Implicit Q-Learning', 'https://arxiv.org/abs/2110.06169'),
    'qmix': ('QMIX: Monotonic Value Function Factorisation for Deep Multi-Agent Reinforcement Learning', 'https://arxiv.org/abs/1803.11485'),
    'rlhf': ('Training language models to follow instructions with human feedback', 'https://arxiv.org/abs/2203.02155'),
    'dpo': ('Direct Preference Optimization: Your Language Model is Secretly a Reward Model', 'https://arxiv.org/abs/2305.18290'),
    'grpo': ('DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models', 'https://arxiv.org/abs/2402.03300'),
    'dapo': ('DAPO: An Open-Source LLM Reinforcement Learning System at Scale', 'https://arxiv.org/abs/2503.14476'),
    'gspo': ('Group Sequence Policy Optimization', 'https://arxiv.org/abs/2507.18071'),
}

# Question-specific expert notes. Each item is intentionally concise; the renderer expands it
# into derivation/engineering/interview sections rather than adding generic filler.
E = {
1: dict(core='MDP 的关键不是“五元组背诵”，而是把环境的因果接口压缩为状态、动作、转移与奖励。一个状态是否合格，应看它是否足以支持 Markov 化，而不是看它是不是原始观测。', math='从轨迹分布出发：p(τ)=ρ₀(s₀)∏ₜπ(aₜ|sₜ)P(sₜ₊₁|sₜ,aₜ)。RL 的优化对象是由 π 改变的整条轨迹分布，而不是独立样本。', eng=['区分 observation 与 state；POMDP 中 observation 往往不是 Markov state。','设计环境接口时同时定义 terminated 与 truncated，避免把时间截断当真实终止。','奖励、状态、动作的单位/范围需要进入日志与 schema。']),
2: dict(core='Markov 性是“条件独立”而不是“无历史依赖”。历史信息可以存在，只要已经被当前状态充分编码。', math='检验形式：P(sₜ₊₁|s₀,a₀,…,sₜ,aₜ)=P(sₜ₊₁|sₜ,aₜ)。在 POMDP 中可用 belief state bₜ(s)=P(sₜ=s|o₀:ₜ,a₀:ₜ₋₁) 恢复 Markov 表示。', eng=['部分可观测任务可用 frame stack、RNN/Transformer history encoder 或显式 belief state。','如果同一 observation 下最优动作依赖早期历史，通常说明 state representation 不充分。']),
3: dict(core='γ 同时承担数学收敛、时间偏好和有效规划视野三个角色。它不是“越接近 1 越好”的无害超参。', math='有界奖励 |r|≤Rmax 且 γ<1 时，|Gₜ|≤Rmax/(1−γ)。有效 horizon 常用 1/(1−γ) 粗略估计，但真正 credit horizon 还受 episode、λ 与 bootstrapping 影响。', eng=['γ 增大通常放大 target 方差和 value scale。','比较实验时 reward scale、γ、episode length 应一起记录，否则 return 不可横向解释。']),
4: dict(core='V 是策略下“平均动作”的状态价值，Q 是条件于首个动作的价值，A 则是相对于该状态平均水平的中心化增益。A 的中心化性质正是 policy gradient 方差控制的关键。', math='Vπ(s)=Eₐ~π[Qπ(s,a)]，因此 Eₐ~π[Aπ(s,a)]=0。这个零均值性质解释了 advantage 作为 baseline-centered signal 的意义。', eng=['连续动作 actor-critic 中 Q(s,a) 常用于直接优化 actor；PPO 常用 V(s) 形成 GAE。','检查 advantage 是否近似零均值、合理方差，是 PPO debug 的第一批指标。']),
5: dict(core='Bellman expectation equation 是“递归分解 return”的恒等式；它不是某个算法专属更新式。DP、TD、critic 学习都只是对这个固定点方程采用不同估计方式。', math='Vπ(s)=Eπ[rₜ₊₁+γVπ(sₜ₊₁)|sₜ=s]。有限状态下写成向量式 V=Rπ+γPπV，因此 V=(I−γPπ)⁻¹Rπ（可逆时）。', eng=['实现 critic target 时必须 stop-gradient/target network，避免把 target 两端同时更新成错误计算图。','terminal state 应关闭 bootstrap：y=r+γ(1−done)V(s′)。']),
6: dict(core='Expectation equation 评价给定策略；Optimality equation 把下一步策略选择替换为最优算子。两者对应 policy evaluation 与 control 的根本区别。', math='TπV=Rπ+γPπV；T*V(s)=maxₐ E[r+γV(s′)]。T* 在 sup norm 下是 γ-contraction，因此反复应用可收敛到唯一 V*（有限折扣 MDP）。', eng=['max 算子会放大估计噪声，这是 Double Q-learning 动机之一。','离线 RL 中对 OOD action 做 max 尤其危险。']),
7: dict(core='三者最大的区分维度是：是否需要模型、是否 bootstrap、target 的 bias/variance。把它们看成 target construction 的三种方案，比背表格更可靠。', math='MC target=完整 Gₜ；TD(0) target=r+γV(s′)；DP 则对已知 P,R 做期望而非采样。', eng=['短 episode、可并行仿真可容忍 MC；continuing task 常依赖 TD。','模型可知但状态巨大时 DP 仍可能不可行，不能把“有模型”误等于“能做 DP”。']),
8: dict(core='MC 的 target 更接近真实回报但高方差；TD 用当前估计 bootstrap，降低方差并支持在线更新，同时引入 bias。', math='TD 的误差来源可分成 sampling noise 与 bootstrap approximation error；MC 则把整条未来随机性都纳入 target。', eng=['value 初期很差时长 bootstrap 链会传播偏差；但 episode 很长时 MC 的方差与延迟又会显著恶化。']),
9: dict(core='TD error 不只是 value loss 的残差，它还是“当前一步比预期更好/更坏”的局部创新信号，并直接构成 GAE、PER 优先级等方法。', math='δₜ=rₜ+γV(sₜ₊₁)−V(sₜ)。在真实 Vπ 下，E[δₜ|sₜ,aₜ]=Aπ(sₜ,aₜ)（一步条件形式）。', eng=['TD error 爆炸通常先检查 reward scale、terminal mask、target lag 与 value learning rate。','PER 用 |δ| 作为“学习价值”的近似，但需要 importance correction。']),
10: dict(core='Monte Carlo 的核心是用样本均值近似期望，并用大数定律/中心极限定理解释一致性和误差缩放。面试时要能从普通期望自然迁移到 importance sampling。', math='μ=E[f(X)]，μ̂=1/N∑f(Xᵢ)，Var(μ̂)=Var(f)/N；标准误差随 1/√N 缩放。', eng=['报告 MC 结果时应带置信区间而非单个均值。','rare-event 或权重长尾时，增加样本数并不一定是最有效的降方差手段。']),
11: dict(core='n-step return 是从“纯 bootstrap”到“纯采样回报”的连续桥梁。n 增大让真实奖励更快传播，但同时增加方差和 off-policy mismatch。', math='Gₜ⁽ⁿ⁾=∑_{k=0}^{n−1}γᵏrₜ₊ₖ+γⁿV(sₜ₊ₙ)。TD(λ)/GAE 可视为对不同 n-step target 的指数加权。', eng=['分布式 RL 中 n-step 还受 rollout chunk 边界影响，需正确处理 bootstrap value。']),
12: dict(core='on/off-policy 的定义来自“数据分布由谁产生”，不是来自是否有 replay buffer。关键对象是 behavior policy μ 与 target policy π。', math='off-policy 评价通常需要校正 d^μ(s)μ(a|s) 与目标分布，importance ratio π(a|s)/μ(a|s) 是最直接但高方差的校正。', eng=['trajectory 必须带 policy version/log-prob 才能量化 policy lag。','SAC/DQN 可 off-policy 重放；PPO 只能有限复用旧 rollout。']),
13: dict(core='Importance Sampling 把“错误分布下采样”转成加权无偏估计，但代价是权重方差；RL 中高维轨迹的权重乘积尤其容易爆炸。', math='Eₚ[f]=E_q[(p/q)f]。trajectory IS 权重为 ∏ₜ π(aₜ|sₜ)/μ(aₜ|sₜ)，随 horizon 指数式产生高方差；per-decision IS 可缓解。', eng=['实现 PPO ratio 用 exp(new_logp−old_logp)，避免直接概率相除下溢。','监控 ratio 分位数，不只看均值。']),
14: dict(core='SARSA 的 target 跟随实际行为策略，Q-learning 的 target 使用 greedy max。前者学习“带探索的真实行为后果”，后者学习 greedy optimality fixed point。', math='SARSA: y=r+γQ(s′,a′), a′~π；Q-learning: y=r+γmaxₐ′Q(s′,a′)。', eng=['安全控制里 exploration 本身有成本时，SARSA 的行为敏感性常是重要直觉。']),
15: dict(core='探索不是“多加随机性”这么简单，而是让数据覆盖足以区分潜在高价值行为，同时控制探索成本。', math='ε-greedy 是 action-space 随机化；entropy regularization 则直接把 H(π(·|s)) 纳入优化目标。', eng=['探索策略应与动作空间结构匹配：连续控制常用 stochastic policy/parameter noise；稀疏奖励可用 intrinsic reward/curriculum。','评估时要区分 train exploration policy 与 deterministic/low-temperature eval policy。']),
16: dict(core='Q-learning 是 off-policy TD control：利用 Bellman optimality target 学 Q*，不需要环境转移模型。', math='Q←Q+α[r+γmaxₐ′Q(s′,a′)−Q(s,a)]。在表格、充分探索与合适步长条件下可收敛。', eng=['函数逼近后不再自动继承表格收敛保证。','terminal mask、reward clipping/scale、target stale 都会显著影响深度版本。']),
17: dict(core='DQN loss 是对 Bellman optimality target 的回归。terminal mask 决定是否允许从 s′ bootstrap，是最常见且隐蔽的实现错误之一。', math='y=r+γ(1−terminated)maxₐ′Qθ⁻(s′,a′)，L=Huber(Qθ(s,a)−stopgrad(y))。truncated 不一定等价 terminated。', eng=['使用 gather 取已执行 action 的 Q；target 分支必须 no_grad。','Gymnasium 中 terminated 与 truncated 要分开处理。']),
18: dict(core='Experience Replay 解决样本相关性与复用，Target Network 解决 moving target；二者分别从数据分布和优化目标两侧稳定 DQN。', math='在线网络 θ 负责预测/选动作，目标网络 θ⁻ 在一段时间内近似固定 Bellman target。', eng=['replay 太小导致强相关，太旧则 behavior distribution 可能严重失配。','target 更新太快退化为 moving target，太慢则 target stale。']),
19: dict(core='Replay 的价值不只在“打乱相关性”，还在于把一次昂贵环境交互转成多次 SGD 更新；代价是数据陈旧与分布偏移。', math='replay ratio≈每个环境 transition 被用于多少次 gradient update，是 sample efficiency 与 overfitting 的关键系统超参。', eng=['监控 buffer age、action/reward 分布和 replay ratio。','非平稳环境中旧数据可能从资产变成负担。']),
20: dict(core='Target Network 用慢变量把“自举目标”暂时冻结，使回归问题局部上更接近监督学习。', math='hard: θ⁻←θ 每 C 步；Polyak: θ⁻←τθ+(1−τ)θ⁻。后者相当于参数的指数滑动平均。', eng=['不要误把 τ 的定义方向写反；不同代码库常用 tau=0.005 或 polyak=0.995 两种记法。']),
21: dict(core='Deadly Triad 指 function approximation + bootstrapping + off-policy 三者组合可能使 value learning 发散。它解释“为什么 Bellman 方程没错，神经网络 Q-learning 仍会炸”。', math='线性函数逼近下已有经典反例；关键是更新不再是对一个稳定监督目标做 contraction。', eng=['target network、replay、Double Q、保守正则都可视为从不同方向减轻 triad 风险，但不是通用收敛证明。']),
22: dict(core='Double DQN 解耦“谁来选最大动作”和“谁来给这个动作估值”，降低 max 对噪声的系统性正偏。', math='a*=argmaxₐQθ(s′,a)，y=r+γQθ⁻(s′,a*)。与 DQN 的 maxₐQθ⁻ 同时选择和评估不同。', eng=['Double 并不意味着一定有两个完全独立网络；在线/目标网络已经提供了两套参数角色。']),
23: dict(core='Dueling 架构在表示层显式拆 V(s) 与 A(s,a)，特别适合很多动作价值接近、但“状态好坏”更容易先学出的场景。', math='Q=V+A−meanₐA（或减 max）。中心化是为了解决 V/A 不可辨识：给 V 加常数、A 减常数仍得到同一 Q。', eng=['最终仍训练 Q loss；dueling 是网络结构改造，不是新 Bellman target。']),
24: dict(core='PER 用 TD error 近似样本的“当前学习价值”，优先采样高 surprise transition；但这会改变训练分布，因此需要 IS 权重修正。', math='P(i)=pᵢ^α/∑pⱼ^α，wᵢ=(N·P(i))^{-β}。α 控制 prioritization，β 控制 bias correction。', eng=['priority 要防 0：p=|δ|+ε。','极端 outlier 可长期霸占采样，常需 clip 或 rank-based priority。']),
25: dict(core='n-step DQN 让稀疏/延迟 reward 更快传播到前面的 state-action，但 n 越大越依赖 behavior trajectory，off-policy 偏差也越明显。', math='y⁽ⁿ⁾=∑_{k=0}^{n−1}γᵏrₖ+γⁿmaxₐQ(sₙ,a)。', eng=['遇到 episode terminal 要提前截断 n-step 累积；并行 env 要独立维护 n-step queue。']),
26: dict(core='Distributional RL 学 return 随机变量 Z(s,a) 的分布，而不是只学其均值 Q=E[Z]。不同未来风险结构可有相同 Q，但分布学习常提供更丰富的训练信号。', math='distributional Bellman: Z(s,a) ᴰ= R+γZ(s′,A′)。C51 用固定原子 support + projection。', eng=['不要把 distributional RL 等同于 risk-sensitive RL；若最终仍按期望选动作，策略目标可以仍是 risk-neutral。']),
27: dict(core='Rainbow 的意义是“组件互补性实证”：Double、Dueling、PER、multi-step、distributional、NoisyNet 分别处理不同 failure mode。面试应能逐一映射问题，而不是背六个名词。', math='可按四层归类：target bias(Double)、representation(Dueling)、data sampling(PER)、credit propagation(n-step)、return representation(C51)、exploration(NoisyNet)。', eng=['组合算法时要检查超参耦合，例如 PER 与 n-step 会共同改变 TD error 分布。']),
28: dict(core='DQN 不需要 PPO 式 action-probability IS，是因为 Q-learning 的控制 target 本来就是 off-policy Bellman optimality operator；但这不意味着 DQN 永远不需要任何分布校正。', math='PPO 直接优化 E_{a~π}[·]，旧策略数据需 ratio；Q-learning 回归 r+γmaxQ，不要求行为动作来自 target greedy policy。', eng=['PER 仍使用 IS 修正“非均匀 replay sampling”；这是另一种 importance correction。']),
29: dict(core='Value-based 间接通过 argmax(Q) 定义策略；Policy-based 直接参数化 π。连续动作、随机最优策略与受约束策略通常更偏 policy-based。', math='policy gradient 优化 J(θ)；value-based 逼近 Bellman fixed point。两类方法可在 Actor-Critic 中结合。', eng=['动作维数增长时 argmax Q 的计算代价是选择算法的重要因素。']),
30: dict(core='Policy Gradient Theorem 的核心价值是：梯度不需要对未知环境转移 P 求导；只需对策略 log-prob 求导并用 Q/advantage 加权。', math='∇J=E_{dπ(s),a~π}[∇θlogπθ(a|s)Qπ(s,a)]。log-derivative: ∇π=π∇logπ。', eng=['实现离散策略时使用 distribution.log_prob；连续 Gaussian policy 注意 tanh squash 的 log-det Jacobian。']),
31: dict(core='REINFORCE 是 trajectory-level Monte Carlo policy gradient：无 critic、target 简洁，但完整 return 带来高方差和延迟学习。', math='∇J≈∑ₜGₜ∇logπ(aₜ|sₜ)。reward-to-go 比把整条 episode return 给每一步更低方差。', eng=['先做 return normalization/baseline 再谈复杂技巧；否则 scale 常导致训练表面不稳定。']),
32: dict(core='baseline 不改变期望，是因为对 action-independent b(s)，E_{a~π}[∇logπ(a|s)b(s)]=0；它只重排随机梯度的方差。', math='b(s)∑ₐπ(a|s)∇logπ(a|s)=b(s)∇∑ₐπ(a|s)=0。', eng=['baseline 不能依赖当前采样 action，否则一般会引入 bias，除非采用特殊 correction。']),
33: dict(core='Actor-Critic 用 critic 把 MC return 替换为低方差的 value/advantage estimate，代价是 critic bias 会传给 actor。', math='actor: −E[logπ(a|s)Â]；critic: E[(V(s)−Vtarget)²]。', eng=['critic underfit：advantage 噪声大；critic overfit/错误 bootstrap：actor 被系统性误导。','监控 explained variance 比单看 value loss 更有解释力。']),
34: dict(core='A3C 的异步 worker 用参数服务器式更新提升并行探索；A2C 用同步批次换取更一致的梯度与现代 GPU 友好性。', math='两者都用 advantage actor-critic objective，差别主要在 rollout/gradient synchronization 机制。', eng=['现代实现更常 vectorized synchronous env + batched learner，因为 GPU 批处理效率通常优于原始异步 CPU worker。']),
35: dict(core='A3C 不稳定的根源之一是 stale policy/stale gradient：worker 采样和计算期间全局参数已经变化，梯度对应的分布与当前 learner 不一致。', math='policy lag 可用 KL(π_actor || π_learner) 或 parameter/version gap 量化。', eng=['增加 worker 并不保证线性加速；actor throughput 超过 learner 会积压越来越旧的数据。']),
36: dict(core='GAE 是对未来 TD residual 的指数加权，λ 控制从短 bootstrap 到长 return 的 bias-variance tradeoff。', math='Âₜ=δₜ+(γλ)δₜ₊₁+(γλ)²δₜ₊₂+…；δₜ=rₜ+γV(sₜ₊₁)−V(sₜ)。', eng=['必须按 episode/mask 倒序扫描；truncated boundary 是否 bootstrap 取决于环境语义。','advantage normalization 应只在有效 token/steps 上统计。']),
37: dict(core='TRPO 的 trust region 来自“旧策略数据只在新策略足够近时仍可靠”。它用平均 KL 约束近似保证 surrogate improvement 不被大步更新破坏。', math='maxθ E[rₜ(θ)Aₜ] s.t. E[KL(πold||πθ)]≤δ。二阶近似引出 Fisher/Hessian-vector product 与 conjugate gradient。', eng=['TRPO 理论漂亮但实现复杂、吞吐不友好，PPO 因此更流行。']),
38: dict(core='PPO 的设计目标不是“比 TRPO 理论更强”，而是用一阶 SGD + clipped surrogate 近似 trust-region 行为，支持 minibatch 与多 epoch。', math='ratio r=πθ/πold；clip 把极端概率变化带来的 surrogate 改善截平。', eng=['PPO 稳定性来自组合：advantage/GAE、ratio clip、KL 监控、value/entropy、gradient clipping，而不是单独一个 clip。']),
39: dict(core='Clipped objective 是对每个样本构造的悲观 surrogate：只有当新策略的概率变化仍处于可信区域时，优势带来的收益才继续增长。', math='A>0: min(r,1+ε)A；A<0: max(r,1−ε)A（由 min 与负 A 等价推出）。因此正负 advantage 的有效截断方向相反。', eng=['重点监控 ratio p1/p50/p99、clipfrac、approx_kl、advantage std。','clipfrac 高不一定马上失败，但意味着很多样本进入“无继续收益”区，数据利用效率下降。']),
40: dict(core='PPO ratio 是“对同一已采 action，新策略相对 rollout 策略改变了多少概率密度”，不是两个策略整体距离。', math='rₜ=exp(logπnew(aₜ|sₜ)−logπold(aₜ|sₜ))。r=1 表示该 action 概率不变。', eng=['连续动作是 density ratio，不要说成“概率值”而忽略密度。','LLM token 级 ratio 必须只在 response mask 上计算。']),
41: dict(core='PPO 的目标是当前策略下的 policy gradient，但数据来自旧策略，因此 ratio 是显式分布校正；DQN 的 Bellman optimality update 天生允许 behavior 与 target 不同。', math='PPO: E_{a~πnew}[A] 用 old sample 重写为 E_{a~πold}[rA]；Q-learning 不做这个积分重写。', eng=['如果 PPO rollout 太旧，ratio correction 也会因高方差失效，不能把 IS 当无限数据复用许可证。']),
42: dict(core='clip 的对象是 likelihood ratio，并通过 advantage 符号决定哪一侧构成“过度改进”。面试最容易错在把区间理解成直接截断参数或梯度。', math='A>0 时 r>1+ε 不再奖励；A<0 时 r<1−ε 不再奖励。另一侧仍可能产生梯度，因为那代表策略朝错误方向移动。', eng=['画 r 横轴、objective 纵轴的分段函数是最快白板解释法。']),
43: dict(core='完整 PPO 通常是 policy surrogate + value regression − entropy bonus；LLM RL 还常加入 reference KL。每一项负责不同稳定性目标。', math='Ltotal=−Lclip+c_v Lvalue−c_e H + β KL（具体符号按最小化/最大化约定）。', eng=['不同 loss 的数值尺度不同，不能只看总 loss。','共享 backbone 时 value 梯度会影响表征，需要观察 gradient conflict/权重。']),
44: dict(core='一次 backward 在数学上当然可行，只要总 loss 的计算图正确；问题在于参数共享、不同学习率、梯度尺度与 optimizer state 是否需要解耦。', math='若 θshared 同时进入 Lπ 与 Lv，则 ∇θshared L=∇Lπ+c_v∇Lv。', eng=['actor/critic 分离可独立 optimizer；共享 backbone 可用不同 head 与 loss coefficient。','retain_graph 通常不是正确解决重复 backward 的默认方式，先重构计算图。']),
45: dict(core='ratio clip 是局部样本 surrogate 机制，不是全局 KL 硬约束；许多 token/状态的小变化叠加后，整体 policy 仍可能漂移很大。', math='empirical KL 常由 old_logp−new_logp 的样本估计或更精确分布 KL 近似。', eng=['KL 突增时常联动出现 clipfrac↑、entropy↓、ratio tail↑。','可用 target-KL early stop 或 adaptive KL coefficient。']),
46: dict(core='PPO 通过 old log-prob 固定 rollout 分布并用 ratio+clip 做有限的样本复用。每多一个 epoch，新策略离 behavior 更远，bias/variance 与 clip saturation 都会上升。', math='epoch 内 old_logp 不更新；若把 old_logp 每 minibatch 重算成当前策略，会破坏 PPO 的参照。', eng=['监控 epoch 内 KL/clipfrac 演化；后几轮几乎全 clip 时继续训练收益很低。']),
47: dict(core='PPO 的核心缺点是 on-policy rollout 昂贵、critic/advantage 依赖强、超参耦合，以及长序列/大动作空间下 token-level 更新与 sequence reward 的 credit mismatch。', math='sample reuse 受 trust-region 限制；不能像 replay-based off-policy 算法那样任意重放。', eng=['仿真便宜时 PPO 的稳定性常胜过 sample-efficiency；真实机器人或 LLM rollout 昂贵时成本压力更明显。']),
48: dict(core='手撕 PPO 的本质是把数据血缘写对：rollout 时保存 old logp/value/reward/mask，之后固定 old policy 信息，倒序算 GAE，再多 epoch 计算 new logp 和 clipped loss。', math='ratio=exp(new_logp−old_logp.detach())；returns=adv+old_value（或基于 target value 定义）。', eng=['old_logp 未 detach、mask 统计维度错误、done/truncated 混淆、advantage 跨 episode 泄漏是四类高频 bug。','建议对一个极小手工 trajectory 写单元测试。']),
49: dict(core='DQN 的瓶颈是 maxₐQ(s,a)：连续动作上无法枚举，且对一般神经 Q 没有廉价全局 argmax。Actor-Critic 用可微 actor 直接输出候选动作。', math='a=μθ(s) 将“每一步求 argmax”替换为学习一个 amortized optimizer。', eng=['低维连续动作可离散化做 baseline，但维数升高后组合数指数爆炸。']),
50: dict(core='DDPG 是 deterministic actor + off-policy critic。critic 学 Bellman target，actor 沿 Q 对 action 的梯度把动作推向更高价值。', math='y=r+γQφ⁻(s′,μθ⁻(s′)); ∇θJ=E[∇aQφ(s,a)|a=μθ(s) ∇θμθ(s)]。', eng=['actor loss 常写 −Q(s,actor(s)).mean()。','target actor/critic 使用 Polyak averaging。']),
51: dict(core='DDPG 的脆弱性来自“actor 会主动利用 critic 的函数逼近误差”。critic 一旦对某区域虚高，actor 会快速把动作推过去，随后 bootstrap 进一步放大。', math='这是 optimization over estimated Q 引入的 extrapolation/overestimation 问题。', eng=['关注 Q scale、actor saturation、exploration noise 与 critic target 分布。','TD3 的三项改进正对应这些病灶。']),
52: dict(core='TD3 三项改动不是独立 trick 清单，而是统一围绕 function approximation error：双 critic 抑制正偏，delayed actor 给 critic 更多追赶时间，target smoothing 防止策略利用尖锐 Q 峰。', math='y=r+γ min(Q1⁻,Q2⁻)(s′, μ⁻(s′)+clip(ε))。actor 每 d 次 critic update 更新一次。', eng=['target noise 只用于 target action，不等于环境探索噪声。','两个 critic 参数/optimizer 应真正独立。']),
53: dict(core='min(Q1,Q2) 引入受控悲观性，目标是抵消 actor 对正估计误差的系统性选择偏差；平均值不能消除“选最大虚高区域”的驱动力。', math='若 Qᵢ=Q*+εᵢ，min 会降低正偏但可能带来负偏，因此 TD3 是 bias tradeoff 而非无偏估计。', eng=['两个 critic 高度相关时 min 的收益下降；独立初始化/批次路径仍很重要。']),
54: dict(core='SAC 把 reward 与 entropy 同时作为最优性定义，学习随机策略并允许 off-policy replay。entropy 不是仅用于探索的临时 bonus，而是目标的一部分。', math='J=E[∑γᵗ(rₜ+αH(π(·|sₜ)))]；soft value 含 −α logπ 项。', eng=['Gaussian+tanh policy 需做 reparameterization 与 log-prob Jacobian correction。','常用 twin Q + target Q 提升稳定性。']),
55: dict(core='α 是 reward 与 entropy 的拉格朗日式权衡系数。自动温度调节把“目标随机程度”转成优化问题，而不是手工固定探索强度。', math='常见 Lα=E[−α(logπ(a|s)+Htarget)]（按参数化符号约定实现）。', eng=['α 爆高可能表示 target entropy 不合适或 policy log-prob 计算错误。','动作维数变化时 target entropy 通常也需调整。']),
56: dict(core='算法选择要围绕环境交互成本、动作空间、是否允许 replay、稳定性与部署约束，而不是按 leaderboard 排名。', math='PPO：on-policy stochastic；TD3：off-policy deterministic；SAC：off-policy maximum-entropy stochastic。', eng=['昂贵真实交互优先考虑 off-policy；海量廉价并行仿真可优先 PPO。','多峰最优动作或需要随机策略时 SAC 通常比 TD3 更自然。']),
57: dict(core='离散化的主要问题是组合爆炸和控制分辨率/计算量 tradeoff。每维 K 档、d 维动作即 K^d 个组合。', math='若要保持每维误差 ≤ε，K 常随区间/ε 增长，整体动作数指数依赖 d。', eng=['可用 factorized action head 缓解但会引入动作维度独立性假设。']),
58: dict(core='top-k 是 inference-time 截断/重归一化；SAC 的 stochasticity 来自训练 objective 与 learned policy。一个是 decoding heuristic，一个是最优控制定义。', math='top-k 改的是采样分布的 support；SAC 通过 αH(π) 改变训练得到的 π 本身。', eng=['LLM RL 中 temperature/top-p 仍会影响 rollout distribution，因此与 policy learning 的数据分布耦合，但概念上不是 SAC entropy objective。']),
59: dict(core='Offline RL 的约束是训练期间不能通过新交互纠正错误，所以 dataset coverage 与 learned policy distribution shift 成为中心问题。', math='D固定来自 behavior μ；目标 π 若访问 D 中低密度 (s,a)，Q 的 extrapolation error 可能被 policy optimization 放大。', eng=['必须报告 dataset quality/coverage，而不能只报算法。','真实业务还要考虑 logging policy、selection bias 与 action support。']),
60: dict(core='普通 Q-learning 在 offline setting 会对未见动作做 max 并 bootstrap；函数逼近器对 OOD action 的任意误差会被 max 选择并反复放大。', math='a*=argmaxₐQ(s,a) 可落在 μ(a|s)≈0 区域；随后 target 继续用这个 Q。', eng=['观察 learned action 与 dataset action 的距离/密度，是离线 RL 诊断关键。']),
61: dict(core='BC 只拟合 behavior action，不利用 reward 做策略改进；Offline RL 希望在不出 support 太远的条件下利用 reward 对数据内行为重新加权/改进。', math='BC: max E_D logπ(a|s)；AWR/IQL 类方法则用 exp(βA) 对高价值动作提高权重。', eng=['高质量 expert-only 数据上 BC 往往是强 baseline；offline RL 不应默认一定胜过 BC。']),
62: dict(core='CQL 的思想是“对未被数据支持的高 Q 保持悲观”：在 Bellman error 之外加入 Q regularizer，降低 policy 对 OOD action 的虚高估计。', math='离散形式常见 α[E_s log∑ₐexpQ(s,a)−E_{(s,a)~D}Q(s,a)] + Bellman loss。第一项抬高“所有动作”惩罚压力，第二项把数据动作拉回。', eng=['α 太大会过度保守，策略退化接近 behavior。','连续动作下 logsumexp 需用采样近似。']),
63: dict(core='IQL 通过只对 dataset action 训练 Q，并用 expectile V 近似数据内较优动作价值，避免显式对当前 policy 的 OOD action 查询 Q。', math='V 用 expectile regression 拟合 Q(s,a)；Q target=r+γV(s′)；policy 用 exp(β(Q−V)) 加权 BC。', eng=['expectile τ 越高越偏向数据内高 Q action；β 决定 policy improvement 激进程度。']),
64: dict(core='Model-based RL 把环境 dynamics/reward 也作为可学习对象，获得额外 imagined data/规划能力；主要风险是 model bias 在长 rollout 中累积并被 policy exploitation。', math='真实 P 被 P̂θ 代替；k-step imagined rollout 的误差通常随 horizon 累积。', eng=['常限制 model rollout horizon、做 uncertainty penalty/ensemble。','world model 评估不能只看 one-step prediction loss，还要看 rollout calibration。']),
65: dict(core='Reward shaping 的关键是防止改变真正任务目标或制造捷径。Potential-based shaping 给出一种保留最优策略的经典充分结构。', math='F(s,a,s′)=γΦ(s′)−Φ(s)。在标准条件下加入该 shaping 不改变最优 policy 集。', eng=['每个 reward component 单独记录；调权重前先看分布/量纲。','避免可被 agent 独立刷取但与最终成功无关的 dense reward。']),
66: dict(core='稀疏奖励必须先区分 exploration failure 与 credit-assignment failure：没到过成功状态，靠更好 advantage estimator 没用；到过成功但学不回去，才是 credit assignment 更核心。', math='探索类：intrinsic/curriculum/demo/HER；credit 类：n-step/GAE/hierarchical return decomposition。', eng=['统计“成功状态到访率”和“到访后前置动作学习速度”可帮助区分两类问题。']),
67: dict(core='Intrinsic motivation 用预测误差、访问新颖度等内部信号补充外部 reward。noisy-TV 表明“不可预测”不等于“有学习价值”。', math='r=r_ext+βr_int；若 r_int≈prediction error，随机噪声状态可能永久保持高误差。', eng=['使用 episodic novelty、可控性/learning progress 等信号可降低 noisy-TV。']),
68: dict(core='Self-play 的 curriculum 来自对手分布随自身能力共同演化：策略提高后，旧的简单对手逐渐失去训练价值，更强对手自然出现。', math='目标不再是固定 MDP，而是与 opponent policy distribution 共同定义。', eng=['只打最新自己容易循环/遗忘；常维护 opponent pool、league 或历史 checkpoint。','评估必须对固定基准对手集，不能只看 self-play win rate。']),
69: dict(core='MARL 的核心难题包括 non-stationarity、credit assignment 与 decentralized execution。QMIX 用单调 mixing network 让 centralized Q_tot 的 greedy 动作可由各 agent 局部 greedy 一致实现。', math='∂Q_tot/∂Q_i ≥0 ⇒ argmax joint Q 可由各 Q_i 的 argmax 组合（在结构假设下）。', eng=['单调约束提高可分解性但限制表达能力；不是所有协作任务都适合 QMIX。']),
70: dict(core='Sim2Real 的目标不是让 simulator 完美，而是让训练策略对真实系统误差不敏感。Domain Randomization 用参数分布覆盖可能的真实动力学。', math='训练目标变成 E_{ξ~p(ξ)} J(π;M_ξ)，ξ 可包括质量、摩擦、延迟、噪声。', eng=['随机范围过窄覆盖不足，过宽则任务变难且学到过度保守策略。','真实部署前应做 system identification 与安全约束测试。']),
71: dict(core='经典 RLHF 可以拆成三种学习信号：SFT 提供行为先验，preference/RM 提供 sequence-level 目标，RL 在当前 policy 分布上搜索并优化；reference KL 防止策略无约束漂移。', math='常见 RL objective: E_{y~πθ}[rφ(x,y)−β log(πθ(y|x)/πref(y|x))]。PPO 再用 old policy ratio 实现稳定更新。', eng=['区分四个模型角色：actor、reference、reward、critic；它们的参数冻结与显存放置是系统设计核心。','实际系统要记录 prompt→response→reward components→policy version 全链路 provenance。']),
72: dict(core='SFT 只能模仿数据中的 token-level 行为；RL 可以直接优化不可微、sequence-level、交互式的目标，并通过当前 policy rollout 探索 SFT 数据之外的新解。', math='SFT 最小化 −logπ(y*|x)；RL 最大化 E_{y~π}[R(x,y)]，目标与数据似然不再等价。', eng=['可验证任务（代码测试、数学 checker）是 RL 最有价值的区域之一；开放文本无可靠 reward 时 RL 风险更高。']),
73: dict(core='Reward Model 通常把 preference pair 转成相对排序学习。它学习的是“在数据分布上的偏好函数近似”，不是客观真值标量。', math='P(y_w≻y_l|x)=σ(rφ(x,y_w)−rφ(x,y_l)); L=−logσ(r_w−r_l)。', eng=['要做 position/order 随机化、长度偏差分析、annotator disagreement 切片。','RM 评估要包含 policy-generated OOD responses，而不只静态 held-out pair accuracy。']),
74: dict(core='RM 验证准确率高并不能保证被优化时稳健，因为 RL policy 会主动搜索 RM 的误差最大区域；这是“预测模型面对优化器”的 Goodhart/reward hacking 问题。', math='训练数据分布 D_RM 与逐步更新后的 D_π 分离，argmax_y r̂(y) 会放大 r̂−r_true 的局部误差。', eng=['同时跟踪 RM reward 与独立 verifier/human eval 的 gap。','用 reward ensemble、adversarial red-team、online relabeling 减轻。']),
75: dict(core='Reference Model 充当策略先验/锚点，把 reward optimization 约束在原模型附近，降低语言能力漂移和 reward hacking。', math='KL-regularized objective 的最优策略满足 π*(y|x)∝πref(y|x)exp(r(y)/β)（理想化 bandit 形式）。', eng=['reference 通常冻结；log-prob 可离线/在线计算，系统上要权衡显存与吞吐。']),
76: dict(core='RLHF 中 KL 是“性能收益 vs 偏离先验”的控制旋钮。太大说明 update 激进或 reward 强诱导；太小说明 policy 几乎没学或 KL 系数太强。', math='reward shaping 常用 r_total=r_RM−β(logπ−logπ_ref) 的 token/sequence 聚合近似。', eng=['按 prompt 难度/长度切 KL 分布；平均 KL 会掩盖少数极端 response。','自适应 β 可围绕 target KL 调整。']),
77: dict(core='经典 RLHF 采用 PPO 主要因为它能在大随机策略上用一阶优化直接最大化 learned reward，并用 clipping/KL 控制 policy shift；不是因为 PPO 对 LLM 有专属理论最优性。', math='old-policy ratio 允许对 rollout batch 做有限多 epoch 更新；reference KL 是另一层相对 SFT/reference 的约束。', eng=['LLM PPO 的成本来自 actor/reference/reward/critic + autoregressive rollout。','今天应同时能比较 DPO、GRPO 等替代方案。']),
78: dict(core='RM 定义“什么是好输出”，Critic 估计“从当前 prefix 继续下去期望得到多少总 reward”。前者是 objective model，后者是 variance-reduction/value estimator。', math='RM 通常给 sequence reward R(x,y)；critic 学 V(s_t)=E[R_future|prefix_t]，用于 Â_t。', eng=['RM 冻结也可以，critic 必须跟随当前 policy 分布持续训练。']),
79: dict(core='DPO 把 KL-regularized RLHF 的最优策略关系代回 Bradley–Terry preference model，得到只依赖 policy/reference log-ratio 的分类损失，从而绕过显式 RM+online PPO。', math='L_DPO=−logσ(β[(logπθ(yw)−logπref(yw))−(logπθ(yl)−logπref(yl))])。', eng=['chosen/rejected tokenization 与 prompt mask 必须一致。','β 改变偏离 reference 的激进程度；数据噪声/长度偏差仍会被直接学习。']),
80: dict(core='DPO 与 PPO 的关键不是“新旧算法谁更强”，而是 offline preference fitting 与 online reward-driven exploration 的差别。', math='DPO 只在固定 pair D 上优化；PPO/RL 可从当前 π 继续采新 y 并获得 verifier/reward。', eng=['静态人类偏好、成本敏感场景：DPO 类更简单；可验证推理、需要发现新 trajectory：online RL 更有优势。']),
81: dict(core='GRPO 用同 prompt 的一组 completions 构造相对 baseline/advantage，核心收益是去掉单独 value critic，同时让难度差异在 prompt 内部被中心化。', math='对 q 采 G 个 y_i，A_i≈(r_i−mean(r))/std(r)。随后对每个 token 使用 PPO-style ratio/clip（具体实现可有变体）并加 reference KL。', eng=['group size 影响 reward baseline 方差和 rollout 成本。','要统计每组 reward variance、有效组比例、group-level success distribution。']),
82: dict(core='GRPO 省显存的直接来源是移除 critic/value model 及其 optimizer states/activation；但总训练成本不一定同比下降，因为每个 prompt 需要多 completion rollout。', math='PPO memory≈actor+critic(+optimizers)+reference/RM；GRPO 去掉 critic 路径，但增加 G-way sampling。', eng=['判断系统收益要看“显存、rollout tokens、learner FLOPs、wall-clock”四项，而不是只看模型个数。']),
83: dict(core='组内全对/全错时 reward 没有相对差异，中心化 advantage 约为 0，这批 prompt 对 policy-gradient 几乎不提供学习信号。', math='若 r_i=c ∀i，则 r_i−mean(r)=0；即使 std 加 ε，A_i 仍为 0。', eng=['统计 zero-variance group ratio。','Dynamic Sampling 的思想就是减少这类无效 rollout 进入更新。']),
84: dict(core='Rule/verifier reward 优势是可重复、抗 learned-RM 漏洞，缺点是覆盖窄；Neural RM 能评价开放语义但存在偏差、分布漂移和被优化攻击的风险。', math='可组合 R=R_verify+λR_model，但必须注意尺度与可被 exploit 的交互。', eng=['优先“能执行就执行、能严格检查就检查”；LLM judge 更适合作为无法形式化部分的辅助信号。']),
85: dict(core='DAPO 针对大规模长推理 GRPO 的具体 pathology，而不是简单改名：decoupled Clip-Higher、Dynamic Sampling、Token-level Policy Gradient Loss、Overlong Reward Shaping。', math='核心思想分别对应：放宽正向探索的 ratio 上界；过滤零梯度组；改变长短 response 的 loss weighting；将超长截断从硬失败改成更平滑信号。', eng=['监控 entropy、upper/lower clipfrac、zero-variance group ratio、length/reward joint distribution。','实现时必须明确 token-level normalization 的分母是 token 数还是 sequence 数。']),
86: dict(core='GSPO 把 importance ratio 的基本单位从 token 改为 sequence likelihood，希望让优化粒度与 sequence-level reward 更一致，并提升尤其 MoE RL 的稳定性。', math='sequence ratio 可由 response token log-ratio 聚合后指数化（论文定义含长度归一化细节）；同一 response 的 tokens 共享 sequence-level clipping/weighting。', eng=['需要关注长序列下 log-ratio 聚合的数值稳定与长度归一化。','GSPO牺牲部分 token 级细粒度 credit，换取 sequence 一致性。']),
87: dict(core='演化主线可按“价值估计成本”和“优化粒度”理解：PPO=critic+token/action ratio；GRPO=组相对 baseline 去 critic；DAPO=修 long-CoT pathology；GSPO=把 ratio/clip 提升到 sequence 粒度。', math='不要画成严格单线替代关系：这些方法针对的 tradeoff 不完全相同，实际系统可混合其思想。', eng=['面试回答应比较 memory、rollout、stability、credit granularity、zero-signal groups、MoE friendliness。']),
88: dict(core='GRPO 的 KL 通常仍是 policy 对 reference policy 的正则，它与“old policy ratio 用于 PPO-style update”是两个不同参照关系：old 控制本轮更新，reference 控制长期偏离。', math='可写 objective≈L_clip−β KL(πθ||πref)；old_logp 出现在 ratio，ref_logp 出现在 KL。', eng=['日志中分别保存 old_logp 与 ref_logp，混用会产生很隐蔽的训练错误。','KL 的 token 聚合/sequence 归一化会影响长度偏置。']),
89: dict(core='Agentic RL 的 reward 需要把最终任务成功、工具调用合法性、步骤成本和中间状态进展拆开，但必须避免让 dense process reward 成为新的可刷捷径。', math='R=R_terminal+∑ₜw_k rₜ^{(k)}−λ·cost；step reward 可通过 return/GAE 或 outcome redistribution 传到 token。', eng=['工具调用以 step 为自然 credit unit；自然语言 token 是更细粒度执行单元。','记录 tool success、invalid-call、latency、token cost、final success 的联合分布。']),
90: dict(core='长尾 rollout 的系统问题是同步 batch 被最慢序列拖住：大多数 GPU 已完成却等待少数超长 response。解决方向是动态批处理、异步 rollout、长度感知调度与超长策略。', math='同步 step wall-time≈max_i T_i，而有效计算利用取决于 mean(T)/max(T)。尾部越重浪费越大。', eng=['按预测长度 bucketing；continuous batching；异步 producer-consumer；设置软长度惩罚/合理 max tokens。','不要只截断：需评估截断对 reward 与学习信号的偏置。']),
91: dict(core='reward 全 0/1 首先是“数据/验证器/任务难度”诊断题，不应第一反应调学习率。GRPO 里还会直接造成 group advantage 退化。', math='统计按 prompt 的 success rate p；p≈0 或 1 都意味着 Bernoulli reward 方差 p(1−p) 很低。', eng=['先人工抽样 verifier input/output；再看 parser、mask、label leakage；最后才调采样温度/curriculum。']),
92: dict(core='Entropy Collapse 是策略分布过早变尖，探索空间快速收缩。它可能与 reward 上升同时发生，因此不能只用 reward 判断训练健康。', math='H(π)=−E logπ；离散 token 可看 response token entropy/每位置 entropy。', eng=['联动看 entropy↓、KL↑、clipfrac↑、unique response↓。','提高 entropy bonus/temperature、放宽正向 clip 或改善 prompt sampling 都可能缓解。']),
93: dict(core='Reward Hacking 是 policy 优化代理目标的漏洞而非真实目标。它是“模型预测误差 + 强优化”的自然结果，不等同于模型故意作弊。', math='若 R̂=Rtrue+ε，优化 max_y R̂ 会倾向选到 ε 极端为正的区域。', eng=['建立独立 held-out evaluator；追踪 proxy reward 与真实 KPI gap；对高 reward 异常样本做人工/规则审计。']),
94: dict(core='Long-CoT 越来越长常来自 reward 对“更多尝试/更多自检”存在隐性正激励，而 token 成本未被纳入目标；硬截断又会引入不连续惩罚。', math='若 P(correct|length) 上升而 reward 只看 correctness，则最优策略可能把长度推到上限。', eng=['画 reward/accuracy vs length 曲线；加入 token cost、软 overlong shaping、长度分层评估。']),
95: dict(core='大规模 PPO/GRPO 系统的核心是把 rollout、reward、learner、weight sync 解耦，并让每条 trajectory 带完整 policy/version provenance。系统瓶颈常在 autoregressive rollout 而不是 backward。', math='吞吐可粗分：rollout tokens/s、reward eval/s、learner tokens/s；整体受最慢 stage 与同步 barrier 限制。', eng=['组件：prompt sampler→rollout engine→reward/verifier→trajectory store→advantage→learner→checkpoint/broadcast。','必须设计 backpressure、失败重试、去重、版本一致性和 deterministic replay/debug。']),
96: dict(core='Policy Lag 是 actor 采样 policy 与 learner 当前 policy 的差异。系统越异步、learner 更新越快，lag 越大，数据越 off-policy。', math='可用 policy_version gap 或 sampled KL(π_actor||π_learner) 度量。', eng=['设置最大允许 version lag；trajectory 超期丢弃/降权；加快 weight broadcast。','同时监控 queue age，避免只看参数版本。']),
97: dict(core='把游戏“定义成 RL”最难的是状态是否足够、动作是否可学习、reward 是否与胜负一致。工程上还要处理帧率、动作持续时间、部分可观测、对手非平稳与模拟吞吐。', math='最终 objective 应以 win/score return 为主；shaping 只作为学习辅助。', eng=['state 分 self/allies/enemies/map/history；action 可分层；reward components 独立日志。','self-play 要有 opponent pool 与固定评估对手。']),
98: dict(core='LLM Reasoning RL pipeline 应形成闭环：prompt curriculum→多样 rollout→可验证 reward→有效样本选择→policy update→独立 eval→失败簇回流。算法与系统不能分开设计。', math='核心统计单位既有 prompt/group、sequence，也有 token；每层 normalization 必须显式定义。', eng=['至少记录 reward、accuracy/pass@k、KL、entropy、clipfrac、length、zero-variance groups、GPU utilization、policy lag。','eval 与 training verifier 分离可降低 reward overfitting。']),
99: dict(core='手撕 GRPO 要展示数据形状意识：B prompts × G completions × T tokens。group reward 在 G 维归一化，sequence advantage 再 broadcast 到有效 response tokens，ratio/clip 在 token 或算法规定粒度计算。', math='A[b,g]=(r[b,g]−mean_g r)/(std_g r+ε)；ratio=exp(logp_new−logp_old)；loss=−masked_mean(min(ratio*A,clip(ratio)*A))。', eng=['prompt tokens 必须 mask；padding 不参与均值；std=0 要稳定处理；old/ref logp 角色分离。','写 shape assert 与 tiny synthetic test 比多写一层封装更重要。']),
100: dict(core='专业 RL 诊断必须把“数据→估计器→优化→策略分布→真实任务”指标联动起来。单个 loss 或 reward 没有足够因果解释力。', math='常用：return/reward components、advantage/value/Q、ratio/KL/entropy、clipfrac、grad norm、success/pass@k、length/cost。', eng=['建立 joint dashboard：reward↑但 success↓→reward hacking；KL↑+entropy↓→collapse；value loss↑+explained variance↓→critic failure；GPU util↓+p99 length↑→rollout straggler。'])
}

PAPER_BY_Q = {
17:'dqn',18:'dqn',20:'dqn',22:'double-dqn',23:'dueling',24:'per',26:'distributional',27:'rainbow',
36:'gae',37:'trpo',38:'ppo',39:'ppo',40:'ppo',41:'ppo',42:'ppo',43:'ppo',45:'ppo',46:'ppo',47:'ppo',48:'ppo',
50:'ddpg',51:'ddpg',52:'td3',53:'td3',54:'sac',55:'sac',56:'sac',
62:'cql',63:'iql',69:'qmix',71:'rlhf',73:'rlhf',75:'rlhf',77:'rlhf',78:'rlhf',
79:'dpo',80:'dpo',81:'grpo',82:'grpo',83:'grpo',85:'dapo',86:'gspo',87:'gspo',88:'grpo',89:'grpo',90:'dapo',98:'dapo',99:'grpo'
}

CHAPTER_CHECKLIST = {
'01-foundations': ['明确随机变量与条件分布，不把采样值和期望混写。','明确 terminal、horizon、γ 以及状态是否真正 Markov。','能从 return 定义推回 Bellman/TD，而不是只背更新式。'],
'02-value-based': ['区分 online network 与 target network 的角色。','写清 action selection 与 action evaluation 是否由同一估计器完成。','检查 replay 分布、bootstrap mask、Q scale 与 overestimation。'],
'03-policy-gradient-ppo': ['区分采样策略、当前策略、reference/behavior。','所有概率比优先在 log-space 计算。','同时观察 advantage、ratio、KL、entropy、value，而不是只看 reward。'],
'04-continuous-control': ['动作是否经过 squash/scale，log-prob/Jacobian 是否正确。','critic target 与 actor update 的 stop-gradient 边界明确。','区分环境探索噪声、target smoothing noise 与 stochastic policy entropy。'],
'05-offline-model-marl-robotics': ['先描述数据覆盖和行为策略，再谈算法。','明确 OOD action / model bias / non-stationarity 属于哪一类分布偏移。','给出保守性与策略改进之间的 tradeoff。'],
'06-llm-post-training-rl': ['明确 prompt、sequence、token 三种粒度。','明确 old policy、current policy、reference policy 三个角色。','记录 rollout policy version、response mask、reward components、KL/entropy/length。'],
'07-debug-infra-system-design': ['先排数据/实现 bug，再调算法超参。','所有均值都至少配 p50/p95/p99 或按长度/难度切片。','系统吞吐与算法有效样本率必须一起优化。'],
}


def render(q):
    qid=q['id']; e=E[qid]
    ch=q['chapter_slug']
    lines=[]
    lines.append('## 4.3 Repo v2 专业深化：从第一原则理解')
    lines.append('')
    lines.append(e['core'])
    lines.append('')
    lines.append('### 数学/推导抓手')
    lines.append('')
    lines.append(e['math'])
    lines.append('')
    lines.append('> **面试要求**：这里的公式不是“背出来就结束”。需要能解释每个期望是对什么随机变量取、哪些量来自 rollout、哪些量是 learned estimate、哪些分支必须 stop-gradient。')
    lines.append('')
    lines.append('### 工程化检查点')
    lines.append('')
    for x in e['eng']:
        lines.append(f'- {x}')
    for x in CHAPTER_CHECKLIST[ch]:
        lines.append(f'- {x}')
    lines.append('')
    lines.append('### 面试中如何把回答从 70 分提升到 90 分')
    lines.append('')
    lines.append('1. **先给结论**：一句话说明该方法解决的 failure mode。')
    lines.append('2. **再写公式**：只写决定算法差异的那一项，不堆无关符号。')
    lines.append('3. **解释估计误差**：指出 bias、variance、distribution shift 或 optimization instability 从哪里来。')
    lines.append('4. **给反例**：说明算法在哪类数据/环境/系统条件下会失效。')
    lines.append('5. **落到日志**：说清你会看哪些指标来验证判断，而不是“调参试试”。')
    lines.append('')
    return '\n'.join(lines)


def followup_answers(q):
    # Use concise, question-aware answers derived from the expert note instead of inventing new questions.
    f=q.get('follow') or []
    if not f: return ''
    e=E[q['id']]
    out=['## 7.1 高频追问参考答法', '']
    for i, question in enumerate(f,1):
        out.append(f'### 追问 {i}：{question}')
        out.append('')
        # tailored answer seed: core + one relevant engineering observation
        if i==1:
            ans=e['core']
        else:
            ans=e['eng'][0] if e['eng'] else e['math']
        out.append(ans)
        out.append('')
        out.append('回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。')
        out.append('')
    return '\n'.join(out)


def paper_block(qid):
    key=PAPER_BY_Q.get(qid)
    if not key: return ''
    title,url=PAPERS[key]
    return f'''## 11.1 Primary Source 精读建议\n\n- [{title}]({url})\n\n阅读时不要只看摘要。建议至少定位：**problem formulation → objective/algorithm box → ablation → failure/limitation**。面试里真正有区分度的是能把论文中的设计选择与本题的 failure mode 对上。\n'''

for q in DATA:
    p=ROOT/q['path']
    text=p.read_text(encoding='utf-8')
    # Idempotent cleanup for reruns
    text=re.sub(r'\n## 4\.3 Repo v2 专业深化：从第一原则理解.*?(?=\n## 5\.)','',text,flags=re.S)
    text=re.sub(r'\n## 7\.1 高频追问参考答法.*?(?=\n## 8\.)','',text,flags=re.S)
    text=re.sub(r'\n## 11\.1 Primary Source 精读建议.*?(?=\n---\n)','',text,flags=re.S)
    # Insert before section 5
    marker='\n## 5. 工程实现与训练观测'
    if marker not in text:
        raise RuntimeError(f'marker5 missing {p}')
    text=text.replace(marker,'\n'+render(q)+'\n'+marker,1)
    # Insert followup before section 8
    marker8='\n## 8. 易错点'
    if marker8 not in text:
        raise RuntimeError(f'marker8 missing {p}')
    block=followup_answers(q)
    if block:
        text=text.replace(marker8,'\n'+block+'\n'+marker8,1)
    # Insert primary source before final hr/nav
    if paper_block(q['id']):
        # after existing section 11 content, before final ---
        idx=text.rfind('\n---\n')
        if idx==-1: raise RuntimeError(f'final hr missing {p}')
        text=text[:idx]+'\n'+paper_block(q['id'])+text[idx:]
    p.write_text(text,encoding='utf-8')

print(f'Enhanced {len(DATA)} question markdown files.')
