# Agent Failure Taxonomy

PDF 附录 C 的 GitHub 化与扩展版本。

| 层 | 典型症状 | 应查看的证据 | 典型修复 |
|---|---|---|---|
| Model | 推理错误、误解目标、过早结束 | model response / reasoning-independent signals | 换模型或 targeted prompting |
| Context | 遗漏关键信息、污染、过时 | retrieval set / token composition | filter / compact / reset / retrieval |
| Tool Interface | 选错工具、参数错误 | tool-call distribution / schema errors | rename / schema / examples / retrieval |
| Tool Runtime | timeout、partial failure | latency/error / operation state | retry / idempotency / saga |
| Policy/Security | 误拒绝、越权 | policy decision trace | risk model / scoped grants / sandbox |
| State | 丢进度、stale/conflict | checkpoint / version / event log | CAS / event sourcing / reconciliation |
| Environment | 依赖漂移、脏状态 | env hash / git / package state | pin / reset / verify baseline |
| Eval | grader 偏差、泄漏 | human disagreement / tamper evidence | calibration / isolation / new grader |
| Infra | rate limit、容量、网络 | provider metrics / queue / fleet | backoff / admission / capacity |

## 调试原则

先判断“失败发生在哪一层”，再改那一层。最常见的无效工作，是把工具设计、环境、grader 和状态问题全部用 prompt patch 掩盖。

## Repo 增补：Failure Record 模板

```yaml
failure_id: F-2026-001
run_id: ...
symptom: ...
layer: tool_runtime
impact: ...
reproduction: ...
evidence:
  trace_span: ...
  state_diff: ...
root_cause: ...
fix: ...
regression_case: evals/cases/...
rollout_guard: ...
```

每个高损失线上失败，最终都应沉淀成“minimal reproduction + grader + regression”。


## Failure Signature → First Debug Action

| Signature | 首查 | 常见根因 | 下一步实验 |
|---|---|---|---|
| 模型反复调用同一工具 | tool trace + error contract | observation 不可行动、retry policy 错误 | 固定模型，替换结构化 error |
| Agent 说完成但验收失败 | stop reason + verifier | model-declared completion 被当事实 | 强制 environment verification |
| crash 后出现重复外部动作 | operation ledger | 缺 idempotency/reconciliation | kill at side-effect/checkpoint window |
| 长任务后半段质量下降 | context/state diff | context rot、plan drift、stale state | phase-length / reset ablation |
| Multi-Agent 成本暴涨但质量不变 | worker trace | duplicate work、fan-out 过大 | 降并发/限制子任务依赖 |
| 安全审批很多但事故仍发生 | policy/audit | approval fatigue、sandbox 不足 | permission vs sandbox ablation |
| Eval 突然掉点 | grader/env version | eval noise、环境漂移、grader change | old/new matrix |
| p95 latency 激增 | critical-path spans | tool tail、queue、serial turns | phase-level latency decomposition |

## Incident Reduction 模板

将一次生产失败沉淀为 eval 时，保留：

1. **最小触发条件**；
2. **期望环境状态与实际状态**；
3. **首次分叉的 trace span/event**；
4. **failure class**；
5. **是否涉及安全/副作用**；
6. **可重复运行的 grader**；
7. **修复后必须长期守住的 regression assertion**。
