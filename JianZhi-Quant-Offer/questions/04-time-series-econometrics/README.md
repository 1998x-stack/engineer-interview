# D. 时间序列与计量

> **模块目标**：时间序列与计量  
> **统一方法**：先判断平稳性和时间可用性，再讨论预测；把 serial dependence、heteroskedasticity、非同步采样和 regime change 视为一等公民。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 识别 stationarity/unit root/cointegration
- 构造无泄漏的时间序列验证
- 理解 volatility、异步采样和预测因果

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
| [031. 什么叫弱平稳（weak stationarity）？](q031-什么叫弱平稳-weak-stationarity.md) | ★☆☆ | 时间序列｜stationarity |
| [032. AR(1) 什么时候平稳？长期方差和 ACF 是什么？](q032-AR-1-什么时候平稳-长期方差和-ACF-是什么.md) | ★★☆ | AR(1)｜ACF｜稳定性 |
| [033. Random Walk 为什么 non-stationary？](q033-Random-Walk-为什么-non-stationary.md) | ★☆☆ | Unit root｜随机游走 |
| [034. 什么是 Unit Root？ADF test 在检验什么？](q034-什么是-Unit-Root-ADF-test-在检验什么.md) | ★★☆ | ADF｜unit root｜检验方向 |
| [035. 为什么两个独立 Random Walk 回归会产生 Spurious Regression？](q035-为什么两个独立-Random-Walk-回归会产生-Spurious-Regression.md) | ★★☆ | 伪回归｜非平稳｜t-stat |
| [036. 什么是 Cointegration？](q036-什么是-Cointegration.md) | ★★★ | Cointegration｜ECM｜长期关系 |
| [037. Granger Causality 是真正的因果吗？](q037-Granger-Causality-是真正的因果吗.md) | ★★☆ | 预测因果｜时序｜混杂 |
| [038. 为什么收益自相关低，但平方收益自相关高？](q038-为什么收益自相关低-但平方收益自相关高.md) | ★★☆ | Volatility clustering｜GARCH |
| [039. 为什么金融时间序列不能随机 train/test split？](q039-为什么金融时间序列不能随机-train-test-split.md) | ★☆☆ | 时间泄漏｜walk-forward｜validation |
| [040. Tick data 中两个资产的相关性如何估计？直接时间戳对齐有什么问题？](q040-Tick-data-中两个资产的相关性如何估计-直接时间戳对齐有什么问题.md) | ★★★ | 异步数据｜Epps effect｜sampling |

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

- Hamilton, *Time Series Analysis*；Tsay, *Analysis of Financial Time Series*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
