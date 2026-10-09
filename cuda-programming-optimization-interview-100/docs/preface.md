# 前言：这不是一本“背答案”的 CUDA 题库

CUDA 面试最常见的误区，是把大量术语背成孤立结论：shared memory 很快、occupancy 越高越好、atomic 很慢、256 threads 最优。真正的高阶面试会继续追问：**为什么？在什么条件下？用什么 profiler 指标证明？如果换到 Hopper / Blackwell 还成立吗？**

本仓库以 100 道题为骨架，每道题按照“考察意图 → 思路拆解 → 标准回答 → Gotchas → 追问”保留 PDF 基线，并增加深入分析、性能验证和架构视角。Reduction、Scan、Histogram、Transpose、GEMM 等 coding 题提供可讨论的 CUDA C++ 骨架；Nsight、Roofline、TMA、warp specialization、TMEM、CUDA Tile 等题强调性能因果链。

## 真题口径

- 少数问题可以在公开面经中直接核验，例如 synchronization、reduction、memory hierarchy、software pipelining、warp specialization。
- 其余问题按 CUDA/GPU 岗长期高频考点构造成“真题型问题”。
- 不把无法核验的问题虚构成某家公司逐字原题。

## 30 秒回答法

先给一句结论，再给 3 个关键因果点；面试官继续追问时，再进入硬件 transaction、资源约束、代码和 profiler 证据。

## 当前技术口径

- CUDA Toolkit 13.3 Programming / Best Practices 文档作为 PDF 基础口径。
- 经典优化：coalescing、shared-memory reuse、bank conflict、occupancy、register/spill、asynchronous copy。
- Hopper：Thread Block Cluster、DSM、TMA、异步 barrier 与 warp-specialized pipeline。
- Blackwell：TCGen05、TMEM、CUTLASS/CuTe 新数据路径与新 warp-specialization 结构。
- 性能诊断：Nsight Systems → Nsight Compute → Roofline/SOL → stalls/resource/traffic 因果闭环。
