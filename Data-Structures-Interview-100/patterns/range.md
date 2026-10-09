# Range Structures

> **一句话：** 动态更新与区间聚合的统一框架

## 1. 核心模型

静态前缀在更新后会失效；Range Structures 通过分层聚合让一次更新只触碰 O(log n) 个摘要。选择 Fenwick / Segment Tree / Ordered Intervals 取决于操作与坐标模型。

## 2. 识别信号

- update + range query
- 动态 kth/rank
- 区间 add/remove/query
- 大量逆序/频次前缀查询

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> 每个树节点/规范区间的摘要与其覆盖范围完全一致；局部更新后所有受影响祖先/相邻区间都被恢复到规范状态。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| Fenwick | 前缀可组合、代码短 | 常数小 |
| Segment Tree | 任意可 merge 聚合 | 可 lazy/persistent |
| Ordered Intervals | 坐标巨大、区间数少 | 操作与受影响区间 k 相关 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- 闭区间/半开区间混用
- Fenwick 0/1-based 下标混乱
- Lazy tag 组合/下推顺序错误
- 坐标压缩后忘记保留区间长度语义

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
