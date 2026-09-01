---
id: Q001
title: "为什么分类任务通常用交叉熵而不是 MSE？"
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

# Q001 为什么分类任务通常用交叉熵而不是 MSE？

**第 1 章 · 数学、概率与机器学习基础** | [Q002 →](Q002-precision-recall-f1.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`ml-foundations`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q001.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

多分类为什么常用 Softmax + Cross Entropy，而不是对 one-hot 标签直接做 MSE？

## 2. 面试官到底在考什么

判断候选人是否能把“经验用法”还原成概率建模与梯度性质。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

交叉熵对应分类分布的负对数似然；配合 Softmax 后，对 logit 的梯度简洁为“预测概率 - 标签”。 MSE 并非不能用于分类，但概率解释更弱，且与 Softmax 组合时梯度常更不利。

## 4. 白板核心公式

- $p_k=\frac{e^{z_k}}{\sum_j e^{z_j}}$
- $\mathcal L=-\sum_k y_k\log p_k$
- $\frac{\partial \mathcal L}{\partial z_k}=p_k-y_k$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：从最大似然出发：若 y 服从 categorical distribution，最大化 P(y|x) 等价于最小化 -log p_y。
- **PDF 基线要点**：Softmax + CE 的链式求导发生消项，梯度直接反映概率误差，利于优化。
- **PDF 基线要点**：“CE 一定比 MSE 好”不是数学定理；特殊任务、校准目标或非标准输出空间可能采用其他损失。
- **扩展理解**：从最大似然角度推导 CE，而不是停留在“分类就用 CE”的经验规则。
- **扩展理解**：把 Softmax Jacobian 与交叉熵求导连起来，解释为何最终得到 p-y。
- **扩展理解**：指出 MSE 并非非法：关键是概率模型、梯度几何与优化目标是否匹配。

## 6. 专业深挖：原理、边界与工程

### 从概率建模到梯度
- Cross Entropy 对应 categorical/Bernoulli 条件分布的负对数似然；先假设 $P(y|x)$，再最大化似然，就自然得到 CE，而不是因为“分类题约定俗成”。
- Softmax + CE 有关键消项：$\partial L/\partial z_k=p_k-y_k$。梯度直接由预测概率和标签差异决定，自信但错误的样本仍会收到强纠正信号。
- 若在 Softmax 概率上使用 MSE，梯度会额外经过 Softmax Jacobian，极端概率区域更容易饱和。MSE 不是“不能分类”，而是统计假设和优化几何通常不如 CE 匹配。
### 边界与工程
- 多标签任务是多个 Bernoulli，通常用 sigmoid+BCE，不是单个 Softmax CE；排序、校准、噪声标签任务也可能使用其他 surrogate loss。
- 工程上优先使用 fused `cross_entropy(logits, target)`，不要先 `softmax` 再 `log`；同时处理 padding mask、token-level normalization 和 `ignore_index`。
- 高级追问要能连接 Label Smoothing、Focal Loss、Brier Score 与 Calibration：它们优化的是不同目标，不应只比较“谁收敛快”。

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

- 只说“CE 收敛快”但解释不了为什么。
- 把“分类用 CE、回归用 MSE”当成不可违反的规则。

## 9. 追问树

1. 二分类 BCE 与多分类 CE 有什么关系？
2. Label Smoothing 改变了什么？
3. 为什么回归 MSE 可由高斯噪声假设推出？

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

- [Q002 Precision、Recall、F1：什么时候 Accuracy 会骗人？](Q002-precision-recall-f1.md)
- [Q009 什么是概率校准 Calibration？](Q009-calibration.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)

## 13. 一句话收束

> **从概率建模到梯度**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
