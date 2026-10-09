# 第 10 章｜Hopper、Blackwell 与 CUDA 13.x

Cluster/DSM/TMA/TMEM/CUDA Tile 与架构特化优化。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 091 | [Hopper Thread Block Cluster 是什么？](q091.md) |
| 092 | [什么是 Distributed Shared Memory（DSM）？](q092.md) |
| 093 | [TMA 与 `cp.async` 的核心差别是什么？](q093.md) |
| 094 | [为什么 Hopper GEMM 适合 Producer-Consumer Warp Specialization？](q094.md) |
| 095 | [Blackwell Tensor Memory（TMEM）是什么？与 TMA 有什么区别？](q095.md) |
| 096 | [为什么 Blackwell 的 Warp Specialization 不能简单照搬 Hopper？](q096.md) |
| 097 | [CUDA Graph 什么时候能明显提升性能？](q097.md) |
| 098 | [为什么 `cudaMallocAsync` / Stream-Ordered Allocator 更适合高性能程序？](q098.md) |
| 099 | [CUDA Tile C++ / Tile Programming 为什么值得关注？](q099.md) |
| 100 | [给你一个比理论峰值慢 20 倍的 CUDA Kernel，你如何系统优化？](q100.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

第 7-9 章；能阅读 NVIDIA Programming/Tuning/CUTLASS 文档。

### 本章核心因果模型

现代 CUDA 的重点是跨 block 协作、专用数据搬运和新 Tensor Core 数据路径：Cluster/DSM 扩大协作范围，TMA 负责 tensor transfer，TMEM/TCGen05 改变 Blackwell 计算与 accumulator workflow。

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

1. 画 SM90 producer-consumer pipeline
2. 对比 SM90/SM100 CUTLASS recipe
3. CUDA Graph microkernel replay
4. cudaMallocAsync memory-pool benchmark

### 掌握度检查

- [ ] 能严格区分 TMA/TMEM
- [ ] 能解释 Blackwell 为什么不能照搬 Hopper
- [ ] 能用架构特性解决已证实瓶颈而非炫技

### 本章题目矩阵

| # | Question |
|---:|---|
| Q091 | [Hopper Thread Block Cluster 是什么？](q091.md) |
| Q092 | [什么是 Distributed Shared Memory（DSM）？](q092.md) |
| Q093 | [TMA 与 `cp.async` 的核心差别是什么？](q093.md) |
| Q094 | [为什么 Hopper GEMM 适合 Producer-Consumer Warp Specialization？](q094.md) |
| Q095 | [Blackwell Tensor Memory（TMEM）是什么？与 TMA 有什么区别？](q095.md) |
| Q096 | [为什么 Blackwell 的 Warp Specialization 不能简单照搬 Hopper？](q096.md) |
| Q097 | [CUDA Graph 什么时候能明显提升性能？](q097.md) |
| Q098 | [为什么 `cudaMallocAsync` / Stream-Ordered Allocator 更适合高性能程序？](q098.md) |
| Q099 | [CUDA Tile C++ / Tile Programming 为什么值得关注？](q099.md) |
| Q100 | [给你一个比理论峰值慢 20 倍的 CUDA Kernel，你如何系统优化？](q100.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
