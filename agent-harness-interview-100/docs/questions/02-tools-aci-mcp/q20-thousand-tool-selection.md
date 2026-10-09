---
id: q20
title: "如果有 1000 个 Tools，怎么设计 Tool Selection？"
chapter: 2
difficulty: "★★★★☆"
frequency: "★★★★☆"
role: "Agent / Applied AI"
source_pdf_page: 22
tags: [02-tools-aci-mcp, agent-harness, interview, tools]
status: expanded
---

# Q20. 如果有 1000 个 Tools，怎么设计 Tool Selection？

> **一句话结论**：先检索能力，再让模型在小候选集内决策；权限过滤应尽可能在暴露前完成。
>
> **难度**：★★★★☆　**高频**：★★★★☆　**岗位**：Agent / Applied AI　**PDF**：第 22 页起

[← Q19](q19-api-tool-vs-computer-use.md) · [章节目录](README.md) · [Q21 →](../03-context-memory/q21-prompt-vs-context-engineering.md)

> **内容分层**：第 1–13 节以 PDF 原稿为主并做结构化整理；第 14 节是 Repo v1.1 的工程扩展，结合公开一手资料与系统设计方法补强。


## 1. 面试官真正想考什么

你是否能把模型调用与工具执行之间的接口设计成稳定、可恢复、可测试的 action system。

**更深一层：** 1000 Tools 场景需要两级甚至三级路由：能力检索 -> tool family -> concrete tool，并将权限过滤前置。

## 2. Know-Why：为什么这是 Harness 问题

工具接口是给模型使用的“人机接口”。接口语义、错误结构和结果长度会直接决定模型能否稳定采取正确动作。针对本题，关键不是记住术语，而是识别系统中的“控制点”：先检索能力，再让模型在小候选集内决策；权限过滤应尽可能在暴露前完成。 这类控制点一旦缺失，模型即使单次推理正确，也可能因为重试、上下文污染、环境状态、权限或错误反馈而在真实任务中失败。

### 三条工程不变量

1. 工具调用必须有稳定 contract：输入、输出、错误与副作用语义都要显式。
2. 高风险副作用必须可审计、可去重、可恢复。
3. 工具目录应控制选择歧义和上下文成本。

这些不变量不是“最佳实践口号”，而是用来约束设计空间的。面试时如果方案违反其中一条，应主动解释为什么值得承担风险，以及如何用实验和监控把风险显式化。

## 3. Know-How：怎样落到生产系统

- semantic retrieval + namespace + metadata + task classifier + policy filter。

- 把这一机制做成可配置、可追踪、可评测的 runtime primitive。

### 推荐的工程 Artifact

实现 Top-K Tool Retrieval + namespace router + permission prefilter，并测 selection accuracy/token cost。

### 本章参考架构

```mermaid
flowchart LR
  G[Goal] --> R[Tool Retriever/Router]
  R --> M[Model]
  M --> C[Typed Tool Call]
  C --> P[Permission + Validation]
  P --> X[Execution]
  X --> O[Structured Result/Error]
  O --> M
```

> 图是本章公共心智模型；回答本题时只展开与题目相关的节点，避免把所有组件一次性画满。

## 3A. Production Deep Dive：把概念变成系统协议

### 3A.1 核心机制

1000 tools 需要两阶段或多阶段 selection，而不是把 schema 全塞进上下文

**Source of Truth：** Tool registry + retriever。在面试中主动指出这一点很重要，因为 Agent 的自然语言状态只是“认知状态”，真正能决定是否继续、是否重试、是否完成的通常是外部持久状态或环境。

### 3A.2 推荐状态 / 数据模型

```text
ToolSpec { name, version, input_schema, output_schema, risk_class }
ToolCall { call_id, run_id, tool, args_hash, timeout_ms }
Operation { operation_id, call_id, state, idempotency_key, result_ref }
ToolResult { call_id, status, error_type, retryable, payload_ref }
```

这不是要求所有系统都使用同一 schema；重点是把本题涉及的**身份、版本、状态、结果引用和恢复语义**从自然语言中提取出来，变成可验证 contract。

### 3A.3 具体故障场景

> **Scenario**：retriever recall 不足导致正确工具根本没暴露

排查时不要只看最终回答。建议从 `goal/version → model decision → policy → tool/action → environment mutation → persisted state → grader` 顺序追踪，确认“模型认为发生了什么”与“环境实际发生了什么”在哪一步分叉。

### 3A.4 可证伪实验

**Experiment：** 测 retrieval recall@k + downstream selection accuracy。

一个好的 Harness 改动必须能写成可证伪假设，例如：“如果这个机制解决了目标 failure mode，那么在固定 model/task/env 后，专项指标应改善；如果没有改善，就不应把复杂度长期留在 runtime。”

**Success criterion / SLO：** recall@k 与最终 solve-rate 达标。

### 3A.5 Production Checklist

- [ ] Schema 可机器验证且错误可分类
- [ ] 副作用工具有 idempotency / dedupe 语义
- [ ] tool result 有 token budget 与 artifact reference
- [ ] 权限过滤不只存在于 prompt
- [ ] tool catalog 版本化并监控 selection confusion

## 4. Failure Modes：低分答案与真实故障

- 把 1000 个 schema 一次塞进 prompt

### 生产环境再多想三层

- **Detectability**：这个失败在 trace / state diff / tool result / grader 中留下什么证据？
- **Recoverability**：失败后是 retry、replan、compensate、rollback、ask human，还是 terminate？
- **Blast Radius**：错误最多影响一次 tool call、一个 run、一个 tenant，还是外部真实世界？

## 5. Trade-offs：不要只讲“最佳方案”

更细工具提高可解释性，但工具数和 round-trip 可能上升；更粗工具减少调用次数，却扩大参数组合和副作用范围。

面试中建议明确给出 baseline，并说明新机制增加了什么复杂度、成本或延迟。只有当它针对一个可观测 failure mode，并带来可测量收益时，才值得进入 Harness。

## 6. 最小 Eval：怎样证明设计有效

一个可复用的最小实验框架：

1. 固定 task set、model version、environment version。
2. 只改变本题讨论的一个 Harness 变量。
3. 每个 task 运行多 trial，记录 outcome + trace。
4. 按 failure taxonomy 聚类，不只比较平均分。
5. 同时报告质量、稳定性、延迟、token/cost 和安全指标。

### 建议观测指标

- `tool-selection accuracy`
- `invalid-argument rate`
- `tool error recovery rate`
- `tool-result tokens`
- `side-effect duplicate rate`

**本题专项 Eval：** 实现 Top-K Tool Retrieval + namespace router + permission prefilter，并测 selection accuracy/token cost。

## 7. 面试追问

- 如果这个机制失败，你会在 Trace 中看到什么证据？

- 如何构造一个最小 Eval 来证明你的设计真的比 baseline 更好？

- 如果要求成本下降 40%，你会优先移除或简化哪一层？

建议继续自问：

- 这个设计里**谁拥有最终真相**：模型、数据库、环境、grader，还是人工？
- 如果请求在任意一步 crash，**恢复点**在哪里？
- 如果模型能力提升一代，这个 Harness 机制还需要吗？怎样做 ablation？

## 8. 90 秒回答版本

先给结论：先检索能力，再让模型在小候选集内决策；权限过滤应尽可能在暴露前完成。 1000 Tools 场景需要两级甚至三级路由：能力检索 -> tool family -> concrete tool，并将权限过滤前置。 实现 Top-K Tool Retrieval + namespace router + permission prefilter，并测 selection accuracy/token cost。

## 9. 5 分钟深挖版本

5 分钟展开时，按 `结论 → failure mode → 最小设计 → 数据/状态语义 → trade-off → eval/metrics` 六步回答。本题的关键工程焦点是：1000 Tools 场景需要两级甚至三级路由：能力检索 -> tool family -> concrete tool，并将权限过滤前置。 具体落地时，优先产出：实现 Top-K Tool Retrieval + namespace router + permission prefilter，并测 selection accuracy/token cost。

## 10. PDF 原稿中的工程证据 / 研究结论

_PDF 原稿未单列此节。_

> 本节只整理 PDF 原稿已有证据；下面“扩展阅读”是本仓库新增的外部资料，不与 PDF 原始内容混淆。

## 11. Offer 级回答结构

建议用 4 段式回答：①先给结论和适用边界；②解释 failure mode，也就是“为什么需要它”；③给出最小实现和关键数据结构；④主动给出 trade-off + eval 指标。这样能把概念答案升级为工程答案。第二章复盘：把 10 道题串成一个系统本章一句话 从单个 Tool 的语义与 schema，扩展到错误恢复、幂等和 tool retrieval，最后把 MCP/API/Computer Use 统一到 action registry 与 policy 层。第三章 Context Engineering 与 Memory本章核心 把上下文视为有限预算：选择、压缩、外置状态、跨 Session 恢复。上下文是有限资源。稳定 Harness 会把长期事实、任务状态和临时观察分开，并让每一轮只携带对当前决策最有价值的信息。本章面试目标

- 能设计 context budget 与 memory policy。

- 理解 compaction/reset/cross-session state。

- 能把 RAG 从静态检索升级为 agentic retrieval。

可以进一步升级为 6 段：`结论 → Why/Failure → How/Data Model → Recovery/Security → Trade-off → Eval/SLO`。

## 12. 扩展阅读（Repo 增补）

- [Anthropic - Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [MCP Specification](https://modelcontextprotocol.io/specification/)
- [SWE-agent ACI](https://arxiv.org/abs/2405.15793)

## 13. 关联题

- 本章：[第二章 Tool / ACI / MCP 与执行接口](README.md)
- [Q19. API Tool 和 Computer Use 如何选择？](q19-api-tool-vs-computer-use.md)
- [Q21. Prompt Engineering 和 Context Engineering 有什么区别？](../03-context-memory/q21-prompt-vs-context-engineering.md)
- [Q12. Tool 越多 Agent 能力是不是越强？](q12-too-many-tools.md)
- [Q18. MCP Server 越多越好吗？](q18-too-many-mcp-servers.md)
- [Q51. 设计 Agent Permission System。](../06-permission-sandbox-security/q51-permission-system-design.md)

## 14. 专业深挖：把“会回答”升级为“会设计”

### 14.1 核心判断与边界

**核心判断：** 千工具选择需要“检索+策略+权限”三层，而不是把 1000 schemas 全塞进上下文。

**必须讲清的边界：** 先按 capability/tenant/policy 过滤，再做语义 retrieval/rerank，最后让模型选择。

这意味着面试时不能只描述一个 happy path。应先明确 **source of truth、可接受的错误语义、不可违反的不变量、恢复策略**，再谈具体框架。工具接口既是模型的 action space，也是权限、幂等、错误恢复和可观测性的边界。

### 14.2 设计审查：上线前必须回答的问题

- [ ] 工具语义是否互斥
- [ ] schema 是否强类型
- [ ] 错误是否可行动
- [ ] 副作用是否幂等
- [ ] 工具是否按权限动态暴露

对于本题，还要额外确认：

1. **最坏情况下会错成什么样？** 不只问“会不会失败”，而是问错误是否会变成重复副作用、状态漂移、越权、成本爆炸或不可恢复。
2. **系统如何知道自己错了？** 至少需要一个环境信号、结构化状态、grader 或 trace 证据，而不是模型自我反省。
3. **失败后下一步是否确定？** retry、repair、reconcile、compensate、rollback、ask-human、terminate 应尽量由错误类型和策略决定。
4. **模型升级后是否仍需要这层机制？** 若答案无法用 ablation 验证，Harness 很容易累积成永久技术债。

### 14.3 推荐的实现接口 / 状态语义

```python
class ToolContract:
    name: str
    input_schema: dict
    output_schema: dict
    error_codes: list[str]
    idempotency: str
    risk_level: str
```

本题最值得落到白板或代码里的 Artifact 是：**实现 ToolIndex{embedding,namespace,risk,tags,version}。**

建议所有关键对象都带 `run_id / version / timestamp / provenance`；涉及副作用时再加入 `operation_id / idempotency_key`，涉及安全时加入 `principal / tenant / policy_version`。这样 trace、checkpoint、audit 和 eval 才能关联成同一条因果链。

### 14.4 Fault Injection：如何主动证明系统能扛住坏情况

**故障注入场景：** 构造语义相近的 1000 工具库，测 top-k recall 与最终误选。

专业的 Harness 测试不应该只做“模型有没有回答对”，而应把故障点插到**状态提交边界、网络边界、权限边界、上下文转换边界**。测试成功的标准不是“不报错”，而是：

- 最终状态可解释；
- 不产生不可接受的重复副作用；
- trace 能定位失败阶段；
- recovery 不依赖人工猜测；
- 若无法自动恢复，系统能安全停在可人工处理的状态。

### 14.5 可证伪实验 / Ablation

**实验：** 分别 ablate policy filter、retriever、reranker、model selection。

建议用 paired trials：固定 task set、model、environment、seed policy 和 grader，只改变本题对应的 Harness primitive。至少运行足够多 trial 以看到方差，并同时报告均值与分位数/置信区间。若方案只提升平均 solve-rate，却显著恶化尾延迟、成本或高风险错误率，应明确写成 trade-off，而不是宣布“全面提升”。

### 14.6 指标：至少同时看质量、稳定性和系统代价

| 指标 | Why | 建议切片 |
|---|---|---|
| `tool_recall_at_k` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `final_selection_accuracy` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `exposure_tokens` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |

除了专项指标，建议保留四个全局指标：`verified_success_rate`、`cost_per_success`、`p95_end_to_end_latency`、`human_intervention_rate`。安全敏感题再增加 `unsafe_action_rate` 或 `policy_escape_rate`。

### 14.7 Debugging Playbook

遇到失败时按以下顺序缩小范围：

1. **重放输入与版本**：确认 model / prompt / tools / harness / environment / grader 是否完全一致；
2. **定位第一个分叉点**：从 trace 中找出预期轨迹与失败轨迹首次不同的 model decision、tool result 或 state transition；
3. **区分认知错误与系统错误**：模型“想错了”与工具实际执行失败必须分开；
4. **检查状态提交窗口**：尤其关注 action 已发生但 result/checkpoint 未持久化的窗口；
5. **构造最小复现**：删掉无关上下文和工具，把 failure 固化成 regression case；
6. **做单变量修复**：修改 schema/context/policy/runtime 中最小的一项，再跑原始失败集。

### 14.8 Senior / Staff 级回答信号

Staff 级会关注 tool discovery 的 false negative：没暴露正确工具比模型选错更难排查。

面试官通常会继续追问“为什么不是更简单的方案”。因此答案中应主动给出 **baseline → failure evidence → mechanism → measurable gain → added complexity → rollback/ablation plan**，这比只列组件更能体现 Agent Systems 能力。

### 14.9 进一步阅读（Repo 研究层，不等同 PDF 原稿）

- [SWE-agent / ACI](https://arxiv.org/abs/2405.15793)
- [Anthropic - Writing effective tools for agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
- [MCP Specification](https://modelcontextprotocol.io/specification/)

---

[← Q19](q19-api-tool-vs-computer-use.md) · [章节目录](README.md) · [Q21 →](../03-context-memory/q21-prompt-vs-context-engineering.md)
