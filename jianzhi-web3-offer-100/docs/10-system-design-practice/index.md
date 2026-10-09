# Chapter 10 - 系统设计与现场实战

高级 Web3 面试最终会回到软件工程：实现、审查、调试、可恢复性、幂等性、账本、一致性和安全边界。

## 本章能力目标

- 先澄清 functional / non-functional requirements，再画数据流和用户可见状态机。
- 列资产不变量和信任边界，再决定链上/链下边界、升级与权限模型。
- 故障设计覆盖 timeout、retry、idempotency、reorg、replacement、backfill、灾备和降级。
- 最后才谈吞吐、缓存、分片与成本；Staff 级答案必须给 observability 和 runbook。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- 前九章的状态、安全、DeFi 与 infra 基础
- 幂等、事务、队列、缓存、数据库与 SRE 基础
- 威胁建模与可观测性

### 统一分析模型

系统设计题先分离 `On-chain source of truth`、`Off-chain orchestration` 和 `Derived read model`。然后画资产流、状态机、信任边界和失败恢复路径；最后才讨论具体数据库、队列或框架。

### 从基础到高级的学习顺序

- **建立模型**：Q92、Q96、Q91 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q97、Q98、Q100 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 故障注入：RPC/DB/queue/worker 重启与网络分区
- [ ] 幂等与 exactly-once-like 行为验证
- [ ] reorg/backfill/replay 的恢复演练
- [ ] 容量、延迟、资金安全和权限边界的压测/攻防测试
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q91 | [Coding：实现一个 Mini ERC-20 Staking Contract，怎样从 O(N) 奖励更新到 O(1)？](q91.md) | ★★★★ | ★★★★★ | Solidity/DeFi | 104 |
| Q92 | [Coding Review：看到一个 Withdraw 函数，如何快速审查？](q92.md) | ★★★ | ★★★★★ | Solidity/安全 | 105 |
| Q93 | [System Design：设计一个 NFT Marketplace。](q93.md) | ★★★★ | ★★★★★ | Solidity/全栈 | 106 |
| Q94 | [System Design：设计 DAO Governance System。](q94.md) | ★★★★ | ★★★★★ | Governance/Protocol | 107 |
| Q95 | [System Design：设计 Multi-sig Wallet。](q95.md) | ★★★★ | ★★★★★ | Wallet/Solidity | 108 |
| Q96 | [System Design：设计 Token Vesting Contract。](q96.md) | ★★★ | ★★★★☆ | Solidity | 109 |
| Q97 | [System Design：设计高可靠 Blockchain Indexing Service。](q97.md) | ★★★★★ | ★★★★★ | Backend/Staff | 110 |
| Q98 | [System Design：设计中心化交易平台 Deposit System。](q98.md) | ★★★★★ | ★★★★★ | Backend/Exchange | 111 |
| Q99 | [Debug：用户说“交易失败了”，你如何系统排查？](q99.md) | ★★★★ | ★★★★★ | 全栈/Support/Senior | 112 |
| Q100 | [Staff 题：从用户点击按钮到链上结算，设计完整 Web3 Protocol。](q100.md) | ★★★★★ | ★★★★★ | Staff/Protocol/全栈 | 113 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)