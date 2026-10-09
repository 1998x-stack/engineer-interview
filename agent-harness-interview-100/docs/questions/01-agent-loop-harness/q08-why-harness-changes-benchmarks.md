---
id: q08
title: "为什么同一个模型换一个 Harness，Benchmark 可能差很多？"
chapter: 1
difficulty: "★★★★☆"
frequency: "★★★★☆"
role: "Agent / Applied AI"
source_pdf_page: 11
tags: [01-agent-loop-harness, agent-harness, interview]
status: expanded
---

# Q08. 为什么同一个模型换一个 Harness，Benchmark 可能差很多？

> **一句话结论**：Harness 改变 observation space、action space、feedback quality 和 search strategy，因此会改变 模型策略分布。
>
> **难度**：★★★★☆　**高频**：★★★★☆　**岗位**：Agent / Applied AI　**PDF**：第 11 页起

[← Q07](q07-model-vs-harness-failures.md) · [章节目录](README.md) · [Q09 →](q09-agent-runtime-abstractions.md)

> **内容分层**：第 1–13 节以 PDF 原稿为主并做结构化整理；第 14 节是 Repo v1.1 的工程扩展，结合公开一手资料与系统设计方法补强。


## 1. 面试官真正想考什么

你是否理解 Agent 的“控制平面”，以及为什么生产系统不能把所有责任推给模型。

**更深一层：** 同模型不同 Harness 的差异必须用 ablation 验证；工具接口、错误反馈、context 和 edit primitives 都会改变策略分布。

## 2. Know-Why：为什么这是 Harness 问题

真正的 Agent 工程不是“让模型多想几步”，而是把一个概率策略放进可约束、可观测、可恢复的软件运行时。针对本题，关键不是记住术语，而是识别系统中的“控制点”：Harness 改变 observation space、action space、feedback quality 和 search strategy，因此会改变模型策略分布。 这类控制点一旦缺失，模型即使单次推理正确，也可能因为重试、上下文污染、环境状态、权限或错误反馈而在真实任务中失败。

### 三条工程不变量

1. 模型输出不是事实状态；关键完成条件必须由环境或结构化验证器确认。
2. 所有循环都必须有硬预算与可解释的 stop reason。
3. 任何新增 Harness 机制都应能通过 trace 和 eval 证明价值。

这些不变量不是“最佳实践口号”，而是用来约束设计空间的。面试时如果方案违反其中一条，应主动解释为什么值得承担风险，以及如何用实验和监控把风险显式化。

## 3. Know-How：怎样落到生产系统

- 对 tool schema、context、error feedback、edit interface 做独立消融。

- 把这一机制做成可配置、可追踪、可评测的 runtime primitive。

### 推荐的工程 Artifact

做 2×2 ablation：old/new model × old/new harness，再逐项替换 tool/context/error feedback。

### 本章参考架构

```mermaid
flowchart LR
  U[Goal] --> C[Context Builder]
  C --> M[Model]
  M -->|tool call| P[Policy]
  P --> T[Tool Runtime]
  T --> E[Environment]
  E --> O[Observation]
  O --> S[State Update]
  S --> C
  M -->|final| V[Goal Verifier]
```

> 图是本章公共心智模型；回答本题时只展开与题目相关的节点，避免把所有组件一次性画满。

## 3A. Production Deep Dive：把概念变成系统协议

### 3A.1 核心机制

Harness 改变 action/observation space，因此会改变模型策略分布和 benchmark

**Source of Truth：** Outcome + full trajectory。在面试中主动指出这一点很重要，因为 Agent 的自然语言状态只是“认知状态”，真正能决定是否继续、是否重试、是否完成的通常是外部持久状态或环境。

### 3A.2 推荐状态 / 数据模型

```text
Run { run_id, thread_id, goal, status, budget, context_version }
Turn { turn_id, run_id, model_call_id, stop_reason, started_at, ended_at }
Event { event_id, run_id, type, payload_ref, sequence_no }
Budget { max_turns, max_tokens, max_cost, deadline }
```

这不是要求所有系统都使用同一 schema；重点是把本题涉及的**身份、版本、状态、结果引用和恢复语义**从自然语言中提取出来，变成可验证 contract。

### 3A.3 具体故障场景

> **Scenario**：新工具更强但描述冲突导致 selection accuracy 下降

排查时不要只看最终回答。建议从 `goal/version → model decision → policy → tool/action → environment mutation → persisted state → grader` 顺序追踪，确认“模型认为发生了什么”与“环境实际发生了什么”在哪一步分叉。

### 3A.4 可证伪实验

**Experiment：** paired benchmark + trace-diff + tool-selection confusion matrix。

一个好的 Harness 改动必须能写成可证伪假设，例如：“如果这个机制解决了目标 failure mode，那么在固定 model/task/env 后，专项指标应改善；如果没有改善，就不应把复杂度长期留在 runtime。”

**Success criterion / SLO：** 同模型性能变化可解释。

### 3A.5 Production Checklist

- [ ] 明确 source of truth：goal/state/environment 谁拥有最终真相
- [ ] 所有循环都有硬预算和可观测 stop reason
- [ ] 模型输出与环境验证分离
- [ ] 运行状态可序列化，进程不是状态所有者
- [ ] 版本化 model/prompt/tools/harness，方便回归定位

## 4. Failure Modes：低分答案与真实故障

- 把 Benchmark 分数只归功于模型参数

### 生产环境再多想三层

- **Detectability**：这个失败在 trace / state diff / tool result / grader 中留下什么证据？
- **Recoverability**：失败后是 retry、replan、compensate、rollback、ask human，还是 terminate？
- **Blast Radius**：错误最多影响一次 tool call、一个 run、一个 tenant，还是外部真实世界？

## 5. Trade-offs：不要只讲“最佳方案”

更强的控制和可观测性会增加 runtime 复杂度；应从最小循环开始，只为真实 failure mode 增加机制。

面试中建议明确给出 baseline，并说明新机制增加了什么复杂度、成本或延迟。只有当它针对一个可观测 failure mode，并带来可测量收益时，才值得进入 Harness。

## 6. 最小 Eval：怎样证明设计有效

一个可复用的最小实验框架：

1. 固定 task set、model version、environment version。
2. 只改变本题讨论的一个 Harness 变量。
3. 每个 task 运行多 trial，记录 outcome + trace。
4. 按 failure taxonomy 聚类，不只比较平均分。
5. 同时报告质量、稳定性、延迟、token/cost 和安全指标。

### 建议观测指标

- `task success rate`
- `turns per task`
- `stop-reason distribution`
- `tool-selection error rate`
- `model-vs-harness failure share`

**本题专项 Eval：** 做 2×2 ablation：old/new model × old/new harness，再逐项替换 tool/context/error feedback。

## 7. 面试追问

- 如果这个机制失败，你会在 Trace 中看到什么证据？

- 如何构造一个最小 Eval 来证明你的设计真的比 baseline 更好？

- 如果要求成本下降 40%，你会优先移除或简化哪一层？

建议继续自问：

- 这个设计里**谁拥有最终真相**：模型、数据库、环境、grader，还是人工？
- 如果请求在任意一步 crash，**恢复点**在哪里？
- 如果模型能力提升一代，这个 Harness 机制还需要吗？怎样做 ablation？

## 8. 90 秒回答版本

先给结论：Harness 改变 observation space、action space、feedback quality 和 search strategy，因此会改变 模型策略分布。 同模型不同 Harness 的差异必须用 ablation 验证；工具接口、错误反馈、context 和 edit primitives 都会改变策略分布。 做 2×2 ablation：old/new model × old/new harness，再逐项替换 tool/context/error feedback。

## 9. 5 分钟深挖版本

5 分钟展开时，按 `结论 → failure mode → 最小设计 → 数据/状态语义 → trade-off → eval/metrics` 六步回答。本题的关键工程焦点是：同模型不同 Harness 的差异必须用 ablation 验证；工具接口、错误反馈、context 和 edit primitives 都会改变策略分布。 具体落地时，优先产出：做 2×2 ablation：old/new model × old/new harness，再逐项替换 tool/context/error feedback。

## 10. PDF 原稿中的工程证据 / 研究结论

Evidence SWE-agent 论文把 ACI 作为核心研究变量，显示“给模型什么接口”会显著改变软件工程任务表现。[W8]

> 本节只整理 PDF 原稿已有证据；下面“扩展阅读”是本仓库新增的外部资料，不与 PDF 原始内容混淆。

## 11. Offer 级回答结构

建议用 4 段式回答：①先给结论和适用边界；②解释 failure mode，也就是“为什么需要它”；③给出最小实现和关键数据结构；④主动给出 trade-off + eval 指标。这样能把概念答案升级为工程答案。

可以进一步升级为 6 段：`结论 → Why/Failure → How/Data Model → Recovery/Security → Trade-off → Eval/SLO`。

## 12. 扩展阅读（Repo 增补）

- [Anthropic Engineering - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [SWE-agent paper](https://arxiv.org/abs/2405.15793)
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)

## 13. 关联题

- 本章：[第一章 Agent Loop 与 Harness 基础](README.md)
- [Q07. Model 能力和 Harness 能力如何区分？](q07-model-vs-harness-failures.md)
- [Q09. Agent Runtime 最重要的抽象是什么？](q09-agent-runtime-abstractions.md)
- [Q11. 怎样设计一个 LLM-friendly Tool？](../02-tools-aci-mcp/q11-llm-friendly-tool-design.md)
- [Q99. Debug：Agent Solve Rate 从 72% 掉到 58%，怎么查？](../10-system-design-debugging/q99-debug-solve-rate-regression.md)

## 14. 专业深挖：把“会回答”升级为“会设计”

### 14.1 核心判断与边界

**核心判断：** Benchmark 测到的是 Model×Harness×Environment×Grader，而不是裸模型。

**必须讲清的边界：** 对比时必须固定工具能力、环境镜像、budget、prompt、grader；否则结果不可归因。

这意味着面试时不能只描述一个 happy path。应先明确 **source of truth、可接受的错误语义、不可违反的不变量、恢复策略**，再谈具体框架。模型负责提出下一步，运行时负责执行语义、持久状态和终止语义。

### 14.2 设计审查：上线前必须回答的问题

- [ ] 控制权是否明确
- [ ] 状态是否可恢复
- [ ] stop reason 是否可观测
- [ ] 模型与环境真相是否分离

对于本题，还要额外确认：

1. **最坏情况下会错成什么样？** 不只问“会不会失败”，而是问错误是否会变成重复副作用、状态漂移、越权、成本爆炸或不可恢复。
2. **系统如何知道自己错了？** 至少需要一个环境信号、结构化状态、grader 或 trace 证据，而不是模型自我反省。
3. **失败后下一步是否确定？** retry、repair、reconcile、compensate、rollback、ask-human、terminate 应尽量由错误类型和策略决定。
4. **模型升级后是否仍需要这层机制？** 若答案无法用 ablation 验证，Harness 很容易累积成永久技术债。

### 14.3 推荐的实现接口 / 状态语义

```python
class RunState:
    run_id: str
    status: str
    turn: int
    budget: dict
    checkpoint_version: int

# Model proposes; runtime decides/executes/persists.
```

本题最值得落到白板或代码里的 Artifact 是：**输出 benchmark configuration manifest。**

建议所有关键对象都带 `run_id / version / timestamp / provenance`；涉及副作用时再加入 `operation_id / idempotency_key`，涉及安全时加入 `principal / tenant / policy_version`。这样 trace、checkpoint、audit 和 eval 才能关联成同一条因果链。

### 14.4 Fault Injection：如何主动证明系统能扛住坏情况

**故障注入场景：** 只改变 tool-result formatting，观察 solve-rate 大幅变化。

专业的 Harness 测试不应该只做“模型有没有回答对”，而应把故障点插到**状态提交边界、网络边界、权限边界、上下文转换边界**。测试成功的标准不是“不报错”，而是：

- 最终状态可解释；
- 不产生不可接受的重复副作用；
- trace 能定位失败阶段；
- recovery 不依赖人工猜测；
- 若无法自动恢复，系统能安全停在可人工处理的状态。

### 14.5 可证伪实验 / Ablation

**实验：** 对关键 harness primitive 做逐项 ablation，并报告置信区间。

建议用 paired trials：固定 task set、model、environment、seed policy 和 grader，只改变本题对应的 Harness primitive。至少运行足够多 trial 以看到方差，并同时报告均值与分位数/置信区间。若方案只提升平均 solve-rate，却显著恶化尾延迟、成本或高风险错误率，应明确写成 trade-off，而不是宣布“全面提升”。

### 14.6 指标：至少同时看质量、稳定性和系统代价

| 指标 | Why | 建议切片 |
|---|---|---|
| `solve_rate_delta` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `cost_delta` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `variance` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |

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

高阶答案会讨论 benchmark contamination、infra noise 与 non-stationary model endpoint。

面试官通常会继续追问“为什么不是更简单的方案”。因此答案中应主动给出 **baseline → failure evidence → mechanism → measurable gain → added complexity → rollback/ablation plan**，这比只列组件更能体现 Agent Systems 能力。

### 14.9 进一步阅读（Repo 研究层，不等同 PDF 原稿）

- [OpenAI Codex Agents role](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/)
- [OpenAI Agents SDK - Running agents](https://openai.github.io/openai-agents-python/running_agents/)
- [Anthropic - Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)

---

[← Q07](q07-model-vs-harness-failures.md) · [章节目录](README.md) · [Q09 →](q09-agent-runtime-abstractions.md)
