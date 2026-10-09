# 第 9 章｜GEMM、Tensor Core 与 CUTLASS

分层 tiling、Tensor Core、persistent/Stream-K 与 warp specialization。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 081 | [为什么 GEMM 是 CUDA 性能优化的“综合大题”？](q081.md) |
| 082 | [GEMM 为什么 Arithmetic Intensity 很高？](q082.md) |
| 083 | [GEMM 为什么需要多级 Tiling？](q083.md) |
| 084 | [Tensor Core 与普通 CUDA Core 的区别是什么？](q084.md) |
| 085 | [FP32、TF32、FP16、BF16、FP8、FP4 怎么选？](q085.md) |
| 086 | [WMMA、PTX MMA、CUTLASS、cuBLAS 各处于什么抽象层？](q086.md) |
| 087 | [CUTLASS 的核心设计思想是什么？](q087.md) |
| 088 | [什么是 Warp Specialization？](q088.md) |
| 089 | [什么是 Persistent Kernel？](q089.md) |
| 090 | [什么是 Split-K / Stream-K？什么时候能解决 GEMM 利用率问题？](q090.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

Tiling、async pipeline、Roofline、Tensor Core 基础。

### 本章核心因果模型

GEMM 把多级数据复用、矩阵指令、software pipeline、warp specialization 与 scheduler 集成到一个 kernel。理解 CUTLASS 应从 mainloop/epilogue/layout/scheduler 四块拆解。

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

1. naive→tiled GEMM
2. CUTLASS profiler top-kernel 对比
3. small/skinny GEMM + split-K/Stream-K

### 掌握度检查

- [ ] 能画 CTA/warp/MMA tile hierarchy
- [ ] 能解释 dtype 与 Tensor Core trade-off
- [ ] 能说清 persistent/warp-specialized/Stream-K

### 本章题目矩阵

| # | Question |
|---:|---|
| Q081 | [为什么 GEMM 是 CUDA 性能优化的“综合大题”？](q081.md) |
| Q082 | [GEMM 为什么 Arithmetic Intensity 很高？](q082.md) |
| Q083 | [GEMM 为什么需要多级 Tiling？](q083.md) |
| Q084 | [Tensor Core 与普通 CUDA Core 的区别是什么？](q084.md) |
| Q085 | [FP32、TF32、FP16、BF16、FP8、FP4 怎么选？](q085.md) |
| Q086 | [WMMA、PTX MMA、CUTLASS、cuBLAS 各处于什么抽象层？](q086.md) |
| Q087 | [CUTLASS 的核心设计思想是什么？](q087.md) |
| Q088 | [什么是 Warp Specialization？](q088.md) |
| Q089 | [什么是 Persistent Kernel？](q089.md) |
| Q090 | [什么是 Split-K / Stream-K？什么时候能解决 GEMM 利用率问题？](q090.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
