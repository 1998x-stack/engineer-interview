# 复合数据结构设计

> 本章覆盖 **093-100**，共 8 题。

## 源书稿章节导语

> 把单一结构的短板通过组合补齐，并用 invariant 驱动 API 复杂度设计。

## 章节能力目标

- 逐个写出 API 的目标复杂度，再找单一结构无法满足的地方，最后组合 Hash、链表、堆、桶、树或环形数组。

## 深化版章节训练目标

**章节核心：** 从 API 复杂度反推结构组合

**主要 Pattern：** `Hash + DLL / Buckets / Array / Heap / Ring Buffer`

### 面试前的三次检查

1. 逐 API 拆 primitive operation
2. 给跨结构一致性 invariant
3. 先正确再谈并发/分布式扩展

### 难度分布

- `H`：4 题
- `H+`：1 题
- `M`：1 题
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
| Q093 | [LRU Cache](Q093-LRU-Cache.md) | M/H | HashMap / Doubly Linked List |
| Q094 | [LFU Cache](Q094-LFU-Cache.md) | H | HashMap / Frequency Buckets |
| Q095 | [Time Based Key-Value Store](Q095-Time-Based-Key-Value-Store.md) | M | HashMap / Binary Search |
| Q096 | [All O(1) Data Structure](Q096-All-O-1-Data-Structure.md) | H+ | HashMap / Bucket DLL |
| Q097 | [RandomizedCollection：允许重复的 O(1) 随机集合](Q097-RandomizedCollection-允许重复的-O-1-随机集合.md) | H | Array / HashMap |
| Q098 | [简化 Twitter News Feed](Q098-简化-Twitter-News-Feed.md) | H | HashMap / Heap |
| Q099 | [设计内存文件系统](Q099-设计内存文件系统.md) | H | Trie / Tree |
| Q100 | [Hit Counter：最近 5 分钟请求计数](Q100-Hit-Counter-最近-5-分钟请求计数.md) | M/H | Queue / Circular Buffer |
