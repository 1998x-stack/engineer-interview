# Heap / Priority Queue

> 本章覆盖 **059-066**，共 8 题。

## 源书稿章节导语

> Top-K、动态最值、K 路归并、在线中位数与调度。

## 章节能力目标

- Top-K、动态最值、K 路归并和调度优先考虑 Heap；必须讲清堆大小和复杂度中的 k。

## 深化版章节训练目标

**章节核心：** 边界候选、Top-K 与事件驱动

**主要 Pattern：** `Heap / K-way Merge / Two Heaps / Lazy Deletion`

### 面试前的三次检查

1. Heap 规模写成 k/F/S
2. 只放仍可能影响答案的候选
3. 任意删除需单独设计

### 难度分布

- `H`：2 题
- `H+`：1 题
- `M`：3 题
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
| Q059 | [数组第 K 大元素](Q059-数组第-K-大元素.md) | M | Heap / Quickselect |
| Q060 | [距离原点最近的 K 个点](Q060-距离原点最近的-K-个点.md) | M | Heap / Quickselect |
| Q061 | [日志 Top-K 活跃用户，并保留阈值并列者](Q061-日志-Top-K-活跃用户-并保留阈值并列者.md) | M/H | HashMap / Heap |
| Q062 | [Meeting Rooms II：最少会议室](Q062-Meeting-Rooms-II-最少会议室.md) | M | Heap / 区间 |
| Q063 | [K 个有序数组的归并](Q063-K-个有序数组的归并.md) | M/H | Heap / K-way Merge |
| Q064 | [数据流中位数](Q064-数据流中位数.md) | H | Heap / Two Heaps |
| Q065 | [滑动窗口中位数](Q065-滑动窗口中位数.md) | H+ | Two Heaps / Lazy Deletion |
| Q066 | [多服务器任务调度](Q066-多服务器任务调度.md) | H | Heap / 设计 |
