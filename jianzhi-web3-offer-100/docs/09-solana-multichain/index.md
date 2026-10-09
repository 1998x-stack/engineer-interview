# Chapter 09 - Solana 与 Multi-chain：另一种执行模型

不要把 Solana 当“更快的 EVM”。它的 program/account 分离、显式账户列表、PDA/CPI 和并行执行模型带来完全不同的工程边界。

## 本章能力目标

- Solana 题先说清 `program` 与 `data account` 分离，再谈 signer/writable/owner 权限。
- PDA 问题要同时回答 derivation、off-curve、bump、创建账户和 `invoke_signed`。
- CPI 要检查 privilege propagation、account validation 与 reentrancy/composability。
- 并行性来自显式账户访问集合，而不是“Solana 天生所有交易并行”。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- Solana accounts/programs/instructions
- PDA/CPI/Signer 权限
- Ethereum 与 Solana transaction/state model 差异

### 统一分析模型

Solana 题用 `Program Code + Explicit Accounts + Runtime Ownership/Locks` 建模；多链题则抽象为统一 intent，但每条链保留独立的 address、fee、signing、finality、token 与 error semantics。

### 从基础到高级的学习顺序

- **建立模型**：Q82、Q83、Q81 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q90、Q86、Q89 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 错误 owner/signer/PDA seeds 的拒绝测试
- [ ] CPI 权限与 account aliasing
- [ ] 并发 writable account 冲突与 retry
- [ ] 跨链 mint/burn/lock accounting invariant
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q81 | [Ethereum 与 Solana 最大的编程模型区别是什么？](q81.md) | ★★★ | ★★★★★ | Multi-chain/Solana | 93 |
| Q82 | [Solana Account 是什么？](q82.md) | ★★ | ★★★★★ | Solana | 94 |
| Q83 | [为什么 Solana Program 通常被称为 Stateless？](q83.md) | ★★ | ★★★★☆ | Solana | 95 |
| Q84 | [什么是 PDA？为什么没有私钥？](q84.md) | ★★★ | ★★★★★ | Solana/钱包 | 96 |
| Q85 | [什么是 CPI？](q85.md) | ★★★ | ★★★★★ | Solana/DeFi | 97 |
| Q86 | [Solana 为什么更容易并行执行某些 Transactions？](q86.md) | ★★★★ | ★★★★★ | Solana/系统 | 98 |
| Q87 | [Ethereum 与 Solana Transaction Atomicity 有何异同？](q87.md) | ★★★ | ★★★★☆ | Multi-chain | 99 |
| Q88 | [为什么 Multi-chain dApp 比单链难很多？](q88.md) | ★★★ | ★★★★★ | 全栈/架构 | 100 |
| Q89 | [Multi-chain Token 如何保证 Total Supply Invariant？](q89.md) | ★★★★ | ★★★★★ | Bridge/Token/安全 | 101 |
| Q90 | [设计一个 Ethereum + Solana Wallet SDK。](q90.md) | ★★★★★ | ★★★★★ | Wallet/Staff/Multi-chain | 102 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)