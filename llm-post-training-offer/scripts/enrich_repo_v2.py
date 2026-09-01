from pathlib import Path
import json, re, ast, textwrap, hashlib, csv, subprocess, os, shutil

ROOT = Path('/mnt/data/llm-post-training-offer')
QDATA = json.loads(Path('/mnt/data/questions_parsed.json').read_text(encoding='utf-8'))
qbyid = {q['id']: q for q in QDATA}

# Extract existing focus/formula/pseudocode mappings without importing the destructive builder.
source = Path('/mnt/data/build_repo.py').read_text(encoding='utf-8')
tree = ast.parse(source)
vals = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name):
        name=node.targets[0].id
        if name in {'focus','formula_map','pseudocode','slugs','chapters','priority20'}:
            try: vals[name]=ast.literal_eval(node.value)
            except Exception: pass
focus = vals['focus']; formula_map=vals['formula_map']; pseudocode=vals['pseudocode']; slugs=vals['slugs']; chapters=vals['chapters']; priority20=vals['priority20']

# Per-question expert implementation focus. These are deliberately concrete and non-generic.
specific = {
1:'把后训练拆成“能力是否存在、行为是否被触发、偏好是否一致、环境是否可交互”四层。项目复盘时分别给出 base→SFT→preference/RL 的增益与回退，避免把所有变化都归因于“模型更聪明”。',
2:'检查 label mask 是否只覆盖 assistant token、chat template 是否与推理一致、长回答是否因 token 数获得不成比例梯度。比较 response-only loss 与全序列 loss，能直接暴露实现是否混入 prompt 学习。',
3:'把筛选器做成可校准的多阶段 cascade：规则/哈希先挡廉价错误，模型 judge 处理语义质量，verifier 处理可验证正确性；记录每一级保留率与误杀率，才能做数据 ROI。',
4:'用“有效信息量/token”而不是样本数评价扩容：对重复簇、难度分桶、能力分桶做等 token ablation，并观察 scaling curve 是否已进入低边际收益区。',
5:'构建旧能力 regression suite，并把 forgetting 定义为可量化的 delta；混入 replay 时分别 sweep replay ratio、LR、训练步数，确认是梯度冲突还是单纯过训练。',
6:'把 mixture 当成资源分配优化：每个 domain 维护当前能力、目标能力、数据质量和边际收益估计；定期重估，而不是整个训练周期固定比例。',
7:'对 prompt 做意图级聚类和表述级扰动，分别测“同意图不同问法”的一致性；若只有 lexical diversity 而 intent coverage 不变，增强价值往往有限。',
8:'CoT 管线至少区分 final-answer verifier、过程一致性 judge、格式/语言过滤与去模板化；对正确答案但错误推理的样本单独统计，否则会把伪推理当监督信号。',
9:'先估计初始策略的 success probability 与 pass@k；若在可承受 rollout budget 下几乎采不到正样本，cold-start SFT 比盲目扩大 RL batch 更有效。',
10:'先回答四个门槛：有没有可靠 reward、需不需要探索、偏好数据是否静态、rollout 系统能否承受；再从 SFT/DPO/online RL 中选择，而不是按“先进程度”排序。',
11:'训练 RM 时同时报告 pair accuracy、AUC、calibration、不同 margin 的准确率；BT 假设只给相对效用，不能把 reward 数值跨版本直接比较。',
12:'建立 policy-version→RM-dataset-version 映射；定期用最新 policy 采 hard negatives。若 RM 长期只看旧模型输出，online optimizer 会快速进入 RM 的 OOD 区域。',
13:'对 pair 按 reward/quality margin 和 annotator agreement 二维分桶；最有价值区域通常是“难但可判”的边界，而不是极易 pair 或纯噪声 pair。',
14:'保留 annotator ID 与 confidence，先做 inter-annotator agreement 和分群分析；真实多峰偏好应建模或分层，不应一律当作噪声删除。',
15:'把 RM 当作会被主动攻击的模型：定期对 top-reward 样本做 adversarial audit，并用独立 evaluator 复核；policy 越强，越要缩短 RM 刷新周期。',
16:'每类 hacking 用四元组记录：proxy、模型策略、可观测异常、修复。只有“举例”没有检测与修复路径，面试上通常只能拿基础分。',
17:'不要只监控 mean reward；重点看 reward top-quantile、reward-vs-length/format 相关性、独立 judge gap，以及同一 prompt 的多样性是否塌缩。',
18:'如果引入 PRM，先验证 step label precision，并做“PRM on/off + outcome reward 固定”的 ablation；错误的 dense reward 会比 sparse reward 更系统性地误导策略。',
19:'先把不可违反项变成 gate/constraint，再对可权衡目标做归一化和组合；线性加权前必须处理 reward 尺度漂移，否则一个分量会因数值尺度垄断梯度。',
20:'verifier 要单独做测试集：等价答案、格式扰动、边界值、超时、对抗输出。RLVR 的上限通常先受 verifier precision 限制，再受 policy optimizer 限制。',
21:'在日志里显式记录 rollout policy version、old-policy version、learner step；“PPO 是 on-policy”不是口号，而是要能量化 data age 和每批数据复用次数。',
22:'importance ratio 用 logprob 差计算并先在 log-space 观察分布；极端 ratio 往往不是正常学习，而是版本错位、mask/tokenizer 不一致或 stale rollout 的信号。',
23:'除了 policy loss，还记录 clip fraction、approx KL、ratio p1/p50/p99。若 clip fraction 长期过高，说明更新幅度或数据新鲜度与 PPO 假设不匹配。',
24:'白板上分 A>0/A<0 两种情况逐段分析 min/clip；工程上用构造的正负 advantage toy batch 做单元测试，是避免符号和实现错误的最有效方式。',
25:'critic 需要 value loss、explained variance、value clipping 和 return scale 监控；value loss 下降并不代表 advantage 好，关键看 baseline 是否真正降低 policy-gradient variance。',
26:'GAE 的调参不能脱离 horizon 与 reward sparsity：短任务可用更低 lambda，长稀疏任务通常需要更长信用传播；同时检查 bootstrap 截断是否正确处理 EOS/timeout。',
27:'四个逻辑角色可通过共享底座、冻结、量化或分时加载降低物理常驻成本，但任何共享都会引入耦合；面试要同时说“逻辑角色”和“实际部署方式”。',
28:'KL 的实现需明确 forward/reverse、token-level/sequence-level、是否采样估计；reference tokenizer/template 不一致会让 KL 失去行为锚点含义。',
29:'adaptive KL 的控制器要看 target KL、更新速率与滞后；控制太激进会形成振荡。把它当闭环控制问题解释，比只说“自动调 beta”更专业。',
30:'profile PPO 时分拆 generation、RM inference、critic/actor backward、all-gather/all-reduce、weight sync；通常先找 wall-clock 占比最大的阶段，而不是先改算法。',
31:'DPO 实现最容易错在 chosen/rejected mask、sequence logprob 聚合、reference logprob 缓存和 beta 符号；用可控 toy pair 验证 preference margin 是否朝正确方向更新。',
32:'推导时必须说出 C(x) 为什么在 pair difference 中消掉，以及 BT preference likelihood 如何把不可辨识的 reward 常数消去；这是从公式背诵到真正理解的分水岭。',
33:'DPO 省掉的是在线 rollout/critic/RM 训练闭环，不代表“没有 reward 假设”；implicit reward 仍被 reference 与 preference model 假设约束。',
34:'决策时比较“数据是否覆盖目标策略分布”和“探索是否有价值”。若任务存在可验证新策略空间，online RL 的潜在增益更大；若主要做风格偏好，DPO 往往性价比更高。',
35:'用 policy checkpoint 距离、generation behavior shift 与新旧数据 win-rate 衡量 offline shift；必要时迭代采样/重标，而不是在旧 pair 上无限加 epoch。',
36:'做 length-controlled preference eval，并分别统计 chosen/rejected 长度差；若 DPO win-rate 随长度强相关，先处理数据偏差再调 beta。',
37:'beta 的解释要与 KL-regularized RLHF 的温度联系起来；实际 sweep 时同时画 preference accuracy、KL/reference drift、generation quality，而不是只看训练 loss。',
38:'KTO 的工程价值在于不要求同 prompt pair，但单点 desirable/undesirable 标签的基准与类比例更重要；需检查类别不平衡和 reference anchor 的影响。',
39:'ORPO 把 SFT 与 preference pressure 合并，需关注两个目标是否在同一 batch/长度分布下相互干扰；比较时固定数据和总训练 token，避免“少一个阶段”造成不公平。',
40:'SimPO 的平均 logprob 与 margin 设计缓解长度效应，但不是自动消除所有 length bias；仍要做长度分桶与生成端控制实验。',
41:'GRPO 不是“PPO 去 critic”这么简单：baseline 的统计来源从 learned value 变成同 prompt group；variance、采样成本和可用 reward 结构都随之改变。',
42:'group normalization 要处理 std≈0、reward ties、不同 task reward scale；建议记录 group std 分布与有效 group 比率，而不是只看 global reward。',
43:'算清楚成本转移：critic forward/backward 省掉多少，G 倍 rollout 增加多少；在长 CoT 场景，decode token 往往比省下的 critic 计算更贵。',
44:'sequence reward 广播到每个 token 会把“结果好”视为整条轨迹都好；若过程含冗余/错误修正，token credit 会非常粗。至少比较 token/sequence aggregation 与长度控制结果。',
45:'all-correct/all-wrong group 应单独统计；若比例高，说明题太易/太难或 G/temperature 不合适。Dynamic Sampling 本质是提高有效梯度样本占比。',
46:'G 的选择受 reward 方差、任务难度、temperature、最大长度和预算共同影响；用“单位 rollout token 的有效 advantage 信息”而不是固定 G 经验值比较。',
47:'在异步系统中给每条 trajectory 写入 rollout version、old-logprob source 与 learner version；没有版本追踪，任何 off-policy 诊断都只能猜。',
48:'large batch 的问题不是 batch size 本身，而是排队和更新周期延长导致 data age 增长；监控 staleness histogram 比只记录 batch size 更有解释力。',
49:'同步策略是 throughput—freshness trade-off。可以用最大 version lag、队列 TTL、stale sample drop 和 importance correction 构成分层防线。',
50:'数学/代码适合 GRPO/RLVR的关键是 verifier 高 precision 且成本低；若 verifier 弱，group relative 只会高效放大错误信号。',
51:'回答 DAPO 时必须把每个 trick 对应到具体 failure：Clip-Higher→探索，Dynamic Sampling→无效 group，Token-level loss→长度权重，Overlong shaping→边界噪声。',
52:'观察正向 ratio 的 upper-tail 与 entropy 变化，证明 higher clip 是否真的保留低概率优质动作，而不是简单扩大更新幅度。',
53:'Dynamic Sampling 要考虑数据分布被重新加权：过滤易/极难题提高梯度效率，但也可能改变 curriculum；必须保留原分布 eval，防止只优化中等难度。',
54:'长 CoT 下要明确 denominator 是 sequence、token 还是有效 token；不同 normalization 会隐式改变“长回答每 token 的梯度预算”。',
55:'token-level aggregation 不等同于 token-level reward；前者改变 loss 的权重/归一化粒度，后者改变 credit signal。面试中把二者混为一谈是高频失分点。',
56:'overlong shaping 应画 reward-vs-length 曲线检查是否连续；硬 cliff 会让临界长度附近样本产生高方差甚至错误优化方向。',
57:'GSPO 的关键不是“把 ratio 平均一下”，而是把 policy update 的信赖与 clip 粒度上升到 sequence；这更匹配 sequence reward，并降低 token ratio 极端值的影响。',
58:'长度归一化是对 log-ratio 求 token 平均再指数化；数值上必须在 log-space 聚合，避免直接乘 token probability 的下溢。',
59:'MoE 需额外记录 routing mismatch、expert load 与 train/rollout backend 差异；若 token-level ratio 被 routing perturbation 放大，sequence-level objective 往往更稳。',
60:'DAPO 和 GSPO不是互斥“版本号”：前者是一组 failure-driven recipe，后者改变优化粒度。项目选择应基于观察到的 failure，而不是追新。',
61:'验证“RL 提升 reasoning”时要控制 inference compute：若 RL 模型只是输出更长，能力提升可能来自更多 test-time compute，而非策略本身更优。',
62:'用 base/SFT/RL 的 pass@k、trajectory pattern 与可复现新策略分析“elicitation vs creation”；结论通常是连续谱，而不是二元命题。',
63:'先测 reward/verifier 的可判定率和错误率。开放任务若 judge noise 高，应优先改善评价协议，而不是直接套数学 RL 的 recipe。',
64:'PRM 与 ORM 的比较必须等总 reward compute、等 rollout budget；PRM 的 dense signal 若来自昂贵模型 judge，成本与延迟可能改变最优方案。',
65:'稀疏 reward 先从 curriculum 和 sampling 提高正例率，再考虑 shaping；shaping 一定要检查是否改变了真正最优策略。',
66:'把长度当成本而不是能力 proxy：报告 accuracy-vs-tokens、reward-vs-length、同长度分桶能力，才能判断“思考更久”是否真的更有效。',
67:'熵要按 token position、task、reward quantile 分桶；global entropy 可能掩盖某些关键决策点先发生 collapse。',
68:'训练 reward 是优化器看到的 proxy；评估必须至少有一个独立于训练 reward 的 evaluator，并审计高 reward 尾部行为。',
69:'verifier hacking 要做 adversarial test suite，并把已发现漏洞固化成 regression；仅靠换一个更大 judge，往往只是延后被利用。',
70:'一个可用 reward 设计文档应写清 true objective、proxy、不可抵消约束、scale/normalization、attack surface、cost 和回归评测。',
71:'画 GRPO 数据流时标清每个 tensor 的 producer/consumer、shape、dtype、device 和 version；这能把算法理解直接落到框架实现。',
72:'teacher forcing 可并行处理整序列，decode 必须自回归；因此同 token 数下 rollout 的 wall-clock 与 KV-cache 压力通常更高。',
73:'长尾问题用输出长度 histogram、p95/p99 decode latency、batch active slots、GPU active ratio 联合定位；平均长度不足以解释尾部拖累。',
74:'优化顺序一般是调度→token budget→continuous batching→异步/分离→截断策略；每一步都要复测 useful tokens/s，避免只是让日志上的利用率好看。',
75:'vLLM 的价值来自 KV cache 管理和 continuous batching；在 RL 场景还要考虑频繁权重更新、logprob 一致性与 rollout/learner backend 差异。',
76:'FSDP 对参数/梯度/optimizer state 做分片并引入 all-gather/reduce-scatter；面试应同时解释内存下降和通信/碎片化/重计算代价。',
77:'ZeRO-1/2/3 记忆表只是起点；进一步要能估算每阶段每卡状态量，并解释 stage 越高为什么通信与实现复杂度越大。',
78:'RL 显存需把模型状态、optimizer、activation、KV cache、old/reference logits/logprobs 与临时通信 buffer 分开核算，避免笼统说“四模型”。',
79:'训推分离要有版本协议：何时发布新权重、rollout 如何标记版本、最大 staleness、同步失败怎么处理；没有协议的异步只是在制造不可控 off-policy。',
80:'比较 TRL/verl/OpenRLHF 时不要停在 API：看 execution graph、placement、rollout engine、reward API、sharding、weight sync、async support 与可观测性。',
81:'质量 gate 应覆盖 optimization、policy、reward、capability、behavior、system 六层；每层定义“继续训练/回滚/人工审计”的阈值。',
82:'采用假设树而非调参树：先验 reward bug/泄漏/长度偏差，再查分布差异和饱和，最后才是 optimizer。每一步都要有能否证伪的最小实验。',
83:'KL spike 的第一目标是定位“从哪一步开始分叉”；联合 ratio、clip fraction、grad norm、policy version、reward scale 能快速区分算法更新过猛与数据错位。',
84:'entropy down 不一定坏；关键看 reward/benchmark/diversity 是否同步改善。若 reward plateau 同时 entropy 继续掉，才更像 collapse。',
85:'reward variance 先分解为 task variance、judge noise、length/scale、sampling variance；直接全局 normalize 可能把真实难度信息一并抹掉。',
86:'离线 eval 需要覆盖线上 failure taxonomy；线上 A/B 又必须有安全门槛与回滚。二者是互补的“可重复性 vs 生态真实性”。',
87:'ablation 必须控制 compute/data/token budget；对系统 trick 还要控制 hardware/placement。否则“更好”可能只是多花了 rollout。',
88:'SFT 变好但 RL 变差时，检查 entropy、pass@k、sampling diversity 与初始化 KL；SFT 可能把 policy 锁进一个高似然但探索不足的局部区域。',
89:'hard-example flywheel 要防“只追当前模型盲点”导致分布越来越窄；保留稳定 anchor set，并监控新数据对旧能力的回归。',
90:'用最小复现矩阵定位层级：常量 reward、固定数据、单卡/多卡、同步/异步、冻结 policy。最早导致分叉的层通常就是根因所在。',
91:'Agentic RL 需要明确 state 里包含哪些 observation、tool result、history 和 hidden environment state；state 定义不清，credit 与 Markov 假设都无从讨论。',
92:'长程 credit 可从终局 return、step reward、value、hierarchical option 等多层处理；先确认 reward attribution 是否可信，再追求更“dense”。',
93:'工具数据一定包含 no-tool、wrong-tool、bad-args、tool-error、retry、stop 等负例；只教成功调用会让模型学成“遇事就 call”。',
94:'agent reward 最好采用 success 主目标 + cost/latency 次目标 + invalid/safety hard constraint；任意线性加权会产生“可用成功分抵消非法动作”的漏洞。',
95:'重复调用、无意义搜索、刷中间分都是 tool-loop hacking；除了每次调用 cost，还需要去重、预算、状态机约束与终止条件。',
96:'multi-turn 的数据单位是 trajectory，不是单 response；日志要能回放每个 environment transition，否则失败只能看到终局，无法定位哪一步偏离。',
97:'GRPO 对 critic 难学的长 horizon 有工程吸引力，但 group-level outcome credit 很粗；若有可靠 dense value/process signal，PPO/actor-critic 仍可能更有效。',
98:'process reward 的设计要测“是否帮助任务成功”而不是“是否符合人工偏好的步骤”；过强 shaping 会让 agent 拒绝发现更短或新颖路径。',
99:'70B pipeline 必须把阶段目标、数据来源、模型 checkpoint、reward、GPU budget、eval gate、回滚条件写成 release train；否则只是算法列表。',
100:'项目答辩用决策树：任务→可用数据→reward可靠性→探索价值→credit horizon→系统预算→baseline→failure→升级。最重要的是说出“为什么没选其它方法”。'
}

chapter_expert = {
1:{'objective':'把 base model 的通用能力塑造成目标行为分布','unit':'instruction / response token','bias':'数据选择偏差、模板偏差、遗忘','system':'data pipeline + supervised trainer','scale':'有效 token、质量过滤吞吐、训练 GPU-hours'},
2:{'objective':'把人类/规则偏好映射成可优化的相对质量信号','unit':'pair / response / reward component','bias':'annotator noise、proxy gap、OOD exploitation','system':'label/judge/verifier + RM service','scale':'标注成本、judge latency、reward refresh 周期'},
3:{'objective':'在 KL/信赖约束下做稳定的在线策略改进','unit':'token/action + trajectory return','bias':'advantage variance、critic bias、policy lag','system':'actor/critic/RM/ref + rollout/learner','scale':'rollout tokens、四角色显存、通信与同步'},
4:{'objective':'直接从离线偏好数据调整策略相对 reference 的隐式 reward','unit':'chosen/rejected sequence','bias':'offline distribution shift、length bias、pair noise','system':'policy + reference logprob + preference dataset','scale':'训练 token、reference inference/cache、数据覆盖'},
5:{'objective':'用同 prompt 的组内相对 reward 替代 learned critic','unit':'group / sequence advantage / token logprob','bias':'group degeneracy、粗粒度 credit、staleness','system':'rollout pool + verifier + learner + versioning','scale':'G×rollout tokens、verifier、有效 group 比'},
6:{'objective':'修复 long-CoT/大规模 RL 中的稳定性与粒度失配','unit':'token aggregation 或 sequence ratio','bias':'length weighting、entropy collapse、MoE mismatch','system':'高吞吐 rollout + sequence/token statistics','scale':'长序列 KV cache、有效样本、路由/后端一致性'},
7:{'objective':'让策略通过可验证反馈探索更好的 reasoning trajectory','unit':'trajectory / step / token','bias':'sparse credit、reward hacking、test-time compute confound','system':'sampler + verifier/PRM + evaluation','scale':'pass@k/group sampling、verifier cost、长 CoT'},
8:{'objective':'让 rollout、reward、learner 和权重同步形成高吞吐稳定闭环','unit':'tokens/s、batch、model shard、version','bias':'tail latency、OOM、通信瓶颈、staleness','system':'inference engine + distributed trainer + scheduler','scale':'GPU/节点拓扑、KV cache、network bytes/s'},
9:{'objective':'把异常训练曲线转化为可证伪的分层诊断','unit':'metric slice / checkpoint / minimal repro','bias':'指标混淆、相关≠因果、不可复现','system':'instrumentation + regression + experiment registry','scale':'诊断迭代速度、复现成本、回归覆盖'},
10:{'objective':'在环境交互中优化长程任务成功、效率与安全','unit':'state-action-observation trajectory','bias':'long-horizon credit、environment noise、tool hacking','system':'agent runtime + tools + environment + RL trainer','scale':'environment latency、steps/trajectory、tool budget'}
}

question_profile_override = {
99:{'objective':'设计一个可回滚、可评测、分阶段放大的 70B reasoning 后训练 release pipeline','unit':'training stage / checkpoint / data & reward gate','bias':'阶段间干扰、能力回退、reward/数据版本漂移','system':'SFT + RLVR + preference/safety + Agentic RL + eval/release train','scale':'70B sharding、长 CoT rollout、阶段 GPU budget 与回归门槛'},
100:{'objective':'在任务、reward、探索、credit 与系统预算约束下做可辩护的算法选择','unit':'decision hypothesis / baseline / failure / controlled ablation','bias':'新算法偏好、实验混杂、proxy 与系统成本遗漏','system':'端到端 post-training pipeline + experiment/evaluation stack','scale':'quality-per-compute、稳定性、policy freshness、维护复杂度'}
}

chapter_metrics = {
1:['effective tokens','dedup rate','filter keep-rate','train/heldout loss','capability regression','domain/difficulty coverage'],
2:['pair accuracy','AUC/calibration','reward margin','annotator agreement','reward-vs-length correlation','OOD/top-reward audit rate'],
3:['approx KL','clip fraction','ratio quantiles','entropy','value loss/explained variance','grad norm','data age'],
4:['preference margin','chosen/rejected logprob','implicit reward gap','reference KL','length-controlled win-rate','offline coverage'],
5:['group reward mean/std','effective-group ratio','pass@k','ratio quantiles','entropy','policy-version lag','useful rollout tokens/s'],
6:['entropy','positive/negative clip fraction','effective sample rate','response length p50/p95','sequence ratio','routing mismatch','training stability'],
7:['pass@1/pass@k','verifier precision','reward sparsity','trajectory diversity','accuracy/token','entropy','independent eval gap'],
8:['rollout tokens/s','learner tokens/s','GPU active ratio','p95/p99 latency','peak memory','network bytes/s','weight-sync time','queue depth'],
9:['reward/benchmark delta','KL/entropy/grad norm','metric slices','seed variance','regression failures','time-to-reproduce'],
10:['task success','steps/trajectory','tool calls','invalid-action rate','retry rate','latency/cost','environment failure rate','long-horizon success']
}

chapter_case = {
1:'假设你在做一个 32B 通用助手的 SFT，原始池 300 万条，最终只能训练 30 万条；你的设计必须回答“删谁、留谁、怎么证明删得对”。',
2:'假设 preference 数据来自三种来源：人工标注、强模型 judge、规则 verifier；三者成本与噪声不同，你需要设计可校准的 reward pipeline。',
3:'假设 32B 模型使用 PPO 做 RLHF，训练出现 KL 抖动和 GPU 利用率不足；需要同时从目标函数与系统数据流定位。',
4:'假设你有 50 万 preference pairs，但无法持续在线 rollout；你需要证明 offline preference optimization 的收益与边界。',
5:'假设数学 reasoning 任务每个 prompt 采 8 条长 CoT，verifier 是 0/1；你需要在 rollout 成本、group 信号与稳定性之间取舍。',
6:'假设模型平均 CoT 从 1k 增长到 8k tokens，并且是 MoE；原先 GRPO 训练开始出现 entropy 下降、ratio 尾部异常与吞吐恶化。',
7:'假设数学/代码任务有可靠终局 verifier，但过程 reward 不完美；你要决定 credit 粒度、探索强度与 anti-hacking 方案。',
8:'假设 64 张 GPU 上 rollout 与 learner 分池运行，生成长度重尾、权重同步昂贵；目标是提升 useful tokens/s 而不显著增加 policy lag。',
9:'假设某次 RL 实验 reward 稳定上涨，但 held-out benchmark 3 天不动；你不能“再跑一轮看看”，必须设计最小诊断矩阵。',
10:'假设 agent 需要搜索、代码执行和结构化 API，多轮最长 30 steps；最终成功率稀疏且工具调用有真实成本。'
}

level_rubric = {
1:'能给出准确边界与核心定义；如果只能背名词，不足以通过算法面。',
2:'除定义外，需要解释机制、一个 failure mode 和一个可执行实验。',
3:'需要能推导/拆解目标函数，讨论 bias-variance 或系统 trade-off，并给出监控指标。',
4:'需要能处理反例、实现细节、分布式/规模化约束，并从 failure 反推方法选择。'
}

def qfile(qid):
    ch=(qid-1)//10+1
    folder=chapters[ch][0]
    return ROOT/'docs'/folder/f"q{qid:03d}-{slugs[qid]}.md"

def clean(s):
    return re.sub(r'\s+', ' ', (s or '')).strip()

def metrics_for(q):
    ch=(q['id']-1)//10+1
    mets=chapter_metrics[ch][:]
    t=(q['title']+' '+q.get('core','')+' '+q.get('deep','')).lower()
    specials=[]
    for kw,ms in [
        ('length',['length histogram','reward-length correlation']),('entropy',['entropy by position/task']),('kl',['KL target/error']),
        ('reward',['reward quantiles','reward calibration']),('rollout',['queue depth','data age']),('moe',['expert load balance','routing mismatch']),
        ('fsdp',['all-gather time','shard memory']),('zero',['optimizer/grad/param shard bytes']),('dpo',['chosen-rejected margin']),
        ('group',['group std','tie rate']),('tool',['tool success/error rate']),('data',['data keep-rate','contamination rate'])]:
        if kw in t: specials+=ms
    out=[]
    for x in specials+mets:
        if x not in out: out.append(x)
    return out[:8]

def expert_block(q):
    qid=q['id']; ch=(qid-1)//10+1; prof=question_profile_override.get(qid, chapter_expert[ch])
    core=clean(q['core']).rstrip('。；;'); deep=clean(q['deep']).rstrip('。；;'); foc=focus[qid]; sp=specific[qid]
    mets=metrics_for(q)
    formula=formula_map.get(qid,'')
    pseudo=pseudocode.get(qid,'')
    metrics_table='\n'.join([f"| {i+1} | `{m}` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |" for i,m in enumerate(mets)])
    if formula:
        math_note=f"本题已有白板公式。专业回答应继续说明：**优化变量是谁、期望/归一化是按 token 还是 sequence、数据由哪个 policy 采样、极端值如何被 clip/normalize、公式假设在异步系统中何时失效**。"
    else:
        math_note="本题未必需要单一闭式公式，但仍应把关键量形式化：输入分布、优化对象、约束、成本与观测指标。能把工程问题写成可测量变量，本身就是算法能力的一部分。"
    code = pseudo if pseudo else f'''```text
# Interview-to-engineering skeleton for Q{qid:03d}
def investigate(problem):
    assumptions = define_scope(problem)
    baseline = build_minimal_baseline(assumptions)
    metrics = instrument(baseline)
    failure = reproduce_and_slice(metrics)
    hypothesis = connect_failure_to_mechanism(failure)
    result = run_controlled_ablation(hypothesis)
    return validate_on_heldout_and_regression(result)
```'''
    return f'''<!-- V2_EXPERT_START -->
## 15. V2 专业进阶：从“会答”到“能做研究/工程”

> **内容属性**：本节是基于 PDF 原始提要的扩展讲义。它不是对 PDF 原文的复述，而是把本题展开到真实后训练项目所需要的假设、实现、诊断与实验层级。

### 15.1 把题目还原成一个可研究的问题

本题不能停在“{core}”。更专业的表述是先确定五个对象：

| 维度 | 本题应明确的内容 |
|---|---|
| Optimization objective | {prof['objective']} |
| Statistical unit | {prof['unit']} |
| 关键估计误差 | {prof['bias']} |
| 系统承载 | {prof['system']} |
| Scale variable | {prof['scale']} |

对 **Q{qid:03d}**，最关键的机制判断是：**{foc}**

再进一步，工程上真正需要落地的是：{sp}

### 15.2 机制链：输入 → 估计 → 更新 → 行为 → 评测

建议把本题按下面的因果链讲清楚：

1. **输入分布**：样本/trajectory 来自哪里？是否与当前 policy 一致？是否存在 selection bias？
2. **训练信号**：监督标签、preference、reward、advantage 或系统指标具体由谁产生？噪声和尺度如何控制？
3. **优化更新**：哪个参数被更新？梯度是按 token、sequence、group 还是 trajectory 聚合？
4. **行为变化**：模型概率分布应该发生什么方向的变化？若没有发生，优先怀疑哪一层？
5. **独立验证**：至少使用一个不参与训练信号构造的 held-out evaluator，避免“训练 proxy 自证成功”。

本题 PDF 的深入结论是：{deep}。把它变成研究问题时，需要追问：**哪一个可观测量能够证伪这句话？** 如果无法设计证伪实验，说明理解仍停留在概念层。

### 15.3 数学与数值实现的专业要求

{math_note}

工程上建议始终保存原始统计量，不要只保存均值。例如 ratio/reward/length/KL 至少保留分位数或 histogram；大量 RL failure 都发生在尾部，而不会先体现在 mean 上。

## 16. 工程实现：最小可验证闭环

{code}

### 16.1 实现检查表

- **数据身份**：每条样本能追溯 `dataset_version / prompt_id / policy_version / reward_version` 中适用的字段。
- **mask 与长度**：明确 prompt token、response token、padding、EOS、truncation 是否进入 loss/reward/normalization。
- **数值稳定**：logprob 差优先在 log-space 计算；标准化必须显式加 epsilon；极端值要记录而不是静默丢弃。
- **可复现性**：模型 checkpoint、tokenizer/chat template、随机 seed、生成参数、verifier 版本全部进入实验元数据。
- **独立评测**：训练 reward/judge 与最终评测至少有一层独立实现或独立数据。
- **失败可回放**：保留能还原单条 trajectory 的最小日志，而不是只有 aggregate dashboard。

### 16.2 一个真实项目场景

{chapter_case[ch]}

如果面试官把本题放进这个场景，回答时不要先给算法名。先给**约束、基线和最小实验**，再说明为什么某个算法/数据策略是由 failure mode 推出来的。

## 17. 指标仪表盘与实验设计

### 17.1 本题优先监控的指标

| # | 指标 | 如何解释 |
|---:|---|---|
{metrics_table}

### 17.2 推荐的三层实验

**Layer A — correctness test**：在 toy data / 小模型上验证符号、mask、归一化、版本和边界条件。例如把 reward 固定成常量、构造全对/全错 group、手工设置正负 advantage，确认梯度方向。

**Layer B — mechanism ablation**：固定模型、数据、总 token、rollout budget、seed，只改本题对应机制。目标不是追最高点，而是验证预期中间量是否变化，例如 entropy、group std、clip fraction、length distribution。

**Layer C — scaling test**：在更长 context、更大模型、更大 batch、更异步的设置下验证结论是否保持。很多方法在单机 toy case 正确，但在 policy lag、MoE routing 或重尾长度下失效。

### 17.3 怎样避免“伪 ablation”

- 总训练 step 相同但 rollout token 不同，不是等 compute。
- 数据条数相同但平均长度不同，不是等 token。
- 一个方案使用更强 judge/verifier，不能把增益全部归因于 optimizer。
- 系统吞吐变快导致看到更多样本，也会改变学习曲线；算法质量与系统效率需要拆开报告。

## 18. 反事实、边界条件与方法比较

### 18.1 三个必须会回答的反事实

1. **如果去掉本题机制，最早会坏哪个指标？** 先说中间量，再说最终 benchmark。
2. **如果把模型/长度/batch 放大 10×，哪个假设最先失效？** 优先考虑 estimator variance、memory、communication、policy freshness 与 evaluator reliability。
3. **如果训练 reward 很好但独立评测不涨，怎样证明不是 reward hacking 或数据泄漏？** 给出 held-out evaluator、行为切片、top-reward audit 与污染检查。

### 18.2 与相邻题目的关系

本题不是孤立知识点。它应被放回本章主线：**{prof['objective']}**。面试中如果能主动说明“当前方法解决了什么 failure，同时引入了什么新成本/新偏差”，通常比继续罗列算法名更有区分度。

### 18.3 常见高级误区

- 把论文中的**目标函数**当成完整系统；真实结果还取决于 sampling、版本、mask、normalization、scheduler 与 evaluator。
- 把 correlation 当 causal evidence；例如长度与 reward 同涨，不等于“更长 reasoning 导致能力提升”。
- 只比较最终分数，不比较 compute、variance、稳定性和回归项。
- 只描述成功 recipe，不解释它在什么分布、模型规模和 verifier 假设下成立。

## 19. 面试评分 Rubric：怎样从 60 分答到 95 分

| 档位 | 面试表现 |
|---|---|
| 60–70 | 能复述核心结论：{core} |
| 70–80 | 能解释机制，并写出适用的公式/数据流；知道一个主要 failure mode。 |
| 80–90 | 能给出工程实现、关键监控指标、最小 ablation，并讨论 bias/variance 或系统成本。 |
| 90–95+ | 能处理反事实和规模化约束；从真实 failure 反推算法选择；能说明为什么**不选**另一个常见方案。 |

**本题难度 L{q['level']} 的最低合格线**：{level_rubric.get(q['level'],level_rubric[4])}

## 20. 复习与项目化清单

在认为自己“掌握 Q{qid:03d}”之前，至少能独立完成：

- [ ] 不看资料给出 30 秒结论，不混淆概念边界。
- [ ] 白板写出关键公式/变量关系，逐项解释数据从哪里来。
- [ ] 画出端到端数据流，并标出最可能的三个 failure point。
- [ ] 给出至少一个能证伪自己判断的 controlled ablation。
- [ ] 给出一组线上/离线监控指标，以及一个异常时的排查顺序。
- [ ] 用自己的项目数字重述本题：模型规模、数据量、G/长度、GPU、吞吐、收益或回归。
- [ ] 回答“为什么不用另一种方法”，并明确 trade-off 而不是说“效果更好”。

<!-- V2_EXPERT_END -->'''

# Insert V2 block into each question markdown.
for q in QDATA:
    p=qfile(q['id'])
    text=p.read_text(encoding='utf-8')
    text=re.sub(r'\n?<!-- V2_EXPERT_START -->.*?<!-- V2_EXPERT_END -->\n?', '\n', text, flags=re.S)
    marker='\n---\n\n['
    idx=text.rfind(marker)
    if idx<0:
        idx=len(text)
    text=text[:idx].rstrip()+"\n\n"+expert_block(q)+"\n\n"+text[idx:].lstrip()
    p.write_text(text,encoding='utf-8')

# Enrich chapter READMEs with a standalone dashboard.
for ch,(folder,title,desc) in chapters.items():
    p=ROOT/'docs'/folder/'README.md'
    text=p.read_text(encoding='utf-8')
    text=re.sub(r'\n?<!-- CHAPTER_V2_START -->.*?<!-- CHAPTER_V2_END -->\n?', '\n', text, flags=re.S)
    prof=chapter_expert[ch]
    met='\n'.join([f'- `{m}`' for m in chapter_metrics[ch]])
    qids=range((ch-1)*10+1,ch*10+1)
    high=[f'Q{i:03d}' for i in qids if i in priority20]
    block=f'''<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：{prof['objective']}
- **Unit of optimization**：{prof['unit']}
- **主要统计偏差**：{prof['bias']}
- **系统载体**：{prof['system']}
- **规模化变量**：{prof['scale']}

### 本章必须会看的指标

{met}

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：{', '.join(high) if high else '以章节内 L3/L4 题为主'}。

### 章节级案例

{chapter_case[ch]}

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->'''
    # Insert before final nav/separator if possible, else append.
    idx=text.rfind('\n---\n')
    if idx<0: idx=len(text)
    text=text[:idx].rstrip()+"\n\n"+block+"\n\n"+text[idx:].lstrip()
    p.write_text(text,encoding='utf-8')

# Additional high-value guide pages.
research_methodology = '''# 后训练研究方法论：从现象到可证伪实验

> 这份页面解决一个比“背算法”更重要的问题：**当训练真的出问题时，如何形成可以被实验否证的判断。**

## 1. 研究闭环

```mermaid
flowchart LR
    O[Observation 现象] --> H[Hypothesis 假设]
    H --> P[Prediction 可观测预测]
    P --> A[Ablation 最小实验]
    A --> E[Evidence 证据]
    E --> D[Decision 决策]
    D --> R[Regression 固化]
    R --> O
```

一个专业 post-training 实验不是“改一个超参看分数”，而是：

1. 现象必须能被复现，并且有明确时间点/样本切片。
2. 假设必须对应机制，而不是“可能是学习率”。
3. 假设必须产生一个**中间量预测**，例如 clip fraction 上升、group std 下降、data age 增大。
4. ablation 只改一个因子，并控制 token/compute/evaluator。
5. 结论需要同时覆盖 quality、behavior、stability、system cost。
6. 修复后把 failure case 进入自动 regression。

## 2. 四层假设树

| 层 | 典型问题 | 最小隔离方法 |
|---|---|---|
| Data | 分布、污染、难度、长度、标签错 | 固定 checkpoint，换干净小数据 |
| Reward/Objective | proxy、scale、mask、normalization | 常量/人工 reward、toy batch |
| Optimizer/Algorithm | ratio、clip、advantage、KL | 单卡、同步、固定 old policy |
| System | staleness、通信、OOM、backend mismatch | 单卡 vs 多卡；同步 vs 异步 |

## 3. 三种最常见的伪因果

### 3.1 “reward 涨，所以模型变好”

训练 reward 是优化器直接看到的 proxy。必须用独立 evaluator 验证，并审计 top-reward tail。

### 3.2 “长 CoT 涨，所以 reasoning 变强”

必须做 length-controlled evaluation 或 accuracy/token；否则可能只是更多 test-time compute。

### 3.3 “新算法更好，因为最终分更高”

如果新算法使用了更多 rollout tokens、更强 verifier 或更长训练，就不能把增益归因于 objective。

## 4. 一份合格实验记录必须包含

- Git commit / model checkpoint / tokenizer / chat template
- dataset/reward/verifier/policy version
- generation config：temperature、top-p、max tokens、G
- optimizer config：LR、beta、clip、epochs、batch/token budget
- system config：GPU、节点、sharding、rollout backend、sync policy
- 中间统计：ratio、KL、entropy、reward、length、group std、data age
- 结果：held-out benchmark、行为回归、system throughput
- 失败案例与下一步假设

## 5. 与 100 题的使用方式

每道题的 V2 专业进阶都给出 correctness test、mechanism ablation 与 scaling test。复习时不要把它们当附加阅读，而应把它们变成你自己的“实验设计口述题”。
'''
(ROOT/'docs'/'00-guide'/'research-methodology.md').write_text(research_methodology,encoding='utf-8')

implementation_checklist = '''# 后训练工程实现检查表

这份 checklist 用于 code review、实验启动前检查和面试项目复盘。

## Data / Tokenization

- [ ] tokenizer、special token、chat template 与 reference/rollout/learner 完全一致。
- [ ] 明确 loss mask：prompt、assistant、tool observation、padding、EOS、truncated token。
- [ ] 数据可追溯到 source/version；train/eval contamination 有独立检查。
- [ ] 长度、领域、难度、语言、来源分布进入 dashboard。

## Policy / LogProb

- [ ] old/current/rollout/reference policy 角色与版本能区分。
- [ ] logprob 在相同 tokenization、mask 与 precision 下计算。
- [ ] ratio 使用 log-space 差，保存 p1/p50/p99 和极端样本。
- [ ] 对 padding/EOS/工具 token 的 ratio/advantage 处理有单元测试。

## Reward / Verifier

- [ ] reward scale、normalization、clipping、missing/timeout 明确定义。
- [ ] verifier 有独立 adversarial/regression set。
- [ ] reward top tail 定期人工或独立 judge 审计。
- [ ] 训练 evaluator 与最终 evaluator 至少一层独立。

## Distributed / System

- [ ] peak memory 分解到 param/grad/optimizer/activation/KV/buffer。
- [ ] rollout tokens/s、learner tokens/s、GPU active ratio、queue depth、p99 latency 可观测。
- [ ] weight sync 有版本号、失败恢复与最大 staleness 策略。
- [ ] 单卡/多卡数值一致性有 smoke test。

## Evaluation / Release Gate

- [ ] benchmark 不只看总分，按任务/难度/长度/语言切片。
- [ ] 记录 KL、entropy、长度、拒答、格式、diversity 等行为指标。
- [ ] 关键能力 regression 设硬门槛。
- [ ] 发布前有 reward hacking/verifier hacking 专项测试。
'''
(ROOT/'docs'/'00-guide'/'implementation-checklist.md').write_text(implementation_checklist,encoding='utf-8')

whiteboard = '''# 白板训练：后训练算法岗 12 组必画图 / 必推公式

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
'''
(ROOT/'docs'/'11-playbooks'/'whiteboard-drills.md').write_text(whiteboard,encoding='utf-8')

expdesign = '''# 实验设计 Playbook：如何证明一个 Post-Training 改动真的有效

## 1. 先写“预注册式”实验卡

在开跑前写清：

- Hypothesis：机制假设是什么？
- Prediction：哪个中间量先变化？
- Primary metric：最终判断指标是什么？
- Guardrails：哪些能力不能回退？
- Compute control：如何保证 token/GPU-hours/verifier 等价？
- Stop condition：什么情况提前判定失败？

## 2. 常用对照矩阵

| 问题 | A | B | 需要固定 |
|---|---|---|---|
| 数据筛选有效吗 | raw mixture | filtered mixture | 有效 token、steps、model |
| DPO beta 是否合适 | beta1 | beta2 | pairs、reference、steps |
| GRPO G 是否值得 | G1 | G2 | 总 rollout token budget |
| DAPO trick 是否有效 | off | on | 其它 trick、compute |
| 系统调度是否有效 | scheduler A | B | workload、hardware、quality |
| PRM 是否有效 | ORM | ORM+PRM | reward compute、rollout budget |

## 3. 结果报告模板

不要只报“+2.3”。至少报告：

- quality：pass@1/pass@k/win-rate/benchmark
- behavior：length、entropy、diversity、format/safety
- optimization：KL、ratio、clip fraction、grad norm、group std
- system：tokens/s、GPU active ratio、memory、p99、staleness
- cost：GPU-hours、rollout tokens、judge/verifier calls
- regression：下降的能力与失败样本类别

## 4. 结论写法

专业结论应该是：

> 在固定 X/Y/Z 的条件下，改动 A 使中间量 M 朝机制预期变化，同时主指标 P 提升、guardrail G 不回退；增益在 seed/长度/难度分桶中保持，代价是 C。因此证据支持“机制 H 在当前设置下成立”，而不是笼统声称“A 优于 B”。
'''
(ROOT/'docs'/'11-playbooks'/'experiment-design.md').write_text(expdesign,encoding='utf-8')

glossary='''# Glossary：LLM Post-Training 核心术语

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
'''
(ROOT/'docs'/'12-appendix'/'glossary.md').write_text(glossary,encoding='utf-8')

# Expand root README with V2 section.
rp=ROOT/'README.md'
r=rp.read_text(encoding='utf-8')
r=re.sub(r'\n?<!-- README_V2_START -->.*?<!-- README_V2_END -->\n?', '\n', r, flags=re.S)
readme_block='''<!-- README_V2_START -->
## V2：Professional Deep-Dive Edition

这一版把每道题从“面试笔记”升级成**可独立阅读的研究/工程知识卡**。每个 Q001–Q100 新增：

- 问题形式化：objective / statistical unit / bias / system / scale；
- 机制链：input → signal → update → behavior → evaluation；
- 数学与数值实现要求；
- 最小可验证工程闭环与真实项目场景；
- 指标 dashboard、correctness test、mechanism ablation、scaling test；
- 反事实与 10× scale 思考；
- 60→95 分面试评分 Rubric；
- 可勾选的项目化掌握清单。

新增全局资料：

- [后训练研究方法论](docs/00-guide/research-methodology.md)
- [工程实现检查表](docs/00-guide/implementation-checklist.md)
- [白板训练 12 组](docs/11-playbooks/whiteboard-drills.md)
- [实验设计 Playbook](docs/11-playbooks/experiment-design.md)
- [核心术语 Glossary](docs/12-appendix/glossary.md)

> **来源边界**：每题原有“PDF 原始提要”保持来源标记；新增 V2 内容明确标记为扩展讲义，不伪装成 PDF 原文或逐字真题。
<!-- README_V2_END -->'''
insertpos=r.find('\n## ')
if insertpos==-1: insertpos=len(r)
r=r[:insertpos]+"\n\n"+readme_block+"\n"+r[insertpos:]
rp.write_text(r,encoding='utf-8')

# Expand central guide files with pointers / professional reading protocol.
for rel, block in {
'docs/00-guide/README.md':'''## V2 · 专业版阅读协议\n\n每道题至少经过四次：**定义复述 → 白板推导 → failure-driven 追问 → 项目数字复盘**。优先把“为什么成立、何时失效、如何证伪”说清，再追求术语覆盖。\n\n推荐同时使用：[研究方法论](research-methodology.md) · [工程实现检查表](implementation-checklist.md) · [白板训练](../11-playbooks/whiteboard-drills.md)。''',
'docs/00-guide/knowledge-map.md':'''## V2 · 依赖关系的读法\n\n把知识图谱视为依赖 DAG：SFT/Data 是数据分布基础；RM/Verifier 定义优化信号；PPO/DPO/GRPO 等定义更新机制；DAPO/GSPO 是 failure-driven 修正；RL System 决定这些公式是否在真实吞吐和版本一致性下成立；Eval/Debug 决定你能否证明改动有效；Agentic RL 把 horizon 与环境交互进一步放大。''',
'docs/00-guide/core-formulas.md':'''## V2 · 公式不只要“会写”\n\n每个公式都按六问检查：**随机变量从哪里采样？谁是优化变量？baseline/reference 是谁？归一化粒度是什么？数值尾部怎么处理？异步/分布式后哪个等式只剩近似？** 这六问比再背十个变体更接近实际算法面试。''',
'docs/00-guide/algorithm-evolution.md':'''## V2 · Failure-Driven 决策原则\n\n不要把 PPO→GRPO→DAPO/GSPO 画成“新算法替代旧算法”的时间线。更准确的是：**critic 成本、group 退化、长序列权重、entropy、MoE/back-end mismatch、policy freshness** 分别触发不同修正；只在观测到对应 failure 时升级方法。''',
'docs/00-guide/scoring-rubric.md':'''## V2 · 95 分回答的证据结构\n\n高分回答至少形成一条完整链：**定义 → 公式/机制 → 中间量预测 → failure → 指标 → controlled ablation → scale trade-off → 为什么不选替代方案**。如果缺“中间量预测”和“证伪实验”，即使术语很多也仍然接近背诵。'''
}.items():
    p=ROOT/rel; txt=p.read_text(encoding='utf-8')
    marker='<!-- GUIDE_V2 -->'
    if marker in txt:
        txt=txt.split(marker)[0].rstrip()+"\n"
    txt += f"\n\n{marker}\n{block}\n"
    p.write_text(txt,encoding='utf-8')

# Update docs index with new resources.
p=ROOT/'docs'/'index.md'; txt=p.read_text(encoding='utf-8')
if 'research-methodology.md' not in txt:
    txt += '''\n\n## V2 专业版工具箱\n\n- [研究方法论：从现象到可证伪实验](00-guide/research-methodology.md)\n- [后训练工程实现检查表](00-guide/implementation-checklist.md)\n- [白板训练：12 组必画图/必推公式](11-playbooks/whiteboard-drills.md)\n- [实验设计 Playbook](11-playbooks/experiment-design.md)\n- [Glossary](12-appendix/glossary.md)\n'''
p.write_text(txt,encoding='utf-8')

# Update mkdocs nav with new docs if not already present.
mk=ROOT/'mkdocs.yml'; m=mk.read_text(encoding='utf-8')
# Safer: insert under guide/playbooks/appendix anchors by simple string replacement when missing.
if 'research-methodology.md' not in m:
    m=m.replace('      - 评分标准: 00-guide/scoring-rubric.md', '      - 评分标准: 00-guide/scoring-rubric.md\n      - 研究方法论: 00-guide/research-methodology.md\n      - 工程实现检查表: 00-guide/implementation-checklist.md')
if 'whiteboard-drills.md' not in m:
    m=m.replace('      - RL 系统排障: 11-playbooks/rl-system-debug.md', '      - RL 系统排障: 11-playbooks/rl-system-debug.md\n      - 白板训练: 11-playbooks/whiteboard-drills.md\n      - 实验设计: 11-playbooks/experiment-design.md')
if 'glossary.md' not in m:
    m=m.replace('      - 参考资料: 12-appendix/references.md', '      - 参考资料: 12-appendix/references.md\n      - Glossary: 12-appendix/glossary.md')
mk.write_text(m,encoding='utf-8')

# Enrich playbooks/appendix markdowns with a consistent professional footer.
for p in list((ROOT/'docs'/'11-playbooks').glob('*.md')) + list((ROOT/'docs'/'12-appendix').glob('*.md')):
    txt=p.read_text(encoding='utf-8')
    if '<!-- PROFESSIONAL_FOOTER -->' not in txt:
        txt += '''\n\n<!-- PROFESSIONAL_FOOTER -->\n## 使用建议\n\n把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。\n'''
        p.write_text(txt,encoding='utf-8')

# Add a reproducible enrichment script into the repository.
scripts_dir=ROOT/'scripts'
shutil.copy2('/mnt/data/enrich_repo_v2.py', scripts_dir/'enrich_repo_v2.py')

# Update changelog.
cp=ROOT/'CHANGELOG.md'; c=cp.read_text(encoding='utf-8')
entry='''\n## v2.0.0 — Professional Deep-Dive Edition\n\n- Q001–Q100 全部新增专业进阶讲义：问题形式化、机制链、数值实现、工程闭环、指标、三层实验、反事实、评分 Rubric、项目化清单。\n- 10 个章节 README 新增工程/研究 Dashboard。\n- 新增 research methodology、implementation checklist、whiteboard drills、experiment-design、glossary。\n- 保留 PDF 原始提要与扩展讲义的来源边界。\n- 增加可复现 `scripts/enrich_repo_v2.py`。\n'''
if 'v2.0.0' not in c:
    c=c.rstrip()+"\n"+entry
cp.write_text(c,encoding='utf-8')

# Refresh data index with size stats and V2 flag.
qjson=ROOT/'data'/'questions.json'
if qjson.exists():
    data=json.loads(qjson.read_text(encoding='utf-8'))
    if isinstance(data,list):
        for row in data:
            qid=int(str(row.get('id','0')).replace('Q',''))
            if 1<=qid<=100:
                f=qfile(qid)
                row['professional_v2']=True
                row['markdown_chars']=len(f.read_text(encoding='utf-8'))
        qjson.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

# Rebuild manifest excluding .git and manifest itself.
manifest=[]
for f in sorted(ROOT.rglob('*')):
    if not f.is_file() or '.git' in f.parts or f.name=='MANIFEST.sha256': continue
    h=hashlib.sha256(f.read_bytes()).hexdigest()
    manifest.append(f"{h}  {f.relative_to(ROOT).as_posix()}")
(ROOT/'MANIFEST.sha256').write_text('\n'.join(manifest)+'\n',encoding='utf-8')

print('V2 enrichment complete')
