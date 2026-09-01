---
id: Q009
title: "什么是概率校准 Calibration？"
chapter: "数学、概率与机器学习基础"
difficulty: "★★★"
frequency: "★★★★"
tags:
  - ml-foundations
  - calibration
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q009 什么是概率校准 Calibration？

[← Q008](Q008-class-imbalance.md) | **第 1 章 · 数学、概率与机器学习基础** | [Q010 →](Q010-bayes-base-rate.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`ml-foundations`, `calibration`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q009.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

一个准确率很高的分类器为什么仍可能不 calibrated？怎么校准？

## 2. 面试官到底在考什么

判断候选人是否理解“分对”与“置信度可信”是两件事。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

若模型给出 0.8 概率的一组样本中约 80% 真为正例，则较为 calibrated。准确率只看 argmax 是 否正确，不约束概率数值的可靠性。

## 4. 白板核心公式

- $\mathrm{ECE}=\sum_m\frac{|B_m|}{n}\,|\mathrm{acc}(B_m)-\mathrm{conf}(B_m)|$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：常用 ECE、Brier score、reliability diagram。
- **PDF 基线要点**：Temperature scaling 在验证集上学习单个温度参数，通常保持分类排序但改变置信度。
- **PDF 基线要点**：LLM 的 token probability、verbal confidence 与任务正确率之间也存在校准问题。
- **扩展理解**：Calibration 评价“概率是否可信”，与 discrimination/ranking 是不同维度。
- **扩展理解**：ECE 依赖分桶设计，不能作为唯一指标；可结合 reliability diagram、Brier score、NLL。
- **扩展理解**：Temperature scaling 通常不改变类别 argmax，却能调整置信度尺度。

## 6. 专业深挖：原理、边界与工程

### Calibration 与 Ranking 是两件事
- 校准要求“所有预测为 0.8 的事件最终约 80% 发生”；它不等同于 Accuracy，也不等同于 AUC。
- 一个模型可以排序完美但极度过度自信；Temperature Scaling 通过单个 $T$ 缩放 logits，通常不改变 argmax/排序，却能改善概率尺度。
- ECE 依赖分桶，Brier Score 和 NLL 是 proper scoring rules；专业回答应知道它们衡量口径不同。
### 边界与工程
- 校准会随 prior/domain/time drift 失效，不能“一次校准永久有效”。
- 多类别、token-level 置信度和 sequence-level LLM confidence 是不同问题；后者往往要组合 logprob、verifier、retrieval evidence 等信号。
- 线上应保留原始 logits/score distribution，并按关键 slice 绘 reliability diagram，而不是只报一个 ECE 数字。

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

- 把 softmax 最大值直接当“真实概率”。
- 在测试集上拟合温度。

## 9. 追问树

1. 温度 T>1 会让分布怎样变化？
2. Calibration 和 ranking 能否同时优秀/差？

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

- [Q008 类别极度不平衡怎么处理？](Q008-class-imbalance.md)
- [Q010 贝叶斯基准率陷阱：99% 准确率为何不代表 99% 可信？](Q010-bayes-base-rate.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)

## 13. 一句话收束

> **Calibration 与 Ranking 是两件事**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
