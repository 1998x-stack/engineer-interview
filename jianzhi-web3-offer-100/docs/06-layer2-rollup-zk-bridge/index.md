# Chapter 06 - Layer2、Rollup、ZK 与 Bridge

扩容题要按 execution、data availability、settlement、proof、sequencing 五层拆解。只说“L2 更快更便宜”远远不够。

## 本章能力目标

- 先画安全模型：执行在哪里、数据在哪里、证明/挑战在哪里验证、最终结算在哪里。
- 区分 L2 inclusion、batch publication、L1 inclusion、L1 finality 和 withdrawal finality。
- 任何桥或 rollup 设计都要问：数据不可用、sequencer 离线、prover/challenger 失败时用户如何退出。
- 升级权限、pause/guardian、proof system 和 DA committee 都是 trust boundary。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- L1 execution/consensus/finality
- state root 与 Merkle commitment
- data availability、proof 与 bridge trust model

### 统一分析模型

Rollup 题至少拆成四层：`Execution → State Commitment/Proof → Data Availability → Settlement/Finality`。Bridge 再额外加入“跨域消息真实性如何验证”。不要把低费用、proof 和 DA 混成一个概念。

### 从基础到高级的学习顺序

- **建立模型**：Q51、Q52、Q53 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q60、Q54、Q55 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] batch/proof/challenge 的状态机测试
- [ ] sequencer/prover/batcher 停机演练
- [ ] L1 reorg 与 delayed message 重放测试
- [ ] bridge message nonce/domain/source chain 验证
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q51 | [为什么 Ethereum 需要 Layer2？](q51.md) | ★★ | ★★★★★ | 全岗位 | 60 |
| Q52 | [Optimistic Rollup 的工作原理是什么？](q52.md) | ★★★ | ★★★★★ | L2/协议 | 61 |
| Q53 | [ZK Rollup 与 Optimistic Rollup 的核心区别？](q53.md) | ★★★ | ★★★★★ | L2/ZK | 62 |
| Q54 | [EIP-4844 为什么对 Rollup 重要？](q54.md) | ★★★★ | ★★★★★ | L2/Ethereum | 63 |
| Q55 | [Data Availability 到底是什么意思？](q55.md) | ★★★★ | ★★★★★ | L2/协议 | 64 |
| Q56 | [Sequencer 是什么？中心化 Sequencer 有哪些风险？](q56.md) | ★★★ | ★★★★★ | L2/后端 | 65 |
| Q57 | [Validium 与 ZK Rollup 有什么区别？](q57.md) | ★★★★ | ★★★★☆ | L2/ZK | 66 |
| Q58 | [为什么 Bridge 是 Web3 高风险组件？](q58.md) | ★★★ | ★★★★★ | 跨链/安全 | 67 |
| Q59 | [ZK Proof 的 Completeness、Soundness、Zero-Knowledge 分别是什么？](q59.md) | ★★★★ | ★★★★☆ | ZK/研究 | 68 |
| Q60 | [设计一个 Rollup 需要哪些核心组件？](q60.md) | ★★★★★ | ★★★★★ | L2/Staff | 69 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)