# 《剑指 Web3 Offer》GitHub Edition

本仓库包含 PDF 全部 100 道题，每题一个 Markdown，并在 PDF 主干上增加工程化分析、测试清单、Mermaid 白板图、交叉引用和 2026 扩展阅读。

## 阅读入口

- [编写说明与能力地图](00-preface/index.md)
- [Core 30](11-appendix/core-30.md)
- [7 天冲刺计划](11-appendix/7-day-plan.md)
- [Security Checklist](11-appendix/security-review-checklist.md)
- [System Design Checklist](11-appendix/system-design-checklist.md)
- [References](references.md)

## 10 大章节

1. [Blockchain 基础与密码学直觉](01-blockchain-fundamentals/index.md) - Q01-Q10
2. [Ethereum / EVM：从交易到状态转换](02-ethereum-evm/index.md) - Q11-Q20
3. [Solidity 工程：语言语义、ABI 与 Gas](03-solidity/index.md) - Q21-Q30
4. [智能合约安全：从漏洞列表到 Invariant](04-smart-contract-security/index.md) - Q31-Q40
5. [DeFi：AMM、Lending 与经济不变量](05-defi/index.md) - Q41-Q50
6. [Layer2、Rollup、ZK 与 Bridge](06-layer2-rollup-zk-bridge/index.md) - Q51-Q60
7. [钱包、签名与 Account Abstraction](07-wallet-signature-account-abstraction/index.md) - Q61-Q70
8. [Oracle、MEV 与 Web3 基础设施](08-oracle-mev-infrastructure/index.md) - Q71-Q80
9. [Solana 与 Multi-chain：另一种执行模型](09-solana-multichain/index.md) - Q81-Q90
10. [系统设计与现场实战](10-system-design-practice/index.md) - Q91-Q100

## 100 题索引

| Q | 题目 | 章节 | 难度 | 高频度 | PDF 页 |
|---|---|---|---:|---:|---:|
| Q01 | [Blockchain 到底解决了什么问题？](01-blockchain-fundamentals/q01.md) | 01 | ★★ | ★★★★★ | 5 |
| Q02 | [UTXO 模型与 Account Model 有什么区别？](01-blockchain-fundamentals/q02.md) | 01 | ★★ | ★★★★☆ | 6 |
| Q03 | [Hash 在 Blockchain 中有哪些作用？](01-blockchain-fundamentals/q03.md) | 01 | ★★ | ★★★★☆ | 7 |
| Q04 | [Merkle Tree 为什么特别适合 Blockchain？](01-blockchain-fundamentals/q04.md) | 01 | ★★ | ★★★★★ | 8 |
| Q05 | [什么是区块链 Finality？](01-blockchain-fundamentals/q05.md) | 01 | ★★★ | ★★★★☆ | 9 |
| Q06 | [PoW 与 PoS 的本质差异是什么？](01-blockchain-fundamentals/q06.md) | 01 | ★★ | ★★★★☆ | 10 |
| Q07 | [Fork、Fork Choice 与 Hard Fork 有什么区别？](01-blockchain-fundamentals/q07.md) | 01 | ★★ | ★★★☆☆ | 11 |
| Q08 | [为什么区块链需要 Gas？](01-blockchain-fundamentals/q08.md) | 01 | ★★ | ★★★★★ | 12 |
| Q09 | [Private Key、Public Key、Address、Signature 的关系是什么？](01-blockchain-fundamentals/q09.md) | 01 | ★★ | ★★★★★ | 13 |
| Q10 | [为什么“Code is Law”并不完全成立？](01-blockchain-fundamentals/q10.md) | 01 | ★★★ | ★★★☆☆ | 14 |
| Q11 | [EVM 是什么？](02-ethereum-evm/q11.md) | 02 | ★★ | ★★★★★ | 16 |
| Q12 | [Stack / Memory / Storage / Transient Storage 有什么区别？](02-ethereum-evm/q12.md) | 02 | ★★★ | ★★★★★ | 17 |
| Q13 | [Solidity 的 storage、memory、calldata 有什么区别？](02-ethereum-evm/q13.md) | 02 | ★★ | ★★★★★ | 18 |
| Q14 | [CALL 与 DELEGATECALL 有什么区别？](02-ethereum-evm/q14.md) | 02 | ★★★ | ★★★★★ | 19 |
| Q15 | [ABI Function Selector 和 calldata 如何编码？](02-ethereum-evm/q15.md) | 02 | ★★ | ★★★★☆ | 20 |
| Q16 | [Mapping 在 EVM Storage 中如何定位？](02-ethereum-evm/q16.md) | 02 | ★★★ | ★★★★★ | 21 |
| Q17 | [CREATE 与 CREATE2 有什么区别？](02-ethereum-evm/q17.md) | 02 | ★★★ | ★★★★☆ | 22 |
| Q18 | [EIP-1559 的费用机制如何工作？](02-ethereum-evm/q18.md) | 02 | ★★★ | ★★★★★ | 23 |
| Q19 | [EIP-1153 Transient Storage 解决了什么？](02-ethereum-evm/q19.md) | 02 | ★★★★ | ★★★☆☆ | 24 |
| Q20 | [一笔 Ethereum Transaction 从钱包到 Finality 经历什么？](02-ethereum-evm/q20.md) | 02 | ★★★★ | ★★★★★ | 25 |
| Q21 | [public / external / internal / private 有什么区别？](03-solidity/q21.md) | 03 | ★★ | ★★★★★ | 27 |
| Q22 | [view 与 pure 有什么区别？](03-solidity/q22.md) | 03 | ★ | ★★★★☆ | 28 |
| Q23 | [receive() 与 fallback() 有什么区别？](03-solidity/q23.md) | 03 | ★★ | ★★★★★ | 29 |
| Q24 | [Solidity 0.8 之后为什么还会使用 unchecked？](03-solidity/q24.md) | 03 | ★★ | ★★★★☆ | 30 |
| Q25 | [immutable 与 constant 有什么区别？](03-solidity/q25.md) | 03 | ★★ | ★★★★☆ | 31 |
| Q26 | [Event 为什么通常比 storage 便宜？什么时候不能用 Event 替代 Storage？](03-solidity/q26.md) | 03 | ★★★ | ★★★★★ | 32 |
| Q27 | [Custom Error 为什么比 revert string 更适合生产合约？](03-solidity/q27.md) | 03 | ★★ | ★★★★☆ | 33 |
| Q28 | [ERC-20 Allowance Race Condition 是什么？](03-solidity/q28.md) | 03 | ★★★ | ★★★★★ | 34 |
| Q29 | [ERC-721 与 ERC-1155 的核心区别是什么？](03-solidity/q29.md) | 03 | ★★ | ★★★★☆ | 35 |
| Q30 | [如何系统做 Solidity Gas Optimization？](03-solidity/q30.md) | 03 | ★★★ | ★★★★★ | 36 |
| Q31 | [什么是 Reentrancy？](04-smart-contract-security/q31.md) | 04 | ★★ | ★★★★★ | 38 |
| Q32 | [Checks-Effects-Interactions 为什么有效？](04-smart-contract-security/q32.md) | 04 | ★★ | ★★★★★ | 39 |
| Q33 | [ReentrancyGuard 是否解决所有 Reentrancy？](04-smart-contract-security/q33.md) | 04 | ★★★ | ★★★★★ | 40 |
| Q34 | [为什么不能使用 tx.origin 做 Authorization？](04-smart-contract-security/q34.md) | 04 | ★★ | ★★★★★ | 41 |
| Q35 | [Oracle Manipulation 的根因是什么？](04-smart-contract-security/q35.md) | 04 | ★★★ | ★★★★★ | 42 |
| Q36 | [Flash Loan 为什么不是漏洞本身？](04-smart-contract-security/q36.md) | 04 | ★★★ | ★★★★★ | 43 |
| Q37 | [Access Control 应如何设计？](04-smart-contract-security/q37.md) | 04 | ★★★ | ★★★★★ | 44 |
| Q38 | [Transparent Proxy 与 UUPS Proxy 有什么区别？](04-smart-contract-security/q38.md) | 04 | ★★★★ | ★★★★★ | 45 |
| Q39 | [Upgradeable Contract 为什么不能随便改变 State Variable 顺序？](04-smart-contract-security/q39.md) | 04 | ★★★★ | ★★★★★ | 46 |
| Q40 | [给你一份 200 行 Solidity 合约，如何系统做 Security Review？](04-smart-contract-security/q40.md) | 04 | ★★★★★ | ★★★★★ | 47 |
| Q41 | [Uniswap V2 为什么使用 x*y=k？](05-defi/q41.md) | 05 | ★★ | ★★★★★ | 49 |
| Q42 | [Slippage 与 Price Impact 有什么区别？](05-defi/q42.md) | 05 | ★★ | ★★★★★ | 50 |
| Q43 | [什么是 Impermanent Loss？](05-defi/q43.md) | 05 | ★★★ | ★★★★☆ | 51 |
| Q44 | [Uniswap V3 Concentrated Liquidity 解决了什么问题？](05-defi/q44.md) | 05 | ★★★ | ★★★★★ | 52 |
| Q45 | [Uniswap V3 Tick 与 sqrtPriceX96 是什么？](05-defi/q45.md) | 05 | ★★★★ | ★★★★☆ | 53 |
| Q46 | [Lending Protocol 的 Health Factor 是什么？](05-defi/q46.md) | 05 | ★★★ | ★★★★★ | 54 |
| Q47 | [为什么 DeFi Lending 通常需要 Over-collateralization？](05-defi/q47.md) | 05 | ★★ | ★★★★☆ | 55 |
| Q48 | [Liquidation 的经济机制是什么？](05-defi/q48.md) | 05 | ★★★ | ★★★★★ | 56 |
| Q49 | [Stablecoin 有哪些主要设计与 Failure Modes？](05-defi/q49.md) | 05 | ★★★ | ★★★★☆ | 57 |
| Q50 | [设计 DeFi Protocol 时最重要的 Invariant 是什么？](05-defi/q50.md) | 05 | ★★★★★ | ★★★★★ | 58 |
| Q51 | [为什么 Ethereum 需要 Layer2？](06-layer2-rollup-zk-bridge/q51.md) | 06 | ★★ | ★★★★★ | 60 |
| Q52 | [Optimistic Rollup 的工作原理是什么？](06-layer2-rollup-zk-bridge/q52.md) | 06 | ★★★ | ★★★★★ | 61 |
| Q53 | [ZK Rollup 与 Optimistic Rollup 的核心区别？](06-layer2-rollup-zk-bridge/q53.md) | 06 | ★★★ | ★★★★★ | 62 |
| Q54 | [EIP-4844 为什么对 Rollup 重要？](06-layer2-rollup-zk-bridge/q54.md) | 06 | ★★★★ | ★★★★★ | 63 |
| Q55 | [Data Availability 到底是什么意思？](06-layer2-rollup-zk-bridge/q55.md) | 06 | ★★★★ | ★★★★★ | 64 |
| Q56 | [Sequencer 是什么？中心化 Sequencer 有哪些风险？](06-layer2-rollup-zk-bridge/q56.md) | 06 | ★★★ | ★★★★★ | 65 |
| Q57 | [Validium 与 ZK Rollup 有什么区别？](06-layer2-rollup-zk-bridge/q57.md) | 06 | ★★★★ | ★★★★☆ | 66 |
| Q58 | [为什么 Bridge 是 Web3 高风险组件？](06-layer2-rollup-zk-bridge/q58.md) | 06 | ★★★ | ★★★★★ | 67 |
| Q59 | [ZK Proof 的 Completeness、Soundness、Zero-Knowledge 分别是什么？](06-layer2-rollup-zk-bridge/q59.md) | 06 | ★★★★ | ★★★★☆ | 68 |
| Q60 | [设计一个 Rollup 需要哪些核心组件？](06-layer2-rollup-zk-bridge/q60.md) | 06 | ★★★★★ | ★★★★★ | 69 |
| Q61 | [EOA 与 Smart Contract Account 有什么区别？](07-wallet-signature-account-abstraction/q61.md) | 07 | ★★ | ★★★★★ | 71 |
| Q62 | [ecrecover 做什么？有哪些安全注意事项？](07-wallet-signature-account-abstraction/q62.md) | 07 | ★★★ | ★★★★☆ | 72 |
| Q63 | [什么是 Signature Replay Attack？](07-wallet-signature-account-abstraction/q63.md) | 07 | ★★★ | ★★★★★ | 73 |
| Q64 | [EIP-712 解决什么问题？](07-wallet-signature-account-abstraction/q64.md) | 07 | ★★★ | ★★★★★ | 74 |
| Q65 | [ERC-2612 Permit 是什么？](07-wallet-signature-account-abstraction/q65.md) | 07 | ★★★ | ★★★★☆ | 75 |
| Q66 | [Account Abstraction 解决哪些 UX 与安全问题？](07-wallet-signature-account-abstraction/q66.md) | 07 | ★★★ | ★★★★★ | 76 |
| Q67 | [ERC-4337 的 UserOperation 与 EntryPoint 流程是什么？](07-wallet-signature-account-abstraction/q67.md) | 07 | ★★★★ | ★★★★★ | 77 |
| Q68 | [ERC-4337 Paymaster 是做什么的？](07-wallet-signature-account-abstraction/q68.md) | 07 | ★★★★ | ★★★★☆ | 78 |
| Q69 | [EIP-7702 与 ERC-4337 是什么关系？](07-wallet-signature-account-abstraction/q69.md) | 07 | ★★★★★ | ★★★★★ | 79 |
| Q70 | [如何设计一个生产级 Smart Wallet？](07-wallet-signature-account-abstraction/q70.md) | 07 | ★★★★★ | ★★★★★ | 80 |
| Q71 | [为什么智能合约不能直接请求普通 HTTP API？](08-oracle-mev-infrastructure/q71.md) | 08 | ★★ | ★★★★★ | 82 |
| Q72 | [一个可靠 Oracle 应具备哪些性质？](08-oracle-mev-infrastructure/q72.md) | 08 | ★★★ | ★★★★★ | 83 |
| Q73 | [什么是 MEV？](08-oracle-mev-infrastructure/q73.md) | 08 | ★★★ | ★★★★★ | 84 |
| Q74 | [Front-running、Back-running、Sandwich 在机制上如何区分？](08-oracle-mev-infrastructure/q74.md) | 08 | ★★★ | ★★★★☆ | 85 |
| Q75 | [为什么 Public Mempool 会产生独特安全问题？](08-oracle-mev-infrastructure/q75.md) | 08 | ★★★ | ★★★★☆ | 86 |
| Q76 | [JSON-RPC 在 Web3 架构中是什么？](08-oracle-mev-infrastructure/q76.md) | 08 | ★★ | ★★★★★ | 87 |
| Q77 | [Archive Node、Full Node、Light Client 有什么区别？](08-oracle-mev-infrastructure/q77.md) | 08 | ★★★ | ★★★★☆ | 88 |
| Q78 | [为什么 Web3 应用通常需要 Indexer？](08-oracle-mev-infrastructure/q78.md) | 08 | ★★★ | ★★★★★ | 89 |
| Q79 | [Indexer 如何正确处理 Chain Reorg？](08-oracle-mev-infrastructure/q79.md) | 08 | ★★★★ | ★★★★★ | 90 |
| Q80 | [RPC Provider 挂了，生产 dApp 应如何降级？](08-oracle-mev-infrastructure/q80.md) | 08 | ★★★ | ★★★★★ | 91 |
| Q81 | [Ethereum 与 Solana 最大的编程模型区别是什么？](09-solana-multichain/q81.md) | 09 | ★★★ | ★★★★★ | 93 |
| Q82 | [Solana Account 是什么？](09-solana-multichain/q82.md) | 09 | ★★ | ★★★★★ | 94 |
| Q83 | [为什么 Solana Program 通常被称为 Stateless？](09-solana-multichain/q83.md) | 09 | ★★ | ★★★★☆ | 95 |
| Q84 | [什么是 PDA？为什么没有私钥？](09-solana-multichain/q84.md) | 09 | ★★★ | ★★★★★ | 96 |
| Q85 | [什么是 CPI？](09-solana-multichain/q85.md) | 09 | ★★★ | ★★★★★ | 97 |
| Q86 | [Solana 为什么更容易并行执行某些 Transactions？](09-solana-multichain/q86.md) | 09 | ★★★★ | ★★★★★ | 98 |
| Q87 | [Ethereum 与 Solana Transaction Atomicity 有何异同？](09-solana-multichain/q87.md) | 09 | ★★★ | ★★★★☆ | 99 |
| Q88 | [为什么 Multi-chain dApp 比单链难很多？](09-solana-multichain/q88.md) | 09 | ★★★ | ★★★★★ | 100 |
| Q89 | [Multi-chain Token 如何保证 Total Supply Invariant？](09-solana-multichain/q89.md) | 09 | ★★★★ | ★★★★★ | 101 |
| Q90 | [设计一个 Ethereum + Solana Wallet SDK。](09-solana-multichain/q90.md) | 09 | ★★★★★ | ★★★★★ | 102 |
| Q91 | [Coding：实现一个 Mini ERC-20 Staking Contract，怎样从 O(N) 奖励更新到 O(1)？](10-system-design-practice/q91.md) | 10 | ★★★★ | ★★★★★ | 104 |
| Q92 | [Coding Review：看到一个 Withdraw 函数，如何快速审查？](10-system-design-practice/q92.md) | 10 | ★★★ | ★★★★★ | 105 |
| Q93 | [System Design：设计一个 NFT Marketplace。](10-system-design-practice/q93.md) | 10 | ★★★★ | ★★★★★ | 106 |
| Q94 | [System Design：设计 DAO Governance System。](10-system-design-practice/q94.md) | 10 | ★★★★ | ★★★★★ | 107 |
| Q95 | [System Design：设计 Multi-sig Wallet。](10-system-design-practice/q95.md) | 10 | ★★★★ | ★★★★★ | 108 |
| Q96 | [System Design：设计 Token Vesting Contract。](10-system-design-practice/q96.md) | 10 | ★★★ | ★★★★☆ | 109 |
| Q97 | [System Design：设计高可靠 Blockchain Indexing Service。](10-system-design-practice/q97.md) | 10 | ★★★★★ | ★★★★★ | 110 |
| Q98 | [System Design：设计中心化交易平台 Deposit System。](10-system-design-practice/q98.md) | 10 | ★★★★★ | ★★★★★ | 111 |
| Q99 | [Debug：用户说“交易失败了”，你如何系统排查？](10-system-design-practice/q99.md) | 10 | ★★★★ | ★★★★★ | 112 |
| Q100 | [Staff 题：从用户点击按钮到链上结算，设计完整 Web3 Protocol。](10-system-design-practice/q100.md) | 10 | ★★★★★ | ★★★★★ | 113 |
