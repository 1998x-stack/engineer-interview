from __future__ import annotations
from pathlib import Path
import json, re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))

# Each entry is intentionally question-specific.  The chapter templates below add
# a shared systems lens, while these notes prevent the handbook from degenerating
# into generic boilerplate.
PROFILES: dict[int, dict[str, str]] = {
1:{'deep':'工业推荐不是一条“模型链”，而是一条受 SLA、候选规模、特征新鲜度、实验平台共同约束的数据闭环。真正的系统边界从曝光日志开始，到下一轮样本构造结束。','case':'假设短视频库有 5 亿条内容：多路召回合并约 5,000 条，粗排压到 600，精排打 600 条，重排输出 20 条。若精排单样本 0.2 ms，则直接扫全库需要约 10^8 ms，分层是计算复杂度决定的，不只是组织习惯。','boundary':'分层越多并不一定越好。每增加一层都引入候选截断误差、版本一致性、特征口径和超时降级问题；低库存、低 QPS 场景可能用更扁平架构更合理。'},
2:{'deep':'四阶段本质是四种不同优化问题：召回追求覆盖，粗排追求单位成本淘汰效率，精排追求个体效用估计，重排追求列表级效用与约束。它们的目标函数、特征预算和延迟预算不同。','case':'若召回 Recall@5000 从 92% 降到 80%，精排再强也找不回已被截掉的正例；反过来召回 99% 但精排排序错误，最终 CTR 仍不会提升。因此要做 stage-wise oracle 分析。','boundary':'“精排分最高的 TopK 就展示”只在几乎没有多样性、库存、公平、广告或安全约束时成立；真实系统通常需要列表级重排。'},
3:{'deep':'多路召回的价值来自误差互补而不是“路数多”。应把每一路视为一个具有独立覆盖分布、成本和相关性的专家，并测 marginal recall，而不是只看该路自己的 hit rate。','case':'ItemCF 召回 1,000、双塔 1,500、热门 300，看起来共 2,800；去重后可能只有 1,900。若移除热门路后整体 Recall@K 几乎不变，它只是重复流量，应缩减配额。','boundary':'多路召回过多会加剧候选重复、融合偏置和维护成本；某些高度相关召回路的“新增量”接近零。'},
4:{'deep':'CTR 是局部、短期、受展示机制影响的代理目标；推荐真正优化的是用户长期效用与平台目标。只优化点击容易学到 clickbait、浅兴趣和位置偏差。','case':'一个标题党模型把 CTR 从 8.0% 拉到 8.5%，但有效播放率从 62% 降到 55%、次日留存下降 0.3%。如果只看 CTR 会得到错误上线决策。','boundary':'多目标也不是越多越好。加入弱标签会引入噪声和梯度冲突，必须明确 primary metric、guardrail 和长期指标。'},
5:{'deep':'系统设计题要从目标、流量、库存、反馈、延迟、训练更新频率六个约束反推架构，而不是从“我会哪些模型”出发。短视频还要特别处理观看时长、完播、负反馈和内容生态。','case':'新用户首屏没有历史序列，应提高内容语义、地域、热门和探索权重；老用户则可使用长序列、多兴趣召回和 target-aware 精排。相同模型并不适合全生命周期。','boundary':'直接把大模型放在全量精排通常不满足成本/QPS；更现实的做法是让大模型生成语义特征、蒸馏或只服务小候选集。'},
6:{'deep':'北极星指标应满足可解释、与长期价值相关、可被实验稳定测量、不会被单一策略轻易“作弊”。训练 label 通常只是北极星指标的代理。','case':'电商把 GMV 当唯一北极星可能诱导高客单价曝光并牺牲转化用户覆盖；更稳健的设计会同时看支付用户数、复购、退款与体验 guardrail。','boundary':'北极星指标不是“一个数字包打天下”。不同业务阶段可能需要分层目标，且必须防 Goodhart\'s Law。'},
7:{'deep':'用户分层的核心不是打标签，而是识别“数据可用性与决策机制不同”的人群，并允许策略、模型容量、探索率、特征窗口发生变化。','case':'对 0 行为新用户用 200 长度序列模型毫无意义；对高活跃用户只用人口属性也会丢掉大部分信号。可按行为长度、活跃度、生命周期做 gating。','boundary':'分层过细会造成样本稀疏、模型维护爆炸和实验功效下降，通常要证明分层带来的异质性收益。'},
8:{'deep':'搜索有显式 Query，推荐需要从历史与上下文推断 latent intent；但现代搜推逐渐统一为 user-query-item-context 四元建模。差异更多体现为意图强度、候选生成和评价口径。','case':'用户搜“无线耳机”时 relevance 是硬约束；首页推荐同样物品时可能更看兴趣、价格敏感度和新颖性。相同 item 在两种场景打分逻辑不同。','boundary':'不能简单说“搜索是主动、推荐是被动”就结束；推荐也有上下文意图，搜索也越来越个性化。'},
9:{'deep':'线上指标突降要按“数据→流量→候选→特征→模型→策略→实验”分层定位，并优先排查共享基础设施，因为模型 bug 往往不是最高先验。','case':'CTR 下降 20% 但曝光量和候选数正常，进一步发现实时 user feature freshness 从 2 分钟变成 2 小时；回滚特征流即可恢复，无需回滚模型。','boundary':'只看全局均值会掩盖问题。必须切 region/app_version/user cohort/traffic source/model version，避免平均值把局部事故冲淡。'},
10:{'deep':'项目价值要建立从“改了什么”到“为什么有效”再到“线上收益”的证据链，并能说明反事实：如果去掉某个组件，指标会怎样。','case':'“AUC +0.5%”不够。强回答会给样本规模、基线、增量实验、召回/排序分桶、P99、在线 lift、实验周期和置信区间。','boundary':'不要把团队整体收益全部归因于个人模型；面试官会通过 ablation、时间线和 ownership 追问识别夸大。'},
11:{'deep':'UserCF 与 ItemCF 都从共现图传播偏好，但稳定性来源不同：UserCF 依赖相似用户集合，ItemCF 依赖物品共现结构。工业上 ItemCF 更容易预计算和缓存。','case':'一个用户刚看了“相机 A”，ItemCF 可直接查相机 A 的邻接表；UserCF 需要找到相似用户并聚合其行为，在线计算与用户漂移更敏感。','boundary':'在用户群体小而物品极多、或社交关系非常强的场景，UserCF 仍可能更合适，不能机械说 ItemCF 永远更好。'},
12:{'deep':'ItemCF 改进的本质是修正“共现并不等于偏好相似”：活跃用户、热门物品、时间跨度、行为类型都会制造伪共现。','case':'一个用户一天点 1,000 个商品，他贡献的任意两物品共现可信度应低于只点 3 个高度相关商品的用户，可用 1/log(1+|I_u|) 降权。','boundary':'过强热门惩罚会伤害真实大众兴趣；时间衰减也不适合耐用品/长期主题，需要按业务半衰期设置。'},
13:{'deep':'矩阵分解通过低秩假设把稀疏交互矩阵映射到共享潜空间；可看作给每个用户和物品学习协同 embedding。关键不是“分解矩阵”本身，而是归纳偏置：相似交互模式共享统计强度。','case':'100 万用户×100 万物品矩阵几乎全空；若 latent dim=64，只需学习约 1.28 亿参数而非 10^12 个显式交互。','boundary':'纯 MF 很难利用文本、图像和冷启动特征，也无法自然表达复杂上下文；工业召回常把它扩展为双塔或图模型。'},
14:{'deep':'双塔适合召回的决定性因素是 item 表示可离线预计算，从而把在线问题变成一次 user encoder + ANN 检索；这把复杂交互模型转成可索引的向量空间。','case':'1 亿 item 若每次都经过 cross network 不可行；双塔把 1 亿 item embedding 预先建索引，在线只算一个 128 维 user 向量并检索 TopK。','boundary':'可索引性来自分离编码，也正是表达力损失来源；需要更复杂 cross 特征时通常放到后续排序。'},
15:{'deep':'双塔的核心瓶颈是 late interaction：user/item 在最终 dot product 前没有条件化交互。改进方向包括多兴趣、多向量、特征交叉蒸馏、hard negative 与更强 item/user encoder。','case':'用户同时喜欢篮球和摄影，单个 user vector 可能落在两兴趣之间，导致两边都不够近；多兴趣召回可以学习多个 query vector。','boundary':'增加 tower 深度不一定解决 late interaction；如果瓶颈是负样本或索引误差，加模型只会增加成本。'},
16:{'deep':'InfoNCE 可以视为候选集合上的分类问题，也可看成互信息/对比学习目标的工程化形式。真正决定边界的是 score、temperature、negative distribution 和 correction。','case':'batch=4096 时，每个正样本天然得到约 4095 个 in-batch negatives；若 8 卡 all-gather，负样本可扩大到约 32767，但通信、热门偏差和 false negative 同时上升。','boundary':'如果负样本并非从目标分布采样，未做 logQ/importance correction 时，训练出的 score 不应直接解释成真实概率。'},
17:{'deep':'In-batch negative 的本质是复用 batch 内 item，计算效率来自一次矩阵乘法 U V^T 同时得到 B×B logits；它把负采样开销从显式读取转为密集 GEMM。','case':'B=2048、d=128 时，可用一次 2048×128 与 128×2048 乘法构造约 419 万对 pair，比逐负例调用 encoder 高效得多。','boundary':'batch 不是 iid 时会污染负例：同一 session、同类目、同作者内容大量共批时 false negative 会升高。'},
18:{'deep':'严重问题主要有 false negative、popularity bias、跨卡重复和 batch distribution bias。因为“别人的正样本”并不自动等于“我的真负样本”。','case':'两个用户都点击同一爆款手机，去重后同 item 可能既作为正例又出现在负列；若不 mask，loss 会给出相互矛盾梯度。','boundary':'一味过滤相似 item 也会把真正困难的负例全部去掉，模型失去细粒度判别能力；应区分 false negative 与 hard negative。'},
19:{'deep':'负样本难度决定梯度信息量。Random negative 保证分布覆盖，hard negative 提供决策边界，semi-hard 在信息量和误标风险之间折中。','case':'“跑鞋”正例的随机负例可能是“冰箱”，梯度很快饱和；同品牌休闲鞋是 hard negative，更能训练细粒度兴趣。','boundary':'用当前模型挖 hard negative 会形成 feedback loop；模型错误会被持续放大，常需混合随机负例和周期性刷新。'},
20:{'deep':'曝光未点击是“未观察到点击”，而不是严格负偏好。点击由相关性、是否被看到、位置、展示样式和当时意图共同决定。','case':'排在第 50 位的 item 未点击很可能根本没进入视野；把它与首位看过后明确跳过的 item 赋相同负权重，会引入 position/examination bias。','boundary':'不是说曝光未点击完全不能用，而是要配合 dwell/examine 信号、位置特征、downweight 或 propensity correction。'},
21:{'deep':'temperature 通过缩放 logit 控制 softmax 熵和梯度集中程度。更小 tau 让模型更关注最相似的负例，相当于提高决策边界“硬度”。','case':'若正例 logit=0.8、hard negative=0.7，tau=1 时差距温和；tau=0.1 后变成 8 与 7，概率差和梯度显著放大。','boundary':'tau 太小会放大噪声与 false negative；最佳值依赖 batch size、score norm 和负例难度，不能照搬论文。'},
22:{'deep':'热门 item 在训练中天然出现频率高；若又被反复当负例，会产生与曝光分布相关的系统性反向梯度。需要区分“被采到多”与“用户真的不喜欢”。','case':'某爆款占训练 item 频率 5%，在大 batch 中几乎每步都作为大量用户的负例，模型可能过度压低其向量相似度。','boundary':'完全按均匀分布采样也不理想，会产生大量极易负例。常用 frequency smoothing、logQ correction 或分桶混合。'},
23:{'deep':'embedding 维度是容量、统计效率、内存带宽和 ANN 成本的联合超参。高 cardinality 不等于必须高维，频次低的 ID 很难估计大维向量。','case':'1 亿 item 从 64 维 FP16 增到 256 维，纯向量存储从约 12.8GB 增到 51.2GB，索引内存和检索带宽也同步上升。','boundary':'维度过小会欠拟合，过大则长尾 ID 过拟合；可考虑 mixed-dimension embedding 按频率分配容量。'},
24:{'deep':'embedding 质量必须用任务闭环验证：exact retrieval quality、ANN index recall、下游 ranking gain 和在线 lift 四层都要看。可视化只能做诊断。','case':'离线 exact Recall@100=90%，但 ANN Recall=80%，则系统端实际只有约 72% 的理想召回上限；继续调 encoder 不如先修索引。','boundary':'t-SNE 聚类“看起来很好”并不代表检索目标好；它会扭曲全局距离，也与在线 TopK 不等价。'},
25:{'deep':'ANN 用近似搜索把线性扫描换成图遍历、倒排分桶或向量量化。选型取决于 recall-latency-memory-update 四维，不存在单一最优算法。','case':'HNSW 通常高 recall、低延迟但内存大；IVF 通过 nprobe 调 recall/latency；PQ 进一步压缩向量，适合内存受限超大库。','boundary':'索引参数离线最优不代表线上最优；还要考虑增量更新、删除、冷热数据、NUMA/缓存和索引重建时间。'},
26:{'deep':'特征交叉是在表达“条件效应”：同一个 item 对不同用户/上下文价值不同。若模型只能学习加法项，就无法表达 user×item×context 的非线性组合。','case':'“夜间”本身不一定提高点击，“烧烤”也不一定；但“夜间×本地用户×烧烤”可能是强信号。','boundary':'显式交叉过多会导致稀疏爆炸；纯 MLP 虽能近似但样本效率可能差，需要在 inductive bias 和泛化之间折中。'},
27:{'deep':'FM 用 latent vector 分解二阶交叉参数，使未共同出现过的特征对也能通过共享维度泛化；这是它比显式 one-hot cross 更适合稀疏推荐的原因。','case':'若“用户城市=上海”和“品类=咖啡”从未同时出现，FM 仍可通过二者各自与其他特征学到的 embedding 内积估计交互。','boundary':'FM 主要表达二阶线性交互，复杂高阶模式需要 DeepFM、DCN 或其他网络补充。'},
28:{'deep':'Wide & Deep 把 memorization 与 generalization 分开建模：wide 记住稳定规则与人工交叉，deep 通过 embedding/MLP 泛化到未见组合。','case':'“用户曾买过该 app”这类强规则可放 wide；相似 app、相似用户的泛化由 deep 学习。','boundary':'wide 部分依赖人工 feature crosses，维护成本高；若业务变化快，DeepFM/DCN 等自动交叉可能更省工程。'},
29:{'deep':'DeepFM 的关键不是“FM+MLP”字面组合，而是 FM 与 deep 共享 embedding，避免 Wide&Deep 中 wide cross 的大量人工设计。','case':'同一个 sparse field embedding 同时用于 FM 二阶内积和 deep 网络输入，训练信号共同更新表示。','boundary':'共享参数减少工程复杂度但也耦合了低阶/高阶目标；极端场景下独立 embedding 可能更灵活。'},
30:{'deep':'FM 的二阶项通过平方和恒等式把 pairwise O(n²d) 化成 O(nd)。面试应能从 Σ_{i<j}<v_i,v_j>x_ix_j 推到 1/2[(Σ v_ix_i)²-Σ(v_ix_i)²]。','case':'100 个非零特征、d=16 时，显式 pair 有 4,950 对；重写后只需对 100×16 的向量做两次聚合。','boundary':'复杂度优化建立在二阶双线性交互结构上，不能直接推广到任意高阶交叉。'},
31:{'deep':'DCN 通过显式 cross layer 逐层构造有界阶数多项式交叉，让网络以更强归纳偏置学习 feature interaction，而纯 MLP 需要隐式逼近。','case':'两层 CrossNet 可产生包含原始特征与高阶组合的表示，同时参数规模远小于枚举所有交叉。','boundary':'原始 DCN 的 cross 参数表达能力有限，web-scale 场景可能欠拟合，这正是 DCNv2 的动机。'},
32:{'deep':'DCNv2 用矩阵 W_l 提升 CrossNet 的交叉表达力，并用 low-rank 与 CrossNet-Mix 控制 O(d²) 成本。面试应同时讲“为什么更强”和“为什么还能上线”。','case':'若 d=1024，完整 W 每层约 100 万参数；rank=64 的 UV 分解参数约 13 万，显著降低内存与计算。','boundary':'rank 太小会成为表达瓶颈；MoE expert 太多还会增加 routing、内存访问和小算子开销。'},
33:{'deep':'XGBoost/LightGBM 都是 GBDT，但工程路径不同。LightGBM 的 histogram、leaf-wise、GOSS/EFB 强调大规模效率；比较时应同时看精度、训练吞吐、内存与过拟合控制。','case':'高维稀疏推荐特征上，LightGBM histogram 能减少候选切分计算，但 leaf-wise 需要 max_depth/num_leaves 约束避免小样本叶过拟合。','boundary':'树模型并非“过时”：在小中规模数据、可解释特征和强非线性 tabular 问题上仍是重要 baseline。'},
34:{'deep':'Sparse ID 的数值大小没有序关系，核心是查表得到 embedding；dense 特征有真实数量意义，需处理尺度、偏态、缺失和截断。','case':'user_id=100 与 101 并不“更接近”，直接作为连续数值是错误；价格 100 与 101 则有自然距离。','boundary':'类别特征也可有序（会员等级），连续特征也可能更适合分桶；应按语义而不是数据类型名字处理。'},
35:{'deep':'标准化保留连续结构、利于优化；分桶引入 piecewise nonlinearity、对异常值更稳健。工业上经常“原值+log/归一化+bucket embedding”并用。','case':'价格呈长尾时可用 log(1+price) 作为 dense，同时做 price_bucket embedding，让模型既看顺序又学区间效应。','boundary':'分桶过细会稀疏，过粗丢信息；bucket 边界应按分位数/业务阈值而非随意等宽。'},
36:{'deep':'数据预处理 normalization 与模型内部 LayerNorm/BatchNorm 是两个层次。dense 输入通常先做稳定缩放；embedding 是可学习表示，不应机械做 z-score。','case':'年龄可先 clip/normalize 后拼接；拼接后的 512 维 hidden 可再 LayerNorm，这两步解决的问题不同。','boundary':'在线统计均值方差必须与训练一致；若用实时漂移统计，会制造 train-serving skew。'},
37:{'deep':'特征选择不是只看 importance 排名，而是判断“增量信息/成本”。要联合 feature ablation、permutation、SHAP/树 gain 与线上读取成本。','case':'一个特征离线 AUC 增 0.02%，却需要跨地域 RPC 增加 P99 8ms，可能不值得上线；应计算 quality-per-cost。','boundary':'高度相关特征会让单特征 importance 不稳定；移除一个后另一个会吸收贡献，因此需要 grouped ablation。'},
38:{'deep':'离线 AUC 到线上业务之间隔着候选分布、校准、位置、策略覆盖、延迟、特征新鲜度与实验流量。AUC 是必要证据但不是充分条件。','case':'新模型 AUC+0.3%，但 P99 增 20ms 导致超时回退率从 0.5% 到 4%，最终线上 CTR 可能下降。','boundary':'不要用“线上不一致”作为万能解释，应先做 score distribution、slice、latency、candidate overlap 和 calibration 的可证伪诊断。'},
39:{'deep':'DIN 的核心动机是一个固定 user vector 无法同时表达多兴趣；它让历史行为对当前 target 做条件化激活，得到 target-aware interest。','case':'同一用户历史含“篮球鞋、相机、咖啡”。候选是镜头时应高权重激活相机行为，而不是平均池化所有历史。','boundary':'DIN 仍缺少显式兴趣演化与长序列效率，target-aware 不等于完整 sequence modeling。'},
40:{'deep':'DIN local activation unit 通常联合 behavior embedding、target embedding、差值和逐元素乘积，经 MLP 产生权重，再对历史加权求和。它与标准 scaled dot-product attention 不同。','case':'对 50 条历史行为，每条构造 [e_i,e_t,e_i-e_t,e_i⊙e_t]，MLP 输出 50 个 activation score，再聚合成用户兴趣向量。','boundary':'不应机械把 DIN 权重称为 softmax probability；原设计强调 activation intensity，不一定归一化。'},
41:{'deep':'DIN 是 target→history 的条件化匹配，Self-Attention 是 history↔history 的上下文建模。前者回答“哪些历史与候选相关”，后者回答“历史之间如何相互影响”。','case':'候选相机触发相机相关行为是 DIN；“买相机后又看镜头”这种行为依赖更像 self-attention/sequence encoder。','boundary':'二者不是互斥，可以先 self-attention 编码历史，再做 target-aware attention。'},
42:{'deep':'DIN 的主要边界：没有显式时间状态转移、长历史对每个候选都计算 attention 成本高、噪声行为会直接参与 target matching。','case':'精排 500 个候选×5000 条历史意味着 250 万级 pair interaction，在线成本很难接受，需要先筛历史或缓存表示。','boundary':'若序列很短且候选少，DIN 的简单性反而可能比复杂长序列模型更优。'},
43:{'deep':'DIEN 把“行为”与“兴趣状态”区分开：GRU 提取随时间变化的 latent interest，再用 target-aware 机制建模与候选相关的兴趣演化。','case':'连续浏览婴儿用品可能表示兴趣逐步增强；DIEN 不只看每个点击与 target 的相似度，还建模状态如何随行为演进。','boundary':'RNN 的顺序计算限制并行性；超长序列和大规模 serving 下会转向 SIM/Transformer/HSTU 等。'},
44:{'deep':'Auxiliary loss 给每个中间兴趣状态局部监督，要求 h_t 能区分真实下一行为与负样本，缓解“只靠最终 CTR label 监督太远”的问题。','case':'序列长度 100 时，若只在最终点击产生 loss，前几十步的状态学习信号间接；aux loss 在每个 t 提供 next-action supervision。','boundary':'aux loss 权重过大可能让模型偏向 next-item prediction 而不是最终 CTR，需验证主任务收益。'},
45:{'deep':'AGRU 用 attention 直接替代 update gate，AUGRU 则用 attention 缩放原 update gate，因此后者保留 GRU 自身的状态更新判断并叠加 target relevance。','case':'若某一步 GRU 本身认为应少更新、attention 又低，AUGRU 的更新会更小；AGRU 则主要由 attention 决定。','boundary':'attention score 的校准与范围会直接影响状态更新稳定性，不能只背公式。'},
46:{'deep':'序列预处理是在建模前决定“什么算一次有效兴趣证据”。重复刷新、误触、机器人、极短 dwell 和系统重试都会污染兴趣强度。','case':'同一视频因网络重连产生 5 次曝光/播放事件，若不 sessionize/dedup，会把一个弱信号放大成 5 次强兴趣。','boundary':'过度去重会抹掉“重复观看本身就是强兴趣”的真实信号，应按事件语义和时间窗定义。'},
47:{'deep':'标准 self-attention 的核心瓶颈是 L² attention matrix，再叠加每候选 target interaction 与在线 batch 小的现实，长序列成本迅速失控。','case':'L=10,000 时单头 attention 有 1 亿 pair；即便矩阵计算可加速，显存、KV/activation 和在线延迟仍很大。','boundary':'FlashAttention 降低 IO/内存但不改变 pair 数量的二次复杂度；它不能自动解决超长推荐序列。'},
48:{'deep':'SIM 采用“先搜索再精建模”：GSU 从 lifelong history 中取 target-related 子序列，ESU 再做高表达建模，把计算集中在最相关历史。','case':'历史 50,000 条，GSU 先筛到 100~200 条，再用 ESU attention；相比对全部历史逐候选做深交互，成本下降两个数量级。','boundary':'GSU 如果召回差，会形成不可恢复的信息截断；因此必须单独评估 long-history search recall。'},
49:{'deep':'Transformer 适合序列的主要优势是并行训练、长距离依赖和多头子空间，但推荐需要额外处理时间间隔、行为类型、高基数 ID 和线上成本。','case':'“购买相机→数周后看镜头”跨度很长，RNN 容易遗忘，self-attention 可直接建立远距离联系并加入 time embedding。','boundary':'短序列/低算力场景 Transformer 未必优于 GRU；模型选择要基于质量-成本曲线。'},
50:{'deep':'LayerNorm 对单样本 hidden dimension 归一化，不依赖 batch 统计；推荐线上 batch 小且序列长度/组成变化大，因此通常更稳定。','case':'在线单请求或 micro-batch=1 时 BatchNorm 的训练统计无法实时复现，而 LayerNorm 行为与 batch size 基本无关。','boundary':'这不是“推荐永远不用 BN”。MLP dense tower 仍可能使用 BN；要按张量维度和 serving 方式判断。'},
51:{'deep':'多任务的价值来自共享统计强度与统一表示，但前提是任务之间存在可利用关系。推荐天然有点击、时长、互动、转化等多个反馈。','case':'点赞样本少但与点击共享部分兴趣表征，联合训练可借助大规模点击数据改善稀疏任务。','boundary':'任务相关性弱或冲突时共享会负迁移；MTL 不是免费午餐。'},
52:{'deep':'Shared Bottom 强制所有任务使用同一 representation，无法选择“哪些知识共享、哪些隔离”。当梯度方向冲突时，一个任务的优化会破坏另一个任务。','case':'点击偏好短刺激内容、长期留存偏好高质量内容，两任务梯度可能在共享层方向相反。','boundary':'任务高度相关、数据规模小或模型简单时 Shared Bottom 仍是很强 baseline，不能一上来就堆 MMoE。'},
53:{'deep':'MMoE 用共享 experts + task-specific gates，把共享从“共享一个底座”改成“每个任务学习不同的共享组合”。这提升了对任务相关性差异的适应能力。','case':'CTR gate 可能偏好 expert1/2，watch-time gate 偏好 expert2/3；expert2 学公共兴趣，其他 expert 学任务特异模式。','boundary':'expert 数过多可能出现 expert collapse 或 gate 负载不均；需要观察 gate entropy/usage。'},
54:{'deep':'普通 MoE 的路由目标通常服务一个任务/主损失；MMoE 的关键是每个 task 有独立 gate，显式允许不同任务使用不同 expert mixture。','case':'同一个输入 x 经过相同专家 E_k，但 CTR 与 CVR 的 g_t(x) 不同，因此得到不同 task representation。','boundary':'MMoE expert 仍共享，任务特异隔离不充分时会继续负迁移，这引出 PLE。'},
55:{'deep':'“跷跷板”说明 Pareto frontier：一个任务提升伴随另一个任务下降。根因可能是共享容量、标签冲突、loss scale 或业务目标本身竞争。','case':'短视频 CTR+1% 但有效时长-0.5%，不一定是模型 bug，也可能是点击诱导与深度消费目标天然冲突。','boundary':'不能只用调 loss 权重掩盖问题；应定位 gradient conflict、样本空间和任务定义。'},
56:{'deep':'PLE 在每层区分 shared experts 与 task-specific experts，并渐进提取共享/私有信息，目标是减少无关共享和 seesaw。','case':'CTR 私有 expert 学点击特性，CVR 私有 expert 学购买信号，共享 expert 学通用用户-商品匹配；gate 决定每层组合。','boundary':'PLE 结构更复杂、成本更高；若任务高度相关，额外隔离未必带来收益。'},
57:{'deep':'Loss weighting 同时改变梯度尺度与业务偏好。固定权重简单可控；动态方法根据不确定性、梯度范数或学习速度自动调整，但也可能不稳定。','case':'若 CTR loss≈0.5、时长 MSE≈100，直接相加会让时长梯度主导；先做尺度归一或使用任务权重才有意义。','boundary':'自动权重算法优化的是训练平衡，不一定等于业务价值；最终仍需线上多指标决策。'},
58:{'deep':'任务收敛速度不同说明共享参数仍被未收敛任务持续推动。可用动态权重、task-specific LR、freeze/stop-gradient 或梯度投影降低已收敛任务回退。','case':'CTR 已稳定而 CVR 仍上升，可降低 CTR loss weight 并监控其验证集退化；完全 freeze 共享层则可能阻碍 CVR。','boundary':'“一个任务收敛”可能只是 plateau，不应凭训练 loss 判断；需要 validation 与业务 slice。'},
59:{'deep':'CVR label 只在点击后可观察，训练样本空间是 clicked impressions，线上推断却面向 all impressions，造成 sample selection bias；同时转化远比点击稀疏。','case':'点击率 5%、点击后转化 2%，全曝光转化率只有 0.1%；仅在 5% 点击样本训练会严重缩小数据空间。','boundary':'若业务推断本身只发生在点击后场景，selection bias 的定义和严重程度会不同。'},
60:{'deep':'ESMM 利用 pCTCVR=pCTR×pCVR，把 CTR 与 CTCVR 在全曝光空间联合训练，通过共享表示间接学习 CVR，避免只在点击子空间监督。','case':'100 万曝光中 5 万点击、1,000 转化；ESMM 可利用全部 100 万曝光训练 CTR/CTCVR，而不是只用 5 万点击拟合 CVR。','boundary':'通过除法隐式得到 pCVR 会有估计误差传播和独立/因果假设问题，后续模型继续修正。'},
61:{'deep':'ESMM 解决了样本空间和稀疏的核心痛点，但 pCVR 是通过乘积约束间接学习，存在估计偏差、概率放大和因果混杂问题；ESCM² 等引入 counterfactual/causal 思路。','case':'当 pCTR 很小时，pCVR≈pCTCVR/pCTR 对微小误差非常敏感，数值上会放大。','boundary':'“后续模型更复杂”不代表必然更好；需要看标签可用性、稳定性和线上增益。'},
62:{'deep':'观看时长是重尾、截断、受内容长度影响的连续目标。直接 MSE 会让少数超长样本主导梯度，且不同视频长度不可比。','case':'30 秒视频看 25 秒与 30 分钟视频看 25 秒意义完全不同；可同时建模 watch_time、completion ratio、有效播放等。','boundary':'只用比例也会伤超短内容；通常需要多目标或分桶/分布式建模。'},
63:{'deep':'BCE 是 Bernoulli likelihood 的负对数似然，适合二元事件概率建模；其梯度与 sigmoid 组合后简洁稳定。','case':'logit z 经 sigmoid 得 p，单样本对 z 的梯度为 p-y，因此预测越错梯度越大且方向明确。','boundary':'BCE 优化概率拟合，不直接优化 NDCG/GMV；类别采样后还要考虑概率校准。'},
64:{'deep':'Pointwise 学单样本标签，Pairwise 学相对偏序，Listwise 直接考虑列表。选择取决于标签形态、采样成本和线上排序目标。','case':'隐式反馈只有正负偏好时 BPR pairwise 很自然；多级 relevance 且关心 TopK 顺序时 listwise/NDCG surrogate 更契合。','boundary':'pair/listwise 并不自动优于 pointwise；大规模系统中 pointwise 的稳定性和校准价值很重要。'},
65:{'deep':'AUC 等价于随机正负 pair 中正样本 score 更高的概率，因此只关心排序不关心绝对校准。','case':'AUC=0.8 可解释为随机抽一个正例和一个负例，模型约 80% 概率把正例排更高。','boundary':'AUC 对 TopK 位置不敏感，也混合不同用户 pair；不能替代 NDCG/GAUC/业务指标。'},
66:{'deep':'AUC 的 TPR/FPR 分别在正负类内部归一，因此类先验变化对其影响小于 Accuracy；但极端不平衡下 PR-AUC 常更能反映正例检出质量。','case':'正例 0.1% 时全预测负类 accuracy=99.9% 却毫无价值；AUC 不会因此自动变高。','boundary':'“稳定”不等于“最合适”。若只关心高精度 TopK，AUC 仍可能误导。'},
67:{'deep':'全局 AUC 会比较跨用户 score，而推荐通常只需同用户内排序。若用户基线点击倾向不同，global AUC 会被用户间 calibration 差异影响。','case':'用户 A 所有 item score 0.9、用户 B 所有 item 0.1，只要 A 正例多，跨用户 pair 可抬高 AUC，即使各自内部排序很差。','boundary':'GAUC 也有用户过滤与权重选择问题，不能认为它完全解决评价偏差。'},
68:{'deep':'GAUC 先算每用户 AUC 再加权。权重决定“谁的话语权”：按曝光权重更接近流量贡献，按用户等权更强调用户公平。','case':'重度用户 10,000 曝光、轻度用户 10 曝光；曝光加权会几乎由重度用户决定，等权则两者同权。','boundary':'只有单一标签类别的用户无法定义 AUC，必须明确过滤策略，避免指标口径漂移。'},
69:{'deep':'Precision@K 衡量推荐出的 K 个里有多少相关，Recall@K 衡量所有相关 item 中找回多少。召回阶段更关注 coverage/Recall，最终展示更看 precision/utility。','case':'用户有 20 个相关 item，Top10 命中 5 个：P@10=0.5，R@10=0.25。','boundary':'隐式反馈中“未点击”并非真无关，离线 P/R 会受曝光日志偏差影响。'},
70:{'deep':'NDCG 同时考虑 relevance gain 与位置折扣，并用 ideal DCG 归一化，适合多级相关性和 TopK 排序。','case':'同样命中 3 个高相关 item，排在 1/2/3 位比 8/9/10 位有更高 DCG；这符合展示位价值。','boundary':'折扣形式和 relevance 标注都是人为设计，NDCG 仍只是线上效用代理。'},
71:{'deep':'Time Split 模拟真实因果时间方向，防止未来交互、未来特征统计和 item 生命周期泄漏进训练。','case':'随机切分可能把用户 9 月购买后的行为放训练，再预测 8 月点击，构成明显未来信息泄漏。','boundary':'严格 time split 会带来 cold item/user，恰好也是线上真实难点，不应为提高离线分数而回避。'},
72:{'deep':'实验分桶需要稳定、均匀、可复现，并与干预单位一致。hash 只是实现细节，更关键是 identity、实验层、互斥/正交和跨端污染。','case':'1000 buckets 中给实验 100 个 treatment、100 个 control；先检查实际流量比例是否接近 1:1，再看指标。SRM 往往比显著性更先发现管线问题。','boundary':'request-level 随机分组会让同一用户跨组体验，违反 SUTVA/稳定处理假设并产生串扰。'},
73:{'deep':'A/A 用相同策略验证随机化、埋点、方差估计和假阳性率。它不是为了证明两组“完全相等”，而是验证实验平台在无 treatment 时行为符合统计预期。','case':'若 A/A 连续多次出现显著差异或 SRM，先修分桶/埋点，不能进入模型 A/B。','boundary':'一次 A/A 不显著不代表平台永久正确；关键链路变更后应重新做健康检查。'},
74:{'deep':'这是典型多指标冲突。要先确认 CTR 提升来自何种内容/人群，再判断停留下降是否触碰 primary/guardrail，而不是简单平均两个指标。','case':'slice 后发现涨幅集中在标题党类目，点击后 3 秒退出率升高，说明模型优化了浅点击而非有效消费。','boundary':'停留下降也可能来自推荐更高效、用户更快完成任务；必须结合业务语义解释。'},
75:{'deep':'0.1% 是否有效取决于基线、样本量、方差、置信区间、MDE、实验成本和长期价值。统计显著与业务显著是两件事。','case':'日活亿级产品的 0.1% 使用时长提升可能巨大；小流量产品同样 uplift 可能落在噪声内。','boundary':'不要只报 p<0.05；要给 effect size 与 CI，并检查多重检验和 novelty effect。'},
76:{'deep':'推荐日志是策略选择后的观测数据，不是自然 iid 数据。Exposure、position、popularity、selection、survivorship 等 bias 会同时存在并互相作用。','case':'模型只学习历史曝光 item，热门 item 因为被更多曝光又得到更多正样本，形成 popularity feedback loop。','boundary':'“加一个 position feature”只能缓解部分相关性，不等价于因果去偏。'},
77:{'deep':'Position Bias 可分解为是否被 examined 与 item relevance；解决方法从随机干预估计 propensity，到 click model/IPS 再到将 position 作为特征。','case':'随机交换少量位置可估计不同 position 的 examine propensity，再用逆倾向加权减少位置对 label 的污染。','boundary':'直接大规模随机排序会伤体验；通常只在安全流量做受控探索。'},
78:{'deep':'IPS 用 1/propensity 重加权恢复目标分布下的无偏估计，但小 propensity 会带来高方差。工程上常 clipping、SNIPS 或 doubly robust。','case':'某样本曝光概率 0.01，则权重 100；单个样本就可能主导 batch 梯度，因此常把权重截到 10/20 等上限并分析 bias-variance。','boundary':'propensity 估计错时 IPS 也会错；必须监控权重分布和 effective sample size。'},
79:{'deep':'类不平衡既是优化问题也是概率校准问题。下采样负例、class weight、focal loss 改变梯度，但也改变训练先验。','case':'真实 CTR=1%，若训练中把正负采成 1:1，模型输出不能直接当线上点击概率，需要 prior correction/calibration。','boundary':'AUC 可能不受 prior 直接影响，但线上阈值、expected value 和多目标融合会受 calibration 影响。'},
80:{'deep':'负采样 policy 定义了模型看到的对比任务，随机采样过易会训练“类别区分”而非“决策边界”。采样策略实际上是模型的一部分。','case':'推荐运动鞋时若负例几乎都是家电，模型很快学会大类目；真正线上竞争却发生在相似鞋款之间。','boundary':'只挖 hardest negative 会噪声高、覆盖差；应混合分布并记录 sampling version。'},
81:{'deep':'Train-Serving Skew 是同名 feature 在训练与线上生成逻辑、时间点、默认值或版本不同。它会让离线验证失真，是工业推荐常见事故源。','case':'训练用“当天最终点击数”，线上只能用“截至当前点击数”；模型事实上偷看未来统计。','boundary':'同一个 Feature Store 也不自动保证一致，仍要检查 point-in-time correctness 和回填逻辑。'},
82:{'deep':'离线训练追求稳定吞吐和全局重训，在线/增量训练追求 freshness。两者主要权衡 label delay、噪声、灾难性遗忘、状态一致性和回滚能力。','case':'新闻推荐兴趣半衰期小时级，日更模型可能太慢；但直接每分钟更新又可能被突发噪声带偏，可采用近实时样本+稳定基座。','boundary':'“在线”不等于每条样本立即 SGD；micro-batch、hourly incremental 都属于连续更新设计。'},
83:{'deep':'漂移分 covariate shift P(X)、label/target shift P(Y) 与 concept drift P(Y|X)。先检测哪种变了，再决定重训、重加权或特征修复。','case':'节假日导致品类流量分布变是 P(X) 变化；相同用户-品类关系改变才更接近 concept drift。','boundary':'频繁重训可能追噪声；需要 drift threshold、回看窗口和 challenger 验证。'},
84:{'deep':'延迟优化要先 profile critical path：feature fetch、embedding lookup、network、kernel、queue 和模型 compute。盲目量化模型可能优化错瓶颈。','case':'若 P99 中 60% 时间在远程特征 RPC，模型从 FP32 改 FP16 只能省很小比例；先做 cache/feature locality 更有效。','boundary':'平均 latency 没意义，推荐 SLA 通常看 P95/P99 与超时回退率。'},
85:{'deep':'Embedding 表是典型 memory-bound 组件。优化方向包括 mixed dimension、quantization、hash、频率分层、pruning、缓存和分布式 parameter server。','case':'10^9 ID×128×FP32 约 512GB；改 FP16 是 256GB，再配长尾 32/64 维可继续下降。','boundary':'压缩会影响 rare ID 与 ANN 精度；必须按频率 slice 评估，而不是只看整体 AUC。'},
86:{'deep':'User Cold Start 的根因是没有协同历史，需要用显式 onboarding、上下文、地域、设备、热门与探索快速收集偏好。目标不仅是首屏质量，也是信息增益。','case':'首次打开让用户选择 3 个主题可显著减少探索空间，但选择成本过高会影响激活，需要平衡问卷与被动探索。','boundary':'人口属性容易刻板化且隐私敏感，应优先使用行为上下文和可撤销偏好。'},
87:{'deep':'Item Cold Start 有内容但缺交互，因此应从文本/图像/类目/作者生成内容表示，并给可控探索流量获取早期反馈。','case':'新视频先通过多模态 encoder 映射到已有内容空间，进入语义召回，再给小流量探索；收集行为后逐步切到协同表示。','boundary':'强行保量低质新内容会伤体验，必须有内容质量/安全 gate。'},
88:{'deep':'User cold start 缺的是 preference evidence，Item cold start 缺的是 interaction evidence。二者可用信息来源、探索对象和成功指标区分。','case':'新用户要探索“这个人喜欢什么”；新 item 要探索“哪些人喜欢它”。因此一个在用户侧做兴趣发现，一个在 item 侧做受众发现。','boundary':'双冷启动（新用户遇到新 item）最难，通常只能依赖内容与上下文。'},
89:{'deep':'热门吞噬长尾是曝光反馈回路：曝光→交互→训练样本→高分→更多曝光。要从 sampling、score calibration、quota 和 exploration 多层治理。','case':'若热门 top1% 获得 50% 曝光，即便长尾质量相同也很难积累样本；可设置 exposure regularization 或分层探索。','boundary':'长尾不是天然优质，目标应是机会与效用平衡，而不是机械均匀曝光。'},
90:{'deep':'多样性可以从 item、类目、作者、语义、时间与供应侧覆盖度量。单一 ILS 只能反映相似度，不能代表用户感知多样性。','case':'10 条推荐来自 10 个作者但都属于同一话题，作者 diversity 高、语义 diversity 仍低，因此需多维指标。','boundary':'多样性过高会牺牲主题连贯和准确性；“随机”不是多样性优化。'},
91:{'deep':'准确率-多样性是列表级多目标优化。MMR 用 relevance 与与已选集合的相似度惩罚做 greedy trade-off；DPP/约束优化可进一步建模集合效用。','case':'λ=1 时完全 relevance；降低 λ 会逐步引入不同类目/作者。应画 Pareto curve 而不是只选一个 λ。','boundary':'离线 diversity 提升不代表用户满意度提升，需要线上 watch/skip/retention 验证。'},
92:{'deep':'信息茧房来自 exploitation feedback loop，需要通过 exploration、diversity、新主题注入与长期目标打破。核心是控制“已知兴趣”的垄断程度。','case':'对高置信兴趣 90% exploitation，留 10% 给相邻主题/新内容探索，并用长期接受率更新探索策略。','boundary':'探索不是强行推无关内容；应限制风险、相关性下界和负反馈成本。'},
93:{'deep':'新内容保量解决“无曝光→无数据→低分→继续无曝光”的鸡生蛋问题。合理保量是受控实验流量，不是无条件补贴。','case':'可给新 item 一个随时间衰减的 exploration bonus，达到最小曝光后按后验质量逐步释放/淘汰。','boundary':'必须设置质量、举报、安全与作者作弊防线，避免利用新内容池刷流量。'},
94:{'deep':'HSTU 的意义不在“把 Transformer 改快一点”，而是为推荐的高基数异构行为序列重新设计 transducer，并证明质量能随 data/model/compute scaling。','case':'ICML 2024 工作报告 HSTU 在长度 8192 序列上相对 FlashAttention2 Transformer 有显著速度优势，并展示大规模线上部署；面试应把论文结果与自己的业务约束分开陈述。','boundary':'论文中的 scaling 结论依赖数据规模、硬件栈、训练 recipe 和目标定义，不能直接外推到所有公司/小数据场景。'},
95:{'deep':'Generative Recommendation 将推荐从“对给定 item 打分”改为“条件于历史生成下一 item/离散标识”，因此候选生成、序列建模和 item vocabulary 设计变成一个统一问题。','case':'传统 pipeline 先 ANN 取候选再 rank；生成式模型可以 autoregressive 生成 semantic ID，再映射到 item，但需要合法性约束和去重。','boundary':'生成不会自动消除检索成本：超大 item space 仍需 tokenization、constrained decoding 或后验检索。'},
96:{'deep':'双塔把 item 映射到连续向量并用 ANN 搜索；生成式召回学习 item token/semantic ID 的条件概率。前者成熟高吞吐，后者表达序列依赖更强但 decoding/合法性更复杂。','case':'双塔一次 query 可取 TopK；生成式可能需要 beam search 多步生成 code，成本随 code length×beam 增长。','boundary':'二者可混合：生成式产 semantic intent/候选簇，ANN 再做高效实体检索。'},
97:{'deep':'Semantic ID/RQ-VAE 把巨大 item vocabulary 分解为多个离散 code，使生成模型复用语义结构并降低单层 softmax 规模。关键是 code 的碰撞、层次和可解码性。','case':'10^9 item 不适合一个 10 亿类 softmax；若用 4 级 codebook、每级 1024 code，组合空间可覆盖巨大 item 集合。','boundary':'量化误差与 code collision 会损害唯一标识；需要 residual code、collision handling 或额外 ID token。'},
98:{'deep':'RankMixer 的核心问题是传统 ranking 模型由大量 CPU 时代手工交叉模块构成，GPU MFU 低、扩展参数规模时收益/成本差。它用硬件友好的 token mixing 统一交互。','case':'论文报告 MFU 从约 4.5% 提到 45%，参数规模可扩约 100×且保持相近推理延迟；这说明“架构可 scaling”与“单模型 AUC 高”是不同能力。','boundary':'论文生产环境的数据/硬件非常特殊，不能把 1B 参数作为普遍目标；中小业务可能首先受数据而非算力限制。'},
99:{'deep':'LLM 进入推荐至少有语义理解、内容编码、用户历史总结、rerank、对话式推荐和生成式推荐六条路径。最有价值的问题是“放在哪一层 ROI 最高”。','case':'全流量精排用 7B LLM 可能不可行，但离线生成 item/user semantic features，再蒸馏进小模型，能以较低成本获得语义泛化。','boundary':'LLM 容易产生 hallucination、延迟和成本问题；涉及 item ID 时必须 constrained grounding，不能生成不存在商品。'},
100:{'deep':'下一代系统更可能是混合架构：成熟召回保证吞吐与覆盖，sequence/generative model 提供更强用户状态，scalable ranker 做高质量交互，重排负责约束与长期效用。','case':'可设计：ItemCF/TwoTower/Semantic retrieval → GPU-friendly coarse/rank → HSTU 用户状态 → multi-task heads → listwise constrained rerank；生成式组件先 shadow/canary。','boundary':'“替换整个 pipeline”通常风险最大。迁移应以可回滚、可度量的模块增量为单位，并比较 quality×latency×cost 的 Pareto frontier。'},
}

CHAPTER_LENS = {
1: r'''### 系统设计的第一性原理

推荐系统首先是一个**受预算约束的决策系统**。面试时建议明确五个预算：候选规模、特征读取、模型计算、端到端延迟、实验/迭代速度。一个方案如果只在模型指标上成立，却无法在这些预算内运行，就不是工业答案。

可以把整条链抽象成：

$$\text{Logs}\rightarrow\text{Data/Features}\rightarrow\text{Candidate Generation}\rightarrow\text{Scoring}\rightarrow\text{List Optimization}\rightarrow\text{Exposure}\rightarrow\text{Feedback}$$

每个箭头都可能产生分布变化和信息损失。因此分析系统时，要同时回答：**输入分布是什么、这一层丢掉什么、下一层还能否补救、线上如何观测。**''',
2: r'''### 召回系统的第一性原理

召回不是“找相似向量”这么简单，而是在严格 latency/memory 预算下最大化**可排序的有效候选覆盖**。模型、负采样和 ANN 索引三者必须联合设计：

$$\text{Training Distribution}\rightarrow \text{Embedding Geometry}\rightarrow \text{Index Approximation}\rightarrow \text{Online Candidates}$$

任何一环偏移都会让离线 embedding 指标与线上候选质量脱节。面试时应至少区分 **model recall、exact retrieval recall、ANN recall、end-to-end recall**。''',
3: r'''### 精排建模的第一性原理

精排的输入通常是高维稀疏 ID、dense 统计、上下文和行为表示。核心难题是：用有限参数和延迟预算表达高价值 feature interactions，并保证概率/排序在训练与 serving 分布上一致。

一个强回答应同时覆盖：**feature semantics → interaction mechanism → optimization → calibration → latency**。只比较模型结构而不谈特征口径和 serving cost，通常停留在论文复述层。''',
4: r'''### 序列建模的第一性原理

用户历史不是“一个很长的 list”，而是带时间、行为类型、噪声、重复、兴趣切换和生命周期的事件流。序列模型要回答三件事：

1. 哪些事件是真实兴趣证据？
2. 如何把过去状态压缩为与当前候选相关的表示？
3. 当历史从几十条扩展到数万条时，计算如何保持可控？

因此 DIN/DIEN/SIM/Transformer/HSTU 可以理解为对这三个问题的不同取舍。''',
5: r'''### 多任务建模的第一性原理

多任务学习的本质是**受控共享**。共享能提高样本效率，但也会通过共享参数传递冲突梯度。分析任何 MTL 模型都可以沿三条线：任务标签空间是否一致、梯度是否冲突、模型如何分配共享/私有容量。

$$L(\theta)=\sum_t \lambda_t L_t(\theta_{shared},\theta_t)$$

真正难点通常不在写出这条式子，而在决定哪些参数该共享、$\lambda_t$ 如何对应业务价值，以及线上多个目标如何合成最终排序。''',
6: r'''### 评价与实验的第一性原理

必须分清三个层次：**训练 Loss、离线 Metric、线上业务目标**。它们是代理关系，不是同一个量。

$$\text{Loss}\Rightarrow \text{Model Behavior}\Rightarrow \text{Offline Metric}\Rightarrow \text{Online Causal Effect}$$

任何“离线涨点就应该上线”的论证都缺少最后一步因果验证。强回答应主动提到分桶、SRM、MDE、置信区间、guardrail 和异质性分析。''',
7: r'''### 数据与 Serving 的第一性原理

推荐训练数据来自历史策略选择后的曝光，而不是 iid 抽样。因此数据偏差、训练分布与线上分布、特征时间一致性、模型更新频率是一个整体问题。

工程上应建立**版本化与可观测性**：sample policy、feature schema、model version、index version、serving config 都应可追踪，才能把线上异常定位到具体环节。''',
8: r'''### 生态与探索的第一性原理

冷启动、长尾、多样性和信息茧房本质上都来自**反馈不足或反馈自增强**。如果系统永远 exploitation，就无法获得新用户/新内容的可靠估计，也会不断放大历史热门。

因此要把推荐看成 sequential decision：当前一次少量探索可能牺牲即时 CTR，但换来信息增益、供给生态与长期价值。''',
9: r'''### 2026 前沿模型的第一性原理

判断前沿推荐模型不要只看参数量或论文指标，而要看四件事：**scaling behavior、hardware efficiency、serving constraints、incremental deployability**。

推荐系统面对高 QPS、巨大 item space、频繁更新和严格成本。一个前沿模型只有在 quality–latency–cost 的 Pareto 曲线上占优，并能灰度/回滚，才真正具有工业价值。''',
}

DECISION_TABLES = {
1: '''| 决策维度 | 面试中要给出的证据 |
|---|---|
| 候选规模 | 每层 input/output 数量、截断率、oracle 上限 |
| 延迟 | P50/P95/P99、超时率、降级路径 |
| 数据 | 样本窗口、特征 freshness、标签延迟 |
| 质量 | Recall/GAUC/NDCG 与线上 primary metric |
| 稳定性 | 回滚、版本一致性、监控与事故隔离 |''',
2: '''| 决策维度 | 典型观测量 |
|---|---|
| 训练 | positive rate、negative source、batch size、temperature |
| 表示 | norm、collapse、类目/兴趣 slice、drift |
| 检索 | exact Recall@K、ANN Recall@K、QPS、P99 |
| 索引 | memory、build/update time、delete/refresh 能力 |
| 线上 | candidate overlap、dedup、route marginal recall |''',
3: '''| 决策维度 | 典型问题 |
|---|---|
| Feature | 是否 point-in-time correct？是否有高代价 RPC？ |
| Interaction | 显式/隐式交叉能否覆盖主要模式？ |
| Capacity | 参数增长是否真的带来可复现增益？ |
| Calibration | score 能否用于多目标融合/阈值？ |
| Serving | embedding lookup 与小矩阵算子谁是瓶颈？ |''',
4: '''| 决策维度 | 需要说明 |
|---|---|
| 序列定义 | event、session、去重、窗口、时间衰减 |
| 编码 | position/time/action/type embedding |
| 兴趣 | 单兴趣、多兴趣、target-aware、state evolution |
| 长序列 | 截断、search-first、sparse/linear attention |
| Serving | 序列缓存、增量状态、每候选交互成本 |''',
5: '''| 决策维度 | 需要监控 |
|---|---|
| Task relation | label overlap、gradient cosine、相关性 |
| Expert/Gate | expert usage、gate entropy、collapse |
| Loss | scale、动态权重、task-specific convergence |
| Calibration | 每任务 reliability / ECE |
| Online | primary + guardrail + Pareto trade-off |''',
6: '''| 层次 | 例子 | 典型误区 |
|---|---|---|
| Loss | BCE/BPR/Listwise | 以为 loss 与业务指标相同 |
| Offline | AUC/GAUC/NDCG | 忽略 logging policy 与 time leakage |
| Online | CTR/时长/GMV/留存 | 只看 p-value 不看 effect size |
| Experiment health | SRM/A/A/埋点 | 数据异常时仍解释 treatment effect |''',
7: '''| 风险 | 应对 |
|---|---|
| Bias | intervention / IPS / model correction |
| Skew | point-in-time feature + shared transform |
| Drift | slice monitor + retrain/reweight trigger |
| Latency | profile critical path + cache/quantize/distill |
| Memory | mixed dimension / quantization / sharding |''',
8: '''| 目标 | 即时指标 | 长期指标 |
|---|---|---|
| 冷启动 | 首屏 CTR/有效消费 | 次日留存、兴趣收敛速度 |
| 长尾 | coverage、有效曝光 | 供给留存、生态集中度 |
| 多样性 | ILS/category coverage | session satisfaction |
| 探索 | exploration regret | 信息增益、长期效用 |''',
9: '''| 维度 | 传统 Pipeline | 前沿/生成式组件 |
|---|---|---|
| 吞吐 | 成熟、高 | 需专门优化 |
| 表达 | 模块化、局部 | 序列/语义统一性更强 |
| 更新 | 索引/模型分开 | token/code/model 可能耦合 |
| 风险 | 可控、易回滚 | decoding/合法性/成本新问题 |
| 评估 | stage-wise | 需同时评估 scaling 与 ROI |''',
}

PSEUDO = {
1: '''```text
request
  -> load user/context features
  -> parallel_recall(routes, deadline)
  -> merge_dedup_quota
  -> coarse_rank
  -> fine_rank(multi_objective)
  -> rerank(constraints, diversity, exploration)
  -> expose + log(all_versions, candidates, scores)
```''',
2: '''```python
# 召回链路的最小可观测抽象
u = user_encoder(user_features)
candidates, ann_meta = ann_index.search(u, topk=K)
log({
    "model_version": model_v,
    "index_version": index_v,
    "candidate_count": len(candidates),
    "ann_latency_ms": ann_meta.latency_ms,
})
```''',
3: '''```python
# 排序伪代码：特征口径与模型版本一起记录
x_sparse, x_dense = feature_service.fetch(request)
z = interaction_model(x_sparse, x_dense)
score = calibration(model_head(z))
return score
```''',
4: '''```python
history = sessionize(dedup(filter_noise(raw_events)))
seq = encode(history, time=True, action_type=True)
user_state = sequence_model(seq)
score = target_condition(user_state, candidate)
```''',
5: '''```python
shared = shared_or_experts(x)
loss = 0.0
for task in tasks:
    pred = task_head[task](route(task, shared))
    loss += weight[task] * criterion[task](pred, label[task])
loss.backward()
```''',
6: '''```text
Pre-register: unit / traffic / primary / guardrails / MDE / duration
        ↓
A/A & SRM health check
        ↓
Run A/B with stable assignment
        ↓
Check data quality → estimate effect + CI → slice → decide
```''',
7: '''```text
log policy/version/propensity
        ↓
point-in-time sample join
        ↓
train + slice validation
        ↓
shadow/canary serving
        ↓
monitor drift/skew/latency → retrain or rollback
```''',
8: '''```python
score = relevance(item)
score += exploration_bonus(item, uncertainty, age)
score -= redundancy(item, selected)
score = apply_quality_and_safety_gates(score)
```''',
9: '''```text
baseline pipeline
   ├─ stable retrieval/ranking path
   └─ frontier component (shadow)
          ↓ quality / latency / cost / legality
       canary → small A/B → scale-up
          ↓
       always keep fallback
```''',
}

VERIFY = {
1: "离线先做 stage-wise oracle 与分层 slice；线上用稳定 A/B 验证 primary metric，同时守住延迟、负反馈、留存等 guardrail。任何链路改动都应记录候选集合和 score 分布，便于解释增益来自哪里。",
2: "分别测 model exact Recall@K、ANN Recall@K、端到端候选命中；线上同时看 candidate count、route overlap、dedup ratio、P99 和超时降级。若换 sampling policy，应做版本隔离而不是直接与旧模型混训。",
3: "离线至少看 AUC/GAUC、calibration、关键 user/item slice 与 latency profile；线上同时观测 score 分布、特征缺失率、P99 和业务主指标。新增特征要做 cost-aware ablation。",
4: "按序列长度、活跃度、新老用户、行为类型做离线 slice；线上监控 history length、有效事件率、序列缓存命中、每候选交互成本和长序列用户收益。不要只看 overall AUC。",
5: "离线逐任务看 metric、calibration、gradient conflict、gate/expert usage；线上用多指标 Pareto 评价，并设置不能被牺牲的 guardrail。新增任务必须证明共享带来增量而非负迁移。",
6: "实验前预注册 unit、primary、guardrail、MDE、duration；开始后先过 SRM/埋点健康检查，再估计 effect size 与置信区间，最后做 cohort heterogeneity 和长期回看。",
7: "同时监控数据分布、feature freshness、missing/default ratio、model/index version、P99 与 rollback rate。任何去偏或重采样策略要记录 propensity/weight 分布和 effective sample size。",
8: "把即时效果与长期生态指标拆开：首屏/CTR 之外看兴趣收敛、coverage、供给留存、重复曝光与负反馈。探索策略要有流量上限、质量 gate 和 regret 监控。",
9: "所有前沿组件先 shadow，比较 quality、latency、cost、GPU/CPU utilization、合法 item rate 与 fallback rate；再 canary、小流量 A/B、逐步放量。必须保留成熟 baseline 作为回退。",
}

LOG_FIELDS = {
1: "request_id、user/session、route candidates、每层 input/output 数、feature/model/index/config version、各 stage latency、final scores、rerank reason、exposure/feedback",
2: "positive source、negative source、sampling version、temperature、embedding norm、index version、ANN visited/probe 参数、candidate count、route overlap、retrieval latency",
3: "feature schema/version、missing/default、embedding lookup hit、cross-model version、raw logit、calibrated score、model latency、timeout/fallback",
4: "raw event count、dedup count、session count、sequence length、time span、action types、cache hit、selected history、attention/search latency",
5: "task labels、loss scale、task weights、gradient norm/cosine、gate entropy、expert utilization、per-task prediction/calibration",
6: "experiment id、unit id、bucket、exposure、metric numerator/denominator、SRM counts、assignment version、guardrail、trigger/stop timestamps",
7: "logging policy、propensity、sample weight、feature event_time、join_time、training snapshot、serving version、drift stats、latency/fallback",
8: "cold-start state、exploration reason、uncertainty/bonus、item age、coverage/diversity、quality gate、negative feedback、long-term outcome",
9: "baseline/frontier version、token/code version、decode steps、valid-item rate、GPU utilization/MFU、latency、cost/request、fallback reason、online lift",
}

CONFUSIONS = {
1: "模型指标 vs 系统指标；候选质量 vs 排序质量；请求级优化 vs 用户长期效用；平均延迟 vs P99。",
2: "训练负样本 vs 真负反馈；exact retrieval vs ANN retrieval；embedding 相似度 vs 概率；model recall vs route marginal recall。",
3: "特征数值尺度 vs embedding 表示；显式交叉 vs MLP 隐式交叉；AUC 排序性 vs calibration 概率性。",
4: "行为序列 vs 兴趣状态；target-aware attention vs self-attention；FlashAttention 的 IO 优化 vs O(L²) pair 数。",
5: "共享表示 vs 共享专家；任务相关性 vs 标签共现；loss 平衡 vs 业务权重；多任务提升 vs Pareto/跷跷板。",
6: "统计显著 vs 业务显著；AUC vs GAUC；随机切分 vs time split；实验随机化 vs 日志无偏。",
7: "相关性修正 vs 因果去偏；class imbalance vs sample selection bias；online inference vs online learning；feature cache vs point-in-time correctness。",
8: "多样性 vs 随机性；探索 vs 低质保量；长尾公平 vs 均匀曝光；短期 CTR vs 长期生态。",
9: "Generative 推荐 vs LLM 推荐；Semantic ID vs 原始 item ID；模型参数大 vs 可 scaling；论文吞吐 vs 真实端到端 serving。",
}

# Primary-source links for clusters. These supplement, not replace, the existing interview references.
PRIMARY = {
14:'- **YouTube DNN Recommendation (candidate generation / ranking)** — https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/',
27:'- **Factorization Machines** — https://www.csie.ntu.edu.tw/~b97053/paper/Rendle2010FM.pdf',
28:'- **Wide & Deep Learning for Recommender Systems** — https://arxiv.org/abs/1606.07792',
29:'- **DeepFM (IJCAI 2017)** — https://www.ijcai.org/proceedings/2017/239',
31:'- **Deep & Cross Network** — https://arxiv.org/abs/1708.05123',
32:'- **DCN V2 (WWW 2021)** — https://doi.org/10.1145/3442381.3450078',
39:'- **DIN** — https://arxiv.org/abs/1706.06978',
43:'- **DIEN (AAAI 2019)** — https://ojs.aaai.org/index.php/AAAI/article/view/4545',
48:'- **SIM (CIKM 2020)** — https://doi.org/10.1145/3340531.3412744',
53:'- **MMoE (KDD 2018)** — https://doi.org/10.1145/3219819.3220007',
56:'- **PLE (RecSys 2020)** — https://doi.org/10.1145/3383313.3412236',
60:'- **ESMM** — https://arxiv.org/abs/1804.07931',
94:'- **Generative Recommenders / HSTU (ICML 2024)** — https://proceedings.mlr.press/v235/zhai24a.html',
98:'- **RankMixer (2025)** — https://arxiv.org/abs/2507.15551',
}
# inherit cluster references across neighboring questions
for ids, refid in [
    (range(14,26),14),(range(27,31),29),(range(31,33),32),(range(39,43),39),
    (range(43,46),43),(range(47,51),48),(range(51,56),53),(range(56,59),56),
    (range(59,62),60),(range(94,98),94),(range(98,101),98)
]:
    for i in ids:
        PRIMARY.setdefault(i, PRIMARY.get(refid,''))

START='<!-- V2_ENRICHMENT_START -->'
END='<!-- V2_ENRICHMENT_END -->'


def build_block(q: dict) -> str:
    qid=q['id']; ch=q['chapter']; p=PROFILES[qid]
    title=q['title']
    primary=PRIMARY.get(qid,'')
    return f'''{START}

## V2 深度版：从“会答”到“能落地”

{CHAPTER_LENS[ch]}

### 针对本题的关键推导

{p['deep']}

这里建议把回答进一步拆成四层证据链：

1. **定义层**：一句话说明“{title}”讨论的对象和优化目标；
2. **机制层**：给出公式、数据生成过程或计算复杂度，解释为什么会有效；
3. **系统层**：指出它在完整推荐链路中的上游输入、下游依赖、成本和失败传播路径；
4. **验证层**：给出 offline slice、线上 A/B、guardrail 与回滚条件。

### 90 秒标准回答（建议练到可以脱稿）

> {p['deep']} 具体到工程上，可以用下面的数量级来理解：{p['case']} 因此我不会只看单一离线指标，而会把这项方法放回完整链路，联合检查候选/特征分布、P95/P99、成本以及线上主指标。如果出现“离线好、线上差”，我会优先检查数据与 serving 一致性、截断/近似误差和策略覆盖。最后还要说明边界：{p['boundary']}

这段 90 秒回答的顺序是 **结论 → 机制 → 数量级 → 工程验证 → 边界**。对于大多数推荐算法题，这比从论文历史开始讲更稳。

### 容易混淆的概念

{CONFUSIONS[ch]}

### 上线验证与监控

{VERIFY[ch]}

**建议至少记录这些字段：** {LOG_FIELDS[ch]}。日志字段不是越多越好，关键是能把一次线上曝光追溯到样本、特征、模型、索引和实验版本。

### 一个可用于面试的具体例子

{p['case']}

面试里具体数字的价值不是“显得真实”，而是迫使方案满足数量级约束。即使没有真实业务数据，也可以明确说“下面用数量级举例”，然后说明候选数、样本量、维度、QPS 或延迟如何影响设计。

### 工程决策矩阵

{DECISION_TABLES[ch]}

回答时不要把所有维度都平均展开。先指出当前题目的**第一瓶颈**，再解释为什么其他维度是二阶约束，这会比罗列术语更像真实工程决策。

### 参考实现 / 伪代码

{PSEUDO[ch]}

这段代码不是为了背 API，而是帮助建立“输入—状态—输出—监控”的工程直觉。真实系统还应记录 feature/model/index/experiment 等版本，确保线上结果能够复现。

### 边界条件与反例

{p['boundary']}

一个强候选人应该主动说明**什么时候不应该使用当前方法**。这能证明你理解的是归纳偏置与业务条件，而不是模型名称。

### 面试官继续追问时，建议用这套框架

- **追公式**：先定义符号，再说明每一项改变了什么概率/几何/梯度；
- **追为什么**：从数据分布或复杂度出发，不用“实验发现更好”作为唯一理由；
- **追线上**：给 P95/P99、候选数、内存、特征 freshness、回退路径；
- **追效果**：区分离线增量、stage-wise oracle、线上 causal lift；
- **追失败**：给至少一个会让方案失效的分布变化或系统约束。

### Senior / Staff 级加分点

如果面试岗位偏高级，可以进一步讨论：

- **反事实与增量价值**：新模块到底创造了新候选/新信息，还是复制已有能力；
- **Pareto frontier**：质量、延迟、成本、稳定性之间是否存在更优点，而不是只报单指标；
- **可观测性**：出现线上退化时，能否在 10~30 分钟内通过 dashboard/slice 定位到具体 stage；
- **可演进性**：模型升级是否要求全量重建特征/索引，是否支持 shadow、canary 和快速 rollback；
- **组织成本**：跨团队依赖、数据口径与长期维护是否会吞掉理论收益。

### 进一步阅读（原始来源优先）

{primary if primary else '- 本题优先结合本页“参考资料”中的原始论文、官方技术材料与公开面经阅读；面经用于理解问法，论文用于校准技术事实。'}

{END}'''

for q in MANIFEST['questions']:
    path=ROOT/q['path']
    text=path.read_text(encoding='utf-8')
    block=build_block(q)
    if START in text:
        text=re.sub(re.escape(START)+r'.*?'+re.escape(END), lambda _m: block, text, flags=re.S)
    else:
        anchor='\n## 工业级工程视角\n'
        if anchor not in text:
            raise RuntimeError(f'missing anchor {path}')
        text=text.replace(anchor, '\n'+block+'\n\n## 工业级工程视角\n', 1)
    path.write_text(text, encoding='utf-8')

print('enriched', len(MANIFEST['questions']), 'question files')
