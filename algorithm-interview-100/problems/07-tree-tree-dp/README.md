# 二叉树与 Tree DP

**核心能力：** Tree DFS/BFS / Tree DP






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：递归返回语义与 Tree DP**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 先定义 dfs 返回什么
- 返回给父节点与全局答案分离
- O(h) 栈要考虑退化树

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
| 054 | 104 | [二叉树最大深度](./054-maximum-depth-of-binary-tree.md) | Easy | S | Tree DFS Return Value |
| 055 | 102 | [二叉树层序遍历](./055-binary-tree-level-order-traversal.md) | Medium | S | BFS by Level |
| 056 | 226 | [翻转二叉树](./056-invert-binary-tree.md) | Easy | B | Recursive Structural Transform |
| 057 | 543 | [二叉树的直径](./057-diameter-of-binary-tree.md) | Easy | S | Post-order Tree DP |
| 058 | 110 | [平衡二叉树](./058-balanced-binary-tree.md) | Easy | A | Early-stop Tree DP |
| 059 | 98 | [验证二叉搜索树](./059-validate-binary-search-tree.md) | Medium | S | Range Invariant / Inorder |
| 060 | 230 | [BST 中第 K 小的元素](./060-kth-smallest-in-bst.md) | Medium | S | Ordered Inorder |
| 061 | 236 | [二叉树最近公共祖先](./061-lowest-common-ancestor-of-a-binary-tree.md) | Medium | S | Recursive Information Merge |
| 062 | 199 | [二叉树右视图](./062-binary-tree-right-side-view.md) | Medium | A | BFS/DFS with Depth |
| 063 | 105 | [前序与中序构造二叉树](./063-construct-binary-tree-from-preorder-and-inorder-traversal.md) | Medium | S | Divide & Conquer + Index Map |
| 064 | 124 | [二叉树中的最大路径和](./064-binary-tree-maximum-path-sum.md) | Hard | S | Tree DP with Global Answer |
| 065 | 314 | [二叉树垂序遍历](./065-binary-tree-vertical-order-traversal.md) | Medium | A | BFS + Column Coordinate |
