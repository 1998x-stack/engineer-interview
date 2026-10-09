# Content Quality & QA

## v1.1.0 质量门槛

本页记录 Repo 内容层面的自动检查，避免“文件很多但内容空心化”。

### Question-level requirements

100 道题必须全部存在且一题一 Markdown；每题至少包含：

- 面试官意图、Know-Why、Know-How；
- Production Deep Dive；
- Failure Modes / Trade-offs；
- 最小 Eval；
- 90 秒 / 5 分钟回答；
- 来源与关联题；
- v1.1 专业深挖：Design Review、Fault Injection、Ablation、Metrics、Debugging、Senior/Staff signal。

### v1.1 内容去模板化检查

第三轮增强为每题分别定义：

1. 唯一的核心工程判断；
2. 唯一的故障注入场景；
3. 唯一的可证伪实验；
4. 唯一的 Senior/Staff 级判断信号。

这些字段由内容审查脚本抽取后检查重复，避免 100 个文件只是替换标题的模板文章。

### Source fidelity

每题明确分层：

- **第 1–13 节**：PDF 原稿为基础的整理与教学扩写；
- **第 14 节**：Repo v1.1 工程研究层；
- **B/W/R References**：分别表示用户提供资料、PDF 已列公开来源、Repo 后续研究来源。

新增外部资料不得被描述为 PDF 原稿证据。

## 本地验证

```bash
python scripts/validate_repo.py
```

检查项包括：100 题完整性、题号唯一性、核心章节、v1.1 深挖章节、来源分层 banner、相对 Markdown 链接和最低内容深度。

MkDocs 的完整构建需要安装 `requirements-docs.txt`；在没有依赖安装条件时，仍可检查 `mkdocs.yml` 中所有 Markdown nav 目标是否存在。
