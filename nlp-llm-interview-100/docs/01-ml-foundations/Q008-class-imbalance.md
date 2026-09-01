---
id: Q008
title: "类别极度不平衡怎么处理？"
chapter: "数学、概率与机器学习基础"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - ml-foundations
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q008 类别极度不平衡怎么处理？

[← Q007](Q007-dropout.md) | **第 1 章 · 数学、概率与机器学习基础** | [Q009 →](Q009-calibration.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`ml-foundations`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q008.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

正例只有万分之一，你会如何训练和评估？

## 2. 面试官到底在考什么

从数据、loss、采样与指标四层回答。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

先定义错误成本，再组合采样、loss reweight、hard negative mining 与适配指标。关键不是机 械地 oversample，而是保持训练分布、校准与线上阈值的一致性。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：数据层：分层采样、正例增强、难负例挖掘。
- **PDF 基线要点**：目标层：class weight、focal loss、pairwise ranking。
- **PDF 基线要点**：评估层：PR-AUC、Recall@ 固定 Precision、成本敏感指标。
- **扩展理解**：先定义目标错误成本，再决定重采样、cost-sensitive loss、focal loss 或阈值。
- **扩展理解**：Hard negative mining 往往比无脑过采样更有信息价值，但会引入 sampling bias。
- **扩展理解**：指标要与线上 base rate 一致，避免离线平衡数据造成错觉。

## 6. 专业深挖：原理、边界与工程

### 不平衡的本质是梯度和代价不平衡
- 类别不平衡不是单纯“样本数量不一样”，而是训练先验、线上先验和 FP/FN 业务成本可能同时不一致。
- Weighted CE 改变类别梯度贡献；Focal Loss 用 $(1-p_t)^\gamma$ 压低易样本权重，把预算集中到 hard examples。
- 数据层还可做 over/under-sampling 与 hard negative mining，但 hard 不等于有价值：脏标签往往也是“高损失样本”。
### 边界与工程
- 过采样可能导致少数类重复过拟合，欠采样会丢多数类信息；应同时看 PR-AUC、per-class recall 和 calibration。
- 训练时改变 class prior 后，输出概率通常需要重新校准；部署阈值应作为独立业务配置而非写死在模型中。
- 检索/推荐中的负例最好分 random、in-batch、hard negative 分层，分别承担稳定训练和边界学习。

## 7. 实现、复杂度与工程验证

- 写清随机变量、概率模型与 loss/metric 的区别。
- 涉及梯度时检查数值尺度、饱和、方差与优化器交互。
- 实验上至少做多 seed、slice 和 calibration/threshold 检查。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 对测试集做过采样导致指标失真。
- 只用 accuracy。

## 9. 追问树

1. Focal Loss 为什么能聚焦 hard example？
2. Hard negative mining 如何避免 false negatives？

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

- [Deep Learning book](https://www.deeplearningbook.org/)
- [AdamW](https://arxiv.org/abs/1711.05101)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q007 Dropout 为什么有效？大模型里为什么常变少？](Q007-dropout.md)
- [Q009 什么是概率校准 Calibration？](Q009-calibration.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)

## 13. 一句话收束

> **不平衡的本质是梯度和代价不平衡**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
