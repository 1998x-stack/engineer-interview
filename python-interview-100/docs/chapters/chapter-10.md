# Chapter 10 - 性能优化、Web 后端与系统设计

把语言知识落到 profiling、内存、流处理、缓存和高并发 API 的综合场景。

## 仓库增强版：章节深挖

### 深入学习路线

本章统一采用“测量驱动”方法。先给 workload 和 SLO，再给瓶颈证据，再做算法/并发/框架选择。没有指标的性能结论只能算猜测。

**工具路线**：`cProfile`、`py-spy`、`tracemalloc`、load test、p95/p99、DB/连接池指标。

**组合追问**：Q91→Q94 是诊断链，Q95→Q96 是 Web 框架链，Q97-Q100 是算法与系统设计链。

## 本章目标

性能优化必须从测量开始；系统设计必须把吞吐、尾延迟、容量隔离、背压、可观测性和故障恢复放在同一张图里讨论。

## 题目列表

- [Q91. Python 程序慢，第一步该做什么？](../questions/10-performance-backend-design/q91.md) - ★★ / 极高
- [Q92. list comprehension 为什么经常比显式 for 更快？](../questions/10-performance-backend-design/q92.md) - ★★ / 中
- [Q93. 为什么 NumPy 往往比 Python for loop 快很多？](../questions/10-performance-backend-design/q93.md) - ★★★ / 极高
- [Q94. 如何系统定位 Python memory leak？](../questions/10-performance-backend-design/q94.md) - ★★★★ / 极高
- [Q95. Django / Flask / FastAPI 应如何选择？](../questions/10-performance-backend-design/q95.md) - ★★★ / 高
- [Q96. FastAPI async def endpoint 为什么仍可能很慢？](../questions/10-performance-backend-design/q96.md) - ★★★ / 极高
- [Q97. 手写 LRU Cache，为什么常用 HashMap + Doubly Linked List？](../questions/10-performance-backend-design/q97.md) - ★★★★ / 极高
- [Q98. 100GB 日志不能进内存，如何处理？](../questions/10-performance-backend-design/q98.md) - ★★★ / 极高
- [Q99. 1 亿 URL 找 Top-K，如何设计？](../questions/10-performance-backend-design/q99.md) - ★★★★ / 高
- [Q100. 设计高并发 Python API，如何选择整体并发模型？](../questions/10-performance-backend-design/q100.md) - ★★★★★ / 极高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
