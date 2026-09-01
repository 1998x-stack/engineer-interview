# 回溯、搜索树与 Trie

**核心能力：** Backtracking / Trie






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：搜索树剪枝与前缀结构**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 选择-递归-撤销必须成对
- 去重发生在“同层”还是“全局”要分清
- 剪枝必须证明安全

## 本章完成标准

- [ ] S 级题全部做到无提示手写；
- [ ] 每题都能先说基线，不依赖“见过原题”；
- [ ] 每个 pattern 至少能给出一个反例说明错误做法为什么错；
- [ ] 能比较至少两种方案的时间、空间和工程 trade-off；
- [ ] 随机抽一题，90 秒内完成口述推导；
- [ ] 至少挑两题继续回答 streaming / sharding / memory-bound 追问。

## 推荐复习方式

第一次按题号顺序建立模式；第二次只看标题随机做；第三次按 pattern 跨章节混刷。真正的“掌握”标志是约束稍改后仍能重新推导，而不是记得某一份代码。

<!-- CHAPTER-ENRICHMENT-V2:END -->

| # | LC | 题目 | 难度 | 优先级 | 模式 |
|---:|---:|---|---|---|---|
| 078 | 78 | [子集](./078-subsets.md) | Medium | S | Backtracking Decision Tree |
| 079 | 46 | [全排列](./079-permutations.md) | Medium | S | Backtracking with Used Set |
| 080 | 39 | [组合总和](./080-combination-sum.md) | Medium | S | Backtracking + Reuse |
| 081 | 90 | [子集 II](./081-subsets-ii.md) | Medium | A | Sort + Same-level Dedup |
| 082 | 79 | [单词搜索](./082-word-search.md) | Medium | S | Grid Backtracking |
| 083 | 131 | [分割回文串](./083-palindrome-partitioning.md) | Medium | A | Partition Backtracking |
| 084 | 51 | [N 皇后](./084-n-queens.md) | Hard | A | Constraint Backtracking |
| 085 | 208 | [实现 Trie](./085-implement-trie.md) | Medium | S | Prefix Tree |
| 086 | 698 | [划分为 K 个相等子集](./086-partition-to-k-equal-sum-subsets.md) | Medium | S | Backtracking + Strong Pruning |
