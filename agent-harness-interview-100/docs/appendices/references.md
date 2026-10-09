# 参考资料与延伸阅读

## A. PDF 所附资料（原稿来源基线）

- **[B1]** Micheal Lanham, *AI Agents in Action*, Manning。PDF 原稿重点使用：Actions/Tools、Memory/Knowledge、Reasoning/Evaluation、Planning/Feedback。
- **[B2]** 凌峰，《AI Agent 开发与应用：基于大模型的智能体构建》。重点：智能体架构、上下文与记忆、RESTful API、向量数据库、ReAct、多智能体与案例实践。
- **[B3]** 《AI Agent 智能工作流》。用于补充 Agent/Workflow/Tool 调用和多 Agent 应用视角。
- **[B4]** 《字节跳动 RAG 实践手册》。重点：检索触发与查询理解、索引/生成评估、全链路监控、成本、安全、Agent+RAG、故障复盘。

> 这些第三方资料**不随仓库重新分发**；仓库只保存本书的分析、题解和引用信息。

## B. PDF 原稿列出的公开一手资料

- **[W1]** OpenAI, AI Systems Engineer - Codex Agents: https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/
- **[W2]** OpenAI, Software Engineer - API Agents: https://openai.com/careers/software-engineer-api-agents-san-francisco/
- **[W3]** OpenAI, Software Engineer - Cloud Agents / Codex Core Agents: https://openai.com/careers/software-engineer-cloud-agents-san-francisco/ ; https://openai.com/careers/software-engineer-codex-core-agents-san-francisco/
- **[W4]** Anthropic, Effective harnesses for long-running agents: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- **[W5]** Anthropic, Harness design for long-running application development: https://www.anthropic.com/engineering/harness-design-long-running-apps
- **[W6]** Anthropic, Effective context engineering for AI agents: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- **[W7]** Anthropic, Demystifying evals for AI agents: https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents ; sandboxing: https://www.anthropic.com/engineering/claude-code-sandboxing
- **[W8]** Yang et al., SWE-agent: https://arxiv.org/abs/2405.15793
- **[W9]** Anthropic engineering: Building Effective Agents / Writing effective tools / Managed Agents / Multi-agent Research: https://www.anthropic.com/engineering
- **[W10]** OpenAI Agents SDK: https://openai.github.io/openai-agents-python/

## C. Repo 增补的一手资料（与 PDF 来源区分）

- OpenAI Agents SDK Tracing: https://openai.github.io/openai-agents-python/tracing/
- OpenAI Agents SDK Agents/Runner: https://openai.github.io/openai-agents-python/agents/
- LangGraph Persistence: https://docs.langchain.com/oss/python/langgraph/persistence
- LangGraph Interrupts: https://docs.langchain.com/oss/python/langgraph/interrupts
- Model Context Protocol Specification: https://modelcontextprotocol.io/specification/
- MCP 2026-07 Release Candidate background: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/

## 资料使用原则

1. PDF 原稿内容与 Repo 新增研究明确分层。
2. 优先引用官方文档、论文与一手工程文章。
3. 对版本相关能力注明访问日期或版本，避免把快速变化的 SDK 细节写成永恒事实。
4. 新增任何“某公司真题”必须有公开可验证出处；否则只标记为“高拟真工程题”。


## D. 2026 Repo v1.1 验证的一手资料

以下资料用于第 14 节的工程扩展，不代表 PDF 原稿逐字引用：

- **[R1] OpenAI Agents SDK — Running agents**：https://openai.github.io/openai-agents-python/running_agents/ ；覆盖 agent loop、run config、state/conversation、tool execution、approval、error behavior。
- **[R2] OpenAI Agents SDK — Agent orchestration**：https://openai.github.io/openai-agents-python/multi_agent/ ；区分 agents-as-tools 与 handoffs 的 ownership 模式。
- **[R3] OpenAI Agents SDK — Handoffs**：https://openai.github.io/openai-agents-python/handoffs/ ；涉及 transfer、input filtering、authorization boundary。
- **[R4] OpenAI Agents SDK — Tracing**：https://openai.github.io/openai-agents-python/tracing/ ；覆盖 task/turn/agent/generation/function/guardrail/handoff 等 span。
- **[R5] OpenAI — AI Systems Engineer, Codex Agents**：https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/ ；公开职责明确包含 agent harness、execution loop、sandbox、state、orchestration、eval、reliability、tokens/latency/cost。
- **[R6] Anthropic — Harness design for long-running application development**：https://www.anthropic.com/engineering/harness-design-long-running-apps ；Planner/Generator/Evaluator、structured artifacts、long-running application development。
- **[R7] Anthropic — Scaling Managed Agents**：https://www.anthropic.com/engineering/managed-agents ；brain/hands 解耦、Harness 假设随模型升级而过时。
- **[R8] Anthropic Engineering Index**：https://www.anthropic.com/engineering ；可追踪 context engineering、tool design、sandboxing、evals、multi-agent、long-running harness 等系列文章。
- **[R9] MCP Specification**：https://modelcontextprotocol.io/specification/ ；Resources/Prompts/Tools 与协议安全边界。
- **[R10] OpenTelemetry Traces**：https://opentelemetry.io/docs/concepts/signals/traces/ ；Trace/Span 的通用可观测性模型。

### 引用分层约定

- `B*`：用户提供的书籍/手册；
- `W*`：PDF 原稿已经列出的公开资料；
- `R*`：Repo v1.1 后续研究补充。

任何问题文件若写“PDF 原稿证据”，只应引用 B/W 层；第 14 节的进一步工程扩展可以引用 R 层，但必须明确不是 PDF 原稿内容。
