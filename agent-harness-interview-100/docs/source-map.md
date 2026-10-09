# PDF → Markdown Source Map

本页用于证明“PDF 中每一道题都有独立 Markdown 落点”。核心题干、Know-Why/How、Failure Modes、Trade-off、追问与 PDF 原稿证据放在对应题目中；Repo 新增内容明确标为 Production Deep Dive / 扩展阅读。

| PDF | Markdown |
|---:|---|
| p.6 · Q01 | [什么是 Agent Harness？它和 Agent Framework 有什么区别？](questions/01-agent-loop-harness/q01-agent-harness-vs-framework.md) |
| p.7 · Q02 | [请从零写出一个最小 Agent Loop。](questions/01-agent-loop-harness/q02-minimal-agent-loop.md) |
| p.8 · Q03 | [Agent Loop 有哪些 Stop Condition？](questions/01-agent-loop-harness/q03-agent-stop-conditions.md) |
| p.9 · Q04 | [为什么 ReAct 不是一个完整的 Agent 架构？](questions/01-agent-loop-harness/q04-react-vs-production-runtime.md) |
| p.9 · Q05 | [Agent 和普通 Workflow 的本质区别是什么？](questions/01-agent-loop-harness/q05-agent-vs-workflow.md) |
| p.10 · Q06 | [什么问题根本不应该使用 Agent？](questions/01-agent-loop-harness/q06-when-not-to-use-agents.md) |
| p.11 · Q07 | [Model 能力和 Harness 能力如何区分？](questions/01-agent-loop-harness/q07-model-vs-harness-failures.md) |
| p.11 · Q08 | [为什么同一个模型换一个 Harness，Benchmark 可能差很多？](questions/01-agent-loop-harness/q08-why-harness-changes-benchmarks.md) |
| p.12 · Q09 | [Agent Runtime 最重要的抽象是什么？](questions/01-agent-loop-harness/q09-agent-runtime-abstractions.md) |
| p.13 · Q10 | [如果不用 LangChain/LangGraph，你如何自己实现 Agent？](questions/01-agent-loop-harness/q10-build-agent-without-framework.md) |
| p.15 · Q11 | [怎样设计一个 LLM-friendly Tool？](questions/02-tools-aci-mcp/q11-llm-friendly-tool-design.md) |
| p.16 · Q12 | [Tool 越多 Agent 能力是不是越强？](questions/02-tools-aci-mcp/q12-too-many-tools.md) |
| p.16 · Q13 | [两个 Tool 功能重叠应该怎么办？](questions/02-tools-aci-mcp/q13-overlapping-tools.md) |
| p.17 · Q14 | [Tool Schema 为什么比 Prompt 更容易被低估？](questions/02-tools-aci-mcp/q14-tool-schema-design.md) |
| p.18 · Q15 | [Tool Error 应该怎样返回给 Agent？](questions/02-tools-aci-mcp/q15-tool-error-contract.md) |
| p.19 · Q16 | [为什么 Tool 必须考虑 Idempotency？](questions/02-tools-aci-mcp/q16-tool-idempotency.md) |
| p.20 · Q17 | [MCP 中 Resources、Prompts、Tools 应如何理解？](questions/02-tools-aci-mcp/q17-mcp-resources-prompts-tools.md) |
| p.20 · Q18 | [MCP Server 越多越好吗？](questions/02-tools-aci-mcp/q18-too-many-mcp-servers.md) |
| p.21 · Q19 | [API Tool 和 Computer Use 如何选择？](questions/02-tools-aci-mcp/q19-api-tool-vs-computer-use.md) |
| p.22 · Q20 | [如果有 1000 个 Tools，怎么设计 Tool Selection？](questions/02-tools-aci-mcp/q20-thousand-tool-selection.md) |
| p.24 · Q21 | [Prompt Engineering 和 Context Engineering 有什么区别？](questions/03-context-memory/q21-prompt-vs-context-engineering.md) |
| p.25 · Q22 | [为什么“上下文越多越好”是错误的？](questions/03-context-memory/q22-more-context-is-not-better.md) |
| p.26 · Q23 | [什么是 Context Rot / Context Pollution？](questions/03-context-memory/q23-context-rot-pollution.md) |
| p.26 · Q24 | [Context Compaction 和 Context Reset 有什么区别？](questions/03-context-memory/q24-compaction-vs-reset.md) |
| p.27 · Q25 | [Short-term Memory 和 Long-term Memory 应如何设计？](questions/03-context-memory/q25-short-vs-long-term-memory.md) |
| p.28 · Q26 | [Agent 应该什么时候写 Memory？](questions/03-context-memory/q26-memory-write-policy.md) |
| p.29 · Q27 | [RAG 和 Agentic Search 有什么区别？](questions/03-context-memory/q27-rag-vs-agentic-search.md) |
| p.29 · Q28 | [Conversation History 应全部发送给模型吗？](questions/03-context-memory/q28-conversation-history-selection.md) |
| p.30 · Q29 | [如何让 Agent 跨 Session 工作？](questions/03-context-memory/q29-cross-session-agent-state.md) |
| p.31 · Q30 | [Context Cache 应怎样设计？](questions/03-context-memory/q30-context-cache-design.md) |
| p.33 · Q31 | [Single Agent 和 Multi-Agent 怎么选？](questions/04-planning-orchestration/q31-single-vs-multi-agent.md) |
| p.34 · Q32 | [Routing 和 Agent 有什么区别？](questions/04-planning-orchestration/q32-routing-vs-agent-loop.md) |
| p.34 · Q33 | [什么是 Orchestrator-Worker Pattern？](questions/04-planning-orchestration/q33-orchestrator-worker-pattern.md) |
| p.35 · Q34 | [Manager-as-Tool 和 Handoff 有什么区别？](questions/04-planning-orchestration/q34-manager-as-tool-vs-handoff.md) |
| p.36 · Q35 | [Agent 并行化最大的问题是什么？](questions/04-planning-orchestration/q35-agent-parallelization.md) |
| p.36 · Q36 | [Evaluator-Optimizer 为什么有效？](questions/04-planning-orchestration/q36-evaluator-optimizer.md) |
| p.37 · Q37 | [Subagent 的独立 Context Window 有什么价值？](questions/04-planning-orchestration/q37-subagent-context-windows.md) |
| p.38 · Q38 | [Multi-Agent 怎么共享状态？](questions/04-planning-orchestration/q38-multi-agent-shared-state.md) |
| p.39 · Q39 | [如何控制 Agent Fan-out？](questions/04-planning-orchestration/q39-control-agent-fanout.md) |
| p.39 · Q40 | [为什么 Multi-Agent 有时比 Single Agent 更差？](questions/04-planning-orchestration/q40-when-multi-agent-is-worse.md) |
| p.41 · Q41 | [为什么 Long-Running Agent 会随着时间变差？](questions/05-long-horizon-durable/q41-long-running-agent-degradation.md) |
| p.42 · Q42 | [为什么 progress file 很重要？](questions/05-long-horizon-durable/q42-progress-artifact.md) |
| p.43 · Q43 | [Initializer Agent 有什么作用？](questions/05-long-horizon-durable/q43-initializer-agent.md) |
| p.43 · Q44 | [什么是 Sprint Contract / Definition of Done？](questions/05-long-horizon-durable/q44-sprint-contract-definition-of-done.md) |
| p.44 · Q45 | [Checkpoint 应该保存什么？](questions/05-long-horizon-durable/q45-checkpoint-schema.md) |
| p.45 · Q46 | [Agent Crash 后怎样 Resume，而不是重新开始？](questions/05-long-horizon-durable/q46-crash-resume-recovery.md) |
| p.46 · Q47 | [如何支持 Human Interrupt？](questions/05-long-horizon-durable/q47-human-interrupt.md) |
| p.47 · Q48 | [Long-running Agent 如何避免 Plan Drift？](questions/05-long-horizon-durable/q48-prevent-plan-drift.md) |
| p.48 · Q49 | [如何判断 Coding Agent 真的完成任务？](questions/05-long-horizon-durable/q49-verify-coding-agent-completion.md) |
| p.48 · Q50 | [设计一个运行 12 小时的 Agent，要新增哪些机制？](questions/05-long-horizon-durable/q50-twelve-hour-agent-design.md) |
| p.50 · Q51 | [设计 Agent Permission System。](questions/06-permission-sandbox-security/q51-permission-system-design.md) |
| p.51 · Q52 | [Permission Prompt 和 Sandbox 有什么区别？](questions/06-permission-sandbox-security/q52-permission-vs-sandbox.md) |
| p.52 · Q53 | [什么是 Approval Fatigue？](questions/06-permission-sandbox-security/q53-approval-fatigue.md) |
| p.53 · Q54 | [Tool Risk 如何分级？](questions/06-permission-sandbox-security/q54-tool-risk-classification.md) |
| p.53 · Q55 | [Prompt Injection 为什么对 Agent 比 Chatbot 更危险？](questions/06-permission-sandbox-security/q55-prompt-injection-agent-risk.md) |
| p.54 · Q56 | [Secret 应该怎么提供给 Agent？](questions/06-permission-sandbox-security/q56-secret-management.md) |
| p.55 · Q57 | [为什么 Sandbox 必须同时考虑 Filesystem 和 Network？](questions/06-permission-sandbox-security/q57-filesystem-network-sandbox.md) |
| p.55 · Q58 | [Least Privilege 在 Agent 中怎样实现？](questions/06-permission-sandbox-security/q58-least-privilege.md) |
| p.56 · Q59 | [哪些动作应该 Human-in-the-loop？](questions/06-permission-sandbox-security/q59-human-in-the-loop-policy.md) |
| p.57 · Q60 | [Agent Audit Log 应记录什么？](questions/06-permission-sandbox-security/q60-agent-audit-log.md) |
| p.58 · Q61 | [Agent Harness 和 Eval Harness 有什么区别？](questions/07-evaluation-observability/q61-agent-harness-vs-eval-harness.md) |
| p.59 · Q62 | [Task、Trial、Trace、Outcome、Grader 分别是什么？](questions/07-evaluation-observability/q62-task-trial-trace-outcome-grader.md) |
| p.60 · Q63 | [为什么应该优先 Eval Outcome，而不是 Tool Trajectory？](questions/07-evaluation-observability/q63-outcome-vs-trajectory-eval.md) |
| p.61 · Q64 | [Code Grader、LLM Grader、Human Grader 怎么选？](questions/07-evaluation-observability/q64-code-llm-human-graders.md) |
| p.61 · Q65 | [pass@k 和 pass^k 区别是什么？](questions/07-evaluation-observability/q65-pass-at-k-vs-pass-power-k.md) |
| p.62 · Q66 | [Agent Eval 为什么一定要多 Trial？](questions/07-evaluation-observability/q66-why-multiple-eval-trials.md) |
| p.63 · Q67 | [Capability Eval 和 Regression Eval 有什么不同？](questions/07-evaluation-observability/q67-capability-vs-regression-eval.md) |
| p.64 · Q68 | [怎样校准 LLM-as-Judge？](questions/07-evaluation-observability/q68-llm-judge-calibration.md) |
| p.64 · Q69 | [Agent 会不会 Hack Eval？](questions/07-evaluation-observability/q69-eval-hacking.md) |
| p.65 · Q70 | [Production Trace 应如何变成 Eval Dataset？](questions/07-evaluation-observability/q70-production-traces-to-evals.md) |
| p.67 · Q71 | [Run、Thread、Turn 应该怎么建模？](questions/08-reliability-distributed/q71-run-thread-turn-model.md) |
| p.68 · Q72 | [Tool Retry 应该怎么设计？](questions/08-reliability-distributed/q72-tool-retry-design.md) |
| p.68 · Q73 | [Agent Tool 能实现 Exactly Once 吗？](questions/08-reliability-distributed/q73-exactly-once-agent-tools.md) |
| p.69 · Q74 | [Cancellation 怎么设计？](questions/08-reliability-distributed/q74-cancellation-design.md) |
| p.70 · Q75 | [Multi-Agent 并发怎么控制？](questions/08-reliability-distributed/q75-multi-agent-concurrency-control.md) |
| p.71 · Q76 | [Shared Agent State 怎么保证一致性？](questions/08-reliability-distributed/q76-shared-state-consistency.md) |
| p.71 · Q77 | [Tool Partial Failure 怎么处理？](questions/08-reliability-distributed/q77-tool-partial-failure.md) |
| p.72 · Q78 | [如何设计 Agent Rate Limiting？](questions/08-reliability-distributed/q78-agent-rate-limiting.md) |
| p.73 · Q79 | [Durable Agent Worker 怎么设计？](questions/08-reliability-distributed/q79-durable-agent-worker.md) |
| p.74 · Q80 | [什么叫 Brain 与 Hands 解耦？](questions/08-reliability-distributed/q80-brain-hands-decoupling.md) |
| p.76 · Q81 | [Agent Latency 怎么拆？](questions/09-cost-latency-performance/q81-agent-latency-breakdown.md) |
| p.77 · Q82 | [怎样做 Model Routing？](questions/09-cost-latency-performance/q82-model-routing.md) |
| p.77 · Q83 | [Parallel Agent 为什么可能更快但更贵？](questions/09-cost-latency-performance/q83-parallel-agent-cost-latency.md) |
| p.78 · Q84 | [Prompt Caching 在 Agent 中为什么特别重要？](questions/09-cost-latency-performance/q84-prompt-caching.md) |
| p.79 · Q85 | [Tool Result 为什么必须 Token Efficient？](questions/09-cost-latency-performance/q85-token-efficient-tool-results.md) |
| p.79 · Q86 | [Streaming 对 Agent 有什么价值？](questions/09-cost-latency-performance/q86-agent-streaming.md) |
| p.80 · Q87 | [模型升级后 Harness 一定应该保持不变吗？](questions/09-cost-latency-performance/q87-model-upgrade-harness-ablation.md) |
| p.81 · Q88 | [Sandbox Cold Start 怎么优化？](questions/09-cost-latency-performance/q88-sandbox-cold-start.md) |
| p.82 · Q89 | [怎样给 Agent 设置 Cost Budget？](questions/09-cost-latency-performance/q89-agent-cost-budget.md) |
| p.82 · Q90 | [如何判断 Agent Optimization 是否真的有效？](questions/09-cost-latency-performance/q90-measure-agent-optimization.md) |
| p.84 · Q91 | [系统设计：设计一个 Coding Agent。](questions/10-system-design-debugging/q91-design-coding-agent.md) |
| p.85 · Q92 | [系统设计：设计一个 Deep Research Agent。](questions/10-system-design-debugging/q92-design-deep-research-agent.md) |
| p.86 · Q93 | [系统设计：设计 Customer Support Agent。](questions/10-system-design-debugging/q93-design-customer-support-agent.md) |
| p.87 · Q94 | [系统设计：设计 Multi-Tenant Agent Platform。](questions/10-system-design-debugging/q94-design-multi-tenant-agent-platform.md) |
| p.88 · Q95 | [Coding：实现 Production Agent Loop，你会加哪些机制？](questions/10-system-design-debugging/q95-production-agent-loop.md) |
| p.88 · Q96 | [Coding：设计 Permission Engine。](questions/10-system-design-debugging/q96-permission-engine.md) |
| p.89 · Q97 | [Coding：设计 Agent Checkpoint Schema。](questions/10-system-design-debugging/q97-checkpoint-data-model.md) |
| p.90 · Q98 | [Coding：Agent Trace Schema 应怎么设计？](questions/10-system-design-debugging/q98-trace-schema.md) |
| p.91 · Q99 | [Debug：Agent Solve Rate 从 72% 掉到 58%，怎么查？](questions/10-system-design-debugging/q99-debug-solve-rate-regression.md) |
| p.92 · Q100 | [给你一个 Agent，你如何系统地提升 30% Performance？](questions/10-system-design-debugging/q100-improve-agent-performance-30-percent.md) |

## 附录映射

- 30 天复习计划 → [appendices/30-day-study-plan.md](appendices/30-day-study-plan.md)
- System Design 白板模板 → [appendices/system-design-template.md](appendices/system-design-template.md)
- Failure Taxonomy → [appendices/failure-taxonomy.md](appendices/failure-taxonomy.md)
- 参考资料 → [appendices/references.md](appendices/references.md)


## v1.1 内容分层说明

此表只证明 PDF 原题到 Markdown 的覆盖关系。每个题目新增的 `第 14 节` 属于 Repo 工程研究层，不声称来自 PDF；其参考资料统一在 `references.md` 的 R 层维护。这样既能保持 source fidelity，也能持续迭代工程深度。

