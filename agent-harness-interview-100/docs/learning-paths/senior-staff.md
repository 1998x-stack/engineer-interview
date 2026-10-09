# Senior / Staff 深挖路线

重点训练“状态语义、失败恢复、安全边界、评测与因果调优”。

- [Q16. 为什么 Tool 必须考虑 Idempotency？](../questions/02-tools-aci-mcp/q16-tool-idempotency.md)
- [Q20. 如果有 1000 个 Tools，怎么设计 Tool Selection？](../questions/02-tools-aci-mcp/q20-thousand-tool-selection.md)
- [Q24. Context Compaction 和 Context Reset 有什么区别？](../questions/03-context-memory/q24-compaction-vs-reset.md)
- [Q29. 如何让 Agent 跨 Session 工作？](../questions/03-context-memory/q29-cross-session-agent-state.md)
- [Q36. Evaluator-Optimizer 为什么有效？](../questions/04-planning-orchestration/q36-evaluator-optimizer.md)
- [Q41. 为什么 Long-Running Agent 会随着时间变差？](../questions/05-long-horizon-durable/q41-long-running-agent-degradation.md)
- [Q45. Checkpoint 应该保存什么？](../questions/05-long-horizon-durable/q45-checkpoint-schema.md)
- [Q46. Agent Crash 后怎样 Resume，而不是重新开始？](../questions/05-long-horizon-durable/q46-crash-resume-recovery.md)
- [Q51. 设计 Agent Permission System。](../questions/06-permission-sandbox-security/q51-permission-system-design.md)
- [Q55. Prompt Injection 为什么对 Agent 比 Chatbot 更危险？](../questions/06-permission-sandbox-security/q55-prompt-injection-agent-risk.md)
- [Q57. 为什么 Sandbox 必须同时考虑 Filesystem 和 Network？](../questions/06-permission-sandbox-security/q57-filesystem-network-sandbox.md)
- [Q61. Agent Harness 和 Eval Harness 有什么区别？](../questions/07-evaluation-observability/q61-agent-harness-vs-eval-harness.md)
- [Q63. 为什么应该优先 Eval Outcome，而不是 Tool Trajectory？](../questions/07-evaluation-observability/q63-outcome-vs-trajectory-eval.md)
- [Q65. pass@k 和 pass^k 区别是什么？](../questions/07-evaluation-observability/q65-pass-at-k-vs-pass-power-k.md)
- [Q68. 怎样校准 LLM-as-Judge？](../questions/07-evaluation-observability/q68-llm-judge-calibration.md)
- [Q70. Production Trace 应如何变成 Eval Dataset？](../questions/07-evaluation-observability/q70-production-traces-to-evals.md)
- [Q73. Agent Tool 能实现 Exactly Once 吗？](../questions/08-reliability-distributed/q73-exactly-once-agent-tools.md)
- [Q74. Cancellation 怎么设计？](../questions/08-reliability-distributed/q74-cancellation-design.md)
- [Q76. Shared Agent State 怎么保证一致性？](../questions/08-reliability-distributed/q76-shared-state-consistency.md)
- [Q79. Durable Agent Worker 怎么设计？](../questions/08-reliability-distributed/q79-durable-agent-worker.md)
- [Q80. 什么叫 Brain 与 Hands 解耦？](../questions/08-reliability-distributed/q80-brain-hands-decoupling.md)
- [Q87. 模型升级后 Harness 一定应该保持不变吗？](../questions/09-cost-latency-performance/q87-model-upgrade-harness-ablation.md)
- [Q91. 系统设计：设计一个 Coding Agent。](../questions/10-system-design-debugging/q91-design-coding-agent.md)
- [Q94. 系统设计：设计 Multi-Tenant Agent Platform。](../questions/10-system-design-debugging/q94-design-multi-tenant-agent-platform.md)
- [Q95. Coding：实现 Production Agent Loop，你会加哪些机制？](../questions/10-system-design-debugging/q95-production-agent-loop.md)
- [Q96. Coding：设计 Permission Engine。](../questions/10-system-design-debugging/q96-permission-engine.md)
- [Q97. Coding：设计 Agent Checkpoint Schema。](../questions/10-system-design-debugging/q97-checkpoint-data-model.md)
- [Q98. Coding：Agent Trace Schema 应怎么设计？](../questions/10-system-design-debugging/q98-trace-schema.md)
- [Q99. Debug：Agent Solve Rate 从 72% 掉到 58%，怎么查？](../questions/10-system-design-debugging/q99-debug-solve-rate-regression.md)
- [Q100. 给你一个 Agent，你如何系统地提升 30% Performance？](../questions/10-system-design-debugging/q100-improve-agent-performance-30-percent.md)


## Senior 与 Staff 的分界

**Senior** 通常能把单个 primitive 做正确：tool contract、checkpoint、permission、eval、trace。

**Staff** 需要进一步回答：

- primitive 之间的依赖关系是什么；
- 哪个状态是真正 source of truth；
- 最坏故障的 blast radius 是什么；
- 如何通过 experiment/ablation 建立因果证据；
- 模型升级后哪些机制应该删除；
- 怎样把生产 incident 变成长期 regression 和平台能力。

建议 Staff 路线重点练 Q07/Q16/Q24/Q36/Q45–Q46/Q51–Q60/Q61–Q70/Q73/Q80/Q87/Q90–Q100。

