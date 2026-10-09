# 第 4 章｜Shared Memory、Warp 与 Divergence

掌握 bank mapping、warp-level primitive 与控制流效率。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 031 | [Shared Memory Bank 是什么？](q031.md) |
| 032 | [什么是 Bank Conflict？Broadcast 为什么是例外？](q032.md) |
| 033 | [为什么 `tile[32][32]` 的列访问会出现 32-Way Bank Conflict？](q033.md) |
| 034 | [为什么 `tile[32][33]` 能消除典型 Transpose Bank Conflict？](q034.md) |
| 035 | [什么是 Warp Divergence？](q035.md) |
| 036 | [`if` 一定产生 Divergence 吗？如何重构控制流？](q036.md) |
| 037 | [Predication 是什么？为什么“消灭 if”不一定更快？](q037.md) |
| 038 | [`__shfl_sync` 为什么可能比 Shared Memory 交换更快？](q038.md) |
| 039 | [`__syncwarp()` 什么时候必须用？](q039.md) |
| 040 | [如何写一个 Warp-Level Reduction？](q040.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

第 1/3 章，尤其 warp 与地址模式。

### 本章核心因果模型

Shared memory 先看 lane→bank 映射；控制流先看 lane→active mask；warp primitive 先看 participating mask。三者都以 warp 为基本分析单位。

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

1. shared stride bank-conflict sweep
2. 32x32 vs 32x33 transpose
3. shared vs shuffle warp reduction

### 掌握度检查

- [ ] 能推导 32-way conflict
- [ ] 能解释 broadcast 例外
- [ ] 能正确使用 shuffle mask 与 syncwarp

### 本章题目矩阵

| # | Question |
|---:|---|
| Q031 | [Shared Memory Bank 是什么？](q031.md) |
| Q032 | [什么是 Bank Conflict？Broadcast 为什么是例外？](q032.md) |
| Q033 | [为什么 `tile[32][32]` 的列访问会出现 32-Way Bank Conflict？](q033.md) |
| Q034 | [为什么 `tile[32][33]` 能消除典型 Transpose Bank Conflict？](q034.md) |
| Q035 | [什么是 Warp Divergence？](q035.md) |
| Q036 | [`if` 一定产生 Divergence 吗？如何重构控制流？](q036.md) |
| Q037 | [Predication 是什么？为什么“消灭 if”不一定更快？](q037.md) |
| Q038 | [`__shfl_sync` 为什么可能比 Shared Memory 交换更快？](q038.md) |
| Q039 | [`__syncwarp()` 什么时候必须用？](q039.md) |
| Q040 | [如何写一个 Warp-Level Reduction？](q040.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
