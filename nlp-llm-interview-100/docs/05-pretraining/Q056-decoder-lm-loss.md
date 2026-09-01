---
id: Q056
title: "Decoder LM Loss：为什么每个 token 都是监督信号？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★"
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

# Q056 Decoder LM Loss：为什么每个 token 都是监督信号？

[← Q055](Q055-subword-byte-tokenization.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q057 →](Q057-perplexity.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q056.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

写出自回归语言模型的因子分解和 loss。

## 2. 面试官到底在考什么

理解预训练目标与数据规模。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

通过链式法则把序列概率分解为每个位置的 next-token 条件概率；训练时 teacher forcing 一次 前向可对多个位置并行计算交叉熵，因此每个 token 都提供监督。

## 4. 白板核心公式

- $\mathcal L=-\sum_{t=1}^T\log P_\theta(x_t|x_{<t})$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：训练可并行，但生成必须按序列依赖逐步 decode。
- **PDF 基线要点**：padding/packing 时要正确构造 loss mask。
- **PDF 基线要点**：instruction tuning 常只对 assistant 部分计算 loss。
- **扩展理解**：causal LM 通过链式法则把序列概率分解为每个位置的 next-token loss。
- **扩展理解**：teacher forcing 训练时所有位置可并行计算，但推理仍串行生成。
- **扩展理解**：需要区分 padding token、ignore index、prompt/response masking。

## 6. 专业深挖：原理、边界与工程

### Decoder LM 的监督密度为什么高
- 自回归分解 $P(x_{1:T})=\prod_tP(x_t|x_{<t})$，因此一个长度 T 的训练序列可提供约 T−1 个 next-token 监督位置。
- Teacher Forcing 训练时整段 target 已知，借助 causal mask 可以并行计算所有位置的 logits；并不是训练也必须逐 token 串行。
- Loss 通常是所有有效 token 的 Cross Entropy，packing 让多个短样本共享长序列，提高 token utilization。
### 边界与工程
- SFT 常只对 assistant response token 计算 loss，prompt/user token 作为条件而不反向监督；这与全量 pretraining LM loss 不同。
- Padding、packed sample boundary、BOS/EOS 的 loss mask 必须定义清楚，否则会产生错误监督。
- 分布式变长 batch 中应按“有效 token 数”正确归一化 loss，避免不同 worker token 数差异改变梯度尺度。

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

- 把“预测下一个词”误认为训练也是一个 token 一个 token 跑。

## 9. 追问树

1. 为什么 teacher forcing 会产生 exposure bias？
2. packing 多条文档时边界如何处理？

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

- [Q055 为什么 LLM 普遍使用 Subword/Byte Tokenization？](Q055-subword-byte-tokenization.md)
- [Q057 Perplexity：什么时候能比、什么时候不能比？](Q057-perplexity.md)
- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)

## 13. 一句话收束

> **Decoder LM 的监督密度为什么高**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
