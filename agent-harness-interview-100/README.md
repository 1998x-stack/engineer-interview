# Agent Harness Interview 100

> 一套面向 **Agent Engineer / Agent Harness Engineer / AI Systems Engineer** 的题目驱动式面试与工程知识库。

本仓库由《Agent Harness 面试 100 题：题目驱动式深度精讲（2026）》拆分、重组并扩写而来。组织方式借鉴题目驱动型技术面试书的学习思想：**一道题对应一个知识切面，通过 Why → How → Failure Modes → Trade-offs → Eval 逐层深入**；不复制第三方图书原文或版式。

## 为什么这个 Repo 不只是“100 个答案”

Agent 工程的难点已经从 `Prompt + RAG + Function Calling` 扩展到：

- execution loop / state machine
- tool / ACI / MCP
- context engineering / memory
- planning / orchestration / multi-agent
- long-running / durable workflows
- permissions / sandbox / identity / security
- evals / tracing / observability
- retry / idempotency / cancellation / consistency
- latency / cost / capacity
- system design / debugging / ablation

因此每一道题都增加了：工程不变量、推荐 Artifact、最小 Eval、指标、失败恢复、90 秒/5 分钟回答和关联题导航。

## 导航

- [编写说明与使用方法](docs/preface.md)
- [100 题总索引](docs/INDEX.md)
- [100 题能力矩阵](docs/question-matrix.md)
- [PDF → Markdown Source Map](docs/source-map.md)
- [Repo 结构与维护约定](docs/repo-structure.md)
- [Agent Harness 总体知识地图](docs/architecture.md)
- [统一面试回答框架](docs/interview-framework.md)
- [30 天冲刺计划](docs/appendices/30-day-study-plan.md)
- [System Design 白板模板](docs/appendices/system-design-template.md)
- [Failure Taxonomy](docs/appendices/failure-taxonomy.md)
- [参考资料](docs/appendices/references.md)
- [术语表](docs/glossary.md)
- [原始 PDF](book/Agent_Harness_面试100题_题目驱动精讲_2026.pdf)

## 10 个章节

| # | 章节 | 题号 | 核心 |
|---:|---|---|---|
| 1 | [第一章 Agent Loop 与 Harness 基础](docs/questions/01-agent-loop-harness/README.md) | Q01-Q10 | 控制循环、状态、终止条件与 Model × Harness 共设计 |
| 2 | [第二章 Tool / ACI / MCP 与执行接口](docs/questions/02-tools-aci-mcp/README.md) | Q11-Q20 | 把工具视作 Agent 的 action space，而不是附属 API |
| 3 | [第三章 Context Engineering 与 Memory](docs/questions/03-context-memory/README.md) | Q21-Q30 | 把上下文视作有限预算，并区分记忆、任务状态与可重建信息 |
| 4 | [第四章 Planning / Orchestration / Multi-Agent](docs/questions/04-planning-orchestration/README.md) | Q31-Q40 | 用任务结构决定编排复杂度，并量化多 Agent 的真实增益 |
| 5 | [第五章 Long-Horizon / Durable Agent](docs/questions/05-long-horizon-durable/README.md) | Q41-Q50 | 让长任务可分解、可验证、可交接、可恢复 |
| 6 | [第六章 Permission / Sandbox / Security](docs/questions/06-permission-sandbox-security/README.md) | Q51-Q60 | 缩小 blast radius，让授权、身份与执行边界成为系统原语 |
| 7 | [第七章 Evaluation / Observability](docs/questions/07-evaluation-observability/README.md) | Q61-Q70 | 以 task/trial/trace/outcome/grader 建模，并建立生产回归闭环 |
| 8 | [第八章 Reliability / Distributed Agent Systems](docs/questions/08-reliability-distributed/README.md) | Q71-Q80 | 用分布式系统语义处理重试、幂等、取消、并发与一致性 |
| 9 | [第九章 Cost / Latency / Performance](docs/questions/09-cost-latency-performance/README.md) | Q81-Q90 | 在 Quality × Reliability × Latency × Cost × Safety 上做 Pareto 优化 |
| 10 | [第十章 System Design / Coding / Debugging](docs/questions/10-system-design-debugging/README.md) | Q91-Q100 | 把前九章组合成可落地、可评测、可运维的完整 Agent 系统 |

## 每题 Markdown 统一结构

1. 面试官真正想考什么
2. Know-Why
3. 工程不变量
4. Know-How / Artifact / 架构
5. Failure Modes
6. Trade-offs
7. 最小 Eval + 指标
8. 面试追问
9. 90 秒回答
10. 5 分钟深挖
11. PDF 原稿证据
12. 扩展阅读
13. 关联题

## 推荐使用方式

- **面试冲刺**：先做 [20 题主干路线](docs/learning-paths/core-20.md)。
- **Senior/Staff**：重点 Q16、Q24、Q36、Q45-Q46、Q51-Q70、Q73、Q80、Q91、Q99-Q100。
- **项目复盘**：按 [Failure Taxonomy](docs/appendices/failure-taxonomy.md) 把真实故障转成 eval case。
- **系统设计**：使用 [白板模板](docs/appendices/system-design-template.md)，每题强制给出 SLO 和 recovery。

## 来源边界

- **PDF-derived**：每题的核心题意、原稿 Know-Why/How、Failure Modes、Trade-off、追问与工程证据。
- **Repo expansion**：工程不变量、推荐 Artifact、最小 Eval、指标、导航与额外一手资料。
- 第三方上传资料只作为引用基线，不在仓库中重新分发。

## 内容质量保障

运行：

```bash
python scripts/validate_repo.py
```

验证 exactly 100 个题目文件、Front Matter、章节索引、相对链接和必要章节完整性。

## License / Attribution

本仓库当前不替内容所有者预设开源许可。发布到公开 GitHub 前，请阅读 [LICENSE.md](LICENSE.md) 并选择适合的内容许可（例如 CC 系列）与代码许可，并确认第三方引用边界。


## v1.1 内容深度升级

每道题新增“专业深挖”层：核心边界、上线设计审查、实现接口/状态语义、Fault Injection、可证伪 Ablation、专项指标、Debugging Playbook、Senior/Staff 信号和研究层一手资料。目标是让题库从“答案集合”升级成 **Agent Harness Design Review Handbook**。

建议阅读方式：先用 1–13 节建立题目答案，再用第 14 节训练生产设计与追问。
