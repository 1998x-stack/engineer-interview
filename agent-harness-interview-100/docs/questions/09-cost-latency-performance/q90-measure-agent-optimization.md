---
id: q90
title: "如何判断 Agent Optimization 是否真的有效？"
chapter: 9
difficulty: "★★★★☆"
frequency: "★★★★★"
role: "Harness / AI Systems"
source_pdf_page: 82
tags: [09-cost-latency-performance, agent-harness, interview, tools, agents, performance, cost]
status: expanded
---

# Q90. 如何判断 Agent Optimization 是否真的有效？

> **一句话结论**：同时报告 solve rate、reliability、latency、tokens、cost、turns、tool calls、human intervention 和 failure severity。
>
> **难度**：★★★★☆　**高频**：★★★★★　**岗位**：Harness / AI Systems　**PDF**：第 82 页起

[← Q89](q89-agent-cost-budget.md) · [章节目录](README.md) · [Q91 →](../10-system-design-debugging/q91-design-coding-agent.md)

> **内容分层**：第 1–13 节以 PDF 原稿为主并做结构化整理；第 14 节是 Repo v1.1 的工程扩展，结合公开一手资料与系统设计方法补强。


## 1. 面试官真正想考什么

你是否能把性能问题拆成关键路径，并做多目标优化。

**更深一层：** Optimization 必须报告 quality/reliability/latency/cost 的联合变化，并明确 Pareto 是否真的改善。

## 2. Know-Why：为什么这是 Harness 问题

Agent 性能优化是多目标优化。最强模型不一定是最佳系统，减少串行回合和无效上下文通常比单纯换模型更划算。针对本题，关键不是记住术语，而是识别系统中的“控制点”：同时报告 solve rate、reliability、latency、tokens、cost、turns、tool calls、human intervention 和 failure severity。 这类控制点一旦缺失，模型即使单次推理正确，也可能因为重试、上下文污染、环境状态、权限或错误反馈而在真实任务中失败。

### 三条工程不变量

1. 优化目标必须是多目标函数，而不是单一模型分数。
2. 减少串行 round-trip 往往比微调单次模型延迟更有效。
3. 任何缓存和路由都要同时度量质量回退与陈旧风险。

这些不变量不是“最佳实践口号”，而是用来约束设计空间的。面试时如果方案违反其中一条，应主动解释为什么值得承担风险，以及如何用实验和监控把风险显式化。

## 3. Know-How：怎样落到生产系统

- 比较 Pareto frontier，不只看单指标涨幅。

- 把这一机制做成可配置、可追踪、可评测的 runtime primitive。

### 推荐的工程 Artifact

建议画 latency/cost critical path，给出 baseline 与优化后 p50/p95、tokens、cost/success 对照表。

### 本章参考架构

```mermaid
flowchart TB
  REQ[Request] --> ROUTE[Model/Tool Routing]
  ROUTE --> CACHE[Prefix/Result Cache]
  CACHE --> LOOP[Agent Loop]
  LOOP --> PAR[Parallelizable Work]
  LOOP --> SER[Serial Critical Path]
  PAR --> OUT[Outcome]
  SER --> OUT
  OUT --> MET[Quality / Reliability / Latency / Cost]
```

> 图是本章公共心智模型；回答本题时只展开与题目相关的节点，避免把所有组件一次性画满。

## 3A. Production Deep Dive：把概念变成系统协议

### 3A.1 核心机制

Agent optimization 要同时看 quality/reliability/latency/cost/safety，并以 Pareto 或 constrained objective 决策

**Source of Truth：** Experiment registry。在面试中主动指出这一点很重要，因为 Agent 的自然语言状态只是“认知状态”，真正能决定是否继续、是否重试、是否完成的通常是外部持久状态或环境。

### 3A.2 推荐状态 / 数据模型

```text
LatencySpan { run_id, span_type, start, end, wait_ms, compute_ms }
CostLedger { run_id, model_tokens, tool_cost, compute_cost, total }
ModelRoute { task_features, model, reason, fallback }
CacheEntry { key, input_version, value_ref, ttl, invalidation_tag }
```

这不是要求所有系统都使用同一 schema；重点是把本题涉及的**身份、版本、状态、结果引用和恢复语义**从自然语言中提取出来，变成可验证 contract。

### 3A.3 具体故障场景

> **Scenario**：solve-rate +2% 但 cost×5、p95×3 仍被称为优化

排查时不要只看最终回答。建议从 `goal/version → model decision → policy → tool/action → environment mutation → persisted state → grader` 顺序追踪，确认“模型认为发生了什么”与“环境实际发生了什么”在哪一步分叉。

### 3A.4 可证伪实验

**Experiment：** 建立 Pareto frontier + rollout gate。

一个好的 Harness 改动必须能写成可证伪假设，例如：“如果这个机制解决了目标 failure mode，那么在固定 model/task/env 后，专项指标应改善；如果没有改善，就不应把复杂度长期留在 runtime。”

**Success criterion / SLO：** 没有单指标虚假胜利。

### 3A.5 Production Checklist

- [ ] 延迟分解到 model/tool/queue/sandbox/retry
- [ ] 优化看 cost per successful task 而非单次调用成本
- [ ] 缓存与并行化都计算一致性/失效代价
- [ ] 模型路由有 fallback 与 quality guardrail
- [ ] 所有优化通过 Pareto + regression 判断

## 4. Failure Modes：低分答案与真实故障

- 成功率 +2% 但成本翻 5 倍仍称优化

### 生产环境再多想三层

- **Detectability**：这个失败在 trace / state diff / tool result / grader 中留下什么证据？
- **Recoverability**：失败后是 retry、replan、compensate、rollback、ask human，还是 terminate？
- **Blast Radius**：错误最多影响一次 tool call、一个 run、一个 tenant，还是外部真实世界？

## 5. Trade-offs：不要只讲“最佳方案”

降低 latency 往往通过并行、缓存和更小模型实现，但可能提高成本、陈旧风险或降低边缘任务质量。

面试中建议明确给出 baseline，并说明新机制增加了什么复杂度、成本或延迟。只有当它针对一个可观测 failure mode，并带来可测量收益时，才值得进入 Harness。

## 6. 最小 Eval：怎样证明设计有效

一个可复用的最小实验框架：

1. 固定 task set、model version、environment version。
2. 只改变本题讨论的一个 Harness 变量。
3. 每个 task 运行多 trial，记录 outcome + trace。
4. 按 failure taxonomy 聚类，不只比较平均分。
5. 同时报告质量、稳定性、延迟、token/cost 和安全指标。

### 建议观测指标

- `p50/p95 E2E latency`
- `TTFT`
- `tokens per success`
- `cost per success`
- `quality under budget`

**本题专项 Eval：** 建议画 latency/cost critical path，给出 baseline 与优化后 p50/p95、tokens、cost/success 对照表。

## 7. 面试追问

- 如果这个机制失败，你会在 Trace 中看到什么证据？

- 如何构造一个最小 Eval 来证明你的设计真的比 baseline 更好？

- 如果要求成本下降 40%，你会优先移除或简化哪一层？

建议继续自问：

- 这个设计里**谁拥有最终真相**：模型、数据库、环境、grader，还是人工？
- 如果请求在任意一步 crash，**恢复点**在哪里？
- 如果模型能力提升一代，这个 Harness 机制还需要吗？怎样做 ablation？

## 8. 90 秒回答版本

先给结论：同时报告 solve rate、reliability、latency、tokens、cost、turns、tool calls、human intervention 和 failure severity。 Optimization 必须报告 quality/reliability/latency/cost 的联合变化，并明确 Pareto 是否真的改善。 建议画 latency/cost critical path，给出 baseline 与优化后 p50/p95、tokens、cost/success 对照表。

## 9. 5 分钟深挖版本

5 分钟展开时，按 `结论 → failure mode → 最小设计 → 数据/状态语义 → trade-off → eval/metrics` 六步回答。本题的关键工程焦点是：Optimization 必须报告 quality/reliability/latency/cost 的联合变化，并明确 Pareto 是否真的改善。 具体落地时，优先产出：建议画 latency/cost critical path，给出 baseline 与优化后 p50/p95、tokens、cost/success 对照表。

## 10. PDF 原稿中的工程证据 / 研究结论

_PDF 原稿未单列此节。_

> 本节只整理 PDF 原稿已有证据；下面“扩展阅读”是本仓库新增的外部资料，不与 PDF 原始内容混淆。

## 11. Offer 级回答结构

建议用 4 段式回答：①先给结论和适用边界；②解释 failure mode，也就是“为什么需要它”；③给出最小实现和关键数据结构；④主动给出 trade-off + eval 指标。这样能把概念答案升级为工程答案。第九章复盘：把 10 道题串成一个系统本章一句话 性能优化先看 critical path，再看 tokens/cost/quality；缓存、并行、模型路由和预算控制都必须通过 Eval 比较 Pareto。第十章 System Design / Coding / Debugging本章核心 把前九章组合成完整系统设计：Coding Agent、Research Agent、平台、多租户、Trace、Checkpoint与回归定位。系统设计题考查的是把模型能力、后端可靠性、安全边界和评测闭环统一起来，而不是画一个“LLM +Tools”的方框。本章面试目标

- 能画完整 Coding/Research/Support/Platform 架构。

- 能写 checkpoint/trace/permission schema。

- 能从 solve-rate regression 做证据驱动调试。

可以进一步升级为 6 段：`结论 → Why/Failure → How/Data Model → Recovery/Security → Trade-off → Eval/SLO`。

## 12. 扩展阅读（Repo 增补）

- [Anthropic - Scaling Managed Agents](https://www.anthropic.com/engineering/managed-agents)
- [OpenAI Agents SDK - Tracing](https://openai.github.io/openai-agents-python/tracing/)

## 13. 关联题

- 本章：[第九章 Cost / Latency / Performance](README.md)
- [Q89. 怎样给 Agent 设置 Cost Budget？](q89-agent-cost-budget.md)
- [Q91. 系统设计：设计一个 Coding Agent。](../10-system-design-debugging/q91-design-coding-agent.md)

## 14. 专业深挖：把“会回答”升级为“会设计”

### 14.1 核心判断与边界

**核心判断：** Agent Optimization 必须同时看质量、可靠性、延迟、成本、安全，并报告 Pareto 改善。

**必须讲清的边界：** 只看 solve-rate 容易用巨大成本换小幅质量。

这意味着面试时不能只描述一个 happy path。应先明确 **source of truth、可接受的错误语义、不可违反的不变量、恢复策略**，再谈具体框架。Agent 优化是多目标约束问题，应看成功质量、可靠性、延迟、成本和安全的 Pareto 前沿。

### 14.2 设计审查：上线前必须回答的问题

- [ ] 是否拆 critical path
- [ ] 成本是否按成功任务归一
- [ ] 缓存是否安全失效
- [ ] 并行是否有边际收益
- [ ] 模型路由是否可升级

对于本题，还要额外确认：

1. **最坏情况下会错成什么样？** 不只问“会不会失败”，而是问错误是否会变成重复副作用、状态漂移、越权、成本爆炸或不可恢复。
2. **系统如何知道自己错了？** 至少需要一个环境信号、结构化状态、grader 或 trace 证据，而不是模型自我反省。
3. **失败后下一步是否确定？** retry、repair、reconcile、compensate、rollback、ask-human、terminate 应尽量由错误类型和策略决定。
4. **模型升级后是否仍需要这层机制？** 若答案无法用 ablation 验证，Harness 很容易累积成永久技术债。

### 14.3 推荐的实现接口 / 状态语义

```python
class RunBudget:
    max_cost_usd: float
    deadline_ms: int
    max_tokens: int
    max_tool_calls: int
    max_subagents: int
```

本题最值得落到白板或代码里的 Artifact 是：**输出 Pareto frontier 和 decision memo。**

建议所有关键对象都带 `run_id / version / timestamp / provenance`；涉及副作用时再加入 `operation_id / idempotency_key`，涉及安全时加入 `principal / tenant / policy_version`。这样 trace、checkpoint、audit 和 eval 才能关联成同一条因果链。

### 14.4 Fault Injection：如何主动证明系统能扛住坏情况

**故障注入场景：** 新方案 solve +2%，cost×4、p95×3。

专业的 Harness 测试不应该只做“模型有没有回答对”，而应把故障点插到**状态提交边界、网络边界、权限边界、上下文转换边界**。测试成功的标准不是“不报错”，而是：

- 最终状态可解释；
- 不产生不可接受的重复副作用；
- trace 能定位失败阶段；
- recovery 不依赖人工猜测；
- 若无法自动恢复，系统能安全停在可人工处理的状态。

### 14.5 可证伪实验 / Ablation

**实验：** baseline vs candidate 多维 paired eval。

建议用 paired trials：固定 task set、model、environment、seed policy 和 grader，只改变本题对应的 Harness primitive。至少运行足够多 trial 以看到方差，并同时报告均值与分位数/置信区间。若方案只提升平均 solve-rate，却显著恶化尾延迟、成本或高风险错误率，应明确写成 trade-off，而不是宣布“全面提升”。

### 14.6 指标：至少同时看质量、稳定性和系统代价

| 指标 | Why | 建议切片 |
|---|---|---|
| `success` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `cost_per_success` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `p95` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `reliability` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `safety` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |

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

高级回答会按产品价值函数选择 operating point，而不是一个万能分数。

面试官通常会继续追问“为什么不是更简单的方案”。因此答案中应主动给出 **baseline → failure evidence → mechanism → measurable gain → added complexity → rollback/ablation plan**，这比只列组件更能体现 Agent Systems 能力。

### 14.9 进一步阅读（Repo 研究层，不等同 PDF 原稿）

- [Anthropic - Managed Agents](https://www.anthropic.com/engineering/managed-agents)
- [OpenAI Codex Agents role](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/)
- [OpenAI Agents SDK - Tracing](https://openai.github.io/openai-agents-python/tracing/)

---

[← Q89](q89-agent-cost-budget.md) · [章节目录](README.md) · [Q91 →](../10-system-design-debugging/q91-design-coding-agent.md)
