# 30 天 Agent Harness 面试冲刺计划

> PDF 附录 A 的 GitHub 化版本。目标不是按天机械刷题，而是把知识从“名词”升级到“可口述、可画图、可实现、可评测”。

| 阶段 | 主题 | 必须产出的 Artifact |
|---|---|---|
| Day 1-5 | Loop / Tool / Context | 手写最小 Agent Loop；实现 4 个工具；完成一次 tool-selection eval |
| Day 6-10 | Memory / RAG / Multi-Agent | 设计 working/long-term memory；实现 agentic retrieval；比较 single vs multi-agent |
| Day 11-15 | Long-running / Checkpoint | 实现 progress artifact、checkpoint、resume；模拟 crash 与 side-effect reconciliation |
| Day 16-20 | Security / Permission | 设计 policy engine、sandbox threat model、scoped credentials、audit trace |
| Day 21-25 | Eval / Distributed Systems | 构建 30 task eval set；多 trial；实现 retry/idempotency/cancellation 设计题 |
| Day 26-30 | System Design / Mock | 每天 1 道 45 分钟系统设计；Q91/Q92/Q94/Q99/Q100 至少各复述两次 |

## 每天 45 分钟训练法

1. **10 分钟**：不看答案口述 3 题。
2. **15 分钟**：选择 1 题画状态机 / 数据模型 / 调用链。
3. **10 分钟**：列 5 个 failure modes，并指出可观测证据。
4. **10 分钟**：设计最小 eval 与至少两个 SLO/指标。

## Repo 增补：每 5 天做一次闭环复盘

- 从错题中选 3 个“只会概念、不会落地”的问题。
- 为每题补一份可执行 artifact：schema、伪代码、时序图或 eval case。
- 把新 failure 归到 [`failure-taxonomy.md`](failure-taxonomy.md)。
- 更新自己的“90 秒答案”，确保不依赖背诵长段落。


## 每日输出物

每天至少产出一种可检查 Artifact，而不是只阅读：

- 状态机 / Mermaid 图；
- JSON/Pydantic schema；
- fault-injection case；
- eval table / ablation matrix；
- 90 秒录音提纲；
- 5 分钟白板答案；
- 一次 production incident 的 root-cause memo。

### Day 30 自测标准

随机抽 10 题：8 题能在 90 秒内结构化回答；随机抽 3 题：能在 5 分钟内落到数据模型、失败恢复和指标；随机抽 1 道系统设计：45 分钟完成完整闭环并主动讨论两种 trade-off。

