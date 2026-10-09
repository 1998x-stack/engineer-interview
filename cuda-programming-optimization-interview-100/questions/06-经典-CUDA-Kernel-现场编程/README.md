# 第 6 章｜经典 CUDA Kernel 现场编程

Reduction、Scan、Histogram、Transpose、GEMM、Compaction。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 051 | [现场手写一个高性能 Reduction：你会如何逐版优化？](q051.md) |
| 052 | [为什么最原始 Interleaved Reduction 很慢？](q052.md) |
| 053 | [Reduction 最后一 Warp 为什么适合用 Shuffle？](q053.md) |
| 054 | [手写 Parallel Scan / Prefix Sum：Hillis-Steele 与 Blelloch 如何比较？](q054.md) |
| 055 | [Parallel Histogram 如何优化 Atomic Contention？](q055.md) |
| 056 | [现场写 Optimized Matrix Transpose。](q056.md) |
| 057 | [手写 Tiled Matrix Multiplication，并解释为什么快。](q057.md) |
| 058 | [为什么 GEMM Tile 越大不一定越快？](q058.md) |
| 059 | [如何实现 Stream Compaction？](q059.md) |
| 060 | [Top-K / Sort / Selection 什么时候不应该自己写 CUDA？](q060.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

前五章全部基础；能独立写 CUDA kernel。

### 本章核心因果模型

每道现场 coding 题都按 Correct→Coalesced→Reuse→Less Sync/Divergence→Warp Primitive→Architecture/Library Baseline 的版本演进回答。

### 推荐学习顺序

```text
概念定义
  ↓
白板地址/线程/数据流
  ↓
定量模型
  ↓
正确 baseline
  ↓
单变量优化
  ↓
Nsight 证据
  ↓
架构迁移检查
```

### 必做实验

1. Reduction V0-V5
2. Blelloch scan
3. shared histogram
4. optimized transpose
5. tiled GEMM

### 掌握度检查

- [ ] 白板写出边界正确版本
- [ ] 每一版能说清减少了什么成本
- [ ] 知道何时停止手写并调用 CUB/cuBLAS

### 本章题目矩阵

| # | Question |
|---:|---|
| Q051 | [现场手写一个高性能 Reduction：你会如何逐版优化？](q051.md) |
| Q052 | [为什么最原始 Interleaved Reduction 很慢？](q052.md) |
| Q053 | [Reduction 最后一 Warp 为什么适合用 Shuffle？](q053.md) |
| Q054 | [手写 Parallel Scan / Prefix Sum：Hillis-Steele 与 Blelloch 如何比较？](q054.md) |
| Q055 | [Parallel Histogram 如何优化 Atomic Contention？](q055.md) |
| Q056 | [现场写 Optimized Matrix Transpose。](q056.md) |
| Q057 | [手写 Tiled Matrix Multiplication，并解释为什么快。](q057.md) |
| Q058 | [为什么 GEMM Tile 越大不一定越快？](q058.md) |
| Q059 | [如何实现 Stream Compaction？](q059.md) |
| Q060 | [Top-K / Sort / Selection 什么时候不应该自己写 CUDA？](q060.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
