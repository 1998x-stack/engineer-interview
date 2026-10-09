# 20 题主干路线

PDF 最后给出的优先级路线。建议按顺序口述 + 画图 + 设计 Eval。

1. [Q01. 什么是 Agent Harness？它和 Agent Framework 有什么区别？](../questions/01-agent-loop-harness/q01-agent-harness-vs-framework.md)
2. [Q02. 请从零写出一个最小 Agent Loop。](../questions/01-agent-loop-harness/q02-minimal-agent-loop.md)
3. [Q07. Model 能力和 Harness 能力如何区分？](../questions/01-agent-loop-harness/q07-model-vs-harness-failures.md)
4. [Q11. 怎样设计一个 LLM-friendly Tool？](../questions/02-tools-aci-mcp/q11-llm-friendly-tool-design.md)
5. [Q16. 为什么 Tool 必须考虑 Idempotency？](../questions/02-tools-aci-mcp/q16-tool-idempotency.md)
6. [Q21. Prompt Engineering 和 Context Engineering 有什么区别？](../questions/03-context-memory/q21-prompt-vs-context-engineering.md)
7. [Q24. Context Compaction 和 Context Reset 有什么区别？](../questions/03-context-memory/q24-compaction-vs-reset.md)
8. [Q29. 如何让 Agent 跨 Session 工作？](../questions/03-context-memory/q29-cross-session-agent-state.md)
9. [Q31. Single Agent 和 Multi-Agent 怎么选？](../questions/04-planning-orchestration/q31-single-vs-multi-agent.md)
10. [Q36. Evaluator-Optimizer 为什么有效？](../questions/04-planning-orchestration/q36-evaluator-optimizer.md)
11. [Q45. Checkpoint 应该保存什么？](../questions/05-long-horizon-durable/q45-checkpoint-schema.md)
12. [Q46. Agent Crash 后怎样 Resume，而不是重新开始？](../questions/05-long-horizon-durable/q46-crash-resume-recovery.md)
13. [Q51. 设计 Agent Permission System。](../questions/06-permission-sandbox-security/q51-permission-system-design.md)
14. [Q52. Permission Prompt 和 Sandbox 有什么区别？](../questions/06-permission-sandbox-security/q52-permission-vs-sandbox.md)
15. [Q63. 为什么应该优先 Eval Outcome，而不是 Tool Trajectory？](../questions/07-evaluation-observability/q63-outcome-vs-trajectory-eval.md)
16. [Q65. pass@k 和 pass^k 区别是什么？](../questions/07-evaluation-observability/q65-pass-at-k-vs-pass-power-k.md)
17. [Q73. Agent Tool 能实现 Exactly Once 吗？](../questions/08-reliability-distributed/q73-exactly-once-agent-tools.md)
18. [Q91. 系统设计：设计一个 Coding Agent。](../questions/10-system-design-debugging/q91-design-coding-agent.md)
19. [Q99. Debug：Agent Solve Rate 从 72% 掉到 58%，怎么查？](../questions/10-system-design-debugging/q99-debug-solve-rate-regression.md)
20. [Q100. 给你一个 Agent，你如何系统地提升 30% Performance？](../questions/10-system-design-debugging/q100-improve-agent-performance-30-percent.md)


## Core 20 的训练标准

每题不是“看懂”就算完成，而是达到四级：

1. **Recall**：90 秒独立回答；
2. **Design**：能画数据流/状态机并写一个核心 schema；
3. **Failure**：能举一个真实故障窗口和恢复方案；
4. **Evidence**：能设计一个最小 eval/ablation 证明方案有效。

如果一题无法达到第 3–4 级，应回到对应章节补题，而不是继续背更多题。

