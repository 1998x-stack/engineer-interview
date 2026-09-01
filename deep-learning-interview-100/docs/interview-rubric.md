# 面试回答评分标准

以 FlashAttention 为例：

| 水平 | 典型回答 | 判定 |
|---|---|---|
| 40 分 | “更快、更省显存。” | 只有标签，没有机制 |
| 60 分 | “分块、kernel fusion，减少中间 attention matrix。” | 知道核心方向 |
| 80 分 | “exact attention；FLOP 阶数未变；关键是 HBM↔SRAM IO、tiling、online softmax。” | 原理+硬件 |
| 90+ | 还能说明何时收益有限，并区分 FlashAttention / GQA / KV Cache / PagedAttention，以及如何用 profiler 验证瓶颈。 | 原理+边界+工程 |

## 通用 90+ 回答结构

1. 结论先行；
2. 数学/shape；
3. 为什么这样设计；
4. 复杂度与资源；
5. trade-off；
6. failure mode；
7. 工程验证或排障。
