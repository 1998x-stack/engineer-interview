from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QDIR = ROOT / "questions"

# 每题的专家级增补：定量抓手 / 工程抓手 / 失败边界 / 专项练习。
# 这些内容用于在已有 PDF 题解基础上继续扩展，而不是替代基础答案。
E = {
1:("线性层的复合仍属于仿射变换族；真正增加函数族复杂度的是层间非线性。可进一步从 piecewise-linear region 数量理解 ReLU 深度带来的表达效率。","做 XOR / two-moons：同参数量下比较纯线性网络与 ReLU MLP，画出决策边界；再把中间 ReLU 去掉验证两层线性可折叠。","注意‘有 softmax 就不需要 FFN 激活’是错误推论：Attention 的 softmax 负责 token 间权重，FFN 非线性负责逐 token 的通道变换。","白板证明三层纯线性网络可以折叠为一层，并解释为什么加入任意非仿射激活后一般不能折叠。"),
2:("反向模式 AD 对标量损失尤其高效：一次反传可得到损失对大量参数的梯度；核心对象是 vector-Jacobian product，而不是显式构造巨大 Jacobian。","用 `retain_grad()`、hook 与 `torch.autograd.grad` 检查中间节点梯度；对一个两层 MLP 用有限差分做 gradient check。","in-place 修改、detach、跨设备/跨 dtype 操作都可能切断或破坏计算图；‘有 grad 属性’不等于梯度路径正确。","手推 `y=(Wx+b)^2` 的 VJP，再用 PyTorch 对比数值；解释为什么反向传播的内存瓶颈常来自保存 activation。"),
3:("Softmax+CE 的简洁梯度来自 log-softmax 与 NLL 的代数消去：对正确类是 `p_y-1`，对其余类是 `p_i`；这也是 logits 直接喂 CE 比先 softmax 更数值稳定的原因。","构造极端 logits（如 ±1000），比较 `log(softmax(x))` 与 `log_softmax(x)`；验证稳定实现依赖 log-sum-exp trick。","不要把多标签 BCE 与互斥多分类 CE 混淆；label smoothing 后梯度仍可写成 `p-y_smooth`。","现场完整推导 `dL/dz=p-y`，并指出 softmax Jacobian 的对角与非对角项如何相消。"),
4:("比较激活函数不能只看曲线，还要看导数、输出均值、饱和区、计算成本与硬件 kernel。GELU/SiLU 的平滑门控与 ReLU 的硬阈值是关键差异。","统计同一 MLP 在 ReLU/GELU/SiLU 下的 activation mean/std、dead ratio、gradient norm；保持初始化与 seed 不变。","Sigmoid 仍适合作为门控或概率输出，不能因为深层 hidden layer 少用就断言它‘过时’。","给出输入从 -10 到 10 的导数曲线，解释每种激活在大正/大负区间的梯度行为。"),
5:("梯度传播应从 Jacobian 连乘与谱范数理解；Residual/Norm/初始化都在控制深层网络的信号与梯度尺度。","记录每层 activation RMS 与 grad RMS，画 depth-wise 曲线；分别去掉 residual、改变初始化方差、开启 gradient clipping 做消融。","Gradient clipping 主要抑制爆炸，不能从根本解决梯度消失；Pre-Norm 也不是任何深度都无条件稳定。","推导简单线性 RNN 中梯度含 `W_h^k`，用特征值大小解释为什么出现指数衰减或增长。"),
6:("Xavier/Kaiming 本质是近似保持前向/反向方差；Kaiming 中系数 2 来自 ReLU 约一半激活被截断的统计假设。","随机生成 100 层 MLP，分别使用过小、Xavier/Kaiming、过大初始化，画每层方差与梯度方差。","初始化推导依赖独立同分布等近似，残差、Norm、门控激活和超深 Transformer 会改变最合适的 scale。","从 `Var(Wx)=fan_in Var(W) Var(x)` 出发推导 Xavier/Kaiming 的数量级。"),
7:("过拟合不是单一指标，而是 generalization gap 随训练推进扩大；应结合 train/val loss、分层指标、数据切分与学习曲线判断。","画随数据量增加的 learning curve；若训练误差高且验证误差高，更像欠拟合而不是过拟合。","验证集污染、重复样本、时间穿越会让‘验证集很好’反而掩盖真正泛化问题。","给出一个 train loss 降、val loss 先降后升的曲线，说明 early stopping 点与进一步诊断步骤。"),
8:("Label smoothing 等价于把目标分布从 delta distribution 拉向先验分布，抑制无限增大 margin；同时会改变置信度与蒸馏信号。","比较 epsilon=0/0.05/0.1 下 accuracy、NLL、ECE 与最大 logit；不要只看 top-1。","强 smoothing 可能伤害需要精确概率、细粒度区分或 teacher logits 的场景；类别不均衡时均匀先验也未必合理。","写出 K 类 smoothing 后正确类与错误类 target，并推导梯度仍为 `p-y'`。"),
9:("Loss 的选择应由数据生成假设与输出结构决定：MSE 对应高斯噪声的负对数似然，BCE 对应独立 Bernoulli，CE 对应 categorical。","对同一错误幅度比较 MSE、MAE、Huber 的梯度；对多标签任务验证 sigmoid+BCE 与 softmax+CE 的行为差异。","不要根据‘回归/分类’标签机械选择 loss；例如排序、metric learning、分割、检测常需要结构化或组合目标。","从最大似然角度分别写出 Gaussian/Bernoulli/Categorical 的 NLL，并对应到常见 loss。"),
10:("类别不平衡需区分先验不平衡、采样不平衡、难例不平衡与代价不对称；解决手段分别作用于 data、loss、sampling、threshold、metric。","用同一模型比较 class weight、focal loss、balanced sampler、threshold tuning；报告 PR-AUC 与固定 recall 下 precision。","ROC-AUC 在极端负样本占比时可能看起来很好但业务 precision 很差；重采样后概率还可能需要校准。","给出 1:1000 数据，解释为什么 accuracy=99.9% 仍无意义，并设计离线评估表。"),
11:("优化器差异可拆成方向平滑、逐参数预条件、bias correction 与状态内存。Adam 每参数通常维护一阶/二阶矩，因此状态显著大于 SGD。","在狭长二次函数上可视化 SGD/Momentum/Adam 轨迹；记录收敛速度、振荡和最终点。","Adam 的‘自适应学习率’不是简单让每个参数永远有独立固定 LR；其 effective step 同时受 moment 与 epsilon 影响。","写出 Momentum、RMSProp、Adam 更新式并比较每参数状态数量和主要超参数。"),
12:("AdamW 的关键是 decoupled weight decay：衰减直接作用于参数，而非把 L2 项混入被自适应预条件的梯度。","在相同 lr/weight_decay 下比较 Adam(L2) 与 AdamW 参数范数轨迹；对 bias/Norm 参数尝试不做 decay。","‘L2=weight decay’只在特定 SGD 情况可等价，放到 adaptive optimizer 上直接混为一谈会失分。","从 Adam 的 `g/sqrt(v)` 说明为什么把 `λw` 加入梯度会被不同维度的 `v` 非均匀缩放。"),
13:("SGD 与 Adam 的泛化差异不是定理，应结合任务、batch、schedule、regularization 与训练预算；现代大模型大多依赖 AdamW。","固定训练 FLOPs 而非 epoch，比较 SGD/AdamW；同时报告训练 loss 和验证指标，避免用收敛快慢混淆泛化。","‘flat minima 一定泛化好’也有参数化依赖，面试应作为解释假说而非绝对结论。","设计一个公平 optimizer ablation：统一 data order、warmup、总 step，并分别调优 learning rate。"),
14:("Warmup 同时缓解大初始步长、Adam moment 未稳定、深层 residual/Norm 初始尺度不稳；它是优化工程手段而非理论必需组件。","记录前 1k step 的 grad norm、update/weight ratio 与 loss；比较无 warmup、线性 warmup、过长 warmup。","Warmup 太长会浪费训练预算，太短又可能在大 batch/大 LR 下不稳定；最优比例随 token budget 与 optimizer 变化。","解释为什么 linear scaling rule 增大 batch/LR 后通常更依赖 warmup。"),
15:("Cosine decay 的优势是平滑、少拐点、后期逐渐减小更新；真正影响结果的还包括 min LR、warmup、总 token 与是否 restart。","画 constant/linear/cosine 的 LR 与 update norm 曲线；比较相同 area-under-LR 的实验。","不要把 scheduler 与 optimizer 独立讨论：AdamW 的 effective update 并不等于表面 LR。","写出 cosine 公式，计算训练 25%、50%、75% 时的 LR 比例。"),
16:("BN 既有归一化效应，也引入 batch-dependent noise；训练使用当前 mini-batch 统计，推理使用 running statistics 是最常考的行为差异。","用同一 batch 在 `train()` 与 `eval()` 下前向，打印 running_mean/var；再改变 batch composition 看单样本输出是否改变。","小 batch、domain shift、冻结错误和 SyncBN 配置不一致都可能造成 train/eval gap。","手推单通道 BN forward，并说明 `gamma/beta` 为什么使网络仍能恢复任意仿射尺度。"),
17:("BN 与 LN 的根本差别是归一化维度和统计依赖：LN 对单样本 hidden dimension 归一化，不依赖其他样本，适合变长序列与 autoregressive serving。","对 `[B,T,D]` 明确写出 BN/LN 分别在哪些轴算 mean/var，并用 batch=1 验证差异。","‘CNN 用 BN、Transformer 用 LN’是经验主流而非物理定律；ConvNeXt 等视觉架构也大量使用 LN。","给 `[B,T,D]` 与 `[B,C,H,W]` 两种张量，现场圈出 BN/LN/GN 的统计轴。"),
18:("RMSNorm 只规范 root-mean-square，不做减均值；通常少一次 mean 计算并保留输入均值信息。现代 LLM 中常与 Pre-Norm 搭配。","实现 20 行 RMSNorm，与 PyTorch LayerNorm 比较输出均值、RMS 与反向梯度。","RMSNorm 更快并不意味着在所有硬件上都显著更快；kernel fusion 和 memory traffic 才决定端到端收益。","写出 RMSNorm 公式并解释可学习 scale 的 shape 为什么通常是 `[D]`。"),
19:("Pre-Norm 把 normalization 放在子层前，residual 主干更接近 identity，梯度可沿 shortcut 直接传播；Post-Norm 往往需要更谨慎的初始化/warmup。","训练深度逐渐增加的 toy Transformer，比较 pre/post norm 的 grad norm 与 loss stability。","Pre-Norm 的稳定性优势可能伴随表示尺度与深度利用问题，现代架构还有 sandwich norm、QK norm 等变体。","对一个 residual block 写出两种结构的梯度路径，指出 identity term 出现在哪里。"),
20:("Dropout 可理解为训练时随机采样子网络并用期望尺度校正；实际作用与 batch size、Norm、数据规模和模型规模耦合。","验证 inverted dropout：训练时 `E[y]≈x`，eval 时不再随机 mask；测试 seed 与 train/eval 切换。","在大规模 LLM 预训练中 dropout 可能很低甚至为 0；不能把它当成必需的泛化手段。","推导 keep probability=p 时为何训练输出通常除以 p。"),
21:("卷积输出尺寸应同时考虑 dilation；参数量与空间分辨率无关，而 FLOPs 与输出 H×W 成正比。","写一个函数随机生成 H/W/K/S/P/D，和 `nn.Conv2d` 输出 shape 自动对拍；再计算 MACs。","常见错误是把 padding 或 dilation 公式漏掉，以及把 groups 卷积参数量仍按普通卷积计算。","给定 `B=8,Cin=64,H=W=56,Cout=128,K=3,S=2,P=1`，现场算输出、参数量和近似 MACs。"),
22:("理论感受野可递推计算 jump 与 receptive field；有效感受野通常集中在理论范围中央，并不均匀覆盖整个区域。","写递推器计算任意 conv/pool 堆叠的 receptive field；再用输入梯度热图观察 effective receptive field。","仅仅增大 dilation 会造成 gridding artifact；大感受野也不等价于模型真正利用了远距离信息。","掌握递推：`j_l=j_{l-1}s_l`，`r_l=r_{l-1}+(k_l-1)d_l j_{l-1}`。"),
23:("1×1 卷积本质是每个 spatial location 上共享权重的 channel mixing，可用于 bottleneck、升降维、跨通道投影。","比较 3×3 Cin→Cout 与先 1×1 降维再 3×3 的参数/FLOPs，给出实际数字。","1×1 不直接扩大空间感受野，但堆在已有空间算子后可混合来自不同感受野的通道特征。","计算 `256→64→256` bottleneck 与直接 `256→256 3×3` 的参数量比例。"),
24:("Depthwise separable conv 将 spatial filtering 与 channel mixing 解耦：depthwise 每通道独立卷积，再用 pointwise 混通道。","对 `Cin=Cout=256,K=3` 计算普通卷积与 DW+PW 的 MAC 比例，并用 profiler 验证实际延迟未必同比例下降。","理论 FLOPs 少不保证墙钟时间更低，小算子、memory access 和 kernel support 会限制收益。","推导普通卷积与 depthwise+pointwise 的参数量公式，并求比值极限。"),
25:("Residual connection 改变优化问题：目标函数可以围绕 identity 做增量修正，同时提供短梯度路径；这比‘防止梯度消失’更完整。","训练 plain 20/56 层与 residual 版本，比较 training error 而非只看 validation；观察 degradation problem。","Residual 不保证任意深度稳定，仍依赖 normalization、initialization、residual scaling 与 optimizer。","从 `y=x+F(x)` 写出 `dy/dx=I+dF/dx`，解释 identity 项的意义。"),
26:("小 batch BN 的核心问题是样本统计估计方差大；检测/分割因高分辨率导致 per-GPU batch 小，因此 GN/FrozenBN/SyncBN 常见。","固定全局 batch，改变每卡 batch 与是否 SyncBN，比较输出统计和吞吐通信成本。","SyncBN 解决统计样本不足但引入跨卡通信；FrozenBN 适合迁移学习但可能受 domain shift 影响。","给出 batch=1 的极端例子，解释 BN 统计为什么不可靠以及 GN 为什么不依赖 batch。"),
27:("NMS 是 greedy selection；IoU 只是几何重叠度，不包含置信度或类别语义。工程实现要注意坐标约定、空框、同分数稳定排序与 class-aware 处理。","随机生成 boxes，与 torchvision NMS 对拍；测试完全重叠、不相交、零面积、不同类别等边界。","Soft-NMS 不直接删除高重叠框，而是衰减 score；在拥挤场景可能优于 hard NMS。","手写 vectorized IoU，再分析 naive NMS 的最坏 O(N²) 与预筛 Top-K 的意义。"),
28:("Focal Loss 的 `(1-p_t)^γ` 动态降低 easy example 权重；α 主要处理类别先验，γ 主要处理难易不平衡，两者作用不同。","画不同 γ 下 loss/gradient 对 `p_t` 的曲线；观察 hard positive 与 easy negative 的相对权重。","γ 过大可能让训练只盯极少难例并放大 label noise；检测器中还需考虑正负样本定义和 assignment。","从 CE 乘 modulating factor，解释 `p_t→1` 与 `p_t→0` 两个极限。"),
29:("CNN 强 locality/translation equivariance inductive bias；ViT 通过 patch token + global attention 用更弱先验换取数据规模与可扩展性。","在小数据/大数据两个 regime 比较 CNN/ViT；控制参数量并记录训练速度、数据增强依赖与迁移性能。","‘ViT 一定比 CNN 强’不成立；输入分辨率使 token 数平方增长，patch size 也会影响细粒度信息。","计算 224² 图片在 patch=16/14 下 token 数，并估算 attention score matrix 大小。"),
30:("Mixup 在输入和标签空间做凸组合，鼓励近似线性行为；CutMix 保留局部真实纹理并按区域面积混合标签。","固定 backbone，比较普通增强/Mixup/CutMix 的 calibration、robustness 与 localization 影响。","增强策略会改变 label semantics；目标检测、分割和细粒度任务不能直接照搬分类配置。","给定 λ 与 CutMix patch 面积，计算修正后的标签权重并解释为何要按实际裁剪面积重算。"),
31:("RNN/LSTM/GRU 应从状态更新方程、门控数量、并行性和长期依赖路径比较；GRU 参数少不必然性能更差。","用同一 hidden size 计算三者参数量，并在长依赖 toy task 上比较梯度与收敛。","现代序列建模已大量使用 Transformer，但 RNN 仍可能在流式、低延迟、小设备场景有价值。","写出 LSTM 四门与 GRU 两门方程，比较每步矩阵乘次数。"),
32:("LSTM 的关键是 cell state 的近似加性更新，梯度可乘 forget gate 而非每步都通过同一个饱和非线性矩阵。","构造 100-step copy task，记录普通 RNN 与 LSTM 对早期输入的梯度范数。","forget gate 长期小于 1 仍会衰减；LSTM 是缓解而不是数学上彻底消除梯度消失。","从 `c_t=f_t c_{t-1}+...` 推导 `∂c_t/∂c_{t-k}` 的乘积结构。"),
33:("Teacher forcing 的 train/inference context distribution 不一致形成 exposure bias；误差在自回归 rollout 中会累积。","比较 teacher-forced validation loss 与 free-running sequence quality；尝试 scheduled sampling 并观察副作用。","scheduled sampling 本身也可能引入不一致估计；现代 LLM 更多从数据、sequence-level objective 或 RL 角度处理。","给出一个早期 token 预测错误导致后续条件分布完全改变的例子，解释 token-level loss 的局限。"),
34:("BERT 的 MLM 允许双向上下文编码；NSP 是原始目标之一，但后续工作表明并非所有预训练都必须依赖它。","实现动态 mask，检查 80/10/10 mask 策略与仅对被选 token 计 loss；比较静态/动态 masking。","回答时要区分 BERT 原始设计和后续 RoBERTa 等改动，避免把 NSP 说成 Encoder-only 的必要条件。","解释 MLM 为什么不能像 decoder LM 那样天然直接做长文本自回归生成。"),
35:("架构选择本质由信息流约束决定：Encoder 双向表征；Decoder 因 causal mask 适合生成；Encoder-Decoder 用 cross-attention 建模输入输出两套序列。","画三种 attention mask / cross-attention 数据流，并比较同 token budget 的训练/推理缓存结构。","不要用‘理解 vs 生成’一刀切：decoder-only 也能做分类/表征，encoder 也可配 decoder 完成生成。","给搜索排序、机器翻译、对话生成三个任务，说明为什么选对应架构并列出替代方案。"),
36:("Subword tokenizer 在词表大小与序列长度之间折中；BPE/WordPiece 的训练准则不同，SentencePiece 还强调从 raw text 直接建模并可处理空格。","训练一个极小 BPE tokenizer，逐轮打印 merge；比较中文、英文、代码文本的 token fertility。","tokenizer 是模型接口的一部分：改词表会影响 embedding、长度分布、成本和兼容性，不能随意替换。","对一个罕见词手算 3 轮 BPE merge，并解释 byte-level fallback 对 OOV 的意义。"),
37:("Causal LM 的 label shift 与 padding mask 是两件事：padding 位置通常设 ignore_index；是否 mask prompt 取决于训练目标。","构造左右 padding 两个 batch，逐 token 打印 input/labels/loss mask，确认 shift 后监督位置正确。","只改 attention_mask 不等于 loss 会忽略 pad；必须理解模型 forward 内部如何 shift labels。","给一段 prompt+assistant token 序列，标出每个位置的 label 与 -100。"),
38:("Padding mask 屏蔽无效 token；causal mask 屏蔽未来 token。二者常通过逻辑与合并并广播到 `[B,1,Tq,Tk]` 或 kernel 特定格式。","对 batch 内不同长度序列可视化最终 mask matrix；测试全 mask 行避免 softmax NaN。","左 padding + KV cache/position_ids 是常见坑，不能只看二维 attention_mask。","手画 T=5 的下三角 causal mask，并叠加一个长度=3 的 padding mask。"),
39:("现代 decoder block 应说清 Norm→Attention→Residual→Norm→FFN/MoE→Residual，并注明具体模型可能使用 RMSNorm、SwiGLU、RoPE、GQA。","打印一个真实开源模型 config，把 textbook Transformer 与实际 block 参数逐项对照。","不要把原始 2017 Transformer 的 Post-Norm、sinusoidal PE 当成所有现代 LLM 的默认实现。","给定 D、H、FFN hidden，估算一层 attention/FFN 参数量并判断哪部分更大。"),
40:("Attention 可分为 similarity、normalization、weighted aggregation 三步；mask 在 softmax 前作用于 logits，数值稳定通常使用 fp32 accumulation/融合 kernel。","手写 attention 与 `torch.nn.functional.scaled_dot_product_attention` 对拍，覆盖 causal/padding、fp16、极端 logits。","不能把 `QK^T` 当最终结果；softmax 的归一化维度、scale 和 mask 任一错都可能 silent bug。","从 `[B,H,T,Dh]` 写出每一步 shape、广播关系与复杂度。"),
41:("除以 √d_k 是控制 dot-product variance 的近似；若 Q/K 已有其他归一化或 QK-Norm，最佳 scaling 机制可能变化。","随机采样不同 d_k 的 Q/K，画未缩放/缩放 logits std 与 softmax entropy。","不要说‘防止梯度爆炸’就结束；直接机制是避免 logits 随维度变大导致 softmax 饱和。","假设 q_i,k_i 独立零均值方差 1，推导 dot-product 方差为 d_k。"),
42:("Q/K/V 是从同一 hidden state 通过不同线性投影得到的角色化表示：Q 负责发起匹配，K 负责被匹配索引，V 承载被聚合内容。","冻结模型，分析 Q/K cosine 与 attention map；交换 K/V 投影观察输出语义与 shape 虽合法但功能失效。","Q/K 相似度高不等于 V 也相似；这正是检索权重与传输内容解耦的意义。","用数据库检索类比解释 Q/K/V，同时回到矩阵公式避免只讲比喻。"),
43:("标准 dense attention 的 score 相关项是 O(T²Dh) / O(T²) memory，但整个 Transformer layer 还有 QKV/FFN 的 O(TD²)；哪个占主导取决于 T 与 D。","对 D=4096、不同 T 计算 attention 与 projection FLOPs 的交叉点；记录显存随 T 的增长曲线。","只说‘Transformer 是 O(T²)’过于粗糙：训练 activation、FlashAttention 和 decode KV cache 的瓶颈形式都不同。","写出一层 MHA 的 projection 与 score 两部分复杂度，说明短序列时为何 FFN/linear 可能更贵。"),
44:("Multi-head 的价值不只是‘关注不同位置’，更重要是不同 learned projection subspace 并行建模关系；最终 concat+O projection 再融合。","可视化不同 head attention entropy/距离分布，并做 head pruning 观察冗余。","head 可高度冗余，head 数增加也不等于表达力线性增加；head_dim 与 kernel efficiency 也要考虑。","在固定 D 下说明 H 增加时 Dh 下降，MHA 主体参数量为何大体不因 H 线性增加。"),
45:("纯 self-attention 对 token permutation 缺少顺序信息；位置机制可注入 absolute index 或直接影响相对 pairwise interaction。","移除/打乱 position 信息训练顺序敏感 toy task，观察准确率；比较 absolute 与 RoPE 外推。","位置编码不是统一的‘加一个向量’：RoPE、ALiBi 等可能直接改 attention score 几何。","证明没有位置编码时 self-attention 对输入 permutation 的等变性。"),
46:("RoPE 将每对隐藏维度视作二维平面按位置旋转，使 `q_m^T k_n` 只与相对位置差的旋转有关；频率分布决定不同尺度的位置敏感性。","实现最小 RoPE，验证对 Q/K 同时旋转后内积满足相对位移性质；测试超训练长度时角频率变化。","长上下文扩展通常不是‘直接把 max_position 改大’，还涉及频率缩放与训练/微调分布。","用二维旋转矩阵推导 `R_m^T R_n = R_{n-m}`。"),
47:("Attention 主要做 token mixing，FFN/MoE 主要做每 token 的 channel-wise 非线性变换；SwiGLU 还引入门控乘法。","统计一层 attention 与 FFN 参数/FLOPs；把 FFN hidden ratio 从 4x 调整，观察容量与速度。","删除 FFN 并不让网络完全线性，因为 attention 有 softmax，但会大幅限制逐位置特征变换容量。","写出 GELU FFN 与 SwiGLU 公式，比较参数量在相同 intermediate size 下的变化。"),
48:("MHA/MQA/GQA 的核心区别是 Q head 与 KV head 的共享比例；GQA 用少量 KV heads 在质量与 cache/带宽之间折中。","给定 Hq=32、Hkv=8/1，计算 KV cache 和 decode KV bandwidth 比例；检查 tensor shape 重复/广播方式。","GQA 省的是 KV 相关内存/带宽，不会把所有 attention 计算按同样比例降低；Q heads 仍然存在。","画出 32 query heads 映射到 8 KV groups 的关系，并写出 cache 公式。"),
49:("KV cache 的量纲必须说全：层数×batch/并发×序列长度×KV heads×head_dim×K/V×dtype；serving 还要加 block 对齐、prefix sharing 与并行分片。","写容量规划脚本，对 context/并发/Hkv 做参数扫描；分别估算 MHA/GQA/MQA 与 BF16/FP8 KV。","缓存 Q 没有同等复用价值：decode 每一步只需要当前 query，而历史 K/V 会被所有未来 query 反复读取。","给定模型配置和 24 GiB 可用 cache 预算，反推可容纳的 token slots/并发。"),
50:("FlashAttention 是 IO-aware exact attention：用 tiling 与 online softmax 避免物化完整 score/probability 到 HBM；FLOP 阶数仍是 dense O(T²D)。","在支持环境中比较 eager attention、SDPA/Flash backend 的 peak memory 和 latency，按 T 扫描而非只测一个点。","短序列、小 batch 或 kernel fallback 时收益可能不明显；mask/head_dim/layout 也会影响可用 backend。","推导 online softmax 的 running max/running sum 更新，并解释旧 block 输出为什么需要 rescale。"),
51:("Sparse/sliding-window 通过限制连接图改变实际计算量；局部窗口适合局部依赖，但全局信息需 global token、dilation、跨层传播或混合层补偿。","实现 window mask，比较 T 增长时 dense 与 window attention 的 score 元素数；在长程 copy task 上观察质量退化。","Sliding-window 的理论 O(Tw) 只有在 kernel 真正利用 sparsity 时才转化为速度；生成 cache 策略也要匹配窗口。","给 T=128k,w=4k 估算连接数相对 dense 的比例。"),
52:("Decoder-only 用统一 next-token objective 覆盖生成、in-context learning 与任务序列化，工程栈和 scaling 简洁；并非因为 encoder ‘没有用’。","同一任务构造成 classifier encoder 与 prompted decoder，比较 token/latency/训练目标。","检索 embedding、token classification 等场景 encoder-only 仍可能更高效；架构选择要结合输出模式。","从 causal factorization `P(x)=∏P(x_t|x_<t)` 解释统一生成目标。"),
53:("Transformer 训练可对序列位置并行，而 RNN 有严格时间依赖；同时任意 token 间的最短路径更短。但 attention 带来二次序列成本。","测同 hidden size 下序列长度增加时 RNN 与 Transformer training throughput；区分训练与 autoregressive decode。","Transformer 的 decode 仍是 token-by-token 串行，不能把‘训练并行’误说成‘生成完全并行’。","比较两个相距 k 的 token 在 RNN 与单层 self-attention 中的信息路径长度。"),
54:("长上下文问题至少分 capacity、compute/memory、position extrapolation、有效利用与数据/eval；窗口大只是 capacity，不代表 retrieval/use 能力等比例增加。","做 needle-in-a-haystack 的 position×length 网格测试，同时加入多 needle 与 distractor，避免单一 benchmark。","Lost-in-the-middle、attention sink、RoPE extrapolation、KV capacity 是不同层面问题，不应混成一个‘长上下文退化’。","设计 4 个实验分别隔离位置、长度、噪声数量和答案距离。"),
55:("手写 MHA 的评分点是 shape、mask、scale、softmax 稳定、contiguous/view 与 API 语义；代码短并不代表容易。","写 reference 版本与 SDPA 对拍 forward/backward；测试 batch=1、T=1、causal+padding、fp16。","`-inf` mask 与全 mask 行、bool/float mask 语义、transpose 后 view 是高频 bug。","要求自己在 15 分钟内无提示写完，并逐行口述 shape。"),
56:("LoRA 认为任务适配的更新可在较低秩子空间表达；训练参数量约 `r(d_in+d_out)`，前向增加低秩两次投影。","对不同 r、target modules 做参数量/显存/质量曲线；训练后对 ΔW 做 SVD 检查有效谱。","低秩是经验假设而非普适定理；domain shift 大、数据足、预算高时 full FT 仍可能更优。","给 4096×4096 线性层计算 r=8/64 的可训练参数比例，并讨论 merge 后推理开销。"),
57:("经典 LoRA 让 B=0、A 随机，使初始 ΔW=0 但第一步 B 有梯度；若 A、B 都为 0，则两侧梯度都可能为 0。现代 PEFT 还支持 PiSSA/EVA/LoftQ/rsLoRA 等初始化或缩放。","打印 LoRA A/B 第一 step 的 grad norm，验证双零初始化退化；比较 rank 与 `alpha/r`、`alpha/sqrt(r)` scaling。","rank 不是越大越好：更大容量增加显存/通信且可能需要不同 scaling；target module 的选择往往和 rank 同样重要。","手推 `ΔW=BA` 时 `∂L/∂A=B^T G`、`∂L/∂B=GA^T`，解释初始化梯度。"),
58:("QLoRA 的关键不是‘LoRA 也 4bit’，而是冻结基座以 4-bit 存储/计算反量化，adapter 仍以较高精度训练；NF4、double quantization 与 paged optimizer 是经典组成。","测 base 4-bit + LoRA 与 BF16 LoRA 的峰值显存、tokens/s、验证指标；确认 quantization compute dtype。","4-bit weight storage 不等于所有 runtime tensor 都 4-bit；activations、LoRA、部分 optimizer/state 仍更高精度。","做 7B 权重存储量级估算，并列出实际显存中额外的 scales、activations、KV。"),
59:("Full FT 与 LoRA 是 capacity/成本/部署治理的决策题：看 domain shift、数据规模、是否需改变知识、硬件、adapter 多租户与最终合并策略。","设计一个决策矩阵：质量上限、训练显存、checkpoint 大小、灾难性遗忘、推理部署、版本管理。","不能仅凭训练样本少就自动选 LoRA；某些小数据任务 full FT 配强正则仍可行，反之大数据也可用 LoRA 做高效适配。","给出两个项目情境，现场说明选择并写出你会跑的最小 ablation。"),
60:("SFT 的上限常由数据混合、去重、格式一致性与难度分布决定；数据流水线必须版本化并可追溯到 source→transform→sample。","为 dataset 生成 data card：来源比例、token 长度、语言/domain、重复率、拒答比例、质量分、train/val leakage。","高质量过滤器本身会引入 selection bias；synthetic data 还需防 teacher artifact、模板污染与 benchmark contamination。","设计从 raw dump 到 train shard 的 10 步 DAG，并为每一步列可监控指标与 rollback 条件。"),
61:("Label mask 决定模型‘在哪些 token 上被监督’，必须与 chat template、shift、packing 和多轮 assistant span 对齐。","可视化一条多轮样本的 token、role、label、loss mask；随机抽样 100 条人工 spot-check。","只按字符串位置 mask 很脆弱；模板特殊 token、截断、packing 边界可能造成 user token 被误监督。","给一条 system/user/assistant/user/assistant 序列，逐 token 标注监督区间。"),
62:("SFT loss 抖动要区分正常 batch variance、数据 outlier、数值异常和 optimizer instability；先用 token-level/slice 诊断再调参。","记录 loss、grad norm、max logit、tokens/batch、长度、domain；对异常 step 回放原始 sample。","盲目降低 LR 可能掩盖坏数据/label bug；NaN 首先定位首次出现在哪个 tensor 和哪个 step。","画一棵从 sample→forward logits→loss→grad→optimizer 的排障树并注明每层观测量。"),
63:("经典 PPO-RLHF 需区分 policy、reference、reward model、value/critic；rollout 后基于 reward+KL 构造 return/advantage，再做 clipped policy/value update。","画一次迭代的数据流并估算四模型驻留/推理成本；记录 ratio、clip fraction、KL、entropy、value loss。","PPO 的稳定性来自一组约束而非单一 clip；reward scale、GAE、batch reuse 和 policy lag 都会影响训练。","写出 clipped surrogate 并解释 `min` 为什么对正负 advantage 形成不同截断。"),
64:("DPO 把偏好优化重写为 policy 与 reference 的 log-ratio logistic objective，省去显式 reward model 拟合和在线 rollout。","手算一个 chosen/rejected pair 的 DPO margin；比较不同 β 对梯度与 reference 约束的影响。","DPO 不等于‘没有 reward 假设’，其推导仍对应特定 Bradley–Terry/隐式 reward 结构；数据质量与 preference noise 很关键。","从 chosen/rejected logprob 写出 DPO loss，并解释 length normalization 是否会改变偏好。"),
65:("GRPO 用同 prompt 的 group responses 做相对 reward 标准化，移除独立 critic；但 rollout、old/current logprob、KL 与 verifier 仍构成复杂系统。","对 G=2/8/32 模拟 reward，统计 advantage 方差；构造全相同 reward 验证学习信号退化。","group 内比较会受采样温度、答案长度和 reward scale 影响；若 reward 大量 ties，增加 G 不一定有用。","推导 group-normalized advantage，并讨论 zero-variance、outlier reward 与 per-token credit assignment。"),
66:("KL 约束扮演 trust-region/anchor：限制 policy 偏离 reference，维护语言能力并抑制 reward exploitation；实现可为 reward penalty 或 loss term。","画 reward 与 KL 随 β 的 Pareto 曲线；使用 adaptive KL controller 观察 target KL 稳定性。","KL 太强会阻碍学习，太弱会漂移；token-level forward/reverse KL 的估计方式也有差异。","给定两组 token distribution 计算 KL，并解释为什么罕见 token 的概率变化可能贡献很大。"),
67:("Reward hacking 是 policy 优化 proxy 的必然风险：格式、长度、关键词、grader 漏洞、工具调用捷径都可能提高分数却偏离真实目标。","对 reward 高分样本做 slice+人工审查；构造 adversarial prompts 和 hidden tests，比较 reward 与真实 success 的相关性。","单纯加更多 reward 项可能形成新的 gaming surface；需要独立 eval、verifier diversity、holdout 和规则约束。","举一个可验证任务的 reward exploit，设计至少三层检测与缓解。"),
68:("后训练达标必须建立多目标 gate：能力、回归、安全、格式、长度、稳定性、reward/KL 与 cost；平均分不能替代 slice。","建立 baseline→candidate scorecard，加入置信区间/paired test、regression budget 和人工 blind review。","训练 reward 上升而 held-out task 下降是典型失败；还要关注输出长度增长造成的假提升和 serving 成本。","为一个推理模型设计 release gate：哪些指标必须 hard pass，哪些允许 Pareto trade-off。"),
69:("InfoNCE 可视为 batch 内分类：正 pair 是目标类，其他 key 为 negatives；温度控制 logit scale，表示通常先 L2 normalize。","实现 symmetric InfoNCE，比较 batch size/negative 数量对 loss 与 retrieval recall 的影响。","in-batch negative 默认假设其他样本为负，false negative 会造成偏差；分布式 all-gather negatives 还需注意 gradient 语义。","从 cross-entropy 视角推导一个 query 对 N keys 的 InfoNCE。"),
70:("temperature 改变 softmax entropy 与梯度集中度；可学习 temperature 要限制范围，否则 logit scale 可能无界。","扫描 τ，画 positive probability、entropy、grad norm；在含 label noise 数据上观察小 τ 放大 hard/noisy negative。","τ 最优值与 embedding normalization、batch size、negative hardness 耦合，不能独立套用 0.07。","对固定 similarity `[0.8,0.6,0.1]` 手算两种 τ 的 softmax 趋势。"),
71:("False negative 本质是语义上正但被 objective 当负，会把本应相近的表示推远；在推荐、多标签、近重复数据尤其常见。","用 metadata/teacher similarity 标记疑似 false negatives，比较过滤、multi-positive、debias loss。","hard negative mining 会同时提高有效难例与 false-negative 风险，必须配合语义过滤。","设计一个 batch 内多正样本 loss，让同一 query 的多个 positives 不互相竞争。"),
72:("CLIP 通过大规模 image-text contrastive alignment 把两模态映射到共享 embedding space；zero-shot 分类本质是 image 与 class prompt embeddings 的相似度分类。","对同类别写多种 prompt template 做 prompt ensembling；比较 raw class name 与自然语言 prompt。","zero-shot 受 prompt、domain shift、类别名语义和训练数据偏差影响；不是无监督万能分类器。","写出 image→embedding、text prompts→embedding、cosine×temperature→softmax 的完整推理链。"),
73:("多模态 LLM 的核心接口是把视觉 encoder 输出映射/压缩成 LLM 可消费的 token 表示；projector、cross-attention、Q-Former 等是不同 bridge。","统计不同分辨率/patch size 的 visual token 数和 LLM context 占比；比较 linear projector 与 token resampler。","只做 embedding dimension 对齐不等于语义对齐；通常还需要图文预训练/指令调优与精细数据。","画 vision encoder→projector/resampler→LLM 的 shape，并说明哪些参数可冻结。"),
74:("视频同时有空间与时间冗余，关键是 frame sampling、temporal encoder、token compression 与长上下文预算；均匀抽帧可能漏掉短事件。","用不同 FPS/scene-based sampling/temporal pooling 测事件定位准确率和 token 成本。","把每帧所有 patch token 直接拼接会迅速爆上下文；压缩过强又会丢动作与时序细节。","给 120 秒视频、2 fps、每帧 576 tokens，算原始 token 数并设计压缩到 8k 的方案。"),
75:("Forward diffusion 是固定 Markov 加噪过程；利用 `bar_alpha_t` 可直接从 x0 采样任意 xt，这是训练高效的关键。","实现 q_sample，验证 t 增大时 SNR 降低；画不同 noise schedule 的 SNR 曲线。","β schedule 影响不同时间步难度和采样质量；forward process 本身通常不学习参数。","从逐步高斯转移推导 closed-form `q(x_t|x_0)`。"),
76:("ε-prediction 只是 diffusion 参数化之一，还可预测 x0 或 v；不同参数化在 SNR 区间与稳定性上有不同特性。","同一 batch 由 x0/ε 互相恢复，验证公式；按 t bucket 统计 loss，观察高/低 SNR 难度。","‘预测噪声因为噪声更简单’过于粗糙；关键是重参数化后训练目标和 score matching 的联系。","推导从 ε 预测恢复 x0 的公式，并解释 v-parameterization 的动机。"),
77:("Latent diffusion 将高维像素压到 VAE latent，再做 denoising，大幅减少空间 token；成本是引入 encoder/decoder 失真与 latent scaling。","比较 pixel/latent 的元素数与 U-Net/DiT FLOPs；检查 VAE reconstruction 质量作为上限之一。","latent 过度压缩会丢文字、细节和高频信息；生成质量不只由 diffusion backbone 决定。","给 1024² RGB 与 8× downsample latent，计算空间元素缩减倍数。"),
78:("DiT 把 latent patchify 后用 Transformer blocks 预测噪声/velocity，具有更直接的模型规模扩展路径；U-Net 则天然多尺度卷积结构。","在固定 latent resolution 下计算 patch size 对 token 数和 attention FLOPs 的影响；比较 adaLN conditioning。","DiT 不是简单把 U-Net 换成 Transformer：conditioning、patchify、positional encoding 与 compute scaling 都要重新设计。","画 DiT token flow，并估算 token 数翻倍时 attention 成本变化。"),
79:("BF16 与 FP32 共享 8-bit exponent，动态范围接近；FP16 mantissa 更细但 exponent 更窄，训练时更容易 overflow/underflow。","打印三种 dtype 的 `finfo`，测试大/小数值表示；记录 FP16 loss scaling 前后的 inf/zero。","BF16 不是‘精度更高’，它是范围更大、有效尾数更少；具体硬件吞吐支持也要考虑。","比较 FP16/BF16 的 exponent/mantissa bit，并解释动态范围与相对精度 trade-off。"),
80:("Mixed precision 的关键是把适合低精度的 matmul/conv 放到 Tensor Core，同时对敏感 reduction/optimizer 等保留更高精度。","用 autocast+GradScaler 训练小模型，记录 scaler 动态变化；再用 BF16 说明为何通常不需要同样的 loss scaling。","并非所有 op 都应强制 cast；手工全模型 `.half()` 可能比 autocast 更不稳定。","解释 FP16 loss scaling 为什么在 backward 前乘 scale、step 前再 unscale。"),
81:("Gradient accumulation 只在 optimizer update 频率层面扩大 effective batch；它不等价于一次真正的大 batch 对 BN、dropout、sequence packing 或通信都完全相同。","验证累积 N 次与一次大 batch 在无 BN/固定 dropout 下梯度接近；再加入 BN 观察差异。","loss 是否除以 accumulation steps 要结合 reduction 定义；scheduler 的 step 单位也常配置错误。","给 micro-batch、DP world size、accum steps，计算 global batch 与每 epoch optimizer steps。"),
82:("Checkpointing 省的是需要保存的 activation，用 backward 重算 forward 片段换显存；最优切分取决于 activation 大小和 recompute 成本。","用 `torch.utils.checkpoint` 比较 peak memory 与 step time；分别 checkpoint attention/FFN block。","如果模型本来受 optimizer/parameter memory 主导，checkpoint 收益有限；随机算子还需注意 RNG state。","画出不 checkpoint 与 checkpoint 的 activation 生命周期，说明为什么 compute 增加。"),
83:("DDP 每 rank 有完整参数副本，数据不同；backward 通过 gradient bucket all-reduce 保持更新一致。通信可与反向计算 overlap。","用 2 GPU 打印各 rank 参数 checksum；故意让某 rank 少跑一步观察 collective hang。","DDP 不会自动帮你正确 shard dataset；不同 rank 控制流不一致、unused parameters 也会引发问题。","解释 ring all-reduce 的数据量级，以及 bucket size 对 overlap 的影响。"),
84:("ZeRO-1/2/3 逐级 shard optimizer/gradient/parameter；PyTorch FSDP/FSDP2 采用参数分片+按需 all-gather/reduce-scatter。2026 的 FSDP2 `fully_shard` 基于 DTensor per-parameter sharding。","列 7B Adam 训练的 parameter/grad/moment 内存账本，估算不同 world size 下 shard 后量级。","节省显存不是免费的：更高 stage 增加通信、调度和 checkpoint 复杂度；小模型可能得不偿失。","画一层 FSDP forward：sharded param→all-gather→compute→reshard；backward 再说明 reduce-scatter。"),
85:("DP 沿 batch 维复制模型；TP 切单层张量计算；PP 切 layer stage。实际大模型常做多维 device mesh，并进一步加入 sequence/context/expert parallel。","为一个 64 GPU 集群设计 DP×TP×PP 分解，计算每维 size；分析跨节点带宽让 TP 尽量留在高速互联域。","并行度越多不一定越快：TP collective、PP bubble、DP gradient sync 都有代价。","给模型单卡放不下、节点内 NVLink、节点间 IB 的条件，说明并行维度映射原则。"),
86:("OOM 要先区分常驻内存与峰值、allocated 与 reserved、forward/backward/optimizer/decode 阶段；再对 parameter/grad/optimizer/activation/KV/workspace 建账本。","在训练脚本每阶段 `reset_peak_memory_stats()` + 打点；记录异常 batch 的 sequence length 和 memory snapshot。","`empty_cache()` 不是解决模型实际内存需求的办法；碎片问题与真实容量不足要分开。","为 AdamW BF16 模型估算每参数内存，再加入 activation，判断优先选 checkpoint 还是 FSDP。"),
87:("NaN/Inf 诊断遵循首次污染原则：找第一个非有限 tensor/step，而不是只看最终 loss；同时追踪 logits、loss components、grad norm、optimizer state。","用 hooks/`detect_anomaly` 在最小复现上定位；保存异常 batch、RNG 与 checkpoint 可重放。","`detect_anomaly` 很慢，不适合长期生产训练；gradient clipping 也可能掩盖根因而非修复。","设计二分法：层级 hook 找首次 NaN 层，再缩到具体 op 与输入范围。"),
88:("低 GPU util 先判断 input-bound、CPU/H2D、kernel launch、memory-bound 还是 communication-bound；利用率单一指标不足以说明 GPU 是否高效。","用 Nsight/PyTorch profiler 看 GPU timeline：是否有空洞、Memcpy、NCCL、很多短 kernel；再一次只改一个瓶颈。","nvidia-smi 采样粒度粗，99% util 也可能吞吐差；需要结合 SM occupancy、memory BW、step time。","给出 dataloader 空洞、NCCL 长条、碎 kernel 三种 timeline，分别提出修复方向。"),
89:("量化应区分 weight-only、weight+activation、KV quantization；真正提速取决于 kernel 是否能减少 memory traffic 并高效执行低比特算术。","比较 BF16/INT8/INT4 的 model size、load bandwidth 与 tokens/s；检查 quant/dequant overhead。","理论 0.5 byte/param 不等于实际峰值显存；group scales、workspace、KV、activations 都要计入。","为 70B 估算 BF16 与 4-bit 权重体积，并讨论单机多卡部署的剩余显存。"),
90:("PTQ 在训练后校准/量化，成本低；QAT 在训练时模拟 quantization noise，使模型适应低比特误差。还要区分 static/dynamic、per-tensor/per-channel/group-wise。","选一层线性权重，比较 per-tensor 与 per-channel quantization error；用 calibration data 看 activation range。","校准集不代表真实分布会导致 PTQ 崩坏；QAT 也会增加训练复杂度并不保证所有算子都有部署 kernel。","写出 affine quantization `q=round(x/s)+z` 与反量化公式，说明 clipping 的作用。"),
91:("PagedAttention 借鉴虚拟内存思想，把每条请求逻辑 KV 映射到固定大小 physical blocks，降低动态序列造成的预留浪费与碎片，并支持共享。","模拟不同长度请求的 contiguous reservation 与 paged allocation，比较内部浪费率；观察 block size trade-off。","PagedAttention 主要解决 KV memory management，不等价于 FlashAttention；两者可同时存在。","给一组请求长度和 block size，手算 allocated blocks、waste tokens 与可复用 prefix blocks。"),
92:("Continuous batching 在 token iteration 边界动态加入/移除请求，提高 GPU occupancy；调度目标是在吞吐、TTFT、TPOT 与公平性之间折中。","模拟 static vs continuous scheduler，统计 idle slots、throughput、P99；加入长输出请求看 head-of-line 影响。","吞吐最大化可能恶化单请求 latency；生产系统常需要优先级、max batched tokens、preemption。","画 4 个不同长度请求的时间轴，比较 static batching 与 iteration-level batching。"),
93:("Prefill 处理整段 prompt，矩阵乘并行度高；decode 每步一个新 token、反复读权重与 KV，算术强度低。优化指标分别偏向 TTFT 与 TPOT。","分别扫 prompt length/output length，画 TTFT/TPOT/GPU memory BW；不要只报总 latency。","‘prefill compute-bound、decode memory-bound’是常见近似而非永恒规律，超长 context、很大 batch、不同硬件会改变瓶颈。","用 roofline 思路比较两阶段 arithmetic intensity，并说明 continuous batching 如何改变 decode batch。"),
94:("Speculative decoding 的关键是 draft 提议多个 token、target 并行评分，再按 rejection sampling 规则接受/修正，保证最终分布与 target 一致。","模拟 acceptance rate 不同的 speedup；统计 draft cost、target verification batch 与 accepted tokens/step。","draft 太慢或 acceptance 低会负收益；模型分布不匹配、候选长度过长都降低效率。","解释为什么‘target 直接接受 draft argmax’会改变分布，而正确接受概率不会。"),
95:("线上变慢要先分 TTFT/TPOT/queue/throughput/P99，再按 gateway→scheduler→prefill→decode→network 分层；最后关联流量分布与版本变更。","建立 dashboard：prompt/output token histogram、queue depth、batch tokens、KV occupancy、GPU BW/SM、NCCL、kernel time；做 canary diff。","平均 latency 不变但 P99 飙升通常指向长尾/排队/straggler；加 GPU 可能只是暂时掩盖调度或流量问题。","给‘TTFT 翻倍但 TPOT 不变’与‘TPOT 变差但 queue 不变’两种现象，各列前三根因。"),
96:("模型选择应从业务目标与约束反推：质量 metric、数据量、latency/SLA、成本、可解释/安全、迭代周期，再比较候选模型的 Pareto frontier。","做 model decision record：baseline、候选、假设、offline、latency、cost、风险、最终决策与 rollback。","不能用‘最新 SOTA’作为理由；若收益小于系统复杂度/维护成本，简单模型可能是更优工程解。","给定 P99<50ms、GPU 成本预算、AUC 目标，设计至少三候选并写 reject 原因。"),
97:("Offline→Online gap 常来自 data/label/metric/serving/feedback loop 五层错位：训练分布、泄漏、目标代理、延迟超时、曝光策略都会改变真实效果。","上线前做 replay/shadow/canary，核对 feature parity、score distribution、calibration、latency 与 segment metrics。","AUC 提升并不保证 CTR/GMV 提升；排序位置、探索策略和业务约束会把模型 gain 转化或抵消。","画从日志→训练→离线评估→serving→用户反馈的数据闭环，标出可能 skew 的接口。"),
98:("Ablation 的目标是因果归因：一次改变一个关键因素或使用正交实验，统一预算与随机性，并报告方差/置信区间。","对 Base+A+B+C 建 factorial/逐项增量实验；至少 3 seeds，记录质量、cost、latency。","只展示最终 full model 与 baseline 不能证明每个模块有效；顺序式 ablation 还可能受 interaction 影响。","设计一个 2×2 实验验证两个模块是否有交互项，而不只是各自提升。"),
99:("Train loss↓而 val metric 不涨首先检查 metric/objective 对齐、split/leakage、label noise 与 evaluation bug，再谈正则或模型容量。","固定 checkpoint 做 prediction dump，按 slice 比较 loss、calibration、ranking metric；验证评估代码与 label 时间窗。","训练 loss 与业务 metric 非单调并不罕见，尤其 surrogate loss；不能把所有情况都归为 overfitting。","列出至少 8 个假设，并按‘最便宜验证优先’排序排障。"),
100:("现场实现题真正看的是从公式到 tensor program 的映射、边界条件、复杂度和测试意识；面试官通常比代码风格更在意正确性与解释。","为 Attention/BN/InfoNCE 各准备 reference implementation + 3 个 unit tests + shape assertions + numerical checks。","不要一上来追求极致向量化；先写正确可解释版本，再优化，能主动说出性能瓶颈更加分。","在白板上先写 API contract、shape、公式、边界，再编码；最后手工走一个最小样例。"),
}
assert len(E) == 100

CHAPTER_RUBRIC = {
1:"基础题的 90 分答案要同时包含：最小数学例子、梯度/表达能力解释、一个反例和一个可复现实验。",
2:"优化与归一化题要区分公式层、统计层、训练动态与工程配置；避免把经验规律说成无条件结论。",
3:"CV 题优先量化 shape、参数量、FLOPs、感受野和任务边界；能给 profiler/ablation 会明显加分。",
4:"序列题要把训练信息流、推理信息流和 mask/tokenization 语义分开，不要只背架构名词。",
5:"Transformer 题默认要求公式、shape、复杂度、数值稳定、GPU/serving 影响五层都能展开。",
6:"Post-training 题必须把 data→sampling→objective→optimization→evaluation 闭环讲完整，并主动讨论 reward/data 风险。",
7:"多模态/生成题要同时说明表示接口、token/compute 成本、训练目标和生成/评估失败模式。",
8:"训练系统题先建资源账本，再定位 compute/memory/communication/input；任何优化都要说明交换来的代价。",
9:"推理题至少区分 prefill/decode、TTFT/TPOT/throughput/P99、weight/KV，并能做容量与性能估算。",
10:"项目题重在证据链：问题定义→假设→实验→指标→线上约束→失败复盘；避免只描述‘做了什么’。",
}

# 题目特定验证方法，替换旧的通用占位代码。
VERIFY = {
1:"用 two-moons/XOR 比较纯线性堆叠与带 ReLU 的 MLP；打印最终两层线性合并后的权重并验证输出完全一致。",
2:"对一个 2 层 MLP 使用 `torch.autograd.grad` 与中心有限差分对同一参数做 gradient check，并打印相对误差。",
3:"对极端 logits 比较 `F.cross_entropy` 与手写 `log_softmax + NLL`，再验证 `grad == softmax - one_hot`。",
4:"采样输入网格，画各激活值与导数；在同一深 MLP 上记录 dead-unit ratio 与 grad RMS。",
5:"给 50/100 层网络注册 hooks，逐层记录 activation RMS、gradient RMS 与最大值，比较 residual/初始化/clipping。",
6:"构造 100 层 MLP，分别用 std=0.01、Xavier、Kaiming、std=1.0，画层间方差传播。",
7:"同时画 train/val learning curve、data-size learning curve，并按数据 slice 查看 gap 是否集中在少数分布。",
8:"扫描 smoothing epsilon，报告 accuracy/NLL/ECE/max-logit，而不是只比较 top-1。",
9:"构造 Gaussian regression、binary multi-label、categorical 三个 toy task，对应验证 MSE/BCE/CE。",
10:"在 1:1000 数据上比较 Accuracy、ROC-AUC、PR-AUC、F1 与固定 Recall 下 Precision，并做 threshold sweep。",
}

# 其余题使用按章节定制的实验模板，仍然会带入该题的专项练习，不再使用空洞占位符。
VERIFY_BY_CHAPTER = {
2:"固定 seed 与数据顺序，记录 loss、update/weight ratio、grad norm、参数范数；一次只改一个 optimizer/normalization/schedule 条件。",
3:"写 shape/参数/FLOPs 计算器并与 PyTorch module 对拍；必要时加 profiler 验证理论计算量是否转化为实际延迟。",
4:"构造最短可解释序列任务，显式打印 token、mask、hidden/label shape，并分别观察 teacher-forced 与 free-running 行为。",
5:"从 `[B,T,D]` 开始逐步断言 Q/K/V、score、mask、output shape；与 PyTorch SDPA/reference 实现对拍并扫序列长度。",
6:"把 data version、token count、LR、grad norm、reward/KL、length distribution 和 held-out eval 一起记录，确保实验可复现。",
7:"对输入分辨率/帧数/token 数/时间步做参数扫描，同时报告质量与 compute/memory，避免只测单个点。",
8:"在 forward/backward/optimizer/collective 各阶段打时间与内存点；使用 profiler 将瓶颈归类到 compute/memory/communication/input。",
9:"做小型 serving 压测，分别扫描 prompt length、output length、concurrency、KV heads，记录 TTFT/TPOT/throughput/P99 与显存。",
10:"建立实验表：hypothesis、baseline、change、offline metric、latency/cost、slice、结论；所有结论都能追溯到具体证据。",
}


PROJECT_EVIDENCE = {
1:("训练/验证 loss、generalization gap、activation/gradient 分布、seed 方差","先证明数学机制，再通过 toy experiment 排除数据与 optimizer 混杂。"),
2:("loss、grad norm、update/weight ratio、参数范数、ECE/稳定性、step time","用 controlled ablation 比较优化或归一化方案，统一训练预算与 data order。"),
3:("mAP/IoU/Top-1、参数量、MACs/FLOPs、peak memory、latency、分辨率敏感性","CV 方案要同时回答精度与计算预算，理论 FLOPs 必须用 profiler 验证。"),
4:("token-level loss、sequence metric、长度分布、mask 正确率、free-running error、tokens/s","显式区分 training context 与 inference context，并做 token/mask 可视化审计。"),
5:("attention entropy、tokens/s、peak memory、TTFT/TPOT、KV bytes、kernel/backend","Transformer 优化必须说明是改数学连接、改 IO、改 KV，还是改 scheduler，避免概念混淆。"),
6:("tokens、loss、grad norm、reward、KL、entropy、length、pass@k/held-out、regression slices","Post-training 的结果必须可追溯到 data/reward/policy/eval 版本，平均 reward 不能作为单一上线依据。"),
7:("retrieval/zero-shot/生成质量、token 数、分辨率/帧数、FLOPs、VRAM、采样步数","多模态与生成模型要把质量曲线与 token/step/分辨率成本放在同一张表里。"),
8:("allocated/reserved/peak memory、step time、GPU util、SM/BW、NCCL time、dataloader wait","系统题用 timeline 和资源账本说话；所有优化都要注明换来的 compute/communication/复杂度。"),
9:("TTFT、TPOT、throughput、P50/P95/P99、queue time、KV occupancy、GPU BW、cost/request","推理方案用负载分布压测，不用单请求 demo；必须报告 warmup、并发和输入/输出 token 分布。"),
10:("业务主指标、guardrail、slice、latency/cost、统计显著性、线上增量、回滚条件","项目题每个结论都应对应一个实验或线上证据，并明确未被证实的假设。"),
}

FIVE_MIN = {
1:"先写最小公式/反例 → 解释梯度或表达能力 → 给 toy experiment → 说现实网络中的边界 → 连接到相邻题。",
2:"先写更新/统计公式 → 解释动态量 → 给可观测指标 → 比较替代方案 → 说明超参数与失败边界。",
3:"先做 shape/参数/FLOPs → 解释 inductive bias → 对比替代模块 → 给任务级指标 → 说硬件实测。",
4:"先画 token/状态信息流 → 写 mask/目标 → 区分训练与推理 → 分析序列误差 → 给实现测试。",
5:"先画 `[B,T,D]` 数据流 → 写 attention/FFN 公式 → 算复杂度/显存 → 讲数值与 kernel → 讲 serving。",
6:"先讲数据来源 → 写 objective → 讲 sampling/update → 讲 reward/KL/稳定性 → 讲 held-out 与 release gate。",
7:"先画模态/latent 接口 → 算 token/step 成本 → 讲训练目标 → 讲质量失败模式 → 给压缩/采样 trade-off。",
8:"先建资源账本 → 定位阶段 → 看 profiler/timeline → 选择优化 → 量化收益和副作用 → 验证可恢复性。",
9:"先拆 TTFT/TPOT/queue → 区分 prefill/decode → 建权重/KV 账本 → 看 scheduler/kernel → 做容量规划。",
10:"先定义业务问题 → 写 baseline/hypothesis → 设计对照 → 给指标与统计 → 解释线上约束 → 复盘失败。",
}


def qnum_from(path: Path) -> int:
    m = re.search(r"Q(\d{3})", path.name)
    if not m:
        raise ValueError(path)
    return int(m.group(1))


def chapter_from(text: str) -> int:
    m = re.search(r'^chapter:\s*(\d+)', text, flags=re.M)
    if not m:
        raise ValueError("missing chapter")
    return int(m.group(1))


def replace_placeholder(text: str, q: int, chapter: int) -> str:
    heading = "## 工程实现 / PyTorch 验证"
    if heading not in text:
        return text
    start = text.index(heading) + len(heading)
    m = re.search(r"\n## ", text[start:])
    if not m:
        return text
    end = start + m.start()
    body = text[start:end]
    protocol = VERIFY.get(q, E[q][1])

    protocol_block = f"### 推荐验证协议\n\n{protocol}\n\n**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。"

    # 清理旧的通用占位 block。
    if "建议的最小验证套路" in body:
        body = "\n\n" + protocol_block + "\n"
    elif "### 推荐验证协议" in body:
        # 保留前面的题目特定代码，只替换验证协议段，确保二次执行可更新。
        body = re.sub(
            r"\n*### 推荐验证协议\n.*?(?=\n### |\Z)",
            "\n\n" + protocol_block + "\n",
            body,
            flags=re.S,
        )
    else:
        body = body.rstrip() + "\n\n" + protocol_block + "\n"
    return text[:start] + body + text[end:]


def build_deep_section(q: int, chapter: int) -> str:
    quant, eng, edge, drill = E[q]
    return f'''## 90 分深挖：从会背到能做设计

### 机制与定量抓手

{quant}

### 工程与实验抓手

{eng}

### 失败边界 / 反例

{edge}

### 白板专项练习

{drill}

> **本章 90 分标准：** {CHAPTER_RUBRIC[chapter]}

## 面试官评分拆解

| 档位 | 典型表现 |
|---|---|
| 40–50 分 | 只会给定义或背结论，缺公式/机制，追问一层就断。 |
| 60–70 分 | 能解释主机制并写关键公式，但缺边界条件和工程证据。 |
| 80–90 分 | 能定量推导、比较替代方案，主动说明失败场景并给验证方法。 |
| 90+ 分 | 能把数学、实现、系统成本和项目决策串成完整证据链，并能反向设计实验验证假设。 |

### 面试表达建议

建议用 **结论 → 机制 → 定量 → trade-off → 边界 → 验证** 六步法回答。先在 60–90 秒内给主线；只有面试官继续追问时再展开公式、代码或系统细节。这样既显示深度，也避免一上来堆知识点失去重点。

## 项目化证据链：如何证明你真的做过

只讲原理只能证明“学过”，项目面试还要证明“做过、量过、复盘过”。针对本题，建议准备一张实验卡：**问题/假设 → baseline → 改动 → 指标 → 结果 → 失败 slice → 结论**。

### 建议报告的指标

- **核心观测：** {PROJECT_EVIDENCE[chapter][0]}。
- **证据原则：** {PROJECT_EVIDENCE[chapter][1]}
- **本题特定证据：** {E[q][1]}

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**{E[q][2]}**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

{FIVE_MIN[chapter]}

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。
'''


def enhance_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    q = qnum_from(path)
    chapter = chapter_from(text)

    # idempotent: replace existing v2 section if present.
    text = re.sub(
        r"\n## 90 分深挖：从会背到能做设计\n.*?(?=\n## 自测清单)",
        "\n",
        text,
        flags=re.S,
    )
    text = replace_placeholder(text, q, chapter)
    marker = "\n## 自测清单"
    if marker not in text:
        raise RuntimeError(f"missing marker: {path}")
    text = text.replace(marker, "\n" + build_deep_section(q, chapter) + marker, 1)

    # 更新审阅日期/版本元数据
    if 'content_level:' not in text.split('---', 2)[1]:
        text = text.replace('last_reviewed: "2026-09-01"', 'last_reviewed: "2026-09-01"\ncontent_level: "v2-deep"', 1)
    else:
        text = re.sub(r'content_level:.*', 'content_level: "v2-deep"', text, count=1)

    path.write_text(text, encoding="utf-8")


def main() -> None:
    files = sorted(QDIR.rglob("Q*.md"))
    assert len(files) == 100, len(files)
    for p in files:
        enhance_file(p)
    print(f"enhanced {len(files)} question files")


if __name__ == "__main__":
    main()
