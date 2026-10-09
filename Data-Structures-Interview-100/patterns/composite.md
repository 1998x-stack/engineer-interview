# Composite Data Structure Design

> **一句话：** 从 API 的 primitive operation 复杂度反推结构组合

## 1. 核心模型

先把 API 拆成“定位、插删、顺序、随机、极值、时间”等 primitive，再用不同结构分别满足。最终难点是跨结构一致性，而不是某个单独数据结构。

## 2. 识别信号

- 多个 API 都要求 O(1)/O(log n)
- 既要 key lookup 又要 eviction/order
- 既要随机访问又要 O(1) 删除
- 缓存/计数/时间窗口/文件系统设计

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> 每个逻辑对象在所有辅助索引中的表示保持一一对应；一次 API 操作结束后所有索引与顺序结构同时反映新状态。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| Hash + DLL | LRU/recency | 定位 + O(1) move/remove |
| Hash + Array | RandomizedSet | lookup + O(1) swap-delete |
| Hash + Buckets | LFU/All O(1) | 按 count 局部分桶 |
| Heap + Hash | 时间/优先级 | 允许 O(log n) 简化实现 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- 只更新主结构忘记辅助索引
- sentinel/minFreq 等冗余状态失同步
- 复杂度目标写出来但没逐 API 证明
- 把算法题无限扩成系统设计而失焦

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
