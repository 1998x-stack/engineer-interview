# Reliability First：Agent 故障题六步框架

> 面试官问“Agent 出问题怎么办”时，最差的开场通常是：“加 retry。”

正确顺序是：

```text
Detect → Classify → Contain → Recover → Preserve → Verify
```

## 1. Detect — 怎么知道出问题了？

任何防护机制先要有 signal。典型 Agent 信号包括：

- `step_count` 异常增长。
- 相同 `tool_name + args_hash` 重复出现。
- `state_hash` 多轮不变化。
- retrieval evidence set 没有增加。
- tool timeout/error rate 激增。
- task milestone 长时间未推进。
- token velocity 或 cost/run 异常。

**高级回答**会给阈值或趋势，而不只说“加监控”。

## 2. Classify — 问题属于哪一层？

推荐 taxonomy：

```text
Goal / Requirement
Planner / Reasoning
Context / Memory
Retrieval / Evidence
Tool / External API
State / Reducer
Coordination / Multi-Agent
Runtime / Infra
Security / Permission
Business Invariant
```

先分类的价值：避免检索错误却去改 Prompt，也避免 Tool 返回正确但 State reducer 写错时误判模型。

## 3. Contain — 怎么阻止故障扩散？

Containment 的目标是限制 blast radius：

- `max_steps / max_depth / TTL / token budget`。
- Circuit Breaker。
- Tool allowlist / least privilege。
- cancellation token。
- HITL interrupt。
- 租户隔离和 resource-level authorization。
- 关闭高风险写操作，只保留 read-only degradation path。

## 4. Recover — 怎么恢复？

按错误类型选择机制：

| 情况 | 典型恢复 |
|---|---|
| 瞬时网络错误 | retry + backoff + jitter |
| 副作用状态未知 | query/reconcile + same operation_id |
| Plan 假设失效 | local/global replan |
| 缺少用户关键信息 | clarify |
| 下游持续故障 | fallback / circuit open |
| 部分事务失败 | Saga / compensation |
| Worker crash | checkpoint resume |
| 高风险不确定 | HITL |

注意：**Recover 不等于 Retry**。

## 5. Preserve — 哪些东西绝对不能丢？

至少考虑：

- 业务 goal / constraints。
- task/run/step identity。
- operation_id / idempotency key。
- 已完成副作用和 canonical result。
- approval decision。
- artifact refs / evidence provenance。
- checkpoint version。
- trace correlation。

尤其不要把这些事实只放进自然语言 summary。

## 6. Verify — 怎么证明修好了？

修复完成需要证据：

1. **Replay**：历史失败轨迹重放。
2. **Fault Injection**：主动制造 timeout、duplicate、crash、乱序。
3. **Regression Eval**：证明没有伤害其他任务。
4. **Canary**：小流量上线。
5. **Production Metric**：目标 failure class 的发生率实际下降。

## 示例：支付 Tool timeout

用户要求退款，远端已经执行成功，但响应在网络中丢失。

### 错误回答

```text
timeout -> retry 3 times
```

### Reliability First

```text
Detect
  -> HTTP timeout / no canonical result
Classify
  -> Tool / Side Effect / Unknown outcome
Contain
  -> 禁止生成新 operation_id 的盲目重试
Recover
  -> query/replay with same operation_id
Preserve
  -> operation_id + request hash + approval_id
Verify
  -> duplicate_refund_rate = 0 in fault injection
```

## 面试表达模板

> “我不会先直接 retry。先根据 trace 判断是 model、retrieval、tool 还是 state failure；如果是 tool timeout，还要区分 read-only 和 side effect。副作用操作进入 UNKNOWN 状态，用持久化 operation_id 查询或幂等重放；超过 retry/deadline budget 再 fallback 或 HITL。整个过程保留 checkpoint 与 trace，最后用故障注入和 regression eval 验证。”

## 什么时候这个框架尤其有价值？

- Tool timeout / partial success。
- Worker crash。
- Multi-Agent 消息重复、乱序。
- Context/Memory 污染。
- RAG 错误驱动动作。
- 成功率线上突降。
- Prompt Injection / 权限问题。

---

## Expanded Edition 使用提示

阅读任何章节时，优先寻找三个东西：**Invariant、Failure Window、Verification Signal**。如果一个方案只有组件名而没有这三项，它通常还停留在 demo 级。完整方法见 [Expanded Edition 内容设计规范](12-expanded-edition-methodology.md)。
