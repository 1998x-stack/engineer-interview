# 最后冲刺｜20 道必刷题

1. [Q002](../questions/01-agent-loop-architecture/q002.md) · 不使用任何 Agent 框架，如何从零实现一个最小 Agent Loop？
2. [Q004](../questions/01-agent-loop-architecture/q004.md) · 生产 Agent 中，哪些逻辑交给 LLM，哪些逻辑必须写死在代码里？
3. [Q010](../questions/01-agent-loop-architecture/q010.md) · 请构建一个 Agent Failure Taxonomy。
4. [Q012](../questions/02-planning-control/q012.md) · Planner 输出的计划为什么不能直接执行？
5. [Q013](../questions/02-planning-control/q013.md) · Agent 执行一半跑偏了，如何在中间发现？
6. [Q015](../questions/02-planning-control/q015.md) · ReAct Agent 为什么经常死循环？怎么识别？
7. [Q021](../questions/03-tools-mcp/q021.md) · Function Calling 背后模型如何决定调用哪个工具？
8. [Q023](../questions/03-tools-mcp/q023.md) · 工具调用 timeout 了，你会直接 retry 吗？
9. [Q024](../questions/03-tools-mcp/q024.md) · 支付 API 成功但响应丢失，Agent 认为失败并重试，如何避免重复执行？
10. [Q030](../questions/03-tools-mcp/q030.md) · 设计一个 Production Tool Gateway。
11. [Q033](../questions/04-multi-agent/q033.md) · 多个 Agent 使用异步 JSON 消息通信，你会设计哪些字段？
12. [Q034](../questions/04-multi-agent/q034.md) · Agent 消息丢失、重复、乱序分别怎么办？
13. [Q035](../questions/04-multi-agent/q035.md) · 主 Agent 怎么知道子 Agent 真正完成？
14. [Q038](../questions/04-multi-agent/q038.md) · 多个 Agent 相互调用进入无限‘甩锅循环’，怎么发现和阻断？
15. [Q041](../questions/05-context-memory/q041.md) · 长任务 Context Window 快爆了怎么办？
16. [Q043](../questions/05-context-memory/q043.md) · 摘要会丢关键细节，如何保证压缩后 Agent 不失忆？
17. [Q061](../questions/07-durable-execution/q061.md) · 一个 Agent 运行 40 分钟，第 39 分钟进程 crash，怎么办？
18. [Q063](../questions/07-durable-execution/q063.md) · Tool 已执行成功，但 Agent 在写 checkpoint 前 crash，会发生什么？
19. [Q071](../questions/08-eval-observability/q071.md) · Agent 每次 Run 到底应该 Trace 什么？
20. [Q079](../questions/08-eval-observability/q079.md) · 用户说‘Agent 答错了’，怎么判断是 Model、RAG、Tool 还是 Planner 的问题？

> 如果只剩 2–3 天，不要再增加题量。把这 20 题练到能在白板上讲出 failure mode、控制点、状态、指标和恢复路径。

---

## Expanded Edition 使用提示

阅读任何章节时，优先寻找三个东西：**Invariant、Failure Window、Verification Signal**。如果一个方案只有组件名而没有这三项，它通常还停留在 demo 级。完整方法见 [Expanded Edition 内容设计规范](12-expanded-edition-methodology.md)。
