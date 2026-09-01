---
id: Q085
title: "预训练数据清洗 Pipeline 应如何设计？"
chapter: "数据工程与 Evaluation"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - data-evaluation
  - data
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q085 预训练数据清洗 Pipeline 应如何设计？

[← Q084](../07-retrieval-rag/Q084-rag-evaluation.md) | **第 8 章 · 数据工程与 Evaluation** | [Q086 →](Q086-exact-dedup-vs-minhash.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`data-evaluation`, `data`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q085.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

从 Common Crawl/文档源到可训练 shard，给出完整数据管线。

## 2. 面试官到底在考什么

现代基础模型岗高频系统题。

### 评分维度

- 强调 provenance、可审计和实验消融。
- 把质量信号与最终训练 utility 分开。
- 讨论误删、污染、Judge 偏差和线上分布。

## 3. 30-60 秒标准回答

典型链路：来源/许可登记 → 解析与正文抽取 →Unicode 规范化 → 语言识别 → 质量/重复/PII 过滤 →Exact/MinHash/substring 去重 →benchmark decontamination→ 统计/分层 →tokenize/- pack/shard。每一步都应保存原因、版本和 retention。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：低成本高精度规则应尽量放前面，昂贵模型过滤放后面。
- **PDF 基线要点**：过滤策略需要 per-domain/per-language 校准。
- **PDF 基线要点**：“流式 pipeline”不代表全局去重能单遍完成。
- **扩展理解**：预训练数据管线不是“过滤器堆叠”，而是来源治理、抽取、质量、去重、隐私、安全、污染、混合和 tokenize 的可审计系统。
- **扩展理解**：每一步都要记录 retention、reason code、版本与 provenance。
- **扩展理解**：最终质量判断必须通过 proxy training/downstream utility，而不只是文本审美。

## 6. 专业深挖：原理、边界与工程

### 预训练数据管线是“可审计的数据系统”
- 完整流程应包含 source/license inventory → parsing/extraction → normalization/language → quality/safety/PII → exact/near/substr dedup → decontamination → mixing → tokenize/pack/shard。
- 低成本、高精度规则尽量前置，昂贵 classifier/LLM filter 后置；但全局 dedup 需要多阶段签名、排序、聚类，不能简单一遍流式完成。
- 每一步都应保存 sample id、source、score、reason code、pipeline/config/model version 和 retention statistics，才能重跑阈值与审计来源。
### 边界与工程
- 不同 source/语言需不同策略：论文的公式符号、代码的长行、网页的菜单模板不能用同一规则。
- 过滤器质量必须通过 proxy training/downstream utility 验证；“删得更多、文本更整齐”不等于训练更好。
- 最终 shard 还要考虑 tokenizer version、packing boundary、shuffle、可恢复任务和数据血缘到训练 token 的反查。

## 7. 实现、复杂度与工程验证

- 为每次过滤保留 reason code、score、阈值、版本和 provenance。
- 质量信号不是 ground truth，必须估计误删/漏删和长尾分布损失。
- 最终用 proxy training/downstream utility 验证数据决策。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 只列步骤，不谈 observability/provenance。
- 删除样本不保存原因。

## 9. 追问树

1. 为什么先抽取正文再做语言识别？
2. 如何重跑阈值而不重算昂贵信号？

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

## 10. 面试现场自检

- [ ] 30-60 秒能给出结论，不绕弯。
- [ ] 能写出关键公式、shape 或状态转移。
- [ ] 至少能解释一个 Why 和一个 trade-off。
- [ ] 能举出一个失败模式或反例。
- [ ] 能回答两层追问。
- [ ] 能把答案连接到真实训练/检索/服务系统。

## 11. 参考资料

- [DataTrove](https://github.com/huggingface/datatrove)
- [Dolma](https://arxiv.org/abs/2402.00159)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q084 如何完整评估一个 RAG 系统？](../07-retrieval-rag/Q084-rag-evaluation.md)
- [Q086 Exact Dedup 与 MinHash：何时用哪一个？](Q086-exact-dedup-vs-minhash.md)
- [Q088 合成数据质量：Validity、Faithfulness、Diversity、Utility](Q088-synthetic-data-quality.md)

## 13. 一句话收束

> **预训练数据管线是“可审计的数据系统”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
