# Pattern 地图

100 题的目标不是 100 种算法，而是建立一组可迁移的数据访问模式和不变量。

| Pattern | 核心思想 |
|---|---|
| [Binary Search](../patterns/binary-search.md) | 每次基于单调判定排除一半空间 |
| [Composite Data Structure Design](../patterns/composite.md) | 从 API 复杂度反推结构组合 |
| [Dijkstra / MST](../patterns/dijkstra-mst.md) | 带权路径与最小连接成本 |
| [Union-Find / DSU](../patterns/dsu.md) | 维护动态等价类 |
| [Fast-Slow Pointer](../patterns/fast-slow.md) | 通过相对速度/距离处理链表结构 |
| [BFS / DFS](../patterns/graph-search.md) | 把隐式/显式关系建模成图后搜索 |
| [Hash Lookup](../patterns/hash-lookup.md) | 把反复线性搜索变成索引查询 |
| [Heap / Top-K](../patterns/heap-topk.md) | 只维护当前最重要的 k 个候选 |
| [Monotonic Structures](../patterns/monotonic.md) | 淘汰未来永远不可能成为答案的候选 |
| [Prefix Sum](../patterns/prefix-sum.md) | 把区间查询转成两个前缀状态之差 |
| [Range Structures](../patterns/range.md) | 动态更新与区间聚合 |
| [Sliding Window](../patterns/sliding-window.md) | 连续区间 + 可单调移动的边界 |
| [Topological Sort](../patterns/toposort.md) | 把依赖关系转成 DAG 上的可执行顺序 |
| [Tree Postorder DP](../patterns/tree-dp.md) | 子树返回局部状态，节点合并形成更大状态 |
| [Trie](../patterns/trie.md) | 用树共享字符串/路径前缀 |
| [Two Pointers](../patterns/two-pointers.md) | 利用有序性/相对运动删除一个循环 |
