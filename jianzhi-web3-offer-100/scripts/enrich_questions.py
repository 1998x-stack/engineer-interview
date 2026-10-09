from __future__ import annotations

from pathlib import Path
import json
import re
from collections import defaultdict

ROOT = Path(__file__).resolve().parents[1]
QUESTIONS = json.loads((ROOT / 'data/questions.json').read_text(encoding='utf-8'))
BY_ID = {q['id']: q for q in QUESTIONS}

START = '<!-- PROFESSIONAL_ENRICHMENT_START -->'
END = '<!-- PROFESSIONAL_ENRICHMENT_END -->'
LAB_START = '<!-- PROFESSIONAL_LAB_START -->'
LAB_END = '<!-- PROFESSIONAL_LAB_END -->'

CHAPTER_PROFILES = {
1: {
    'name': 'Blockchain / 密码学 / 共识',
    'prereqs': ['分布式状态机与复制', '密码学 hash / signature 的基本安全性质', '共识、最终性与网络分区的区别'],
    'model': '先把协议抽象成 `S_{t+1}=F(S_t, T_t)`：节点需要对输入交易的有效性、排序以及最终采用的历史达成一致。随后再标注哪些性质来自密码学、哪些来自共识、哪些来自经济激励。',
    'engineering': [
        '任何“已确认”都要转换成业务确认策略：确认深度、finalized 标记、最大可接受 reorg、回滚方式。',
        '系统不能只存交易哈希；至少保存 block number/hash、parent hash、链 ID 和处理版本，才能在 reorg 或多链环境下恢复。',
        '把协议安全假设写成显式文档，例如诚实多数、弱主观性检查点、可信启动参数或外部数据源。',
        '对密码学对象做 domain separation，避免同一字节串在不同业务语义中被复用。',
    ],
    'failures': ['错误地把“复制很多份”当成拜占庭容错', '把最终性当固定等待时间而非协议/经济保证', '忽视分区、重组与节点视图不一致', '把 hash、签名、加密的安全性质混为一谈'],
    'tests': ['状态机确定性测试：同一状态和交易序列必须得到同一结果', 'reorg/partition 仿真：验证业务层能回滚或延迟确认', '跨链/跨域重放测试：chainId、domain、nonce 必须进入安全边界'],
    'obs': ['tip height / finalized height 差值', 'reorg 深度与频率', 'peer/validator 可用性', '不同 RPC 对 canonical head 的分歧'],
},
2: {
    'name': 'Ethereum / EVM',
    'prereqs': ['EVM call frame、stack/memory/storage', 'ABI 编码与 calldata', 'transaction、gas、receipt 与 state root'],
    'model': '把 EVM 看成带 gas 预算的确定性状态机：每个 opcode 同时更新机器状态（pc/stack/memory）和可能的世界状态；外部调用会创建新的 call frame，而 `DELEGATECALL` 等指令改变代码与存储上下文的组合方式。',
    'engineering': [
        '定位问题时先区分 transaction-level state、call-frame-local state 与 persistent storage，不要把 memory/storage 生命周期混淆。',
        '分析 gas 时先看 storage write、cold/warm access、external call、memory expansion，再看微小 opcode 优化。',
        '涉及 proxy/CREATE2/raw storage 时必须画 storage layout 或 address derivation，避免仅凭 Solidity 表面语义推断。',
        '对 ABI/calldata 问题使用真实编码向量做测试，尤其是 dynamic type、selector、fallback 与 custom error。',
    ],
    'failures': ['storage context 理解错误导致 proxy/DELEGATECALL 漏洞', '错误假设 EOA/contract 可通过 code.length 永久区分', 'gas 估算只看均值，忽略 worst-case 与状态冷热差异', 'ABI 编码歧义或 selector/call data 解析错误'],
    'tests': ['Foundry/Hardhat 单元测试覆盖 call/revert/return data', 'storage slot 断言与 upgrade layout diff', 'gas snapshot 只作为回归信号，不作为安全证明', 'fork test 验证真实主网依赖与边界条件'],
    'obs': ['gas used / revert selector 分布', 'trace 中外部调用深度', 'storage slot 变化', 'nonce / fee / inclusion latency'],
},
3: {
    'name': 'Solidity / 合约工程',
    'prereqs': ['Solidity data location 与 ABI', 'ERC 标准及 token 行为差异', 'compiler checks、revert 与 event'],
    'model': '回答 Solidity 题时把“语言表面规则”下沉到 EVM：参数最终如何编码、状态变量落在哪个 slot、external call 产生什么 call frame、失败时哪些状态会回滚。这样才能解释 gas 与安全后果。',
    'engineering': [
        'API 设计先定义权限、失败语义和事件，再写函数体；外部接口是协议的一部分。',
        '优化前做 profiling，优先减少状态写入、重复 SLOAD、无意义拷贝和外部调用。',
        '兼容 ERC20/721/1155 时要考虑非标准返回值、callback/hook、fee-on-transfer 等现实行为。',
        '生产合约必须有 compiler/version pin、static analysis、fuzz/invariant tests 与部署脚本审计。',
    ],
    'failures': ['把 visibility 当隐私机制', '只按 happy path 处理 token transfer/approve', 'unchecked 或 assembly 缺少数学边界证明', 'event 与 storage 的职责混用导致链上状态不可验证'],
    'tests': ['边界值：0、1、max、空数组、重复调用', 'fuzz ABI 输入与权限边界', 'event 与 state transition 一致性断言', 'gas regression + stateful invariant testing'],
    'obs': ['custom error/revert selector', '关键 event 与状态对账', 'gas per action', '异常 allowance/transfer failure 比例'],
},
4: {
    'name': 'Smart Contract Security',
    'prereqs': ['资产与不变量建模', 'EVM external call / delegatecall', 'oracle、token hook、upgradeability 基础'],
    'model': '安全题统一使用 `Assets → Entry Points → State Transitions → External Interactions → Privileged Roles → Invariants` 六步模型。漏洞名称只是分类结果，真正目标是证明攻击者能让某个 invariant 失效。',
    'engineering': [
        '先写资产与不变量，再枚举攻击面；没有 invariant 的“审计”容易沦为模式匹配。',
        '把所有外部调用视作潜在控制流转移，包括 token hook、callback、fallback、delegatecall 与 oracle read。',
        '权限不是单一 owner：管理员、guardian、upgrader、oracle admin、keeper、pauser 都要单独建模。',
        '把经济攻击纳入威胁模型：瞬时流动性、MEV、oracle 延迟、舍入、清算激励都可能击穿代码层假设。',
    ],
    'failures': ['只贴漏洞标签，不给可利用前提与资产影响', '单函数视角忽略 cross-function / cross-contract 状态', '管理员路径未纳入安全审计', 'mitigation 修补症状但没有恢复 invariant'],
    'tests': ['stateful fuzz / invariant：资产守恒、权限、份额/债务关系', 'adversarial callback 合约测试重入与 hook', 'fork test 模拟真实 oracle/liquidity/token 行为', 'upgrade、pause、recovery 等 privileged path 单独测试'],
    'obs': ['关键 invariant 的链上派生指标', '异常大额/高频调用', 'oracle deviation/staleness', 'admin/upgrader/guardian 行为审计日志'],
},
5: {
    'name': 'DeFi / AMM / Lending',
    'prereqs': ['token accounting 与 decimals', 'AMM 定价/套利直觉', 'oracle、抵押、清算与风险参数'],
    'model': 'DeFi 题先写资产负债表和不变量：谁的资产进入协议、协议欠谁什么、价格从哪里来、何时允许价值转移。随后再讨论曲线、利率或清算参数，否则公式容易脱离经济语义。',
    'engineering': [
        '所有价格都写明 source、window、liquidity、staleness、decimal 与 fallback，不允许“price”成为黑盒变量。',
        '对 shares/assets、collateral/debt、reserve/invariant 使用固定精度并定义舍入方向。',
        '风险参数要考虑极端市场：流动性枯竭、gas 飙升、oracle 停更、相关性突变、坏账瀑布。',
        '交易路径必须有 slippage/deadline/minOut 等用户保护，并考虑 MEV 与 sandwich 风险。',
    ],
    'failures': ['把 flash loan 当漏洞根因而忽略被放大的错误假设', '用瞬时 spot price 作为高价值抵押定价', '舍入/精度偏差在循环中累积为可提取价值', '清算激励不足导致坏账，激励过高又伤害用户'],
    'tests': ['价格跳变、流动性枯竭、极端 decimals 的 fuzz', '资产/份额/债务守恒 invariant', '清算边界前后与 oracle stale 场景', 'MEV/顺序敏感模拟和 fork-based integration test'],
    'obs': ['TVL 与可用流动性', 'health factor / utilization 分布', 'oracle deviation/staleness', 'bad debt / liquidation success rate'],
},
6: {
    'name': 'Layer2 / Rollup / ZK / Bridge',
    'prereqs': ['L1 execution/consensus/finality', 'state root 与 Merkle commitment', 'data availability、proof 与 bridge trust model'],
    'model': 'Rollup 题至少拆成四层：`Execution → State Commitment/Proof → Data Availability → Settlement/Finality`。Bridge 再额外加入“跨域消息真实性如何验证”。不要把低费用、proof 和 DA 混成一个概念。',
    'engineering': [
        '明确每个状态的最终性层级：L2 soft confirmation、batch posted、proof/challenge complete、L1 finalized。',
        '把 sequencer/prover/batcher/bridge/admin 的故障与恶意行为分别建模。',
        'withdrawal 与 emergency exit 必须回答“最坏情况下用户如何拿回资产”。',
        '数据发布、blob/call data、offchain DA 的成本与信任假设要一起讨论。',
    ],
    'failures': ['把 validity proof 错当 data availability 保证', '把 sequencer 停机等同于资金一定丢失', 'bridge 只审计 Solidity 不审计跨链验证逻辑', '忽视 upgrade keys / pause keys 带来的系统性信任'],
    'tests': ['batch/proof/challenge 的状态机测试', 'sequencer/prover/batcher 停机演练', 'L1 reorg 与 delayed message 重放测试', 'bridge message nonce/domain/source chain 验证'],
    'obs': ['L2→L1 batch lag', 'proof/challenge backlog', 'DA publication success', 'bridge message pending/failed/duplicate'],
},
7: {
    'name': 'Wallet / Signature / Account Abstraction',
    'prereqs': ['ECDSA/签名验证基础', 'nonce、domain separation 与 replay protection', 'EOA、smart account 与 transaction lifecycle'],
    'model': '钱包题统一拆成 `Intent → Authorization → Validation → Execution → Gas Payment → Recovery`。签名只是 authorization 的一种载体；真正安全边界由 domain、nonce、权限范围、过期时间和执行上下文共同决定。',
    'engineering': [
        '签名结构必须绑定 chain/domain/action/nonce/deadline，不能只签“看起来唯一”的 message。',
        'owner、guardian、session key、module、paymaster 各自使用最小权限与独立撤销路径。',
        'AA 系统要把 validation gas、execution gas、sponsor policy 和 bundler failure 分开观测。',
        'UX 必须展示真实授权范围，避免无限授权、隐式 delegation 或不可理解的 typed data。',
    ],
    'failures': ['跨链/跨合约/跨函数 replay', '恢复/升级路径权限大于日常 owner', 'session key 无到期或 scope 过宽', 'paymaster 被 griefing 或 sponsor policy 可绕过'],
    'tests': ['错误 chainId/domain/nonce/deadline 的签名拒绝测试', '批处理部分失败与原子性测试', 'recovery/module/session-key 撤销与过期', 'bundler/paymaster 拒绝、超时、gas 边界测试'],
    'obs': ['signature validation failure', 'nonce gap / replay attempts', 'UserOp inclusion latency', 'paymaster spend / rejection reason'],
},
8: {
    'name': 'Oracle / MEV / Infrastructure',
    'prereqs': ['节点/RPC 与 canonical chain', 'mempool 与交易排序', '事件日志、索引器与外部数据源'],
    'model': 'Infra 题要区分“链上共识事实”和“应用派生视图”。RPC、Indexer、Oracle 都是把底层状态暴露给上层的基础设施，但它们有不同一致性、可用性和信任模型。',
    'engineering': [
        '所有外部依赖都要定义 freshness、quorum/fallback、timeout、重试、幂等与降级策略。',
        'Indexer 永远按 block hash/parent hash 维护 canonical chain，不能只按递增 block number。',
        'RPC 多供应商需要做结果一致性校验，而不是简单 round-robin。',
        'MEV 风险要从公开意图、排序权和可提取价值三者分析，并优先设计用户保护。',
    ],
    'failures': ['RPC 返回 stale/forked view 仍被业务当最终事实', 'Indexer reorg 后重复/漏处理事件', 'oracle source 单点或 staleness 未处理', '公开 mempool 暴露订单意图导致顺序型攻击'],
    'tests': ['多 RPC 分歧与故障注入', 'reorg rollback/replay/idempotency', 'oracle stale/deviation/source-down 场景', 'private/public submission 路径与顺序敏感仿真'],
    'obs': ['RPC error/latency/head divergence', 'indexer lag/reorg depth', 'oracle update age/deviation', 'mempool→inclusion latency / failed replacement'],
},
9: {
    'name': 'Solana / Multi-chain',
    'prereqs': ['Solana accounts/programs/instructions', 'PDA/CPI/Signer 权限', 'Ethereum 与 Solana transaction/state model 差异'],
    'model': 'Solana 题用 `Program Code + Explicit Accounts + Runtime Ownership/Locks` 建模；多链题则抽象为统一 intent，但每条链保留独立的 address、fee、signing、finality、token 与 error semantics。',
    'engineering': [
        '明确 writable/read-only/signer/owner 等 account 权限，避免把“传进来的 account”自动视为可信。',
        'PDA seeds、bump、program id 和初始化流程属于地址安全边界。',
        'CPI 需要重新审视权限传播、reentrancy-like composition 和 account aliasing。',
        '多链 SDK 应统一接口但不能抹平链语义；finality、fee estimation、simulation 需要 per-chain adapter。',
    ],
    'failures': ['account owner/signer 校验不足', 'PDA seed domain 不清导致地址碰撞或权限混淆', '多链统一抽象隐藏链特有失败语义', '跨链 supply/accounting 只做“消息成功”而不做资产守恒'],
    'tests': ['错误 owner/signer/PDA seeds 的拒绝测试', 'CPI 权限与 account aliasing', '并发 writable account 冲突与 retry', '跨链 mint/burn/lock accounting invariant'],
    'obs': ['transaction simulation error', 'account lock contention', 'slot/finality lag', '跨链消息与 supply reconciliation'],
},
10: {
    'name': 'System Design / Coding / Debug',
    'prereqs': ['前九章的状态、安全、DeFi 与 infra 基础', '幂等、事务、队列、缓存、数据库与 SRE 基础', '威胁建模与可观测性'],
    'model': '系统设计题先分离 `On-chain source of truth`、`Off-chain orchestration` 和 `Derived read model`。然后画资产流、状态机、信任边界和失败恢复路径；最后才讨论具体数据库、队列或框架。',
    'engineering': [
        '先写功能/非功能需求和 invariant，再画组件图，避免一上来堆技术名词。',
        '所有写路径都要回答幂等键、重试、重复消息、事务边界和补偿策略。',
        '链上与内部 ledger 必须可对账；金额、decimals、chain/token identity 都要有强类型语义。',
        '安全设计必须覆盖 admin key、upgrade、pause、incident response、审计日志与最坏情况用户退出。',
    ],
    'failures': ['没有定义 source of truth，链上与数据库互相覆盖', '只画 happy path，没有 reorg/RPC/queue/db failure', '余额直接 UPDATE 而非 ledger/可审计账务', '把“去中心化”当作自动高可用而忽略前端/RPC/indexer 单点'],
    'tests': ['故障注入：RPC/DB/queue/worker 重启与网络分区', '幂等与 exactly-once-like 行为验证', 'reorg/backfill/replay 的恢复演练', '容量、延迟、资金安全和权限边界的压测/攻防测试'],
    'obs': ['end-to-end settlement latency', 'queue lag / retry rate', 'ledger reconciliation delta', 'reorg/RPC/indexer incident indicators'],
},
}

SPECIAL = {
    1: ('信任模型不是“完全无信任”', '最准确的表述是把信任从单个管理员转化为协议假设：密码学难题、诚实/经济多数、客户端实现与社会协调。面试中主动说出“trust minimization 而非 trust elimination”会更严谨。'),
    2: ('状态依赖如何影响并行性', 'UTXO 把冲突暴露在输入引用中；Account Model 允许函数动态访问共享状态，因此静态推断冲突更难。工程上这直接影响 wallet coin selection、mempool 冲突处理和并行执行调度。'),
    3: ('Hash 的语义边界', 'Hash 提供的是摘要/承诺，不提供保密性。签名通常对 hash 后的结构化消息做认证，而 encryption 解决 confidentiality；三者不要混用。'),
    4: ('Merkle proof 证明了什么', 'proof 只证明“某个 leaf 按既定编码规则属于某个 root”，不证明 leaf 对应的现实世界事实正确。root 的可信来源仍需额外安全假设。'),
    5: ('业务 Finality 与协议 Finality', '交易平台常定义多层状态：observed → confirmed → credited → finalized。高价值业务可以在协议 finality 前采取额度冻结或延迟提现，降低 reorg 风险。'),
    6: ('比较 PoW/PoS 时的正确维度', '应比较 Sybil resistance、攻击资本、惩罚机制、fork choice、finality、弱主观性、恢复与中心化压力，而不是把能源消耗或 TPS 当作唯一维度。'),
    7: ('Fork ≠ Hard Fork', '短期 fork 是运行时多个候选历史；fork choice 决定 canonical head；hard fork 是验证规则不兼容升级。应用工程最直接处理的是 reorg，而不是协议政治。'),
    8: ('Gas 是资源计量，不是价格', '`gasUsed` 描述执行资源，`effectiveGasPrice` 把资源映射为 ETH 成本。优化时应先减少高成本状态变化，而不是机械追求更少 Solidity 行数。'),
    9: ('签名验证的完整上下文', '生产签名方案至少考虑 message format、domain、chainId、nonce、expiry、signer recovery 与 malleability/low-s 规则；仅验证“恢复出的地址等于 owner”通常不够。'),
    10: ('Code is Law 的治理现实', '协议真实控制面还包括 upgrade keys、multisig、oracle、frontend、治理和社会共识。评价“去中心化”要看这些控制面是否可单方改变用户资产规则。'),
    11: ('EVM 的两层状态', '要区分 machine state 与 world state：stack/memory/pc 属于调用执行上下文，account/storage 属于持久世界状态。很多调试错误来自把两层混在一起。'),
    12: ('四种数据区域的生命周期', 'stack 是操作数栈；memory 随 call frame 生命周期；storage 持久跨交易；transient storage 跨同一交易内的调用但交易结束清空。生命周期是最重要的区分维度。'),
    13: ('data location 不是风格选择', '`calldata` 适合只读外部输入，`memory` 是可变临时副本，`storage` 引用持久状态。选择会影响 copy、aliasing、gas 与可修改性。'),
    14: ('DELEGATECALL 的危险本质', '危险不是“它会调用别的合约”，而是“在调用者 storage/context 中执行别人的 code”。这使 storage layout 与 implementation trust 成为安全边界。'),
    15: ('ABI 解析要以字节布局说话', '高级回答应能解释 4-byte selector、32-byte word、head/tail dynamic encoding，以及 revert/custom error 同样走 ABI 编码。'),
    16: ('Mapping 没有可枚举目录', 'mapping 的 slot 是由 key 与声明 slot 计算出的伪随机位置；链上没有“所有 key 列表”。需要枚举时必须额外维护数组/事件/索引器。'),
    17: ('CREATE2 的地址承诺对象', 'CREATE2 地址依赖 deployer、salt 与 initcode hash，而不是最终 runtime bytecode 本身。constructor 参数改变 initcode，因此也会改变预测地址。'),
    18: ('1559 不保证交易费低', 'EIP-1559 改善费用估算与 base fee 机制，但拥堵时 base fee 仍可很高。用户体验还受 priority fee、blob fee、L2 fee model 等影响。'),
    19: ('Transient Storage 的安全使用', '它适合 transaction-scoped coordination，例如 reentrancy lock，但必须理解 delegatecall/ownership context；“自动更安全”是错误结论。'),
    20: ('Transaction lifecycle 是跨层问题', '钱包签名、mempool、builder/validator、execution、receipt、consensus finality 都可能失败。排障时必须明确失败发生在哪一层。'),
    21: ('Visibility 不等于 confidentiality', '`private` 只限制 Solidity 级访问，链上 storage 仍可读取。敏感信息不能靠变量 visibility 保密。'),
    22: ('view/pure 与“免费”无关', '它们是编译器语义约束；作为 transaction 内部调用仍消耗 gas。用户通过 `eth_call` 本地模拟时才无需链上付费。'),
    23: ('Fallback 是协议入口', 'proxy、forwarder、未知 selector 处理都依赖 fallback。任何 fallback 中的 delegatecall/ETH 接收逻辑都应视为高风险入口。'),
    24: ('unchecked 需要证明，不需要勇气', '只有当循环边界或算术不变量能证明不会 overflow/underflow 时才使用；审计时要能写出这个证明而不是“为了省 gas”。'),
    25: ('constant/immutable 的部署语义', '`constant` 在编译期确定；`immutable` 在 constructor 设置并固化进部署后的 code 访问路径。二者都不是可升级配置。'),
    26: ('Event 是观测面，不是计算面', '日志适合链下索引和审计，但 EVM 合约不能像数据库一样查询任意历史日志来执行业务逻辑。关键链上决策仍需 state。'),
    27: ('错误类型是 ABI 的一部分', 'custom error 既节省部署/运行成本，也让调用方稳定解析失败原因。生产 API 应把 error selector 当作兼容性契约管理。'),
    28: ('Allowance 的本质是可消费授权状态', '安全分析要关注“授权额度如何变化”和“spender 在两个状态之间能否抢先消费”，并进一步考虑 permit、Permit2、temporary approval 等不同授权模型。'),
    29: ('Token 标准差异来自资产模型', 'ERC-721 以 tokenId 唯一所有权为中心；ERC-1155 以 `(id, balance)` 支持多类型与批处理。选择标准应由资产语义和交互模式决定。'),
    30: ('Gas Optimization 的正确优先级', '正确性与安全 > 算法/状态写入优化 > storage/data layout > ABI/copy 优化 > 微型 opcode 技巧。先 profile 再优化。'),
    31: ('Reentrancy 是控制流问题', '外部调用把控制权交给不可信代码，而本地状态可能仍处于中间态。不要把它简化成“withdraw 函数漏洞”。'),
    32: ('CEI 是局部证明技巧', '先完成 checks 和 effects 可以减少回调看到中间态的机会，但复杂协议仍可能存在 cross-function / cross-contract 共享状态，因此 CEI 不是全局安全证明。'),
    33: ('Guard 的作用域决定覆盖面', '单个 `nonReentrant` 锁只覆盖进入同一 guard domain 的路径；只读函数、另一个合约或共享 oracle 状态仍可能形成可重入观测问题。'),
    34: ('Authorization 应绑定直接调用者/签名语义', '`tx.origin` 暴露的是交易最初 EOA，并不能表达“当前调用路径被授权”。协议应基于 `msg.sender`、角色或显式签名验证。'),
    35: ('Oracle Manipulation 是信任窗口问题', '根因通常是协议在高价值决策中采用了可被短时、低成本操纵的价格信号，而不是“DEX 有漏洞”。必须同时分析 liquidity、window 与 decision size。'),
    36: ('Flash Loan 放大原子性', '它提供瞬时巨额资本和单交易回滚特性，使本来“需要大量资本”的经济攻击变得可行；被攻击协议的错误 invariant 才是根因。'),
    37: ('Access Control 是权限图', '把角色、可调用函数、可修改参数、升级/暂停能力画成矩阵；再检查角色授予/撤销和 role-admin 关系。'),
    38: ('Proxy 模式的差异在 upgrade control plane', 'Transparent 与 UUPS 的核心不只是部署 gas，而是 upgrade logic 位于哪里、admin 如何与普通调用隔离、implementation 如何授权升级。'),
    39: ('Upgradeable storage 是长期 ABI', 'storage slot 顺序一旦进入生产，就类似永久数据 schema。升级必须做 layout compatibility 检查，并警惕 inheritance/order/type change。'),
    40: ('Security Review 从 invariant 开始', '最专业的审计不是扫漏洞列表，而是先列资产与 invariant，再从每个 external/privileged entrypoint 逆向寻找能破坏 invariant 的路径。'),
    41: ('xy=k 是定价约束，不是市场真理', '它定义了在无费用理想模型下 reserve 如何随交易变化；真实价格还受 fee、arbitrage、外部市场和离散交易影响。'),
    42: ('Slippage 包含但不限于 Price Impact', 'price impact 是自己改变 AMM 状态造成的价格变化；slippage 是期望与实际成交结果差异，还可能来自市场变化、ordering 与 MEV。'),
    43: ('Impermanent Loss 是相对基准', '它比较“作为 LP 后的资产价值”与“持有原资产”的差异；手续费收入可能抵消该差异，因此不能把 IL 单独当作最终收益。'),
    44: ('Concentrated Liquidity 把资本部署到价格区间', '收益来自提高活跃价格附近的资本效率，代价是 LP 需要管理 range，价格出区间后持仓与手续费行为发生变化。'),
    45: ('Tick 是离散价格索引', 'v3 使用 tick 对价格做对数离散，并用 sqrtPriceX96 提高乘除和流动性计算效率。面试中应能从 tick 推到 price，而非死记结构体字段。'),
    46: ('Health Factor 是风险状态压缩', '它把多抵押/多债务按 oracle 价格和 liquidation threshold 聚合成风险指标。真正风险仍取决于 oracle、流动性和清算执行能力。'),
    47: ('Over-collateralization 替代传统信用追偿', '无许可借贷缺少现实身份与法律追偿，因此用超额抵押和自动清算把信用风险转成市场/流动性风险。'),
    48: ('Liquidation 是协议的坏账防火墙', '清算 incentive 必须让第三方愿意及时偿债，同时不能过度惩罚用户；极端拥堵时还要考虑 keeper 竞争和可用流动性。'),
    49: ('Stablecoin 先问“谁承担赎回承诺”', 'fiat-backed、crypto-collateralized、endogenous/algorithmic 方案的核心差异在资产负债表与 peg defense，而不是名称。'),
    50: ('Invariant 是 DeFi 设计的第一性原理', '先写“任何状态下必须成立的资产/债务/份额关系”，再定义每个函数如何保持它。测试和审计都围绕 invariant 展开。'),
    51: ('L2 扩容不是“绕开 Ethereum”', 'rollup 把执行移出 L1，但仍把 settlement/DA/proof 等安全关键部分锚定到 Ethereum。扩容收益来自批处理与摊销。'),
    52: ('Optimistic 的关键是可挑战性', '不是“完全没有 proof”，而是默认接受状态并提供时间窗口/机制让错误状态被挑战。安全依赖数据可获得与诚实 challenger 假设。'),
    53: ('ZK vs Optimistic 要按安全路径比较', '一个依赖 validity proof，一个依赖 fraud/challenge；还要比较 DA、EVM compatibility、proving cost、withdrawal/finality，而不是简单贴“ZK 更安全”。'),
    54: ('Blob 是专门的 DA 资源市场', 'EIP-4844 把 rollup data 从普通 calldata 迁到短期 blob data，并引入独立费用市场，从而降低 L2 数据发布成本。'),
    55: ('DA 回答“别人能否重建状态”', '只有 state root 而没有交易/状态差异数据，外部验证者无法重放并验证状态转换。proof correctness 与 data availability 是两个独立维度。'),
    56: ('Sequencer 同时掌握 liveness 与 ordering', '中心化 sequencer 的主要风险是审查、停机与排序权；安全设计需要 forced inclusion、fallback 和明确的 L1 escape path。'),
    57: ('Validium 主要改变 DA 信任', '它仍可有 validity proof，但数据不完全发布到 Ethereum；因此费用更低，同时用户恢复状态依赖额外 DA 假设。'),
    58: ('Bridge 是跨域验证系统', '真正问题不是“把 token 从 A 转到 B”，而是 B 如何验证 A 上事件的真实性、最终性和唯一性，并在验证失败时保护托管资产。'),
    59: ('三性质对应三种保证', 'completeness 保证诚实证明能通过；soundness 约束伪命题；zero-knowledge 约束泄露。工程系统还要考虑 setup、proof system assumptions 与实现安全。'),
    60: ('Rollup 是一组服务 + L1 contracts', 'sequencer、batcher、prover/challenger、bridge、node、DA、L1 contracts 与 governance 共同构成系统。任何单点都要有故障/恶意模型。'),
    61: ('账户的核心是“谁能授权状态变化”', 'EOA 原生绑定私钥签名规则；smart account 把验证逻辑写成代码。账户抽象的价值来自把认证与执行策略从协议固定规则中解耦。'),
    62: ('ecrecover 只是 primitive', '它恢复地址，但不会自动做 domain separation、nonce、expiry、low-s、prefix/type encoding 等高层安全检查。'),
    63: ('Replay 是“有效签名被放到错误上下文”', '同一个字节级签名如果缺少 domain/chain/contract/nonce/action scope，就可能在另一个场景仍被验证为有效。'),
    64: ('EIP-712 提供结构化语义与 domain', '它改善人类可读性和 domain separation，但应用仍需自己加入 nonce/deadline 与权限语义；typed data 不是自动防 replay。'),
    65: ('Permit 把 approve 的授权从 transaction 变为 signature', 'spender/relayer 可提交签名完成 allowance 设置；安全仍依赖 nonce、deadline、domain 与 token 实现正确性。'),
    66: ('AA 是权限系统，不只是免 gas', 'social recovery、session key、batching、sponsorship 都意味着更复杂的授权模型。UX 提升必须与可撤销性和最小权限一起设计。'),
    67: ('4337 把“用户操作”变成独立验证流水线', 'UserOperation 先在 alt mempool/bundler 环境验证，再由 EntryPoint 在链上统一处理 account validation、paymaster 与 execution。'),
    68: ('Paymaster 是 gas sponsor policy engine', '它既承担资金，又执行谁可被赞助的策略。必须防止模拟/执行差异、griefing、deposit drain 与 sponsor abuse。'),
    69: ('7702 与 4337 是互补层次', '7702 改变 EOA 可委托代码的协议能力；4337 提供 UserOp/bundler/paymaster/EntryPoint 生态。现代账户可结合二者而不是二选一。'),
    70: ('Smart Wallet 的核心资产是“授权能力”', '钱包安全不仅保护 ETH/token，还要保护 owner、recovery、module、session-key、upgrade 与 sponsor policy。模块化越强，权限图越需要可审计。'),
    71: ('共识执行要求确定性输入', '普通 HTTP 可能因时间、节点、地区或服务状态得到不同结果，因此不能直接进入共识执行。Oracle 的职责是把外部事实转换成可验证/可治理的链上输入。'),
    72: ('Oracle 可靠性是组合属性', 'source diversity、aggregation、freshness、deviation、fallback、governance 与 economic security 共同决定可用性；“用了知名 oracle”不是完整答案。'),
    73: ('MEV 来自排序权与状态依赖', '如果交易结果依赖前后顺序，能控制 inclusion/order 的参与者就可能提取额外价值。分析 MEV 应从用户损失和协议设计出发。'),
    74: ('三者是不同排序位置', 'front-run 在目标前，back-run 在目标后，sandwich 同时夹住目标。面试中重点应放在 slippage、private orderflow、batch auction 等防御设计。'),
    75: ('Public Mempool 暴露“尚未执行的意图”', '这是 Web2 后端很少面对的威胁模型：攻击者可以在交易执行前读取参数、模拟结果并提交竞争交易。'),
    76: ('JSON-RPC 是节点能力的远程边界', 'RPC 方法提供链状态读取、模拟、交易广播与日志访问。生产系统要区分 provider API 与协议本身，并处理 rate limit/stale response。'),
    77: ('节点类型是存储/验证权衡', 'Full node 维护验证当前链所需状态；archive 额外保留历史状态；light client 用更少资源验证必要证明。业务选型取决于查询需求与信任边界。'),
    78: ('Indexer 是派生读模型', '它把 append-only block/log 转换成可查询数据库。数据库可以重建，所以 source of truth 仍是 canonical chain；这决定了 reorg rollback 设计。'),
    79: ('Reorg 处理的核心是可逆派生状态', '每个派生更新必须能追溯到 block hash；检测 parent mismatch 后找到 common ancestor，回滚 orphaned blocks，再按新 canonical chain replay。'),
    80: ('RPC 高可用不等于随机切 provider', '不同 provider 可能处于不同 head 或配置。生产 failover 需要健康检查、head consistency、方法级能力矩阵、timeout/circuit breaker。'),
    81: ('Solana 显式账户列表换取并行调度信息', 'Ethereum contract 可在执行中动态访问全局状态；Solana instruction 预声明 accounts，让 runtime 更容易推断读写冲突并并行执行。'),
    82: ('Solana Account 是通用状态容器', '它可能承载余额、程序数据或程序代码，不应与 Ethereum EOA 等同。owner 字段决定哪个 program 可修改 data。'),
    83: ('Program stateless 指“状态外置”', '程序逻辑驻留在 executable program，而可变业务状态保存在 data accounts；升级和账户 ownership 仍是重要控制面。'),
    84: ('PDA 是 runtime 可授权的确定性地址', '它由 seeds + program id 推导且位于曲线外，没有私钥；program 通过 `invoke_signed` 证明 seeds 来代表 PDA 签名。'),
    85: ('CPI 是 Solana 的 composability 边界', 'Program A 调用 B 时需要传递账户与 signer/writable 权限。审计重点是权限是否被过度转发以及被调用 program 是否可信。'),
    86: ('并行性来自可预测的读写集合', 'runtime 根据 transaction 声明的账户锁判断冲突；共享热门 writable account 会成为 contention hotspot，限制理论并行度。'),
    87: ('两条链都提供 transaction-level atomicity', '差异主要在 transaction 内部表达：Ethereum 通过 call tree，Solana 通过多个 instructions + accounts；失败语义和费用/资源限制也不同。'),
    88: ('Multi-chain 的难点是语义异构', '地址、签名、nonce、fee、token、finality、RPC、simulation 都不同。好的抽象统一用户 intent，而不是伪装底层语义完全一致。'),
    89: ('跨链 token 首先是会计系统', '无论 lock/mint 还是 burn/mint，都要定义全局 supply invariant、消息唯一性和故障补偿；bridge message 成功不代表会计必然正确。'),
    90: ('Wallet SDK 要统一接口、保留链语义', '公共层负责 intent、signer、status；adapter 层负责 chain-specific address/fee/transaction/finality。错误模型必须携带足够链上下文。'),
    91: ('O(1) staking 的关键是累计指数', '不要逐用户更新时间。维护全局 `rewardPerTokenStored`，每个用户只在交互时结算 `earned += balance*(global-userPaid)`，把成本从用户数量解耦。'),
    92: ('Withdraw review 先画资金与状态顺序', '检查 authorization、余额变化、external call、返回值、reentrancy、token 行为和事件。不要只搜索 `call.value` 这种历史模式。'),
    93: ('Marketplace 的核心是订单状态机', 'listing/order、signature、nonce、expiry、fill、fee/royalty、asset transfer 共同构成结算协议。高级设计通常偏向 offchain order + onchain settlement。'),
    94: ('Governance 是控制面，不只是投票 UI', 'proposal creation、voting power snapshot、quorum、timelock、execution、guardian 与 upgrade authority 都必须进入威胁模型。'),
    95: ('Multisig 的 invariant 是阈值授权 + 唯一执行', '交易哈希必须绑定 chain/wallet/nonce/action；签名去重、owner 变更和 threshold 修改都要防 replay 与自锁死。'),
    96: ('Vesting 是时间函数 + 已领取会计', '核心 invariant 是 `claimed <= vested(t) <= allocation`，同时要定义 cliff、revocation、rounding、beneficiary 与 token 异常行为。'),
    97: ('Indexer 的本质是可重放状态机', '任何数据库行都应该能追溯到 canonical block/event，并支持从 checkpoint 重建。高可靠性来自幂等、回滚、backfill 与多 RPC 校验。'),
    98: ('Deposit System 先做 ledger，再做余额', '链上 deposit 只是外部事实，内部 credit 必须通过可审计双重记账和 confirmation policy；reorg 后需要冻结/冲正而不是直接减余额。'),
    99: ('交易失败要先定位生命周期层级', '构造/签名、广播、mempool、inclusion、execution/revert、finality、frontend/indexer 每层都有不同证据。先拿 hash/chain/receipt/trace，再做假设。'),
    100: ('Staff 题的答案是“端到端不变量 + 降级路径”', '除了组件图，必须解释资产如何保持安全、授权如何验证、依赖如何失败、状态如何恢复、谁能升级，以及用户最坏情况下如何退出。'),
}

ROLE_FOCUS = [
    ('安全', '把攻击者能力、资产、不变量、可利用前提和 mitigation 说完整；不要止于 API 定义。'),
    ('协议', '强调状态机、共识/经济假设、不变量、边界条件和 protocol-level trade-off。'),
    ('后端', '强调幂等、reorg、RPC/节点一致性、数据模型、重试与可观测性。'),
    ('钱包', '强调签名域、nonce/replay、用户授权范围、链切换与错误恢复。'),
    ('Solidity', '强调 EVM 语义、storage/call context、gas、安全测试与部署约束。'),
    ('DeFi', '强调资产守恒、oracle、liquidity、rounding、清算与极端市场。'),
    ('AA', '强调 validation/execution/gas sponsorship/recovery/module permissions。'),
    ('Senior', '主动补 failure mode、migration/upgrade、observability 和 blast radius。'),
    ('Staff', '从局部机制上升到端到端信任边界、SLO、控制面与事故恢复。'),
]


def qfile(qid: int) -> Path:
    candidates = list((ROOT/'docs').glob(f'[0-9][0-9]-*/q{qid:02d}.md')) + list((ROOT/'docs').glob(f'[0-9][0-9]-*/q{qid}.md'))
    if not candidates:
        raise FileNotFoundError(qid)
    return candidates[0]


def related_questions(q):
    qt = set(q.get('tags', [])) - {'web3', 'interview', 'core-30'}
    scored=[]
    for other in QUESTIONS:
        if other['id']==q['id']:
            continue
        ot=set(other.get('tags', [])) - {'web3','interview','core-30'}
        overlap=len(qt & ot)
        same=1 if other['chapter']==q['chapter'] else 0
        distance=max(0, 5-abs(other['id']-q['id']))/10
        score=overlap*3+same+distance
        if score>0:
            scored.append((score, other))
    scored.sort(key=lambda x:(-x[0], x[1]['id']))
    picked=[]
    for _,o in scored:
        if len(picked)>=5: break
        if o not in picked: picked.append(o)
    return picked


def rel_link(src_q, other):
    src = qfile(src_q['id'])
    dst = qfile(other['id'])
    rel = Path(__import__('os').path.relpath(dst, src.parent)).as_posix()
    return f"[Q{other['id']:02d} {other['title']}]({rel})"


def role_paragraph(q):
    roles=q.get('roles','')
    hits=[]
    for k,text in ROLE_FOCUS:
        if k.lower() in roles.lower() or k in roles:
            hits.append(f'- **{k} 视角**：{text}')
    if not hits:
        hits.append('- **通用工程视角**：先给定义，再给机制、边界、失败模式、测试与生产取舍。')
    # Always add interviewer escalation
    hits.append('- **高级面试升级**：最后补一句“这个结论依赖哪些假设、线上怎样观测、出现异常如何回滚/降级”，通常能明显区分 Senior 与纯知识型回答。')
    return '\n'.join(hits)


def formal_model(q, profile):
    formulas=q.get('formula') or []
    if formulas:
        fs='；'.join(f'`{x}`' for x in formulas)
        return f"本题已有公式/关系：{fs}。不要只背公式，要逐个说明变量的物理/协议含义、单位、取值边界以及公式失效的前提。\n\n在此基础上，{profile['model']}"
    return profile['model']


def concepts(q):
    lines=[]
    for i,k in enumerate(q.get('keypoints',[])[:6],1):
        lines.append(f'{i}. **{k}**：面试中需要把它从关键词展开成“定义 → 机制 → 边界 → 工程后果”，不能只念术语。')
    return '\n'.join(lines)


def question_case(q):
    title=q['title']
    chapter=q['chapter']
    if chapter==1:
        return f"你在做一个需要处理 **{title.replace('？','')}** 的交易平台/协议服务。请分别写出“协议保证”“应用层仍需自行保证”的内容，并给出一次 reorg 或节点分歧时的恢复方案。"
    if chapter==2:
        return f"给定一个包含多层 external call 的交易，围绕 **{title.replace('？','')}** 画出 call frame、storage context、calldata/return data 和 gas 消耗边界；然后说明如何用 trace 证明你的判断。"
    if chapter==3:
        return f"把 **{title.replace('？','')}** 落成一段最小 Solidity 示例：先写最直观版本，再写生产版本，并用测试证明两者在功能、安全或 gas 上的差异。"
    if chapter==4:
        return f"围绕 **{title.replace('？','')}** 构造一个最小可利用场景：写出攻击者前提、资产、被破坏 invariant、调用序列、影响和 mitigation，并给出至少一个能长期防回归的 invariant test。"
    if chapter==5:
        return f"围绕 **{title.replace('？','')}** 建立一张协议资产负债表，模拟价格跳变、流动性下降或高 gas 情况，说明哪个风险参数先触发、协议如何保持 solvency。"
    if chapter==6:
        return f"围绕 **{title.replace('？','')}** 画 `L2 → DA → L1` 状态时间线，分别标注用户看到成功、系统可挑战/证明、L1 finalized 的时点，并说明 sequencer/prover/DA 任一故障时用户资产怎样退出。"
    if chapter==7:
        return f"围绕 **{title.replace('？','')}** 设计一次授权：明确 signer、domain、chainId、nonce、deadline、scope、gas payer 和 revoke path，然后逐项尝试 replay / privilege escalation。"
    if chapter==8:
        return f"围绕 **{title.replace('？','')}** 做一次故障演练：让主 RPC/Oracle/Indexer 产生 stale 或 forked view，说明系统如何检测、切换、回滚以及避免重复副作用。"
    if chapter==9:
        return f"围绕 **{title.replace('？','')}** 同时画 Ethereum 与 Solana 的状态/账户访问，明确 signer、owner、writable accounts 与 finality，再说明统一 SDK 层应该暴露什么、隐藏什么。"
    return f"把 **{title.replace('？','')}** 作为真实系统设计题：先写需求和 invariant，再给组件/状态机/数据模型，最后完成故障注入、安全测试、容量估算和事故恢复方案。"


def build_enrichment(q):
    p=CHAPTER_PROFILES[q['chapter']]
    special_title, special_text = SPECIAL[q['id']]
    related=related_questions(q)
    rels='\n'.join(f'- {rel_link(q,o)}：建议用“相同底层机制 / 不同应用边界”方式对比复习。' for o in related)
    failure_lines='\n'.join(f'- {x}' for x in (q.get('pitfalls',[]) + p['failures']))
    eng_lines='\n'.join(f'- {x}' for x in p['engineering'])
    test_lines='\n'.join(f'- [ ] {x}' for x in p['tests'])
    obs_lines='\n'.join(f'- `{x}`' for x in p['obs'])
    prereq_lines='\n'.join(f'- {x}' for x in p['prereqs'])
    keyconcepts=concepts(q)
    return f"""
{START}
### 6.3 前置知识与概念边界

这题属于 **{p['name']}**。以下 6.3–6.12 属于 **GitHub 专业深化（通用工程知识与推导）**，并非 PDF 原文；PDF 主干仍以上文第 1–5 节为准。\n\n在进入细节前，建议先确认下面三个前置层次：

{prereq_lines}

本题已有关键点可以进一步拆成：

{keyconcepts}

> **边界原则**：能回答“它是什么”只能达到基础分；高级回答必须继续回答“它不是什么、依赖什么假设、失败时会怎样”。

### 6.4 形式化模型 / 白板推导

{formal_model(q,p)}

白板时建议固定使用以下推导顺序：

1. **对象**：列出参与者、状态、资产或数据结构；
2. **输入**：哪些交易/消息/价格/签名会驱动状态变化；
3. **规则**：哪些条件决定有效、排序、授权或价格；
4. **状态变化**：写出成功路径和失败/回滚路径；
5. **Invariant**：任何正常或恶意输入下必须保持什么；
6. **Trust assumption**：哪些条件不是代码能独立保证的。

### 6.5 本题最值得深挖的一层：{special_title}

{special_text}

如果面试官继续追问，不要立刻换新术语。先从上述核心模型推出一个**具体后果**，再给一个**反例或边界条件**，最后说明**生产系统如何验证/缓解**。

### 6.6 生产工程决策

{eng_lines}

对本题而言，工程答案最好至少包含一个“**正常路径**”和一个“**故障路径**”。前者证明你理解功能，后者证明你理解系统。

### 6.7 Threat Model / Failure Modes

把失败模式分成三类会更专业：

- **语义错误**：概念或状态模型理解错，导致实现从根上错误；
- **对抗性输入**：攻击者利用排序、回调、价格、签名、权限等主动破坏假设；
- **系统性故障**：RPC、节点、sequencer、oracle、数据库或管理员路径异常。

本题重点检查：

{failure_lines}

> 面试时最好把“风险”改写成可验证句式：**在条件 A 下，攻击者/故障 B 可以让状态 C 违反 invariant D，影响资产/可用性 E。**

### 6.8 测试策略：Unit → Fuzz → Invariant → Integration

{test_lines}

进一步建议：

- **Unit test**：验证局部 API 与边界输入；
- **Fuzz test**：搜索你没有手工枚举的输入组合；
- **Invariant test**：验证任意调用序列下核心关系仍成立；
- **Integration/Fork test**：验证真实 token、oracle、RPC、链状态或跨合约行为；
- **Failure injection**：主动让依赖超时、重组、停机、返回异常，验证恢复路径。

### 6.9 可观测性与线上排障

如果这道题变成线上事故，不要只说“看日志”。先定义你要观察的**链上事实、派生状态与外部依赖**。本章常用信号包括：

{obs_lines}

排障顺序建议固定为：

```text
用户现象
  ↓
确认 chain / tx / block / request identity
  ↓
确认 source of truth
  ↓
定位状态机停在哪一步
  ↓
查看依赖与权限变化
  ↓
复现 / simulate / trace
  ↓
决定 retry / rollback / pause / compensate
```

### 6.10 不同岗位如何回答同一道题

{role_paragraph(q)}

### 6.11 面试官评分 Rubric

| 层级 | 候选人表现 | 典型判断 |
|---|---|---|
| **0 - 术语记忆** | 只能给一句定义，追问就断 | 不足以独立处理生产问题 |
| **1 - 机制理解** | 能解释核心流程和关键对象 | 基础工程能力 |
| **2 - 边界意识** | 能主动指出前提、反例和 Failure Mode | 中高级候选人信号 |
| **3 - 工程闭环** | 能给测试、监控、回滚、兼容性与成本取舍 | Senior 信号 |
| **4 - 系统推导** | 能用 invariant / trust model 串起上下游并提出替代设计 | Staff / Protocol 信号 |

### 6.12 关联题：把知识连成网络

{rels}

不要把 100 题当成 100 个孤立答案。真正的面试常从当前题连续跳到 storage、signature、oracle、reorg、upgrade、MEV 或 system design；建立跨题连接比继续背更多定义更重要。
{END}
""".strip()


def build_lab(q):
    related=related_questions(q)[:3]
    rel='、'.join(f'Q{o["id"]:02d}' for o in related)
    return f"""
{LAB_START}
### 10.1 实战训练：把这题变成可展示的工程证据

**场景任务**：{question_case(q)}

建议输出物：

1. 一张状态机 / 资产流 / 调用图；
2. 一份 10～30 行的最小代码、伪代码或数据结构；
3. 3 个 happy-path 测试 + 3 个 adversarial/failure-path 测试；
4. 至少 1 个 invariant；
5. 一段 2 分钟口述答案，要求不看稿；
6. 与 **{rel}** 做一次对比复盘，说明相同底层机制与不同工程边界。

### 10.2 反向面试：你可以问面试官什么

为了判断团队真实工程成熟度，可以围绕本题反问：

- 这个系统当前最关键的 invariant / SLO 是什么？
- 过去出现过哪类与本题相关的线上事故或审计问题？
- 团队如何做 fork/invariant/failure-injection 测试？
- 协议升级或依赖变更时，谁负责 compatibility review 和 rollback plan？
- 哪些安全/可靠性判断是链上强制，哪些依赖 off-chain service 或人工流程？

这些问题既能帮助你了解岗位，也能体现你关注**长期正确性和运行质量**，而不只是完成一次编码任务。
{LAB_END}
""".strip()


def replace_or_insert(txt: str, start: str, end: str, block: str, before_pattern: str) -> str:
    if start in txt and end in txt:
        pattern=re.escape(start)+r'.*?'+re.escape(end)
        return re.sub(pattern, block, txt, flags=re.S)
    m=re.search(before_pattern, txt, flags=re.M)
    if not m:
        raise ValueError(f'Cannot find insertion point: {before_pattern}')
    return txt[:m.start()] + block + '\n\n' + txt[m.start():]


def enrich_questions():
    for q in QUESTIONS:
        f=qfile(q['id'])
        txt=f.read_text(encoding='utf-8')
        txt=replace_or_insert(txt, START, END, build_enrichment(q), r'^## 7\. 高频追问与回答方向')
        txt=replace_or_insert(txt, LAB_START, LAB_END, build_lab(q), r'^## 11\. 参考资料')
        f.write_text(txt, encoding='utf-8')


def enrich_chapter_indexes():
    for ch in range(1,11):
        idx=list((ROOT/'docs').glob(f'{ch:02d}-*/index.md'))[0]
        txt=idx.read_text(encoding='utf-8')
        marker_start='<!-- CHAPTER_ENRICHMENT_START -->'
        marker_end='<!-- CHAPTER_ENRICHMENT_END -->'
        p=CHAPTER_PROFILES[ch]
        qs=[q for q in QUESTIONS if q['chapter']==ch]
        easy=sorted(qs,key=lambda q:(len(q['difficulty']),q['id']))[:3]
        hard=sorted(qs,key=lambda q:(-len(q['difficulty']),q['id']))[:3]
        block=f"""{marker_start}
## 本章专业学习框架

### 前置知识
{chr(10).join('- '+x for x in p['prereqs'])}

### 统一分析模型

{p['model']}

### 从基础到高级的学习顺序

- **建立模型**：{'、'.join(f'Q{q["id"]:02d}' for q in easy)} —— 先确保基础对象与状态边界不混淆。
- **形成工程闭环**：完成本章全部题目的 failure mode、测试和 observability 小节。
- **冲击高级面试**：{'、'.join(f'Q{q["id"]:02d}' for q in hard)} —— 尝试用 invariant / trust model 在白板上连续讲 5～10 分钟。

### 本章实验建议

1. 选 2 道题写最小可运行 demo；
2. 为其中 1 道加入 fuzz/invariant 或 failure injection；
3. 写一份 1 页 incident note：现象、根因、影响、修复、长期预防；
4. 把结果放进个人 GitHub，面试时作为可验证工程证据。

### 本章生产 Checklist

{chr(10).join('- [ ] '+x for x in p['tests'])}
{marker_end}
"""
        if marker_start in txt and marker_end in txt:
            txt=re.sub(re.escape(marker_start)+r'.*?'+re.escape(marker_end),block,txt,flags=re.S)
        else:
            # insert before 题目列表
            txt=txt.replace('## 题目列表', block+'\n\n## 题目列表',1)
        idx.write_text(txt,encoding='utf-8')


def update_stats_and_changelog():
    qfiles=[qfile(i) for i in range(1,101)]
    chars=[len(f.read_text(encoding='utf-8')) for f in qfiles]
    stats=json.loads((ROOT/'data/repo_stats.json').read_text(encoding='utf-8'))
    stats.update({
        'question_markdown_chars_total': sum(chars),
        'question_markdown_chars_avg': sum(chars)//len(chars),
        'question_markdown_chars_min': min(chars),
        'question_markdown_chars_max': max(chars),
        'enrichment_version': 'v2-professional-deep-dive',
        'professional_enrichment_sections_per_question': 12,
    })
    (ROOT/'data/repo_stats.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

    ch=ROOT/'CHANGELOG.md'
    txt=ch.read_text(encoding='utf-8')
    entry='''## 2026-09-02 · v2 Professional Deep Dive\n\n- 全量增强 Q01–Q100：新增前置知识、形式化模型、关键深挖、生产工程决策、Threat Model、Failure Modes、测试策略、可观测性、岗位差异、评分 Rubric、关联题与实战训练。\n- 每章新增统一分析模型、实验建议与生产 Checklist。\n- 新增可重复执行的 `scripts/enrich_questions.py`，保证后续内容升级可维护、可重建。\n- 更新 repo stats，并继续保持 PDF → Markdown 一一映射。\n\n'''
    if 'v2 Professional Deep Dive' not in txt:
        # after main heading
        pos=txt.find('\n', txt.find('#'))+1
        txt=txt[:pos]+'\n'+entry+txt[pos:]
        ch.write_text(txt,encoding='utf-8')


def main():
    enrich_questions()
    enrich_chapter_indexes()
    update_stats_and_changelog()
    print('Enriched 100 question files + 10 chapter indexes.')

if __name__=='__main__':
    main()
