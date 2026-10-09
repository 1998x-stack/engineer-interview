# HashMap / HashSet

> 本章覆盖 **016-023**，共 8 题。

## 源书稿章节导语

> 理解 O(1) lookup 的价值，也理解它只是平均复杂度；从应用走到底层冲突与扩容。

## 章节能力目标

- 明确平均 O(1) 与最坏 O(n) 的区别，说明 key 设计、冲突、负载因子以及是否需要保存下标/频次/最后位置。

## 深化版章节训练目标

**章节核心：** Key 设计、冲突与空间换时间

**主要 Pattern：** `Frequency / Reverse Index / Set / Sparse Representation`

### 面试前的三次检查

1. 先定义 key 的语义
2. 区分 membership 与 metadata
3. 把 average O(1) 与 worst-case 分开

### 难度分布

- `E`：1 题
- `E/M`：1 题
- `M`：6 题

### 推荐训练顺序

1. **基础结构题**：先练接口与基本不变量，不追求花哨优化。
2. **Pattern 题**：把同一结构的 2–3 题连续做，找共同状态定义。
3. **Hard/变体题**：只看约束，不看题名，练从 baseline 推 structure。
4. **Follow-up 复盘**：不重写整题，只回答“哪个前提变了、哪一层结构要换”。

> 章节 README 只负责能力地图；真正的证明、代码审查与对抗测试都在各 `Qxxx.md` 的 §12 专业深化中。

## 题目列表

| ID | 题目 | 难度 | 核心 |
|---|---|---|---|
| Q016 | [有效字母异位词](Q016-有效字母异位词.md) | E | Hash / 计数 |
| Q017 | [按字母异位词分组](Q017-按字母异位词分组.md) | M | Hash / 字符串签名 |
| Q018 | [最长连续整数序列](Q018-最长连续整数序列.md) | M | HashSet / 集合 |
| Q019 | [K 距离内是否存在重复值](Q019-K-距离内是否存在重复值.md) | E/M | HashMap / 滑动集合 |
| Q020 | [O(1) Insert/Delete/GetRandom 集合](Q020-O-1-Insert-Delete-GetRandom-集合.md) | M | 设计 / HashMap |
| Q021 | [从零实现 HashMap](Q021-从零实现-HashMap.md) | M | HashMap / 底层实现 |
| Q022 | [Hash Collision、负载因子与复杂度退化](Q022-Hash-Collision、负载因子与复杂度退化.md) | M | HashMap / 理论 |
| Q023 | [稀疏向量点积](Q023-稀疏向量点积.md) | M | HashMap / 双指针 |
