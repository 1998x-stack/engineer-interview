# 常用复杂度速查

| 操作 | 结构 | 典型复杂度 | 备注 |
|---|---|---:|---|
| append / pop tail | list | 摊还 O(1) | 扩容时单次可 O(n) |
| insert / pop head | list | O(n) | 需要移动引用 |
| index access | list / tuple | O(1) | 连续数组索引 |
| membership | list / tuple | O(n) | 线性扫描 |
| lookup / insert | dict / set | 平均 O(1) | 依赖 hash/equality；最坏可退化 |
| appendleft / popleft | deque | O(1) | 两端队列优势 |
| heap push / pop | heapq | O(log n) | Top-K 常用 |
| sort | list.sort / sorted | O(n log n) | Timsort；输入结构会影响实际表现 |

> 面试中一定注明：**平均 / 摊还 / 最坏**，不要只报一个大 O。
