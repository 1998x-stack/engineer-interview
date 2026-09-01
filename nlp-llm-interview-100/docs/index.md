# NLP / LLM 算法岗面试 100 题 · v2.0

这是一份按照 **“短答案 → 公式 → Why → 边界 → 工程 → 验证”** 组织的专业面试手册，而不是关键词堆叠式题库。

## 学习目标

完成 100 题后，目标不是“见过这些名词”，而是能做到：

- ML 基础题：从概率模型或优化目标推导公式。
- Transformer 题：写清 tensor shape、mask、复杂度与训练 / decode 差异。
- RAG 题：区分召回、精排、生成，能给端到端指标和 latency budget。
- 数据题：讨论 provenance、false positive / false negative、proxy training utility。
- Infra 题：会做 FLOPs / KV / HBM / communication 资源账本。
- Coding 题：先建立 reference 和不变量，再做向量化 / cache / kernel 优化。

## 章节导航

1. [数学、概率与机器学习基础](01-ml-foundations/index.md)
2. [统计 NLP 与传统 NLP](02-classical-nlp/index.md)
3. [表示学习与序列模型](03-representation-sequence/index.md)
4. [Transformer 核心原理](04-transformer/index.md)
5. [BERT、GPT 与大模型预训练](05-pretraining/index.md)
6. [SFT、PEFT 与对齐](06-alignment/index.md)
7. [检索、搜索与 RAG](07-retrieval-rag/index.md)
8. [数据工程与 Evaluation](08-data-evaluation/index.md)
9. [推理、分布式与 AI Infra](09-inference-infra/index.md)
10. [手写代码与 Debug](10-coding-debug/index.md)

## 三种阅读模式

### 面试前 1–3 天

只读每题的 **30–60 秒标准回答 + 高频失分点 + 一句话收束**。

### 系统学习

依次完成“公式 / 结构 → 专业深挖 → 工程验证 → 追问树”，每章结束后随机抽 3 题做 3 分钟回答。

### 高阶冲刺

优先 ★★★★ / ★★★★★ 题，并要求：

1. 给一个白板推导；
2. 给一个真实工程瓶颈；
3. 给一个失败模式；
4. 设计一个验证实验。

## 推荐入口

- [如何使用](00-guide/how-to-use.md)
- [面试回答框架](00-guide/answer-framework.md)
- [30 天计划](00-guide/30-day-plan.md)
- [按主题索引](indexes/by-topic.md)
- [按难度索引](indexes/by-difficulty.md)
- [公式速查](appendices/formula-cheatsheet.md)
- [Coding Checklist](appendices/coding-checklist.md)
- [术语表](appendices/glossary.md)
- [参考资料](appendices/references.md)

## 版本说明

v2.0 保留 PDF v1.0 的题目、短答案与核心 Know-Why，并将原先偏模板化的“深度分析”替换为 100 个逐题专属的专业扩展。来源与扩展边界见 [真实性说明](00-guide/authenticity.md) 和 [Provenance](../sources/provenance.md)。
