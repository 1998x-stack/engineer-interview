# M04 · Tool Gateway / Durable Recovery Failure Lab

> 本模块新增的**可执行教学实验**；不是 PDF 原有 100 题的一部分，也不是生产级 Agent Runtime。

该实验把 [Q023 timeout](../questions/03-tools-mcp/q023.md)、[Q024 幂等](../questions/03-tools-mcp/q024.md)、[Q063 crash window](../questions/07-durable-execution/q063.md)、[Q081 Prompt Injection](../questions/09-security-hitl/q081.md) 与 [Q089 授权边界](../questions/09-security-hitl/q089.md) 的 invariant 映射为可检验的 Python 测试。

## 文件与运行

- `examples/tool_gateway.py`：标准库 SQLite 操作日志、能力策略、显式审批、请求指纹和远端对账。
- `tests/test_tool_gateway.py`：超时、崩溃、重放、跨租户、未授权操作、参数冲突及审批的故障注入。
- `scripts/check_contracts.py`：题库 JSON/CSV/Markdown frontmatter 契约、PDF SHA-256 真实一致性。

在模块根目录运行：

```bash
python -m pip install pytest
python scripts/validate_repo.py
python scripts/check_contracts.py
python scripts/build_index.py --check
python scripts/check_links.py
python -m pytest -q tests
```

全部使用 Python 3.12 和标准库，只有测试运行器需 `pytest`。

## 关键状态迁移

```text
Proposal + trusted Identity
        ↓
trusted policy / independent approval
        ↓
canonical args digest + durable SQLite reservation (IN_FLIGHT)
        ↓
trusted tool adapter (operation_id, args)
        ├── returns JSON business result → SUCCEEDED
        ├── timeout / exception        → UNKNOWN
        └── process crash              → IN_FLIGHT persists
                                       ↓
On restart: IN_FLIGHT / UNKNOWN -> block replay
                                       ↓
Trusted API lookup(operation_id) -> authoritative COMMITTED result
                                       ↓
                                   SUCCEEDED
```

### 不变量与反例

| 要求 | 故障注入 | 预期 |
|---|---|---|
| 不允许未授权跨租户 Tool | 伪造网页文本要求赋权 | Gateway 仍拒绝 |
| 写入前保存 operation_id | 成功远端动作后进程崩溃 | 重启时识别 IN_FLIGHT，禁止直接重放 |
| timeout ≠ 未执行 | Tool 抛出 TimeoutError | 标记 UNKNOWN，不会自动再次调用 |
| 幂等键是业务请求身份 | 同 operation_id 修改 args 或 tool | 抛 IdempotencyConflict |
| 审批来自独立可信策略 | 自己填写 `approval_id` 字符串 | 未在可信审批表中验证则拒绝 |
| Reconciliation 不等于 retry | 远端查询得到 None | 维持 UNKNOWN，不能自行重发 |
| 成功之后 replay 无额外副作用 | 两个 Gateway 实例访问同一 SQLite 文件 | 读取保存的 canonical result |

## 信任边界与限制

1. `Identity`、`capabilities` 和 `approvals` 必须由可信调用层注入，**不能从模型建议、网页、检索结果、Prompt 或客户端传来的未认证 JSON 中读取为事实**。
2. 业务 API 必须独立执行 AuthN/AuthZ，必要时使用稳定 `operation_id` 去重；本地 SQLite 只保护**共享同一账本的调用者**，不能保证跨机器数据库、第三方服务的端到端 exactly-once。
3. `reconcile_committed` 的 `lookup` 必须是已认证、可审计、可信的远端状态查询。返回 `None` 并不证明操作失败，故不会自动重放。
4. 示例不是 Sandbox、凭证管理系统、分布式锁或实际工具执行平台。生产需补充独立的资源侧授权、强审批流程、参数 Schema 校验、加密存储/敏感结果脱敏、跨进程恢复调度、超时预算和 SLO。
5. 查询成功前的 **crash window** 被保守视为未确认；不能以“checkpoint 每秒写一次”替代外部对账。
6. 测试利用假的受信任业务 API，验证关键状态不变量；不等于第三方系统真实一致性验证。

## 下一阶段实验

M04.2 可将教学参考扩展为**可重放 Agent Loop**：转移事件日志、step/token/deadline budget、独立 isolated runner、trajectory evaluator，以及 Tool Gateway + 模型调度器的分层接口。应在当前安全边界与失败窗口测试稳定后继续。
