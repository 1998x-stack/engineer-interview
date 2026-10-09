# Heap / Top-K

> **一句话：** 只维护当前最重要的边界候选，而不是完整排序

## 1. 核心模型

Heap 的价值来自只关心极值/Top-K 边界。size-k heap 的堆顶通常是“当前第 k 阈值”；K-way merge 中堆顶则是所有有序源的下一全局候选。

## 2. 识别信号

- Top-K
- K 路归并
- 动态最值
- 在线中位数
- 调度/最早完成事件

遇到题目时先问：**如果不用这个 Pattern，基线方案正在重复做什么？** Pattern 的价值必须能对应到一类被消除的重复工作。

## 3. 不变量模板

> Heap 中只保留所有尚可能影响下一输出/最终阈值的候选；堆顶是当前结构定义下最先需要处理的边界。

建议把不变量写到代码旁边，并用“初始化 → 保持 → 终止”三步证明，而不是只背操作模板。

## 4. 结构选择对照

| 结构 / 方法 | 最适合 | 关键 Trade-off |
|---|---|---|
| Full Sort | 需要完整排序结果 | O(n log n) |
| Size-K Heap | 只需 Top-K | O(n log k) |
| Quickselect | 静态 kth/Top-K 无序 | 平均 O(n) |
| Balanced Tree | 需要删除任意元素/顺序统计 | O(log n) 更新 |

## 5. 复杂度表达

不要只写一个 `O(n)`。至少明确：

- 主规模是 `n`、`V/E`、字符串长度 `L`、窗口 `W`、候选数 `k` 中的哪一个；
- 是 worst-case、average 还是 amortized；
- 是否有排序、建索引、坐标压缩等 preprocessing；
- 输出本身若有 `m` 项，是否存在 `Ω(m)` 下界；
- 递归栈、Heap/Trie 节点、缓存副本是否计入 auxiliary space。

## 6. 高频误区

- Python heap 比较对象无 tie-break
- 把 O(log n) 写成 O(log k)
- Heap 不支持任意删除却直接 remove
- 双堆平衡用物理长度而忽略 lazy 元素

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
