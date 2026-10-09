# 数据结构面试 100 题：Professional Interview Handbook

> 以《数据结构面试100题：专业面试宝典》PDF 为源书稿，重构为适合 GitHub 学习、检索、维护和扩展的知识仓库。

## 为什么这个仓库不是“100 个答案”

核心目标是把 100 道题压缩成有限的 Pattern，并训练完整面试链路：

**澄清 → 基线 → 瓶颈 → 结构选择 → 不变量 → 编码 → 正确性 → 复杂度 → 边界 → Follow-up**。

每个问题都有独立 Markdown，完整承接 PDF 原稿，并新增正确性证明框架、复杂度审查、边界测试、Code Review、追问答题方向和自测清单。

## Repository Structure

```text
.
├── README.md
├── assets/pdf/                  # 原始专业版 PDF
├── docs/                        # 原稿前置内容、附录、方法论、学习路线
├── patterns/                    # 核心 Pattern 深化
├── questions/                   # 100 题；一题一个 Markdown
│   ├── 01-arrays-strings-matrix-intervals/
│   ├── 02-hashmap-hashset/
│   ├── ...
│   └── 10-composite-design/
├── progress/                    # 可复制的复习进度表
├── scripts/                     # 仓库完整性检查
└── .github/workflows/           # CI：校验 100 题与必要章节
```

## 原始 PDF

- [下载/查看《数据结构面试100题：专业面试宝典》](assets/pdf/数据结构面试100题_专业版.pdf)
- [PDF 前置内容（抽取版）](docs/source-book-frontmatter.md)
- [PDF 附录与结语（抽取版）](docs/source-book-appendices.md)

## 章节导航

- [数组、字符串、矩阵与区间（Q001-Q015）](questions/01-arrays-strings-matrix-intervals/README.md)
- [HashMap / HashSet（Q016-Q023）](questions/02-hashmap-hashset/README.md)
- [链表（Q024-Q033）](questions/03-linked-list/README.md)
- [Stack / Queue / Deque（Q034-Q043）](questions/04-stack-queue-deque/README.md)
- [Binary Tree / BST（Q044-Q058）](questions/05-binary-tree-bst/README.md)
- [Heap / Priority Queue（Q059-Q066）](questions/06-heap-priority-queue/README.md)
- [Trie / Prefix Tree（Q067-Q072）](questions/07-trie-prefix-tree/README.md)
- [Graph / BFS / DFS / Union-Find（Q073-Q086）](questions/08-graph-bfs-dfs-dsu/README.md)
- [Fenwick / Segment Tree / Range Structure（Q087-Q092）](questions/09-range-data-structures/README.md)
- [复合数据结构设计（Q093-Q100）](questions/10-composite-design/README.md)

## 交叉索引

- [按难度索引](docs/INDEX_BY_DIFFICULTY.md)
- [按核心结构索引](docs/INDEX_BY_CORE.md)
- [Pattern 地图](docs/PATTERN_MAP.md)
- [Follow-up 索引](docs/FOLLOWUP_INDEX.md)
- [公开面经变体索引](docs/PUBLIC_INTERVIEW_VARIANTS.md)
- [模拟面试评分 Rubric](docs/REVIEW_RUBRIC.md)
- [构建血缘 / Provenance](docs/PROVENANCE.md)

## Pattern 导航

- [Hash Lookup](patterns/hash-lookup.md) · [Two Pointers](patterns/two-pointers.md) · [Sliding Window](patterns/sliding-window.md)
- [Prefix Sum](patterns/prefix-sum.md) · [Monotonic Structures](patterns/monotonic.md) · [Binary Search](patterns/binary-search.md)
- [Fast-Slow Pointer](patterns/fast-slow.md) · [Tree DP](patterns/tree-dp.md) · [Heap / Top-K](patterns/heap-topk.md)
- [Trie](patterns/trie.md) · [BFS / DFS](patterns/graph-search.md) · [DSU](patterns/dsu.md) · [Topological Sort](patterns/toposort.md)
- [Dijkstra / MST](patterns/dijkstra-mst.md) · [Range Structures](patterns/range.md) · [Composite Design](patterns/composite.md)

## 推荐使用方式

1. **第一遍：** 只看题目与澄清，自己给出 baseline。
2. **第二遍：** 只看关键洞察和 invariant，再独立手写代码。
3. **第三遍：** 只做边界与 follow-up，练结构替换。
4. **模拟面试：** 随机抽题，45 分钟内完整讲清思考与复杂度，不以“代码通过”为唯一目标。
5. **复盘：** 使用 [`progress/progress.csv`](progress/progress.csv) 记录是否能独立完成、卡在哪里、下次复习时间。


## v2 深化版说明

当前 100 道题已完成第二轮专业深化。除源 PDF 内容外，每个 `Qxxx.md` 额外包含：

- 约束 → Pattern 的识别信号；
- 状态最小化与“未来充分统计量”分析；
- 2–4 种解法谱系与 Trade-off；
- 针对本题的正确性证明；
- 隐藏复杂度参数与工程复杂度边界；
- Pattern 定制 Dry Run 表；
- Code Review 清单；
- 对抗性测试矩阵；
- 每个 Follow-up 的展开答题方向；
- Pattern 迁移与面试官评分视角。

详见 [`docs/DEEP_REVIEW_GUIDE.md`](docs/DEEP_REVIEW_GUIDE.md)。

## 100 题目录

| ID | 题目 | 难度 | 章节 |
|---|---|---|---|
| Q001 | [Two Sum：两数之和](questions/01-arrays-strings-matrix-intervals/Q001-Two-Sum-两数之和.md) | E | 数组、字符串、矩阵与区间 |
| Q002 | [3Sum：三数之和](questions/01-arrays-strings-matrix-intervals/Q002-3Sum-三数之和.md) | M | 数组、字符串、矩阵与区间 |
| Q003 | [最长无重复字符子串](questions/01-arrays-strings-matrix-intervals/Q003-最长无重复字符子串.md) | M | 数组、字符串、矩阵与区间 |
| Q004 | [最小覆盖子串](questions/01-arrays-strings-matrix-intervals/Q004-最小覆盖子串.md) | H | 数组、字符串、矩阵与区间 |
| Q005 | [除自身以外数组乘积](questions/01-arrays-strings-matrix-intervals/Q005-除自身以外数组乘积.md) | M | 数组、字符串、矩阵与区间 |
| Q006 | [最大连续子数组和](questions/01-arrays-strings-matrix-intervals/Q006-最大连续子数组和.md) | M | 数组、字符串、矩阵与区间 |
| Q007 | [和为 K 的子数组数量](questions/01-arrays-strings-matrix-intervals/Q007-和为-K-的子数组数量.md) | M | 数组、字符串、矩阵与区间 |
| Q008 | [滑动窗口最大值](questions/01-arrays-strings-matrix-intervals/Q008-滑动窗口最大值.md) | H | 数组、字符串、矩阵与区间 |
| Q009 | [接雨水](questions/01-arrays-strings-matrix-intervals/Q009-接雨水.md) | H | 数组、字符串、矩阵与区间 |
| Q010 | [旋转有序数组查找](questions/01-arrays-strings-matrix-intervals/Q010-旋转有序数组查找.md) | M | 数组、字符串、矩阵与区间 |
| Q011 | [合并重叠区间](questions/01-arrays-strings-matrix-intervals/Q011-合并重叠区间.md) | M | 数组、字符串、矩阵与区间 |
| Q012 | [员工 Shift 时间线：输出每段时间的在岗人员](questions/01-arrays-strings-matrix-intervals/Q012-员工-Shift-时间线-输出每段时间的在岗人员.md) | H | 数组、字符串、矩阵与区间 |
| Q013 | [矩阵螺旋遍历](questions/01-arrays-strings-matrix-intervals/Q013-矩阵螺旋遍历.md) | M | 数组、字符串、矩阵与区间 |
| Q014 | [第一个缺失的正整数](questions/01-arrays-strings-matrix-intervals/Q014-第一个缺失的正整数.md) | H | 数组、字符串、矩阵与区间 |
| Q015 | [两个有序数组的中位数](questions/01-arrays-strings-matrix-intervals/Q015-两个有序数组的中位数.md) | H+ | 数组、字符串、矩阵与区间 |
| Q016 | [有效字母异位词](questions/02-hashmap-hashset/Q016-有效字母异位词.md) | E | HashMap / HashSet |
| Q017 | [按字母异位词分组](questions/02-hashmap-hashset/Q017-按字母异位词分组.md) | M | HashMap / HashSet |
| Q018 | [最长连续整数序列](questions/02-hashmap-hashset/Q018-最长连续整数序列.md) | M | HashMap / HashSet |
| Q019 | [K 距离内是否存在重复值](questions/02-hashmap-hashset/Q019-K-距离内是否存在重复值.md) | E/M | HashMap / HashSet |
| Q020 | [O(1) Insert/Delete/GetRandom 集合](questions/02-hashmap-hashset/Q020-O-1-Insert-Delete-GetRandom-集合.md) | M | HashMap / HashSet |
| Q021 | [从零实现 HashMap](questions/02-hashmap-hashset/Q021-从零实现-HashMap.md) | M | HashMap / HashSet |
| Q022 | [Hash Collision、负载因子与复杂度退化](questions/02-hashmap-hashset/Q022-Hash-Collision、负载因子与复杂度退化.md) | M | HashMap / HashSet |
| Q023 | [稀疏向量点积](questions/02-hashmap-hashset/Q023-稀疏向量点积.md) | M | HashMap / HashSet |
| Q024 | [反转单链表](questions/03-linked-list/Q024-反转单链表.md) | E | 链表 |
| Q025 | [判断链表是否有环](questions/03-linked-list/Q025-判断链表是否有环.md) | E/M | 链表 |
| Q026 | [寻找链表环入口](questions/03-linked-list/Q026-寻找链表环入口.md) | M | 链表 |
| Q027 | [合并两个有序链表](questions/03-linked-list/Q027-合并两个有序链表.md) | E | 链表 |
| Q028 | [合并 K 个有序链表](questions/03-linked-list/Q028-合并-K-个有序链表.md) | H | 链表 |
| Q029 | [删除倒数第 N 个节点](questions/03-linked-list/Q029-删除倒数第-N-个节点.md) | M | 链表 |
| Q030 | [重排链表 L0→Ln→L1→Ln-1…](questions/03-linked-list/Q030-重排链表-L0→Ln→L1→Ln-1….md) | M | 链表 |
| Q031 | [两个单链表的交点](questions/03-linked-list/Q031-两个单链表的交点.md) | E/M | 链表 |
| Q032 | [复制带 Random Pointer 的链表](questions/03-linked-list/Q032-复制带-Random-Pointer-的链表.md) | M/H | 链表 |
| Q033 | [回文链表](questions/03-linked-list/Q033-回文链表.md) | M | 链表 |
| Q034 | [有效括号](questions/04-stack-queue-deque/Q034-有效括号.md) | E | Stack / Queue / Deque |
| Q035 | [Min Stack](questions/04-stack-queue-deque/Q035-Min-Stack.md) | M | Stack / Queue / Deque |
| Q036 | [两个栈实现队列](questions/04-stack-queue-deque/Q036-两个栈实现队列.md) | E/M | Stack / Queue / Deque |
| Q037 | [一个/两个队列实现栈](questions/04-stack-queue-deque/Q037-一个-两个队列实现栈.md) | E | Stack / Queue / Deque |
| Q038 | [每日温度：下一个更高温度](questions/04-stack-queue-deque/Q038-每日温度-下一个更高温度.md) | M | Stack / Queue / Deque |
| Q039 | [Next Greater Element 通用模板](questions/04-stack-queue-deque/Q039-Next-Greater-Element-通用模板.md) | M | Stack / Queue / Deque |
| Q040 | [柱状图最大矩形](questions/04-stack-queue-deque/Q040-柱状图最大矩形.md) | H | Stack / Queue / Deque |
| Q041 | [Decode String：解码嵌套重复串](questions/04-stack-queue-deque/Q041-Decode-String-解码嵌套重复串.md) | M | Stack / Queue / Deque |
| Q042 | [碰撞模拟：Asteroid Collision](questions/04-stack-queue-deque/Q042-碰撞模拟-Asteroid-Collision.md) | M | Stack / Queue / Deque |
| Q043 | [Basic Calculator：表达式求值](questions/04-stack-queue-deque/Q043-Basic-Calculator-表达式求值.md) | H | Stack / Queue / Deque |
| Q044 | [二叉树最大深度](questions/05-binary-tree-bst/Q044-二叉树最大深度.md) | E | Binary Tree / BST |
| Q045 | [翻转二叉树](questions/05-binary-tree-bst/Q045-翻转二叉树.md) | E | Binary Tree / BST |
| Q046 | [二叉树层序遍历](questions/05-binary-tree-bst/Q046-二叉树层序遍历.md) | M | Binary Tree / BST |
| Q047 | [二叉树右视图](questions/05-binary-tree-bst/Q047-二叉树右视图.md) | M | Binary Tree / BST |
| Q048 | [二叉树直径](questions/05-binary-tree-bst/Q048-二叉树直径.md) | M | Binary Tree / BST |
| Q049 | [判断平衡二叉树](questions/05-binary-tree-bst/Q049-判断平衡二叉树.md) | E/M | Binary Tree / BST |
| Q050 | [验证二叉搜索树](questions/05-binary-tree-bst/Q050-验证二叉搜索树.md) | M | Binary Tree / BST |
| Q051 | [BST 第 K 小元素](questions/05-binary-tree-bst/Q051-BST-第-K-小元素.md) | M | Binary Tree / BST |
| Q052 | [BST 最近公共祖先](questions/05-binary-tree-bst/Q052-BST-最近公共祖先.md) | M | Binary Tree / BST |
| Q053 | [普通二叉树最近公共祖先](questions/05-binary-tree-bst/Q053-普通二叉树最近公共祖先.md) | M | Binary Tree / BST |
| Q054 | [Preorder + Inorder 重建二叉树](questions/05-binary-tree-bst/Q054-Preorder-+-Inorder-重建二叉树.md) | M | Binary Tree / BST |
| Q055 | [二叉树序列化与反序列化](questions/05-binary-tree-bst/Q055-二叉树序列化与反序列化.md) | H | Binary Tree / BST |
| Q056 | [二叉树最大路径和](questions/05-binary-tree-bst/Q056-二叉树最大路径和.md) | H | Binary Tree / BST |
| Q057 | [判断子树](questions/05-binary-tree-bst/Q057-判断子树.md) | M | Binary Tree / BST |
| Q058 | [二叉树原地展开为链表](questions/05-binary-tree-bst/Q058-二叉树原地展开为链表.md) | M | Binary Tree / BST |
| Q059 | [数组第 K 大元素](questions/06-heap-priority-queue/Q059-数组第-K-大元素.md) | M | Heap / Priority Queue |
| Q060 | [距离原点最近的 K 个点](questions/06-heap-priority-queue/Q060-距离原点最近的-K-个点.md) | M | Heap / Priority Queue |
| Q061 | [日志 Top-K 活跃用户，并保留阈值并列者](questions/06-heap-priority-queue/Q061-日志-Top-K-活跃用户-并保留阈值并列者.md) | M/H | Heap / Priority Queue |
| Q062 | [Meeting Rooms II：最少会议室](questions/06-heap-priority-queue/Q062-Meeting-Rooms-II-最少会议室.md) | M | Heap / Priority Queue |
| Q063 | [K 个有序数组的归并](questions/06-heap-priority-queue/Q063-K-个有序数组的归并.md) | M/H | Heap / Priority Queue |
| Q064 | [数据流中位数](questions/06-heap-priority-queue/Q064-数据流中位数.md) | H | Heap / Priority Queue |
| Q065 | [滑动窗口中位数](questions/06-heap-priority-queue/Q065-滑动窗口中位数.md) | H+ | Heap / Priority Queue |
| Q066 | [多服务器任务调度](questions/06-heap-priority-queue/Q066-多服务器任务调度.md) | H | Heap / Priority Queue |
| Q067 | [实现 Trie：insert/search/startsWith](questions/07-trie-prefix-tree/Q067-实现-Trie-insert-search-startsWith.md) | M | Trie / Prefix Tree |
| Q068 | [支持通配符 . 的词典](questions/07-trie-prefix-tree/Q068-支持通配符-.-的词典.md) | M | Trie / Prefix Tree |
| Q069 | [Autocomplete：前缀返回 Top-K 候选](questions/07-trie-prefix-tree/Q069-Autocomplete-前缀返回-Top-K-候选.md) | H | Trie / Prefix Tree |
| Q070 | [Word Search II：棋盘中查找多个单词](questions/07-trie-prefix-tree/Q070-Word-Search-II-棋盘中查找多个单词.md) | H | Trie / Prefix Tree |
| Q071 | [最短词根替换句子](questions/07-trie-prefix-tree/Q071-最短词根替换句子.md) | M | Trie / Prefix Tree |
| Q072 | [层级路径/域名祖先值聚合](questions/07-trie-prefix-tree/Q072-层级路径-域名祖先值聚合.md) | H | Trie / Prefix Tree |
| Q073 | [岛屿数量](questions/08-graph-bfs-dfs-dsu/Q073-岛屿数量.md) | M | Graph / BFS / DFS / Union-Find |
| Q074 | [Clone Graph](questions/08-graph-bfs-dfs-dsu/Q074-Clone-Graph.md) | M | Graph / BFS / DFS / Union-Find |
| Q075 | [判断无向图是否为树](questions/08-graph-bfs-dfs-dsu/Q075-判断无向图是否为树.md) | M | Graph / BFS / DFS / Union-Find |
| Q076 | [无向图连通分量数量](questions/08-graph-bfs-dfs-dsu/Q076-无向图连通分量数量.md) | M | Graph / BFS / DFS / Union-Find |
| Q077 | [Course Schedule：课程依赖是否可完成](questions/08-graph-bfs-dfs-dsu/Q077-Course-Schedule-课程依赖是否可完成.md) | M | Graph / BFS / DFS / Union-Find |
| Q078 | [Alien Dictionary：未知字母序](questions/08-graph-bfs-dfs-dsu/Q078-Alien-Dictionary-未知字母序.md) | H | Graph / BFS / DFS / Union-Find |
| Q079 | [Word Ladder 最短转换路径](questions/08-graph-bfs-dfs-dsu/Q079-Word-Ladder-最短转换路径.md) | H | Graph / BFS / DFS / Union-Find |
| Q080 | [Pacific Atlantic Water Flow](questions/08-graph-bfs-dfs-dsu/Q080-Pacific-Atlantic-Water-Flow.md) | M/H | Graph / BFS / DFS / Union-Find |
| Q081 | [Binary Matrix 最短路径](questions/08-graph-bfs-dfs-dsu/Q081-Binary-Matrix-最短路径.md) | M | Graph / BFS / DFS / Union-Find |
| Q082 | [Network Delay：Dijkstra 单源最短路](questions/08-graph-bfs-dfs-dsu/Q082-Network-Delay-Dijkstra-单源最短路.md) | M | Graph / BFS / DFS / Union-Find |
| Q083 | [连接所有点的最小代价：MST](questions/08-graph-bfs-dfs-dsu/Q083-连接所有点的最小代价-MST.md) | M/H | Graph / BFS / DFS / Union-Find |
| Q084 | [Accounts Merge](questions/08-graph-bfs-dfs-dsu/Q084-Accounts-Merge.md) | M | Graph / BFS / DFS / Union-Find |
| Q085 | [Redundant Connection：找成环边](questions/08-graph-bfs-dfs-dsu/Q085-Redundant-Connection-找成环边.md) | M | Graph / BFS / DFS / Union-Find |
| Q086 | [无根度≤3 树重新选根，使其成为二叉树并满足层颜色模式](questions/08-graph-bfs-dfs-dsu/Q086-无根度≤3-树重新选根-使其成为二叉树并满足层颜色模式.md) | H+ | Graph / BFS / DFS / Union-Find |
| Q087 | [Fenwick Tree：动态单点修改 + 区间和](questions/09-range-data-structures/Q087-Fenwick-Tree-动态单点修改-+-区间和.md) | M/H | Fenwick / Segment Tree / Range Structure |
| Q088 | [Segment Tree：动态 Range Min/Max/Sum](questions/09-range-data-structures/Q088-Segment-Tree-动态-Range-Min-Max-Sum.md) | H | Fenwick / Segment Tree / Range Structure |
| Q089 | [Range Module：动态添加/删除/查询区间](questions/09-range-data-structures/Q089-Range-Module-动态添加-删除-查询区间.md) | H+ | Fenwick / Segment Tree / Range Structure |
| Q090 | [逆序对数量](questions/09-range-data-structures/Q090-逆序对数量.md) | H | Fenwick / Segment Tree / Range Structure |
| Q091 | [动态第 K 小：Order Statistic Tree](questions/09-range-data-structures/Q091-动态第-K-小-Order-Statistic-Tree.md) | H+ | Fenwick / Segment Tree / Range Structure |
| Q092 | [SummaryRanges：数据流维护不相交区间](questions/09-range-data-structures/Q092-SummaryRanges-数据流维护不相交区间.md) | H | Fenwick / Segment Tree / Range Structure |
| Q093 | [LRU Cache](questions/10-composite-design/Q093-LRU-Cache.md) | M/H | 复合数据结构设计 |
| Q094 | [LFU Cache](questions/10-composite-design/Q094-LFU-Cache.md) | H | 复合数据结构设计 |
| Q095 | [Time Based Key-Value Store](questions/10-composite-design/Q095-Time-Based-Key-Value-Store.md) | M | 复合数据结构设计 |
| Q096 | [All O(1) Data Structure](questions/10-composite-design/Q096-All-O-1-Data-Structure.md) | H+ | 复合数据结构设计 |
| Q097 | [RandomizedCollection：允许重复的 O(1) 随机集合](questions/10-composite-design/Q097-RandomizedCollection-允许重复的-O-1-随机集合.md) | H | 复合数据结构设计 |
| Q098 | [简化 Twitter News Feed](questions/10-composite-design/Q098-简化-Twitter-News-Feed.md) | H | 复合数据结构设计 |
| Q099 | [设计内存文件系统](questions/10-composite-design/Q099-设计内存文件系统.md) | H | 复合数据结构设计 |
| Q100 | [Hit Counter：最近 5 分钟请求计数](questions/10-composite-design/Q100-Hit-Counter-最近-5-分钟请求计数.md) | M/H | 复合数据结构设计 |

## 内容来源与边界

- **源书稿内容：** 来自仓库内 PDF，对应题目的题意、基线方案、关键洞察、不变量、Python 参考实现、复杂度、失分点、追问和 60 秒口述。
- **仓库深化内容：** 在源书稿之上增加工程化学习结构，包括证明框架、复杂度审查、边界用例、Code Review、Follow-up 解题方向、Pattern 迁移和自测。
- **公开面经变体：** 仅沿用 PDF 已明确标注的来源口径，不把候选人自述视为公司官方题库。
- **《剑指 Offer》参考边界：** 仅借鉴“问题驱动、逐步优化、强调代码质量与面试沟通”的教学思想，不复制其原文、插图或页面。

## Validation

```bash
python scripts/validate_repo.py
```

CI 会检查：题目文件数量是否恰好为 100、Q001-Q100 是否连续、每题是否包含必备章节、README 链接目标是否存在。

## License / Publication

当前仓库没有主动授予第三方开源再许可。公开发布前请阅读 [`LICENSE.md`](LICENSE.md)，并按你的发布目标替换为合适的软件/内容许可证。
