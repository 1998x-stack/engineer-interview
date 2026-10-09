# Hash Lookup

> **一句话：** 把反复线性搜索变成索引查询

## 1. 核心模型

把历史信息压缩成 `key -> minimal state`。真正的设计问题不是“要不要 Hash”，而是 **key 如何定义、value 保存什么、什么时候写入/删除**。

## 2. 识别信号

- 对每个元素都在历史/后缀里找另一个对象
- 需要频次、去重、反向索引或 O(1) 平均 membership
- 暴力复杂度里出现重复的线性查找

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> 处理到位置 i 时，Hash 只包含已经合法处理的历史状态；当前查询若在历史中存在，必能通过其 canonical key 命中。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| HashSet | 只关心存在性/去重 | 不保存额外元数据 |
| HashMap | 需要 index/frequency/node 等 | 平均 O(1) lookup |
| Sorting | 可牺牲顺序换确定有序扫描 | O(n log n) 但避免 hash 最坏退化 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- 把平均 O(1) 说成严格最坏 O(1)
- key 构造本身可能是 O(L)
- 需要下标却只保存 bool
- hash 相等后忘记 key equality

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
