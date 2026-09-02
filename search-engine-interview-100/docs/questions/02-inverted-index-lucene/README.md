# 第 2 章 · 倒排索引与 Lucene 内核

> 题目范围：Q011–Q020 · 共 10 题

## 本章目标

### 本章高级视角

倒排索引题要同时懂算法和存储。建议持续追问自己：数据是否有序？能否 delta encode？能否 block skip？哪些信息必须存 positions？更新是原地还是 append/segment？如果能把“CPU cache / sequential IO / compression / branch pruning”讲出来，回答会明显高一个层级。

## 本章高级面试检查表

| 维度 | 要求 |
|---|---|
| 核心能力 | Inverted Index & Lucene 不只会定义，要能解释它在端到端 Search Pipeline 中解决的瓶颈 |
| 必看指标 | postings visited / blocks skipped / segment count / merge bytes |
| 白板要求 | 手写 posting intersection；解释 WAND/BMW、delta compression、immutable segment 和 merge。 |
| 高频失分 | 只会倒排定义，不会解释查询执行和 merge 成本。 |
| Senior/Staff 加分 | 给规模、成本、失败模式、可观测性、灰度/回滚，并用 oracle/ablation 证明优先级 |

### 本章完成标准

完成本章后，应能把任意一道题回答成四层：**30 秒结论 → 5 分钟原理 → 10 分钟工程 trade-off → 20 分钟系统/实验设计**。如果只能复述术语而不能给数量级、反例和验证方式，说明还没有达到高级算法岗面试深度。

## 题目列表

| 题号 | 题目 | 难度 | 频率 |
|---:|---|:---:|:---:|
| Q011 | [什么是倒排索引？](Q011-inverted-index.md) | 2/5 | S |
| Q012 | [为什么叫“倒排”？正排索引还有什么用？](Q012-inverted-vs-forward-index.md) | 1/5 | B |
| Q013 | [Posting List 中一般存哪些信息？](Q013-posting-list-contents.md) | 3/5 | A |
| Q014 | [两个有序 Posting List 的 AND 查询怎么做？](Q014-posting-list-intersection.md) | 2/5 | S |
| Q015 | [Posting List 很长时，WAND / Block-Max WAND 在做什么？](Q015-wand-block-max-wand.md) | 5/5 | A |
| Q016 | [为什么 DocID 常用 gap/delta 编码？](Q016-docid-gap-delta-encoding.md) | 3/5 | A |
| Q017 | [Term Dictionary 为什么常用 FST，而不只是 HashMap？](Q017-term-dictionary-fst.md) | 4/5 | A |
| Q018 | [Trie 为什么适合做 Search Autocomplete？](Q018-trie-autocomplete.md) | 2/5 | A |
| Q019 | [Lucene Segment 为什么设计成 immutable？](Q019-lucene-immutable-segment.md) | 4/5 | S |
| Q020 | [Segment Merge 为什么既重要又危险？](Q020-segment-merge-tradeoffs.md) | 4/5 | S |

## 本章复习法

1. 第一遍只看每题的 **30 秒回答**，建立概念骨架。
2. 第二遍手写公式/伪代码，验证能否从定义恢复推导。
3. 第三遍只看“追问链”，模拟连续压力追问。
4. 最后完成每题“实战练习”，把知识转换为工程判断。

[← 返回全局索引](../../INDEX.md)
