# F. 市场微观结构

> **模块目标**：市场微观结构  
> **统一方法**：把价格看成由撮合、队列、订单流和信息不对称共同产生的随机过程；所有短周期信号都必须和 execution、latency、queue position 一起分析。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 从 order book/queue 解释短期价格
- 理解 fill/adverse selection/impact/latency
- 把信号研究和执行模型绑定

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
| [051. Bid、Ask、Mid、Spread 分别是什么？为什么 last price 可能不如 mid？](q051-Bid-Ask-Mid-Spread-分别是什么-为什么-last-price-可能不如-mid.md) | ★☆☆ | Microstructure｜quote｜price |
| [052. 什么是 Bid-Ask Bounce？](q052-什么是-Bid-Ask-Bounce.md) | ★★☆ | Microstructure noise｜短期自相关 |
| [053. 什么是 Adverse Selection？](q053-什么是-Adverse-Selection.md) | ★★☆ | Conditional probability｜information｜microstructure |
| [054. Order Book Imbalance 如何定义？为什么不能把它当永恒预测信号？](q054-Order-Book-Imbalance-如何定义-为什么不能把它当永恒预测信号.md) | ★★☆ | LOB｜imbalance｜state feature |
| [055. Price-Time Priority 是什么？](q055-Price-Time-Priority-是什么.md) | ★☆☆ | Matching engine｜queue｜priority |
| [056. 为什么 Fill Probability 是 execution simulation 的关键？](q056-为什么-Fill-Probability-是-execution-simulation-的关键.md) | ★★☆ | Execution model｜queue｜simulation bias |
| [057. Market Impact 的 temporary 与 permanent 如何理解？](q057-Market-Impact-的-temporary-与-permanent-如何理解.md) | ★★☆ | Impact｜execution cost｜information |
| [058. Tick Size 为什么会改变市场行为？](q058-Tick-Size-为什么会改变市场行为.md) | ★★☆ | Tick size｜queue competition｜liquidity |
| [059. 什么是 Microprice？为什么可能不同于 Mid？](q059-什么是-Microprice-为什么可能不同于-Mid.md) | ★★☆ | Microprice｜imbalance｜short-horizon state |
| [060. Latency 为什么既是系统问题，也是统计问题？](q060-Latency-为什么既是系统问题-也是统计问题.md) | ★★☆ | Latency｜signal decay｜distribution |

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

- Hasbrouck, *Empirical Market Microstructure*；Harris, *Trading and Exchanges*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
