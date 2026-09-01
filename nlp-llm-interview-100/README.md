# NLP / LLM Interview 100 — Professional Handbook v2.0

> 面向 **NLP、搜索 / RAG、Foundation Model 训练、后训练、数据工程与 AI Infra** 算法岗位的系统化面试手册。

本仓库以《NLP / LLM 算法岗面试 100 题 — 2026 专业版》PDF 为 **v1.0 内容基线**，将 100 道题拆成 100 个独立 Markdown，并在不改变原题核心口径的前提下升级到 v2.0：每题增加逐题专属的原理推导、边界条件、工程实现、验证方法、知识网络与复习路径。

目标不是做一份“背答案”的八股题库，而是训练下面这条完整能力链：

```text
Definition
   ↓
Objective / Formula
   ↓
Why / Derivation
   ↓
Trade-off / Boundary
   ↓
Implementation / Complexity
   ↓
Failure Mode / Verification
   ↓
Production / System Thinking
```

---

## 1. v2.0 内容规模

- **100 / 100** 道独立题解，题号连续、可独立引用与 Review。
- **10** 个知识章节，从 ML 基础一路覆盖到 LLM Serving / Distributed。
- 每题保留 PDF 原始核心答案，同时增加 **专业深挖：原理、边界与工程**。
- 每题包含 difficulty / frequency / tags / version / reading time 等 frontmatter。
- 每题包含 60 秒回答、Know-Why、公式 / 结构、工程验证、失分点、追问树与关联题。
- PDF 原始文本与逐题 raw extraction 保存在 `sources/`，支持 provenance 审计。
- `data/questions.json` 提供机器可读索引；`data/deepdives_v2.mdpack` 保存 v2 专属扩写源。
- MkDocs 配置可直接构建静态站点。
- GitHub Actions / 本地脚本可自动检查题号、结构、链接和源文件完整性。

---

## 2. 章节地图

| 章节 | 题号 | 核心能力 |
|---|---:|---|
| [数学、概率与机器学习基础](docs/01-ml-foundations/index.md) | Q001–Q012 | 概率建模、指标、优化、数值 |
| [统计 NLP 与传统 NLP](docs/02-classical-nlp/index.md) | Q013–Q024 | HMM/CRF、BM25、DP、数据增强 |
| [表示学习与序列模型](docs/03-representation-sequence/index.md) | Q025–Q034 | Word2Vec、PMI、RNN/LSTM、Seq2Seq |
| [Transformer 核心原理](docs/04-transformer/index.md) | Q035–Q050 | Attention、RoPE、Norm、FFN、GQA |
| [BERT、GPT 与大模型预训练](docs/05-pretraining/index.md) | Q051–Q064 | LM 目标、Tokenizer、Scaling、Data、MoE |
| [SFT、PEFT 与对齐](docs/06-alignment/index.md) | Q065–Q074 | LoRA/QLoRA、Distill、RLHF、DPO、GRPO |
| [检索、搜索与 RAG](docs/07-retrieval-rag/index.md) | Q075–Q084 | Sparse/Dense、ANN、Rerank、RAG Eval |
| [数据工程与 Evaluation](docs/08-data-evaluation/index.md) | Q085–Q090 | Curation、Dedup、Decontam、Synthetic、Judge |
| [推理、分布式与 AI Infra](docs/09-inference-infra/index.md) | Q091–Q096 | KV Cache、Quant、Serving、并行通信 |
| [手写代码与 Debug](docs/10-coding-debug/index.md) | Q097–Q100 | 数值稳定、Shape、向量化、Transformer Debug |

---

## 3. 每一道题的标准结构

```text
1. 题目
2. 面试官到底在考什么
3. 30–60 秒标准回答
4. 白板核心公式 / 结构
5. 第一性原理与 Know-Why
6. 专业深挖：原理、边界与工程
7. 实现、复杂度与工程验证
8. 高频失分点
9. 追问树
10. 面试现场自检
11. 参考资料
12. 关联题目与知识网络
13. 一句话收束
```

v2.0 的重点是第 6–7 节：不再使用统一模板解释所有问题，而是逐题加入特定推导与系统细节。例如：

- RoPE：从 $R_m^TR_n=R_{n-m}$ 推相对位置，并连接 KV Cache position offset。
- GQA：从 $H_{kv}$ 推 KV Cache bytes 与 decode HBM 带宽。
- DPO：从 KL-regularized optimal policy 解释 policy/reference log-ratio。
- BM25：解释 TF saturation、length normalization 与 RAG chunking 的耦合。
- MinHash：区分 Jaccard 估计、LSH 候选概率与多阶段外部去重。
- Transformer Debug：使用 cached-vs-full logits consistency 作为核心不变量测试。

---

## 4. 推荐学习方式

### Pass 1 — 建立全局地图

只读每题的 **30–60 秒标准回答**。目标不是记细节，而是能回答“这道题一句话在解决什么”。

### Pass 2 — 白板推导

所有公式题必须闭卷写；Transformer 题必须写 shape；系统题必须画数据流 / 资源账本。

### Pass 3 — 追问与反例

每题强制回答：

1. 为什么？
2. 上一代方法的问题是什么？
3. 代价是什么？
4. 什么时候不成立？
5. 生产怎么验证？

### Pass 4 — 随机模拟

禁止按题号顺序背诵。使用 [按主题索引](docs/indexes/by-topic.md) 或 [按难度索引](docs/indexes/by-difficulty.md) 随机抽题，限制 60 秒 / 3 分钟两档时间。

更完整方法见：

- [如何使用这 100 道题](docs/00-guide/how-to-use.md)
- [专业面试回答框架](docs/00-guide/answer-framework.md)
- [30 天刷题计划](docs/00-guide/30-day-plan.md)

---

## 5. Repo 结构

```text
.
├── README.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── CHANGELOG.md
├── mkdocs.yml
├── data/
│   ├── questions.json
│   ├── deepdives_v2.mdpack
│   └── build_stats_v2.json
├── docs/
│   ├── 00-guide/
│   ├── 01-ml-foundations/
│   ├── ...
│   ├── 10-coding-debug/
│   ├── appendices/
│   └── indexes/
├── sources/
│   ├── pdf_text.txt
│   ├── questions_raw/
│   └── provenance.md
├── assets/pdf/
├── scripts/
│   ├── check_repo.py
│   └── enrich_v2.py
└── .github/workflows/
```

---

## 6. 快速入口

- [文档首页](docs/index.md)
- [30 天刷题计划](docs/00-guide/30-day-plan.md)
- [回答框架](docs/00-guide/answer-framework.md)
- [按主题索引](docs/indexes/by-topic.md)
- [按难度索引](docs/indexes/by-difficulty.md)
- [公式速查](docs/appendices/formula-cheatsheet.md)
- [Coding / Debug Checklist](docs/appendices/coding-checklist.md)
- [术语表](docs/appendices/glossary.md)
- [参考资料](docs/appendices/references.md)
- [真实性与来源](docs/00-guide/authenticity.md)
- [数据血缘 / Provenance](sources/provenance.md)

---

## 7. 本地构建

```bash
python -m pip install -r requirements-docs.txt
mkdocs serve
```

完整性检查：

```bash
python scripts/check_repo.py
```

重新应用 v2 深度扩写：

```bash
python scripts/enrich_v2.py
```

---

## 8. 内容质量标准

一个高质量 PR / 题解至少应满足：

- **Correct**：公式、定义与代码语义正确。
- **Source-aware**：PDF 基线与后续扩展可区分；新增事实优先给论文 / 官方文档。
- **Interview-first**：先有短答案，再有推导；不要把题解写成无重点论文综述。
- **Boundary-aware**：至少说明一个 trade-off / failure mode / 不适用条件。
- **Engineering-aware**：能给 shape、复杂度、资源账本、验证方法中的至少一种。
- **Maintainable**：题号、链接、frontmatter 和导航不破坏。

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

---

## 9. 来源与真实性

本仓库 **不是任何公司的内部题库**。PDF 与 Repo 中“公开题型”来自公开候选人经验、开源题库、公开职位能力要求与经典高频问法的归纳。扩写部分属于原创学习材料。

- 原始 PDF：`assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf`
- PDF 文本：`sources/pdf_text.txt`
- 逐题原始抽取：`sources/questions_raw/Q001.txt ... Q100.txt`
- v2 专属扩写：`data/deepdives_v2.mdpack`

具体转换原则见 [sources/provenance.md](sources/provenance.md)。

---

## 10. License

本仓库原创整理与扩展内容采用 **CC BY-NC-SA 4.0**。第三方论文、项目、候选人公开经验及 PDF 中涉及的第三方材料仍归各自权利人所有。
