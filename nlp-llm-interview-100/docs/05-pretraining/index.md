# 第 5 章 · BERT、GPT 与大模型预训练

> **章节目标**：从训练目标、tokenization、scaling、数据与数值系统理解 Foundation Model 预训练。

## 1. 先修知识

Transformer、Cross Entropy、基本训练循环。

## 2. 本章知识路线

Q051–Q058 目标/tokenizer → Q059–Q064 scaling、数据、精度、内存、MoE。

## 3. 必须白板掌握

- MLM vs causal LM
- BERT/GPT 条件分布差异
- Tokenizer trade-off
- Perplexity 可比性
- Scaling Law
- Dedup
- BF16
- Gradient Checkpointing
- MoE

## 4. 高频失分模式

- 把 BERT/GPT 差异只说成理解/生成
- 跨 tokenizer 比 PPL
- 把数据质量当单一分数
- BF16=更高精度
- MoE 只谈 Top-k 不谈通信

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q051 | [BERT 原始预训练任务：MLM 与 NSP](Q051-bert-mlm-nsp.md) | ★★ | ★★★★★ |
| Q052 | [为什么 BERT 不能天然像 GPT 一样左到右生成？](Q052-bert-vs-autoregressive-generation.md) | ★★★ | ★★★★★ |
| Q053 | [BERT 与 GPT：双向理解和因果生成如何取舍？](Q053-bert-vs-gpt.md) | ★★ | ★★★★★ |
| Q054 | [BPE、WordPiece、Unigram/SentencePiece 有什么区别？](Q054-bpe-wordpiece-unigram.md) | ★★★ | ★★★★★ |
| Q055 | [为什么 LLM 普遍使用 Subword/Byte Tokenization？](Q055-subword-byte-tokenization.md) | ★★ | ★★★★ |
| Q056 | [Decoder LM Loss：为什么每个 token 都是监督信号？](Q056-decoder-lm-loss.md) | ★★ | ★★★★★ |
| Q057 | [Perplexity：什么时候能比、什么时候不能比？](Q057-perplexity.md) | ★★★ | ★★★★ |
| Q058 | [Weight Tying：为什么输入 Embedding 与 LM Head 可以共享？](Q058-weight-tying.md) | ★★ | ★★★ |
| Q059 | [Scaling Law：为什么不能只堆参数？](Q059-scaling-laws.md) | ★★★★ | ★★★★★ |
| Q060 | [大模型训练为什么必须去重？](Q060-pretraining-dedup.md) | ★★★ | ★★★★★ |
| Q061 | [为什么“数据质量越高越好”是危险说法？](Q061-data-quality-tradeoff.md) | ★★★★ | ★★★★★ |
| Q062 | [Mixed Precision：BF16 为什么常比 FP16 稳？](Q062-mixed-precision.md) | ★★★ | ★★★★ |
| Q063 | [Gradient Checkpointing：省了什么、付出什么？](Q063-gradient-checkpointing.md) | ★★ | ★★★★ |
| Q064 | [MoE：为什么参数变大但每 token 计算不同比例增长？](Q064-moe.md) | ★★★★ | ★★★★★ |

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
