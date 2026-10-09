# 剑指 Web3 Offer - 100 道真题级面试题（2026 GitHub Edition）

> Web3 / Solidity / EVM / Security / DeFi / L2 / Account Abstraction / Infrastructure / Solana / System Design

本仓库把 **116 页 PDF** 完整拆解为可维护的 GitHub 知识库：**100 道题 = 100 个独立 Markdown**。每题保留 PDF 的原始主干，并增加生产工程、审计、测试、白板图、高频追问回答方向和扩展阅读。当前为 **v2 Professional Deep Dive**：100 题正文合计约 **84 万字符**，平均每题约 **8.4K 字符**。

## 核心特点

- **100/100 题独立 Markdown**：每题均含元数据、PDF 页码和前后导航。
- **PDF 主干完整保留**：面试官意图、30 秒回答、深入解析、公式/代码、关键点、追问、Gotchas、记忆锚点均进入 Markdown。
- **专业扩展**：每题增加工程化理解、验证/测试清单、自测题、Mermaid 白板图。
- **Core 30 冲刺路线**：优先掌握最能区分候选人层级的 30 道题。
- **2026 技术口径**：覆盖 EIP-1153、EIP-4844、ERC-4337、EIP-7702、OpenZeppelin 5.x 与 Solana account/program/PDA/CPI。
- **可机器读取**：`data/questions.json` 可直接用于搜索、RAG、静态站点或题库应用。
- **可自动校验**：`python scripts/validate_repo.py` 检查 100 题、内部链接、PDF 映射与元数据。

## v2 Professional Deep Dive

每道题在 PDF 主干之外，统一增加以下专业层：

- 前置知识与概念边界；
- 形式化模型 / 白板推导；
- 题目特有的关键深挖；
- 生产工程决策；
- Threat Model / Failure Modes；
- Unit / Fuzz / Invariant / Integration 测试策略；
- 可观测性与线上排障；
- 不同岗位的回答重点；
- 面试官评分 Rubric；
- 关联题知识网络；
- 实战训练与反向面试问题。

> 内容边界：每题第 1–5 节以原 PDF 为主干；标记为“GitHub 专业深化”的部分属于基于通用工程知识的扩展推导，不应误认为 PDF 原文。


## 快速入口

- 📚 [在线阅读入口（docs/index.md）](docs/index.md)
- 🎯 [Core 30](docs/11-appendix/core-30.md)
- 🗓️ [7 天冲刺计划](docs/11-appendix/7-day-plan.md)
- 🛡️ [Solidity Security Checklist](docs/11-appendix/security-review-checklist.md)
- 🏗️ [Web3 System Design Checklist](docs/11-appendix/system-design-checklist.md)
- 🔗 [官方参考资料](docs/references.md)
- 📄 [原始 PDF](assets/pdf/Jianzhi_Web3_Offer_100_Interview_Questions_2026.pdf)
- 🧭 [PDF -> Markdown 对照表](SOURCE_MAPPING.md)
- 🤝 [贡献指南](CONTRIBUTING.md)

## Repo 结构

```text
jianzhi-web3-offer-100/
├── README.md
├── SOURCE_MAPPING.md
├── assets/pdf/                 # 原始 116 页 PDF
├── data/                       # questions.json / refs / page map / source manifest
├── docs/
│   ├── 00-preface/
│   ├── 01-blockchain-fundamentals/
│   ├── 02-ethereum-evm/
│   ├── 03-solidity/
│   ├── 04-smart-contract-security/
│   ├── 05-defi/
│   ├── 06-layer2-rollup-zk-bridge/
│   ├── 07-wallet-signature-account-abstraction/
│   ├── 08-oracle-mev-infrastructure/
│   ├── 09-solana-multichain/
│   ├── 10-system-design-practice/
│   └── 11-appendix/
├── scripts/
│   ├── enrich_questions.py      # 可重复生成 v2 专业深化层
│   └── validate_repo.py         # 完整性 / 链接 / 内容质量校验
├── mkdocs.yml
└── .github/workflows/docs.yml
```

## 推荐学习方法

一个高级回答按五层推进：

```text
定义
  -> 原理
    -> Failure Mode
      -> Mitigation
        -> Invariant / Trade-off
```

不要把题库当作“100 个定义”。真正需要训练的是：**能推导、能找边界、能写不变量、能落地到生产系统**。

## 10 大章节

- **01** [Blockchain 基础与密码学直觉](docs/01-blockchain-fundamentals/index.md) - Q01-Q10
- **02** [Ethereum / EVM：从交易到状态转换](docs/02-ethereum-evm/index.md) - Q11-Q20
- **03** [Solidity 工程：语言语义、ABI 与 Gas](docs/03-solidity/index.md) - Q21-Q30
- **04** [智能合约安全：从漏洞列表到 Invariant](docs/04-smart-contract-security/index.md) - Q31-Q40
- **05** [DeFi：AMM、Lending 与经济不变量](docs/05-defi/index.md) - Q41-Q50
- **06** [Layer2、Rollup、ZK 与 Bridge](docs/06-layer2-rollup-zk-bridge/index.md) - Q51-Q60
- **07** [钱包、签名与 Account Abstraction](docs/07-wallet-signature-account-abstraction/index.md) - Q61-Q70
- **08** [Oracle、MEV 与 Web3 基础设施](docs/08-oracle-mev-infrastructure/index.md) - Q71-Q80
- **09** [Solana 与 Multi-chain：另一种执行模型](docs/09-solana-multichain/index.md) - Q81-Q90
- **10** [系统设计与现场实战](docs/10-system-design-practice/index.md) - Q91-Q100

## 本地校验

```bash
python scripts/validate_repo.py
```

## 本地文档站（可选）

```bash
pip install -r requirements-docs.txt
mkdocs serve
```

## 来源与扩展边界

- 每题中标注 **PDF 主干** 的内容来自当前 PDF/其结构化生成源。
- 标注 **GitHub 扩展** 的内容是为了工程化学习而新增的分析与检查清单。
- 外部资料优先引用协议规范或官方文档；规范会变化，因此保留“最后核验日期”而不把任何第三方总结视为永久事实。

## License

当前仓库未替你选择开源许可证。公开发布前请根据你希望别人如何使用、修改和再分发这套材料，选择合适的 LICENSE。
