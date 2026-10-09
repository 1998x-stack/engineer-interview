# Glossary

| 术语 | 工程定义 |
|---|---|
| Agent Harness | 围绕模型构建的运行时控制系统：context、loop、tools、state、policy、checkpoint、trace、eval 等 |
| Agent Framework | 帮助实现 Harness 的软件抽象/SDK，不等同完整生产 Harness |
| ACI | Agent-Computer Interface；Agent 与计算机/环境交互的接口设计 |
| Action Space | Agent 被允许选择的动作集合，通常由 tool schema / UI actions 定义 |
| Observation Space | Agent 每轮能看见的环境反馈、上下文和工具结果 |
| Checkpoint | 用于 durable resume 的持久化状态快照/游标，而非简单聊天记录 |
| Progress Artifact | 跨 context/session 的结构化任务进展与验证证据 |
| Idempotency | 重复执行同一 logical operation 不产生重复副作用的语义 |
| Reconciliation | crash/超时后重新确认外部副作用与内部状态是否一致 |
| Handoff | 将控制权/责任转移给另一个 Agent 或 session 的机制 |
| Evaluator-Optimizer | generator 产出、独立 evaluator 按 rubric 检查、再进行 targeted revision 的模式 |
| pass@k | k 次 trial 至少一次成功的概率/指标 |
| pass^k | k 次 trial 全部成功的概率/指标，强调稳定可靠性 |
| Blast Radius | 一次错误或越权行为可能影响的最大范围 |
| Tool Retrieval | 在大工具目录中按当前任务动态选择要暴露给模型的少量工具 |
| Context Rot/Pollution | 长上下文中因噪声、陈旧、冲突或注意力稀释导致的性能退化 |
| Brain / Hands | reasoning/orchestration 与 execution environment 的解耦架构 |


## 容易混淆的术语对

| A | B | 最重要区别 |
|---|---|---|
| Prompt | Context | Prompt 是指令的一部分；Context 是本轮 inference 的完整信息集合 |
| Memory | State | Memory 是可复用认知信息；State 是任务/环境必须可靠保存的事实 |
| Retry | Reconciliation | Retry 再执行；Reconciliation 先判断之前动作到底发生没有 |
| Permission | Sandbox | Permission 决定“可不可以”；Sandbox 强制“最多能影响哪里” |
| Trace | Audit Log | Trace 面向调试/性能；Audit 面向安全、合规和不可抵赖证据 |
| Outcome Grader | Trajectory Grader | 前者判断最终结果；后者约束过程、安全或成本 |
| Handoff | Agent-as-Tool | Handoff 转移 active ownership；Agent-as-Tool 保留 manager ownership |
| Checkpoint | Conversation History | Checkpoint 是恢复协议；History 只是模型可见文本的一部分 |

## 建议在面试中主动使用的术语

`source of truth`、`blast radius`、`fault injection`、`reconciliation`、`fencing token`、`critical path`、`paired trial`、`ablation`、`provenance`、`verified completion`。这些词只有在能解释对应机制时才使用，不要作为术语堆砌。

