# Chapter 02 - Ethereum / EVM：从交易到状态转换

本章是 Solidity 岗位的地基：你需要能从 calldata、opcode、storage slot 一直追到整笔交易状态转换。

## 本章能力目标

- 沿着 `transaction -> calldata -> call frame -> opcode -> storage/log -> receipt` 推导，尽量能落到字节级。
- 明确执行上下文：`msg.sender`、`msg.value`、`address(this)`、storage owner、delegatecall context。
- 对 gas 问题先区分执行成本、持久状态成本和 calldata/data-availability 成本。
- 调试时优先使用 trace、raw calldata、storage slot 与 revert data，而不是只看 Solidity 源码表象。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- EVM call frame、stack/memory/storage
- ABI 编码与 calldata
- transaction、gas、receipt 与 state root

### 统一分析模型

把 EVM 看成带 gas 预算的确定性状态机：每个 opcode 同时更新机器状态（pc/stack/memory）和可能的世界状态；外部调用会创建新的 call frame，而 `DELEGATECALL` 等指令改变代码与存储上下文的组合方式。

### 从基础到高级的学习顺序

- **建立模型**：Q11、Q13、Q15 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q19、Q20、Q12 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] Foundry/Hardhat 单元测试覆盖 call/revert/return data
- [ ] storage slot 断言与 upgrade layout diff
- [ ] gas snapshot 只作为回归信号，不作为安全证明
- [ ] fork test 验证真实主网依赖与边界条件
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q11 | [EVM 是什么？](q11.md) | ★★ | ★★★★★ | Solidity/协议/安全 | 16 |
| Q12 | [Stack / Memory / Storage / Transient Storage 有什么区别？](q12.md) | ★★★ | ★★★★★ | Solidity/安全 | 17 |
| Q13 | [Solidity 的 storage、memory、calldata 有什么区别？](q13.md) | ★★ | ★★★★★ | Solidity | 18 |
| Q14 | [CALL 与 DELEGATECALL 有什么区别？](q14.md) | ★★★ | ★★★★★ | Solidity/安全/Proxy | 19 |
| Q15 | [ABI Function Selector 和 calldata 如何编码？](q15.md) | ★★ | ★★★★☆ | Solidity/后端/安全 | 20 |
| Q16 | [Mapping 在 EVM Storage 中如何定位？](q16.md) | ★★★ | ★★★★★ | Solidity/安全 | 21 |
| Q17 | [CREATE 与 CREATE2 有什么区别？](q17.md) | ★★★ | ★★★★☆ | Solidity/钱包/协议 | 22 |
| Q18 | [EIP-1559 的费用机制如何工作？](q18.md) | ★★★ | ★★★★★ | 后端/钱包/协议 | 23 |
| Q19 | [EIP-1153 Transient Storage 解决了什么？](q19.md) | ★★★★ | ★★★☆☆ | EVM/高级 Solidity | 24 |
| Q20 | [一笔 Ethereum Transaction 从钱包到 Finality 经历什么？](q20.md) | ★★★★ | ★★★★★ | 全栈/后端/协议 | 25 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)