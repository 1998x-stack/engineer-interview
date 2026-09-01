# LLM Pretraining Interview 100

> 面向 **LLM / Foundation Model 预训练算法岗** 的系统化面试手册：100 道核心题，每题一个 Markdown，强调 **Know-What → Know-Why → Know-How → Trade-off → Production**。

[![Questions](https://img.shields.io/badge/questions-100-1f6feb)](#题库导航)
[![A-type](https://img.shields.io/badge/public-interview-patterns-43-2ea44f)](#题源说明)
[![B-type](https://img.shields.io/badge/deep-followups-57-6f42c1)](#题源说明)
[![Docs](https://img.shields.io/badge/docs-MkDocs-526CFE)](./mkdocs.yml)
[![PDF](https://img.shields.io/badge/PDF-93_pages-B31B1B)](./book/LLM-Pretraining-Interview-100.pdf)

## 为什么做这个 Repo

多数 LLM 面试资料停留在“Transformer 八股”。真正的预训练岗位会继续追问：

- **数学**：Attention/RoPE/Scaling/Optimizer 的公式与尺度；
- **Data**：Tokenizer、清洗、去重、mixture、污染、packing；
- **Systems**：TP/PP/DP/CP/EP、ZeRO/FSDP、通信与拓扑；
- **Performance**：显存账本、BF16/FP8、FlashAttention、MFU；
- **MoE / Long Context**：routing、A2A、load balancing、CP；
- **Production**：loss spike、NaN、straggler、checkpoint/recovery；
- **Project Defense**：能否用数字证明自己真的训练过模型。

本项目借鉴《剑指 Offer》的**问题驱动、层层追问、强调解题思路与现场表达**的学习范式；内容、题解与组织均为独立编写，不复制原书文本或版式。

## 📘 PDF 完整版

Repo 同时维护可打印、可离线阅读的完整书稿：

- **[下载 / 在线查看：LLM-Pretraining-Interview-100.pdf](./book/LLM-Pretraining-Interview-100.pdf)**
- A4，93 页；覆盖 100 道题、10 大章节与全部书稿内容。
- PDF 与 `book/llm_pretrain_offer.html` 共同作为版式化书稿；每题更细的工程实验、评分 Rubric、自测与最新补充继续以 `questions/` 为主。
- 可运行 `python scripts/build_pdf.py` 从 HTML 重新生成 PDF。

> 建议：**PDF 用于连续阅读和打印复习，Markdown 用于按题深挖、链接跳转与持续维护。**

## Repo 结构

```text
.
├── README.md
├── questions/                 # 100 题；一题一个 Markdown
│   ├── 01-transformer-architecture/
│   ├── 02-tokenizer-data/
│   ├── 03-objective-optimizer/
│   ├── 04-scaling-law/
│   ├── 05-distributed-training/
│   ├── 06-memory-precision-performance/
│   ├── 07-moe/
│   ├── 08-long-context/
│   ├── 09-stability-debug-eval/
│   └── 10-coding-system-project/
├── cheatsheets/               # 高频公式/显存/并行/Debug 速查
├── study-plan/                # 4 周冲刺与 S 级题复习路线
├── templates/                 # 架构题/系统题/项目题答题模板
├── references/                # 论文、官方文档、公开面经题源说明
├── book/                      # 93 页 PDF、HTML 书稿与结构化 source-of-truth
├── scripts/                   # 索引与一致性校验
├── mkdocs.yml                 # 可直接构建文档站
└── .github/workflows/         # CI：检查 100 题、内部链接与结构
```

## 每道题的统一结构

每个 Markdown 都包含：

1. **面试官为什么问**
2. **30 秒结论**
3. **3 分钟标准回答**
4. **数学/机制深挖**
5. **Know-how：实现与训练系统**
6. **高频追问与回答方向**
7. **常见错误：为什么错**
8. **面试评分 Rubric**
9. **自测/白板练习**
10. **一句话记忆**
11. **题源与可信度**
12. **原始论文/官方文档延伸阅读**

完整总表：[`QUESTIONS.md`](./QUESTIONS.md)

## 题库导航

| 章节 | 范围 | 核心能力 |
|---|---:|---|
| [01. Transformer 与模型架构](./questions/01-transformer-architecture/README.md) | Q001–Q010 | 从公式、张量形状、归一化、位置编码到 7B 架构 sizing。 |
| [02. Tokenizer 与预训练数据](./questions/02-tokenizer-data/README.md) | Q011–Q020 | 从 tokenizer fertility 到清洗、去重、数据 mixture、污染检测和 synthetic data。 |
| [03. 目标函数、Optimizer 与 Training Recipe](./questions/03-objective-optimizer/README.md) | Q021–Q030 | 从 CLM、AdamW、warmup、batch 到 MTP，理解训练 recipe 的优化逻辑。 |
| [04. Scaling Law 与预算设计](./questions/04-scaling-law/README.md) | Q031–Q040 | 把参数、Token、FLOPs、GPU-hours 与能力预测放到同一套预算框架。 |
| [05. 分布式训练](./questions/05-distributed-training/README.md) | Q041–Q050 | 掌握 DP/TP/PP/CP/EP、ZeRO/FSDP、collective 与千卡拓扑设计。 |
| [06. 显存、数值精度与性能](./questions/06-memory-precision-performance/README.md) | Q051–Q060 | 训练显存手算、BF16/FP8、FlashAttention、算术强度和 MFU。 |
| [07. Mixture-of-Experts](./questions/07-moe/README.md) | Q061–Q070 | 从 routing、负载均衡到 expert parallel 与 All-to-All 的系统瓶颈。 |
| [08. 长上下文与高效 Attention](./questions/08-long-context/README.md) | Q071–Q080 | 从 O(S²)、RoPE 外推到 continued pretraining、CP 与真实长上下文评测。 |
| [09. 训练稳定性、Debug 与评测](./questions/09-stability-debug-eval/README.md) | Q081–Q090 | 用可复现、可定位、可回归的故障树处理 loss spike、NaN、straggler 和恢复。 |
| [10. 手撕、系统设计与项目拷打](./questions/10-coding-system-project/README.md) | Q091–Q100 | 把知识变成代码、手算、系统设计和可量化项目证明。 |

## S 级优先题

如果时间有限，先把下面 20 题练到可以连续被追问 10–15 分钟：

- [Q001. 手推 Self-Attention：为什么要除以 √d_k？](./questions/01-transformer-architecture/001.md)
- [Q007. RoPE 为什么能把相对位置信息写进 Attention？](./questions/01-transformer-architecture/007.md)
- [Q014. 从 Common Crawl 到训练 Token：完整预训练数据 Pipeline 怎么设计？](./questions/02-tokenizer-data/014.md)
- [Q017. 预训练数据 Mixture 到底怎么调？](./questions/02-tokenizer-data/017.md)
- [Q019. Packing 与 Padding 有什么区别？为什么 Packing 不是简单拼接？](./questions/02-tokenizer-data/019.md)
- [Q023. AdamW 为什么长期是 LLM 预训练默认优化器？](./questions/03-objective-optimizer/023.md)
- [Q027. Global Batch、Micro Batch、Gradient Accumulation 如何换算？](./questions/03-objective-optimizer/027.md)
- [Q031. 什么是 Scaling Law？预训练团队为什么需要它？](./questions/04-scaling-law/031.md)
- [Q034. 为什么训练 FLOPs 常粗略写成 6ND？](./questions/04-scaling-law/034.md)
- [Q035. 给定固定 GPU-hours，如何决定模型大小和 Token 数？](./questions/04-scaling-law/035.md)
- [Q042. Tensor Parallel 如何切 Transformer？](./questions/05-distributed-training/042.md)
- [Q046. ZeRO-1、ZeRO-2、ZeRO-3 分别 Shard 什么？](./questions/05-distributed-training/046.md)
- [Q048. Sequence Parallel 与 Context Parallel 有什么区别？](./questions/05-distributed-training/048.md)
- [Q050. 给你 1024 张 GPU，TP/PP/DP/CP/EP 怎么设计？](./questions/05-distributed-training/050.md)
- [Q052. Adam 混合精度训练每参数到底多少 Bytes？](./questions/06-memory-precision-performance/052.md)
- [Q058. FlashAttention 为什么快？它是不是近似 Attention？](./questions/06-memory-precision-performance/058.md)
- [Q063. 为什么 MoE 会出现 Expert Collapse / Hot Expert？](./questions/07-moe/063.md)
- [Q065. DeepSeek-V3 的 Auxiliary-Loss-Free Load Balancing 为什么重要？](./questions/07-moe/065.md)
- [Q081. 100B 模型训练到 42k Step 突然 Loss Spike，怎么排查？](./questions/09-stability-debug-eval/081.md)
- [Q100. 你在预训练项目中真正解决的最难问题是什么？](./questions/10-coding-system-project/100.md)

## 题源说明

- **A 类高频真题型：43 道**。来自公开候选人面经中出现或高度近似的题型，题干统一做了规范化重写；公开面经不是公司官方试卷。
- **B 类等价深挖题：57 道**。根据预训练岗位能力模型、主流技术报告和高频追问构建，不宣称来自某家公司逐字原题。
- 技术事实优先参考原始论文、官方技术报告与 NVIDIA Megatron Core 官方文档。
- 当前版本技术校准日期：**2026-09-01**。

详见 [`references/README.md`](./references/README.md)。

## 推荐学习方式

### 第一遍：建立知识地图
只读每题的 **30 秒结论 + 一句话记忆**，建立 100 题全局连接。

### 第二遍：练“3 分钟主答”
闭卷回答后再对照 Markdown。任何无法用自己的语言解释的公式，都视为没有掌握。

### 第三遍：只练追问
让同伴/模型连续问 Why / How / Trade-off / Production。目标是从算法自然切到训练系统。

### 第四遍：映射到真实项目
每个 S 级题至少准备一个真实数字：参数量、Tokens、GPU、seq len、batch、LR、MFU、显存、吞吐或事故指标。

完整计划：[`study-plan/4-week-plan.md`](./study-plan/4-week-plan.md)。

## 构建文档站

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## 内容校验

```bash
python scripts/validate_repo.py
```

CI 会检查：恰好 100 个问题文件、Q001–Q100 连续、章节范围正确、相对链接可解析、每题核心章节完整。

## 版权与贡献

本项目是独立编写的面试学习资料。对《剑指 Offer》的参考仅限学习组织范式。引用的论文、官方文档和公开面经归原作者/平台所有。

欢迎通过 Issue/PR 补充：更好的数学推导、真实训练事故复盘、公开可验证面经来源、勘误和新的系统实现差异。见 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。
