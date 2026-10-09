# 第 1 章｜CUDA 执行模型与 SIMT

从线程层级映射到 warp/SM 调度与同步语义。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 001 | [Thread、Warp、Block、Grid、SM 分别是什么？](q001.md) |
| 002 | [CUDA 为什么称 SIMT，而不是传统 SIMD？](q002.md) |
| 003 | [为什么 Warp 是 CUDA 性能分析最重要的单位？](q003.md) |
| 004 | [Kernel launch 后，Block 是如何调度到 SM 的？](q004.md) |
| 005 | [为什么 block size 常从 128/256 开始，而不是随便选？](q005.md) |
| 006 | [什么是 Grid-Stride Loop？为什么它是 CUDA 常用模式？](q006.md) |
| 007 | [`__syncthreads()` 到底同步什么？](q007.md) |
| 008 | [CUDA 有哪些同步层级？](q008.md) |
| 009 | [为什么 kernel launch 通常是异步的？如何正确计时？](q009.md) |
| 010 | [为什么 GPU 更偏 throughput，而 CPU 更偏 latency？](q010.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

C/C++ 基础、kernel launch 语法、线程索引。

### 本章核心因果模型

软件抽象 Grid→Block→Thread 必须映射到硬件 GPU→SM→Warp。同步、分支、内存访问与 occupancy 的讨论都从这张映射图出发。

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

1. 用不同 block size 测最后一个 partial warp
2. 写 grid-stride loop 并控制 grid 大小
3. 用 CUDA Event 与 host wall-clock 对比 kernel 计时

### 掌握度检查

- [ ] 能解释 block 为什么不跨 SM
- [ ] 能区分 warp/block/device 同步
- [ ] 能从 grid/block 配置推测 waves 与并行度

### 本章题目矩阵

| # | Question |
|---:|---|
| Q001 | [Thread、Warp、Block、Grid、SM 分别是什么？](q001.md) |
| Q002 | [CUDA 为什么称 SIMT，而不是传统 SIMD？](q002.md) |
| Q003 | [为什么 Warp 是 CUDA 性能分析最重要的单位？](q003.md) |
| Q004 | [Kernel launch 后，Block 是如何调度到 SM 的？](q004.md) |
| Q005 | [为什么 block size 常从 128/256 开始，而不是随便选？](q005.md) |
| Q006 | [什么是 Grid-Stride Loop？为什么它是 CUDA 常用模式？](q006.md) |
| Q007 | [`__syncthreads()` 到底同步什么？](q007.md) |
| Q008 | [CUDA 有哪些同步层级？](q008.md) |
| Q009 | [为什么 kernel launch 通常是异步的？如何正确计时？](q009.md) |
| Q010 | [为什么 GPU 更偏 throughput，而 CPU 更偏 latency？](q010.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
