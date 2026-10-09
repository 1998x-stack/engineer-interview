# Trie

> **一句话：** 共享字符串/路径前缀，把多查询重复前缀扫描变成树遍历

## 1. 核心模型

Trie 节点不是“一个单词”，而是一个前缀状态。terminal、children、计数/Top-K cache 等增强字段分别承担不同语义。

## 2. 识别信号

- prefix 查询
- 多个词共享前缀
- wildcard DFS
- autocomplete
- 层级 path/domain

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> 根到当前节点的边标签恰好等于当前前缀；不存在 child 就意味着词典中不存在任何以该前缀开头的目标。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| HashSet | 完整词 membership | 前缀能力弱 |
| Sorted List + Binary Search | 静态前缀范围 | 更紧凑但更新较贵 |
| Trie | 在线 prefix/DFS 剪枝 | 空间取决于不同前缀数 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- 节点存在误当完整词存在
- alphabet 大却用巨大定长 children
- Top-K cache 忽略更新成本
- Word Search 找到词后不去重/不剪枝

## 7. 面试推导模板

1. 给出一个一定正确的 baseline。
2. 指出 baseline 里最贵的重复工作。
3. 说明本 Pattern 利用了什么性质：有序、单调、前缀、局部聚合、等价类或 API 局部性。
4. 写出只包含“未来充分信息”的状态。
5. 用 invariant 证明一次更新安全。
6. 给出复杂度，并点名隐藏参数。
7. follow-up 时先指出被改变的前提，再局部替换结构。

## 8. 对应题目



## 9. 训练方式

- **Pattern-first：** 随机抽本页任意两题，不看答案先写同一个不变量模板如何实例化。
- **Contrastive：** 选一个“看起来也能做”的替代结构，解释它在哪个 API/约束上更差。
- **Follow-up-only：** 只看追问，练习判断“哪个前提失效”。
- **Complexity audit：** 检查代码里有没有 hidden `sort`、slice、linear delete、重复 DFS。
