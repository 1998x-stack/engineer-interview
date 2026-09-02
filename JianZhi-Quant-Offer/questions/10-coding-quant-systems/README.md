# J. Coding、算法与量化系统

> **模块目标**：算法与量化系统  
> **统一方法**：同时回答正确性、复杂度、内存/缓存行为、时间戳语义、幂等性和 replay；量化系统的核心是状态正确性与可重现。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 掌握 streaming/top-k/heap/as-of join
- 理解 event state、timestamp、cache locality
- 构建 replay/parity/production-grade 诊断能力

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
| [091. 长度 N 的序列，如何 O(N) 计算 rolling mean？](q091-长度-N-的序列-如何-O-N-计算-rolling-mean.md) | ★☆☆ | Sliding window｜算法｜streaming |
| [092. Streaming 数据中实时维护 median 怎么做？](q092-Streaming-数据中实时维护-median-怎么做.md) | ★★☆ | Heap｜streaming median｜DSA |
| [093. 十亿行数据只找最大的 1000 个元素，如何做？](q093-十亿行数据只找最大的-1000-个元素-如何做.md) | ★☆☆ | Top-K｜heap｜large data |
| [094. 如何实现 event-driven order-book reconstruction？](q094-如何实现-event-driven-order-book-reconstruction.md) | ★★★ | State machine｜hash map｜ordered map |
| [095. 给无序 trade events，如何检测 timestamp 问题？](q095-给无序-trade-events-如何检测-timestamp-问题.md) | ★★☆ | Timestamp｜clock｜data QA |
| [096. SQL 中如何做 As-Of Join？](q096-SQL-中如何做-As-Of-Join.md) | ★★☆ | SQL｜time series join｜point-in-time |
| [097. 为什么 NumPy 通常比 Python for-loop 快？](q097-为什么-NumPy-通常比-Python-for-loop-快.md) | ★★☆ | Vectorization｜memory｜Python runtime |
| [098. C++ Quant/HFT 面试为什么常问 cache locality？](q098-C++-Quant-HFT-面试为什么常问-cache-locality.md) | ★★☆ | CPU cache｜data layout｜latency |
| [099. Research code 与 production code 最大区别是什么？](q099-Research-code-与-production-code-最大区别是什么.md) | ★★☆ | Software engineering｜research-to-prod |
| [100. 压轴：Backtest 与 Live 表现差异巨大，如何系统定位？](q100-压轴-Backtest-与-Live-表现差异巨大-如何系统定位.md) | ★★★ | 系统诊断｜research parity｜distribution shift |

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

- Kleppmann, *Designing Data-Intensive Applications*；Bryant & O’Hallaron, *Computer Systems: A Programmer’s Perspective*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
