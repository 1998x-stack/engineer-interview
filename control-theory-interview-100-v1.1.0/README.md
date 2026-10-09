# Control Theory Interview 100 / 控制论原理面试 100 题

> 从经典控制到现代控制的系统面试宝典：**问题驱动 · 数学推导 · 工程直觉 · 高频追问 · 实机 Gotchas**

[![Questions](https://img.shields.io/badge/questions-100-16324F)](BOOK_INDEX.md)
[![PDF](https://img.shields.io/badge/PDF-101_pages-1D6F8A)](pdf/control-theory-interview-100-2026.pdf)
[![CI](https://img.shields.io/badge/CI-content_validation-success)](.github/workflows/validate.yml)

## 项目定位

面向控制算法、机器人、自动驾驶、无人机、工业控制、电机控制、航空航天与嵌入式控制岗位。仓库以随附的 **101 页专业版 PDF** 为内容基线，并把其中 100 道题拆成 **100 个独立 Markdown**。

每题完整保留 PDF 的：

- 标准回答；
- 公式与推导；
- 工程直觉；
- 常见误区 / Gotcha；
- 高频追问；
- 30 秒口述版。

在此基础上，GitHub **v1.1 专家扩展版**进一步新增：题目专属专家补充、推导路线与适用条件、可计算小例子、工程验证矩阵、**300 个高频追问的实质详答**、反例/失效条件、30 秒/2 分钟/5 分钟三档答题深度以及自测题。原有 PDF 内容仍逐项完整保留。

> **重要边界：** 每题用明确标题区分“PDF 原始内容”和“仓库增强”，不会把外部扩展悄悄改写成 PDF 原文。详见 [来源与内容边界](docs/source-notes.md)。

## 快速入口

- 📚 [100 题总索引](BOOK_INDEX.md)
- 📖 [前言与使用说明](docs/preface.md)
- 📄 [专业版 PDF](pdf/control-theory-interview-100-2026.pdf)
- 🧠 [知识图谱](docs/knowledge-map.md)
- 🧮 [核心公式速查](docs/formula-cheatsheet.md)
- 🗓️ [7 天冲刺路线](docs/seven-day-plan.md)
- 🔗 [高频追问链](docs/followup-chains.md)
- 🧪 [Python 最小实验](examples/python/)
- 🛠️ [实机调试 Checklist](docs/engineering-debug-checklist.md)
- ✅ [v1.1 内容质量报告](docs/content-quality-report.md)
- 🧾 [结语](docs/closing.md)

## 目录

| 章 | 主题 | 题号 | 核心能力 |
|---:|---|---:|---|
| 1 | 控制论基础与建模 | Q001–Q010 | feedback / modeling / poles & zeros / uncertainty |
| 2 | 时域响应与二阶系统 | Q011–Q020 | time-domain / damping / steady-state error |
| 3 | PID 与工程实现 | Q021–Q030 | PID / anti-windup / cascade / feedforward |
| 4 | 稳定性与根轨迹 | Q031–Q040 | Routh / root locus / lead-lag / internal stability |
| 5 | 频率响应与鲁棒直觉 | Q041–Q050 | Bode / Nyquist / margins / sensitivity |
| 6 | 状态空间与现代线性控制 | Q051–Q060 | state-space / MIMO / linearization / state feedback |
| 7 | 可控可观、观测器与 Kalman | Q061–Q070 | controllability / observability / estimator |
| 8 | 最优、MPC、鲁棒与自适应 | Q071–Q080 | LQR / MPC / H∞ / adaptive |
| 9 | 离散控制与数字实现 | Q081–Q090 | sampling / ZOH / z-plane / real-time implementation |
| 10 | 非线性与系统级工程面试 | Q091–Q100 | Lyapunov / nonlinear design / debugging |

## Repository Layout

```text
control-theory-interview-100/
├── README.md
├── BOOK_INDEX.md
├── questions/                 # 10 章 × 每题一个 Markdown
│   ├── 01-foundations-modeling/
│   │   ├── README.md
│   │   ├── q001.md
│   │   └── ...
│   └── 10-nonlinear-system-engineering/
├── data/questions.json        # 100 题结构化源数据 + PDF 页码
├── data/question_enrichment_v2.json # 100 题专家扩展 + 300 追问详答
├── pdf/                       # 101 页专业版 PDF
├── assets/figures/            # PDF 原始自制图示
├── docs/                      # 公式、路线、知识图谱、调试清单等
├── examples/python/           # 10 个章节级最小实验
├── scripts/validate_repo.py   # 内容一致性 + 链接校验
├── book/SUMMARY.md            # GitBook/mdBook 风格导航
└── .github/                   # CI 与 issue templates
```

## 每题模板

```text
Qxxx
├── 面试官为什么问
├── PDF 原始内容（完整保留）
│   ├── 标准回答
│   ├── 公式与推导
│   ├── 工程直觉
│   ├── Gotcha
│   ├── 高频追问
│   └── 30 秒口述版
└── 仓库增强
    ├── 深度展开与工程场景
    ├── 专家版扩展 v2
    │   ├── 核心边界与题目专属专家补充
    │   ├── 推导路线与适用条件
    │   ├── 可计算小例子
    │   ├── 工程验证矩阵
    │   ├── 高频追问详答
    │   ├── 反例与失效条件
    │   ├── 30 秒 / 2 分钟 / 5 分钟回答深度
    │   └── 自测题
    ├── 白板推导 Checklist
    ├── 实验建议
    ├── 面试评分点
    ├── 相关题目
    └── 参考资料
```

## 本地校验

```bash
python scripts/validate_repo.py
```

校验器会检查：

1. 恰好 100 个问题文件；
2. 每题完整包含 PDF 的核心字段；
3. 每题明确区分 PDF 与扩展内容；
4. 内部 Markdown 链接不存在断链；
5. PDF 资源存在；
6. 100 题均包含“专家版扩展 v2”和“高频追问详答”；
7. 不允许遗留模板化追问占位答案；
8. 每题正文达到最低专业内容长度，并检查异常控制字符。

## Python 实验

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-examples.txt
python examples/python/02_second_order_response.py
```

## 内容来源与参考

题库结构的公开参考主干包括 MIT 16.06、Stanford EE363、University of Michigan CTMS、UC Berkeley nonlinear systems、Stanford EE364B MPC 与 MathWorks PID anti-windup。完整列表见 [references](docs/references.md)。

题库不声称某一道题属于某家公司某一场未经公开验证的面试原题。

## License

- Markdown/图文内容：见 `LICENSE-CONTENT`（CC BY 4.0）。
- 示例代码与脚本：见 `LICENSE-CODE`（MIT）。

## Contributing

欢迎修正公式、补工程案例、增加可复现实验或补充公开来源。提交前请运行 `python scripts/validate_repo.py`。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。
