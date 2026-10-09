---
id: q93
title: "系统设计：设计 Customer Support Agent。"
chapter: 10
difficulty: "★★★★☆"
frequency: "★★★☆☆"
role: "Senior / Staff Agent Systems"
source_pdf_page: 86
tags: [10-system-design-debugging, agent-harness, interview, agents]
status: expanded
---

# Q93. 系统设计：设计 Customer Support Agent。

> **一句话结论**：身份、政策检索、客户状态、动作权限、升级人工和审计比聊天体验更重要。
>
> **难度**：★★★★☆　**高频**：★★★☆☆　**岗位**：Senior / Staff Agent Systems　**PDF**：第 86 页起

[← Q92](q92-design-deep-research-agent.md) · [章节目录](README.md) · [Q94 →](q94-design-multi-tenant-agent-platform.md)

> **内容分层**：第 1–13 节以 PDF 原稿为主并做结构化整理；第 14 节是 Repo v1.1 的工程扩展，结合公开一手资料与系统设计方法补强。


## 1. 面试官真正想考什么

你能否把前面所有原语组合成一套可落地、可调试、可演进的系统。

**更深一层：** Customer Support Agent 首先是身份与政策执行系统，其次才是聊天系统；退款/改订等 action 必须有授权与状态验证。

## 2. Know-Why：为什么这是 Harness 问题

系统设计题考查的是把模型能力、后端可靠性、安全边界和评测闭环统一起来，而不是画一个“LLM +Tools”的方框。针对本题，关键不是记住术语，而是识别系统中的“控制点”：身份、政策检索、客户状态、动作权限、升级人工和审计比聊天体验更重要。 这类控制点一旦缺失，模型即使单次推理正确，也可能因为重试、上下文污染、环境状态、权限或错误反馈而在真实任务中失败。

### 三条工程不变量

1. 先画最小闭环，再添加横切能力；不要一上来画“微服务宇宙”。
2. 每个系统设计必须给出核心数据模型、关键 API、SLO 和 failure recovery。
3. 优化与调试必须通过对照实验/消融建立因果证据。

这些不变量不是“最佳实践口号”，而是用来约束设计空间的。面试时如果方案违反其中一条，应主动解释为什么值得承担风险，以及如何用实验和监控把风险显式化。

## 3. Know-How：怎样落到生产系统

- verify identity -> retrieve policy -> reason -> action -> verify state -> confirm。

- 把这一机制做成可配置、可追踪、可评测的 runtime primitive。

### 推荐的工程 Artifact

建议用 45 分钟系统设计模板：Goal -> Environment -> Loop -> State -> Security -> Recovery -> Eval -> SLO。

### 本章参考架构

```mermaid
flowchart TB
  U[User] --> RM[Run Manager]
  RM --> CB[Context Builder]
  CB --> L[LLM]
  L --> P[Policy]
  P --> TR[Tool Router]
  TR --> ENV[Sandbox / APIs / Browser]
  ENV --> ST[State + Checkpoint]
  ST --> CB
  RM --> EV[Eval]
  RM --> OT[Trace / Observability]
```

> 图是本章公共心智模型；回答本题时只展开与题目相关的节点，避免把所有组件一次性画满。

## 3A. Production Deep Dive：把概念变成系统协议

### 3A.1 核心机制

Support Agent 必须把 identity/policy/customer-state/action authorization/handoff 组合成受控闭环

**Source of Truth：** CRM/order system + policy。在面试中主动指出这一点很重要，因为 Agent 的自然语言状态只是“认知状态”，真正能决定是否继续、是否重试、是否完成的通常是外部持久状态或环境。

### 3A.2 推荐状态 / 数据模型

```text
Run { id, goal, tenant, status, budget, version }
Checkpoint { run_id, version, state_ref, event_offset, env_ref }
Operation { id, run_id, tool, state, idempotency_key, result_ref }
TraceSpan { span_id, parent_id, kind, input_ref, output_ref, latency, cost }
EvalResult { run_id, task_id, graders, outcome, failure_class }
```

这不是要求所有系统都使用同一 schema；重点是把本题涉及的**身份、版本、状态、结果引用和恢复语义**从自然语言中提取出来，变成可验证 contract。

### 3A.3 具体故障场景

> **Scenario**：模型给出正确退款建议却对错误账户执行退款

排查时不要只看最终回答。建议从 `goal/version → model decision → policy → tool/action → environment mutation → persisted state → grader` 顺序追踪，确认“模型认为发生了什么”与“环境实际发生了什么”在哪一步分叉。

### 3A.4 可证伪实验

**Experiment：** identity/authz/amount boundary cases。

一个好的 Harness 改动必须能写成可证伪假设，例如：“如果这个机制解决了目标 failure mode，那么在固定 model/task/env 后，专项指标应改善；如果没有改善，就不应把复杂度长期留在 runtime。”

**Success criterion / SLO：** unauthorized action=0。

### 3A.5 Production Checklist

- [ ] 先画闭环再画微服务
- [ ] 给出数据模型、关键 API、SLO、failure recovery
- [ ] 把安全/状态/评测作为横切能力
- [ ] 每个设计都说明 source of truth 与 blast radius
- [ ] 调优必须用 version matrix + ablation 建因果证据

## 4. Failure Modes：低分答案与真实故障

- 能回答退款政策就自动退款

### 生产环境再多想三层

- **Detectability**：这个失败在 trace / state diff / tool result / grader 中留下什么证据？
- **Recoverability**：失败后是 retry、replan、compensate、rollback、ask human，还是 terminate？
- **Blast Radius**：错误最多影响一次 tool call、一个 run、一个 tenant，还是外部真实世界？

## 5. Trade-offs：不要只讲“最佳方案”

系统设计越通用越容易过度抽象；面试中应先给针对场景的最小闭环，再说明扩展点。

面试中建议明确给出 baseline，并说明新机制增加了什么复杂度、成本或延迟。只有当它针对一个可观测 failure mode，并带来可测量收益时，才值得进入 Harness。

## 6. 最小 Eval：怎样证明设计有效

一个可复用的最小实验框架：

1. 固定 task set、model version、environment version。
2. 只改变本题讨论的一个 Harness 变量。
3. 每个 task 运行多 trial，记录 outcome + trace。
4. 按 failure taxonomy 聚类，不只比较平均分。
5. 同时报告质量、稳定性、延迟、token/cost 和安全指标。

### 建议观测指标

- `solve rate`
- `reliability`
- `p95 latency`
- `cost/success`
- `human intervention rate`
- `incident/debug MTTR`

**本题专项 Eval：** 建议用 45 分钟系统设计模板：Goal -> Environment -> Loop -> State -> Security -> Recovery -> Eval -> SLO。

## 7. 面试追问

- 如果这个机制失败，你会在 Trace 中看到什么证据？

- 如何构造一个最小 Eval 来证明你的设计真的比 baseline 更好？

- 请把设计落到核心数据模型、关键 API 和两个 SLO 上。

建议继续自问：

- 这个设计里**谁拥有最终真相**：模型、数据库、环境、grader，还是人工？
- 如果请求在任意一步 crash，**恢复点**在哪里？
- 如果模型能力提升一代，这个 Harness 机制还需要吗？怎样做 ablation？

## 8. 90 秒回答版本

先给结论：身份、政策检索、客户状态、动作权限、升级人工和审计比聊天体验更重要。 Customer Support Agent 首先是身份与政策执行系统，其次才是聊天系统；退款/改订等 action 必须有授权与状态验证。 建议用 45 分钟系统设计模板：Goal -> Environment -> Loop -> State -> Security -> Recovery -> Eval -> SLO。

## 9. 5 分钟深挖版本

5 分钟展开时，按 `结论 → failure mode → 最小设计 → 数据/状态语义 → trade-off → eval/metrics` 六步回答。本题的关键工程焦点是：Customer Support Agent 首先是身份与政策执行系统，其次才是聊天系统；退款/改订等 action 必须有授权与状态验证。 具体落地时，优先产出：建议用 45 分钟系统设计模板：Goal -> Environment -> Loop -> State -> Security -> Recovery -> Eval -> SLO。

## 10. PDF 原稿中的工程证据 / 研究结论

_PDF 原稿未单列此节。_

> 本节只整理 PDF 原稿已有证据；下面“扩展阅读”是本仓库新增的外部资料，不与 PDF 原始内容混淆。

## 11. Offer 级回答结构

建议用 4 段式回答：①先给结论和适用边界；②解释 failure mode，也就是“为什么需要它”；③给出最小实现和关键数据结构；④主动给出 trade-off + eval 指标。这样能把概念答案升级为工程答案。

可以进一步升级为 6 段：`结论 → Why/Failure → How/Data Model → Recovery/Security → Trade-off → Eval/SLO`。

## 12. 扩展阅读（Repo 增补）

- [Anthropic - Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [Anthropic - Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [SWE-agent paper](https://arxiv.org/abs/2405.15793)

## 13. 关联题

- 本章：[第十章 System Design / Coding / Debugging](README.md)
- [Q92. 系统设计：设计一个 Deep Research Agent。](q92-design-deep-research-agent.md)
- [Q94. 系统设计：设计 Multi-Tenant Agent Platform。](q94-design-multi-tenant-agent-platform.md)

## 14. 专业深挖：把“会回答”升级为“会设计”

### 14.1 核心判断与边界

**核心判断：** Customer Support Agent 是权限与业务规则综合题：身份、政策检索、账户状态、可逆动作、升级人工。

**必须讲清的边界：** 回答政策与执行退款是不同风险等级，必须分开授权。

这意味着面试时不能只描述一个 happy path。应先明确 **source of truth、可接受的错误语义、不可违反的不变量、恢复策略**，再谈具体框架。系统设计题要把前九章组合成可落地、可恢复、可安全运行、可评测的闭环。

### 14.2 设计审查：上线前必须回答的问题

- [ ] source of truth
- [ ] 关键 API/data model
- [ ] 故障恢复
- [ ] 安全边界
- [ ] SLO/Eval
- [ ] 扩展与成本

对于本题，还要额外确认：

1. **最坏情况下会错成什么样？** 不只问“会不会失败”，而是问错误是否会变成重复副作用、状态漂移、越权、成本爆炸或不可恢复。
2. **系统如何知道自己错了？** 至少需要一个环境信号、结构化状态、grader 或 trace 证据，而不是模型自我反省。
3. **失败后下一步是否确定？** retry、repair、reconcile、compensate、rollback、ask-human、terminate 应尽量由错误类型和策略决定。
4. **模型升级后是否仍需要这层机制？** 若答案无法用 ablation 验证，Harness 很容易累积成永久技术债。

### 14.3 推荐的实现接口 / 状态语义

```python
# Design order
Goal -> Environment -> Observation -> Action Space
     -> State -> Control -> Recovery -> Security
     -> Eval -> Economics -> Observability
```

本题最值得落到白板或代码里的 Artifact 是：**画 Verify→RetrievePolicy→Reason→Action→VerifyState。**

建议所有关键对象都带 `run_id / version / timestamp / provenance`；涉及副作用时再加入 `operation_id / idempotency_key`，涉及安全时加入 `principal / tenant / policy_version`。这样 trace、checkpoint、audit 和 eval 才能关联成同一条因果链。

### 14.4 Fault Injection：如何主动证明系统能扛住坏情况

**故障注入场景：** 未验证身份就执行账户修改。

专业的 Harness 测试不应该只做“模型有没有回答对”，而应把故障点插到**状态提交边界、网络边界、权限边界、上下文转换边界**。测试成功的标准不是“不报错”，而是：

- 最终状态可解释；
- 不产生不可接受的重复副作用；
- trace 能定位失败阶段；
- recovery 不依赖人工猜测；
- 若无法自动恢复，系统能安全停在可人工处理的状态。

### 14.5 可证伪实验 / Ablation

**实验：** policy compliance + identity + action safety suite。

建议用 paired trials：固定 task set、model、environment、seed policy 和 grader，只改变本题对应的 Harness primitive。至少运行足够多 trial 以看到方差，并同时报告均值与分位数/置信区间。若方案只提升平均 solve-rate，却显著恶化尾延迟、成本或高风险错误率，应明确写成 trade-off，而不是宣布“全面提升”。

### 14.6 指标：至少同时看质量、稳定性和系统代价

| 指标 | Why | 建议切片 |
|---|---|---|
| `resolution_rate` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `policy_violation` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `handoff_rate` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `customer_latency` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |

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

Staff 级会讨论 policy versioning、transaction limits、PII、audit 和 human escalation。

面试官通常会继续追问“为什么不是更简单的方案”。因此答案中应主动给出 **baseline → failure evidence → mechanism → measurable gain → added complexity → rollback/ablation plan**，这比只列组件更能体现 Agent Systems 能力。

### 14.9 进一步阅读（Repo 研究层，不等同 PDF 原稿）

- [OpenAI Codex Agents role](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/)
- [Anthropic - Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)
- [SWE-agent](https://arxiv.org/abs/2405.15793)

---

[← Q92](q92-design-deep-research-agent.md) · [章节目录](README.md) · [Q94 →](q94-design-multi-tenant-agent-platform.md)
