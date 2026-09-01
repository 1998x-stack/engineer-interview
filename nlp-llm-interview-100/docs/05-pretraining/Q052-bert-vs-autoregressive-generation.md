---
id: Q052
title: "为什么 BERT 不能天然像 GPT 一样左到右生成？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★★"
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

# Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？

[← Q051](Q051-bert-mlm-nsp.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q053 →](Q053-bert-vs-gpt.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`, `bert`, `gpt`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q052.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

BERT 会预测词，为什么不能直接当 GPT 用？

## 2. 面试官到底在考什么

从概率分解解释架构差异。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

BERT 的 MLM 学的是被遮蔽位置在双向上下文条件下的条件分布，并没有训练完整的自回归链式 分解。GPT 直接优化 P(x_t|x_<t)，与逐 token 生成过程一致。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：可以用 Gibbs-like iterative masking 生成，但效率与分布不同。
- **PDF 基线要点**：Encoder-only 更适合表示/理解；decoder-only 统一生成接口。
- **PDF 基线要点**：Prefix-LM/encoder-decoder 是中间路线。
- **扩展理解**：BERT 的 MLM 条件分布使用左右上下文，训练目标与严格左到右生成的概率分解不匹配。
- **扩展理解**：可以通过迭代 mask 生成，但效率和建模目标都不同。
- **扩展理解**：现代生成模型采用 decoder-only 主要因为 autoregressive objective 与推理方式一致。

## 6. 专业深挖：原理、边界与工程

### BERT 不能天然左到右生成的根本原因是训练条件分布不同
- BERT 每个被 mask 的位置可同时看到左、右上下文，学的是双向条件恢复；GPT 学的是 $P(x_t|x_{<t})$，训练目标与 autoregressive generation 完全一致。
- 若直接让 BERT 逐步生成，下一个 token 的条件分布并没有在同样因果约束下被训练，且模型会习惯看到“未来”信息。
- 理论上可以用 iterative masking 等方式让 BERT 生成，但那是不同采样过程，不等于标准一次一 token 的 decoder LM。
### 边界与工程
- Encoder–Decoder 模型可同时用双向 encoder 理解输入、因果 decoder 生成输出，兼顾两类优势。
- Prefix-LM、UniLM 等通过 attention mask 设计可以在统一 Transformer 中训练不同条件结构。
- “BERT 不能生成”不是绝对物理限制，更准确是它没有按标准 autoregressive factorization 训练，因此不天然适合 GPT 式生成。

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

- 回答“因为 BERT 是 encoder，GPT 是 decoder”但不说明训练目标。

## 9. 追问树

1. T5 为什么能生成？
2. BERT 做填空生成的局限？

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

- [Q051 BERT 原始预训练任务：MLM 与 NSP](Q051-bert-mlm-nsp.md)
- [Q053 BERT 与 GPT：双向理解和因果生成如何取舍？](Q053-bert-vs-gpt.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **BERT 不能天然左到右生成的根本原因是训练条件分布不同**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
