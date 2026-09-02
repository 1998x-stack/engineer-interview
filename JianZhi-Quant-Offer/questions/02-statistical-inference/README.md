# B. 数理统计与统计推断

> **模块目标**：统计推断与研究可信度  
> **统一方法**：区分 estimand、estimator、sampling distribution 与 decision rule；任何显著性结果都要检查依赖、异方差、多重检验和选择偏差。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 从 estimator 性质理解统计结论
- 正确处理 standard error、multiple testing 与 robust inference
- 把显著性转化为可复验的研究证据

## 3. 面试能力分层

### Level 1：会做
能在 2–5 分钟内得到基础答案，符号和条件不出错。

### Level 2：会解释
能回答“为什么”，并给出至少一个反例/边界条件。

### Level 3：会迁移
能把数学结构映射到真实市场数据、研究协议或系统设计。

### Level 4：会审计
面对异常结果时，主动检查数据生成、时间信息、统计假设和实现差异，而不是默认结论正确。

## 4. 本章 10 题

| 题目 | 难度 | 标签 |
|---|---:|---|
| [011. Bernoulli 参数 p 的 MLE 是什么？](q011-Bernoulli-参数-p-的-MLE-是什么.md) | ★☆☆ | MLE｜Bernoulli｜一致性 |
| [012. 正态分布均值/方差的 MLE 是什么？为什么样本方差常除以 n-1？](q012-正态分布均值-方差的-MLE-是什么-为什么样本方差常除以-n-1.md) | ★★☆ | MLE｜无偏性｜自由度 |
| [013. Bias-Variance Tradeoff 如何从预测误差分解理解？](q013-Bias-Variance-Tradeoff-如何从预测误差分解理解.md) | ★★☆ | 泛化｜正则化｜噪声 |
| [014. p-value 到底表示什么？](q014-p-value-到底表示什么.md) | ★☆☆ | 假设检验｜p-value｜解释 |
| [015. 测试 10,000 个特征，总会出现显著结果，怎么处理？](q015-测试-10-000-个特征-总会出现显著结果-怎么处理.md) | ★★☆ | Multiple testing｜FDR｜研究过拟合 |
| [016. 为什么普通 OLS t-stat 在金融时间序列里常失真？](q016-为什么普通-OLS-t-stat-在金融时间序列里常失真.md) | ★★☆ | OLS｜HAC｜序列相关 |
| [017. Ridge 与 Lasso 的本质区别？](q017-Ridge-与-Lasso-的本质区别.md) | ★★☆ | Regularization｜高维特征｜共线性 |
| [018. Bootstrap 为什么不能直接 IID resample 金融时间序列？](q018-Bootstrap-为什么不能直接-IID-resample-金融时间序列.md) | ★★☆ | Bootstrap｜依赖｜block resampling |
| [019. Mean、Median、Trimmed Mean 在异常值下如何权衡？](q019-Mean-Median-Trimmed-Mean-在异常值下如何权衡.md) | ★☆☆ | Robust statistics｜异常值 |
| [020. 95% Confidence Interval 的正确频率学解释是什么？](q020-95%-Confidence-Interval-的正确频率学解释是什么.md) | ★★☆ | 置信区间｜coverage｜calibration |

## 5. 推荐刷题顺序

1. **第一遍：** 只做题，不看答案，每题限制 10 分钟。
2. **第二遍：** 强制补“假设 + Why + 一个失效场景”。
3. **第三遍：** 回答每题追问树，并做 30 秒口述。
4. **第四遍：** 把本章知识迁移到一个真实 research/system 案例。

## 6. 本章检查清单

完成本章后，你应该能：

- [ ] 不看答案复述 10 题核心结论；
- [ ] 对每题写出 formal model / key equation；
- [ ] 至少指出一个常见误用；
- [ ] 给出一个量化金融中的对应场景；
- [ ] 解释如何用 OOS / simulation / replay 验证。

## 7. 推荐阅读

- Casella & Berger, *Statistical Inference*；Efron & Hastie, *Computer Age Statistical Inference*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
