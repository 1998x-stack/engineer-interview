# Backtracking

**识别信号：** 所有方案、排列组合、放置、剪枝
**核心原则：** 选择 -> 递归 -> 撤销；剪枝必须保证只删除不可能产生合法解的分支。

## 面试推导顺序

1. 先写一个正确基线并指出重复工作。
2. 明确这个模式依赖的单调性、状态复用或结构不变量。
3. 写出更新顺序和边界。
4. 用一个反例检查“为什么不能换一种移动/更新方式”。
5. 解释复杂度来自每个元素/状态被处理的次数。






<!-- PATTERN-ENRICHMENT-V2:START -->

## Pattern 深度理解

### 什么时候应该想到它

识别信号：**所有方案、排列组合、放置、剪枝**。但不要只做关键词匹配：真正判断依据是题目是否存在与该模式一致的**信息复用方式或单调结构**。

### 不变量优先

> 选择 -> 递归 -> 撤销；剪枝必须保证只删除不可能产生合法解的分支。

面试里最重要的不是说出 “我用 Backtracking”，而是把容器中的每个元素、指针边界或 DP 状态的语义说精确。

### 正确性证明模板

1. 初始化时 invariant 成立；
2. 每次更新后 invariant 仍成立；
3. 被删除/跳过/合并的候选不可能影响最终最优解；
4. 终止时已覆盖全部需要考虑的候选。

### 复杂度分析模板

- 先数**状态数量**；
- 再数**每个状态被访问/入栈/出栈/松弛/转移的次数**；
- 单独计入排序、Hash、Heap、递归栈和输出空间；
- 随机算法区分 worst / average / expected。

### 失败条件：什么时候不要硬套

- 关键单调性不存在；
- 输入的更新方式破坏了静态假设；
- 为了套模板引入比基线更多的状态；
- 不能清楚说明丢弃信息为什么安全；
- 复杂度看似更好，但排序/预处理/内存成本被漏算。

### 工程化追问

完成一道代表题后至少追加三个问题：**数据变成流怎么办？内存只有 1/100 怎么办？数据分片以后哪些状态可以 merge？** 这三问能把刷题模式迁移到算法系统。

<!-- PATTERN-ENRICHMENT-V2:END -->

## 代表题

- [078. LC78 子集](../../problems/09-backtracking-trie/078-subsets.md) - `Backtracking Decision Tree`
- [079. LC46 全排列](../../problems/09-backtracking-trie/079-permutations.md) - `Backtracking with Used Set`
- [080. LC39 组合总和](../../problems/09-backtracking-trie/080-combination-sum.md) - `Backtracking + Reuse`
- [081. LC90 子集 II](../../problems/09-backtracking-trie/081-subsets-ii.md) - `Sort + Same-level Dedup`
- [082. LC79 单词搜索](../../problems/09-backtracking-trie/082-word-search.md) - `Grid Backtracking`
- [083. LC131 分割回文串](../../problems/09-backtracking-trie/083-palindrome-partitioning.md) - `Partition Backtracking`
- [084. LC51 N 皇后](../../problems/09-backtracking-trie/084-n-queens.md) - `Constraint Backtracking`
- [086. LC698 划分为 K 个相等子集](../../problems/09-backtracking-trie/086-partition-to-k-equal-sum-subsets.md) - `Backtracking + Strong Pruning`

## 进一步训练

- 把“求是否存在”改成“计数/最短/最长/返回路径”。
- 增加重复值、负数、在线更新或内存限制。
- 不看代码，用 90 秒说明：基线 -> 瓶颈 -> 不变量 -> 正确性 -> 复杂度。
