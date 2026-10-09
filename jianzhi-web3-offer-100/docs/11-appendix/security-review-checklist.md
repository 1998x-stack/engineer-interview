# Solidity Security 速查清单

- [ ] 资产：合约持有哪些 ETH/token/share/claim？最大 TVL/单笔价值是多少？
- [ ] 权限：owner/admin/upgrader/pauser/oracle setter/treasury 各自能造成什么最坏后果？
- [ ] 外部调用：CALL/delegatecall/token callback/hook 之前是否恢复 invariant？
- [ ] Accounting：shares/assets、debt/collateral、fee、rounding direction 是否始终一致？
- [ ] Oracle：freshness、deviation、decimals、liquidity、sequencer downtime、fallback？
- [ ] Upgrade：initializer、storage layout、implementation lock、authorizeUpgrade、timelock？
- [ ] DoS：unbounded loop、push payment、单个恶意用户能否阻塞全局进度？
- [ ] Token compatibility：fee-on-transfer、rebasing、ERC777 callback、non-standard return？
- [ ] Testing：unit + fuzz + invariant + fork + static analyzer + adversarial receiver。
