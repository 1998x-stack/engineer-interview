# 第 6 章｜Cache 与存储层次

> **本章目标**：Cache 的本质是用有限的高速 SRAM 保存“未来最可能再次使用”的主存副本。所有设计都围绕命中率、命中延迟、带宽、容量与一致性开销做权衡。

## 能力阶梯

| 层级 | 你应该做到什么 |
|---|---|
| L1 定义 | 30 秒说清术语和目标 |
| L2 机制 | 能画出最小硬件/执行链 |
| L3 定量 | 能用公式、数量级或 PMU 指标分析 |
| L4 边界 | 能指出架构保证与微架构差异 |
| L5 工程 | 能设计 benchmark / profiling 验证假设 |

## 本章核心指标

关注 hit latency、miss rate、miss penalty、MPKI、AMAT、带宽、MLP 与 cache-line 利用率。

```mermaid
flowchart LR
A[Load/Store] --> L1[L1 Cache]
L1 -->|miss| L2[L2]
L2 -->|miss| LLC[LLC]
LLC -->|miss| MC[Memory Controller]
MC --> DRAM[DRAM]
DRAM --> MC --> LLC --> L2 --> L1
```

## 题目索引

| 题号 | 题目 | 难度 | 频率 | PDF 页 |
|---|---|---|---|---:|
| [Q051](q051-cache.md) | 为什么需要 Cache？什么是局部性？ | ★★★★★ | 必考 | 63 |
| [Q052](q052-l1-l2-l3.md) | L1/L2/L3 为何容量越大通常越慢？ | ★★★★★ | 高频 | 64 |
| [Q053](q053-cache-line-64b.md) | Cache Line 是什么？为什么常见为 64B？ | ★★★★★ | 必考 | 65 |
| [Q054](q054-cache-tag-index-offset.md) | Cache 地址中的 Tag/Index/Offset 如何划分？ | ★★★★★ | 必考 | 66 |
| [Q055](q055-question.md) | 直接映射、全相联和组相联如何权衡？ | ★★★★★ | 必考 | 67 |
| [Q056](q056-cache-miss.md) | Cache Miss 有哪些经典类型？ | ★★★★★ | 必考 | 68 |
| [Q057](q057-cache-lru.md) | 为什么真实 Cache 很少做精确 LRU？ | ★★★★☆ | 进阶 | 69 |
| [Q058](q058-write-through-write-back.md) | Write-Through 与 Write-Back 怎么选？ | ★★★★★ | 必考 | 70 |
| [Q059](q059-write-allocate-no-write-allocate.md) | Write-Allocate 与 No-Write-Allocate 有什么区别？ | ★★★★☆ | 高频 | 71 |
| [Q060](q060-amat-miss-rate.md) | AMAT 如何计算？如何判断优化一个 miss rate 值不值得？ | ★★★★★ | 必考 | 72 |

## 学习要求

建议每题完成三轮：

1. **30 秒**：只答结论、机制、边界；
2. **2 分钟**：加入一个公式/最小例子；
3. **5 分钟**：加入架构差异、工程指标与反例。

完成本章后，不应只“认识名词”，而应能把 10 道题连接成一条因果链。
