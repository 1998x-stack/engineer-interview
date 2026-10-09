# Follow-up 索引

> 将 100 题中的“面试官追问”集中到一起，适合第三遍复习时只练约束变化和结构替换。

## [Q001 Two Sum：两数之和](../questions/01-arrays-strings-matrix-intervals/Q001-Two-Sum-两数之和.md)

- 如果数组已经有序，能否做到 O(1) 额外空间？
- 如果要返回所有不重复数值对，如何去重？
- 数据流场景下如何在线判断？

## [Q002 3Sum：三数之和](../questions/01-arrays-strings-matrix-intervals/Q002-3Sum-三数之和.md)

- 改成 4Sum 如何泛化？
- 如何写一个通用 k-Sum？
- 若只要求是否存在而不是列举所有答案，能否更早退出？

## [Q003 最长无重复字符子串](../questions/01-arrays-strings-matrix-intervals/Q003-最长无重复字符子串.md)

- 如果最多允许 K 个不同字符怎么办？
- 如果最多允许重复一次怎么办？
- 若输入是无限字符流，状态如何维护？

## [Q004 最小覆盖子串](../questions/01-arrays-strings-matrix-intervals/Q004-最小覆盖子串.md)

- 如果要求覆盖 t 的任意排列，本题为何仍适用？
- 如果要求最短子序列而非子串，结构会怎样变化？

## [Q005 除自身以外数组乘积](../questions/01-arrays-strings-matrix-intervals/Q005-除自身以外数组乘积.md)

- 如果数据会溢出怎么办？
- 如果只允许单遍扫描，能否做到同样复杂度？为什么困难？

## [Q006 最大连续子数组和](../questions/01-arrays-strings-matrix-intervals/Q006-最大连续子数组和.md)

- 如何返回具体区间？
- 若允许删除一个元素，状态如何增加？
- 二维矩阵最大子矩形如何由此扩展？

## [Q007 和为 K 的子数组数量](../questions/01-arrays-strings-matrix-intervals/Q007-和为-K-的子数组数量.md)

- 若只求最长和为 k 子数组，哈希表应存什么？
- 二维矩阵中统计和为 target 的子矩形怎样降维？

## [Q008 滑动窗口最大值](../questions/01-arrays-strings-matrix-intervals/Q008-滑动窗口最大值.md)

- 如何同时输出 min 和 max？
- 如果窗口大小动态变化怎么办？
- 为什么这是一种摊销 O(1) 操作？

## [Q009 接雨水](../questions/01-arrays-strings-matrix-intervals/Q009-接雨水.md)

- 用单调栈如何做？
- 二维高度图接雨水为什么需要最小堆？

## [Q010 旋转有序数组查找](../questions/01-arrays-strings-matrix-intervals/Q010-旋转有序数组查找.md)

- 允许重复元素后最坏复杂度为何可能退化为 O(n)？
- 如何找旋转数组最小值？

## [Q011 合并重叠区间](../questions/01-arrays-strings-matrix-intervals/Q011-合并重叠区间.md)

- 插入一个新区间并合并如何做到 O(n)？
- 若区间来自在线数据流，使用什么有序结构？

## [Q012 员工 Shift 时间线：输出每段时间的在岗人员](../questions/01-arrays-strings-matrix-intervals/Q012-员工-Shift-时间线-输出每段时间的在岗人员.md)

- 若需要按员工优先级输出怎么办？
- 若输入持续在线到达，如何支持增量查询？
- 如果只要求人数，结构可简化成什么？

## [Q013 矩阵螺旋遍历](../questions/01-arrays-strings-matrix-intervals/Q013-矩阵螺旋遍历.md)

- 逆时针如何改？
- 如果要求原地把矩阵按螺旋顺序重排怎么办？

## [Q014 第一个缺失的正整数](../questions/01-arrays-strings-matrix-intervals/Q014-第一个缺失的正整数.md)

- 如果数组只读，最优空间/时间 trade-off 是什么？
- 类似技巧还能解决 Find All Missing Numbers 吗？

## [Q015 两个有序数组的中位数](../questions/01-arrays-strings-matrix-intervals/Q015-两个有序数组的中位数.md)

- 如何求两个有序数组联合第 K 小？
- 推广到多个有序数组，中位数还能保持对数复杂度吗？

## [Q016 有效字母异位词](../questions/02-hashmap-hashset/Q016-有效字母异位词.md)

- 若字符仅为 a-z，怎样避免 HashMap？
- 海量字符串外存场景如何做？

## [Q017 按字母异位词分组](../questions/02-hashmap-hashset/Q017-按字母异位词分组.md)

- Unicode 文本最合适的 signature 是什么？
- 如果要保持每组原输入顺序怎么办？

## [Q018 最长连续整数序列](../questions/02-hashmap-hashset/Q018-最长连续整数序列.md)

- 如果数据量大到内存放不下怎么办？
- 若要动态 insert 并实时查询最长连续段，如何用 DSU？

## [Q019 K 距离内是否存在重复值](../questions/02-hashmap-hashset/Q019-K-距离内是否存在重复值.md)

- 如果再要求 |nums[i]-nums[j]|<=t，需要什么有序结构/桶化技巧？

## [Q020 O(1) Insert/Delete/GetRandom 集合](../questions/02-hashmap-hashset/Q020-O-1-Insert-Delete-GetRandom-集合.md)

- 允许重复元素怎样改？见 Q97
- 如何按权重随机抽样？

## [Q021 从零实现 HashMap](../questions/02-hashmap-hashset/Q021-从零实现-HashMap.md)

- Open Addressing 如何处理 tombstone？
- 为什么容量常选 2 的幂或质数？
- 如何抵御恶意 hash collision？

## [Q022 Hash Collision、负载因子与复杂度退化](../questions/02-hashmap-hashset/Q022-Hash-Collision、负载因子与复杂度退化.md)

- Separate chaining 与 linear probing 的 cache locality 谁更好？
- 删除在 open addressing 中为何需要 tombstone？
- Java HashMap 树化思想解决了什么最坏情况？

## [Q023 稀疏向量点积](../questions/02-hashmap-hashset/Q023-稀疏向量点积.md)

- 一边极稀疏、一边较稠密时最优表示是什么？
- 矩阵乘法中的 CSR/CSC 与这个问题有什么联系？

## [Q024 反转单链表](../questions/03-linked-list/Q024-反转单链表.md)

- 递归版本如何写？
- 如何反转区间 [m,n]？
- K 个一组反转如何复用这个 primitive？

## [Q025 判断链表是否有环](../questions/03-linked-list/Q025-判断链表是否有环.md)

- 如何找到环入口？见 Q26
- 如何计算环长度？

## [Q026 寻找链表环入口](../questions/03-linked-list/Q026-寻找链表环入口.md)

- 证明可用模运算还是路程方程？
- 如果链表结构允许多个 outgoing edge，这个技巧为何失效？

## [Q027 合并两个有序链表](../questions/03-linked-list/Q027-合并两个有序链表.md)

- 递归版本复杂度如何？
- 如果节点不可修改，需要怎样复制？

## [Q028 合并 K 个有序链表](../questions/03-linked-list/Q028-合并-K-个有序链表.md)

- 若 k 极大而每条链很短，分治与 heap 的 cache 行为如何？
- 外存 K 路归并为什么同样用 heap？

## [Q029 删除倒数第 N 个节点](../questions/03-linked-list/Q029-删除倒数第-N-个节点.md)

- 如果 n 可能非法如何健壮处理？
- 单向链表为什么不能从尾部直接访问？

## [Q030 重排链表 L0→Ln→L1→Ln-1…](../questions/03-linked-list/Q030-重排链表-L0→Ln→L1→Ln-1….md)

- 能否把三阶段写成可复用 helper？
- 如何证明最终不会产生 cycle？

## [Q031 两个单链表的交点](../questions/03-linked-list/Q031-两个单链表的交点.md)

- 若两链各自可能有环，交点情况怎样分类？

## [Q032 复制带 Random Pointer 的链表](../questions/03-linked-list/Q032-复制带-Random-Pointer-的链表.md)

- 如果节点还有多个任意引用边，本质上是否变成 Clone Graph？

## [Q033 回文链表](../questions/03-linked-list/Q033-回文链表.md)

- 如何恢复原链表？
- 递归方案的隐含空间复杂度是多少？

## [Q034 有效括号](../questions/04-stack-queue-deque/Q034-有效括号.md)

- 若括号字符串中夹杂普通字符如何处理？
- 如何返回第一个错误位置？

## [Q035 Min Stack](../questions/04-stack-queue-deque/Q035-Min-Stack.md)

- 只用一个栈如何编码旧最小值？
- 进一步支持 getMax 怎么办？

## [Q036 两个栈实现队列](../questions/04-stack-queue-deque/Q036-两个栈实现队列.md)

- 用势能法如何证明摊销复杂度？

## [Q037 一个/两个队列实现栈](../questions/04-stack-queue-deque/Q037-一个-两个队列实现栈.md)

- 如果严格只允许 enqueue/dequeue/front，代码如何调整？

## [Q038 每日温度：下一个更高温度](../questions/04-stack-queue-deque/Q038-每日温度-下一个更高温度.md)

- 如何求下一个更小元素？
- 循环数组的 Next Greater 如何处理？

## [Q039 Next Greater Element 通用模板](../questions/04-stack-queue-deque/Q039-Next-Greater-Element-通用模板.md)

- 为什么单调栈经常能把 O(n^2) 的“向左/右找第一个”降成 O(n)？

## [Q040 柱状图最大矩形](../questions/04-stack-queue-deque/Q040-柱状图最大矩形.md)

- 最大矩形在二进制矩阵中如何复用本题？

## [Q041 Decode String：解码嵌套重复串](../questions/04-stack-queue-deque/Q041-Decode-String-解码嵌套重复串.md)

- 若输出可能指数级巨大但只询问第 K 个字符，如何避免完整展开？

## [Q042 碰撞模拟：Asteroid Collision](../questions/04-stack-queue-deque/Q042-碰撞模拟-Asteroid-Collision.md)

- 如果速度不同，为什么栈模型可能不再足够？

## [Q043 Basic Calculator：表达式求值](../questions/04-stack-queue-deque/Q043-Basic-Calculator-表达式求值.md)

- 加入 * / 后用双栈还是递归下降？
- 如何构建 AST 而不只是求值？

## [Q044 二叉树最大深度](../questions/05-binary-tree-bst/Q044-二叉树最大深度.md)

- 如何迭代实现？
- 最小深度为何不能直接把 max 改 min？

## [Q045 翻转二叉树](../questions/05-binary-tree-bst/Q045-翻转二叉树.md)

- 如何用 BFS 原地翻转？

## [Q046 二叉树层序遍历](../questions/05-binary-tree-bst/Q046-二叉树层序遍历.md)

- Zigzag 层序如何改？
- 如何只用 O(1) 额外空间遍历 perfect tree 的 next 指针？

## [Q047 二叉树右视图](../questions/05-binary-tree-bst/Q047-二叉树右视图.md)

- 左视图？顶部视图需要额外什么坐标信息？

## [Q048 二叉树直径](../questions/05-binary-tree-bst/Q048-二叉树直径.md)

- 如何返回直径对应的实际路径？
- N 叉树直径如何改？

## [Q049 判断平衡二叉树](../questions/05-binary-tree-bst/Q049-判断平衡二叉树.md)

- AVL 树如何在插入/删除后维持这个约束？

## [Q050 验证二叉搜索树](../questions/05-binary-tree-bst/Q050-验证二叉搜索树.md)

- 用 inorder 如何验证？
- 如果 BST 允许重复值且规定重复都放右边，边界如何改变？

## [Q051 BST 第 K 小元素](../questions/05-binary-tree-bst/Q051-BST-第-K-小元素.md)

- 如果频繁查询 kth，如何给每个节点维护 subtree_size 使单次查询 O(h)？

## [Q052 BST 最近公共祖先](../questions/05-binary-tree-bst/Q052-BST-最近公共祖先.md)

- 若只给数值不保证存在于树中，需要先验证吗？

## [Q053 普通二叉树最近公共祖先](../questions/05-binary-tree-bst/Q053-普通二叉树最近公共祖先.md)

- 若需要验证两节点都存在，返回状态怎么扩展？
- 多个节点的 LCA 如何做？

## [Q054 Preorder + Inorder 重建二叉树](../questions/05-binary-tree-bst/Q054-Preorder-+-Inorder-重建二叉树.md)

- Postorder + Inorder 如何重建？
- Preorder + Postorder 为什么一般不能唯一确定？

## [Q055 二叉树序列化与反序列化](../questions/05-binary-tree-bst/Q055-二叉树序列化与反序列化.md)

- 如何设计二进制紧凑格式？
- BST 是否可以省掉 null 标记？为什么？

## [Q056 二叉树最大路径和](../questions/05-binary-tree-bst/Q056-二叉树最大路径和.md)

- 如何返回实际节点路径？
- 边有权而节点无权时怎么改？

## [Q057 判断子树](../questions/05-binary-tree-bst/Q057-判断子树.md)

- 如何用树哈希降低复杂度？
- 哈希碰撞如何处理？

## [Q058 二叉树原地展开为链表](../questions/05-binary-tree-bst/Q058-二叉树原地展开为链表.md)

- 递归 reverse-preorder 版本如何写？
- 与 Morris traversal 有何关系？

## [Q059 数组第 K 大元素](../questions/06-heap-priority-queue/Q059-数组第-K-大元素.md)

- 数据流版本为什么 heap 更合适？
- 若 k 接近 n，是否可以维护 n-k+1 的 max heap？

## [Q060 距离原点最近的 K 个点](../questions/06-heap-priority-queue/Q060-距离原点最近的-K-个点.md)

- 更高维点如何泛化？
- Quickselect 的 partition invariant 是什么？

## [Q061 日志 Top-K 活跃用户，并保留阈值并列者](../questions/06-heap-priority-queue/Q061-日志-Top-K-活跃用户-并保留阈值并列者.md)

- 如果日志是流式且内存有限怎么办？
- Count-Min Sketch 能提供什么近似保证？

## [Q062 Meeting Rooms II：最少会议室](../questions/06-heap-priority-queue/Q062-Meeting-Rooms-II-最少会议室.md)

- 用 start/end 两个排序数组如何 O(n log n) 完成？
- 如何实际分配 room id？

## [Q063 K 个有序数组的归并](../questions/06-heap-priority-queue/Q063-K-个有序数组的归并.md)

- 外排序/日志归并为什么是相同结构？
- 若数组在远程机器上，如何考虑 I/O 和批量预取？

## [Q064 数据流中位数](../questions/06-heap-priority-queue/Q064-数据流中位数.md)

- 如何支持删除任意元素？见 Q65
- 如何求在线 90% 分位数？

## [Q065 滑动窗口中位数](../questions/06-heap-priority-queue/Q065-滑动窗口中位数.md)

- 如果语言提供 multiset/order-statistic tree，方案会更简单吗？
- 为什么这是“逻辑删除”与“物理删除”分离？

## [Q066 多服务器任务调度](../questions/06-heap-priority-queue/Q066-多服务器任务调度.md)

- 加入服务器故障/动态扩容后结构怎样演化？
- 与事件驱动模拟有什么关系？

## [Q067 实现 Trie：insert/search/startsWith](../questions/07-trie-prefix-tree/Q067-实现-Trie-insert-search-startsWith.md)

- 如何支持 delete？
- Radix Tree/Patricia Trie 如何压缩单孩子链？

## [Q068 支持通配符 . 的词典](../questions/07-trie-prefix-tree/Q068-支持通配符-.-的词典.md)

- 若支持 * 匹配任意长度，状态空间怎样变化？

## [Q069 Autocomplete：前缀返回 Top-K 候选](../questions/07-trie-prefix-tree/Q069-Autocomplete-前缀返回-Top-K-候选.md)

- 写多读少如何改成查询时计算？
- 如何做个性化 autocomplete？
- 分布式场景如何 shard？

## [Q070 Word Search II：棋盘中查找多个单词](../questions/07-trie-prefix-tree/Q070-Word-Search-II-棋盘中查找多个单词.md)

- 如何加入对角线？
- 如果棋盘很大且词典变化频繁，预处理谁更合适？

## [Q071 最短词根替换句子](../questions/07-trie-prefix-tree/Q071-最短词根替换句子.md)

- 如果词根有权重且要选择“最优”而非最短，节点需要存什么？

## [Q072 层级路径/域名祖先值聚合](../questions/07-trie-prefix-tree/Q072-层级路径-域名祖先值聚合.md)

- 如果查询很多但更新也频繁，如何缓存？
- 路径存在 wildcard 时结构如何改？

## [Q073 岛屿数量](../questions/08-graph-bfs-dfs-dsu/Q073-岛屿数量.md)

- 8 邻接如何改？
- 动态增加陆地并实时报告岛屿数如何用 DSU？

## [Q074 Clone Graph](../questions/08-graph-bfs-dfs-dsu/Q074-Clone-Graph.md)

- 如何迭代 BFS 实现？
- 若节点包含更多 mutable metadata，深拷贝边界怎么定义？

## [Q075 判断无向图是否为树](../questions/08-graph-bfs-dfs-dsu/Q075-判断无向图是否为树.md)

- 多次动态加边，哪种 DSU API 更自然？

## [Q076 无向图连通分量数量](../questions/08-graph-bfs-dfs-dsu/Q076-无向图连通分量数量.md)

- 为什么路径压缩 + 按秩合并近似常数？

## [Q077 Course Schedule：课程依赖是否可完成](../questions/08-graph-bfs-dfs-dsu/Q077-Course-Schedule-课程依赖是否可完成.md)

- 如何返回一条合法课程顺序？
- 如何返回一个具体 cycle？

## [Q078 Alien Dictionary：未知字母序](../questions/08-graph-bfs-dfs-dsu/Q078-Alien-Dictionary-未知字母序.md)

- 如何判断拓扑序是否唯一？

## [Q079 Word Ladder 最短转换路径](../questions/08-graph-bfs-dfs-dsu/Q079-Word-Ladder-最短转换路径.md)

- 双向 BFS 为什么通常更快？
- 如何返回所有最短路径？

## [Q080 Pacific Atlantic Water Flow](../questions/08-graph-bfs-dfs-dsu/Q080-Pacific-Atlantic-Water-Flow.md)

- 类似“边界可达性”问题还有哪些反向搜索例子？

## [Q081 Binary Matrix 最短路径](../questions/08-graph-bfs-dfs-dsu/Q081-Binary-Matrix-最短路径.md)

- 不同格子成本不同后为什么要 Dijkstra/0-1 BFS？

## [Q082 Network Delay：Dijkstra 单源最短路](../questions/08-graph-bfs-dfs-dsu/Q082-Network-Delay-Dijkstra-单源最短路.md)

- 有负边用什么？
- 权重只有 0/1 时如何用 deque 做 0-1 BFS？

## [Q083 连接所有点的最小代价：MST](../questions/08-graph-bfs-dfs-dsu/Q083-连接所有点的最小代价-MST.md)

- 稠密完整图上 Prim O(V^2) 什么时候反而更合适？

## [Q084 Accounts Merge](../questions/08-graph-bfs-dfs-dsu/Q084-Accounts-Merge.md)

- 如果 email 关系会被删除，DSU 为什么不擅长动态删除？

## [Q085 Redundant Connection：找成环边](../questions/08-graph-bfs-dfs-dsu/Q085-Redundant-Connection-找成环边.md)

- 有向版本为何复杂很多？

## [Q086 无根度≤3 树重新选根，使其成为二叉树并满足层颜色模式](../questions/08-graph-bfs-dfs-dsu/Q086-无根度≤3-树重新选根-使其成为二叉树并满足层颜色模式.md)

- 如何把每个 root 的 BFS 从 O(n^2) 优化成 reroot DP？
- 若树边带权，层的概念如何定义？

## [Q087 Fenwick Tree：动态单点修改 + 区间和](../questions/09-range-data-structures/Q087-Fenwick-Tree-动态单点修改-+-区间和.md)

- 如何做 range add + point query？
- 如何通过两个 BIT 做 range add + range sum？

## [Q088 Segment Tree：动态 Range Min/Max/Sum](../questions/09-range-data-structures/Q088-Segment-Tree-动态-Range-Min-Max-Sum.md)

- Range update 如何引出 Lazy Propagation？
- 为何 min 无法像 sum 一样简单用前缀差？

## [Q089 Range Module：动态添加/删除/查询区间](../questions/09-range-data-structures/Q089-Range-Module-动态添加-删除-查询区间.md)

- query 单点与 query 区间的 API 差异
- 隐式动态 Segment Tree 如何只创建访问到的节点？

## [Q090 逆序对数量](../questions/09-range-data-structures/Q090-逆序对数量.md)

- 归并排序计数如何证明？
- Count Smaller After Self 与它是什么关系？

## [Q091 动态第 K 小：Order Statistic Tree](../questions/09-range-data-structures/Q091-动态第-K-小-Order-Statistic-Tree.md)

- 若键动态出现，平衡 BST 的 subtree_size 怎么维护？

## [Q092 SummaryRanges：数据流维护不相交区间](../questions/09-range-data-structures/Q092-SummaryRanges-数据流维护不相交区间.md)

- 如果支持删除一个数，区间可能 split，如何处理？

## [Q093 LRU Cache](../questions/10-composite-design/Q093-LRU-Cache.md)

- 并发 LRU 如何加锁？
- 加入 TTL 怎么办？
- LFU 为什么需要额外频率维度？

## [Q094 LFU Cache](../questions/10-composite-design/Q094-LFU-Cache.md)

- 如果频率无限增长如何 aging？
- 为什么“频率+时间”两个排序维度不适合一个简单 heap？

## [Q095 Time Based Key-Value Store](../questions/10-composite-design/Q095-Time-Based-Key-Value-Store.md)

- 如果版本可删除/乱序写入，需要什么结构？
- 如何做 MVCC/TTL？

## [Q096 All O(1) Data Structure](../questions/10-composite-design/Q096-All-O-1-Data-Structure.md)

- 与 LFU 的 bucket 结构有什么共性？

## [Q097 RandomizedCollection：允许重复的 O(1) 随机集合](../questions/10-composite-design/Q097-RandomizedCollection-允许重复的-O-1-随机集合.md)

- 若希望每个 distinct value 等概率，结构如何变化？

## [Q098 简化 Twitter News Feed](../questions/10-composite-design/Q098-简化-Twitter-News-Feed.md)

- 大 V 用户（百万粉丝）怎么扩展？
- feed 缓存失效策略？

## [Q099 设计内存文件系统](../questions/10-composite-design/Q099-设计内存文件系统.md)

- 如何增加 rm/mv/symlink？
- 如何维护目录总大小并支持增量更新？

## [Q100 Hit Counter：最近 5 分钟请求计数](../questions/10-composite-design/Q100-Hit-Counter-最近-5-分钟请求计数.md)

- 分布式计数器如何处理时钟偏差？
- 近似统计可否使用时间桶？
- 若窗口从固定变成任意长度怎么办？
