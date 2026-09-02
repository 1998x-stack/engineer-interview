# Repository Architecture

仓库按 **内容层 → 结构化数据层 → 导航层 → 发布层 → 质量层** 组织。目标是让“100 题技术书”既适合人类阅读，也适合后续自动生成网站、Anki、Mock Interview、PDF 和数据 API。

## 1. 目录结构

```text
JianZhi-Quant-Offer/
├── README.md
├── book/                         # 冻结版 PDF
├── questions/                    # 10 章 / 100 个独立题目
│   ├── 01-probability-expectation/
│   └── ...
├── data/
│   └── questions.json            # 结构化元数据 / PDF 转录层
├── docs/                          # 知识地图、学习路径、索引
├── references/                    # 官方题型能力依据
├── scripts/                       # QA / inspection
├── mkdocs.yml                     # 文档网站
└── .github/workflows/             # CI / Pages
```

## 2. 内容层：一题一个 Markdown

稳定标识采用 `qXXX`。标题/文件名可优化，但 ID 不应随意变化。

V2 每题固定 14 段，详见 [Question Writing Standard](question-writing-standard.md)。这样做的收益：

- 单题 Git diff 清晰；
- issue/PR 可精确引用题号；
- 页面级搜索和 SEO 更友好；
- 可按题目元数据自动抽取 flashcards / interview packets；
- 后续可以只重建变动题，而不是整本书。

## 3. 结构化数据层

`data/questions.json` 保存 PDF/初版题库中的结构化字段：

```text
id / title / difficulty / tags
answer / derivation
followups / pitfalls / interview
chapter / markdown_path
```

### Source of truth 策略

- PDF 是**冻结出版物**；
- `questions.json` 是 PDF 题目基础内容的结构化转录；
- `questions/*.md` 是 **V2 可维护教材源**，允许在明确标注边界的前提下加入专业扩展。

因此，扩展 Markdown 时不能悄悄改写 PDF 的题目来源口径。

## 4. 导航层

不同导航只是对同一内容的不同投影：

- [100 题总索引](100-question-index.md)：按题号；
- [Knowledge Map](knowledge-map.md)：按知识依赖；
- [Difficulty Index](difficulty-index.md)：按难度；
- [Company Skill Matrix](company-skill-matrix.md)：按公开能力范围；
- [Learning Path](learning-path.md)：按学习时间/岗位目标。

导航层不应复制单题正文，而应回答“我下一步看什么”。

## 5. 发布层

MkDocs Material 用于把 Markdown 发布成在线教材。MathJax 支持公式，GitHub Actions 可自动部署 Pages。

理想发布流程：

```text
edit markdown
  ↓
validate_repo.py
  ↓
mkdocs build --strict
  ↓
GitHub Actions
  ↓
GitHub Pages
```

## 6. 质量层

`validate_repo.py` 当前检查：

- 100 个题目文件齐全；
- q001–q100 连续；
- V2 14 段结构完整；
- 每题达到最低内容密度；
- Markdown 相对链接存在；
- 无 ASCII 控制字符；
- 原 PDF 存在；
- `questions.json` 100 条可解析；
- MkDocs nav 目标存在。

### 为什么内容密度也要检查

只验证“文件存在”会允许批量模板生成大量空洞页面。V2 因此增加最低字符量和结构校验，但这仍不能替代人工 technical review。

## 7. 推荐的下一阶段架构

可以继续增加：

```text
examples/                # Python/C++/SQL 数值实验
tests/                   # 示例代码测试
assets/figures/          # LOB、vol surface、efficient frontier 等
mock-interviews/         # 30/60/90 分钟题单
anki/                    # 自动生成卡片
company-guides/          # 只基于官方公开能力要求的复习指南
benchmarks/              # 自测评分与进度数据
```

## 8. 贡献的架构原则

任何新内容优先保持：

**稳定 ID、清晰 provenance、可验证链接、可自动 QA、PDF 内容与扩展内容边界明确。**
