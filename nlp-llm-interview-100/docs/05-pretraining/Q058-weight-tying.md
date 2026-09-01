---
id: Q058
title: "Weight Tying：为什么输入 Embedding 与 LM Head 可以共享？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★"
frequency: "★★★"
tags:
  - pretraining
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q058 Weight Tying：为什么输入 Embedding 与 LM Head 可以共享？

[← Q057](Q057-perplexity.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q059 →](Q059-scaling-laws.md)

> **难度**：★★  ·  **频率**：★★★  ·  **标签**：`pretraining`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q058.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

把 input embedding E 与 output projection W 设为 E^T 有什么好处？

## 2. 面试官到底在考什么

理解词表输入输出对偶结构。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

输入和输出都位于同一词汇空间，共享参数可减少大词表带来的参数量，并鼓励输入/输出语义表示 对齐。

## 4. 白板核心公式

- $W_{\mathrm{LM\ head}}=E^\top$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：大词表模型中 embedding/head 可占显著参数。
- **PDF 基线要点**：共享后两端梯度共同更新同一矩阵。
- **PDF 基线要点**：并非所有架构都必须 tying，维度/并行策略也会影响。
- **扩展理解**：weight tying 共享输入 lexical space 与输出 classifier，减少参数并提供结构先验。
- **扩展理解**：需要明确矩阵转置关系和词表维度。
- **扩展理解**：某些架构会保留独立 output head，选择取决于容量和经验。

## 6. 专业深挖：原理、边界与工程

### Weight Tying 是“词空间输入输出共享”
- 输入 Embedding 是 $E\in\mathbb R^{V\times d}$，输出 LM Head 常为 $W_{out}\in\mathbb R^{V\times d}$；Weight Tying 令二者共享参数或使用 $E^T$ 关系。
- 输入端学习“词如何被表示”，输出端学习“hidden 与哪个词相似”；共享可让两种词空间几何互相约束，同时减少约 $Vd$ 参数。
- 大词表模型中 Embedding/LM Head 参数占比不一定是主导，但共享仍能显著节省内存。
### 边界与工程
- hidden dimension 与 embedding dimension 必须兼容；某些模型有额外 projection 时不能直接简单 tying。
- 量化/张量并行时共享权重意味着 embedding lookup 与 LM head shard 需要一致布局。
- Tying 是建模选择，不是绝对最佳；输入和输出分布极不对称的任务可能受益于不共享。

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

- 认为 tying 不改变训练动态。

## 9. 追问树

1. 输出 bias 还需要吗？
2. 矩阵并行下怎么切词表 head？

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

- [Q057 Perplexity：什么时候能比、什么时候不能比？](Q057-perplexity.md)
- [Q059 Scaling Law：为什么不能只堆参数？](Q059-scaling-laws.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **Weight Tying 是“词空间输入输出共享”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
