# 第 2 章｜GPU Memory Hierarchy

理解 register/shared/L1/L2/HBM 与主机内存的数据移动成本。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 011 | [请完整描述 GPU Memory Hierarchy。](q011.md) |
| 012 | [Register 为什么快？为什么又不能无限使用？](q012.md) |
| 013 | [什么情况下变量会 Spill 到 Local Memory？如何发现？](q013.md) |
| 014 | [Shared Memory 为什么快？它解决的三个核心问题是什么？](q014.md) |
| 015 | [L1 Cache 与 Shared Memory 的区别是什么？](q015.md) |
| 016 | [L2 Cache 为什么对多 Block / 多 SM 工作负载重要？](q016.md) |
| 017 | [Constant Memory 什么访问模式最快？](q017.md) |
| 018 | [Texture / Read-Only Cache 什么时候有价值？](q018.md) |
| 019 | [`cudaMalloc` 与 Unified Memory / `cudaMallocManaged` 怎么选？](q019.md) |
| 020 | [Pinned Host Memory 为什么能提高 H2D/D2H 吞吐？](q020.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

第 1 章执行模型；知道 global/shared/register 基本语法。

### 本章核心因果模型

所有优化都可看成让数据尽量停留在更近、更可复用的层级，同时控制资源占用。重点区分 hardware-managed cache 与 software-managed storage。

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

1. 测 register pressure→spill 拐点
2. shared reuse vs global reload
3. pinned/pageable/UM 三类 host-device 数据移动

### 掌握度检查

- [ ] 能画完整 memory hierarchy
- [ ] 能解释 spill 为什么危险
- [ ] 能根据访问模式选择 constant/texture/UM/pinned

### 本章题目矩阵

| # | Question |
|---:|---|
| Q011 | [请完整描述 GPU Memory Hierarchy。](q011.md) |
| Q012 | [Register 为什么快？为什么又不能无限使用？](q012.md) |
| Q013 | [什么情况下变量会 Spill 到 Local Memory？如何发现？](q013.md) |
| Q014 | [Shared Memory 为什么快？它解决的三个核心问题是什么？](q014.md) |
| Q015 | [L1 Cache 与 Shared Memory 的区别是什么？](q015.md) |
| Q016 | [L2 Cache 为什么对多 Block / 多 SM 工作负载重要？](q016.md) |
| Q017 | [Constant Memory 什么访问模式最快？](q017.md) |
| Q018 | [Texture / Read-Only Cache 什么时候有价值？](q018.md) |
| Q019 | [`cudaMalloc` 与 Unified Memory / `cudaMallocManaged` 怎么选？](q019.md) |
| Q020 | [Pinned Host Memory 为什么能提高 H2D/D2H 吞吐？](q020.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
