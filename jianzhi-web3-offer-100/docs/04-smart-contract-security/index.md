# Chapter 04 - 智能合约安全：从漏洞列表到 Invariant

真正的安全面试不是背 SWC 编号，而是识别资产、信任边界、状态不变量、外部调用和经济假设。

## 本章能力目标

- 先列资产与不变量，再列可调用入口和 privileged roles；漏洞名称只是后续分类。
- 外部调用前后检查状态：可重入点、callback/hook、delegatecall、token fallback 都属于攻击面。
- 经济安全和代码安全一起看：oracle、liquidity、rounding、MEV、flash liquidity 都可能打破业务假设。
- 审计结论需要 severity、可利用前提、影响范围、PoC 思路和 mitigation，而不是只说“有风险”。

<!-- CHAPTER_ENRICHMENT_START -->
## 本章专业学习框架

### 前置知识
- 资产与不变量建模
- EVM external call / delegatecall
- oracle、token hook、upgradeability 基础

### 统一分析模型

安全题统一使用 `Assets → Entry Points → State Transitions → External Interactions → Privileged Roles → Invariants` 六步模型。漏洞名称只是分类结果，真正目标是证明攻击者能让某个 invariant 失效。

### 从基础到高级的学习顺序

- **建立模型**：Q31、Q32、Q34 —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：Q40、Q38、Q39 —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

- [ ] stateful fuzz / invariant：资产守恒、权限、份额/债务关系
- [ ] adversarial callback 合约测试重入与 hook
- [ ] fork test 模拟真实 oracle/liquidity/token 行为
- [ ] upgrade、pause、recovery 等 privileged path 单独测试
<!-- CHAPTER_ENRICHMENT_END -->




## 题目列表

| 题号 | 题目 | 难度 | 高频度 | 岗位 | PDF 页 |
|---|---|---:|---:|---|---:|
| Q31 | [什么是 Reentrancy？](q31.md) | ★★ | ★★★★★ | Solidity/安全/DeFi | 38 |
| Q32 | [Checks-Effects-Interactions 为什么有效？](q32.md) | ★★ | ★★★★★ | Solidity/安全 | 39 |
| Q33 | [ReentrancyGuard 是否解决所有 Reentrancy？](q33.md) | ★★★ | ★★★★★ | 安全/DeFi | 40 |
| Q34 | [为什么不能使用 tx.origin 做 Authorization？](q34.md) | ★★ | ★★★★★ | Solidity/安全 | 41 |
| Q35 | [Oracle Manipulation 的根因是什么？](q35.md) | ★★★ | ★★★★★ | DeFi/安全 | 42 |
| Q36 | [Flash Loan 为什么不是漏洞本身？](q36.md) | ★★★ | ★★★★★ | DeFi/安全 | 43 |
| Q37 | [Access Control 应如何设计？](q37.md) | ★★★ | ★★★★★ | Solidity/安全/治理 | 44 |
| Q38 | [Transparent Proxy 与 UUPS Proxy 有什么区别？](q38.md) | ★★★★ | ★★★★★ | Solidity/高级/安全 | 45 |
| Q39 | [Upgradeable Contract 为什么不能随便改变 State Variable 顺序？](q39.md) | ★★★★ | ★★★★★ | Solidity/Proxy/安全 | 46 |
| Q40 | [给你一份 200 行 Solidity 合约，如何系统做 Security Review？](q40.md) | ★★★★★ | ★★★★★ | 安全/Senior/Protocol | 47 |

## 建议学习方式

1. 第一遍只读每题的 **30 秒标准回答 + 记忆锚点**。
2. 第二遍关闭答案，手画白板图并口述“定义 -> 原理 -> Failure Mode -> Mitigation”。
3. 第三遍只做追问、自测题和测试清单。
4. Core 30 题必须达到能在 2-5 分钟内连续深挖的程度。

[← 返回总目录](../index.md)