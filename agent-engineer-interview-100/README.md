# Agent Engineer Offer 100

> **生产级智能体工程面试手册 · GitHub Edition**  
> 从 Agent Loop 到 Multi-Agent、Context、RAG、Durable Execution、Eval、Security 与 Production System Design。

[![Questions](https://img.shields.io/badge/questions-100-blue)](#100-道题) [![Chapters](https://img.shields.io/badge/chapters-10-orange)](#能力轴) [![Focus](https://img.shields.io/badge/focus-Agent%20Reliability-success)](docs/04-reliability-first.md) [![PDF](https://img.shields.io/badge/PDF-122%20pages-red)](assets/Agent_Engineer_Offer_100_Interview_Handbook.pdf)

## 为什么有这个仓库

Agent 岗面试已经不再主要考“用过哪个框架”，而是在追问：

- 多 Agent 通信丢消息、重复、乱序怎么办？
- Context Window 快爆了如何 compaction / reset？
- Tool timeout 为什么不能直接 retry？
- Agent 执行一半跑偏，怎么在中途发现？
- Worker crash 后如何从 checkpoint 恢复？
- 如何避免重复退款、重复下单等副作用？
- RAG 错误为什么会进一步放大成错误行动？
- Prompt Injection、权限、HITL 如何落到可信执行层？
- 成功率下降时，怎么定位 first bad transition？

这 100 题的主线只有一句话：

> **让 Agent 成功并不难；真正的工程能力，是让它可控地失败。**

## 快速入口

- 📚 [100 道题总索引](questions/README.md)
- 🧭 [10 条能力轴](docs/03-capability-map.md)
- 🛡️ [Reliability First 六步答题框架](docs/04-reliability-first.md)
- ⭐ [20 道必刷题](docs/05-priority-20.md)
- 🧱 [系统设计白板模板](docs/06-whiteboard-system-design.md)
- 📅 [7 天冲刺计划](docs/07-7-day-plan.md)
- 🧪 [面试评分 Rubric](docs/10-interview-rubric.md)
- 🧠 [Expanded Edition 内容设计规范](docs/12-expanded-edition-methodology.md)
- ✅ [Content Quality Gate](docs/13-content-quality.md)
- 📝 [模拟面试评分模板](templates/mock-interview-scorecard.md)
- 🏗️ [系统设计回答模板](templates/system-design-answer-template.md)
- 📄 [122 页 PDF](assets/Agent_Engineer_Offer_100_Interview_Handbook.pdf)

## 能力轴

| # | 章节 | 范围 | 核心关键词 |
|---:|---|---|---|
| 01 | [Agent 架构与 Agent Loop](questions/01-agent-loop-architecture/README.md) | Q001–Q010 | Agent Loop / State / Harness / Completion |
| 02 | [Planning、Reflection 与任务控制](questions/02-planning-control/README.md) | Q011–Q020 | Plan / ReAct / Reflection / Drift / Stop |
| 03 | [Tool Calling、MCP 与外部动作](questions/03-tools-mcp/README.md) | Q021–Q030 | Tool / MCP / Idempotency / Gateway |
| 04 | [Multi-Agent 通信与协作](questions/04-multi-agent/README.md) | Q031–Q040 | Protocol / Handoff / Isolation / Coordination |
| 05 | [Context Engineering 与 Memory](questions/05-context-memory/README.md) | Q041–Q050 | Context / Compaction / Memory / Provenance |
| 06 | [Agentic RAG](questions/06-agentic-rag/README.md) | Q051–Q060 | Retrieval / Hybrid / Rerank / ACL / Eval |
| 07 | [Durable Execution 与 Fault Tolerance](questions/07-durable-execution/README.md) | Q061–Q070 | Checkpoint / Retry / Saga / Versioning |
| 08 | [Evaluation、Tracing 与 Observability](questions/08-eval-observability/README.md) | Q071–Q080 | Trace / Eval / Regression / SLO |
| 09 | [Security、Permission 与 HITL](questions/09-security-hitl/README.md) | Q081–Q090 | Injection / Least Privilege / HITL / Sandbox |
| 10 | [性能、成本与综合系统设计](questions/10-performance-system-design/README.md) | Q091–Q100 | Latency / Cost / Scale / System Design |

## 100 道题

每个问题都是独立的 **Expanded Professional Markdown**，不再只是提纲：

**题目定位 → 核心 Invariant → 面试官意图 → 30 秒回答 → 3 分钟专业展开 → 架构/状态设计 → 伪代码 → Failure Modes → Trade-off → Metrics → 连续追问 → Know-Why / Know-How → Production Checklist → 关联题目**。

因此可以把每一题当成一个小型系统设计章节独立阅读。

进入：[questions/README.md](questions/README.md)

### 20 道必刷

[Q002](questions/01-agent-loop-architecture/q002.md) · [Q004](questions/01-agent-loop-architecture/q004.md) · [Q010](questions/01-agent-loop-architecture/q010.md) · [Q012](questions/02-planning-control/q012.md) · [Q013](questions/02-planning-control/q013.md) · [Q015](questions/02-planning-control/q015.md) · [Q021](questions/03-tools-mcp/q021.md) · [Q023](questions/03-tools-mcp/q023.md) · [Q024](questions/03-tools-mcp/q024.md) · [Q030](questions/03-tools-mcp/q030.md) · [Q033](questions/04-multi-agent/q033.md) · [Q034](questions/04-multi-agent/q034.md) · [Q035](questions/04-multi-agent/q035.md) · [Q038](questions/04-multi-agent/q038.md) · [Q041](questions/05-context-memory/q041.md) · [Q043](questions/05-context-memory/q043.md) · [Q061](questions/07-durable-execution/q061.md) · [Q063](questions/07-durable-execution/q063.md) · [Q071](questions/08-eval-observability/q071.md) · [Q079](questions/08-eval-observability/q079.md)

## Reliability First

遇到“Agent 出问题怎么办”，不要先报方案。先按六步组织：

```text
Detect → Classify → Contain → Recover → Preserve → Verify
```

详见：[docs/04-reliability-first.md](docs/04-reliability-first.md)

## Repository Structure

```text
agent-engineer-interview-100/
├── README.md
├── assets/
│   └── Agent_Engineer_Offer_100_Interview_Handbook.pdf
├── questions/
│   ├── README.md
│   ├── 01-agent-loop-architecture/
│   │   ├── README.md
│   │   ├── q001.md
│   │   └── ... q010.md
│   └── ...
├── docs/
│   ├── 01-publication-note.md
│   ├── 02-preface.md
│   ├── 03-capability-map.md
│   ├── 04-reliability-first.md
│   ├── 05-priority-20.md
│   ├── 06-whiteboard-system-design.md
│   ├── 07-7-day-plan.md
│   ├── 08-glossary.md
│   ├── 09-references.md
│   ├── 10-interview-rubric.md
│   ├── 11-repo-architecture.md
│   ├── 12-expanded-edition-methodology.md
│   └── 13-content-quality.md
├── data/
│   ├── questions.json
│   └── questions.csv
├── scripts/
│   ├── validate_repo.py
│   ├── build_index.py
│   ├── check_links.py
│   └── random_interview.py
├── templates/
│   ├── mock-interview-scorecard.md
│   └── system-design-answer-template.md
└── .github/
    ├── workflows/validate.yml
    ├── ISSUE_TEMPLATE/
    └── pull_request_template.md
```

## 使用方法

### 求职者

1. 第一遍只读“30 秒回答”。
2. 第二遍遮住答案，按 Reliability First 六步答。
3. 第三遍只练 20 道必刷，每题回答 3 分钟。
4. 最后单独攻 Q100，并接受 20 个连续系统设计追问。

### 面试官

可使用 `scripts/random_interview.py` 按章节、难度和频率抽题：

```bash
python scripts/random_interview.py --count 5 --difficulty 难
python scripts/random_interview.py --chapter 4 --count 3
python scripts/random_interview.py --priority20 --count 5
```

### 仓库维护者

```bash
python scripts/validate_repo.py
python scripts/build_index.py --check
python scripts/check_links.py
```

## 内容来源边界

- Q001–Q100、前言、能力地图、Reliability 框架、20 道必刷、白板模板、7 天计划、术语和参考说明均由 PDF 源内容结构化迁移。
- `docs/10-interview-rubric.md` 与 `docs/11-repo-architecture.md` 是 GitHub 版本新增的工程化扩展，并在文件中明确标注。
- 仓库不会重新分发参考资料书籍原文件，只提供本项目原创面试手册 PDF。

详见：[参考资料与来源说明](docs/09-references.md)。

## Contributing

欢迎提交：概念修正、工程案例、追问改进、题目标签、面试评分建议和新的 failure mode。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

**核心原则：Know-Why + Know-How。不要停留在“会用框架”，要能解释“为什么这样设计，以及失败时系统怎么活下来”。**
