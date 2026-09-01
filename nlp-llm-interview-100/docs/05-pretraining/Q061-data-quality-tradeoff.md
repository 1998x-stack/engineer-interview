---
id: Q061
title: "为什么“数据质量越高越好”是危险说法？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - pretraining
  - data
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q061 为什么“数据质量越高越好”是危险说法？

[← Q060](Q060-pretraining-dedup.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q062 →](Q062-mixed-precision.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`, `data`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q061.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

如果只保留最像 Wikipedia/教材的文本，会发生什么？

## 2. 面试官到底在考什么

考察数据分布工程意识。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

过强过滤提高平均可读性，但可能降低覆盖、多样性、长尾与独特 token 数。真正目标应是训练效 用，而不是某个单一 quality classifier 分数。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：质量模型本身带有教师偏好与域偏差。
- **PDF 基线要点**：高质量小数据重复多 epoch 可能不如更大、适度噪声的数据。
- **PDF 基线要点**：应通过小模型/proxy training 与 downstream ablation 验证过滤策略。
- **扩展理解**：过强过滤提高平均质量同时会降低覆盖、多样性和 unique tokens。
- **扩展理解**：现代数据工程更关心 quality×coverage×diversity×scale 的联合 utility。
- **扩展理解**：分类器“高质量”往往意味着“像其正样本分布”，不是客观真理。

## 6. 专业深挖：原理、边界与工程

### “高质量”不是单一标量
- 过滤得越狠，平均文本质量可能提高，但 unique token、长尾领域、口语、少数语言和风格多样性会下降；训练效用可能反而变差。
- 质量分类器通常学习“像某些正例来源”的分布偏好，不等于客观真值；教育文本分类器会天然偏向解释性、正式书面语。
- 更合理目标是固定训练预算下优化 quality × coverage × diversity × uniqueness × downstream utility。
### 边界与工程
- 过滤器应保存连续 score 与 reason code，支持阈值消融，而不是一遍删除后丢失信息。
- 不同语言/领域需要独立校准，英文网页阈值不能无脑复制到代码、论文或低资源语言。
- 真正判断数据决策需要 proxy model 训练或 downstream ablation，而不是人工读十条文本。

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

- “越干净越好”是典型错误。

## 9. 追问树

1. 如何设计 quality bucket？
2. 如何量化 diversity 与 coverage？

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

- [Q060 大模型训练为什么必须去重？](Q060-pretraining-dedup.md)
- [Q062 Mixed Precision：BF16 为什么常比 FP16 稳？](Q062-mixed-precision.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)

## 13. 一句话收束

> **“高质量”不是单一标量**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
