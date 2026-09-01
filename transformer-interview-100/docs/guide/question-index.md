# Transformer 面试 100 题索引

> 每个问题一个 Markdown。建议先按章节刷，再用随机抽题进行二次复习。

## 第 1 章 · Transformer 总体架构与设计动机

从 RNN 的结构瓶颈出发，建立 Encoder、Decoder、Residual Stream、Tensor Shape 与信息流的统一视角。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q001](../questions/chapter-01/Q001.md) | 为什么 Transformer 能取代 RNN/LSTM？ | 2/5 |
| [Q002](../questions/chapter-01/Q002.md) | 请完整描述一个 Transformer Encoder Layer | 2/5 |
| [Q003](../questions/chapter-01/Q003.md) | 请完整描述 Transformer Decoder | 2/5 |
| [Q004](../questions/chapter-01/Q004.md) | Residual Connection 到底解决什么问题？ | 3/5 |
| [Q005](../questions/chapter-01/Q005.md) | 为什么 Transformer 更常用 LayerNorm 而不是 BatchNorm？ | 2/5 |
| [Q006](../questions/chapter-01/Q006.md) | 手写 Transformer 时最重要的 Tensor Shape 链是什么？ | 2/5 |
| [Q007](../questions/chapter-01/Q007.md) | 标准 Multi-Head Attention 参数量如何估算？ | 2/5 |
| [Q008](../questions/chapter-01/Q008.md) | Self-Attention 与 Cross-Attention 的本质区别是什么？ | 2/5 |
| [Q009](../questions/chapter-01/Q009.md) | Attention 与 FFN 分别承担什么功能？ | 2/5 |
| [Q010](../questions/chapter-01/Q010.md) | 如果完全删除 Position Encoding，会发生什么？ | 3/5 |

## 第 2 章 · Attention 数学与实现细节

从点积方差、Softmax 数值稳定性、Mask、Multi-Head 到复杂度，要求能手推、能编码、能解释边界。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q011](../questions/chapter-02/Q011.md) | 写出 Scaled Dot-Product Attention，并逐项解释 | 2/5 |
| [Q012](../questions/chapter-02/Q012.md) | 为什么必须除以 √d_k？ | 3/5 |
| [Q013](../questions/chapter-02/Q013.md) | 为什么 Mask 要加在 Softmax 之前？ | 2/5 |
| [Q014](../questions/chapter-02/Q014.md) | Softmax 如何避免数值溢出？ | 2/5 |
| [Q015](../questions/chapter-02/Q015.md) | 为什么需要 Multi-Head Attention？ | 3/5 |
| [Q016](../questions/chapter-02/Q016.md) | 为什么通常设置 d_head=d_model/H？ | 2/5 |
| [Q017](../questions/chapter-02/Q017.md) | Q、K、V 为什么使用不同投影？ | 3/5 |
| [Q018](../questions/chapter-02/Q018.md) | 为什么使用 Dot-Product Attention，而不是任意 MLP 相似度？ | 3/5 |
| [Q019](../questions/chapter-02/Q019.md) | Self-Attention 的时间复杂度到底是多少？ | 3/5 |
| [Q020](../questions/chapter-02/Q020.md) | Causal Mask 的矩阵结构是什么？ | 2/5 |
| [Q021](../questions/chapter-02/Q021.md) | Padding Mask 与 Causal Mask 如何组合？ | 3/5 |
| [Q022](../questions/chapter-02/Q022.md) | Attention Dropout 通常加在哪里？ | 2/5 |
| [Q023](../questions/chapter-02/Q023.md) | Attention Weight 能否直接作为模型解释？ | 3/5 |
| [Q024](../questions/chapter-02/Q024.md) | 为什么 Linear Attention 不能简单替代 Softmax Attention？ | 4/5 |
| [Q025](../questions/chapter-02/Q025.md) | 写出经典 Sinusoidal Position Encoding | 2/5 |

## 第 3 章 · 位置编码与 RoPE

从 permutation equivariance 出发，推导 Absolute/Relative Position、RoPE、ALiBi 与长上下文外推。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q026](../questions/chapter-03/Q026.md) | 为什么原始 Transformer 使用固定 Sin/Cos？ | 2/5 |
| [Q027](../questions/chapter-03/Q027.md) | Learned Position Embedding 有什么限制？ | 2/5 |
| [Q028](../questions/chapter-03/Q028.md) | Absolute Position 与 Relative Position 的区别是什么？ | 3/5 |
| [Q029](../questions/chapter-03/Q029.md) | RoPE 的核心数学是什么？ | 4/5 |
| [Q030](../questions/chapter-03/Q030.md) | 为什么 RoPE 通常作用在 Q/K 而不是 V？ | 3/5 |
| [Q031](../questions/chapter-03/Q031.md) | RoPE 为什么会遇到长上下文外推问题？ | 4/5 |
| [Q032](../questions/chapter-03/Q032.md) | ALiBi 与 RoPE 的思想有什么区别？ | 3/5 |
| [Q033](../questions/chapter-03/Q033.md) | Position Interpolation 的基本思想是什么？ | 3/5 |
| [Q034](../questions/chapter-03/Q034.md) | 技术上支持 64K 与真正有效 64K 有什么区别？ | 4/5 |
| [Q035](../questions/chapter-03/Q035.md) | Pre-LN 与 Post-LN 有什么区别？ | 3/5 |

## 第 4 章 · Norm、Residual 与 FFN

理解深层 Transformer 为什么能训练，以及 RMSNorm、SwiGLU、初始化等现代模块为什么出现。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q036](../questions/chapter-04/Q036.md) | 为什么现代 LLM 普遍偏向 Pre-Norm？ | 4/5 |
| [Q037](../questions/chapter-04/Q037.md) | LayerNorm 到底沿哪个维度计算？ | 2/5 |
| [Q038](../questions/chapter-04/Q038.md) | RMSNorm 与 LayerNorm 有什么区别？ | 3/5 |
| [Q039](../questions/chapter-04/Q039.md) | FFN 为什么不可缺少？ | 2/5 |
| [Q040](../questions/chapter-04/Q040.md) | 为什么经典 Transformer 常用 d_ff≈4d_model？ | 3/5 |
| [Q041](../questions/chapter-04/Q041.md) | GELU 为什么比 ReLU 常见？ | 2/5 |
| [Q042](../questions/chapter-04/Q042.md) | SwiGLU 是什么，为什么现代 LLM 常用？ | 3/5 |
| [Q043](../questions/chapter-04/Q043.md) | 为什么深层 Transformer 对初始化特别敏感？ | 4/5 |
| [Q044](../questions/chapter-04/Q044.md) | 为什么 Input Embedding 与 LM Head 经常 Weight Tying？ | 3/5 |

## 第 5 章 · BERT、GPT 与 Encoder-Decoder

比较三类架构、预训练目标、Teacher Forcing 与 Exposure Bias，建立任务与架构选择框架。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q045](../questions/chapter-05/Q045.md) | Encoder-only、Decoder-only、Encoder-Decoder 的本质区别？ | 2/5 |
| [Q046](../questions/chapter-05/Q046.md) | BERT 为什么可以双向？ | 2/5 |
| [Q047](../questions/chapter-05/Q047.md) | BERT 为什么用 MLM，而 GPT 用 CLM？ | 3/5 |
| [Q048](../questions/chapter-05/Q048.md) | BERT 的 NSP 是什么，为什么后来常被移除？ | 3/5 |
| [Q049](../questions/chapter-05/Q049.md) | GPT 的 Causal LM 训练目标是什么？ | 2/5 |
| [Q050](../questions/chapter-05/Q050.md) | 为什么自回归模型训练时还能并行？ | 2/5 |
| [Q051](../questions/chapter-05/Q051.md) | 为什么 Decoder-only 成为通用 LLM 主流之一？ | 3/5 |
| [Q052](../questions/chapter-05/Q052.md) | Cross-Attention 为什么适合机器翻译？ | 3/5 |
| [Q053](../questions/chapter-05/Q053.md) | Teacher Forcing 是什么？ | 3/5 |
| [Q054](../questions/chapter-05/Q054.md) | Exposure Bias 是什么？ | 3/5 |

## 第 6 章 · 训练、优化与分布式

从 label shift、loss mask、NaN Debug 到 AdamW、BF16、Scaling Law 和多 GPU 并行。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q055](../questions/chapter-06/Q055.md) | Decoder LM 的 label 为什么必须 shift？ | 2/5 |
| [Q056](../questions/chapter-06/Q056.md) | Padding token 为什么不能参与 loss？ | 3/5 |
| [Q057](../questions/chapter-06/Q057.md) | Transformer loss 变成 NaN，如何系统排查？ | 4/5 |
| [Q058](../questions/chapter-06/Q058.md) | 为什么训练早期常用 Learning Rate Warmup？ | 3/5 |
| [Q059](../questions/chapter-06/Q059.md) | Adam 与 AdamW 的核心区别？ | 3/5 |
| [Q060](../questions/chapter-06/Q060.md) | Gradient Clipping 为什么有用？ | 3/5 |
| [Q061](../questions/chapter-06/Q061.md) | Gradient Accumulation 是否完全等价于大 Batch？ | 4/5 |
| [Q062](../questions/chapter-06/Q062.md) | FP16 与 BF16 为什么训练表现不同？ | 3/5 |
| [Q063](../questions/chapter-06/Q063.md) | 训练正常但验证每次结果不同，先查什么？ | 2/5 |
| [Q064](../questions/chapter-06/Q064.md) | Transformer 初始化不合理有哪些症状？ | 4/5 |
| [Q065](../questions/chapter-06/Q065.md) | 固定训练 FLOPs，模型更大还是 token 更多？ | 4/5 |
| [Q066](../questions/chapter-06/Q066.md) | Transformer 多 GPU 有哪些并行方式？ | 4/5 |
| [Q067](../questions/chapter-06/Q067.md) | Decoder-only LLM 的生成过程是什么？ | 2/5 |

## 第 7 章 · 自回归推理与 KV Cache

从增量解码推导 KV Cache、MQA/GQA、sampling、TTFT/TPOT、PagedAttention 与 FlashAttention。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q068](../questions/chapter-07/Q068.md) | KV Cache 缓存了什么，为什么不缓存 Q？ | 3/5 |
| [Q069](../questions/chapter-07/Q069.md) | KV Cache 内存如何估算？ | 4/5 |
| [Q070](../questions/chapter-07/Q070.md) | 为什么训练不需要像 decode 一样使用 KV Cache？ | 3/5 |
| [Q071](../questions/chapter-07/Q071.md) | Prefill 与 Decode 的瓶颈有什么不同？ | 4/5 |
| [Q072](../questions/chapter-07/Q072.md) | MHA、MQA、GQA 的区别？ | 3/5 |
| [Q073](../questions/chapter-07/Q073.md) | Greedy、Beam Search 与 Sampling 如何选择？ | 3/5 |
| [Q074](../questions/chapter-07/Q074.md) | Temperature、Top-k、Top-p 分别做什么？ | 2/5 |
| [Q075](../questions/chapter-07/Q075.md) | 为什么模型会陷入重复生成？ | 3/5 |
| [Q076](../questions/chapter-07/Q076.md) | LLM Serving 的关键 latency 指标有哪些？ | 3/5 |
| [Q077](../questions/chapter-07/Q077.md) | Continuous Batching 为什么适合 LLM？ | 4/5 |
| [Q078](../questions/chapter-07/Q078.md) | PagedAttention 解决什么问题？ | 4/5 |
| [Q079](../questions/chapter-07/Q079.md) | Speculative Decoding 为什么能加速且保持目标分布？ | 4/5 |
| [Q080](../questions/chapter-07/Q080.md) | FlashAttention 到底优化了什么？ | 3/5 |

## 第 8 章 · 长上下文、高性能 Attention 与 MoE

理解 FlashAttention 的 IO 本质、Online Softmax、Sparse/Linear Attention、MoE、量化与长上下文瓶颈。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q081](../questions/chapter-08/Q081.md) | FlashAttention 为什么不需要存完整 Attention Matrix？ | 4/5 |
| [Q082](../questions/chapter-08/Q082.md) | Online Softmax 如何分块仍保持精确？ | 5/5 |
| [Q083](../questions/chapter-08/Q083.md) | Sparse Attention 如何降低复杂度？ | 4/5 |
| [Q084](../questions/chapter-08/Q084.md) | Linear Attention 与 FlashAttention 最大区别？ | 3/5 |
| [Q085](../questions/chapter-08/Q085.md) | 长上下文 Transformer 至少有哪些瓶颈？ | 4/5 |
| [Q086](../questions/chapter-08/Q086.md) | Sliding Window Attention 的优势与损失？ | 3/5 |
| [Q087](../questions/chapter-08/Q087.md) | MoE 为什么能在相近每-token FLOPs 下增加参数量？ | 3/5 |
| [Q088](../questions/chapter-08/Q088.md) | MoE 最大训练难点是什么？ | 4/5 |
| [Q089](../questions/chapter-08/Q089.md) | Quantization 为什么对 Transformer 推理重要？ | 4/5 |
| [Q090](../questions/chapter-08/Q090.md) | Coding：从零实现 Multi-Head Attention | 3/5 |

## 第 9 章 · Coding / Debug / System Design

把公式转成正确代码，并通过不变量、行为测试、tiny overfit 与系统指标验证实现。

| 题号 | 题目 | 难度 |
|---|---|---|
| [Q091](../questions/chapter-09/Q091.md) | Coding：下面的 Attention 有哪些 bug？ | 3/5 |
| [Q092](../questions/chapter-09/Q092.md) | Coding：给 Transformer 加 KV Cache | 4/5 |
| [Q093](../questions/chapter-09/Q093.md) | 给你几百行 Transformer 代码，如何系统 Debug？ | 4/5 |
| [Q094](../questions/chapter-09/Q094.md) | Coding：如何验证 causal mask 没有未来泄漏？ | 3/5 |
| [Q095](../questions/chapter-09/Q095.md) | Coding：如何验证 KV Cache 实现正确？ | 4/5 |
| [Q096](../questions/chapter-09/Q096.md) | Coding：为什么 transpose 后 view 经常报错或 silently 出问题？ | 3/5 |
| [Q097](../questions/chapter-09/Q097.md) | Coding：如何处理全 Mask 行导致的 NaN？ | 4/5 |
| [Q098](../questions/chapter-09/Q098.md) | Coding：如何做 Tiny Overfit Test？ | 3/5 |
| [Q099](../questions/chapter-09/Q099.md) | Coding：如何为 Attention 写 Shape Assertions？ | 3/5 |
| [Q100](../questions/chapter-09/Q100.md) | System Design：用 Transformer 设计文本分类系统 | 3/5 |
