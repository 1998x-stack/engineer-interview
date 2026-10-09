# 20 条高分面试原则

1. 先区分 Python 语言规范与 CPython 实现细节。
2. 复杂度一定注明平均、摊还还是最坏。
3. 参数传递用“对象共享/名字绑定”解释，不用含混的“引用传递”。
4. 可变性、哈希性、身份、相等是四个不同概念。
5. 默认参数与闭包题都要问“何时绑定/何时求值”。
6. descriptor 是 property、method binding、ORM field 的共同底层协议。
7. super 沿 MRO 继续查找，不等于固定调用直接父类。
8. generator 的价值是惰性和状态暂停，不等于异步。
9. 资源释放使用 context manager，不依赖 GC 时机。
10. RSS 不下降不自动等于 Python 对象泄漏。
11. GIL 不等于业务线程安全。
12. 2026 回答 GIL 必须补充 free-threaded build。
13. 并发模型选择先分类 workload，再看通信/隔离成本。
14. async def 不会把内部 blocking 代码自动变成非阻塞。
15. TaskGroup 的价值是任务所有权和失败/取消传播。
16. 取消是控制流，cleanup 后通常继续传播 CancelledError。
17. type hints 是静态契约，不是默认 runtime validation。
18. mock 边界而不是 mock 每个实现细节。
19. 性能优化先 profile，算法/I/O 次数通常优先于微优化。
20. 系统设计答案必须包含 backpressure、timeout、容量隔离和 observability。
