# Repository Architecture

本仓库采用“**题目即最小知识单元**”的组织方式：每一道题独立 Markdown，章节负责导航，学习资料负责跨题串联，代码样例负责把关键公式落到可执行实现。

```text
recsys-interview-100/
├── README.md
├── REPO_STRUCTURE.md
├── mkdocs.yml
├── Makefile
├── manifest.json
├── requirements-docs.txt
├── .github/
│   ├── workflows/
│   │   ├── quality.yml          # 内容/链接/代码 QA
│   │   └── docs.yml             # MkDocs → GitHub Pages
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── docs/
│   ├── index.md
│   ├── assets/
│   │   └── recommender_system_interview_100_pro.pdf
│   ├── guide/
│   │   ├── how-to-use.md
│   │   └── knowledge-map.md
│   ├── questions/
│   │   ├── 01-system-architecture/
│   │   ├── 02-retrieval-embedding/
│   │   ├── 03-ranking-feature-cross/
│   │   ├── 04-sequential-modeling/
│   │   ├── 05-multitask-cvr/
│   │   ├── 06-loss-metrics-experiment/
│   │   ├── 07-bias-data-serving/
│   │   ├── 08-coldstart-diversity/
│   │   └── 09-frontier-generative/
│   ├── study/
│   │   ├── high-frequency-20.md
│   │   ├── five-level-followup.md
│   │   ├── project-grilling-template.md
│   │   └── roadmap.md
│   ├── references/
│   │   ├── README.md
│   │   └── primary-sources.md
│   └── source/
│       ├── README.md
│       └── pdf-extracted-text.txt
├── examples/
│   ├── itemcf.py
│   ├── two_tower_infonce.py
│   ├── fm.py
│   ├── metrics.py
│   ├── ab_bucket.py
│   ├── ips.py
│   └── mmr.py
└── scripts/
    ├── qa_repo.py
    ├── enrich_v2.py
    ├── enrich_followups.py
    └── polish_followups.py
```

## 为什么这样组织

1. **一个问题一个文件**：Git diff 与 PR 粒度清晰，便于单题修订、引用和复习。
2. **章节不承载大段正文**：章节 `index.md` 只负责导航，避免产生第二份“权威正文”。
3. **学习路线与题库解耦**：高频 20、7/30 天路线、项目拷打模板都通过链接组合题目，不复制题目正文。
4. **论文与面经集中治理**：参考资料集中维护；单题只列最相关来源。
5. **原 PDF 可追溯**：PDF 与抽取文本保留在 `docs/`，用于核对迁移完整性。
6. **文档即产品**：MkDocs 提供全文搜索、公式、Mermaid；GitHub Actions 保证内容可持续发布。

## 单题 Markdown 规范

每题至少包含：题目定位、30 秒回答、深入拆解、公式/机制、V2 第一性原理、90 秒标准回答、具体数量级案例、工程决策矩阵、上线验证与监控、边界条件、Senior/Staff 加分点、工业级工程视角、常见失分、评分标准、**5 个连续追问及 5 个参考答案**、自测清单、相关题、参考资料。

如要扩展题库，应优先增强现有题目的**证据、边界条件、失败案例与工程数字**，而不是机械增加更多同义题。


## V2 内容质量门槛

`scripts/qa_repo.py` 会阻止以下退化：

- 题目总数不是 100；
- 任一问题正文小于 10 KB；
- 缺少 V2 深度章节、90 秒回答、工程案例或边界分析；
- 连续追问不是严格 5 个，或缺少对应参考答案；
- 遗留通用占位答案；
- PDF 抽取造成的典型公式/模型名乱码；
- 任一本地 Markdown 交叉链接失效。

这使仓库从“一次性生成的资料”转变为可以持续 PR 维护的知识产品。
