# Computer Organization Interview 100

> 计算机组成原理 / 计算机体系结构面试题库：100 题，一题一个 Markdown，覆盖数据表示、ISA、流水线、乱序执行、Cache、MMU/TLB、多核一致性、DMA/互连、存储与性能分析。

## v2 深度增强版

- 100/100 题已升级为 **第一性原理 → 机制 → 定量 → 边界 → 工程验证 → 架构差异 → 追问树** 的完整结构。
- 每题都保留 PDF 原始内容，并明确标记 GitHub v2 新增部分，避免来源混淆。
- 每题加入 30 秒 / 2 分钟 / 5 分钟三档回答，以及 PMU/微基准验证思路。
- 各章 README 增加能力阶梯、关键指标和架构图。

## v2 深度增强版

- 100/100 题已升级为 **第一性原理 → 机制 → 定量 → 边界 → 工程验证 → 架构差异 → 追问树** 的完整结构。
- 每题都保留 PDF 原始内容，并明确标记 GitHub v2 新增部分，避免来源混淆。
- 每题加入 30 秒 / 2 分钟 / 5 分钟三档回答，以及 PMU/微基准验证思路。
- 各章 README 增加能力阶梯、关键指标和架构图。

## v2 深度增强版

- 100/100 题已升级为 **第一性原理 → 机制 → 定量 → 边界 → 工程验证 → 架构差异 → 追问树** 的完整结构。
- 每题都保留 PDF 原始内容，并明确标记 GitHub v2 新增部分，避免来源混淆。
- 每题加入 30 秒 / 2 分钟 / 5 分钟三档回答，以及 PMU/微基准验证思路。
- 各章 README 增加能力阶梯、关键指标和架构图。

## 特点

- **100 道题 = 100 个 Markdown**，适合 GitHub Review、PR 式维护和按题学习。
- **来源可追溯**：每题标记原 PDF 页码，并链接仓库内 PDF。
- **内容分层**：PDF 核心要点与 GitHub 增强内容明确区分。
- **面试导向**：30–60 秒标准回答 + 深挖机制 + 高阶追问 + 工程连接。
- **现代体系结构**：不止五级流水线，进一步覆盖 OoO、ROB、VIPT、MESI、RVWMO、DMA/Cache coherence 等。
- **可发布为文档站**：内置 MkDocs Material 与 GitHub Pages workflow。

## Repo 结构

```text
.
├── README.md
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── 01-architecture-data/      # Q001-Q010
│   ├── 02-arithmetic-alu/         # Q011-Q020
│   ├── 03-isa-abi/                # Q021-Q030
│   ├── 04-datapath-control/       # Q031-Q040
│   ├── 05-pipeline-ooo/           # Q041-Q050
│   ├── 06-cache-memory/           # Q051-Q060
│   ├── 07-mmu-tlb/                # Q061-Q070
│   ├── 08-coherence-memory-model/ # Q071-Q080
│   ├── 09-io-dma-interconnect/    # Q081-Q090
│   ├── 10-storage-boot-performance/# Q091-Q100
│   ├── appendices/
│   └── study-plans/
├── docs/assets/pdf/            # 原始 PDF，可被 MkDocs/GitHub 直接访问
├── assets/source/             # PDF 结构化抽取索引
├── scripts/
└── .github/workflows/
```

## 推荐学习方式

第一次只读“PDF 核心结论 + 30–60 秒标准回答”；第二次补“深入扩展”；第三次闭卷回答“高阶追问”；最后使用 Q100 把前端、执行、Cache/TLB、DRAM、多核与 I/O 串成性能分析框架。

## 构建文档站

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 内容来源与扩展说明

原始题库 PDF 位于 `assets/pdf/`。`assets/source/questions-from-pdf.json` 是从 PDF 抽取的结构化索引。每个题目 Markdown 中：

- `PDF 核心结论 / PDF 深度解析 / PDF 易错点`：依据原 PDF 对应页整理；
- `深入扩展 / 工程连接 / 高阶追问`：GitHub 版新增内容；
- 具体 ISA 和系统细节优先参考 Intel、Arm、RISC-V 官方资料。

## 版权与使用

本仓库内容为原创教育资料整理与扩展，不复制《剑指 Offer》或其他书籍的原文、题目、插图和版式。发布到公开 GitHub 前，请仓库所有者根据自己的分发意图选择最终许可证；本交付包默认未授予额外再分发许可。
