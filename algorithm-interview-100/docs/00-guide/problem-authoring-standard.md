# Problem Markdown Authoring Standard / 题目页撰写标准

每个问题页不是题解博客，而是“面试训练单元”。新增/修改题目至少满足：

1. 不复制 LeetCode 完整受版权保护题面，只做必要概括并链接原题。
2. 必须有 baseline，并解释 baseline 的瓶颈。
3. 必须给出精确 invariant / state semantics。
4. 至少比较 2 种方案；S 级核心题建议 3–4 种。
5. 正确性说明包含初始化、保持性、不漏解、终止四部分中的适用项。
6. 复杂度必须拆出排序、Heap/Hash、递归栈、输出空间、期望/平均语义。
7. 至少有一条 bug 定向测试，而不是只抄官方样例。
8. Follow-up 至少覆盖：边界/证明、替代算法、经典变体、工程放大。
9. 工程化部分优先讨论 streaming、memory bound、sharding、approximation、P99 latency。
10. 最后必须有 Active Recall 卡片和复盘 checklist。

## S 级题额外要求

- 能在 15–25 分钟 live coding 完成；
- 能解释为什么错误方案失败；
- 能从题目继续升级到算法系统；
- 代码优先可读性和 invariant 对齐，而不是追求极端 code golf。
