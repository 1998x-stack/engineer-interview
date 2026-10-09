# PDF 原稿：附录与结语

> 以下内容从源 PDF 抽取并做最小排版清理。

附录 A：复杂度速查表
    结构                   优势                        短板                      面试识别信号

Array                   随机访问 O(1)                  中间插入/删除 O(n)            连续内存、cache 友好

HashMap/Set             平均查找/插入/删除 O(1)            最坏 O(n)                 依赖 hash 与负载因子

Linked List             已知节点后插删 O(1)               按位置访问 O(n)              指针不变量

Stack/Queue             push/pop/enqueue/dequeue   -                       LIFO/FIFO
                        O(1)

Binary Heap             push/pop O(log n)，peek     任意删除不方便                 Top-K / 调度
                        O(1)

BST(平衡)                 查找/插删 O(log n)             退化树 O(n)                有序、范围查询

Trie                    字符串操作 O(L)                 空间可能很大                  前缀查询

DSU                     近 O(1) union/find          不擅长删除边                  连通分量

Fenwick                 update/query O(log n)      操作类型受限                  前缀聚合

Segment Tree            query/update O(log n)      实现与常数较大                 通用区间结构

附录 B：7 天 / 21 天 / 6 周复习路线
7 天冲刺：只覆盖最常出现的结构，目标是形成识别反射。

    Day 1：Q001-Q015 数组/字符串
    Day 2：Q016-Q033 Hash + 链表
    Day 3：Q034-Q043 栈队列 + Q059-Q066 Heap
    Day 4：Q044-Q058 Tree/BST
    Day 5：Q073-Q086 Graph/DSU
    Day 6：Q067-Q072 Trie + Q093-Q100 设计
    Day 7：随机抽 12 题做完整 45 分钟模拟，强制讲复杂度与 follow-up

21 天：每个章节安排 1-3 天，第一天看 Pattern 与基础题，第二天手写中高难，第三天只做变体与追问。

6 周：第 1-4 周按章节学习；第 5 周按 Pattern 混刷，打破“章节提示”；第 6 周做 45 分钟模拟面试，重点
记录卡顿点、边界 bug 与表达问题。

附录 C：公开资料与趋势证据
Tech Interview Handbook - Data structures and algorithms study cheatsheets — 截至 2026 年的主题优先级与常
见面试准备方法。
   https://www.techinterviewhandbook.org/algorithms/study-cheatsheet/

Tech Interview Handbook - Coding interview techniques — Hash、Graph、Stack/Queue、Heap、Tree/Trie 以及
常见算法模式的识别建议。
   https://www.techinterviewhandbook.org/coding-interview-techniques/

Tech Interview Handbook - Linked List / Heap / Tree / Trie guides — 经典结构的操作、边界与核心练习题。
   https://www.techinterviewhandbook.org/algorithms/

LeetCode Discuss - Google L5 Interview, January 2025 — 候选人自述：Shift sweep-line、无根树重新选根、Range
Module 等变体；非官方。
   https://leetcode.com/discuss/post/6522571/

LeetCode Discuss - Google L3 interview experience, 2025 — 候选人自述：开放式内存文件系统/Trie 设计；非官方。
   https://leetcode.com/discuss/post/6982323/

LeetCode Discuss - Google SWE II Early Careers, 2026 — 候选人自述：Trie+HashMap、Graph+DSU 等组合题趋势；
非官方。
   https://leetcode.com/discuss/post/8449337/

LeetCode Discuss - Google Trie Question — 候选人自述：层级字符串/路径 Trie 变体；非官方。
   https://leetcode.com/discuss/post/7101066/

结语：面试数据结构的真正目标
 不要背 100 份代码 目标是看到约束后，能解释为什么某个结构减少了重复工作；能用不变量证明它正确；能在
 follow-up 改变约束后替换结构，而不是重新从零猜答案。

如果只能记住一句话：先把问题写成“我需要反复查询/维护什么信息”，再问哪种数据结构能以最低成本维
护这个信息。数据结构不是答案，它是为某个不变量服务的工具。
