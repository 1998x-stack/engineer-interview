---
id: q70
title: "Production Trace 应如何变成 Eval Dataset？"
chapter: 7
difficulty: "★★★★★"
frequency: "★★★★★"
role: "Harness / Infra / Backend"
source_pdf_page: 65
tags: [07-evaluation-observability, agent-harness, interview, evaluation, observability]
status: expanded
---

# Q70. Production Trace 应如何变成 Eval Dataset？

> **一句话结论**：生产失败 -> 根因分类 -> 最小复现 -> grader -> fix -> regression，是最重要的持续改进闭环。
>
> **难度**：★★★★★　**高频**：★★★★★　**岗位**：Harness / Infra / Backend　**PDF**：第 65 页起

[← Q69](q69-eval-hacking.md) · [章节目录](README.md) · [Q71 →](../08-reliability-distributed/q71-run-thread-turn-model.md)

> **内容分层**：第 1–13 节以 PDF 原稿为主并做结构化整理；第 14 节是 Repo v1.1 的工程扩展，结合公开一手资料与系统设计方法补强。


## 1. 面试官真正想考什么

你是否能用可重复实验区分“感觉更好”和“系统真的更好”。

**更深一层：** 生产 Trace -> failure clustering -> minimal reproduction -> regression case，是 Agent 工程最有复利的学习闭环。

## 2. Know-Why：为什么这是 Harness 问题

没有 eval 的 Agent 优化不可重复。Agent 的随机轨迹决定了评测必须同时记录过程、结果和多次试验的稳定性。针对本题，关键不是记住术语，而是识别系统中的“控制点”：生产失败 -> 根因分类 -> 最小复现 -> grader ->fix -> regression，是最重要的持续改进闭环。 这类控制点一旦缺失，模型即使单次推理正确，也可能因为重试、上下文污染、环境状态、权限或错误反馈而在真实任务中失败。

### 三条工程不变量

1. 评测对象是 Model × Harness × Environment，而不只是模型。
2. Outcome 优先，Trajectory 只约束真正必须约束的安全/合规路径。
3. 线上失败必须转化为可重复的 regression case。

这些不变量不是“最佳实践口号”，而是用来约束设计空间的。面试时如果方案违反其中一条，应主动解释为什么值得承担风险，以及如何用实验和监控把风险显式化。

## 3. Know-How：怎样落到生产系统

- sample/cluster traces，优先高频高损失 failure。

- 把这一机制做成可配置、可追踪、可评测的 runtime primitive。

### 推荐的工程 Artifact

从一条生产失败 trace 生成 minimal reproduction、grader 和 regression case。

### 本章参考架构

```mermaid
flowchart LR
  D[Eval Dataset] --> R[Runner]
  R --> T1[Trial 1]
  R --> T2[Trial 2]
  R --> TN[Trial N]
  T1 --> G[Graders]
  T2 --> G
  TN --> G
  G --> M[Metrics + Failure Clusters]
  M --> F[Fix]
  F --> D
```

> 图是本章公共心智模型；回答本题时只展开与题目相关的节点，避免把所有组件一次性画满。

## 3A. Production Deep Dive：把概念变成系统协议

### 3A.1 核心机制

生产 trace 应按 failure taxonomy 最小化成可重复 fixture，再进入 regression suite

**Source of Truth：** Incident corpus。在面试中主动指出这一点很重要，因为 Agent 的自然语言状态只是“认知状态”，真正能决定是否继续、是否重试、是否完成的通常是外部持久状态或环境。

### 3A.2 推荐状态 / 数据模型

```text
EvalTask { task_id, prompt_ref, env_fixture, success_criteria }
Trial { trial_id, task_id, model, harness_version, seed, trace_ref }
Outcome { trial_id, final_state_ref, artifacts, side_effects }
Grade { grader_id, rubric_version, score, rationale_ref, confidence }
EvalRun { dataset_version, trials, aggregates, failure_clusters }
```

这不是要求所有系统都使用同一 schema；重点是把本题涉及的**身份、版本、状态、结果引用和恢复语义**从自然语言中提取出来，变成可验证 contract。

### 3A.3 具体故障场景

> **Scenario**：把原始整段用户会话直接塞 eval，含隐私且不可复现

排查时不要只看最终回答。建议从 `goal/version → model decision → policy → tool/action → environment mutation → persisted state → grader` 顺序追踪，确认“模型认为发生了什么”与“环境实际发生了什么”在哪一步分叉。

### 3A.4 可证伪实验

**Experiment：** trace→redact→minimize→fixture pipeline。

一个好的 Harness 改动必须能写成可证伪假设，例如：“如果这个机制解决了目标 failure mode，那么在固定 model/task/env 后，专项指标应改善；如果没有改善，就不应把复杂度长期留在 runtime。”

**Success criterion / SLO：** incident-to-regression lead time 缩短。

### 3A.5 Production Checklist

- [ ] Eval 固定 dataset/model/harness/env 版本
- [ ] 多 trial 报告方差而非单点分数
- [ ] Outcome 优先，trajectory 只约束必要路径
- [ ] grader 有版本、校准和防作弊设计
- [ ] 生产失败自动进入 regression intake

### Production → Regression 闭环

```text
incident/complaint
  -> trace + environment snapshot
  -> redact PII/secrets
  -> minimize to smallest reproducible fixture
  -> assign failure taxonomy
  -> define expected outcome + grader
  -> add regression case
  -> verify fix
  -> keep forever unless behavior intentionally changes
```

这条闭环决定 Agent 团队能否把“线上事故”沉淀为资产。

## 4. Failure Modes：低分答案与真实故障

- 只收集“有趣案例”，无回归

### 生产环境再多想三层

- **Detectability**：这个失败在 trace / state diff / tool result / grader 中留下什么证据？
- **Recoverability**：失败后是 retry、replan、compensate、rollback、ask human，还是 terminate？
- **Blast Radius**：错误最多影响一次 tool call、一个 run、一个 tenant，还是外部真实世界？

## 5. Trade-offs：不要只讲“最佳方案”

更严格 eval 增加运行成本，但没有可靠 grader 的“优化”很容易过拟合几个样例。

面试中建议明确给出 baseline，并说明新机制增加了什么复杂度、成本或延迟。只有当它针对一个可观测 failure mode，并带来可测量收益时，才值得进入 Harness。

## 6. 最小 Eval：怎样证明设计有效

一个可复用的最小实验框架：

1. 固定 task set、model version、environment version。
2. 只改变本题讨论的一个 Harness 变量。
3. 每个 task 运行多 trial，记录 outcome + trace。
4. 按 failure taxonomy 聚类，不只比较平均分。
5. 同时报告质量、稳定性、延迟、token/cost 和安全指标。

### 建议观测指标

- `task success`
- `pass^k`
- `grader-human agreement`
- `eval variance/confidence interval`
- `regression escape rate`

**本题专项 Eval：** 从一条生产失败 trace 生成 minimal reproduction、grader 和 regression case。

## 7. 面试追问

- 如果这个机制失败，你会在 Trace 中看到什么证据？

- 如何构造一个最小 Eval 来证明你的设计真的比 baseline 更好？

- 你的 grader 会不会被 Agent 利用？怎样验证？

建议继续自问：

- 这个设计里**谁拥有最终真相**：模型、数据库、环境、grader，还是人工？
- 如果请求在任意一步 crash，**恢复点**在哪里？
- 如果模型能力提升一代，这个 Harness 机制还需要吗？怎样做 ablation？

## 8. 90 秒回答版本

先给结论：生产失败 -> 根因分类 -> 最小复现 -> grader -> fix -> regression，是最重要的持续改进闭环。 生产 Trace -> failure clustering -> minimal reproduction -> regression case，是 Agent 工程最有复利的学习闭环。 从一条生产失败 trace 生成 minimal reproduction、grader 和 regression case。

## 9. 5 分钟深挖版本

5 分钟展开时，按 `结论 → failure mode → 最小设计 → 数据/状态语义 → trade-off → eval/metrics` 六步回答。本题的关键工程焦点是：生产 Trace -> failure clustering -> minimal reproduction -> regression case，是 Agent 工程最有复利的学习闭环。 具体落地时，优先产出：从一条生产失败 trace 生成 minimal reproduction、grader 和 regression case。

## 10. PDF 原稿中的工程证据 / 研究结论

Evidence 最有价值的 eval 数据往往来自生产 failure trace。将高损失失败压缩成最小复现并进入 regression，能让 Harness 改进形成复利。

> 本节只整理 PDF 原稿已有证据；下面“扩展阅读”是本仓库新增的外部资料，不与 PDF 原始内容混淆。

## 11. Offer 级回答结构

建议用 4 段式回答：①先给结论和适用边界；②解释 failure mode，也就是“为什么需要它”；③给出最小实现和关键数据结构；④主动给出 trade-off + eval 指标。这样能把概念答案升级为工程答案。第七章复盘：把 10 道题串成一个系统本章一句话 把 Agent 行为拆成 Task/Trial/Trace/Outcome/Grader，并让生产失败持续进入 regression，才能建立真正的 eval-driven development。第八章 Reliability / Distributed Agent Systems本章核心 Agent Harness 本质上会遭遇分布式系统问题：重试、幂等、取消、并发、一致性和故障恢复。一旦 Agent 能执行真实副作用，它就继承了分布式系统的经典难题：重复、丢失、乱序、并发、部分失败和恢复。本章面试目标

- 能把 retry/idempotency/cancellation/concurrency 讲到分布式系统级别。

- 能处理 partial failure 与 shared state。

- 能设计 durable worker。

可以进一步升级为 6 段：`结论 → Why/Failure → How/Data Model → Recovery/Security → Trade-off → Eval/SLO`。

## 12. 扩展阅读（Repo 增补）

- [Anthropic - Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI Agents SDK - Tracing](https://openai.github.io/openai-agents-python/tracing/)

## 13. 关联题

- 本章：[第七章 Evaluation / Observability](README.md)
- [Q69. Agent 会不会 Hack Eval？](q69-eval-hacking.md)
- [Q71. Run、Thread、Turn 应该怎么建模？](../08-reliability-distributed/q71-run-thread-turn-model.md)
- [Q99. Debug：Agent Solve Rate 从 72% 掉到 58%，怎么查？](../10-system-design-debugging/q99-debug-solve-rate-regression.md)
- [Q100. 给你一个 Agent，你如何系统地提升 30% Performance？](../10-system-design-debugging/q100-improve-agent-performance-30-percent.md)
- [Q61. Agent Harness 和 Eval Harness 有什么区别？](q61-agent-harness-vs-eval-harness.md)

## 14. 专业深挖：把“会回答”升级为“会设计”

### 14.1 核心判断与边界

**核心判断：** 最强的 eval 飞轮来自生产失败：trace→root cause→minimal reproduction→eval→fix→regression。

**必须讲清的边界：** 不是所有失败都直接进 eval；要去敏、去偶然噪声、最小化并标注 failure class。

这意味着面试时不能只描述一个 happy path。应先明确 **source of truth、可接受的错误语义、不可违反的不变量、恢复策略**，再谈具体框架。优化必须依赖可复现的 task/trial/outcome/grader 和完整 trace，而不是少量 demo。

### 14.2 设计审查：上线前必须回答的问题

- [ ] trial 是否隔离
- [ ] grader 是否版本化/校准
- [ ] outcome 与 trajectory 是否分离
- [ ] 统计不确定性是否报告
- [ ] 生产失败是否进入 regression

对于本题，还要额外确认：

1. **最坏情况下会错成什么样？** 不只问“会不会失败”，而是问错误是否会变成重复副作用、状态漂移、越权、成本爆炸或不可恢复。
2. **系统如何知道自己错了？** 至少需要一个环境信号、结构化状态、grader 或 trace 证据，而不是模型自我反省。
3. **失败后下一步是否确定？** retry、repair、reconcile、compensate、rollback、ask-human、terminate 应尽量由错误类型和策略决定。
4. **模型升级后是否仍需要这层机制？** 若答案无法用 ablation 验证，Harness 很容易累积成永久技术债。

### 14.3 推荐的实现接口 / 状态语义

```python
class Trial:
    task_id: str
    trial_id: str
    harness_version: str
    model_version: str
    environment_version: str
    outcome_ref: str
    trace_id: str
```

本题最值得落到白板或代码里的 Artifact 是：**设计 FailureCase lineage 到 production trace。**

建议所有关键对象都带 `run_id / version / timestamp / provenance`；涉及副作用时再加入 `operation_id / idempotency_key`，涉及安全时加入 `principal / tenant / policy_version`。这样 trace、checkpoint、audit 和 eval 才能关联成同一条因果链。

### 14.4 Fault Injection：如何主动证明系统能扛住坏情况

**故障注入场景：** 直接把完整生产 trace 当题目导致隐私泄露和不稳定。

专业的 Harness 测试不应该只做“模型有没有回答对”，而应把故障点插到**状态提交边界、网络边界、权限边界、上下文转换边界**。测试成功的标准不是“不报错”，而是：

- 最终状态可解释；
- 不产生不可接受的重复副作用；
- trace 能定位失败阶段；
- recovery 不依赖人工猜测；
- 若无法自动恢复，系统能安全停在可人工处理的状态。

### 14.5 可证伪实验 / Ablation

**实验：** 对 incident 做 reduction，比较 repro stability。

建议用 paired trials：固定 task set、model、environment、seed policy 和 grader，只改变本题对应的 Harness primitive。至少运行足够多 trial 以看到方差，并同时报告均值与分位数/置信区间。若方案只提升平均 solve-rate，却显著恶化尾延迟、成本或高风险错误率，应明确写成 trade-off，而不是宣布“全面提升”。

### 14.6 指标：至少同时看质量、稳定性和系统代价

| 指标 | Why | 建议切片 |
|---|---|---|
| `repro_rate` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `regression_catch_rate` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |
| `time_to_eval` | 衡量本题设计是否真的改善，而不是只增加 Harness 复杂度 | 建议按 task type / risk / model version 分桶 |

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

Staff 级会做 failure clustering、active sampling 和 eval coverage gap 分析。

面试官通常会继续追问“为什么不是更简单的方案”。因此答案中应主动给出 **baseline → failure evidence → mechanism → measurable gain → added complexity → rollback/ablation plan**，这比只列组件更能体现 Agent Systems 能力。

### 14.9 进一步阅读（Repo 研究层，不等同 PDF 原稿）

- [Anthropic - Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [OpenAI Agents SDK - Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [OpenAI Codex Agents role](https://openai.com/careers/ai-systems-engineer-codex-agents-san-francisco/)

---

[← Q69](q69-eval-hacking.md) · [章节目录](README.md) · [Q71 →](../08-reliability-distributed/q71-run-thread-turn-model.md)
