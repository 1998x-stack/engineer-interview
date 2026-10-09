# Professional V2 Content Standard

本页定义 100 道题的第二版内容标准，目的是让仓库从“面试答案集合”升级成“GPU 性能工程训练材料”。

## 1. Source Boundary

每个题解区分两类内容：

1. **PDF 基线题解**：来自仓库附带 PDF，是原始题库的内容基线；
2. **Repository Expansion / Professional V2**：在基线之上增加的推导、实验、Profiler 与架构分析。

新增内容不应悄悄改写 PDF 基线。发现基线有错误时，应在扩展区明确写“修正/版本差异”，并给官方来源。

## 2. The Eight Required V2 Blocks

每题必须包含：

1. 硬件机制与核心心智模型；
2. 定量推导 / 性能模型；
3. 代码 / 白板核心片段；
4. Nsight 证据链；
5. 架构迁移视角；
6. 可复现实验；
7. 深挖追问树；
8. 高分回答检查清单。

## 3. “Detailed” Does Not Mean “Long”

专业题解必须至少回答四个问题：

```text
Why does the hardware behave this way?
What is the quantitative cost / bound?
What evidence would prove or disprove it?
When would the recommendation stop being true?
```

单纯增加背景介绍、重复定义或堆术语不计入“深度”。

## 4. Quantitative Requirement

优先使用：

- bytes / transaction / sector；
- FLOPs / arithmetic intensity；
- occupancy / register / smem resource equations；
- stage/pipeline overlap lower bound；
- Amdahl / Roofline；
- algorithmic work/span；
- numerical error / determinism trade-off。

无法给精确数字时，写变量关系和假设，不猜某代 GPU 的硬件常数。

## 5. Profiler Requirement

题解不应只写“用 Nsight 看一下”。要说明：

- 看哪一类指标；
- 指标应该朝哪个方向变化；
- 什么结果会推翻当前假设；
- 为什么时间下降与该指标存在因果关系。

推荐格式：

| Hypothesis | Expected counter change | Runtime expectation |
|---|---|---|
| Reduce overfetch | sectors/request ↓ | memory-bound runtime ↓ |
| Hide latency | eligible warps / overlap ↑ | exposed-stall cycles ↓ |

## 6. Architecture Boundary

稳定原则与架构实现分开：

- 稳定：warp 粒度、数据复用、依赖、Roofline、资源平衡；
- 变化快：SM 资源常数、cache 容量、TMA/TMEM/TCGen05、CUTLASS recipe、CUDA Tile API。

Hopper/Blackwell/CUDA 13.x 相关事实优先引用 NVIDIA 官方文档。

## 7. Engineering Baseline

对于 reduction/scan/sort/GEMM 等已有成熟库的算子，题解必须提醒：

> 手写 kernel 的面试价值是展示原理；工程价值需要通过 CUB/cuBLAS/CUTLASS 等成熟实现作为 baseline 证明。

## 8. Reproducibility

实验至少记录：

- GPU 型号 / compute capability；
- driver / CUDA / compiler；
- 编译 flags；
- shape / dtype；
- warm-up 与 iteration；
- median/p95；
- correctness tolerance；
- profiler 版本与关键指标。
