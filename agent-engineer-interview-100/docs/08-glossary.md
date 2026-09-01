# Agent Engineering 术语速查

> 面试里术语不是越多越好。关键是能给出**工程语义、边界和典型 failure mode**。

| 术语 | 工程定义 | 常见误解 |
|---|---|---|
| Agent Loop | 模型决策、工具执行、观察回写、终止验证的迭代控制流 | 等同于 while tool_call |
| Harness | 包围模型的工具、状态、权限、上下文、恢复、观测和生命周期控制 | 等同于 Prompt |
| Invariant | 系统任何时刻都不能违反的条件 | 写在 System Prompt 就算约束 |
| State | 可被 runtime 持久化/迁移/验证的任务事实 | 所有 messages |
| Context | 当前模型调用的有限工作集 | 所有历史数据 |
| Compaction | 在同一连续任务中压缩上下文历史 | 等同于随便 summary |
| Context Reset | 用结构化 handoff 在新上下文边界继续任务 | 清空历史重新猜 |
| Memory | 跨轮/跨任务可检索复用的信息系统 | 把全部对话 embedding |
| Provenance | 信息来自哪里、何时、以什么权限获得 | 只有 source URL |
| Idempotency | 同一逻辑操作重复请求不会重复产生业务结果 | HTTP retry 不报错 |
| operation_id | 跨 retry/crash 稳定的逻辑操作身份 | 每次请求重新生成 UUID |
| Reconciliation | 恢复时查询/对账外部真实状态，修正本地未知状态 | 再执行一次 |
| Compensation | Saga 中对已执行步骤进行语义上的逆操作 | 数据库 rollback 的同义词 |
| Checkpoint | 可恢复执行的持久化状态快照 | 保存聊天历史 |
| Durable Execution | 进程故障后基于持久状态恢复长期工作流 | 服务器永不重启 |
| Circuit Breaker | 下游持续异常时快速失败，限制故障扩散 | 一种 retry |
| Deadline Propagation | 父任务剩余时间传给所有子调用 | 每个服务独立 timeout |
| Backpressure | 过载时限制进入/积压速度保护系统 | 无限加队列 |
| Handoff | 把任务控制权/上下文契约转移给另一个 Agent | 复制全部聊天记录 |
| Artifact | 任务生成的持久化、可引用结果 | 消息正文 |
| Task Ownership | 哪个组件负责某任务状态和完成判定 | 谁最后回复用户 |
| At-least-once | 消息/请求可能被重复交付 | 业务一定重复 |
| Exactly-once | 常作为业务最终效果目标，需要幂等/去重等机制逼近 | 网络层天然保证一次 |
| Retrieval Trigger | 判断何时需要检索 | 永远 top-k |
| Hybrid Retrieval | 组合 sparse/dense 等不同召回信号 | 两个向量库 |
| Rerank | 对候选证据进行更精细重排 | 再做一次向量搜索 |
| Grounding | 输出/动作被可信证据约束 | 只要用了 RAG 就 grounded |
| Trajectory Eval | 评价中间决策与动作路径 | 只评 final answer |
| First Bad Transition | 执行轨迹中第一个从正确状态转向错误状态的点 | 最终报错位置 |
| Guardrail | 对输入/输出/工具动作执行的确定性或独立策略检查 | 另一段 Prompt |
| HITL | 在高风险/高不确定步骤暂停，等待人批准、编辑或拒绝 | 所有操作人工确认 |
| Least Privilege | 当前主体只拥有完成当前任务所需最小能力 | 只隐藏工具名 |
| Blast Radius | 一次错误可能影响的用户、资源和后续步骤范围 | 单次错误消息 |
| Cost per Success | 总资源成本 / 成功完成的业务任务数 | token 单价 |

## MCP / A2A 快速区分

- **Function Calling**：模型输出一个结构化工具调用。
- **MCP**：标准化 Host/Client/Server 与 tools/resources/prompts 等外部能力集成。
- **A2A**：独立 Agent 系统之间的 discovery、Task、Message、Artifact 和异步协作协议。

不要把三者当同一层。
