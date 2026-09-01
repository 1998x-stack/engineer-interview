# 第 3 章 · 表示学习与序列模型

> **章节目标**：理解从共现统计到上下文化表示、从递归依赖到 Attention 的演进逻辑。

## 1. 先修知识

矩阵乘法、概率语言模型、基础反向传播。

## 2. 本章知识路线

Q025–Q030 词表示 → Q031–Q034 序列依赖与 Attention。

## 3. 必须白板掌握

- Skip-Gram/CBOW
- Negative Sampling
- SGNS≈shifted PMI
- RNN Jacobian 连乘
- LSTM cell path
- Seq2Seq Attention

## 4. 高频失分模式

- 只背模型时间线
- 不会把 embedding 与共现统计连接
- 只说“RNN 梯度消失”不写 Jacobian
- 把 Attention 只解释为权重可视化

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q025 | [CBOW 与 Skip‑Gram：输入输出正好相反吗？](Q025-cbow-vs-skipgram.md) | ★★ | ★★★★ |
| Q026 | [Word2Vec 为什么需要 Negative Sampling？](Q026-negative-sampling.md) | ★★★ | ★★★★★ |
| Q027 | [Hierarchical Softmax 为什么是 O(log|V|)？](Q027-hierarchical-softmax.md) | ★★★ | ★★★ |
| Q028 | [SGNS 为什么与 PMI Matrix Factorization 有关系？](Q028-sgns-pmi.md) | ★★★★ | ★★★ |
| Q029 | [GloVe 与 Word2Vec 的差异](Q029-glove-vs-word2vec.md) | ★★ | ★★★ |
| Q030 | [静态词向量为什么解决不了一词多义？](Q030-contextual-embeddings.md) | ★★ | ★★★★ |
| Q031 | [RNN 为什么梯度消失/爆炸？](Q031-rnn-gradient.md) | ★★★ | ★★★★★ |
| Q032 | [LSTM 为什么缓解长依赖问题？](Q032-lstm-long-dependency.md) | ★★★ | ★★★★ |
| Q033 | [GRU 与 LSTM 怎么选？](Q033-gru-vs-lstm.md) | ★★ | ★★★ |
| Q034 | [Seq2Seq 为什么需要 Attention？](Q034-seq2seq-attention.md) | ★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
