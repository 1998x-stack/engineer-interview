# Macroeconomics Interview 100 · 宏观经济学面试 100 题

> 一套面向经济学复试、保研/夏令营、研究生面试与宏观岗位面试的 **GitHub-native 题库与训练系统**。

![Questions](https://img.shields.io/badge/questions-100-blue)
![Modules](https://img.shields.io/badge/modules-10-success)
![Edition](https://img.shields.io/badge/edition-2026-informational)
![Content](https://img.shields.io/badge/content-Chinese%20%2B%20English-lightgrey)

## 为什么不是一个 78 页 PDF 的简单拆分？

PDF 适合线性阅读，面试训练更需要**随机抽题、交叉链接、追问、版本管理和来源追溯**。本仓库把 PDF 的全部核心内容拆成 100 个独立 Markdown，并为每题增加：

- YAML 元数据与 PDF 页码追溯；
- 90 秒标准回答；
- 核心公式与结构；
- 更深入的专业扩展；
- 模型假设、边界与可证伪思维；
- 教授追问的答题路径；
- 常见错误与迁移训练；
- 10 分制面试 Rubric；
- 跨章节关联题；
- 官方资料/数据来源。

## 目录

- **PART 01** [国民收入核算与宏观数据](docs/01-national-accounts/README.md) — Q001-Q010
- **PART 02** [凯恩斯交叉与乘数](docs/02-keynesian-cross/README.md) — Q011-Q020
- **PART 03** [IS-LM 与政策组合](docs/03-is-lm/README.md) — Q021-Q030
- **PART 04** [AD-AS、通胀、失业与周期](docs/04-ad-as/README.md) — Q031-Q040
- **PART 05** [开放经济与汇率](docs/05-open-economy/README.md) — Q041-Q050
- **PART 06** [长期增长](docs/06-growth/README.md) — Q051-Q060
- **PART 07** [现代宏观与预期](docs/07-modern-macro/README.md) — Q061-Q070
- **PART 08** [财政、债务、货币与金融传导](docs/08-fiscal-monetary-finance/README.md) — Q071-Q080
- **PART 09** [2026 中国宏观热点](docs/09-china-2026/README.md) — Q081-Q090
- **PART 10** [研究能力与压力面试](docs/10-research-interview/README.md) — Q091-Q100

## 快速开始

```bash
git clone <your-repository-url>
cd macroeconomics-interview-100
python scripts/validate_repo.py
python scripts/random_mock_interview.py --count 10 --seed 42
```

本地预览文档站：

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 关键入口

- [在线文档首页（仓库内）](docs/index.md)
- [6 层回答法](docs/00-guide/answer-framework.md)
- [模型选择树](docs/appendices/model-selection-tree.md)
- [高频公式表](docs/appendices/formula-sheet.md)
- [30 天刷题计划](docs/appendices/30-day-plan.md)
- [原始 PDF](book/macroeconomics-interview-100-2026.pdf)

## 内容完整性

`book/pdf-text-extracted.txt` 保存 PDF 的完整文本抽取版本；`data/questions.json` / `questions.csv` 保存结构化题库。CI 中的 `scripts/validate_repo.py` 会检查 100 道题是否齐全、Front Matter 是否完整、PDF 溯源页码是否存在、内部链接是否断裂。

## 真题与版权说明

公开渠道通常不会合法公开完整复试题库。仓库中的“真题母题”主要来自官方考纲高频考点、公开可核验的面试机制与经典复试题型的原创重构；热点题使用官方统计与 IMF 等资料。**不声称 100 题均为某校逐字原题，也不包含泄露题库。**

本项目借鉴高质量面试刷题书的任务化组织思想，但不复制《剑指 Offer》或其他第三方作品的原文、题解和版式。

## 贡献

参见 [CONTRIBUTING.md](CONTRIBUTING.md)。如果修正 2026 数据，请同时更新来源、日期与受影响题目。

## License Notice

当前仓库未主动授予开源内容许可；详见 [LICENSE-NOTICE.md](LICENSE-NOTICE.md)。代码与内容的后续授权方式应由仓库维护者明确决定。
