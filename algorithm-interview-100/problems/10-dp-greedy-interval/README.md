# 动态规划、贪心与区间

**核心能力：** DP / Greedy / Interval






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：状态定义、最优子结构与交换论证**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- DP 先写 state/transition/base/order
- 空间压缩先证明依赖
- 贪心必须有证明，不靠直觉

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
| 087 | 70 | [爬楼梯](./087-climbing-stairs.md) | Easy | S | 1D DP |
| 088 | 198 | [打家劫舍](./088-house-robber.md) | Medium | S | Take/Skip DP |
| 089 | 322 | [零钱兑换](./089-coin-change.md) | Medium | S | Unbounded Knapsack |
| 090 | 300 | [最长递增子序列](./090-longest-increasing-subsequence.md) | Medium | S | DP + Patience Binary Search |
| 091 | 1143 | [最长公共子序列](./091-longest-common-subsequence.md) | Medium | S | 2D Sequence DP |
| 092 | 72 | [编辑距离](./092-edit-distance.md) | Medium | S | 2D Alignment DP |
| 093 | 139 | [单词拆分](./093-word-break.md) | Medium | S | Prefix DP |
| 094 | 416 | [分割等和子集](./094-partition-equal-subset-sum.md) | Medium | S | 0/1 Knapsack |
| 095 | 152 | [乘积最大子数组](./095-maximum-product-subarray.md) | Medium | A | Dual-state DP |
| 096 | 121 | [买卖股票的最佳时机](./096-best-time-to-buy-and-sell-stock.md) | Easy | S | One-pass State / Greedy |
| 097 | 56 | [合并区间](./097-merge-intervals.md) | Medium | S | Sort + Sweep |
| 098 | 57 | [插入区间](./098-insert-interval.md) | Medium | A | Three-phase Interval Scan |
| 099 | 435 | [无重叠区间](./099-non-overlapping-intervals.md) | Medium | A | Interval Scheduling Greedy |
| 100 | 45 | [跳跃游戏 II](./100-jump-game-ii.md) | Medium | S | Layered Greedy |
