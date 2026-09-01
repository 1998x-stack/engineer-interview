# 二分搜索与答案空间

**核心能力：** Boundary Search / Binary Search on Answer






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：单调答案空间与边界语义**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 先证明单调性再二分
- 固定闭区间/半开区间模板
- 答案二分先写 check(x)

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
| 037 | 704 | [二分查找](./037-binary-search.md) | Easy | S | Exact Binary Search |
| 038 | 33 | [搜索旋转排序数组](./038-search-in-rotated-sorted-array.md) | Medium | S | Partitioned Monotonicity |
| 039 | 153 | [寻找旋转排序数组中的最小值](./039-find-minimum-in-rotated-sorted-array.md) | Medium | A | Boundary Binary Search |
| 040 | 34 | [查找元素首尾位置](./040-find-first-and-last-position.md) | Medium | S | Lower/Upper Bound |
| 041 | 4 | [寻找两个正序数组的中位数](./041-median-of-two-sorted-arrays.md) | Hard | S | Binary Partition |
| 042 | 875 | [爱吃香蕉的珂珂](./042-koko-eating-bananas.md) | Medium | S | Binary Search on Answer |
| 043 | 1011 | [在 D 天内送达包裹的能力](./043-capacity-to-ship-packages-within-d-days.md) | Medium | S | Feasibility Search |
| 044 | 162 | [寻找峰值](./044-find-peak-element.md) | Medium | A | Slope Binary Search |
