---
id: Q017
title: "中文分词：传统方法与 LLM 时代如何看？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★"
frequency: "★★★"
tags:
  - classical-nlp
  - llm
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q017 中文分词：传统方法与 LLM 时代如何看？

[← Q016](Q016-crf-emission-transition.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q018 →](Q018-ner-evolution.md)

> **难度**：★★  ·  **频率**：★★★  ·  **标签**：`classical-nlp`, `llm`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q017.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

中文分词有哪些经典方法？为什么它与 BPE/SentencePiece 的 tokenization 不是同一个问 题？

## 2. 面试官到底在考什么

区分 NLP task segmentation 与 tokenizer segmentation。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

中文分词任务目标是恢复“词”边界，可用词典、HMM、CRF、BiLSTM-CRF、BERT 标注；LLM tokenizer 的 subword 切分主要服务模型计算与词表压缩，不保证语言学意义上的词。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：最大匹配依赖词典，简单但歧义处理弱。
- **PDF 基线要点**：序列标注可用 B/M/E/S 或 BIO 标签。
- **PDF 基线要点**：下游任务未必需要显式中文分词，端到端 subword 模型常直接学习。
- **扩展理解**：中文 word segmentation 与 tokenizer segmentation 是两个概念：前者是语言学任务，后者是模型输入编码。
- **扩展理解**：LLM 时代仍可能需要显式分词，例如搜索索引、词典特征、可解释标注。
- **扩展理解**：评估通常用 boundary/span F1，而不是只看 token accuracy。

## 6. 专业深挖：原理、边界与工程

### “中文分词”与“Tokenizer”不是一回事
- 中文分词是语言学/任务层的词边界预测；BPE/WordPiece/SentencePiece 是模型输入单位的构造，两者目标完全不同。
- 传统 CWS 可用 B/M/E/S 序列标签建模，从 HMM/CRF 到 BiLSTM/BERT-CRF；现代 LLM 不一定需要显式词边界才能建模中文。
- 但搜索、词法分析、实体对齐等系统仍可能需要可解释词粒度，因此分词没有因为 LLM 出现而“消失”。
### 边界与工程
- 不同标注规范对专名、数字、组合词的切分并不唯一；必须先明确 gold standard。
- 搜索系统常使用词、字、字符 n-gram 多粒度索引，降低单一分词错误对 recall 的不可逆影响。
- 评估除了总体 F1，还要看 OOV recall、领域新词和歧义句 slice。

## 7. 实现、复杂度与工程验证

- 给出状态/标签空间、独立性假设和训练/解码复杂度。
- 区分局部 score、全局归一化与解码约束。
- 真实 NLP 数据要考虑 OOV、标注规范、领域词典和 span 对齐。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 把“Tokenizer”与“中文分词”混为一谈。
- 只列工具名。

## 9. 追问树

1. 新词发现怎么做？
2. 分词错误会如何传播到检索/NER？

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

- [CRF](https://repository.upenn.edu/cis_papers/159/)
- [BM25 overview (Stanford IR book)](https://nlp.stanford.edu/IR-book/html/htmledition/okapi-bm25-a-non-binary-model-1.html)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q016 CRF 的 Emission 与 Transition Matrix 分别表示什么？](Q016-crf-emission-transition.md)
- [Q018 NER 模型为什么从 HMM 演化到 BERT/LLM？](Q018-ner-evolution.md)
- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **“中文分词”与“Tokenizer”不是一回事**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
