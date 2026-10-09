# Repo 结构与维护约定

这个仓库把“书”拆成 **可独立阅读、可链接、可评测、可持续维护** 的知识单元。

```text
agent-harness-interview-100/
├── README.md
├── CHANGELOG.md
├── LICENSE.md
├── MANIFEST.json
├── book/
│   └── Agent_Harness_面试100题_题目驱动精讲_2026.pdf
├── assets/architecture/
│   └── *.png
├── docs/
│   ├── INDEX.md
│   ├── question-matrix.md
│   ├── source-map.md
│   ├── architecture.md
│   ├── interview-framework.md
│   ├── glossary.md
│   ├── questions/
│   │   ├── 01-agent-loop-harness/
│   │   │   ├── README.md
│   │   │   └── q01-...md ... q10-...md
│   │   └── ... 10 chapters / 100 questions
│   ├── learning-paths/
│   └── appendices/
├── scripts/
│   └── validate_repo.py
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/content-check.yml
├── mkdocs.yml
└── requirements-docs.txt
```

## 为什么一题一个 Markdown

它同时解决四个问题：

1. **面试训练**：单题可直接分享、复习、做 flashcard；
2. **知识演进**：MCP、SDK、模型与生产实践变化时，可局部更新；
3. **工程关联**：通过 Related Questions 把知识组织成图，而不是只能线性翻书；
4. **质量治理**：CI 能逐题检查 metadata、必需章节和链接完整性。

## 内容分层

每题明确区分：

- **PDF-derived core**：来自原 PDF 的题干、核心解释、Know-Why/How、Failure Modes、Trade-off、追问与证据；
- **Repo expansion**：Production Deep Dive、状态模型、实验、SLO、Checklist、扩展阅读；
- **External references**：优先官方文档、论文与一手工程文章，并与 PDF 原始来源分开列出。

## 修改一题时的 Definition of Done

提交前至少确认：

- [ ] 题目核心结论没有被外部补充内容悄悄改写；
- [ ] Why 解释了 failure mode，而不只是下定义；
- [ ] How 至少落到一个数据结构、状态机、API 或 runtime primitive；
- [ ] 明确 source of truth；
- [ ] 至少有一个 concrete failure scenario；
- [ ] 至少有一个可证伪的 eval / fault-injection / ablation；
- [ ] Trade-off 同时讨论收益与复杂度/成本/延迟/风险；
- [ ] 关联题链接正确；
- [ ] 运行 `python scripts/validate_repo.py` 通过。


## 内容层级约定

每道题分成三层，便于长期维护：

1. **Source Layer**：PDF 原稿明确支持的题干、Know-Why/How、证据；
2. **Teaching Layer**：面试回答、Failure Modes、Trade-offs、追问、关联题；
3. **Engineering Research Layer**：第 14 节的 production design、fault injection、ablation、metrics 与 2026 一手资料。

新增事实时应先判断属于哪一层，避免“后来研究到的内容”被误标成原 PDF 来源。

