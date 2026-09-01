# 双指针与滑动窗口

**核心能力：** Two Pointers / Sliding Window






<!-- CHAPTER-ENRICHMENT-V2:START -->

## 本章训练目标

**主题：单调移动与窗口不变量**。完成本章后，不只要能 AC，还要能在白板上主动完成“基线 → 瓶颈 → invariant → 最优实现 → 证明 → 变体”的完整链路。

- 先写“窗口何时合法”
- 左右指针必须单调前进
- 看到嵌套 while 不要机械判 O(n²)

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
| 011 | 167 | [有序数组两数之和](./011-two-sum-ii.md) | Medium | A | Opposite Pointers |
| 012 | 15 | [三数之和](./012-3sum.md) | Medium | S | Sort + Two Pointers |
| 013 | 11 | [盛最多水的容器](./013-container-with-most-water.md) | Medium | S | Greedy Two Pointers |
| 014 | 42 | [接雨水](./014-trapping-rain-water.md) | Hard | S | Two Pointers / Monotonic Stack |
| 015 | 3 | [无重复字符的最长子串](./015-longest-substring-without-repeating-characters.md) | Medium | S | Variable Window |
| 016 | 424 | [替换后的最长重复字符](./016-longest-repeating-character-replacement.md) | Medium | A | Window Invariant |
| 017 | 76 | [最小覆盖子串](./017-minimum-window-substring.md) | Hard | S | Need/Have Sliding Window |
| 018 | 438 | [找到字符串中所有字母异位词](./018-find-all-anagrams-in-a-string.md) | Medium | A | Fixed Window |
| 019 | 209 | [长度最小的子数组](./019-minimum-size-subarray-sum.md) | Medium | A | Positive-number Window |
| 020 | 239 | [滑动窗口最大值](./020-sliding-window-maximum.md) | Hard | S | Monotonic Deque |
