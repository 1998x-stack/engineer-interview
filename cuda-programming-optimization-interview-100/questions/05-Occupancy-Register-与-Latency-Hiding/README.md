# 第 5 章｜Occupancy、Register 与 Latency Hiding

理解资源约束、TLP/ILP、spill 与 occupancy 的真实关系。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 041 | [什么是 Occupancy？](q041.md) |
| 042 | [为什么 100% Occupancy 不一定最快？](q042.md) |
| 043 | [哪些资源会限制 Resident Blocks / Occupancy？](q043.md) |
| 044 | [什么是 Register Pressure？如何权衡？](q044.md) |
| 045 | [如何查看 Kernel 使用多少 Registers / Shared Memory / Spills？](q045.md) |
| 046 | [`-maxrregcount` 是不是越小越好？](q046.md) |
| 047 | [`__launch_bounds__` 用来解决什么问题？](q047.md) |
| 048 | [ILP 与 TLP 有什么区别？](q048.md) |
| 049 | [GPU 如何用 Warp Scheduling 隐藏 Memory Latency？](q049.md) |
| 050 | [Block Size 应该如何系统调优，而不是猜 256？](q050.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

执行模型、memory hierarchy、基本 profiler。

### 本章核心因果模型

Occupancy 是资源约束的结果，不是目标。真正目标是足够 eligible work 隐藏 latency，同时保留 register/shared reuse 与 ILP。

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

1. 动态 shared memory 控制 occupancy
2. unroll/register-pressure sweep
3. block-size autotune CSV

### 掌握度检查

- [ ] 能写 residency min-formula
- [ ] 能解释 100% occupancy 反例
- [ ] 能从 spill/eligible warp 判断 register trade-off

### 本章题目矩阵

| # | Question |
|---:|---|
| Q041 | [什么是 Occupancy？](q041.md) |
| Q042 | [为什么 100% Occupancy 不一定最快？](q042.md) |
| Q043 | [哪些资源会限制 Resident Blocks / Occupancy？](q043.md) |
| Q044 | [什么是 Register Pressure？如何权衡？](q044.md) |
| Q045 | [如何查看 Kernel 使用多少 Registers / Shared Memory / Spills？](q045.md) |
| Q046 | [`-maxrregcount` 是不是越小越好？](q046.md) |
| Q047 | [`__launch_bounds__` 用来解决什么问题？](q047.md) |
| Q048 | [ILP 与 TLP 有什么区别？](q048.md) |
| Q049 | [GPU 如何用 Warp Scheduling 隐藏 Memory Latency？](q049.md) |
| Q050 | [Block Size 应该如何系统调优，而不是猜 256？](q050.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
