---
id: Q002
title: "Precision、Recall、F1：什么时候 Accuracy 会骗人？"
chapter: "数学、概率与机器学习基础"
difficulty: "★★"
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

# Q002 Precision、Recall、F1：什么时候 Accuracy 会骗人？

[← Q001](Q001-cross-entropy-vs-mse.md) | **第 1 章 · 数学、概率与机器学习基础** | [Q003 →](Q003-auc-ranking-interpretation.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`ml-foundations`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q002.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

解释 Precision、Recall、F1；给出 Accuracy 很高但模型不可用的例子。

## 2. 面试官到底在考什么

考察指标是否与业务错误成本建立联系。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

Precision 关注“预测为正的有多少是真的” ；Recall 关注“真实正例找回多少” ；F1 是二者调和平 均。类别极不平衡时，全预测多数类也可获得很高 Accuracy。

## 4. 白板核心公式

- $P=\frac{TP}{TP+FP}$
- $R=\frac{TP}{TP+FN}$
- $F_1=\frac{2PR}{P+R}$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：指标选择必须回到 FP 与 FN 的业务成本：风控、召回、审核、检索任务的权衡不同。
- **PDF 基线要点**：F1 不使用 TN，因此更聚焦正类识别，但也因此不是所有业务都适合。
- **PDF 基线要点**：阈值变化会移动 Precision-Recall，需要结合 PR 曲线或固定 Recall 下看 Precision。
- **扩展理解**：把指标选择转换成 FP/FN 成本问题；不同业务可能更关心固定 Recall 下 Precision。
- **扩展理解**：理解 micro/macro/weighted averaging 对长尾类别的不同偏置。
- **扩展理解**：阈值调优属于决策层，和模型打分能力本身要分开分析。

## 6. 专业深挖：原理、边界与工程

### 指标背后的条件概率
- Precision 的条件是“预测为正”，Recall 的条件是“真实为正”；二者分母不同，分别对应误报和漏报。Accuracy 把 FP/FN/TN/TP 都按样本等价计价，因此在长尾类别下可能非常误导。
- $F_1$ 是 Precision 与 Recall 的调和平均，只有二者同时高时才高；它忽略 TN，所以不是所有分类任务的通用最优指标。
- 阈值改变会沿 PR/ROC 曲线移动。真正的生产问题通常是“固定 Recall≥95% 时最大化 Precision”或最小化显式业务成本，而不是最大化某个孤立指标。
### 边界与工程
- 多分类要说明 Macro/Micro/Weighted F1；Macro 对小类更敏感，Micro 更接近总体样本计数。
- 极端不平衡时 PR-AUC 往往比 ROC-AUC 更符合正类检出体验；线上还要按语言、地域、长度、实体新旧等 slice 监控。
- 面试中最好用“1% 正例、全部预测负类，Accuracy=99% 但 Recall=0”快速证明 Accuracy 的局限。

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

- 只背公式，不说明 threshold。
- 把 F1 当成“永远比 Accuracy 好”。

## 9. 追问树

1. Macro-F1 与 Micro-F1 区别？
2. 为什么 PR-AUC 在稀有正例场景常比 ROC-AUC 更有解释力？

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

- [Q001 为什么分类任务通常用交叉熵而不是 MSE？](Q001-cross-entropy-vs-mse.md)
- [Q003 AUC 的两种理解为什么等价？](Q003-auc-ranking-interpretation.md)
- [Q009 什么是概率校准 Calibration？](Q009-calibration.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)

## 13. 一句话收束

> **指标背后的条件概率**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
