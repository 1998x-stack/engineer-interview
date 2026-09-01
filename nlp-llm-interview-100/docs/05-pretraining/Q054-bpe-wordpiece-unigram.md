---
id: Q054
title: "BPE、WordPiece、Unigram/SentencePiece 有什么区别？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - pretraining
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q054 BPE、WordPiece、Unigram/SentencePiece 有什么区别？

[← Q053](Q053-bert-vs-gpt.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q055 →](Q055-subword-byte-tokenization.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q054.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

比较 BPE、WordPiece、Unigram；SentencePiece 又是什么层级的概念？

## 2. 面试官到底在考什么

Tokenizer 是数据与模型接口。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

BPE 迭代合并高频 pair；WordPiece 使用与似然/评分相关的合并准则；Unigram 从候选子词集 合出发，通过概率模型逐步删减。SentencePiece 是可直接在原始文本上训练/编码的工具框架，常 实现 BPE 或 Unigram。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：Tokenizer 决定序列长度、词表大小、数字/代码切分和多语言公平性。
- **PDF 基线要点**：byte-level 方法可避免 OOV。
- **PDF 基线要点**：同一模型参数量下，tokenizer 改变实际可见字符长度与训练 token 预算。
- **扩展理解**：BPE 是贪心 merge；Unigram 是概率词表选择；WordPiece 常用 likelihood 类准则描述。
- **扩展理解**：SentencePiece 是 tokenizer framework，可实现 BPE/Unigram，并不等于一种算法。
- **扩展理解**：面试应关注训练、encode/decode、special token 与 normalization pipeline。

## 6. 专业深挖：原理、边界与工程

### 三类 Subword 方法的优化对象不同
- BPE 从字符/字节初始符号出发，反复合并高频 pair；WordPiece 也做子词构造，但经典描述更强调基于语言模型似然/增益选择 merge。
- Unigram LM 从较大候选词表出发，给每个 token 概率，通过删除对似然贡献小的 token 逐步缩词表；分词时可用 Viterbi/采样。
- SentencePiece 是工具/框架，可实现 BPE 或 Unigram，并直接在原始文本上把空格也视为符号；不能把 SentencePiece 当成与 BPE 完全平级的一种唯一算法。
### 边界与工程
- 实际 tokenizer 还涉及 normalization、byte fallback、special tokens、pre-tokenization 和 vocabulary size，往往比“算法名”更影响模型行为。
- 中英多语言时字节/Unicode coverage、长尾字符和 emoji 处理非常关键。
- tokenizer 一旦用于训练 checkpoint 就成为模型接口的一部分，后续随意改词表会破坏 embedding/LM head 对齐。

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

- 把 SentencePiece 当作一种唯一算法。

## 9. 追问树

1. 为什么中文/代码的 token fertility 很重要？
2. tokenizer vocabulary 越大越好吗？

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

- [Q053 BERT 与 GPT：双向理解和因果生成如何取舍？](Q053-bert-vs-gpt.md)
- [Q055 为什么 LLM 普遍使用 Subword/Byte Tokenization？](Q055-subword-byte-tokenization.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **三类 Subword 方法的优化对象不同**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
