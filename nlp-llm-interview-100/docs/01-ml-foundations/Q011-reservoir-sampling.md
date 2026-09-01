---
id: Q011
title: "超长文件如何等概率抽取 k 行？Reservoir Sampling"
chapter: "数学、概率与机器学习基础"
difficulty: "★★★"
frequency: "★★★★"
tags:
  - ml-foundations
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q011 超长文件如何等概率抽取 k 行？Reservoir Sampling

[← Q010](Q010-bayes-base-rate.md) | **第 1 章 · 数学、概率与机器学习基础** | [Q012 →](Q012-adam-vs-adamw.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`ml-foundations`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q011.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

文件太大无法载入内存，如何只用 O(k) 内存等概率抽取 k 行？

## 2. 面试官到底在考什么

考察流式算法证明能力。

### 评分维度

- 先给定义和假设，再给公式。
- 必须解释指标/损失与概率建模或业务目标的关系。
- 能说明边界条件、反例与常见误用。

## 3. 30-60 秒标准回答

使用 Reservoir Sampling：先装入前 k 个元素；第 i 个元素以 k/i 概率进入水库，并随机替换一个 已有元素。最终每个元素被保留的概率均为 k/N。

## 4. 白板核心公式

- $P(\text{item }i\text{ survives})=\frac{k}{N}$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：关键是能证明早期元素在后续多次“可能被替换”后最终概率仍为 k/N。
- **PDF 基线要点**：适用于未知总长度的 streaming data。
- **PDF 基线要点**：分布式场景可扩展为加权/合并水库。
- **扩展理解**：Reservoir Sampling 的关键不是代码，而是用归纳法证明每个样本最终被保留概率都是 k/N。
- **扩展理解**：该算法只需单遍扫描和 O(k) 内存，非常适合流式或未知总长度数据。
- **扩展理解**：扩展问题包括加权 reservoir sampling 与分布式合并。

## 6. 专业深挖：原理、边界与工程

### 为什么 Reservoir Sampling 严格无偏
- 前 k 个样本先进入池；第 i 个样本以 $k/i$ 概率进入，并均匀替换池中一个位置。
- 对第 i 个元素，进入概率是 $k/i$；之后每一步 j 被替换的概率为 $1/j$，存活概率连乘后恰好得到最终 $k/N$。
- 因此它在不知道 N、不能回看数据的单遍流式条件下仍保证所有样本等概率，时间 $O(N)$、空间 $O(k)$。
### 边界与工程
- 分布式场景“每个 shard 各抽 k 再拼”会偏向小 shard；需要按 shard 大小加权或使用可 merge 的随机 priority/top-k 方法。
- 加权抽样、时间衰减、分层采样需要相应的 weighted reservoir 变体。
- 单元测试可做 Monte Carlo：重复采样很多次，检查每个位置被选中的频率是否接近 $k/N$。

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

- 只描述算法，不会证明等概率。
- i 与下标从 0/1 开始混乱。

## 9. 追问树

1. 如何做 weighted reservoir sampling？
2. 如果多机各处理一个 shard，如何合并？

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

- [Q010 贝叶斯基准率陷阱：99% 准确率为何不代表 99% 可信？](Q010-bayes-base-rate.md)
- [Q012 Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md)
- [Q009 什么是概率校准 Calibration？](Q009-calibration.md)

## 13. 一句话收束

> **为什么 Reservoir Sampling 严格无偏**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
