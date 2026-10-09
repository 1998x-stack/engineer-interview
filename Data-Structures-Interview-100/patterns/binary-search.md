# Binary Search

> **一句话：** 基于单调判定函数每次排除一半搜索空间

## 1. 核心模型

二分的核心不是 `while lo <= hi` 模板，而是找到单调 predicate，并明确答案位于 predicate 从 False→True 或 True→False 的边界。

## 2. 识别信号

- 输入有序/局部有序
- 求最小可行值/最大不可行值
- 答案域可被单调验证
- partition 条件

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> 每轮开始时答案仍处于当前候选区间；一次判定能安全排除整个半区。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| Index Binary Search | 直接在有序数组找值 | O(log n) |
| Boundary Search | first/last true | 最常见 off-by-one |
| Answer-space Search | 搜索答案而非元素 | 需要 `check(mid)` 单调 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- 先背模板后猜边界
- 没有证明 predicate 单调
- 旋转/重复值时仍假设严格有序
- 忘记在短数组上二分 partition 类问题

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
