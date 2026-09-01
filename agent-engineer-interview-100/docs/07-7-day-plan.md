# 7 天 Agent Engineer 面试冲刺计划

> 每天目标不是“看完 15 题”，而是形成可复用的回答模型。

## Day 1 — Agent Runtime 基础

**范围**：Q001–Q010

训练：

1. 手画最小 Agent Loop。
2. 定义 AgentState。
3. 列出“必须写死在代码中的 invariant”。
4. 给 10 类 failure taxonomy 各写一个 signal。

当天输出：不用任何框架名，3 分钟解释 Agent Runtime。

## Day 2 — Planning + Tool Semantics

**范围**：Q011–Q030

重点：Q012 / Q013 / Q015 / Q021 / Q023 / Q024 / Q030。

训练：

- 给 ReAct loop 写 stagnation detector。
- 分别处理 read-only timeout 和 payment timeout。
- 画 Tool Gateway。
- 解释 exactly-once 为什么通常是业务语义而不是传输保证。

## Day 3 — Multi-Agent / Protocol

**范围**：Q031–Q040

训练：

- 设计 Task + Message + Artifact schema。
- 注入 duplicate / out-of-order / late result。
- 画 A→B→C→A 调用环并设计 cycle guard。
- 比较 Single-Agent vs Multi-Agent 的净收益。

## Day 4 — Context / Memory / RAG

**范围**：Q041–Q060

训练：

- 把 lossless state 与 lossy context 分开。
- 给 100K token budget 做分配。
- 设计 Memory write/read policy。
- 画 retrieval evidence pipeline。
- 解释 ACL / freshness 为什么是 RAG correctness 的一部分。

## Day 5 — Durable Execution

**范围**：Q061–Q070

这是最建议动手画状态机的一天。

训练故障：

1. Tool success → checkpoint 前 crash。
2. Worker 在 39 分钟 crash。
3. Queue redelivery。
4. v1 checkpoint 用 v2 code 恢复。

每个场景都用 `Detect → Classify → Contain → Recover → Preserve → Verify`。

## Day 6 — Eval / Security / Production

**范围**：Q071–Q099

训练：

- 画 Trace span tree。
- 做一次 first-bad-transition 归因。
- 设计 Prompt Injection trust boundary。
- 列 HITL 风险分级。
- 设计 8 秒 latency budget。
- 解释 cost/task 和 cost/success 的区别。

## Day 7 — Q100 全真模拟

独立完成 [Q100](../questions/10-performance-system-design/q100.md)。

### 45 分钟节奏

- 0–5 min：需求/SLO。
- 5–15 min：主架构 + state。
- 15–25 min：Tool / RAG / Multi-Agent。
- 25–35 min：failure / security / HITL。
- 35–40 min：trace/eval/cost。
- 40–45 min：连续追问。

## 每天评分

使用 [Mock Interview Scorecard](../templates/mock-interview-scorecard.md)，重点看：

- 结论是否先行。
- 是否先定义 invariant。
- 是否主动讲 failure mode。
- 是否有结构化 state。
- 是否有可验证指标。
- 是否解释 trade-off。

## 最终合格线

- 20 道必刷均可 30 秒回答。
- 至少 10 道能稳定讲 3–5 分钟。
- Q100 不看资料完成完整白板。
- 任意故障题都能自然进入 Reliability First 六步。
