---
id: Q078
title: "Dense Retrieval 的负样本怎么构造？"
chapter: "检索、搜索与 RAG"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - retrieval-rag
  - retrieval
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q078 Dense Retrieval 的负样本怎么构造？

[← Q077](Q077-multi-stage-retrieval.md) | **第 7 章 · 检索、搜索与 RAG** | [Q079 →](Q079-hnsw.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`retrieval-rag`, `retrieval`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q078.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

随机负样本、in-batch negative、hard negative 各有什么优缺点？

## 2. 面试官到底在考什么

检索训练核心题。

### 评分维度

- 把 recall、precision、latency 分阶段分析。
- 能从 index/negative sampling/rerank 解释系统设计。
- 评价必须端到端可诊断。

## 3. 30-60 秒标准回答

随机负样本多但太容易；in-batch 利用同批其他文档提高效率；hard negative 语义/词面接近但 不相关，学习信号强。难点是 false negative：看似负例其实也能回答。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：DPR 类方法常从 BM25 挖 hard negative。
- **PDF 基线要点**：更强 retriever 挖出的 negatives 更难，但可能形成自举偏差。
- **PDF 基线要点**：可用 teacher reranker/标签做 denoise。
- **扩展理解**：随机负例太容易；in-batch 提高效率；hard negative 提供更有信息的决策边界。
- **扩展理解**：最危险的是 false negative：语义上其实相关却被当负例。
- **扩展理解**：可用 cross-encoder/judge 过滤 hard negatives，并监控负例难度分布。

## 6. 专业深挖：原理、边界与工程

### Dense Retrieval 的性能高度依赖负样本
- Random Negative 往往太容易，只教模型分开明显无关文档；In-batch Negative 低成本扩大负例数量；Hard Negative 则逼模型学习细粒度决策边界。
- 经典对比学习 loss 将正确文档与 batch/队列中的负文档竞争；温度决定 softmax 分布尖锐度和梯度集中程度。
- BM25/旧 retriever 挖出的“词面很像但答案错”的文档是常见 hard negative 来源。
### 边界与工程
- 最危险的是 false negative：语料中另一个真正相关文档被当负例，会向模型注入矛盾梯度。
- Hard-negative mining 要周期刷新；模型学会旧负例后其训练价值会下降。
- 多正例任务应支持 multiple positives/soft labels，而不是强行只认一个 gold doc。

## 7. 实现、复杂度与工程验证

- 拆成 recall→rerank→generation，各层用不同指标和延迟预算。
- 检索系统必须同时考虑 index freshness、长尾实体、ANN recall 与线上 latency。
- 任何更强 reranker 都要回答每个 query 需要多少次模型前向。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 把所有非正例都当真负例。

## 9. 追问树

1. 多正例 query 如何训练？
2. temperature 对 contrastive loss 有何作用？

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

## 10. 面试现场自检

- [ ] 30-60 秒能给出结论，不绕弯。
- [ ] 能写出关键公式、shape 或状态转移。
- [ ] 至少能解释一个 Why 和一个 trade-off。
- [ ] 能举出一个失败模式或反例。
- [ ] 能回答两层追问。
- [ ] 能把答案连接到真实训练/检索/服务系统。

## 11. 参考资料

- [DPR](https://arxiv.org/abs/2004.04906)
- [Sentence-BERT](https://arxiv.org/abs/1908.10084)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q077 为什么搜索系统通常是多阶段 Retrieval→Rerank？](Q077-multi-stage-retrieval.md)
- [Q079 HNSW：为什么多层小世界图能快速 ANN？](Q079-hnsw.md)
- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](Q075-sparse-vs-dense-retrieval.md)
- [Q084 如何完整评估一个 RAG 系统？](Q084-rag-evaluation.md)

## 13. 一句话收束

> **Dense Retrieval 的性能高度依赖负样本**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
