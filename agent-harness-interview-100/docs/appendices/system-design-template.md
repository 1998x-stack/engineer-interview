# Agent System Design 白板模板

PDF 附录 B 的工程化版本。

## 11 步白板顺序

1. Clarify Goal / Success Metric
2. Environment & Trust Boundary
3. Observation / Context Sources
4. Action Space / Tool Registry
5. Agent Loop / Orchestration
6. State / Memory / Checkpoint
7. Permission / Identity / Sandbox
8. Failure Recovery / Idempotency
9. Eval / Trace / Monitoring
10. Cost / Latency / Capacity
11. Rollout / Regression / Ablation

> **面试技巧**：先画“最小闭环”，再补横切能力。不要一上来画 20 个微服务。面试官通常更关心：成功条件、状态语义、失败恢复和安全边界是否清晰。

## 主动给出的 SLO / 指标

- Task success / solve rate
- pass^k / stable-success rate
- p50 / p95 end-to-end latency
- average turns / tool calls
- tokens / cost per successful task
- human intervention rate
- unsafe / blocked action rate
- resume success / recovery time

## 推荐 45 分钟节奏

| 时间 | 产出 |
|---|---|
| 0-5 min | 澄清目标、用户、风险、成功指标 |
| 5-12 min | 最小闭环与 action/observation space |
| 12-20 min | state/checkpoint/tool contract |
| 20-28 min | security/recovery/side effects |
| 28-35 min | eval/trace/SLO |
| 35-42 min | capacity/cost/latency/trade-offs |
| 42-45 min | 总结 + 1 个 rollout/ablation 方案 |


## Design Review 最后 10 分钟 Checklist

- [ ] 谁是最终 `source of truth`？
- [ ] 模型说 done 时谁验证？
- [ ] action 成功但响应丢失怎么办？
- [ ] worker 任意时刻 crash 能否恢复？
- [ ] credential / tenant / sandbox 的边界在哪里？
- [ ] 哪个操作不可逆，是否需要 approval/compensation？
- [ ] p95 latency 的 critical path 是什么？
- [ ] cost budget 如何向 subagent/tool 分配？
- [ ] production failure 怎样进入 eval/regression？
- [ ] 如果下一代模型更强，哪些 Harness 机制可以删？

## 最小数据模型套件

```text
Run(run_id, goal, status, budget, version)
Turn(turn_id, run_id, stop_reason)
Event(event_id, run_id, sequence_no, type, payload_ref)
Operation(operation_id, idempotency_key, state, external_ref)
Checkpoint(run_id, version, event_offset, state_ref, env_fingerprint)
PolicyDecision(decision_id, principal, action, resource, effect, rule_id)
TraceSpan(trace_id, span_id, parent_id, kind, latency, error)
```

不是每个系统都要原样采用；这套 schema 的作用是逼迫答案从“组件框”进入“恢复与因果语义”。

