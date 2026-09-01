# 第 8 章 · 数据工程与 Evaluation

> **章节目标**：把“数据清洗”升级成可审计、可重跑、可消融的数据平台，并正确评价 synthetic/Judge。

## 1. 先修知识

数据工程、hash/Jaccard、基本实验设计。

## 2. 本章知识路线

Q085–Q087 清洗/去重/污染 → Q088–Q090 合成数据、Judge、线上评估。

## 3. 必须白板掌握

- 完整 curation pipeline
- Exact vs MinHash
- LSH 概率
- Decontamination 多层召回
- Synthetic 4D quality
- Judge bias
- Offline-online gap

## 4. 高频失分模式

- 过滤越多越好
- MinHash 当硬阈值
- 无字符串重叠=无污染
- Judge=真值
- 删样本不留 reason/provenance

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q085 | [预训练数据清洗 Pipeline 应如何设计？](Q085-pretraining-data-pipeline.md) | ★★★★ | ★★★★★ |
| Q086 | [Exact Dedup 与 MinHash：何时用哪一个？](Q086-exact-dedup-vs-minhash.md) | ★★★★ | ★★★★★ |
| Q087 | [Benchmark Decontamination 为什么不能只做 Exact Match？](Q087-benchmark-decontamination.md) | ★★★★ | ★★★★★ |
| Q088 | [合成数据质量：Validity、Faithfulness、Diversity、Utility](Q088-synthetic-data-quality.md) | ★★★★★ | ★★★★★ |
| Q089 | [LLM‑as‑a‑Judge 有哪些系统性偏差？](Q089-llm-as-judge.md) | ★★★★ | ★★★★★ |
| Q090 | [离线指标涨了，为什么线上可能变差？](Q090-offline-online-gap.md) | ★★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
