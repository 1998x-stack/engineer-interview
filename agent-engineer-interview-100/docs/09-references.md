# 参考资料与来源说明

> 本仓库采用两层来源：**PDF/上传资料提供知识结构与原始题目骨架**；GitHub Expanded Edition 在此基础上加入生产系统工程分析、分布式系统机制和截至 2026-09 的官方 Agent 工程资料。新增内容不是对原书逐字摘录。

## A. 本项目基础资料

### S1 · Micheal Lanham, *AI Agents in Action*, Manning, 2025

用于 Agent / Multi-Agent / Actions & Tools / Memory & Knowledge / Reasoning & Evaluation / Planning & Feedback 的知识结构参考。

### S2 · 凌峰，《AI Agent开发与应用：基于大模型的智能体构建》，清华大学出版社，2025

用于感知-决策-执行、上下文与记忆、ReAct、动态工具集成、多智能体通信与容错等结构参考。

### S3 · 《AI Agent智能工作流》

用于 Agent 工具调用、MCP、记忆压缩、企业安全架构、监控与沙箱等主题参考。

### S4 · 《字节跳动 RAG 实践手册》

用于索引、检索触发、Hybrid/Rerank、效果评估、全链路监控、故障复盘、成本归因与权限安全等 RAG 主题参考。

## B. 2026 官方工程资料（GitHub Expanded Edition）

### Agent Runtime / Handoff / Tracing

- OpenAI Agents SDK — Running agents: https://openai.github.io/openai-agents-python/running_agents/
- OpenAI Agents SDK — Agent orchestration: https://openai.github.io/openai-agents-python/multi_agent/
- OpenAI Agents SDK — Handoffs: https://openai.github.io/openai-agents-python/handoffs/
- OpenAI Agents SDK — Guardrails: https://openai.github.io/openai-agents-python/guardrails/
- OpenAI Agents SDK — Tracing: https://openai.github.io/openai-agents-python/tracing/

这些资料对应本仓库关于 agent loop、handoff history shaping、guardrail、tool execution 与 trace/span 的工程扩展。

### Context / Long-running Agent / Eval

- Anthropic — Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic — Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps
- Anthropic — Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- Anthropic — How we built our multi-agent research system: https://www.anthropic.com/engineering/multi-agent-research-system

这些资料对应 context compaction/reset、structured artifact handoff、长任务拆分、trajectory eval 与 multi-agent orchestration。

### MCP

- MCP Specification 2025-11-25: https://modelcontextprotocol.io/specification/2025-11-25
- MCP Tools: https://modelcontextprotocol.io/specification/2025-11-25/server/tools
- MCP Authorization: https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization
- MCP Tasks: https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks

MCP 不应被简化为“另一种 Function Calling”。协议还覆盖 Host/Client/Server、Resources、Prompts、Tools、授权以及实验性的 durable Tasks 等语义。

### Agent-to-Agent Protocol

- A2A Protocol v1.0: https://a2a-protocol.org/v1.0.0/
- A2A Latest Specification: https://a2a-protocol.org/dev/specification/

A2A 的 Task / Message / Artifact / Agent Card 等概念可用于理解跨框架、跨组织 Agent 通信的协议化设计。消息不等于最终 artifact，Task 是有生命周期的状态对象。

### Durable Execution / HITL

- LangGraph Persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph Interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- LangChain Human-in-the-loop: https://docs.langchain.com/oss/python/langchain/human-in-the-loop

这些资料说明 checkpoint/persistence 如何支持 fault tolerance、HITL、resume 和 time-travel；也强调 interrupt 前的 side effect 必须具备幂等语义。

## C. 来源边界

1. **PDF-derived**：原始 Q001-Q100 的题目、30 秒回答、深挖点、连续追问、易错回答、Know-Why、Know-How，以及能力轴组织。
2. **GitHub Expanded Edition**：3 分钟专业回答、状态/接口设计、Mermaid 架构、Failure Modes、Trade-off、Metrics、Production Checklist、关联题目和当前官方资料索引。
3. **分布式系统扩展**：idempotency、Saga、Circuit Breaker、deadline propagation、outbox、reconciliation、schema/version migration 等用于把 Agent 问题提升到可上线、可恢复、可治理的系统工程语境。

> 仓库仅包含本项目原创生成的面试手册 PDF，不重新分发参考书籍/资料原文件。
