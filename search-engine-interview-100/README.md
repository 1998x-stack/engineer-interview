# 搜索引擎算法岗面试宝典 · 100 题

> Search Relevance · Information Retrieval · Learning to Rank · ANN · Hybrid Search · RAG

这不是“100 个答案的堆叠”，而是一套按搜索系统因果链组织的面试知识库。仓库以配套 PDF 为基线，**100 道题一题一个 Markdown**，并在每题上增加工程化分析、数学恢复、追问参考回答、Gotchas、实战练习与权威参考资料。

## v2 深度增强

2026-09-02 起，100 道题全部完成第二轮专业扩展。每题在原有“30 秒回答 / 5 分钟回答 / 追问 / Gotcha”基础上新增：

- 题目特有的核心机制再拆解；
- 数据链路与可复现性要求；
- 复杂度、内存、候选数、p99 等规模感；
- 白板公式 / 伪代码 / 可执行实验抓手；
- 线上失败模式与 stage-wise diagnosis；
- 可观测性与 query slice；
- Senior / Staff 级追问与 60/75/85/90+ 回答 Rubric；
- 最小可复现实验：用 quality–cost frontier 替代纯背诵。

仓库的定位因此从“100 题题解”升级为“搜索算法 / Relevance / Retrieval 面试与工程知识库”。

## 快速入口

- 📘 [配套 PDF](assets/search_engine_interview_100.pdf)
- 📖 [使用说明与序言](docs/00-preface.md)
- 🧭 [100 题总索引](docs/INDEX.md)
- 🗺️ [3 天 / 14 天 / 按岗位学习路径](docs/STUDY_PATHS.md)
- 🧮 [核心公式速查](docs/appendices/A-formulas.md)
- 🏗️ [系统设计答题模板](docs/appendices/B-system-design-template.md)
- 🏷️ [标签索引](docs/TAGS.md)
- 📒 [术语表](docs/GLOSSARY.md)
- 🎯 [模拟面试评分 Rubric](docs/INTERVIEW_RUBRIC.md)
- ✅ [v2 内容增强与质量报告](docs/ENRICHMENT_REPORT.md)
- 📚 [技术参考资料](docs/references/README.md)

## 知识地图

```text
Query
  ↓
Understanding / Rewrite
  ↓
Lexical Recall + Dense Recall + Specialized Recall
  ↓
Fusion / PreRank
  ↓
LTR / Neural Ranker
  ↓
Cross-Encoder / ReRank / Policy
  ↓
SERP / RAG Context

Supporting loops:
Indexing & Serving  ←→  Logs & Labels & Training & A/B
```

## 章节

1. [搜索引擎全局架构](docs/questions/01-search-architecture/README.md) — Q001–Q010
2. [倒排索引与 Lucene 内核](docs/questions/02-inverted-index-lucene/README.md) — Q011–Q020
3. [TF-IDF、BM25 与词法检索](docs/questions/03-bm25-lexical-retrieval/README.md) — Q021–Q030
4. [Query Understanding 与 Query Rewrite](docs/questions/04-query-understanding/README.md) — Q031–Q040
5. [Learning to Rank：从 RankNet 到 LambdaMART](docs/questions/05-learning-to-rank/README.md) — Q041–Q052
6. [搜索指标、点击偏差与实验](docs/questions/06-evaluation-click-ab/README.md) — Q053–Q062
7. [Dense Retrieval 与 ANN](docs/questions/07-dense-retrieval-ann/README.md) — Q063–Q074
8. [Hybrid Search、Neural Reranking 与 RAG](docs/questions/08-hybrid-rag-rerank/README.md) — Q075–Q084
9. [分布式搜索与工程](docs/questions/09-search-infrastructure/README.md) — Q085–Q094
10. [综合系统设计与 0→1 方法论](docs/questions/10-system-design/README.md) — Q095–Q100

## 每题 Markdown 的统一结构

```text
YAML front matter
题目画像
面试官到底在考什么
30 秒回答
5 分钟深度回答
数学 / 白板推导（适用题）
进一步深挖：从“会答”到“能做”
第二轮专业扩展（题目特有）
  ├── 核心机制再拆一层
  ├── 数据链路与可复现性
  ├── 复杂度、成本与规模感
  ├── 白板公式 / 伪代码 / 实验抓手
  ├── 失败模式与线上诊断
  ├── 可观测性与 Query Slice
  └── Senior / Staff 级追问 + 回答分层
工业落地 6 问
追问链：参考回答
PDF 原始追问链
Gotchas
实战练习
一句话记忆
参考资料
```

## 目录结构

```text
search-engine-interview-100/
├── README.md
├── INDEX.md
├── assets/
│   └── search_engine_interview_100.pdf
├── data/
│   └── questions.json
├── docs/
│   ├── INDEX.md
│   ├── STUDY_PATHS.md
│   ├── questions/
│   │   ├── 01-search-architecture/
│   │   ├── ...
│   │   └── 10-system-design/
│   ├── appendices/
│   └── references/
├── scripts/
│   └── validate_repo.py
└── .github/workflows/validate.yml
```

## 设计原则

1. **一题一文件**：便于搜索、链接、review、PR 和后续扩写。
2. **原 PDF 内容可追踪**：核心短答、深答、追问、Gotcha、记忆点保留并重排。
3. **工程扩展独立标注**：新增的工程分析、当前实现参数和练习明确标为仓库扩展。
4. **优先第一性原理**：公式必须能解释极限情况；系统必须有数量级估算与 SLO。
5. **可维护**：CI 自动检查 100 题数量、ID、内部链接和 JSON manifest。

## 本地验证

```bash
python scripts/validate_repo.py
```

## 内容边界与版权

本仓库是原创技术面试学习材料，组织方式借鉴“问题驱动、递进追问”的通用学习范式，不复制《剑指 Offer》或其他出版物的原文、题解与页面设计。公开面经中的题型只能视为候选人回忆与高频知识点，不代表任何公司的官方题库。

## License

本仓库未预设开源许可证。公开发布前请由仓库所有者根据自己的传播/商业使用需求选择 LICENSE。
