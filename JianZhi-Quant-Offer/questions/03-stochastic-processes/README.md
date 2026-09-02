# C. 随机过程

> **模块目标**：随机过程与状态演化  
> **统一方法**：先定义 filtration/state，再明确 Markov、martingale、stationarity 等性质；连续时间题要区分路径性质、条件期望和二次变差。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 理解 filtration、martingale、Markov 与 hitting time
- 掌握 Brownian/SDE 的路径和条件期望直觉
- 能把连续时间模型与离散观测联系起来

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
| [021. Brownian Motion 的核心性质是什么？](q021-Brownian-Motion-的核心性质是什么.md) | ★★☆ | 随机过程｜Brownian Motion |
| [022. 为什么 Brownian Motion 几乎处处不可微？](q022-为什么-Brownian-Motion-几乎处处不可微.md) | ★★★ | 尺度分析｜quadratic variation｜Itô 直觉 |
| [023. 什么是 Martingale？](q023-什么是-Martingale.md) | ★★☆ | 条件期望｜公平游戏｜过滤 |
| [024. Optional Stopping Theorem 为什么不能随便套？](q024-Optional-Stopping-Theorem-为什么不能随便套.md) | ★★★ | Stopping time｜martingale｜条件 |
| [025. 几何布朗运动为什么保持价格为正？](q025-几何布朗运动为什么保持价格为正.md) | ★★☆ | SDE｜GBM｜Itô |
| [026. Ornstein-Uhlenbeck Process 的长期均值是什么？](q026-Ornstein-Uhlenbeck-Process-的长期均值是什么.md) | ★★☆ | Mean reversion｜OU｜SDE |
| [027. Poisson Process 的 inter-arrival time 为什么是指数分布？](q027-Poisson-Process-的-inter-arrival-time-为什么是指数分布.md) | ★★☆ | Poisson｜Exponential｜memoryless |
| [028. 给定 Markov transition matrix，如何求 stationary distribution？](q028-给定-Markov-transition-matrix-如何求-stationary-distribution.md) | ★★☆ | Markov chain｜stationary｜ergodicity |
| [029. Kalman Filter 的本质是什么？](q029-Kalman-Filter-的本质是什么.md) | ★★★ | State space｜Bayesian filtering｜线性高斯 |
| [030. HMM 与普通 Markov Chain 的区别？](q030-HMM-与普通-Markov-Chain-的区别.md) | ★★☆ | HMM｜latent state｜EM |

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

- Shreve, *Stochastic Calculus for Finance II*；Øksendal, *Stochastic Differential Equations*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
