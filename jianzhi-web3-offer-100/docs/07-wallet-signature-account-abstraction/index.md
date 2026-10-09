# Chapter 07 - 钱包、签名与 Account Abstraction

钱包题的本质是授权系统设计：谁能签、签什么、签名能否重放、谁付 gas、账户如何恢复和限制权限。

## 本章能力目标

- 把授权、执行和付费分开：谁证明“可以做”、谁真正执行、谁承担 gas。
- 所有签名问题默认检查 domain、chainId、verifying contract、nonce、deadline 与 action-specific fields。
- Smart wallet 设计不仅是 UX，还要包含 recovery、session key、module/plugin 权限和升级路径。
- ERC-4337 与 EIP-7702 要从“基础设施路线 vs protocol-level delegation”理解，而不是当作同一东西。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- ECDSA/签名验证基础
- nonce、domain separation 与 replay protection
- EOA、smart account 与 transaction lifecycle

### 统一分析模型

钱包题统一拆成 `Intent → Authorization → Validation → Execution → Gas Payment → Recovery`。签名只是 authorization 的一种载体；真正安全边界由 domain、nonce、权限范围、过期时间和执行上下文共同决定。

### 从基础到高级的学习顺序

- **建立模型**：Q61、Q62、Q63 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q69、Q70、Q67 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] 错误 chainId/domain/nonce/deadline 的签名拒绝测试
- [ ] 批处理部分失败与原子性测试
- [ ] recovery/module/session-key 撤销与过期
- [ ] bundler/paymaster 拒绝、超时、gas 边界测试
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q61 | [EOA 与 Smart Contract Account 有什么区别？](q61.md) | ★★ | ★★★★★ | 钱包/AA/全栈 | 71 |
| Q62 | [ecrecover 做什么？有哪些安全注意事项？](q62.md) | ★★★ | ★★★★☆ | Solidity/钱包/安全 | 72 |
| Q63 | [什么是 Signature Replay Attack？](q63.md) | ★★★ | ★★★★★ | 钱包/安全/DeFi | 73 |
| Q64 | [EIP-712 解决什么问题？](q64.md) | ★★★ | ★★★★★ | 钱包/前端/Solidity | 74 |
| Q65 | [ERC-2612 Permit 是什么？](q65.md) | ★★★ | ★★★★☆ | DeFi/钱包 | 75 |
| Q66 | [Account Abstraction 解决哪些 UX 与安全问题？](q66.md) | ★★★ | ★★★★★ | 钱包/产品/协议 | 76 |
| Q67 | [ERC-4337 的 UserOperation 与 EntryPoint 流程是什么？](q67.md) | ★★★★ | ★★★★★ | AA/钱包/协议 | 77 |
| Q68 | [ERC-4337 Paymaster 是做什么的？](q68.md) | ★★★★ | ★★★★☆ | AA/钱包 | 78 |
| Q69 | [EIP-7702 与 ERC-4337 是什么关系？](q69.md) | ★★★★★ | ★★★★★ | AA/高级 Ethereum | 79 |
| Q70 | [如何设计一个生产级 Smart Wallet？](q70.md) | ★★★★★ | ★★★★★ | 钱包/Staff | 80 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)