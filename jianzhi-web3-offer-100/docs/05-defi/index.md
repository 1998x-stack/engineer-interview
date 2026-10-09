# Chapter 05 - DeFi：AMM、Lending 与经济不变量

DeFi 面试看的是“公式如何成为资金状态机”。你需要从定价曲线、份额 accounting、清算与 oracle 风险推导系统行为。

## 本章能力目标

- 所有 DeFi 数学先标单位与 decimals，再讨论公式；很多事故来自单位、方向和舍入，而不是高深数学。
- 把协议写成 accounting invariants，例如 assets、shares、debt、collateral、fees 的守恒关系。
- 把 oracle、liquidity、liquidation 和 MEV 当作同一经济系统的一部分分析。
- 极端场景要覆盖低流动性、价格跳跃、拥堵、坏账、token 非标准行为和治理参数变化。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- token accounting 与 decimals
- AMM 定价/套利直觉
- oracle、抵押、清算与风险参数

### 统一分析模型

DeFi 题先写资产负债表和不变量：谁的资产进入协议、协议欠谁什么、价格从哪里来、何时允许价值转移。随后再讨论曲线、利率或清算参数，否则公式容易脱离经济语义。

### 从基础到高级的学习顺序

- **建立模型**：Q41、Q42、Q47 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q50、Q45、Q43 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 价格跳变、流动性枯竭、极端 decimals 的 fuzz
- [ ] 资产/份额/债务守恒 invariant
- [ ] 清算边界前后与 oracle stale 场景
- [ ] MEV/顺序敏感模拟和 fork-based integration test
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q41 | [Uniswap V2 为什么使用 x*y=k？](q41.md) | ★★ | ★★★★★ | DeFi/Solidity | 49 |
| Q42 | [Slippage 与 Price Impact 有什么区别？](q42.md) | ★★ | ★★★★★ | DeFi/前端 | 50 |
| Q43 | [什么是 Impermanent Loss？](q43.md) | ★★★ | ★★★★☆ | DeFi | 51 |
| Q44 | [Uniswap V3 Concentrated Liquidity 解决了什么问题？](q44.md) | ★★★ | ★★★★★ | DeFi/协议 | 52 |
| Q45 | [Uniswap V3 Tick 与 sqrtPriceX96 是什么？](q45.md) | ★★★★ | ★★★★☆ | DeFi/高级 | 53 |
| Q46 | [Lending Protocol 的 Health Factor 是什么？](q46.md) | ★★★ | ★★★★★ | DeFi/后端 | 54 |
| Q47 | [为什么 DeFi Lending 通常需要 Over-collateralization？](q47.md) | ★★ | ★★★★☆ | DeFi | 55 |
| Q48 | [Liquidation 的经济机制是什么？](q48.md) | ★★★ | ★★★★★ | DeFi/安全/后端 | 56 |
| Q49 | [Stablecoin 有哪些主要设计与 Failure Modes？](q49.md) | ★★★ | ★★★★☆ | DeFi/协议 | 57 |
| Q50 | [设计 DeFi Protocol 时最重要的 Invariant 是什么？](q50.md) | ★★★★★ | ★★★★★ | Protocol/Senior | 58 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)