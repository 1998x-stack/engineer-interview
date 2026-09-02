# H. 组合、风险与优化

> **模块目标**：组合、风险与优化  
> **统一方法**：优化器会放大输入估计误差；回答时必须同时讨论目标函数、约束、估计误差、数值条件性和可交易性。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 推导基础组合优化与风险分解
- 理解 covariance estimation error 的放大
- 把成本、约束、稳定性加入优化器

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
| [071. 推导 Minimum-Variance Portfolio。](q071-推导-Minimum-Variance-Portfolio.md) | ★★★ | Portfolio optimization｜Lagrange |
| [072. 为什么直接使用 sample covariance matrix 很危险？](q072-为什么直接使用-sample-covariance-matrix-很危险.md) | ★★☆ | Covariance｜high-dimensional｜conditioning |
| [073. 什么是 Covariance Shrinkage？](q073-什么是-Covariance-Shrinkage.md) | ★★☆ | Shrinkage｜bias-variance｜risk model |
| [074. PCA 在风险模型里是什么意思？](q074-PCA-在风险模型里是什么意思.md) | ★★☆ | PCA｜eigenportfolio｜factor |
| [075. VaR 与 Expected Shortfall 有什么区别？](q075-VaR-与-Expected-Shortfall-有什么区别.md) | ★★☆ | Tail risk｜VaR｜ES |
| [076. 为什么 Volatility Targeting 不等于风险恒定？](q076-为什么-Volatility-Targeting-不等于风险恒定.md) | ★★☆ | Vol targeting｜estimation lag｜risk |
| [077. 什么是 Marginal Contribution to Risk？](q077-什么是-Marginal-Contribution-to-Risk.md) | ★★☆ | Risk decomposition｜gradient |
| [078. 为什么 Portfolio Optimization 容易产生极端权重？](q078-为什么-Portfolio-Optimization-容易产生极端权重.md) | ★★☆ | Estimation error｜inverse problem｜constraints |
| [079. 如何把 turnover/transaction-cost penalty 放入优化？](q079-如何把-turnover-transaction-cost-penalty-放入优化.md) | ★★☆ | Convex optimization｜turnover｜regularization |
| [080. Factor Neutralization 怎么理解？](q080-Factor-Neutralization-怎么理解.md) | ★★☆ | Residualization｜exposure｜confounding |

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

- Boyd & Vandenberghe, *Convex Optimization*；Grinold & Kahn, *Active Portfolio Management*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
