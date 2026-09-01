---
id: Q060
title: "大模型训练为什么必须去重？"
chapter: "BERT、GPT 与大模型预训练"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - pretraining
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q060 大模型训练为什么必须去重？

[← Q059](Q059-scaling-laws.md) | **第 5 章 · BERT、GPT 与大模型预训练** | [Q061 →](Q061-data-quality-tradeoff.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`pretraining`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q060.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

同一网页重复 100 次会发生什么？Exact、MinHash、substring dedup 分别解决什么？

## 2. 面试官到底在考什么

数据工程高频。

### 评分维度

- 区分 objective、architecture、data 与 scaling。
- 关注训练稳定性、数据分布和 token/compute budget。
- 能说明“经验规律”的适用范围，而不是绝对化。

## 3. 30-60 秒标准回答

重复相当于隐式上采样，会浪费 compute、扭曲分布、增加记忆与 benchmark contamination 风险。精确去重查完全相同，MinHash 查近重复文档，substring/句子去重查局部复制。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：去重“越彻底越好”也不成立：重复频率可能携带重要性信号。
- **PDF 基线要点**：保留哪个代表文档应考虑质量与 provenance。
- **PDF 基线要点**：多阶段去重往往需要外部排序/索引，不能简单单遍流式完成。
- **扩展理解**：重复会隐式上采样某些内容，增加 memorization、浪费 token budget，并放大污染风险。
- **扩展理解**：需要区分 exact、near-duplicate、sentence/substr dedup，不同粒度误删风险不同。
- **扩展理解**：全局去重也可能抹掉“频率本身的分布信号”，需要训练消融。

## 6. 专业深挖：原理、边界与工程

### 去重不仅省 Compute，还改变训练分布
- 同一文档重复出现相当于隐式高权重采样，会让模型浪费 token 预算、增加记忆与训练集泄漏风险，并扭曲来源/主题频率。
- Exact Dedup 解决完全相同内容；MinHash/LSH 解决高 Jaccard 近重复；Sentence/Substring Dedup 进一步处理跨文档模板和局部复制。
- 去重的关键不是“越彻底越好”：重复次数可能包含流行度/重要性信号，过强去重也会删除合法引用、法律条文和模板化知识。
### 边界与工程
- 必须定义 normalization：大小写、空白、Unicode、标点处理会决定“什么算重复”。
- 大规模 dedup 通常是多阶段、需要中间签名/外排/cluster，不是一个 Python set 就能做完。
- 代表文档最好按质量、来源、元数据完整性选，而不是永远“第一个出现的留下”。

## 7. 实现、复杂度与工程验证

- 把训练目标与数据分布联系起来：哪些 token 产生监督、模型实际最大化什么。
- 比较 tokenizer/架构时给出序列长度、FLOPs、唯一 token、显存和推理代价。
- 预训练决策最终需要固定 compute/token 预算下的消融，而不是只看局部 loss。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 只会说 hash 去重。

## 9. 追问树

1. MinHash 为什么能估计 Jaccard？
2. 跨语言/改写语义重复怎么处理？

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

- [FineWeb](https://arxiv.org/abs/2406.17557)
- [Nemotron-CC](https://arxiv.org/abs/2412.02595)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q059 Scaling Law：为什么不能只堆参数？](Q059-scaling-laws.md)
- [Q061 为什么“数据质量越高越好”是危险说法？](Q061-data-quality-tradeoff.md)
- [Q056 Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md)

## 13. 一句话收束

> **去重不仅省 Compute，还改变训练分布**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
