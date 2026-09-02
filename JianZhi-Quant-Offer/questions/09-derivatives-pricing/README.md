# I. 衍生品与定价

> **模块目标**：衍生品与定价  
> **统一方法**：从 no-arbitrage、复制和 risk-neutral valuation 出发，而不是死背公式；明确 Greeks 是局部敏感度，现实中还有离散对冲、微笑、跳跃和交易摩擦。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 从复制与无套利推导核心关系
- 理解 Greeks、IV 与 volatility surface
- 理解模型错设与离散对冲误差

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
| [081. Put-Call Parity 是什么？如何从无套利推导？](q081-Put-Call-Parity-是什么-如何从无套利推导.md) | ★★☆ | Options｜no-arbitrage｜parity |
| [082. Black-Scholes 的核心假设是什么？哪些明显不现实？](q082-Black-Scholes-的核心假设是什么-哪些明显不现实.md) | ★★☆ | Black-Scholes｜assumptions｜model risk |
| [083. 为什么 Black-Scholes PDE 中真实 drift μ 消失？](q083-为什么-Black-Scholes-PDE-中真实-drift-μ-消失.md) | ★★★ | Risk-neutral pricing｜delta hedge｜PDE |
| [084. Delta 是什么？它是不是“期权上涨概率”？](q084-Delta-是什么-它是不是“期权上涨概率”.md) | ★★☆ | Greeks｜Delta｜sensitivity |
| [085. Gamma 为什么重要？](q085-Gamma-为什么重要.md) | ★★☆ | Greeks｜convexity｜hedging error |
| [086. Vega 是什么？为什么 vanilla option 通常 Vega>0？](q086-Vega-是什么-为什么-vanilla-option-通常-Vega-0.md) | ★★☆ | Greeks｜volatility｜convexity |
| [087. Implied Volatility 如何从期权价格反求？](q087-Implied-Volatility-如何从期权价格反求.md) | ★★☆ | Numerical methods｜IV｜root finding |
| [088. 为什么存在 Volatility Smile/Skew？](q088-为什么存在-Volatility-Smile-Skew.md) | ★★☆ | Vol surface｜fat tails｜model misspecification |
| [089. American 与 European Option 最大区别是什么？](q089-American-与-European-Option-最大区别是什么.md) | ★★☆ | Early exercise｜optimal stopping |
| [090. 为什么离散 Delta Hedging 不能完全复制连续理论？](q090-为什么离散-Delta-Hedging-不能完全复制连续理论.md) | ★★★ | Discrete hedging｜model risk｜P&L |

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

- Hull, *Options, Futures, and Other Derivatives*；Shreve, *Stochastic Calculus for Finance II*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
