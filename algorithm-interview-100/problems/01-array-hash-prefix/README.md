# 数组、哈希与前缀状态

**核心能力：** Hash / Prefix State / In-place Mapping






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：状态压缩与信息复用**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 先问历史查询能否 O(1)
- 连续区间优先想到 prefix 关系
- O(1) 额外空间题要考虑复用输入状态

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
| 001 | 1 | [两数之和](./001-two-sum.md) | Easy | S | Hash 查补数 |
| 002 | 49 | [字母异位词分组](./002-group-anagrams.md) | Medium | S | Canonical Key |
| 003 | 128 | [最长连续序列](./003-longest-consecutive-sequence.md) | Medium | S | Hash Set + 起点判定 |
| 004 | 238 | [除自身以外数组的乘积](./004-product-of-array-except-self.md) | Medium | S | Prefix/Suffix Product |
| 005 | 560 | [和为 K 的子数组](./005-subarray-sum-equals-k.md) | Medium | S | Prefix Sum + Hash Count |
| 006 | 525 | [连续数组](./006-contiguous-array.md) | Medium | A | Prefix State Compression |
| 007 | 41 | [缺失的第一个正数](./007-first-missing-positive.md) | Hard | S | In-place Index Mapping |
| 008 | 73 | [矩阵置零](./008-set-matrix-zeroes.md) | Medium | A | State Reuse |
| 009 | 54 | [螺旋矩阵](./009-spiral-matrix.md) | Medium | A | Boundary Simulation |
| 010 | 380 | [O(1) 插入删除与随机获取](./010-insert-delete-getrandom-o.md) | Medium | A | Hash + Dynamic Array |
