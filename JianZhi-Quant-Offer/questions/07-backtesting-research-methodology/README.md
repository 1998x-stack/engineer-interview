# G. 数据、回测与研究方法论

> **模块目标**：回测与研究方法论  
> **统一方法**：先证明实验没有泄漏、幸存者偏差和成本幻觉，再谈 alpha；把每一次试验本身也视为需要记录和审计的数据。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 系统审计 look-ahead/survivorship/PIT/cost
- 建立 walk-forward 与 research lineage
- 识别 multiple testing 与 backtest overfit

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
| [061. 什么是 Look-Ahead Bias？](q061-什么是-Look-Ahead-Bias.md) | ★☆☆ | Backtest｜leakage｜timestamp |
| [062. 什么是 Survivorship Bias？](q062-什么是-Survivorship-Bias.md) | ★☆☆ | Universe｜delisting｜历史数据 |
| [063. Corporate Actions 为什么会把回测搞坏？](q063-Corporate-Actions-为什么会把回测搞坏.md) | ★★☆ | Adjusted data｜split｜dividend |
| [064. Point-in-Time Data 是什么？](q064-Point-in-Time-Data-是什么.md) | ★★☆ | PIT｜revision｜data lineage |
| [065. 为什么 transaction cost 不能简单固定减 1bp？](q065-为什么-transaction-cost-不能简单固定减-1bp.md) | ★★☆ | Cost model｜spread｜impact |
| [066. 一个 backtest Sharpe=3，你信吗？第一步做什么？](q066-一个-backtest-Sharpe=3-你信吗-第一步做什么.md) | ★★★ | Research skepticism｜audit｜Sharpe |
| [067. Walk-Forward Validation 怎么做？](q067-Walk-Forward-Validation-怎么做.md) | ★★☆ | OOS｜rolling｜expanding |
| [068. Alternative Data 有大量 missing values，怎么处理？](q068-Alternative-Data-有大量-missing-values-怎么处理.md) | ★★☆ | Missingness｜MNAR｜数据质量 |
| [069. 如何判断 improvement 是真 signal 还是 research overfitting？](q069-如何判断-improvement-是真-signal-还是-research-overfitting.md) | ★★★ | OOS｜ablation｜robustness |
| [070. 一个可复现 Quant Research Experiment 应保存什么？](q070-一个可复现-Quant-Research-Experiment-应保存什么.md) | ★★☆ | Reproducibility｜lineage｜MLOps |

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

- Bailey et al. 关于 backtest overfitting 的系列工作；López de Prado, *Advances in Financial Machine Learning*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
