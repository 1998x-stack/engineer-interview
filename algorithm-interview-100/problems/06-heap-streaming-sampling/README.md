# 堆、Top-K、流式计算与随机采样

**核心能力：** Heap / Streaming / Sampling






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：Top-K、在线统计与概率正确性**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 区分 full sort / heap / select
- streaming 只保留最小充分状态
- sampling 必须给概率证明

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
| 045 | 215 | [数组中的第 K 个最大元素](./045-kth-largest-element-in-an-array.md) | Medium | S | Heap / QuickSelect |
| 046 | 347 | [前 K 个高频元素](./046-top-k-frequent-elements.md) | Medium | S | Frequency + Selection |
| 047 | 973 | [最接近原点的 K 个点](./047-k-closest-points-to-origin.md) | Medium | S | Top-K / QuickSelect |
| 048 | 295 | [数据流的中位数](./048-find-median-from-data-stream.md) | Hard | S | Two Heaps |
| 049 | 23 | [合并 K 个升序链表](./049-merge-k-sorted-lists.md) | Hard | S | K-way Merge |
| 050 | 346 | [数据流中的移动平均值](./050-moving-average-from-data-stream.md) | Easy | A | Fixed-size Stream State |
| 051 | 528 | [按权重随机选择](./051-random-pick-with-weight.md) | Medium | S | Prefix Weight + Sampling |
| 052 | 470 | [用 Rand7 实现 Rand10](./052-implement-rand10-using-rand7.md) | Medium | S | Rejection Sampling |
| 053 | 912 | [排序数组](./053-sort-an-array.md) | Medium | S | Sorting Implementation |
