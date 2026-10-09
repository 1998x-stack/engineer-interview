# Fenwick / Segment Tree / Range Structure

> 本章覆盖 **087-092**，共 6 题。

## 源书稿章节导语

> 处理“动态更新 + 区间查询”，理解数据结构如何缓存可组合的区间信息。

## 章节能力目标

- 先区分静态/动态、点更新/区间更新、可逆/不可逆操作，再选择 Fenwick、Segment Tree 或有序区间结构。

## 深化版章节训练目标

**章节核心：** 动态区间聚合与顺序统计

**主要 Pattern：** `Fenwick / Segment Tree / Ordered Intervals`

### 面试前的三次检查

1. 先判断操作是否可 merge
2. 统一区间开闭语义
3. 动态更新后静态 prefix 是否失效

### 难度分布

- `H`：3 题
- `H+`：2 题
- `M/H`：1 题

### 推荐训练顺序

1. **基础结构题**：先练接口与基本不变量，不追求花哨优化。
2. **Pattern 题**：把同一结构的 2–3 题连续做，找共同状态定义。
3. **Hard/变体题**：只看约束，不看题名，练从 baseline 推 structure。
4. **Follow-up 复盘**：不重写整题，只回答“哪个前提变了、哪一层结构要换”。

> 章节 README 只负责能力地图；真正的证明、代码审查与对抗测试都在各 `Qxxx.md` 的 §12 专业深化中。

## 题目列表

| ID | 题目 | 难度 | 核心 |
|---|---|---|---|
| Q087 | [Fenwick Tree：动态单点修改 + 区间和](Q087-Fenwick-Tree-动态单点修改-+-区间和.md) | M/H | Fenwick Tree / 前缀和 |
| Q088 | [Segment Tree：动态 Range Min/Max/Sum](Q088-Segment-Tree-动态-Range-Min-Max-Sum.md) | H | Segment Tree / 区间查询 |
| Q089 | [Range Module：动态添加/删除/查询区间](Q089-Range-Module-动态添加-删除-查询区间.md) | H+ | Interval Tree / Segment Tree |
| Q090 | [逆序对数量](Q090-逆序对数量.md) | H | Fenwick Tree / Merge Sort |
| Q091 | [动态第 K 小：Order Statistic Tree](Q091-动态第-K-小-Order-Statistic-Tree.md) | H+ | Segment Tree / Order Statistics |
| Q092 | [SummaryRanges：数据流维护不相交区间](Q092-SummaryRanges-数据流维护不相交区间.md) | H | Ordered Map / Interval |
