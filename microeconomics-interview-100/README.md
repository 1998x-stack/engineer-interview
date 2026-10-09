# Microeconomics Interview 100 · 微观经济学面试 100 题

> 从“会背定义”训练到“能在陌生 Case 中建模、推导、追问和构造反事实”。

本仓库是《微观经济学面试 100 题：剑指 Offer 式训练手册》的工程化版本。**100 道题，每题一个 Markdown**，并在 PDF 基础上扩充了模型假设、白板推导、识别视角、评分标准、关联题与复习机制。

## 核心特性

- 100 个独立题目 Markdown，稳定编号 Q001-Q100；
- 10 个模块，从供需到综合 economic consulting case；
- 每题包含：30 秒回答、3 分钟展开、公式、假设、识别、追问、错误、迁移、rubric；
- `Core 20` 高频主干，用于快速建立微观面试骨架；
- 原 PDF 收录于 `book/`，仓库内容可脱离 PDF 独立阅读；
- 自带机器可读 `data/questions.json` 与完整性校验脚本；
- 可直接用 MkDocs 构建成文档站点。

## 目录

| Chapter | 模块 | 题号 | 入口 |
|---:|---|---|---|
| 01 | 供给、需求与弹性 | Q001-Q010 | [进入](docs/questions/01-supply-demand-elasticity/index.md) |
| 02 | 消费者理论 | Q011-Q020 | [进入](docs/questions/02-consumer-theory/index.md) |
| 03 | 生产、成本与竞争厂商 | Q021-Q030 | [进入](docs/questions/03-production-costs-competition/index.md) |
| 04 | 垄断与定价 | Q031-Q040 | [进入](docs/questions/04-monopoly-pricing/index.md) |
| 05 | 寡头与博弈论 | Q041-Q052 | [进入](docs/questions/05-oligopoly-game-theory/index.md) |
| 06 | 福利、一般均衡与政府干预 | Q053-Q062 | [进入](docs/questions/06-welfare-general-equilibrium-policy/index.md) |
| 07 | 风险、信息不对称与契约 | Q063-Q072 | [进入](docs/questions/07-risk-information-contracts/index.md) |
| 08 | 产业组织、反垄断与经济咨询 | Q073-Q084 | [进入](docs/questions/08-io-antitrust-consulting/index.md) |
| 09 | 劳动、平台、行为与现代微观 | Q085-Q092 | [进入](docs/questions/09-labor-platform-behavioral/index.md) |
| 10 | 综合 Case 与因果识别 | Q093-Q100 | [进入](docs/questions/10-integrated-cases-identification/index.md) |

## 推荐使用方式

1. 先读 [训练方法](docs/guide/how-to-use.md) 与 [面试评分标准](docs/guide/interview-rubric.md)。
2. 第一遍每题只看题目，强制 30 秒输出。
3. 第二遍白板写关键公式，限制 3 分钟。
4. 第三遍只做追问和迁移题。
5. 用 [7 天冲刺计划](docs/training/7-day-sprint.md) 或 [长期路线](docs/training/mastery-roadmap.md) 复习。

## Core 20

Q001, Q007, Q009, Q015, Q016, Q022, Q023, Q031, Q032, Q040, Q041, Q045, Q046, Q050, Q054, Q066, Q073, Q081, Q093, Q100。

## PDF

- [微观经济学面试 100 题 PDF](book/microeconomics-interview-100.pdf)

## 来源边界

题目按“官方 case 衍生 / 公开面经高频题型 / 经典高仿真面试题”等标注。官方材料用于校准面试风格；匿名公开面经只作为“题型出现过”的线索。**未核验逐字来源的题目不会冒充逐字真题。** 详见 [来源与方法](docs/reference/sources-and-methodology.md)。

## 发布到 GitHub

参见 [发布指南](docs/guide/publishing.md)。

## 本地检查

```bash
python scripts/verify_repo.py
```

## 文档站点

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

> 本仓库参考“剑指 Offer”的训练思想：题型分层、逐题突破、追问与复盘；不复制其受版权保护的原文或版式。

## v2.0 专业深化

100 道题均新增 **Advanced Deep Dive**，每题在原有 30 秒/3 分钟/公式/追问/迁移题基础上继续加入：

- 研究生级理论定位与严格推导路线；
- 图形 / 几何 / 状态空间直觉；
- comparative statics 与可证伪预测；
- Evidence Matrix：机制、方向、因果、反事实、稳健性；
- 高阶追问：动态、异质性、一般均衡、信息结构；
- 研究级模型边界与换模型条件；
- 题目专属延伸阅读路径；
- Mastery Gate，要求从“会背”升级到“会迁移”。

新增跨题参考：

- [`advanced-methods.md`](docs/reference/advanced-methods.md)
- [`econometrics-for-micro-interviews.md`](docs/reference/econometrics-for-micro-interviews.md)
- [`diagram-playbook.md`](docs/reference/diagram-playbook.md)
- [`editorial-standard.md`](docs/guide/editorial-standard.md)

