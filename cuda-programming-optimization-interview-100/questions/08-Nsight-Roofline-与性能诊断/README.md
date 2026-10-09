# 第 8 章｜Nsight、Roofline 与性能诊断

从 timeline 到 counters 建立可证伪的性能工程闭环。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 071 | [优化 CUDA Kernel 的第一步是什么？](q071.md) |
| 072 | [如何判断 Memory-Bound 还是 Compute-Bound？](q072.md) |
| 073 | [Roofline Model 如何指导具体优化？](q073.md) |
| 074 | [Nsight Systems 与 Nsight Compute 怎么分工？](q074.md) |
| 075 | [SM Throughput 95% 是否说明 Kernel 已经最优？](q075.md) |
| 076 | [DRAM Throughput 95% 意味着什么？](q076.md) |
| 077 | [常见 Warp Stall Reasons 应如何解释？](q077.md) |
| 078 | [为什么很短或 Block 很少的 Kernel，Occupancy 指标可能没意义？](q078.md) |
| 079 | [什么是 Speed of Light（SOL）分析？](q079.md) |
| 080 | [如何证明一个 CUDA 优化“真的有效”？](q080.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

至少完成 Q001-Q070；会使用命令行工具。

### 本章核心因果模型

性能诊断必须走证据链：Systems 找热点与空洞→Roofline 分类→Compute counters 找机制→单变量实验证伪。不要从优化口诀出发。

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

1. 建立 nsys→ncu 工作流
2. vector/GEMM roofline
3. 构造三类 stall microbenchmark

### 掌握度检查

- [ ] 能判断 memory/compute/latency/launch bound
- [ ] 能解释 SOL 不等于最优
- [ ] 能设计可重复 benchmark

### 本章题目矩阵

| # | Question |
|---:|---|
| Q071 | [优化 CUDA Kernel 的第一步是什么？](q071.md) |
| Q072 | [如何判断 Memory-Bound 还是 Compute-Bound？](q072.md) |
| Q073 | [Roofline Model 如何指导具体优化？](q073.md) |
| Q074 | [Nsight Systems 与 Nsight Compute 怎么分工？](q074.md) |
| Q075 | [SM Throughput 95% 是否说明 Kernel 已经最优？](q075.md) |
| Q076 | [DRAM Throughput 95% 意味着什么？](q076.md) |
| Q077 | [常见 Warp Stall Reasons 应如何解释？](q077.md) |
| Q078 | [为什么很短或 Block 很少的 Kernel，Occupancy 指标可能没意义？](q078.md) |
| Q079 | [什么是 Speed of Light（SOL）分析？](q079.md) |
| Q080 | [如何证明一个 CUDA 优化“真的有效”？](q080.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
