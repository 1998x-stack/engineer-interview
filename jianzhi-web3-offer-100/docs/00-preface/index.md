# 编写说明与能力地图

[封面信息](cover.md)

> 本仓库是 PDF **《剑指 Web3 Offer：100 道真题级面试题 · 2026》** 的 GitHub 化、扩展版。PDF 原始内容完整保留为每题主干，GitHub 版额外增加工程化分析、测试清单、交叉链接和扩展阅读。

## 编写口径

- 采用问题驱动的面试学习结构：先给面试场景下的短回答，再展开底层原理、工程边界、追问和常见误区。
- 组织思路参考《剑指 Offer》所代表的“以问题带知识点”学习范式，但不复制其原文、题目、图表或版式细节。
- “真题级”表示题目来自 Web3 岗位公开面试模式中反复出现的能力类型，并结合主流协议栈构造成可直接用于真实面试的问法；不把未经公开证实的问题标成某家公司的特定原题。
- 技术口径以 PDF 的 **2026-09** 版本为基础。GitHub 扩展阅读在构建仓库时再次对官方 EVM、EIP-1153、EIP-4844、ERC-4337、EIP-7702、OpenZeppelin 与 Solana 文档做了核验。

原 PDF：[下载/查看](../../assets/pdf/Jianzhi_Web3_Offer_100_Interview_Questions_2026.pdf)

## 使用建议

第一次阅读先掌握每题的“30 秒回答 + 记忆锚点”；第二轮补齐“深入解析 + 高频追问”；冲刺轮只刷五星高频题和系统设计题。

## 面试评分模型

| 层级 | 面试表现 | 面试官判断 | 目标 |
|---|---|---|---|
| L1 定义 | 能解释名词 | 基础了解 | 不丢基础分 |
| L2 原理 | 能推导为什么 | 真正理解 | 通过普通工程面 |
| L3 Failure Mode | 主动说边界/攻击面 | 有生产经验 | 高级工程师 |
| L4 Invariant/System | 能抽象状态机与信任边界 | Protocol/Staff 水平 | 系统设计与终面 |

## Web3 面试能力地图

| 层级 | 能力域 | 关键点 |
|---|---|---|
| 底层 | Blockchain / EVM | 状态、交易、Gas、Storage、ABI |
| 合约 | Solidity / Security | 权限、重入、Proxy、Invariant |
| 协议 | DeFi / L2 / Bridge | AMM、Lending、DA、Proof、Sequencer |
| 账户 | Wallet / AA / Multi-chain | 签名、Replay、4337、7702、PDA |
| 系统 | RPC / Indexer / Ledger | Reorg、幂等、账本、可靠性、调试 |

> 一个可靠的高级回答通常遵循：**定义 -> 原理 -> Failure Mode -> Mitigation -> Invariant / Trade-off**。
