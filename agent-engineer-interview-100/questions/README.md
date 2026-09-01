# 100 道 Agent Engineer 面试题

每个问题独立为一个 Markdown 文件；题号是稳定 ID，方便引用、Issue、PR 和自动化工具处理。

| 题号 | 问题 | 能力轴 | 频率 | 难度 | 必刷 |
|---|---|---|---|---|---|
| [Q001](01-agent-loop-architecture/q001.md) | LLM、Workflow 和 Agent 有什么区别？什么时候不应该使用 Agent？ | Agent 架构与 Agent Loop | 必考 | 中 |  |
| [Q002](01-agent-loop-architecture/q002.md) | 不使用任何 Agent 框架，如何从零实现一个最小 Agent Loop？ | Agent 架构与 Agent Loop | 必考 | 中 | ⭐ |
| [Q003](01-agent-loop-architecture/q003.md) | 为什么说 Agent Loop 本质上可以看成状态机？State 里应该保存什么？ | Agent 架构与 Agent Loop | 高频 | 中 |  |
| [Q004](01-agent-loop-architecture/q004.md) | 生产 Agent 中，哪些逻辑交给 LLM，哪些逻辑必须写死在代码里？ | Agent 架构与 Agent Loop | 必考 | 中 | ⭐ |
| [Q005](01-agent-loop-architecture/q005.md) | Graph Engineer 和 Loop Engineer 的核心区别是什么？ | Agent 架构与 Agent Loop | 高频 | 中 |  |
| [Q006](01-agent-loop-architecture/q006.md) | Agent 的最终完成条件如何定义？为什么不能相信模型说‘完成了’？ | Agent 架构与 Agent Loop | 高频 | 中 |  |
| [Q007](01-agent-loop-architecture/q007.md) | Agent 的 Structured Output 校验失败怎么办？ | Agent 架构与 Agent Loop | 高频 | 中 |  |
| [Q008](01-agent-loop-architecture/q008.md) | 一个 Agent 系统应该有几层状态？ | Agent 架构与 Agent Loop | 中频 | 中 |  |
| [Q009](01-agent-loop-architecture/q009.md) | 什么是 Agent Harness？它和 Prompt、Agent Framework 的区别是什么？ | Agent 架构与 Agent Loop | 必考 | 难 |  |
| [Q010](01-agent-loop-architecture/q010.md) | 请构建一个 Agent Failure Taxonomy。 | Agent 架构与 Agent Loop | 必考 | 难 | ⭐ |
| [Q011](02-planning-control/q011.md) | ReAct、Plan-and-Execute、Reflection 分别适合什么任务？ | Planning、Reflection 与任务控制 | 高频 | 中 |  |
| [Q012](02-planning-control/q012.md) | Planner 输出的计划为什么不能直接执行？ | Planning、Reflection 与任务控制 | 必考 | 中 | ⭐ |
| [Q013](02-planning-control/q013.md) | Agent 执行一半跑偏了，如何在中间发现？ | Planning、Reflection 与任务控制 | 必考 | 难 | ⭐ |
| [Q014](02-planning-control/q014.md) | 计划执行到第三步发现环境变化，全部重规划还是局部重规划？ | Planning、Reflection 与任务控制 | 中频 | 难 |  |
| [Q015](02-planning-control/q015.md) | ReAct Agent 为什么经常死循环？怎么识别？ | Planning、Reflection 与任务控制 | 必考 | 中 | ⭐ |
| [Q016](02-planning-control/q016.md) | max_steps 设置 10 还是 100？依据是什么？ | Planning、Reflection 与任务控制 | 中频 | 中 |  |
| [Q017](02-planning-control/q017.md) | 什么时候 Agent 应该向用户澄清，而不是继续猜？ | Planning、Reflection 与任务控制 | 高频 | 中 |  |
| [Q018](02-planning-control/q018.md) | Reflection 为什么不是简单让模型‘再想一次’？ | Planning、Reflection 与任务控制 | 高频 | 中 |  |
| [Q019](02-planning-control/q019.md) | 一个需要运行 2 小时的任务如何拆分，避免后期越来越跑偏？ | Planning、Reflection 与任务控制 | 必考 | 难 |  |
| [Q020](02-planning-control/q020.md) | 用户在 Agent 执行第 18 步时点击取消，系统如何正确停止？ | Planning、Reflection 与任务控制 | 高频 | 难 |  |
| [Q021](03-tools-mcp/q021.md) | Function Calling 背后模型如何决定调用哪个工具？ | Tool Calling、MCP 与外部动作 | 必考 | 中 | ⭐ |
| [Q022](03-tools-mcp/q022.md) | Agent 总在两个类似工具之间选错，怎么解决？ | Tool Calling、MCP 与外部动作 | 必考 | 中 |  |
| [Q023](03-tools-mcp/q023.md) | 工具调用 timeout 了，你会直接 retry 吗？ | Tool Calling、MCP 与外部动作 | 必考 | 难 | ⭐ |
| [Q024](03-tools-mcp/q024.md) | 支付 API 成功但响应丢失，Agent 认为失败并重试，如何避免重复执行？ | Tool Calling、MCP 与外部动作 | 必考 | 难 | ⭐ |
| [Q025](03-tools-mcp/q025.md) | Tool 返回 partial success，接口应该怎么表达？ | Tool Calling、MCP 与外部动作 | 中频 | 中 |  |
| [Q026](03-tools-mcp/q026.md) | 五个工具可以并行调用，如何决定并行还是串行？ | Tool Calling、MCP 与外部动作 | 高频 | 中 |  |
| [Q027](03-tools-mcp/q027.md) | Tool 返回 100K tokens，直接塞回 context 会发生什么？ | Tool Calling、MCP 与外部动作 | 必考 | 中 |  |
| [Q028](03-tools-mcp/q028.md) | MCP 和普通 Function Calling 有什么本质区别？ | Tool Calling、MCP 与外部动作 | 必考 | 中 |  |
| [Q029](03-tools-mcp/q029.md) | 几百个 MCP Tool 全部暴露给模型为什么是坏设计？ | Tool Calling、MCP 与外部动作 | 高频 | 难 |  |
| [Q030](03-tools-mcp/q030.md) | 设计一个 Production Tool Gateway。 | Tool Calling、MCP 与外部动作 | 必考 | 难 | ⭐ |
| [Q031](04-multi-agent/q031.md) | 什么时候 Multi-Agent 比 Single-Agent 更好？什么时候反而更差？ | Multi-Agent 通信与协作 | 必考 | 中 |  |
| [Q032](04-multi-agent/q032.md) | Orchestrator-Worker 架构怎么设计？ | Multi-Agent 通信与协作 | 必考 | 难 |  |
| [Q033](04-multi-agent/q033.md) | 多个 Agent 使用异步 JSON 消息通信，你会设计哪些字段？ | Multi-Agent 通信与协作 | 必考 | 难 | ⭐ |
| [Q034](04-multi-agent/q034.md) | Agent 消息丢失、重复、乱序分别怎么办？ | Multi-Agent 通信与协作 | 必考 | 难 | ⭐ |
| [Q035](04-multi-agent/q035.md) | 主 Agent 怎么知道子 Agent 真正完成？ | Multi-Agent 通信与协作 | 必考 | 难 | ⭐ |
| [Q036](04-multi-agent/q036.md) | Handoff 时传整个聊天记录还是最小上下文？ | Multi-Agent 通信与协作 | 高频 | 中 |  |
| [Q037](04-multi-agent/q037.md) | 两个 Agent 对同一问题给出冲突结论怎么办？ | Multi-Agent 通信与协作 | 高频 | 难 |  |
| [Q038](04-multi-agent/q038.md) | 多个 Agent 相互调用进入无限‘甩锅循环’，怎么发现和阻断？ | Multi-Agent 通信与协作 | 必考 | 难 | ⭐ |
| [Q039](04-multi-agent/q039.md) | 8 个 Worker 中一个失败，要不要整个任务失败？ | Multi-Agent 通信与协作 | 中频 | 中 |  |
| [Q040](04-multi-agent/q040.md) | 多 Agent 如何实现 Context、Storage、Permission 完全隔离，又允许必要交换？ | Multi-Agent 通信与协作 | 必考 | 难 |  |
| [Q041](05-context-memory/q041.md) | 长任务 Context Window 快爆了怎么办？ | Context Engineering 与 Memory | 必考 | 难 | ⭐ |
| [Q042](05-context-memory/q042.md) | Context Compaction 和 Context Reset 有什么区别？ | Context Engineering 与 Memory | 必考 | 难 |  |
| [Q043](05-context-memory/q043.md) | 摘要会丢关键细节，如何保证压缩后 Agent 不失忆？ | Context Engineering 与 Memory | 必考 | 难 | ⭐ |
| [Q044](05-context-memory/q044.md) | 什么是 Context Pollution？如何判断 context 已经‘脏了’？ | Context Engineering 与 Memory | 高频 | 中 |  |
| [Q045](05-context-memory/q045.md) | 100K token context budget 应该怎么分配？ | Context Engineering 与 Memory | 中频 | 中 |  |
| [Q046](05-context-memory/q046.md) | 多 Agent 是否应该共享同一个 Context？ | Context Engineering 与 Memory | 高频 | 中 |  |
| [Q047](05-context-memory/q047.md) | Agent 什么内容值得写入长期记忆？ | Context Engineering 与 Memory | 必考 | 中 |  |
| [Q048](05-context-memory/q048.md) | 长期记忆出现两条互相冲突的信息怎么办？ | Context Engineering 与 Memory | 高频 | 难 |  |
| [Q049](05-context-memory/q049.md) | Semantic、Episodic、Procedural Memory 分别解决什么问题？ | Context Engineering 与 Memory | 中频 | 中 |  |
| [Q050](05-context-memory/q050.md) | 怎么证明你的 Memory 系统真的有效？ | Context Engineering 与 Memory | 必考 | 难 |  |
| [Q051](06-agentic-rag/q051.md) | Agent 中 RAG 应该一直执行，还是作为 Tool 按需调用？ | Agentic RAG | 高频 | 中 |  |
| [Q052](06-agentic-rag/q052.md) | 模型怎么判断自己现在需要检索？ | Agentic RAG | 高频 | 中 |  |
| [Q053](06-agentic-rag/q053.md) | Chunk 越大越好吗？ | Agentic RAG | 高频 | 中 |  |
| [Q054](06-agentic-rag/q054.md) | 为什么生产 RAG 常采用 Hybrid Retrieval + Rerank？ | Agentic RAG | 必考 | 中 |  |
| [Q055](06-agentic-rag/q055.md) | Retriever 找错资料，Agent 根据错误资料执行错误动作，怎么解决？ | Agentic RAG | 必考 | 难 |  |
| [Q056](06-agentic-rag/q056.md) | Agent 如何做 Multi-hop / Iterative Retrieval？ | Agentic RAG | 高频 | 难 |  |
| [Q057](06-agentic-rag/q057.md) | 有 ACL 的企业知识库，是 retrieval 前过滤还是 retrieval 后过滤？ | Agentic RAG | 必考 | 难 |  |
| [Q058](06-agentic-rag/q058.md) | 知识库一分钟更新一次，但向量索引十分钟更新一次，Agent 如何避免读旧数据？ | Agentic RAG | 高频 | 难 |  |
| [Q059](06-agentic-rag/q059.md) | RAG 到底怎么评估？ | Agentic RAG | 必考 | 难 |  |
| [Q060](06-agentic-rag/q060.md) | 向量数据库挂了，Agent 是直接失败还是降级？ | Agentic RAG | 高频 | 中 |  |
| [Q061](07-durable-execution/q061.md) | 一个 Agent 运行 40 分钟，第 39 分钟进程 crash，怎么办？ | Durable Execution 与 Fault Tolerance | 必考 | 难 | ⭐ |
| [Q062](07-durable-execution/q062.md) | Checkpoint 应该保存什么？ | Durable Execution 与 Fault Tolerance | 必考 | 中 |  |
| [Q063](07-durable-execution/q063.md) | Tool 已执行成功，但 Agent 在写 checkpoint 前 crash，会发生什么？ | Durable Execution 与 Fault Tolerance | 必考 | 难 | ⭐ |
| [Q064](07-durable-execution/q064.md) | 哪些错误应该 retry，哪些绝对不应该 retry？ | Durable Execution 与 Fault Tolerance | 必考 | 中 |  |
| [Q065](07-durable-execution/q065.md) | Agent 为什么需要 Circuit Breaker？ | Durable Execution 与 Fault Tolerance | 高频 | 中 |  |
| [Q066](07-durable-execution/q066.md) | 整个 Agent SLA 30 秒，内部 5 个工具 timeout 怎么分？ | Durable Execution 与 Fault Tolerance | 高频 | 中 |  |
| [Q067](07-durable-execution/q067.md) | 流量突然增长 20 倍，Agent 队列怎么保护系统？ | Durable Execution 与 Fault Tolerance | 高频 | 难 |  |
| [Q068](07-durable-execution/q068.md) | 同一用户同时启动两个修改同一资源的 Agent，怎么办？ | Durable Execution 与 Fault Tolerance | 高频 | 难 |  |
| [Q069](07-durable-execution/q069.md) | Agent 已执行 A、B、C，D 失败，需要 rollback，怎么设计？ | Durable Execution 与 Fault Tolerance | 必考 | 难 |  |
| [Q070](07-durable-execution/q070.md) | v1 代码产生的 checkpoint，在 v2 发布后如何恢复？ | Durable Execution 与 Fault Tolerance | 高频 | 难 |  |
| [Q071](08-eval-observability/q071.md) | Agent 每次 Run 到底应该 Trace 什么？ | Evaluation、Tracing 与 Observability | 必考 | 中 | ⭐ |
| [Q072](08-eval-observability/q072.md) | 线上 Agent 成功率从 85% 降到 70%，怎么定位？ | Evaluation、Tracing 与 Observability | 必考 | 难 |  |
| [Q073](08-eval-observability/q073.md) | Agent Eval Dataset 怎么构建？ | Evaluation、Tracing 与 Observability | 必考 | 中 |  |
| [Q074](08-eval-observability/q074.md) | 为什么 Agent 不能只评最终答案？ | Evaluation、Tracing 与 Observability | 必考 | 难 |  |
| [Q075](08-eval-observability/q075.md) | LLM-as-a-Judge 有什么问题？ | Evaluation、Tracing 与 Observability | 高频 | 中 |  |
| [Q076](08-eval-observability/q076.md) | 修改一句 System Prompt，怎么确定没有让其他任务退化？ | Evaluation、Tracing 与 Observability | 必考 | 中 |  |
| [Q077](08-eval-observability/q077.md) | Agent 在线 A/B Test 应该观察什么？ | Evaluation、Tracing 与 Observability | 高频 | 中 |  |
| [Q078](08-eval-observability/q078.md) | 怎么在线发现一个 Agent 已经开始 runaway？ | Evaluation、Tracing 与 Observability | 必考 | 难 |  |
| [Q079](08-eval-observability/q079.md) | 用户说‘Agent 答错了’，怎么判断是 Model、RAG、Tool 还是 Planner 的问题？ | Evaluation、Tracing 与 Observability | 必考 | 难 | ⭐ |
| [Q080](08-eval-observability/q080.md) | Agent 的 SLO 应该怎么定义？ | Evaluation、Tracing 与 Observability | 高频 | 难 |  |
| [Q081](09-security-hitl/q081.md) | 网页里的 Prompt Injection 告诉 Agent‘忽略之前指令’，怎么办？ | Security、Permission 与 HITL | 必考 | 难 |  |
| [Q082](09-security-hitl/q082.md) | 什么叫 Least Privilege Agent？ | Security、Permission 与 HITL | 必考 | 中 |  |
| [Q083](09-security-hitl/q083.md) | 什么操作应该 Human-in-the-Loop？ | Security、Permission 与 HITL | 必考 | 中 |  |
| [Q084](09-security-hitl/q084.md) | 执行代码的 Agent 为什么要 Sandbox？ | Security、Permission 与 HITL | 高频 | 难 |  |
| [Q085](09-security-hitl/q085.md) | Tracing 很重要，但 Trace 中包含用户敏感信息怎么办？ | Security、Permission 与 HITL | 高频 | 中 |  |
| [Q086](09-security-hitl/q086.md) | Multi-Tenant Agent 如何保证 A 公司数据不会进入 B 公司 Context？ | Security、Permission 与 HITL | 必考 | 难 |  |
| [Q087](09-security-hitl/q087.md) | 工具标记为 read-only、destructive、idempotent 有什么意义？ | Security、Permission 与 HITL | 高频 | 中 |  |
| [Q088](09-security-hitl/q088.md) | Agent 调第三方工具需要 Credential，Credential 应该放在哪里？ | Security、Permission 与 HITL | 必考 | 中 |  |
| [Q089](09-security-hitl/q089.md) | 权限控制应该放在 Prompt、Agent、Tool Gateway 还是业务 API？ | Security、Permission 与 HITL | 必考 | 难 |  |
| [Q090](09-security-hitl/q090.md) | Memory Poisoning 怎么解决？ | Security、Permission 与 HITL | 必考 | 难 |  |
| [Q091](10-performance-system-design/q091.md) | 一个 Agent 每次任务需要 200K tokens，怎么降到 50K？ | 性能、成本与综合系统设计 | 必考 | 难 |  |
| [Q092](10-performance-system-design/q092.md) | 是否所有步骤都需要最强模型？ | 性能、成本与综合系统设计 | 高频 | 中 |  |
| [Q093](10-performance-system-design/q093.md) | Agent 哪些东西适合缓存？ | 性能、成本与综合系统设计 | 高频 | 中 |  |
| [Q094](10-performance-system-design/q094.md) | 并行 10 个 Agent 一定比串行更快吗？ | 性能、成本与综合系统设计 | 高频 | 中 |  |
| [Q095](10-performance-system-design/q095.md) | 怎么设计 Agent latency budget？ | 性能、成本与综合系统设计 | 必考 | 难 |  |
| [Q096](10-performance-system-design/q096.md) | Agent 怎么做 Load Test？ | 性能、成本与综合系统设计 | 高频 | 难 |  |
| [Q097](10-performance-system-design/q097.md) | 遇到 LLM Rate Limit 怎么办？ | 性能、成本与综合系统设计 | 高频 | 中 |  |
| [Q098](10-performance-system-design/q098.md) | 100 个用户和 100 万用户的 Agent architecture 最大区别在哪里？ | 性能、成本与综合系统设计 | 必考 | 难 |  |
| [Q099](10-performance-system-design/q099.md) | Agent 成本怎么归因？ | 性能、成本与综合系统设计 | 必考 | 中 |  |
| [Q100](10-performance-system-design/q100.md) | 综合系统设计：设计一个每天 100 万请求的企业级 Customer Support Agent。 | 性能、成本与综合系统设计 | 压轴 | 难 |  |

## 章节导航

- [CHAPTER 01 · Agent 架构与 Agent Loop](01-agent-loop-architecture/README.md) — Q001–Q010
- [CHAPTER 02 · Planning、Reflection 与任务控制](02-planning-control/README.md) — Q011–Q020
- [CHAPTER 03 · Tool Calling、MCP 与外部动作](03-tools-mcp/README.md) — Q021–Q030
- [CHAPTER 04 · Multi-Agent 通信与协作](04-multi-agent/README.md) — Q031–Q040
- [CHAPTER 05 · Context Engineering 与 Memory](05-context-memory/README.md) — Q041–Q050
- [CHAPTER 06 · Agentic RAG](06-agentic-rag/README.md) — Q051–Q060
- [CHAPTER 07 · Durable Execution 与 Fault Tolerance](07-durable-execution/README.md) — Q061–Q070
- [CHAPTER 08 · Evaluation、Tracing 与 Observability](08-eval-observability/README.md) — Q071–Q080
- [CHAPTER 09 · Security、Permission 与 HITL](09-security-hitl/README.md) — Q081–Q090
- [CHAPTER 10 · 性能、成本与综合系统设计](10-performance-system-design/README.md) — Q091–Q100
