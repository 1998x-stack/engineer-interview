---
id: Q051
title: "BERT 原始预训练任务：MLM 与 NSP"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★"
frequency: "★★★★★"
tags:
  - pretraining
  - bert
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q051 BERT 原始预训练任务：MLM 与 NSP

[← Q050](../04-transformer/Q050-mha-mqa-gqa.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q052 →](Q052-bert-vs-autoregressive-generation.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`, `bert`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q051.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

BERT 的 MLM 与 NSP 分别做什么？后来为什么很多模型去掉 NSP？

## 2. 面试官到底在考什么

理解 encoder-only 训练信号。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

MLM 随机遮蔽部分 token，用双向上下文预测；NSP 判断两段是否连续。后续工作发现更长训练、 更多数据、更合理 sentence packing 等比 NSP 本身更关键，因此不少模型取消或替换它。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：MLM 训练/推理存在 [MASK] mismatch。
- **PDF 基线要点**：动态 masking 可让不同 epoch 看到不同 mask。
- **PDF 基线要点**：BERT 的双向性来自非 causal self-attention。
- **扩展理解**：MLM 是双向 denoising objective，NSP 是句对关系任务；BERT 成功并不意味着 NSP 必不可少。
- **扩展理解**：RoBERTa 等工作通过去掉 NSP、增大数据和动态 mask 改进训练。
- **扩展理解**：要理解 encoder 预训练目标与 downstream representation 的关系。

## 6. 专业深挖：原理、边界与工程

### BERT 的两个原始任务要分开理解
- MLM 随机选择部分 token 做遮盖/替换，让模型利用双向上下文预测原词，本质上学习 $P(x_i|x_{\setminus i})$，不是标准自回归似然。
- NSP 判断两个 segment 是否来自原文连续片段，试图让模型学习句间关系；后续 RoBERTa 等工作显示 NSP 并非 BERT 成功的必要条件。
- BERT 的真正核心是 Encoder-only + 双向 self-attention + 大规模 MLM 预训练，NSP 只是原始配方的一部分。
### 边界与工程
- MLM 只在被选位置产生主要预测损失，训练信号密度低于 decoder LM 的“每个 token 都预测下一个 token”。
- 经典 80/10/10 mask 策略是为减轻 `[MASK]` 训练–下游分布差异，但具体比例不是理论定理。
- 做 BERT 预训练复现时要明确 dynamic masking、whole-word masking、sequence packing 与 tokenizer 版本，它们都会影响结果。

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

- 把 MLM 说成自回归。

## 9. 追问树

1. 15% mask 的 token 如何处理？
2. SOP 与 NSP 有什么不同？

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

- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](../04-transformer/Q050-mha-mqa-gqa.md)
- [Q052 为什么 BERT 不能天然像 GPT 一样左到右生成？](Q052-bert-vs-autoregressive-generation.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **BERT 的两个原始任务要分开理解**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
