# Chapter 03 - Solidity 工程：语言语义、ABI 与 Gas

这一章不考“会不会写语法”，而是考语言语义在 EVM 上的成本、安全后果与接口边界。

## 本章能力目标

- 先讲 Solidity 语言语义，再落到 ABI/EVM；面试官通常希望看到你知道“编译器帮你做了什么”。
- 每个优化都要给安全边界：是否改变可读性、外部行为、overflow 语义、token compatibility。
- 生产合约回答要带版本意识：compiler、OpenZeppelin major version、optimizer/via-IR 都可能影响行为与布局。
- 测试策略至少覆盖 unit、fuzz、invariant 和 fork integration。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- Solidity data location 与 ABI
- ERC 标准及 token 行为差异
- compiler checks、revert 与 event

### 统一分析模型

回答 Solidity 题时把“语言表面规则”下沉到 EVM：参数最终如何编码、状态变量落在哪个 slot、external call 产生什么 call frame、失败时哪些状态会回滚。这样才能解释 gas 与安全后果。

### 从基础到高级的学习顺序

- **建立模型**：Q22、Q21、Q23 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q26、Q28、Q30 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 边界值：0、1、max、空数组、重复调用
- [ ] fuzz ABI 输入与权限边界
- [ ] event 与 state transition 一致性断言
- [ ] gas regression + stateful invariant testing
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q21 | [public / external / internal / private 有什么区别？](q21.md) | ★★ | ★★★★★ | Solidity | 27 |
| Q22 | [view 与 pure 有什么区别？](q22.md) | ★ | ★★★★☆ | Solidity | 28 |
| Q23 | [receive() 与 fallback() 有什么区别？](q23.md) | ★★ | ★★★★★ | Solidity/Proxy | 29 |
| Q24 | [Solidity 0.8 之后为什么还会使用 unchecked？](q24.md) | ★★ | ★★★★☆ | Solidity/Gas | 30 |
| Q25 | [immutable 与 constant 有什么区别？](q25.md) | ★★ | ★★★★☆ | Solidity/Gas | 31 |
| Q26 | [Event 为什么通常比 storage 便宜？什么时候不能用 Event 替代 Storage？](q26.md) | ★★★ | ★★★★★ | Solidity/后端 | 32 |
| Q27 | [Custom Error 为什么比 revert string 更适合生产合约？](q27.md) | ★★ | ★★★★☆ | Solidity/Gas | 33 |
| Q28 | [ERC-20 Allowance Race Condition 是什么？](q28.md) | ★★★ | ★★★★★ | Solidity/DeFi/安全 | 34 |
| Q29 | [ERC-721 与 ERC-1155 的核心区别是什么？](q29.md) | ★★ | ★★★★☆ | Solidity/NFT | 35 |
| Q30 | [如何系统做 Solidity Gas Optimization？](q30.md) | ★★★ | ★★★★★ | Solidity/高级 | 36 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)