# 第 3 章｜Global Memory 与 Coalescing

把 warp 地址模式翻译成 memory transactions 与有效带宽。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 021 | [什么叫 Global Memory Coalescing？](q021.md) |
| 022 | [32 个线程连续读 32 个 float，理想需要多少 transaction？](q022.md) |
| 023 | [什么是 Misaligned Access？现代 GPU 上为什么仍要关注？](q023.md) |
| 024 | [为什么 Strided Access 很危险？](q024.md) |
| 025 | [AoS 与 SoA 哪个更适合 CUDA？](q025.md) |
| 026 | [Vectorized Load/Store（如 float4）什么时候有收益？](q026.md) |
| 027 | [为什么 Matrix Transpose 是经典 CUDA 优化题？](q027.md) |
| 028 | [Effective Bandwidth 怎么计算？](q028.md) |
| 029 | [Requested Bandwidth 与 Actual DRAM Bandwidth 有什么区别？](q029.md) |
| 030 | [一个 Memory-Bound Kernel 最常见的优化方向有哪些？](q030.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

Warp 概念、memory hierarchy、基本地址计算。

### 本章核心因果模型

把一个 warp 的 32 个地址写出来，再计算覆盖多少 memory sectors；requested bytes 与 actual bytes 的比值是理解 coalescing 的最直接入口。

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

1. stride=1..64 memory microbenchmark
2. offset=0..31 misalignment sweep
3. AoS/SoA/AoSoA 对比

### 掌握度检查

- [ ] 能口算连续 float 的 sector 数
- [ ] 能解释高 DRAM throughput 仍可能低效
- [ ] 能给 layout 重构方案

### 本章题目矩阵

| # | Question |
|---:|---|
| Q021 | [什么叫 Global Memory Coalescing？](q021.md) |
| Q022 | [32 个线程连续读 32 个 float，理想需要多少 transaction？](q022.md) |
| Q023 | [什么是 Misaligned Access？现代 GPU 上为什么仍要关注？](q023.md) |
| Q024 | [为什么 Strided Access 很危险？](q024.md) |
| Q025 | [AoS 与 SoA 哪个更适合 CUDA？](q025.md) |
| Q026 | [Vectorized Load/Store（如 float4）什么时候有收益？](q026.md) |
| Q027 | [为什么 Matrix Transpose 是经典 CUDA 优化题？](q027.md) |
| Q028 | [Effective Bandwidth 怎么计算？](q028.md) |
| Q029 | [Requested Bandwidth 与 Actual DRAM Bandwidth 有什么区别？](q029.md) |
| Q030 | [一个 Memory-Bound Kernel 最常见的优化方向有哪些？](q030.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
