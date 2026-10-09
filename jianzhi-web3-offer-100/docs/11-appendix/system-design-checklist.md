# Web3 System Design 速查框架

1. 先定义用户 Intent 与资产安全目标。
2. 画端到端数据流：Wallet -> RPC/Bundler -> Chain -> Logs -> Indexer -> DB -> UI。
3. 画交易状态机：Created -> Signed -> Submitted -> Included -> Finalized；外加 Replaced/Reorged/Failed。
4. 列出每个外部依赖：RPC、Oracle、Sequencer、Bridge、Signer、DB。
5. 为每个依赖写 Timeout / Retry / Idempotency / Fallback。
6. 列出 privileged roles 与最大 blast radius。
7. 定义资产/账本 invariants。
8. 设计 Reorg / replay / duplicate / backfill / disaster recovery。
9. 最后才谈缓存、分片、吞吐与成本优化。
