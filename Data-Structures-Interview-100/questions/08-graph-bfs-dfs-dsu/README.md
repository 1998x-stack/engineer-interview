# Graph / BFS / DFS / Union-Find

> 本章覆盖 **073-086**，共 14 题。

## 源书稿章节导语

> 先建模图，再决定遍历、最短路、拓扑、连通性还是最小生成树。

## 章节能力目标

- 无权最短路用 BFS；依赖用拓扑；动态连通用 DSU；正权最短路用 Dijkstra；最小连接成本用 MST。

## 深化版章节训练目标

**章节核心：** 图建模、连通性、最短路与依赖

**主要 Pattern：** `BFS / DFS / DSU / Topo / Dijkstra / MST`

### 面试前的三次检查

1. 先定义 node/edge/direction/weight
2. 无权最短路优先 BFS
3. 动态合并连通优先 DSU

### 难度分布

- `H`：2 题
- `H+`：1 题
- `M`：9 题
- `M/H`：2 题

### 推荐训练顺序

1. **基础结构题**：先练接口与基本不变量，不追求花哨优化。
2. **Pattern 题**：把同一结构的 2–3 题连续做，找共同状态定义。
3. **Hard/变体题**：只看约束，不看题名，练从 baseline 推 structure。
4. **Follow-up 复盘**：不重写整题，只回答“哪个前提变了、哪一层结构要换”。

> 章节 README 只负责能力地图；真正的证明、代码审查与对抗测试都在各 `Qxxx.md` 的 §12 专业深化中。

## 题目列表

| ID | 题目 | 难度 | 核心 |
|---|---|---|---|
| Q073 | [岛屿数量](Q073-岛屿数量.md) | M | Graph / Grid |
| Q074 | [Clone Graph](Q074-Clone-Graph.md) | M | Graph / DFS/BFS |
| Q075 | [判断无向图是否为树](Q075-判断无向图是否为树.md) | M | Graph / DFS |
| Q076 | [无向图连通分量数量](Q076-无向图连通分量数量.md) | M | Graph / DFS |
| Q077 | [Course Schedule：课程依赖是否可完成](Q077-Course-Schedule-课程依赖是否可完成.md) | M | Graph / Topological Sort |
| Q078 | [Alien Dictionary：未知字母序](Q078-Alien-Dictionary-未知字母序.md) | H | Graph / Topological Sort |
| Q079 | [Word Ladder 最短转换路径](Q079-Word-Ladder-最短转换路径.md) | H | Graph / BFS |
| Q080 | [Pacific Atlantic Water Flow](Q080-Pacific-Atlantic-Water-Flow.md) | M/H | Graph / Reverse Search |
| Q081 | [Binary Matrix 最短路径](Q081-Binary-Matrix-最短路径.md) | M | BFS / Grid |
| Q082 | [Network Delay：Dijkstra 单源最短路](Q082-Network-Delay-Dijkstra-单源最短路.md) | M | Graph / Dijkstra |
| Q083 | [连接所有点的最小代价：MST](Q083-连接所有点的最小代价-MST.md) | M/H | Graph / MST |
| Q084 | [Accounts Merge](Q084-Accounts-Merge.md) | M | DSU / HashMap |
| Q085 | [Redundant Connection：找成环边](Q085-Redundant-Connection-找成环边.md) | M | DSU / Cycle Detection |
| Q086 | [无根度≤3 树重新选根，使其成为二叉树并满足层颜色模式](Q086-无根度≤3-树重新选根-使其成为二叉树并满足层颜色模式.md) | H+ | Tree / Rerooting |
