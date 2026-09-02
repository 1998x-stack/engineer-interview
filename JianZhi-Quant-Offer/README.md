# 剑指 Quant Offer - 金融量化算法岗 100 题

> Quantitative Research · Financial ML · HFT Algorithms · Derivatives

一套面向 **Quantitative Research / Financial ML / Algorithm Developer / Systematic Research / Derivatives Quant** 的问题驱动型面试手册。仓库保留原始专业版 PDF，并把 100 道题拆成 100 个独立 Markdown；Markdown 是可维护、可扩展的“教材源”，内容比 PDF 更细。

## 为什么这样组织

这不是“背答案题库”。每道题采用统一的《剑指 Offer》式结构：

**题目 → 考察目标 → 标准解 → 详细推导 → 核心原理 → 假设/边界 → 量化语境 → 进一步深化 → 追问树 → 高频错误 → 面试表达 → 自测 → 关联题目**。

官方题型校准显示，当前主流 Quant Research/Algorithm 岗共同强调概率统计、开放数据分析、编程算法、机器学习/时间序列、研究严谨性与 research-to-production。详见 [官方题型依据](references/official-sources.md)。

## 目录

| 模块 | 题号 | 主题 | 优先级 |
|---|---:|---|---|
| A | 001-010 | 概率论、条件概率与期望 | ★★★★★ |
| B | 011-020 | 数理统计与统计推断 | ★★★★★ |
| C | 021-030 | 随机过程 | ★★★★☆ |
| D | 031-040 | 时间序列与计量 | ★★★★★ |
| E | 041-050 | 机器学习与 Financial ML | ★★★★★ |
| F | 051-060 | 市场微观结构 | ★★★★☆ |
| G | 061-070 | 数据、回测与研究方法论 | ★★★★★ |
| H | 071-080 | 组合、风险与优化 | ★★★★☆ |
| I | 081-090 | 衍生品与定价 | ★★★☆☆~★★★★★ |
| J | 091-100 | Coding、算法与量化系统 | ★★★★★ |

完整索引：[100 题总索引](docs/100-question-index.md) · [PDF→Repo 内容映射](docs/pdf-content-map.md) · [Repo 架构](docs/repository-architecture.md) · [学习路线](docs/learning-path.md) · [公司能力矩阵](docs/company-skill-matrix.md) · [难度索引](docs/difficulty-index.md)

## PDF

- [《剑指 Quant Offer：金融量化算法岗面试 100 题》Professional Edition](book/剑指QuantOffer_金融量化算法岗100题_专业版.pdf)

## 推荐学习路线

### 通用 QR / Financial ML

`A 概率 → B 统计 → G 研究方法 → D 时序 → E ML → J Coding → F 微观结构 → H 优化 → C 随机过程 → I 衍生品`

### HFT / Algorithm Developer

优先 `A + F + J`，再补 `B + D + G + E`。

### Options / Derivatives Quant

优先 `A + C + I`，第二层补 `B + D + H + J`。

## 本地阅读与 GitHub Pages

仓库包含 `mkdocs.yml`。安装：

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

构建：

```bash
mkdocs build --strict
```

## Repository QA

```bash
python scripts/validate_repo.py
```

验证器会检查：100 个题目文件是否齐全、编号是否唯一、标准章节是否缺失、内部链接是否存在、原 PDF 是否包含在仓库。

## 内容口径

- 只有公司官方 guide/mock interview 明确出现的题，才标为“官方公开题型”。
- 其余为依据官方面试范围和岗位能力要求重构的高可信题型，不冒充未公开内部真题。
- 本仓库用于面试学习与技术研究，不构成投资或交易建议。

## 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md) 与 [STYLE_GUIDE.md](STYLE_GUIDE.md)。新增题目时，优先补充“为什么”“边界条件”“失败模式”和可验证的参考资料，而不是只增加答案长度。


## V2.0：专业扩展版

当前仓库已将 100 道题升级为统一的 **14 段教材模板**：题目、考点、30 秒答案、Formalization、详细推导、Why、量化语境、失效场景、带回答方向的追问树、高频错误、3 分钟回答、自测、关联题、延伸阅读/来源边界。

与 PDF 相比，Markdown 版本的定位是“可持续演化的源教材”：它明确区分 PDF 原始内容与 V2 扩展内容，并强化 research-to-production、PIT、OOS、simulation、replay 与 model-risk 视角。

第二轮专业化已经进一步去除跨题通用模板：10 个模块分别使用自己的建模假设、验证方法、failure-mode 与落地检查框架。目前 100 个题目 Markdown 平均约 5.3k 字符，重点不是字数本身，而是让每题形成 **formalize → derive → cross-check → falsify → implement → communicate** 的完整训练闭环。详见 [内容质量报告](docs/content-quality-report.md) 与 [题目写作规范](docs/question-writing-standard.md)。

### 推荐使用方式

- **系统学习**：按章节 README → 10 道题 → 本章 checklist。
- **面试冲刺**：只看每题 `30 秒版本` + `追问树` + `高频错误`。
- **深度研究**：重点阅读 `Formalization`、`Why`、`量化语境`、`边界条件`。
- **Mock Interview**：面试官只读题目/追问，被面试者用 30 秒与 3 分钟两档回答。
