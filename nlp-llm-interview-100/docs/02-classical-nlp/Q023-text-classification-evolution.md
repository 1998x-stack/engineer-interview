---
id: Q023
title: "文本分类方案如何随数据规模演进？"
chapter: "统计 NLP 与传统 NLP"
difficulty: "★★"
frequency: "★★★★"
tags:
  - classical-nlp
  - data
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q023 文本分类方案如何随数据规模演进？

[← Q022](Q022-edit-distance.md) | **第 2 章 · 统计 NLP 与传统 NLP** | [Q024 →](Q024-nlp-data-augmentation.md)

> **难度**：★★  ·  **频率**：★★★★  ·  **标签**：`classical-nlp`, `data`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q023.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

从小数据、低延迟到大数据/LLM，文本分类可有哪些方案？

## 2. 面试官到底在考什么

考察模型选择而不是背模型列表。

### 评分维度

- 先说模型建模对象与条件独立假设。
- 能写出动态规划/打分函数并解释复杂度。
- 能和神经网络/LLM 时代方案比较适用边界。

## 3. 30-60 秒标准回答

从 TF-IDF+LR/SVM、TextCNN/RNN、BERT classifier，到 zero/few-shot LLM 与 SFT。方案 选择受数据量、标签稳定性、延迟、成本、可解释性影响。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：小数据高维稀疏场景，线性模型常是强 baseline。
- **PDF 基线要点**：BERT 类 encoder 在固定标签空间通常比生成式 LLM 更经济。
- **PDF 基线要点**：标签频繁变化或任务开放时，instruction LLM 灵活性更强。
- **扩展理解**：方案选择应由数据规模、标签成本、延迟、类别变化速度和可解释性驱动。
- **扩展理解**：TF-IDF+LR/SVM 在小数据/低延迟时仍是强基线，BERT/LLM 并非总是最优。
- **扩展理解**：要能说明 encoder fine-tuning、prompting 与 distillation 的成本边界。

## 6. 专业深挖：原理、边界与工程

### 文本分类选型不是“追最新模型”
- 小数据、关键词信号强时 TF-IDF + LR/SVM 是极强 baseline；中等数据可用 CNN/RNN；BERT 类 encoder 在预训练迁移后通常提供更高样本效率。
- LLM zero/few-shot 的优势是标签开放和快速冷启动，代价是推理成本、延迟、格式稳定性和概率校准。
- 一个成熟工业方案常让 LLM 负责 teacher/数据生成，再蒸馏到小型 classifier，实现能力与成本折中。
### 边界与工程
- 长文本直接截断可能丢关键证据，需 chunk aggregation、hierarchical encoder、retrieval-then-classify 或长上下文模型。
- 标签频繁新增时固定 Softmax head 维护成本高，embedding/LLM 方案更灵活。
- 永远先做 lexical/keyword baseline：它既是性能基线，也能暴露数据泄漏和 shortcut。

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

- 一上来就用最大模型。
- 不先做 baseline 和错误分析。

## 9. 追问树

1. 多标签分类怎么做？
2. 层级标签如何建模？

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

- [Q022 编辑距离：动态规划怎么写？如何降空间？](Q022-edit-distance.md)
- [Q024 NLP 数据增强：怎么保证不破坏标签？](Q024-nlp-data-augmentation.md)
- [Q015 BERT 后为什么还要接 CRF？](Q015-bert-crf.md)
- [Q021 BM25 相比 TF‑IDF 改进了什么？](Q021-bm25.md)

## 13. 一句话收束

> **文本分类选型不是“追最新模型”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
