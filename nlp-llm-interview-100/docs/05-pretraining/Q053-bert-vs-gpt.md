---
id: Q053
title: "BERT 与 GPT：双向理解和因果生成如何取舍？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★"
frequency: "★★★★★"
tags:
  - pretraining
  - bert
  - gpt
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q053 BERT 与 GPT：双向理解和因果生成如何取舍？

[← Q052](Q052-bert-vs-autoregressive-generation.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q054 →](Q054-bpe-wordpiece-unigram.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`, `bert`, `gpt`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q053.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

BERT 与 GPT 的核心差异是什么？

## 2. 面试官到底在考什么

面试必须能从 attention mask、objective、任务形态三层比较。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

BERT encoder 使用双向 self-attention， 适合固定输入上的表征与判别； GPT decoder 使用 causal mask 做自回归 next-token prediction，天然适合开放式生成与 in-context learning。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：BERT 并非不能做生成，GPT 也不只做生成，但 inductive bias 不同。
- **PDF 基线要点**：大规模 decoder-only 通过 prompt 将很多理解任务转成生成。
- **PDF 基线要点**：检索双塔仍大量使用 encoder，因为吞吐和向量表示更经济。
- **扩展理解**：Encoder-only 擅长双向表示与判别式任务；decoder-only 天然适合自回归生成和 in-context learning。
- **扩展理解**：架构选择还涉及 pretraining objective、attention mask 和 serving pattern。
- **扩展理解**：不要把 BERT=理解、GPT=生成当成不可跨越的二元划分。

## 6. 专业深挖：原理、边界与工程

### BERT vs GPT 的差异首先是 Attention 可见性和训练目标
- BERT Encoder 允许每个位置同时看左右上下文，适合表示学习、分类、抽取；GPT Decoder 用 causal mask，只允许看前缀，因此天然支持从左到右生成。
- BERT MLM 只预测部分位置；GPT decoder LM 对几乎每个非首 token 都有 next-token supervision，训练信号更密集，也更适合规模化 generative modeling。
- “理解模型 vs 生成模型”只是结果描述；更第一性的区别是条件分布因子化和 attention mask。
### 边界与工程
- Encoder-only 在 dense retrieval、分类、NER 等低延迟判别任务仍非常强；Decoder-only 不是所有 NLP 任务的无条件最优架构。
- 生成式统一接口带来灵活性，但通常推理成本更高、输出更难严格校准。
- 生产选型应比较任务形式、吞吐、标签是否开放、是否需要生成解释，而不是按模型年代决策。

## 7. 实现、复杂度与工程验证

- 把训练目标与数据分布联系起来：哪些 token 产生监督、模型实际最大化什么。
- 比较 tokenizer/架构时给出序列长度、FLOPs、唯一 token、显存和推理代价。
- 预训练决策最终需要固定 compute/token 预算下的消融，而不是只看局部 loss。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 把“encoder 更懂语义”当作绝对事实。

## 9. 追问树

1. 为什么 decoder-only 成为通用 LLM 主流？
2. encoder-decoder 在翻译/条件生成中的优势？

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

- [BERT](https://arxiv.org/abs/1810.04805)
- [RoBERTa](https://arxiv.org/abs/1907.11692)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？](Q052-bert-vs-autoregressive-generation.md)
- [Q054 BPE、WordPiece、Unigram/SentencePiece 有什么区别？](Q054-bpe-wordpiece-unigram.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **BERT vs GPT 的差异首先是 Attention 可见性和训练目标**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
