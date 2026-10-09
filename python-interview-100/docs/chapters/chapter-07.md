# Chapter 07 - 线程、进程、GIL 与多核并行

掌握经典 GIL 模型，并覆盖 Python 3.14 的 free-threaded 与 InterpreterPoolExecutor。

## 仓库增强版：章节深挖

### 深入学习路线

2026 年面试必须避免旧版 GIL 绝对话术。使用统一成本矩阵比较 default GIL、free-threaded、thread、process、subinterpreter。

**版本基线**：Python 3.14 POSIX multiprocessing 默认 start method 为 `forkserver`；free-threaded 仍是可选构建；`InterpreterPoolExecutor` 已进入标准库。

**组合追问**：Q61→Q62→Q63、Q64→Q67→Q68、Q69→Q70。

## 本章目标

并发选择是成本模型：CPU/I/O 比例、共享状态、序列化、隔离、第三方扩展兼容与部署模型共同决定方案。

## 题目列表

- [Q61. GIL 是什么？如何用现代版本回答？](../questions/07-threads-processes-gil/q61.md) - ★★★ / 极高
- [Q62. “有 GIL 所以不需要锁”为什么是错的？](../questions/07-threads-processes-gil/q62.md) - ★★★ / 极高
- [Q63. Python 3.14 free-threaded CPython 改变了什么？](../questions/07-threads-processes-gil/q63.md) - ★★★★★ / 高
- [Q64. Thread vs Process 应该怎么选？](../questions/07-threads-processes-gil/q64.md) - ★★★ / 极高
- [Q65. 多进程的主要代价是什么？](../questions/07-threads-processes-gil/q65.md) - ★★ / 高
- [Q66. multiprocessing 为什么经常出现 pickle error？](../questions/07-threads-processes-gil/q66.md) - ★★★ / 高
- [Q67. ThreadPoolExecutor 与 ProcessPoolExecutor 的关键差异？](../questions/07-threads-processes-gil/q67.md) - ★★ / 极高
- [Q68. fork、spawn、forkserver 有什么区别？](../questions/07-threads-processes-gil/q68.md) - ★★★★ / 高
- [Q69. 什么是 race condition？如何系统治理？](../questions/07-threads-processes-gil/q69.md) - ★★ / 极高
- [Q70. Python 3.14 InterpreterPoolExecutor 是什么？](../questions/07-threads-processes-gil/q70.md) - ★★★★★ / 高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
