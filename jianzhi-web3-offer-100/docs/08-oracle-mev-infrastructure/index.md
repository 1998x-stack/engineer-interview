# Chapter 08 - Oracle、MEV 与 Web3 基础设施

合约不是孤岛。真实系统依赖 oracle、mempool、RPC、node、indexer 和数据库；基础设施错误同样会导致资金与账本事故。

## 本章能力目标

- Web3 基础设施首先是分布式系统：timeout、retry、idempotency、backfill、canonicality、observability 一个都不能少。
- 链上成功与产品成功是两套状态机；RPC、indexer、DB 和 UI 都可能滞后或产生局部错误。
- 涉及 mempool/MEV 时要显式讨论信息泄露、排序权和竞争条件。
- 读链数据时永远保留 block number + block hash；只存高度不足以安全处理 reorg。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- 节点/RPC 与 canonical chain
- mempool 与交易排序
- 事件日志、索引器与外部数据源

### 统一分析模型

Infra 题要区分“链上共识事实”和“应用派生视图”。RPC、Indexer、Oracle 都是把底层状态暴露给上层的基础设施，但它们有不同一致性、可用性和信任模型。

### 从基础到高级的学习顺序

- **建立模型**：Q71、Q76、Q72 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q79、Q72、Q73 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 多 RPC 分歧与故障注入
- [ ] reorg rollback/replay/idempotency
- [ ] oracle stale/deviation/source-down 场景
- [ ] private/public submission 路径与顺序敏感仿真
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q71 | [为什么智能合约不能直接请求普通 HTTP API？](q71.md) | ★★ | ★★★★★ | 全栈/Oracle | 82 |
| Q72 | [一个可靠 Oracle 应具备哪些性质？](q72.md) | ★★★ | ★★★★★ | DeFi/安全 | 83 |
| Q73 | [什么是 MEV？](q73.md) | ★★★ | ★★★★★ | 协议/DeFi/Infra | 84 |
| Q74 | [Front-running、Back-running、Sandwich 在机制上如何区分？](q74.md) | ★★★ | ★★★★☆ | DeFi/安全 | 85 |
| Q75 | [为什么 Public Mempool 会产生独特安全问题？](q75.md) | ★★★ | ★★★★☆ | 后端/DeFi | 86 |
| Q76 | [JSON-RPC 在 Web3 架构中是什么？](q76.md) | ★★ | ★★★★★ | 后端/全栈 | 87 |
| Q77 | [Archive Node、Full Node、Light Client 有什么区别？](q77.md) | ★★★ | ★★★★☆ | Infra/后端 | 88 |
| Q78 | [为什么 Web3 应用通常需要 Indexer？](q78.md) | ★★★ | ★★★★★ | 后端/全栈 | 89 |
| Q79 | [Indexer 如何正确处理 Chain Reorg？](q79.md) | ★★★★ | ★★★★★ | 后端/交易所 | 90 |
| Q80 | [RPC Provider 挂了，生产 dApp 应如何降级？](q80.md) | ★★★ | ★★★★★ | 全栈/Infra | 91 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)