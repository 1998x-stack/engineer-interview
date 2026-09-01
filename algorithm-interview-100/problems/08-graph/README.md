# 图、BFS/DFS、拓扑与并查集

**核心能力：** Graph / Topological Sort / Union-Find






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：连通、依赖、最短路与集合合并**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 先分类问题再选 DFS/BFS/Topo/UF
- 无权最短路用 BFS
- 大图复杂度按 V+E 说

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
| 066 | 200 | [岛屿数量](./066-number-of-islands.md) | Medium | S | Grid Connected Components |
| 067 | 695 | [岛屿的最大面积](./067-max-area-of-island.md) | Medium | S | DFS Aggregation |
| 068 | 133 | [克隆图](./068-clone-graph.md) | Medium | A | DFS/BFS + Node Map |
| 069 | 207 | [课程表](./069-course-schedule.md) | Medium | S | Cycle Detection / Topological Sort |
| 070 | 210 | [课程表 II](./070-course-schedule-ii.md) | Medium | S | Topological Ordering |
| 071 | 127 | [单词接龙](./071-word-ladder.md) | Hard | S | Shortest Path BFS |
| 072 | 994 | [腐烂的橘子](./072-rotting-oranges.md) | Medium | S | Multi-source BFS |
| 073 | 417 | [太平洋大西洋水流问题](./073-pacific-atlantic-water-flow.md) | Medium | A | Reverse Reachability |
| 074 | 721 | [账户合并](./074-accounts-merge.md) | Medium | S | Union-Find |
| 075 | 684 | [冗余连接](./075-redundant-connection.md) | Medium | A | Union-Find Cycle Detection |
| 076 | 841 | [钥匙和房间](./076-keys-and-rooms.md) | Medium | A | Reachability |
| 077 | 399 | [除法求值](./077-evaluate-division.md) | Medium | A | Weighted Graph |
