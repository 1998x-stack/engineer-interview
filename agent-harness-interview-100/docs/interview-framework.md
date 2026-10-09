# 面试回答框架：Know-Why × Know-How

每一道题都尽量按下面 12 个问题组织，而不是背框架 API：

1. **Goal**：系统究竟要完成什么？什么叫成功？
2. **Environment**：Agent 操作的真实世界是什么？
3. **Observation**：模型能看到什么？哪些信息不可信？
4. **Action Space**：可以执行哪些工具和副作用？
5. **State**：状态存在哪里？哪些必须持久化？
6. **Control Loop**：下一步由谁决定？何时停止？
7. **Failure**：典型失败模式是什么？
8. **Recovery**：失败、超时、Crash 后如何恢复？
9. **Security**：权限、凭证、Sandbox、Blast Radius 如何控制？
10. **Evaluation**：如何证明完成，而不是依赖模型自述？
11. **Economics**：Latency / Token / Cost 如何约束？
12. **Observability**：如何从 Trace 还原一次失败？

## Offer 级回答公式

`结论 + 边界 → Why/Failure → How/数据结构 → Recovery/Security → Trade-off → Eval/SLO`

如果回答中没有出现**状态语义、失败恢复、证据或指标**，通常仍停留在概念层。


## 45 分钟 System Design 的时间切片

| 时间 | 要做什么 | 面试官要看到什么 |
|---|---|---|
| 0–5 min | 明确 goal / success / risk / scale | 你不会在需求不清时直接画架构 |
| 5–12 min | 画最小闭环：Observe→Decide→Act→Verify | 掌握 Agent 核心 loop |
| 12–22 min | 展开 state、tools、permission、sandbox | 能落到 production primitives |
| 22–30 min | durability：retry/idempotency/checkpoint/cancel | 分布式系统基础扎实 |
| 30–37 min | eval/trace/SLO/cost | 知道如何证明系统有效 |
| 37–45 min | trade-off、故障案例、扩展性 | 能做 Senior/Staff 级 design review |

## 从低分到高分的回答层级

**L1 名词层**：会说 ReAct、MCP、RAG、LangGraph。

**L2 组件层**：会画 Model / Tool / Memory / Planner。

**L3 协议层**：能讲 state transition、error contract、permission、idempotency、checkpoint。

**L4 证据层**：能给 trace、fault injection、eval、ablation、SLO。

**L5 取舍层**：能解释为什么不选更复杂方案，以及什么时候删除某个 Harness primitive。

面试目标至少达到 L3；Senior 候选人应稳定达到 L4，Staff 候选人需要在关键题上表现出 L5。

## 白板时强制写出的 7 个词

`source of truth`、`operation_id`、`stop reason`、`policy`、`checkpoint`、`trace`、`verifier`。

如果一个 Agent 设计无法回答这 7 个词分别落在哪里，通常还停留在 demo 架构。
