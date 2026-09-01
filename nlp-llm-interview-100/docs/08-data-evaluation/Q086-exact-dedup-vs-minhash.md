---
id: Q086
title: "Exact Dedup 与 MinHash：何时用哪一个？"
chapter: "数据工程与 Evaluation"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - data-evaluation
  - dedup
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q086 Exact Dedup 与 MinHash：何时用哪一个？

[← Q085](Q085-pretraining-data-pipeline.md) | **第 8 章 · 数据工程与 Evaluation** | [Q087 →](Q087-benchmark-decontamination.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`data-evaluation`, `dedup`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q086.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

为什么 exact hash 查不到轻微改写？MinHash 如何近似 Jaccard？

## 2. 面试官到底在考什么

要求会 Jaccard、LSH 概率与工程阶段。

### 评分维度

- 强调 provenance、可审计和实验消融。
- 把质量信号与最终训练 utility 分开。
- 讨论误删、污染、Judge 偏差和线上分布。

## 3. 30-60 秒标准回答

Exact 对规范化文本求 hash，只能抓完全相同；MinHash 对 shingle 集计算多个最小哈希，利用 “最小哈希相等概率等于 Jaccard”的性质，再用 LSH 分桶高效找近重复。

## 4. 白板核心公式

- $J(A,B)=\frac{|A\cap B|}{|A\cup B|}$
- $P[h_{min}(A)=h_{min}(B)]=J(A,B)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：通常先 exact 降规模，再 MinHash。
- **PDF 基线要点**：LSH 阈值不是硬阈值，而是 S 型候选概率。
- **PDF 基线要点**：去重簇代表样本应按质量/provenance 选，而非随机先到。
- **扩展理解**：Exact hash 解决完全重复；MinHash+LSH 近似 Jaccard，用于近重复候选。
- **扩展理解**：MinHash 的“阈值”实际是候选概率曲线，由 bands/rows 参数控制。
- **扩展理解**：生产系统还要考虑代表文档选择、全局 cluster、误删和多语言 tokenization。

## 6. 专业深挖：原理、边界与工程

### Exact Dedup 与 MinHash 解决不同重复定义
- Exact Dedup 对规范化文本算 hash，判断完全一致；速度快、误判低，但多一个页脚/日期就可能漏掉。
- MinHash 先把文档转成 shingle set，利用 $P[h_{min}(A)=h_{min}(B)]=J(A,B)$ 近似 Jaccard，再用 LSH 分桶避免 $O(N^2)$ 全对比较。
- LSH 的 band/rows 参数形成 S 型候选概率，不存在“相似度>0.8 就一定重复”的硬阈值。
### 边界与工程
- `n_gram`、tokenization、Unicode/标点规范化直接决定近重复定义；中文是否用字符/词 shingle 必须单独设计。
- 大规模 MinHash 常是 signature → bucket matching → cluster → filter 多阶段，并需要外排和集中/分布式聚类。
- 推荐先 Exact 再 MinHash，先用便宜算法减少数据规模，再做更昂贵近重复。

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

- 把 MinHash 当语义 embedding。

## 9. 追问树

1. band 数与每 band hash 数怎么影响召回/精度？
2. 中文做 word/char n-gram 怎么选？

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
- [FineWeb](https://arxiv.org/abs/2406.17557)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q085 预训练数据清洗 Pipeline 应如何设计？](Q085-pretraining-data-pipeline.md)
- [Q087 Benchmark Decontamination 为什么不能只做 Exact Match？](Q087-benchmark-decontamination.md)
- [Q088 合成数据质量：Validity、Faithfulness、Diversity、Utility](Q088-synthetic-data-quality.md)

## 13. 一句话收束

> **Exact Dedup 与 MinHash 解决不同重复定义**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
