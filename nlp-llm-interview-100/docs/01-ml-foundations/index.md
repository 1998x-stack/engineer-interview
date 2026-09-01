# 第 1 章 · 数学、概率与机器学习基础

> **章节目标**：把经验规则还原到概率建模、优化与评价指标。

## 1. 先修知识

微积分、线性代数、条件概率、最大似然、基础 Python。

## 2. 本章知识路线

Q001–Q004 建模 → Q005–Q009 泛化/归一化/指标 → Q010–Q012 概率题、流式算法与优化器。

## 3. 必须白板掌握

- Softmax+CE 梯度
- AUC 的 pairwise 解释
- MAP→L1/L2
- LayerNorm 统计轴
- AdamW 解耦 weight decay
- Reservoir Sampling 无偏证明

## 4. 高频失分模式

- 只背公式不说概率假设
- 把 metric 当 loss
- 忽略阈值/基准率/calibration
- 不做数值稳定性分析

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q001 | [为什么分类任务通常用交叉熵而不是 MSE？](Q001-cross-entropy-vs-mse.md) | ★★★ | ★★★★★ |
| Q002 | [Precision、Recall、F1：什么时候 Accuracy 会骗人？](Q002-precision-recall-f1.md) | ★★ | ★★★★★ |
| Q003 | [AUC 的两种理解为什么等价？](Q003-auc-ranking-interpretation.md) | ★★★★ | ★★★★★ |
| Q004 | [L1、L2 正则化与 MAP 的关系](Q004-l1-l2-map.md) | ★★★ | ★★★★★ |
| Q005 | [Bias‑Variance Trade‑off 在大模型时代还成立吗？](Q005-bias-variance.md) | ★★★ | ★★★★ |
| Q006 | [BatchNorm 与 LayerNorm：Transformer 为什么偏爱 LN？](Q006-batchnorm-vs-layernorm.md) | ★★★ | ★★★★★ |
| Q007 | [Dropout 为什么有效？大模型里为什么常变少？](Q007-dropout.md) | ★★ | ★★★★ |
| Q008 | [类别极度不平衡怎么处理？](Q008-class-imbalance.md) | ★★★ | ★★★★★ |
| Q009 | [什么是概率校准 Calibration？](Q009-calibration.md) | ★★★ | ★★★★ |
| Q010 | [贝叶斯基准率陷阱：99% 准确率为何不代表 99% 可信？](Q010-bayes-base-rate.md) | ★★★ | ★★★★ |
| Q011 | [超长文件如何等概率抽取 k 行？Reservoir Sampling](Q011-reservoir-sampling.md) | ★★★ | ★★★★ |
| Q012 | [Adam 与 AdamW 到底差在哪？](Q012-adam-vs-adamw.md) | ★★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
