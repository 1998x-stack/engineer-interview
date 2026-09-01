# Algorithm Interview 100 / 算法岗 LeetCode 面试 100 题

> 面向算法工程师 / MLE / 推荐 / 搜索 / 广告 / NLP / CV / 多模态 / LLM 算法岗位的 **100 道母题 + 25+ 模式 + 工程化追问** 知识库。

[![CI](https://github.com/OWNER/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/OWNER/REPO/actions/workflows/ci.yml)

<!-- V2-DETAIL-BADGE -->
> **v2 教材级扩写**：100 道题现均包含 28 个结构化模块，新增解法谱系、状态表、证明骨架、复杂度深拆、测试工程、Code Review、四级 Follow-up Tree、工业约束、迁移导航、评分 Rubric 与 Active Recall。

## 为什么不是普通题单

目标不是记住 100 个答案，而是训练：

`基线方案 -> 找到信息浪费 -> 定义不变量 -> 最优实现 -> dry-run -> 复杂度 -> 约束变化 -> 算法系统`

每个问题一个 Markdown，并配套 Python 源码。Markdown 在冻结版 PDF 基础上增加：约束澄清、暴力基线、正确性说明、边界测试、工程化追问和迁移训练。

## 数据集概览

- 100 道题：Easy 13 / Medium 74 / Hard 13
- 10 大章节
- 25 个母题 pattern 文档
- 每题独立 Markdown + Python 参考实现
- R/H 证据分级，避免把公开个人面经包装成官方题库
- 内置完整性/Front Matter/链接/Python 语法 CI 检查
- 原始 PDF 与 DOCX 作为冻结发布版保留在 `docs/assets/`

## 推荐入口

1. [六步白板协议](docs/00-guide/whiteboard-protocol.md)
2. [复杂度速查](docs/00-guide/complexity-cheatsheet.md)
3. [S 级核心题](docs/02-roadmaps/s-tier-core.md)
4. [21 天冲刺](docs/02-roadmaps/21-day-sprint.md)
5. [LeetCode -> 算法系统](docs/00-guide/algorithm-to-system.md)
6. [“真题”证据口径](docs/00-guide/evidence-policy.md)
7. [题目页撰写标准](docs/00-guide/problem-authoring-standard.md)
8. [冻结版 PDF](docs/assets/algorithm-interview-100-2026.pdf)

## 目录

### 数组、哈希与前缀状态

- [001. LC1 两数之和 / Two Sum](problems/01-array-hash-prefix/001-two-sum.md) - `Hash 查补数` · Easy · S · H
- [002. LC49 字母异位词分组 / Group Anagrams](problems/01-array-hash-prefix/002-group-anagrams.md) - `Canonical Key` · Medium · S · H
- [003. LC128 最长连续序列 / Longest Consecutive Sequence](problems/01-array-hash-prefix/003-longest-consecutive-sequence.md) - `Hash Set + 起点判定` · Medium · S · H
- [004. LC238 除自身以外数组的乘积 / Product of Array Except Self](problems/01-array-hash-prefix/004-product-of-array-except-self.md) - `Prefix/Suffix Product` · Medium · S · H
- [005. LC560 和为 K 的子数组 / Subarray Sum Equals K](problems/01-array-hash-prefix/005-subarray-sum-equals-k.md) - `Prefix Sum + Hash Count` · Medium · S · H
- [006. LC525 连续数组 / Contiguous Array](problems/01-array-hash-prefix/006-contiguous-array.md) - `Prefix State Compression` · Medium · A · H
- [007. LC41 缺失的第一个正数 / First Missing Positive](problems/01-array-hash-prefix/007-first-missing-positive.md) - `In-place Index Mapping` · Hard · S · H
- [008. LC73 矩阵置零 / Set Matrix Zeroes](problems/01-array-hash-prefix/008-set-matrix-zeroes.md) - `State Reuse` · Medium · A · H
- [009. LC54 螺旋矩阵 / Spiral Matrix](problems/01-array-hash-prefix/009-spiral-matrix.md) - `Boundary Simulation` · Medium · A · H
- [010. LC380 O(1) 插入删除与随机获取 / Insert Delete GetRandom O(1)](problems/01-array-hash-prefix/010-insert-delete-getrandom-o.md) - `Hash + Dynamic Array` · Medium · A · H

### 双指针与滑动窗口

- [011. LC167 有序数组两数之和 / Two Sum II](problems/02-two-pointers-sliding-window/011-two-sum-ii.md) - `Opposite Pointers` · Medium · A · H
- [012. LC15 三数之和 / 3Sum](problems/02-two-pointers-sliding-window/012-3sum.md) - `Sort + Two Pointers` · Medium · S · H
- [013. LC11 盛最多水的容器 / Container With Most Water](problems/02-two-pointers-sliding-window/013-container-with-most-water.md) - `Greedy Two Pointers` · Medium · S · H
- [014. LC42 接雨水 / Trapping Rain Water](problems/02-two-pointers-sliding-window/014-trapping-rain-water.md) - `Two Pointers / Monotonic Stack` · Hard · S · R
- [015. LC3 无重复字符的最长子串 / Longest Substring Without Repeating Characters](problems/02-two-pointers-sliding-window/015-longest-substring-without-repeating-characters.md) - `Variable Window` · Medium · S · H
- [016. LC424 替换后的最长重复字符 / Longest Repeating Character Replacement](problems/02-two-pointers-sliding-window/016-longest-repeating-character-replacement.md) - `Window Invariant` · Medium · A · H
- [017. LC76 最小覆盖子串 / Minimum Window Substring](problems/02-two-pointers-sliding-window/017-minimum-window-substring.md) - `Need/Have Sliding Window` · Hard · S · H
- [018. LC438 找到字符串中所有字母异位词 / Find All Anagrams in a String](problems/02-two-pointers-sliding-window/018-find-all-anagrams-in-a-string.md) - `Fixed Window` · Medium · A · H
- [019. LC209 长度最小的子数组 / Minimum Size Subarray Sum](problems/02-two-pointers-sliding-window/019-minimum-size-subarray-sum.md) - `Positive-number Window` · Medium · A · H
- [020. LC239 滑动窗口最大值 / Sliding Window Maximum](problems/02-two-pointers-sliding-window/020-sliding-window-maximum.md) - `Monotonic Deque` · Hard · S · H

### 链表与缓存设计

- [021. LC206 反转链表 / Reverse Linked List](problems/03-linked-list-cache/021-reverse-linked-list.md) - `Pointer Rewiring` · Easy · S · R
- [022. LC92 反转链表 II / Reverse Linked List II](problems/03-linked-list-cache/022-reverse-linked-list-ii.md) - `Segment Reversal` · Medium · S · R
- [023. LC21 合并两个有序链表 / Merge Two Sorted Lists](problems/03-linked-list-cache/023-merge-two-sorted-lists.md) - `Two-list Merge` · Easy · S · H
- [024. LC141 环形链表 / Linked List Cycle](problems/03-linked-list-cache/024-linked-list-cycle.md) - `Floyd Cycle Detection` · Easy · S · H
- [025. LC142 环形链表 II / Linked List Cycle II](problems/03-linked-list-cache/025-linked-list-cycle-ii.md) - `Floyd Entrance Math` · Medium · S · H
- [026. LC25 K 个一组翻转链表 / Reverse Nodes in k-Group](problems/03-linked-list-cache/026-reverse-nodes-in-k-group.md) - `Chunked Reversal` · Hard · S · H
- [027. LC143 重排链表 / Reorder List](problems/03-linked-list-cache/027-reorder-list.md) - `Middle + Reverse + Merge` · Medium · A · H
- [028. LC148 排序链表 / Sort List](problems/03-linked-list-cache/028-sort-list.md) - `Merge Sort on List` · Medium · A · H
- [029. LC138 复制带随机指针的链表 / Copy List with Random Pointer](problems/03-linked-list-cache/029-copy-list-with-random-pointer.md) - `Node Mapping / Interleaving` · Medium · A · H
- [030. LC146 LRU 缓存 / LRU Cache](problems/03-linked-list-cache/030-lru-cache.md) - `Hash + Doubly Linked List` · Medium · S · R

### 栈、解析器与单调结构

- [031. LC20 有效的括号 / Valid Parentheses](problems/04-stack-parser-monotonic/031-valid-parentheses.md) - `Stack Matching` · Easy · S · H
- [032. LC155 最小栈 / Min Stack](problems/04-stack-parser-monotonic/032-min-stack.md) - `Augmented State` · Medium · S · H
- [033. LC394 字符串解码 / Decode String](problems/04-stack-parser-monotonic/033-decode-string.md) - `Stack Parser` · Medium · S · H
- [034. LC739 每日温度 / Daily Temperatures](problems/04-stack-parser-monotonic/034-daily-temperatures.md) - `Monotonic Stack` · Medium · S · H
- [035. LC84 柱状图中最大的矩形 / Largest Rectangle in Histogram](problems/04-stack-parser-monotonic/035-largest-rectangle-in-histogram.md) - `Monotonic Increasing Stack` · Hard · S · H
- [036. LC224 基本计算器 / Basic Calculator](problems/04-stack-parser-monotonic/036-basic-calculator.md) - `Expression Parsing` · Hard · A · H

### 二分搜索与答案空间

- [037. LC704 二分查找 / Binary Search](problems/05-binary-search/037-binary-search.md) - `Exact Binary Search` · Easy · S · H
- [038. LC33 搜索旋转排序数组 / Search in Rotated Sorted Array](problems/05-binary-search/038-search-in-rotated-sorted-array.md) - `Partitioned Monotonicity` · Medium · S · H
- [039. LC153 寻找旋转排序数组中的最小值 / Find Minimum in Rotated Sorted Array](problems/05-binary-search/039-find-minimum-in-rotated-sorted-array.md) - `Boundary Binary Search` · Medium · A · H
- [040. LC34 查找元素首尾位置 / Find First and Last Position](problems/05-binary-search/040-find-first-and-last-position.md) - `Lower/Upper Bound` · Medium · S · H
- [041. LC4 寻找两个正序数组的中位数 / Median of Two Sorted Arrays](problems/05-binary-search/041-median-of-two-sorted-arrays.md) - `Binary Partition` · Hard · S · R
- [042. LC875 爱吃香蕉的珂珂 / Koko Eating Bananas](problems/05-binary-search/042-koko-eating-bananas.md) - `Binary Search on Answer` · Medium · S · H
- [043. LC1011 在 D 天内送达包裹的能力 / Capacity To Ship Packages Within D Days](problems/05-binary-search/043-capacity-to-ship-packages-within-d-days.md) - `Feasibility Search` · Medium · S · H
- [044. LC162 寻找峰值 / Find Peak Element](problems/05-binary-search/044-find-peak-element.md) - `Slope Binary Search` · Medium · A · H

### 堆、Top-K、流式计算与随机采样

- [045. LC215 数组中的第 K 个最大元素 / Kth Largest Element in an Array](problems/06-heap-streaming-sampling/045-kth-largest-element-in-an-array.md) - `Heap / QuickSelect` · Medium · S · H
- [046. LC347 前 K 个高频元素 / Top K Frequent Elements](problems/06-heap-streaming-sampling/046-top-k-frequent-elements.md) - `Frequency + Selection` · Medium · S · H
- [047. LC973 最接近原点的 K 个点 / K Closest Points to Origin](problems/06-heap-streaming-sampling/047-k-closest-points-to-origin.md) - `Top-K / QuickSelect` · Medium · S · H
- [048. LC295 数据流的中位数 / Find Median from Data Stream](problems/06-heap-streaming-sampling/048-find-median-from-data-stream.md) - `Two Heaps` · Hard · S · H
- [049. LC23 合并 K 个升序链表 / Merge k Sorted Lists](problems/06-heap-streaming-sampling/049-merge-k-sorted-lists.md) - `K-way Merge` · Hard · S · H
- [050. LC346 数据流中的移动平均值 / Moving Average from Data Stream](problems/06-heap-streaming-sampling/050-moving-average-from-data-stream.md) - `Fixed-size Stream State` · Easy · A · R
- [051. LC528 按权重随机选择 / Random Pick with Weight](problems/06-heap-streaming-sampling/051-random-pick-with-weight.md) - `Prefix Weight + Sampling` · Medium · S · R
- [052. LC470 用 Rand7 实现 Rand10 / Implement Rand10() Using Rand7()](problems/06-heap-streaming-sampling/052-implement-rand10-using-rand7.md) - `Rejection Sampling` · Medium · S · R
- [053. LC912 排序数组 / Sort an Array](problems/06-heap-streaming-sampling/053-sort-an-array.md) - `Sorting Implementation` · Medium · S · R

### 二叉树与 Tree DP

- [054. LC104 二叉树最大深度 / Maximum Depth of Binary Tree](problems/07-tree-tree-dp/054-maximum-depth-of-binary-tree.md) - `Tree DFS Return Value` · Easy · S · H
- [055. LC102 二叉树层序遍历 / Binary Tree Level Order Traversal](problems/07-tree-tree-dp/055-binary-tree-level-order-traversal.md) - `BFS by Level` · Medium · S · H
- [056. LC226 翻转二叉树 / Invert Binary Tree](problems/07-tree-tree-dp/056-invert-binary-tree.md) - `Recursive Structural Transform` · Easy · B · H
- [057. LC543 二叉树的直径 / Diameter of Binary Tree](problems/07-tree-tree-dp/057-diameter-of-binary-tree.md) - `Post-order Tree DP` · Easy · S · H
- [058. LC110 平衡二叉树 / Balanced Binary Tree](problems/07-tree-tree-dp/058-balanced-binary-tree.md) - `Early-stop Tree DP` · Easy · A · H
- [059. LC98 验证二叉搜索树 / Validate Binary Search Tree](problems/07-tree-tree-dp/059-validate-binary-search-tree.md) - `Range Invariant / Inorder` · Medium · S · H
- [060. LC230 BST 中第 K 小的元素 / Kth Smallest in BST](problems/07-tree-tree-dp/060-kth-smallest-in-bst.md) - `Ordered Inorder` · Medium · S · H
- [061. LC236 二叉树最近公共祖先 / Lowest Common Ancestor of a Binary Tree](problems/07-tree-tree-dp/061-lowest-common-ancestor-of-a-binary-tree.md) - `Recursive Information Merge` · Medium · S · H
- [062. LC199 二叉树右视图 / Binary Tree Right Side View](problems/07-tree-tree-dp/062-binary-tree-right-side-view.md) - `BFS/DFS with Depth` · Medium · A · H
- [063. LC105 前序与中序构造二叉树 / Construct Binary Tree from Preorder and Inorder Traversal](problems/07-tree-tree-dp/063-construct-binary-tree-from-preorder-and-inorder-traversal.md) - `Divide & Conquer + Index Map` · Medium · S · H
- [064. LC124 二叉树中的最大路径和 / Binary Tree Maximum Path Sum](problems/07-tree-tree-dp/064-binary-tree-maximum-path-sum.md) - `Tree DP with Global Answer` · Hard · S · H
- [065. LC314 二叉树垂序遍历 / Binary Tree Vertical Order Traversal](problems/07-tree-tree-dp/065-binary-tree-vertical-order-traversal.md) - `BFS + Column Coordinate` · Medium · A · R

### 图、BFS/DFS、拓扑与并查集

- [066. LC200 岛屿数量 / Number of Islands](problems/08-graph/066-number-of-islands.md) - `Grid Connected Components` · Medium · S · H
- [067. LC695 岛屿的最大面积 / Max Area of Island](problems/08-graph/067-max-area-of-island.md) - `DFS Aggregation` · Medium · S · R
- [068. LC133 克隆图 / Clone Graph](problems/08-graph/068-clone-graph.md) - `DFS/BFS + Node Map` · Medium · A · H
- [069. LC207 课程表 / Course Schedule](problems/08-graph/069-course-schedule.md) - `Cycle Detection / Topological Sort` · Medium · S · H
- [070. LC210 课程表 II / Course Schedule II](problems/08-graph/070-course-schedule-ii.md) - `Topological Ordering` · Medium · S · H
- [071. LC127 单词接龙 / Word Ladder](problems/08-graph/071-word-ladder.md) - `Shortest Path BFS` · Hard · S · H
- [072. LC994 腐烂的橘子 / Rotting Oranges](problems/08-graph/072-rotting-oranges.md) - `Multi-source BFS` · Medium · S · H
- [073. LC417 太平洋大西洋水流问题 / Pacific Atlantic Water Flow](problems/08-graph/073-pacific-atlantic-water-flow.md) - `Reverse Reachability` · Medium · A · H
- [074. LC721 账户合并 / Accounts Merge](problems/08-graph/074-accounts-merge.md) - `Union-Find` · Medium · S · H
- [075. LC684 冗余连接 / Redundant Connection](problems/08-graph/075-redundant-connection.md) - `Union-Find Cycle Detection` · Medium · A · H
- [076. LC841 钥匙和房间 / Keys and Rooms](problems/08-graph/076-keys-and-rooms.md) - `Reachability` · Medium · A · R
- [077. LC399 除法求值 / Evaluate Division](problems/08-graph/077-evaluate-division.md) - `Weighted Graph` · Medium · A · H

### 回溯、搜索树与 Trie

- [078. LC78 子集 / Subsets](problems/09-backtracking-trie/078-subsets.md) - `Backtracking Decision Tree` · Medium · S · H
- [079. LC46 全排列 / Permutations](problems/09-backtracking-trie/079-permutations.md) - `Backtracking with Used Set` · Medium · S · H
- [080. LC39 组合总和 / Combination Sum](problems/09-backtracking-trie/080-combination-sum.md) - `Backtracking + Reuse` · Medium · S · H
- [081. LC90 子集 II / Subsets II](problems/09-backtracking-trie/081-subsets-ii.md) - `Sort + Same-level Dedup` · Medium · A · H
- [082. LC79 单词搜索 / Word Search](problems/09-backtracking-trie/082-word-search.md) - `Grid Backtracking` · Medium · S · H
- [083. LC131 分割回文串 / Palindrome Partitioning](problems/09-backtracking-trie/083-palindrome-partitioning.md) - `Partition Backtracking` · Medium · A · H
- [084. LC51 N 皇后 / N-Queens](problems/09-backtracking-trie/084-n-queens.md) - `Constraint Backtracking` · Hard · A · H
- [085. LC208 实现 Trie / Implement Trie](problems/09-backtracking-trie/085-implement-trie.md) - `Prefix Tree` · Medium · S · H
- [086. LC698 划分为 K 个相等子集 / Partition to K Equal Sum Subsets](problems/09-backtracking-trie/086-partition-to-k-equal-sum-subsets.md) - `Backtracking + Strong Pruning` · Medium · S · R

### 动态规划、贪心与区间

- [087. LC70 爬楼梯 / Climbing Stairs](problems/10-dp-greedy-interval/087-climbing-stairs.md) - `1D DP` · Easy · S · H
- [088. LC198 打家劫舍 / House Robber](problems/10-dp-greedy-interval/088-house-robber.md) - `Take/Skip DP` · Medium · S · H
- [089. LC322 零钱兑换 / Coin Change](problems/10-dp-greedy-interval/089-coin-change.md) - `Unbounded Knapsack` · Medium · S · H
- [090. LC300 最长递增子序列 / Longest Increasing Subsequence](problems/10-dp-greedy-interval/090-longest-increasing-subsequence.md) - `DP + Patience Binary Search` · Medium · S · H
- [091. LC1143 最长公共子序列 / Longest Common Subsequence](problems/10-dp-greedy-interval/091-longest-common-subsequence.md) - `2D Sequence DP` · Medium · S · H
- [092. LC72 编辑距离 / Edit Distance](problems/10-dp-greedy-interval/092-edit-distance.md) - `2D Alignment DP` · Medium · S · H
- [093. LC139 单词拆分 / Word Break](problems/10-dp-greedy-interval/093-word-break.md) - `Prefix DP` · Medium · S · H
- [094. LC416 分割等和子集 / Partition Equal Subset Sum](problems/10-dp-greedy-interval/094-partition-equal-subset-sum.md) - `0/1 Knapsack` · Medium · S · H
- [095. LC152 乘积最大子数组 / Maximum Product Subarray](problems/10-dp-greedy-interval/095-maximum-product-subarray.md) - `Dual-state DP` · Medium · A · H
- [096. LC121 买卖股票的最佳时机 / Best Time to Buy and Sell Stock](problems/10-dp-greedy-interval/096-best-time-to-buy-and-sell-stock.md) - `One-pass State / Greedy` · Easy · S · H
- [097. LC56 合并区间 / Merge Intervals](problems/10-dp-greedy-interval/097-merge-intervals.md) - `Sort + Sweep` · Medium · S · R
- [098. LC57 插入区间 / Insert Interval](problems/10-dp-greedy-interval/098-insert-interval.md) - `Three-phase Interval Scan` · Medium · A · R
- [099. LC435 无重叠区间 / Non-overlapping Intervals](problems/10-dp-greedy-interval/099-non-overlapping-intervals.md) - `Interval Scheduling Greedy` · Medium · A · H
- [100. LC45 跳跃游戏 II / Jump Game II](problems/10-dp-greedy-interval/100-jump-game-ii.md) - `Layered Greedy` · Medium · S · H

## Repo 结构

```text
algorithm-interview-100/
├── README.md
├── problems/                 # 100 道题：一题一 Markdown
│   ├── 01-array-hash-prefix/
│   ├── ...
│   └── 10-dp-greedy-interval/
├── solutions/python/         # 100 份 Python 面试实现
├── docs/
│   ├── 00-guide/             # 白板协议、复杂度、系统化追问
│   ├── 01-patterns/          # 细粒度模式文档
│   ├── 02-roadmaps/          # S 级与 21 天计划
│   ├── 03-evidence/          # 公开面经证据口径与来源
│   └── assets/               # PDF / DOCX 冻结版
├── data/problems.json        # 机器可读元数据
├── tests/                    # 代表性 smoke tests
├── scripts/check_repo.py     # 完整性 + Front Matter + 链接 + 语法检查
└── .github/workflows/ci.yml
```

## 本地校验

```bash
python scripts/check_repo.py
python -m unittest discover -s tests -v
```

## 内容边界

- 不复制 LeetCode 完整题面。
- 不复刻《剑指 Offer》正文、例题叙述或版式；只借鉴“问题驱动 -> 分析 -> 解法 -> 追问”的学习范式。
- 公开面经属于个人样本证据，不等于公司官方题库。
- 目标是提升模式迁移能力，不承诺“押中原题”。

## License

仓库原创分析、代码与组织结构以 MIT License 发布；第三方网站、题目名称及链接归其权利人所有。
