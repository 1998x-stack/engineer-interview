# 复杂度速查

| 结构 | 典型优势 | 典型短板 |
|---|---|---|
| Array | 随机访问 O(1) | 中间插删 O(n) |
| HashMap/Set | 平均查找/插删 O(1) | 最坏 O(n)，依赖 hash/负载因子 |
| Linked List | 已知节点后插删 O(1) | 按位置访问 O(n) |
| Stack/Queue | 端点操作 O(1) | 访问顺序受限 |
| Binary Heap | push/pop O(log n)，peek O(1) | 任意删除/查找不方便 |
| 平衡 BST | 查找/插删 O(log n) | 需保持平衡 |
| Trie | 字符串操作 O(L) | 空间可能较大 |
| DSU | union/find 近 O(1) 摊销 | 不擅长删除边 |
| Fenwick | update/query O(log n) | 操作类型较受限 |
| Segment Tree | query/update O(log n) | 代码与常数更大 |
