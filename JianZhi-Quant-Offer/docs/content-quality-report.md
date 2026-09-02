# V2 Professional Expanded：内容质量报告

本页记录仓库 Markdown 教材源相对于附带 PDF 的扩展范围、结构要求和自动 QA 结果。它不是对题目“真实公司出处”的额外背书；来源口径仍以每题 front matter 与 `references/official-sources.md` 为准。

## 当前规模

- 独立题目：**100 / 100**
- 模块：**10**（A–J）
- 每题统一一级结构：**14 个章节**
- 当前题目正文平均字符数：约 **5.3k**
- 最短题目：约 **4.8k** 字符
- 最长题目：约 **6.1k** 字符
- 原 Professional Edition PDF：保留于 `book/`

## V2 的核心升级

PDF 中已有的题干、基础答案、原始推导、追问、高频错误与面试表达被保留为内容基线。在此基础上，Markdown 增加：

1. **Formalization**：明确变量、状态、信息集、estimand、目标函数或系统不变量；
2. **模块化专业检查表**：不同领域使用不同的 assumption checklist；
3. **第二验证视角**：解析解之外，引入 simulation、bootstrap、walk-forward、replay、numerical convergence 等交叉验证方式；
4. **高级面试层**：从“会算”推进到“会解释、会证伪、会迁移”；
5. **真实量化/工程语境**：PIT、OOS、cost、queue、latency、calibration、model risk、research-to-production；
6. **Failure modes**：解释错误为什么发生，而不只列一个“错误答案”；
7. **追问 + 回答方向**：所有原始追问都给出继续回答的核心路径；
8. **30 秒 / 3 分钟双档表达**：训练真实面试的信息压缩能力；
9. **交叉链接与延伸阅读**：将 100 题组织为知识图，而不是 100 个孤立页面。

## 10 个模块的专业检查重点

| 模块 | Markdown V2 重点检查 |
|---|---|
| A 概率 | 原子样本空间、独立性、conditioning、stopping state、exact/simulation cross-check |
| B 统计 | estimand、finite vs asymptotic、dependence、multiple testing、robust inference |
| C 随机过程 | filtration、Markov/martingale 区分、SDE 条件、optional stopping、离散化 |
| D 时间序列 | timestamp、stationarity、serial dependence、walk-forward、structural break |
| E Financial ML | label availability、train-only preprocessing、baseline/ablation、calibration、online parity |
| F 微观结构 | L1/L2/L3、venue rule、event time、queue/fill、latency/replay |
| G 回测研究 | PIT、researcher degrees of freedom、cost/execution、untouched OOS、lineage |
| H 优化 | objective/constraints、estimation error、conditioning、turnover/cost、sensitivity |
| I 衍生品 | contract convention、no-arbitrage、real vs risk-neutral、model completeness、numerical checks |
| J 系统 | state/invariants、ordering、complexity/cache、idempotency/recovery、golden replay |

## 自动 QA

运行：

```bash
python scripts/validate_repo.py
```

验证器当前检查：

- 100 个 `q001`–`q100` 文件齐全且连续；
- 每题包含 V2 front matter；
- 14 个必备一级章节齐全；
- 内容密度达到仓库下限；
- 不存在非法控制字符；
- 本地 Markdown 链接存在；
- `questions.json` 为 100 行结构化记录；
- PDF 存在；
- MkDocs nav 指向有效文件。

自动检查不能替代事实核验。涉及公司题型来源时，应继续以官方链接为最高优先级；涉及数学/统计结论时，应以教材、论文或可复现实验继续校验。

## 维护原则

内容质量优先级固定为：

> **correctness > provenance > assumptions > falsifiability > clarity > completeness > style**

扩写不等于堆字。新增一段内容至少应回答以下问题之一：

- 为什么这个结论成立？
- 它依赖什么条件？
- 什么反例会让它失败？
- 怎么用另一种方法验证？
- 在真实量化数据/系统中对应什么问题？
- 面试官继续追问时下一层是什么？

如果一段文字无法回答其中任何一个问题，通常不应加入正文。
