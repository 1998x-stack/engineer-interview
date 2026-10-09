# 第 7 章｜Stream、异步拷贝与 Software Pipeline

构建 copy/compute overlap、多 stage pipeline 与 fusion。

## 本章目标

- 能把概念映射到具体硬件资源与调度行为。
- 能解释一个优化为什么有效，以及会牺牲什么。
- 能给出可测量的 profiler 证据。
- 能区分稳定原理与架构特定实现。

## 题目

| # | Question |
|---:|---|
| 061 | [CUDA Stream 是什么？不同 Stream 真的能并发吗？](q061.md) |
| 062 | [`cudaMemcpyAsync` 为什么不一定真的异步？](q062.md) |
| 063 | [如何设计 H2D - Kernel - D2H 的流水重叠？](q063.md) |
| 064 | [CUDA Event 与 `cudaDeviceSynchronize()` 有什么区别？](q064.md) |
| 065 | [Ampere 的 Async Global→Shared Copy 解决什么问题？](q065.md) |
| 066 | [什么是 Software Pipelining？](q066.md) |
| 067 | [什么是 Double Buffering / Multi-Stage Pipeline？](q067.md) |
| 068 | [Hopper TMA 解决什么问题？](q068.md) |
| 069 | [`cuda::pipeline` / `cuda::barrier` 在 Async Pipeline 中做什么？](q069.md) |
| 070 | [Kernel Fusion 为什么经常有效？什么时候会适得其反？](q070.md) |

## 本章复习方法

先用每题“30 秒”模式完成一遍，再挑 2-3 题做 microbenchmark；最后不看答案，依据 Nsight 指标复盘一次。

<!-- CHAPTER-PROFESSIONAL-V2 -->
## 专业学习指南 V2

### 前置能力

Streams/events 基本 API、shared memory、barrier。

### 本章核心因果模型

性能目标从“单 kernel 更快”升级为“让数据移动与计算流水重叠”。核心是 dependency graph、buffer ownership、stage/phase 与资源预算。

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

1. 双 stream H2D-K-D2H overlap
2. 1/2/3/4 stage pipeline sweep
3. fusion 前后 bytes/registers 对比

### 掌握度检查

- [ ] 能区分 enqueue async 与真实 overlap
- [ ] 能画 pipeline prologue/steady/epilogue
- [ ] 能解释 TMA 与 cp.async 的角色差异

### 本章题目矩阵

| # | Question |
|---:|---|
| Q061 | [CUDA Stream 是什么？不同 Stream 真的能并发吗？](q061.md) |
| Q062 | [`cudaMemcpyAsync` 为什么不一定真的异步？](q062.md) |
| Q063 | [如何设计 H2D - Kernel - D2H 的流水重叠？](q063.md) |
| Q064 | [CUDA Event 与 `cudaDeviceSynchronize()` 有什么区别？](q064.md) |
| Q065 | [Ampere 的 Async Global→Shared Copy 解决什么问题？](q065.md) |
| Q066 | [什么是 Software Pipelining？](q066.md) |
| Q067 | [什么是 Double Buffering / Multi-Stage Pipeline？](q067.md) |
| Q068 | [Hopper TMA 解决什么问题？](q068.md) |
| Q069 | [`cuda::pipeline` / `cuda::barrier` 在 Async Pipeline 中做什么？](q069.md) |
| Q070 | [Kernel Fusion 为什么经常有效？什么时候会适得其反？](q070.md) |

### 面试训练方式

- **第一遍**：每题只看标题，30 秒给结论。
- **第二遍**：每题至少写一个公式或画一张数据流图。
- **第三遍**：选择 2-3 题做 microbenchmark，并保存 profiler 指标。
- **第四遍**：随机抽题，回答“反例是什么 / 换 GPU 哪些结论需要重验 / 用什么指标证明”。
