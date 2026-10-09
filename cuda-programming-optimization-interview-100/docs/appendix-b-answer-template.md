# 附录 B｜面试答题模板：30 秒 / 2 分钟 / 深挖

## 30 秒：先给结论

> **模板**：“结论是 X。核心原因有三点：A 决定了硬件事务，B 影响资源/并行度，C 决定最终是否能隐藏延迟。实际我会用 profiler 的 Y/Z 指标验证。”

## 2 分钟：给因果链

1. 定义问题与作用域：warp / block / device？
2. 建立资源/数据流模型：数据在哪一层、一次搬多少 bytes、需要多少同步？
3. 指出主要 trade-off：memory vs compute、register vs occupancy、reuse vs shared capacity。
4. 给出优化动作，并说明为什么它针对这个瓶颈。
5. 说明 profiler 如何验证。

## 深挖：现场被追问时

- 主动给一个反例：说明某个“常见结论”在哪些条件下不成立。
- 给一段最小代码或地址映射，避免停留在口号。
- 把架构代际差异说清：Ampere `cp.async`、Hopper TMA/cluster、Blackwell TMEM/TCGen05。
- 如果不确定某个微架构常数，不猜数字；说明应查 Programming Guide / compute capability table，再给不依赖常数的分析方法。
