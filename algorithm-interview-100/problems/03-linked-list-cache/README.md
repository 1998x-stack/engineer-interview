# 链表与缓存设计

**核心能力：** Pointer Rewiring / Cache Design






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：指针重连与 O(1) 结构设计**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 画图再写代码
- dummy node 统一边界
- 复杂链表拆成定位/变换/重连

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
| 021 | 206 | [反转链表](./021-reverse-linked-list.md) | Easy | S | Pointer Rewiring |
| 022 | 92 | [反转链表 II](./022-reverse-linked-list-ii.md) | Medium | S | Segment Reversal |
| 023 | 21 | [合并两个有序链表](./023-merge-two-sorted-lists.md) | Easy | S | Two-list Merge |
| 024 | 141 | [环形链表](./024-linked-list-cycle.md) | Easy | S | Floyd Cycle Detection |
| 025 | 142 | [环形链表 II](./025-linked-list-cycle-ii.md) | Medium | S | Floyd Entrance Math |
| 026 | 25 | [K 个一组翻转链表](./026-reverse-nodes-in-k-group.md) | Hard | S | Chunked Reversal |
| 027 | 143 | [重排链表](./027-reorder-list.md) | Medium | A | Middle + Reverse + Merge |
| 028 | 148 | [排序链表](./028-sort-list.md) | Medium | A | Merge Sort on List |
| 029 | 138 | [复制带随机指针的链表](./029-copy-list-with-random-pointer.md) | Medium | A | Node Mapping / Interleaving |
| 030 | 146 | [LRU 缓存](./030-lru-cache.md) | Medium | S | Hash + Doubly Linked List |
