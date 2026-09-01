# Sliding Window

**识别信号：** 连续子串、最长最短、至多 K
**核心原则：** 右端扩张、左端恢复合法性；首先写出窗口合法条件。

## 面试推导顺序

1. 先写一个正确基线并指出重复工作。
2. 明确这个模式依赖的单调性、状态复用或结构不变量。
3. 写出更新顺序和边界。
4. 用一个反例检查“为什么不能换一种移动/更新方式”。
5. 解释复杂度来自每个元素/状态被处理的次数。






<!-- PATTERN-ENRICHMENT-V2:START -->

## Pattern 深度理解

### 什么时候应该想到它

识别信号：**连续子串、最长最短、至多 K**。但不要只做关键词匹配：真正判断依据是题目是否存在与该模式一致的**信息复用方式或单调结构**。

### 不变量优先

> 右端扩张、左端恢复合法性；首先写出窗口合法条件。

面试里最重要的不是说出 “我用 Sliding Window”，而是把容器中的每个元素、指针边界或 DP 状态的语义说精确。

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

- [015. LC3 无重复字符的最长子串](../../problems/02-two-pointers-sliding-window/015-longest-substring-without-repeating-characters.md) - `Variable Window`
- [016. LC424 替换后的最长重复字符](../../problems/02-two-pointers-sliding-window/016-longest-repeating-character-replacement.md) - `Window Invariant`
- [017. LC76 最小覆盖子串](../../problems/02-two-pointers-sliding-window/017-minimum-window-substring.md) - `Need/Have Sliding Window`
- [018. LC438 找到字符串中所有字母异位词](../../problems/02-two-pointers-sliding-window/018-find-all-anagrams-in-a-string.md) - `Fixed Window`
- [019. LC209 长度最小的子数组](../../problems/02-two-pointers-sliding-window/019-minimum-size-subarray-sum.md) - `Positive-number Window`
- [020. LC239 滑动窗口最大值](../../problems/02-two-pointers-sliding-window/020-sliding-window-maximum.md) - `Monotonic Deque`

## 进一步训练

- 把“求是否存在”改成“计数/最短/最长/返回路径”。
- 增加重复值、负数、在线更新或内存限制。
- 不看代码，用 90 秒说明：基线 -> 瓶颈 -> 不变量 -> 正确性 -> 复杂度。
