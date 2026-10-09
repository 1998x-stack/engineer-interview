# Chapter 08 - asyncio 与结构化并发

从 event loop 到 TaskGroup、取消传播、限流、背压与生产级 worker。

## 仓库增强版：章节深挖

### 深入学习路线

不要从 `async/await` 语法开始背；从 event loop 的 run-to-await 模型开始，再学习 Task 生命周期、取消、结构化并发和 backpressure。

**工具路线**：`asyncio.TaskGroup`、`timeout`、`Queue`、`Semaphore`、debug mode、event-loop lag。

**组合追问**：Q72→Q73→Q74、Q75→Q76、Q79→Q80。

## 本章目标

asyncio 的高阶问题不是 async/await 语法，而是任务所有权、取消传播、超时、背压、资源上限和故障边界。

## 题目列表

- [Q71. concurrency 与 parallelism 有什么区别？](../questions/08-asyncio-concurrency/q71.md) - ★ / 极高
- [Q72. coroutine、Task、Future 分别是什么？](../questions/08-asyncio-concurrency/q72.md) - ★★★ / 极高
- [Q73. await 的核心语义是什么？](../questions/08-asyncio-concurrency/q73.md) - ★★ / 极高
- [Q74. 为什么 async 函数里 time.sleep 是严重问题？](../questions/08-asyncio-concurrency/q74.md) - ★ / 极高
- [Q75. asyncio.gather 与 TaskGroup 怎么选？](../questions/08-asyncio-concurrency/q75.md) - ★★★★ / 极高
- [Q76. 为什么不能随便吞 asyncio.CancelledError？](../questions/08-asyncio-concurrency/q76.md) - ★★★★ / 极高
- [Q77. async code 中如何调用阻塞函数？](../questions/08-asyncio-concurrency/q77.md) - ★★ / 极高
- [Q78. async 能解决 CPU-bound 吗？](../questions/08-asyncio-concurrency/q78.md) - ★★ / 极高
- [Q79. Semaphore 在 async 服务中解决什么问题？](../questions/08-asyncio-concurrency/q79.md) - ★★ / 高
- [Q80. 如何设计一个生产级 asyncio worker？](../questions/08-asyncio-concurrency/q80.md) - ★★★★★ / 极高

## 推荐刷题方式

1. 先用 60 秒口述每题标准回答。
2. 再运行最小实验或自己补实验。
3. 最后只看追问，连续回答 3 层。
4. 把不会的题加入自己的复习清单。
