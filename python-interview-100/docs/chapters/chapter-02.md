# Chapter 02 - 核心容器与哈希表

从 list/tuple/dict/set 的 API 进入复杂度、哈希契约、拷贝语义与工程选择。

## 仓库增强版：章节深挖

### 深入学习路线

本章必须同时掌握 **抽象数据类型语义** 与 **CPython 数据结构实现**。复习时把每个容器写成四列：底层结构、核心操作复杂度、退化条件、适用 workload。

**源码路线**：`Objects/listobject.c`、`tupleobject.c`、`dictobject.c`、`setobject.c`。

**组合追问**：Q14→Q15→Q16 是哈希契约主线；Q12→Q13 是动态数组成本主线。

## 本章目标

回答容器题时，必须同时给出数据结构、典型复杂度、语义约束与内存代价；不要只背 API。

## 题目列表

- [Q11. list 和 tuple 的区别是什么？](../questions/02-containers-hashing/q11.md) - ★ / 极高
- [Q12. list.append 为什么是摊还 O(1)？](../questions/02-containers-hashing/q12.md) - ★★ / 高
- [Q13. 为什么 list.insert(0, x) / pop(0) 慢？](../questions/02-containers-hashing/q13.md) - ★ / 高
- [Q14. Python dict 查找为什么平均 O(1)？](../questions/02-containers-hashing/q14.md) - ★★★ / 极高
- [Q15. 什么对象可以作为 dict key？](../questions/02-containers-hashing/q15.md) - ★★ / 极高
- [Q16. 为什么实现 __eq__ 后必须认真考虑 __hash__？](../questions/02-containers-hashing/q16.md) - ★★★ / 高
- [Q17. dict 是否保证插入顺序？](../questions/02-containers-hashing/q17.md) - ★ / 高
- [Q18. dict.get、setdefault、defaultdict 如何选择？](../questions/02-containers-hashing/q18.md) - ★★ / 高
- [Q19. set 为什么能高效查重？](../questions/02-containers-hashing/q19.md) - ★ / 极高
- [Q20. 浅拷贝和深拷贝有什么区别？](../questions/02-containers-hashing/q20.md) - ★★ / 极高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
