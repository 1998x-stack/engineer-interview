---
id: Q004
title: "L1、L2 正则化与 MAP 的关系"
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

# Q004 L1、L2 正则化与 MAP 的关系

[← Q003](Q003-auc-ranking-interpretation.md) | **第 1 章 · 数学、概率与机器学习基础** | [Q005 →](Q005-bias-variance.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`ml-foundations`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q004.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

L1 与 L2 有何区别？为什么可以分别联系 Laplace/Gaussian 先验？

## 2. 面试官到底在考什么

考察优化、概率视角和稀疏性直觉。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

L1 倾向稀疏解，L2 倾向平滑缩小参数。MAP 中，负对数先验会以正则项形式进入目标函数，因此 不同先验对应不同惩罚。

## 4. 白板核心公式

- $\mathcal L_{L1}=\mathcal L+\lambda\|w\|_1$
- $\mathcal L_{L2}=\mathcal L+\lambda\|w\|_2^2$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：L1 在 0 附近存在尖点，更容易把系数压到恰好 0。
- **PDF 基线要点**：L2 对大权重惩罚更强且可微，优化通常更稳定。
- **PDF 基线要点**：深度学习中的 weight decay 与“把 L2 加到 loss”在自适应优化器下并不完全等价。
- **扩展理解**：L1/L2 可分别对应 Laplace/Gaussian 先验，从 MAP 统一理解正则。
- **扩展理解**：L1 的稀疏性来自非光滑几何，而不是“参数小就自动变 0”的口号。
- **扩展理解**：现代优化器中的 weight decay 与 L2 penalty 不应混为一谈。

## 6. 专业深挖：原理、边界与工程

### 正则化的三种解释
- L2 对应高斯先验、L1 对应 Laplace 先验：把先验乘进后验并取负对数，就得到 MAP 目标中的正则项。
- L1 等值线在坐标轴处有尖角，优化解更容易落到精确 0；L2 更倾向于连续缩小所有参数，并可改善病态/共线方向的条件数。
- “参数更小”不是泛化的完整原因，深度学习中还存在优化隐式偏置、数据增强和参数化等因素。
### 边界与工程
- 对强相关特征，L1 的变量选择可能不稳定；Elastic Net 可组合 L1/L2。
- 深度模型中 bias、LayerNorm/RMSNorm scale 常不做 weight decay，需显式 parameter groups。
- 要能解释为什么 Adam 中“把 L2 加进梯度”与 AdamW 的 decoupled weight decay 不等价。

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

- 只说“L1 防过拟合，L2 也防过拟合”。
- 混淆 regularization coefficient 与 learning rate。

## 9. 追问树

1. 为什么 AdamW 要 decouple weight decay？
2. Elastic Net 是什么？

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

- [Q003 AUC 的两种理解为什么等价？](Q003-auc-ranking-interpretation.md)
- [Q005 Bias‑Variance Trade‑off 在大模型时代还成立吗？](Q005-bias-variance.md)
- [Q009 什么是概率校准 Calibration？](Q009-calibration.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)

## 13. 一句话收束

> **正则化的三种解释**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
