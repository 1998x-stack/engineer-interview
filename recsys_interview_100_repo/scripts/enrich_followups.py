from __future__ import annotations
from pathlib import Path
import json,re

ROOT=Path(__file__).resolve().parents[1]
manifest=json.loads((ROOT/'manifest.json').read_text(encoding='utf-8'))

OVERRIDES={
10:["提升来自模型还是数据？","为什么离线涨线上不涨？","如果成本翻倍但指标只涨 0.1% 是否上线？","如何用 ablation 证明每个改动的增量价值？","如何证明短期提升没有牺牲长期价值？"],
25:["索引刷新如何无损切换？","ANN recall 和业务 Recall@K 有何区别？","动态 Item 库如何更新？","动态增量 Item 很多时 HNSW/IVF 如何维护？","为什么 ANN recall 很高但端到端 Recall 仍可能低？"],
30:["推导复杂度为什么从 O(n²d) 变成 O(nd)？","x_i 多数为 0 时还能怎么优化？","数值实现中怎样避免构造所有 pair？","FM 二阶项和直接 pairwise dot 的结果如何验证一致？","在特征数翻倍时，计算和内存如何变化？"],
38:["怎样设计更贴近线上分布的离线评估？","模型 calibration 与 AUC 有什么关系？","如何做 shadow test？","如何设计 offline-online correlation dashboard？","一次 AUC 提升主要来自重度用户，应该上线吗？"],
47:["FlashAttention 是否真正解决了 O(L²)？","为什么 SIM 先 search 再精建模？","HSTU 试图解决的又是什么问题？","序列从 1k 增到 10k 时应该先优化哪个瓶颈？","长序列收益只集中在高活用户时怎么上线？"],
50:["Pre-LN 和 Post-LN 有什么区别？","RMSNorm 与 LayerNorm 有什么区别？","为什么线上 micro-batch 场景更偏向 LayerNorm？","变长序列会如何影响 BatchNorm 统计？","推荐模型里 BatchNorm 什么时候仍然有用？"],
61:["ESCM² 的反事实思想是什么？","中间行为如何建成多阶段转化链？","为什么除法式 pCVR 容易放大误差？","如何比较 ESMM、ESCM² 与普通 CVR baseline？","如果 propensity 本身估计不准怎么办？"],
62:["时长和 CTR 如何做多任务？","完播率为什么有 duration bias？","观看时长重尾分布怎么处理？","分类分桶、回归和分布建模怎么选？","时长模型上线要看哪些 guardrail？"],
75:["最小可检测效应 MDE 是什么？","实验要跑多久？","什么时候应该做 CUPED / variance reduction？","实验跑得越久越可靠吗？为什么不是？","同时看很多指标时如何控制多重检验？"],
85:["hash collision 怎么处理？","INT8 embedding 对召回影响怎么评估？","mixed-dimension embedding 怎么设计？","热 ID/冷 ID 的缓存与存储如何分层？","分布式 embedding sharding 如何保证版本一致？"],
93:["如何定义新内容毕业条件？","探索数据能否直接混入训练？","保量 quota 应该固定还是动态？","如何防作者/内容方利用新内容机制作弊？","新内容策略如何评估长期生态收益？"],
}

# Repair a handful of extraction artifacts even when they are not overridden.
REPAIRS={
'FlashAttention 是否解决了 O(L           )？':'FlashAttention 是否真正解决了 O(L²)？',
'推导复杂度为什么从 n                      变 n？':'推导复杂度为什么从 O(n²d) 变成 O(nd)？',
'ESCM     的反事实思想是什么？':'ESCM² 的反事实思想是什么？',
}

ASSUMPTIONS={
1:'假设请求流量、库存和特征服务的基本约束稳定，且指标变化能通过日志追溯到具体 stage。若库存或流量机制发生结构变化，应先重新定义候选/目标而不是继续调同一模型。',
2:'假设训练负样本、在线竞争集合和索引近似之间有足够 overlap。若 sampling distribution 或 item 库变化，embedding 几何与 ANN 参数都可能需要重估。',
3:'假设特征口径 point-in-time 一致，模型容量是当前瓶颈而非数据/serving。若新增交叉只记忆训练组合或线上特征缺失，离线增益不会迁移。',
4:'假设历史事件能代表兴趣且序列长度确实包含增量信息。若行为噪声大、兴趣极短期或用户历史很短，复杂序列模型可能没有 ROI。',
5:'假设任务之间存在可共享统计强度。若任务目标本身冲突或 label 机制不同，增加共享会加剧 negative transfer，需要私有容量或重新定义任务。',
6:'假设实验随机化和日志采集正确，且用户间干预近似独立。若 SRM、spillover 或频繁窥视结果存在，显著性结论不可信。',
7:'假设 bias/propensity/feature time 能被正确记录。若 logging policy 不可恢复或支持集不重叠，纯离线校正无法可靠恢复反事实。',
8:'假设探索带来的长期信息增益大于短期损失，且有质量/安全 gate。若供给质量低或用户容忍度低，应降低探索强度。',
9:'假设数据、硬件和训练规模足以进入论文所展示的 scaling 区间。若数据小、QPS 低或成本敏感，成熟小模型可能处于更优 Pareto 点。',
}

DEGRADE={
1:'先保核心召回与轻量排序，缩减候选/特征、关闭高成本旁路和复杂重排；保持回退策略与主体验一致，优先保护 P99 和可用性。',
2:'降低向量维度/TopK/nprobe，减少召回路或 hard-negative encoder 成本；用离线 Pareto curve 选择损失最小的降级点，并保留热门/规则 fallback。',
3:'先裁高代价特征和宽层，做蒸馏/量化/低秩；不要盲目砍 embedding lookup 之外的 FLOPs，必须根据 profiler 找瓶颈。',
4:'缩短序列或先 search/summary，再使用轻量 target interaction；高活跃用户可以保留长序列，低活跃用户走小模型。',
5:'减少 expert/hidden size，合并高度相关任务，保留 task heads 与 calibration；避免直接删 guardrail 任务。',
6:'统计方法本身算力不是主瓶颈；应减少不必要 metric 计算但不能牺牲实验健康检查，必要时延长实验而非降低随机化质量。',
7:'优先 cache/locality、量化与 batch/并行优化；数据一致性、版本和监控不能为了省预算被移除。',
8:'保留质量 gate，减少探索比例和复杂集合优化；不能通过取消冷启动保护来“省成本”，否则会形成长期数据债务。',
9:'回退到 hybrid：传统 ANN/小 ranker 全量服务，前沿模型只给高价值流量或离线产生语义特征/teacher signal。',
}

VERIFY={
1:'离线做 stage-wise oracle、候选 overlap 与关键 cohort；线上看 primary metric + latency/negative feedback/retention guardrail，并确保模型、特征、索引版本可追溯。',
2:'离线分 exact Recall、ANN Recall、end-to-end Recall，按热门度/活跃度/新旧 item 分桶；线上看 route marginal recall、candidate count、P99、超时率。',
3:'离线按 user/item/feature freshness 分桶看 AUC/GAUC、calibration 与 latency；线上同时看 score distribution、feature missing、P99 和业务指标。',
4:'按 history length、行为类型、新老用户分桶；线上看序列有效率、缓存、长序列 latency、P99 和长历史用户的真实增量。',
5:'逐任务看 metric/calibration、gradient norm/cosine、gate/expert usage；线上做多目标 A/B，明确 primary 与不可牺牲 guardrail。',
6:'先做 A/A/SRM，实验中看 effect size+CI 而非只看 p-value，按 user cohort/session 分层并预注册停止规则。',
7:'按 propensity/feature freshness/model version 分桶，监控 weight distribution、drift、missing、P99 与 fallback；先排数据质量再解释模型效果。',
8:'看 cold-start cohort、item age、coverage/diversity、探索 regret 和长期留存；线上必须有质量/安全 gate 与探索上限。',
9:'shadow 比较质量、合法 item rate、latency、cost/request、GPU utilization，再 canary/A-B；任何阶段保留成熟 fallback。',
}


def generic_answer(q:str,ch:int)->str:
    s=q.strip()
    # universal repeated questions
    if '隐含假设' in s:
        return ASSUMPTIONS[ch]
    if '离线分桶' in s and 'guardrail' in s:
        return VERIFY[ch]
    if '预算减半' in s or 'QPS/延迟/显存预算减半' in s:
        return DEGRADE[ch]

    # Experiment / metric patterns
    if 'SRM' in s:
        return 'SRM（Sample Ratio Mismatch）是实验实际分组比例显著偏离设计比例。先比较 treatment/control 样本数与期望值，可用卡方检验或平台阈值报警；出现 SRM 时应暂停解释 treatment effect，优先检查分桶、过滤、埋点和资格条件。'
    if '实验污染' in s:
        return '污染指 control 用户受到 treatment 的间接影响，或同一用户/设备跨组。解决靠正确选择 randomization unit、稳定 identity、互斥实验层和 spillover 分析；存在明显网络效应时还需 cluster-level randomization。'
    if '登录前后如何一致' in s:
        return '优先用稳定 user identity；匿名期可用 device/cookie，并在登录合并时制定 deterministic stitching 规则。实验中途 identity 切换最危险，可选择 sticky assignment、冻结首次 bucket 或排除过渡流量，并做跨端污染估计。'
    if '互斥和正交' in s:
        return '把冲突实验放在同一 layer/namespace 内做互斥；可并行实验使用独立 hash salt/层实现近似正交。关键是清楚哪些策略会共同修改同一决策点，不能只靠不同 experiment_id 就假设独立。'
    if 'MDE' in s:
        return 'MDE 是给定显著性水平、统计功效和样本量时可可靠检测的最小真实效应。近似上样本量与 1/MDE² 成正比，所以想把可检测 uplift 从 0.2% 降到 0.1%，样本需求约增到 4 倍。'
    if '实验要跑多久' in s:
        return '由所需样本量、指标方差和业务周期共同决定。通常至少覆盖完整周周期/关键行为延迟；应预先定义停止规则，避免每天看 p-value 后“显著即停”的 optional stopping。'
    if 'CUPED' in s or 'variance reduction' in s:
        return '当有与目标指标强相关、且不受 treatment 影响的实验前协变量时适合 CUPED。用 pre-period metric 做协变量可降低方差、缩短达到同一 MDE 的时间；要验证协变量未被实验污染。'
    if '多重检验' in s:
        return '先明确一个 primary metric，其余作为 secondary/guardrail；大量平行假设需要 Bonferroni/Holm/FDR 等校正或层级检验。否则“看几十个指标总能找到一个显著”会显著抬高假阳性率。'
    if 'A/A 显著' in s:
        return '先查 SRM、随机化、埋点和 metric pipeline；若健康无异常，偶发显著可能是理论假阳性，但若 A/A 反复显著说明方差估计或实验平台有系统问题。'
    if '减少指标方差' in s:
        return '常用更稳定的 randomization unit、CUPED/pre-period covariate、分层随机、winsorization（需预注册）和更长观测窗口。不能为了降方差在看结果后随意删异常样本。'
    if '跑得越久越可靠' in s:
        return '不一定。更久会增加样本，但也会引入 novelty decay、季节性、用户跨组/版本变化和实验干扰；若持续窥视并随时停止，还会破坏经典 p-value 的错误率控制。'
    if 'p-value' in s or '0.1%' in s:
        return '同时报告 effect size、95% CI、基线量级和业务价值。统计显著只能说明与零效应不一致，不能说明 ROI 足够；大流量场景极小 uplift 也可能显著但不值得成本。'

    # Retrieval / sampling patterns
    if 'temperature' in s or 'τ' in s:
        return 'temperature 缩放 logits，控制 softmax 熵与梯度集中度。τ 小会强化 hard negatives 但放大 false negative/噪声；τ 的选择与 embedding norm、batch size、负例难度耦合，应该通过分桶 recall 与训练稳定性调参。'
    if '负例越多' in s:
        return '不是。更多负例通常提高边界信息，但会有边际收益递减，同时增加 false negatives、热门偏差、通信和显存。应比较 effective negatives：去重后难度分布、正负相似度和每新增 1k 负例的 Recall 增益。'
    if '跨卡' in s and 'in-batch' in s:
        return '跨卡 all-gather 可扩大 negatives，但会带来通信同步、重复 item、跨域 batch distribution 和更高 false-negative 率。工程上常 mask duplicate positives，记录 global batch sampling 分布，并评估通信是否抵消 GEMM 收益。'
    if 'sampled softmax' in s:
        return 'sampled softmax 目标更接近对巨大类别 softmax 似然的采样近似，通常显式考虑 sampling probability；InfoNCE 更常表述为正例对一组 negatives 的对比分类。工业实现可非常接近，但解释 score/calibration 时要看是否做了 q(i) correction。'
    if 'logQ' in s:
        return '若负样本按 q(i) 被非均匀采样，训练 logits 会混入“容易被采到”的频率。常见做法从 logit 中减去 log q(i)（具体形式依目标而定），校正 sampling prior，使 score 更接近目标分布下的相对偏好。'
    if 'False Negative' in s or '假负例' in s or 'false negative' in s:
        return '先用 item-id duplicate mask、同用户多正例、语义/类目相似度与后续真实交互估计 false-negative 风险；不要把所有相似负例都过滤，否则会丢 hard negatives。可用 soft label/多正例 loss 做折中。'
    if 'batch size' in s and 'loss' in s:
        return 'batch 变大意味着每个正例竞争的负例数量与分布变化，InfoNCE denominator 变大，梯度和最优 temperature 都可能变化。因此不能只把 batch size 当吞吐参数，应联动学习率、τ 和 sampling correction。'
    if 'MIPS' in s and 'cosine' in s:
        return 'MIPS 最大化内积，向量 norm 会影响排序；cosine 先 L2 normalize，只比较方向。若模型靠 norm 编码热门度/置信度，强制 cosine 会丢信息；若希望稳定几何与 ANN，normalize 反而有利。'
    if 'ANN recall' in s.lower():
        return 'ANN recall 是近似索引相对 exact TopK 的命中率；业务 Recall@K 则看最终候选是否包含真实正例。前者高只能证明索引忠于 embedding，不代表 embedding 本身找对了 item。'
    if '索引刷新' in s or '无损切换' in s:
        return '用 immutable/versioned index：后台构建并 warmup 新索引，完成 exact/ANN sanity check 后原子切换路由；保留旧版本支持秒级 rollback。模型与索引 embedding 必须有兼容 version，避免新 model 查旧 index。'
    if '动态 Item' in s or '增量 Item' in s:
        return '把新 item 分为增量 delta index 与周期主索引，或使用支持 insert/delete 的 HNSW；IVF/PQ 需要额外维护 centroid/quantizer 一致性。应监控 delta 占比，过大时触发 compact/rebuild。'
    if 'embedding norm' in s:
        return '先按 item popularity、频率、类目画 norm 分布与相关性。若 norm 主要编码曝光频率而非偏好，可做 L2 normalize、norm clipping、frequency debias 或把 popularity 独立成特征，再比较 recall/calibration。'
    if 'mixed-dim' in s or 'mixed-dimension' in s:
        return '按 ID 频率/重要性分配不同维度：高频 ID 用较高维，长尾用低维，再通过 projection 对齐下游维度。目标是把容量给有足够样本估计的 ID，同时显著减少内存带宽。'
    if 'INT8 embedding' in s:
        return '同时测量向量重构误差、exact TopK 变化、ANN Recall@K 和线上召回/排序指标；要按热门/长尾 slice，因为低频小 norm 向量可能对量化更敏感。还要测实际 memory bandwidth 与 latency 收益。'
    if 'hash collision' in s:
        return '先控制 hash space/load factor，并对高价值/高频 ID 使用独立表或 collision-free dictionary；长尾可接受共享但要监控冲突率和受影响 slice。多 hash / quotient / feature hashing 都是不同成本折中。'

    # Ranking / feature patterns
    if 'Low-rank rank' in s or 'rank 怎么选' in s:
        return '把 rank 当 expressiveness-cost 超参，做 rank sweep 并画 AUC/GAUC 对参数量和 P99 的 Pareto 曲线。rank 太小形成瓶颈，太大逐渐接近 full matrix 成本；不同 layer 可以不同 rank。'
    if 'Stacked' in s and 'Parallel' in s:
        return 'Stacked 通常让 CrossNet 输出再进入 DNN，强调先显式交叉后深加工；Parallel 让 CrossNet 与 DNN 并行再拼接，保留两种表示路径。选择看 feature interaction 强度与成本，通过 ablation 验证。'
    if 'Leaf-wise' in s:
        return 'Leaf-wise 每次选择全局增益最大的叶继续分裂，训练更快降低 loss，但容易在小样本叶形成很深路径。通过 num_leaves、max_depth、min_data_in_leaf 和正则控制过拟合。'
    if '价格' in s and 'log' in s:
        return '价格常长尾且相对变化比绝对变化更有意义，log1p 可压缩极值并让比例差更线性。仍要保留原值/分桶做 ablation，避免对零值、负值或业务阈值处理错误。'
    if 'OOV' in s:
        return '设置 OOV/UNK bucket 是最低限度；高价值新 ID 可动态建 embedding 或用内容 encoder 生成冷启动表示。需要区分“真正新 ID”和数据字典/特征服务故障导致的 OOV 激增。'
    if 'BatchNorm' in s and 'LayerNorm' in s:
        return 'BN 跨 batch 维统计，适合稳定大 batch 的 dense MLP；LN 在单样本 hidden 维归一，更适合变长序列和在线 micro-batch。选择应按张量语义与 serving batch，而不是“推荐统一用 LN”。'
    if 'RMSNorm' in s:
        return 'RMSNorm 不减均值，只按 root-mean-square 缩放，计算更简洁；很多 Transformer 使用它获得稳定训练。与 LN 的差异通常要通过具体模型验证，不能只凭理论说一定更好。'
    if 'Pre-LN' in s:
        return 'Pre-LN 在子层前归一，残差路径更直接，深网络训练通常更稳定；Post-LN 在子层后归一，原始 Transformer 使用它但深层更易优化困难。最终质量与训练 recipe 相关。'
    if 'calibration' in s and 'AUC' in s:
        return 'AUC 只依赖 score 相对顺序，任何单调变换都不改变 AUC；calibration 关注预测概率与真实频率一致。多目标分数融合、收益估计和阈值决策通常需要良好 calibration。'
    if 'shadow test' in s:
        return '新模型复制真实请求但不影响用户曝光，记录它的候选、score、latency 与异常率，与线上模型做 paired comparison。Shadow 能发现 serving/feature 问题，但不能给出真实 treatment 的因果业务效果，最终仍需 A/B。'

    # Sequence patterns
    if 'softmax' in s and 'DIN' not in s:
        return '是否需要 softmax 取决于权重语义。若希望相对概率分配可归一化；若权重表示独立 activation 强度，强制和为 1 会让序列长度变化产生竞争。DIN 的经典 local activation 不应机械等同标准 softmax attention。'
    if '候选很多' in s and '缓存' in s:
        return '缓存 candidate-independent 的历史 embedding/序列状态，只对 target-dependent interaction 在线计算；更进一步可先筛 target-related history。不要缓存依赖候选的最终 attention，否则候选空间太大。'
    if 'FlashAttention' in s:
        return 'FlashAttention 主要降低 attention 的 HBM IO/中间矩阵存储并提升 kernel efficiency，但标准 dense attention 的 pair 数仍是 O(L²)。因此 L 从 1k 到 10k 时，算法级长序列策略仍然必要。'
    if 'SIM' in s and 'search' in s:
        return '因为 lifelong history 很长，而与当前 target 真正相关的行为通常稀疏。GSU 先以便宜相似度把 10^4~10^5 历史筛到小集合，ESU 才做复杂 target interaction，把算力放到高价值 token。'
    if 'GSU' in s:
        return 'GSU 是不可逆截断：关键行为没召回，ESU 无法凭空补回。因此要单独评估 GSU recall，并用多路 search、较大 M 或联合训练/蒸馏降低截断误差。'
    if '时间间隔' in s:
        return '可使用绝对时间、相对时间 bucket、log-scaled time gap、周期特征和 time decay bias。关键是区分顺序位置与真实时间间隔，因为“相邻 token”可能相隔 1 秒或 1 个月。'
    if 'causal mask' in s:
        return 'next-item/generative 训练通常需要 causal mask 防未来泄漏；如果是对完整历史做双向 encoder 后预测当前候选，可不必严格 causal，但必须保证训练时没有使用预测时不可见的未来事件。'

    # MTL patterns
    if 'expert 数' in s:
        return '从少量 experts 做 sweep，看每任务指标、expert utilization 和 gate entropy。expert 太少无法 specialization，太多会 collapse/负载不均和增加 serving 成本；最终用 Pareto 而非单一 AUC 选。'
    if 'gate 输入' in s:
        return '通常用共享输入/底层表示，也可加入 task/context/domain 特征。gate 输入应能反映“当前样本需要哪类 expert”，但避免使用线上不可稳定获得或泄漏 label 的特征。'
    if 'gate collapse' in s or 'specialization' in s:
        return '画每个 task 的 gate 分布、entropy、top-expert 占比和不同 cohort 使用率；若长期几乎只用一个 expert，说明 collapse。可通过初始化、load-balancing regularization、temperature、expert dropout 或结构调整缓解。'
    if 'GradNorm' in s:
        return '直觉是让各任务在共享参数上的梯度范数/训练速度更平衡，避免某个 loss 因尺度大而主导。它优化的是训练平衡，不自动等于业务权重，线上仍需多指标决策。'
    if '数量级差' in s and 'loss' in s:
        return '先检查 loss 定义和 reduction 是否一致，再做标准化/权重或基于梯度的方法。只把小 loss 乘 1000 可能暂时对齐数值，但应观察共享层 gradient norm 与每任务收敛速度。'
    if 'label 频率' in s:
        return '稀疏任务可用 task-specific sampling、loss normalization、shared representation 和延迟标签处理。不要简单按样本量把稀疏任务权重拉得很大，否则噪声梯度会放大。'
    if 'pCVR' in s and '偏差' in s:
        return 'ESMM 中 pCVR 常通过 pCTCVR/pCTR 的结构约束间接得到；当 pCTR 很小或两者有估计误差时比值会放大误差。此外历史曝光/点击仍可能含策略偏差，后续模型会引入 counterfactual correction。'
    if '加购' in s or '中间行为' in s:
        return '把 impression→click→cart→order 看成多阶段 funnel，可增加对应 task/head 或构建有向转化图，利用条件概率关系共享表示。要注意不同阶段 label delay 和 sample space。'
    if 'duration bias' in s:
        return '完播率天然与视频长度相关：短视频更容易完播。应显式加入 duration、按长度分桶/归一，或联合建模 watch time 与 completion，避免模型系统性偏爱超短内容。'
    if '重尾' in s:
        return '常用 log1p/Huber、分桶分类+期望值、quantile/mixture distribution 或截断/winsorization。选择取决于你是否需要准确期望、尾部风险或排序，而不应默认 MSE。'

    # Metrics patterns
    if 'AUC=0.5' in s:
        return '0.5 表示随机排序水平，1.0 表示所有正例 score 都高于所有负例；低于 0.5 常意味着方向反了或数据/标签有问题。实际推荐要结合用户分组和 TopK 指标。'
    if 'calibration 不影响 AUC' in s:
        return '严格说任何保持排序的单调变换都不改变 AUC，即使概率从 0.1/0.2 变成 0.8/0.9。因此 AUC 高不代表概率可信，logloss/ECE/reliability diagram 才看 calibration。'
    if 'PR-AUC' in s:
        return '当正例极稀疏且重点关心正例检出时 PR-AUC 更敏感，因为 precision 直接受 false positives 影响。它随正例基率变化较大，所以跨数据集比较要谨慎。'
    if 'group 应该按 user' in s:
        return '若排序决策发生在单次 request/session 内，request-level group 更贴近真实竞争集合；若评价长期个性化，可按 user 聚合。必须让 group 与线上“谁和谁竞争”一致。'
    if '全正/全负 group' in s:
        return '该 group 无法形成正负 pair，因此 AUC 未定义。应预先约定过滤，并报告被过滤流量比例；不能默默丢弃导致不同模型口径不一致。'
    if 'HitRate' in s:
        return 'HitRate@K 通常只问 TopK 是否至少命中一个相关 item（0/1），Recall@K 则计算命中的相关 item 数/全部相关 item 数。单正例 leave-one-out 场景二者可能数值相同。'
    if 'MRR' in s:
        return 'MRR 只关心第一个相关结果的倒数排名，适合“尽快找到一个正确答案”；NDCG 可以利用多个相关 item 与多级 relevance，更适合推荐列表整体质量。'
    if 'gain' in s and ('购买' in s or '点击' in s):
        return 'gain 应反映业务相关等级，例如 purchase>cart>click，但权重不宜凭感觉。可基于价值、转化链或线上相关性设计，并做 sensitivity analysis，确认不同映射不会轻易改变模型结论。'
    if 'Time split' in s or '时间采' in s:
        return '训练只用 cutoff 前可见行为，验证/测试使用后续窗口；负样本也要来自当时可曝光/可购买的 item universe，避免把未来上线 item 当过去负例。'

    # Bias / serving patterns
    if 'overlap' in s or 'positivity' in s:
        return 'IPS 需要目标动作在日志策略下有非零概率，即 positivity/overlap。若某类 item 从未被旧策略曝光，propensity=0，纯重加权无法估计其反事实效果，只能靠探索或结构假设。'
    if 'Doubly Robust' in s or s.startswith('DR '):
        return 'DR 结合 outcome model 与 propensity weighting，只要其中一个模型正确就可获得一致性（在标准假设下），通常比纯 IPS 方差更低。但两个模型都错时仍会偏，且实现/诊断更复杂。'
    if 'SNIPS' in s:
        return 'SNIPS 对 IPS 权重做自归一化，用加权和除以权重和，常能降低方差并减小极端权重影响，但会引入有限样本偏差。应同时报告权重分布和 effective sample size。'
    if '概率校准' in s:
        return '可用 Platt/logistic、isotonic、temperature scaling 或分桶校准，并按 user/item/场景 slice 看 reliability。若训练做了负采样，先做 prior correction 再校准通常更合理。'
    if 'Point-in-time correctness' in s:
        return '每条训练样本只能使用该 event_time 当时已经存在的特征值，而不是离线回填后的“最终值”。实现上需要 event-time join、feature version 和回放测试，这是防未来泄漏的核心。'
    if '线上特征回放' in s:
        return '保存原始 event/request 和 feature version，在离线用同一 transform 重放并与线上 dump 的 feature vector 对比；按字段统计 mismatch、missing/default 与数值误差，建立自动 skew test。'
    if 'label 延迟' in s:
        return '定义成熟窗口：未到转化观察期的样本不能直接标负。可用 delayed feedback model、survival/hazard、样本等待或分阶段重训；线上增量训练要避免 premature negative。'
    if '回滚' in s:
        return '模型/特征/索引都用 immutable version，发布走 canary；监控触发阈值后路由原子切回旧版本。在线学习还要能恢复 optimizer/state/feature snapshot，不能只保存权重文件。'
    if '训练窗口' in s:
        return '用 recency-vs-volume 做 sweep：短窗更鲜但方差大，长窗稳定但过时。可采用长窗基座+recency weighting，按 drift 和 cohort 指标选择，而不是固定“7天/30天”经验值。'
    if '概念漂移' in s and '数据异常' in s:
        return '先看原始流量、埋点、feature missing、label rate 是否突变；异常通常是瞬时/局部且伴随管线信号，concept drift 更可能在多源数据一致出现并持续。用 shadow baseline 和多 slice 对照定位。'
    if 'P99' in s:
        return '平均正常但 P99 高通常说明 tail：远程 RPC、cache miss、队列、GC、热点 shard、straggler GPU/kernel。要做 per-stage latency breakdown 和 trace，不要只优化平均模型 FLOPs。'
    if '量化' in s and '线上' in s:
        return '即使离线精度不掉，线上仍可能出现 kernel 不支持导致 fallback、反量化开销、batch-size 敏感、数值溢出、硬件代际差异或 P99 变差，所以必须真实 serving benchmark。'

    # Cold-start/diversity patterns
    if '探索比例' in s:
        return '不应固定拍脑袋；可按用户不确定性、内容年龄和风险动态调。新用户/新 item 高 uncertainty 时多探索，信号稳定后衰减；用 regret、负反馈和长期收益设上限。'
    if '跨 session' in s:
        return '匿名用户可用合规的 device/session cookie 与短期行为状态，登录后按产品规则做 identity merge。必须考虑隐私、过期和共享设备，避免把一个设备永久当成同一人。'
    if 'content-collaborative alignment' in s:
        return '用有交互的老 item 同时获得 content embedding 与 collaborative embedding，通过对比/回归/蒸馏把内容空间对齐协同空间；新 item 只有内容时也能落到可检索位置。'
    if '保量多久' in s or '毕业条件' in s:
        return '不要只按固定时间。可用最小有效曝光/置信区间、质量后验和负反馈阈值决定“毕业”；达到足够证据后转入常规排序，低质则提前退出。'
    if '双冷启动' in s:
        return '只能依赖内容、上下文、热门先验和受控探索，协同信号几乎不可用。可先做语义/地理/时间匹配，通过首屏交互快速更新用户状态和 item 后验。'
    if '曝光集中度' in s:
        return '可看 Gini、Herfindahl-Hirschman Index、top-x% exposure share、catalog coverage 和作者/类目分布。最好同时按供给质量分层，避免把低质库存也当成应该平均曝光。'
    if '新颖性' in s:
        return '多样性强调同一列表内部彼此不同；新颖性强调对该用户而言不熟悉/少见。一个列表可以很多类目但全是用户看过的旧内容，因此 diversity 高而 novelty 低。'
    if '学习 λ' in s:
        return '可把 λ 作为 user/context-conditioned policy，由历史对多样性的接受度、session 阶段和不确定性预测；上线时限制范围并做离线 Pareto + A/B，防止策略学成纯 CTR exploitation。'
    if 'DPP' in s:
        return 'DPP 用集合行列式同时鼓励高质量和彼此不相似，具有概率集合模型解释；MMR 是 greedy relevance-redundancy 线性权衡，更简单可控。DPP 计算和核设计成本更高。'
    if 'Bandit' in s:
        return '普通 A/B 固定随机化估计静态 treatment effect；bandit 根据在线反馈自适应分配流量以优化累计回报。自适应会改变数据分布，离线评估和显著性分析需要相应方法，不能直接套普通 A/B。'
    if '探索数据' in s and '训练' in s:
        return '可以，但必须记录 exploration propensity/policy version。探索流量分布与正常流量不同，直接混入可能改变先验；可加权、分域训练或显式加入 exposure policy 特征。'
    if '作弊' in s:
        return '新内容池要经过质量/安全/去重 gate，按作者/设备/内容相似度做反作弊，并限制单作者探索预算。异常高互动还需检查刷量和互惠行为。'

    # Frontier patterns
    if '长序列' in s and ch==9:
        return 'HSTU/生成式推荐的核心不是无限拉长序列，而是在长序列上保持可扩展计算与高信息密度。需要和截断、search-first、稀疏 attention 做相同 latency/quality 基准。'
    if 'generative framing' in s:
        return '它把用户历史上的行为建成统一 sequence prediction/transduction 目标，使模型可在共享参数上吸收更大数据和更长上下文；但 scaling 优势是否出现取决于数据、tokenization、架构与硬件效率。'
    if 'scaling law' in s:
        return '要固定/系统改变 data、model、compute，并保证训练 recipe、评价集、优化充分度可比；同时检查是否只是更大模型吃到更多 serving 成本。跨公司复现还受数据分布与硬件栈影响。'
    if '十亿 Item' in s:
        return '通常不会直接做十亿类单层 softmax。可用 semantic ID/多级 code、分层 softmax、constrained decoding 或生成簇/码后再实体检索，把巨大类别空间分解。'
    if 'beam search' in s:
        return '可能。成本约随 decode steps×beam×model cost 增长；工业上会用小 beam、并行/缓存、constrained trie、短 code，或让生成式只服务小流量/高价值阶段。'
    if '合法 Item' in s:
        return '用 constrained decoding：trie/FSA 只允许当前 catalog 中有效 code path；解码后再做 availability/safety/business filter，并设置 ANN/传统召回 fallback。'
    if 'codebook size' in s:
        return '大 codebook 减少序列长度但 softmax/量化更难，小 codebook 增加 decode steps。应比较 code collision、reconstruction/retrieval quality、decoding latency 和新 item 增量更新成本。'
    if '唯一映射' in s or 'code 唯一' in s:
        return 'semantic code 负责语义共享时天然可能碰撞；若最终必须唯一，可追加 residual code/leaf ID/原始 ID disambiguation，并维护 code→item 候选表。不要强迫每级 code 本身唯一。'
    if 'MFU' in s:
        return 'MFU 衡量实际模型 FLOPs 相对硬件峰值 FLOPs 的利用率。ranking 常被 embedding、小 GEMM、kernel launch 和内存访问限制；高 MFU 说明架构更能把硬件算力转成有效模型容量，但仍需看端到端成本。'
    if 'quadratic attention' in s or 'token 数小' in s:
        return 'ranking token 数虽然不像 LLM 那么长，但请求 QPS 极高且 feature token 交互小算子多，标准 attention 的投影/softmax/kernel overhead 可能不划算。RankMixer 的重点是更硬件友好的统一 mixing，而非只消除大 L。'
    if 'expert imbalance' in s:
        return '监控每 expert token/request 负载、capacity overflow 和路由熵；用 load-balancing loss、capacity factor、top-k routing、动态路由/专家复制等手段。上线还要避免某 expert 成为热点导致 tail latency。'
    if '过度压缩行为' in s:
        return '会。把长历史总结成一段自然语言可能丢掉频次、顺序和细粒度 item ID。更稳的方法是语义摘要与结构化序列并存，或让 LLM 作为 teacher/feature generator，而不是唯一用户状态。'
    if '蒸馏' in s and ('LLM' in s or 'teacher' in s):
        return 'teacher 可产软 logits、pairwise preference、semantic embedding 或 hard-negative labels；student 双塔用 KL/contrastive/ranking loss 拟合。要在 teacher 可覆盖流量上训练，并单独验证 student 是否保留召回可索引性。'
    if '只允许改一个阶段' in s:
        return '先找 oracle gap 与成本杠杆最大的 stage，而不是默认改精排。若候选 Recall 上限低就先召回；若候选已好但排序差改 rank；若线上被规则覆盖则先重排/策略。用 stage-wise ablation 决策。'
    if 'shadow/canary' in s:
        return 'shadow 只复制流量评估质量/成本/稳定性，不影响用户；canary 给极小真实流量检验端到端风险；再进入正式随机 A/B。每阶段都定义 rollback trigger。'
    if 'GPU 预算减少一半' in s:
        return DEGRADE[9]
    if '增量' in s and '参数' in s:
        return '用 matched-capacity baseline、蒸馏/缩小前沿模型和 stage-wise ablation，比较在相同 latency/cost 下的指标。如果只在参数更多时赢，不能证明新范式本身带来更高 ROI。'

    # General fallback: direct but conservative, tied to chapter.
    return f'回答这类追问时先明确它改变的是数据分布、模型表达、系统成本还是评价口径，再给一个可观测量验证。建议落到本章的验证框架：{VERIFY[ch]}'

for q in manifest['questions']:
    path=ROOT/q['path']
    text=path.read_text(encoding='utf-8')
    m=re.search(r'## 连续追问\n\n(.*?)(?=\n## 自测清单)',text,re.S)
    if not m:
        raise RuntimeError(f'followup block not found: {path}')
    if q['id'] in OVERRIDES:
        items=OVERRIDES[q['id']]
    else:
        raw=re.findall(r'^\d+\.\s*(.+)$',m.group(1),re.M)
        items=[REPAIRS.get(x.strip(),x.strip()) for x in raw[:5]]
    # Ensure exactly five useful prompts.
    defaults=[
        '这个结论依赖哪些隐含假设？如果假设不成立会怎样？',
        '你会用哪些离线分桶与线上 guardrail 验证它？',
        '如果线上收益只集中在一个 cohort，你怎么决策？',
        '如果 QPS/延迟/显存预算减半，你会如何降级？',
        '如何设计一个最小可证伪实验验证你的判断？',
    ]
    for d in defaults:
        if len(items)>=5: break
        if d not in items: items.append(d)
    items=items[:5]
    qlines='\n'.join(f'{i+1}. {x}' for i,x in enumerate(items))
    alines=[]
    for i,x in enumerate(items,1):
        alines.append(f'### 追问 {i}：{x}\n\n{generic_answer(x,q["chapter"])}')
    replacement='## 连续追问\n\n'+qlines+'\n\n## 连续追问参考答案\n\n'+'\n\n'.join(alines)+'\n'
    text=text[:m.start()]+replacement+text[m.end():]
    path.write_text(text,encoding='utf-8')

print('follow-up answer cards added for 100 questions')
