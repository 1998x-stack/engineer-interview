# GPU 架构代际指南：Ampere → Hopper → Blackwell

> 目标：面试时先讲稳定原理，再补架构特定机制。不要把某一代 GPU 的最佳实践当成永恒规则。

## 稳定不变的优化主线

无论架构如何变化，下面五件事始终是性能分析的核心：

1. **Memory Efficiency**：warp 地址是否高效、是否重复搬运无用数据。
2. **Compute Efficiency**：是否使用合适的执行单元与数据类型。
3. **Parallelism**：是否有足够 work 填满 GPU。
4. **Latency Hiding**：是否有足够 eligible work 与 pipeline overlap。
5. **Resource Balance**：register/shared/tile/pipeline stage 是否把 residency 压得过低。

## Ampere：Async Copy 进入主流 Kernel 设计

典型关键词：

- Tensor Core；
- `cp.async` / async global→shared；
- multi-stage shared-memory pipeline；
- TF32 / FP16 / BF16。

面试重点不是背指令，而是解释：为什么把下一 tile 的 global→shared copy 提前，能够把 memory latency 藏在当前 tile 的 compute 后面。

## Hopper：TMA + Cluster + Warp Specialization

Hopper 把数据移动与 block 间协作再向前推进：

- **TMA**：硬件完成多维 tensor bulk copy 与地址生成；
- **Thread Block Cluster**：在 Grid 与 Block 之间增加协作层级；
- **DSM**：cluster 内 block 可访问彼此 shared-memory address space；
- **Warp Specialization**：producer warp group 管 TMA / stage，consumer warp group 管 MMA。

典型数据流：

```text
HBM --TMA--> Shared
              ↓
         WGMMA / Tensor Core
              ↓
          Registers / Output
```

## Blackwell：TMEM / TCGen05 / 新的 Warp-Specialized Kernel 结构

Blackwell 增加了新的 Tensor Core 数据路径与调度机制：

- **TCGen05**：第五代 Tensor Core 指令体系；
- **TMEM**：tensor-oriented memory locale，用于 accumulator / Tensor Core 数据路径；
- **Cluster Launch Control** 等新的 persistent / scheduler 能力；
- CUTLASS SM100 kernel 使用不同于 Hopper 的 warp-specialization recipe。

重要辨析：

```text
TMA  = data movement engine
TMEM = memory locale
DSM  = cluster-level shared-memory addressing capability
```

三者不是同一层概念。

## CUDA 13.3：Tile-Centric Programming

CUDA 13.3 加入 CUDA Tile C++。其意义不是“threads 消失”，而是允许开发者以 tile 作为更高层的编程对象，让编译器/runtime 承担更多底层 thread mapping 与专用硬件映射。

面试比较可用：

| 抽象 | 主要控制粒度 | 优点 | 代价 |
|---|---|---|---|
| CUDA C++ | thread/block | 控制最细、生态成熟 | 手工管理 layout/pipeline 复杂 |
| CUTLASS/CuTe | tile/layout/atom | 高性能组件可组合 | 模板/抽象学习曲线陡 |
| CUDA Tile C++ | tile | 更高层表达，面向专用硬件 | 新生态，需要关注版本与支持范围 |
| cuBLAS | operation | 工程首选、成熟 | 自定义空间小 |

## 面试迁移原则

如果面试官问“这段 Ampere kernel 换 H100/B200 怎么办”，高分回答不是立刻列新指令，而是：

1. 保留算法与数据复用模型；
2. 重新测 problem shape 与并行度；
3. 用目标架构的数据移动原语重做 pipeline；
4. 重新选择 tile / stage / register budget；
5. 用 Nsight 重新验证，不假设旧参数继续最优。

## 官方资料

- CUDA Toolkit Documentation: <https://docs.nvidia.com/cuda/>
- Hopper Architecture In-Depth: <https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/>
- CUTLASS Efficient GEMM: <https://docs.nvidia.com/cutlass/latest/media/docs/cpp/efficient_gemm.html>
- CUTLASS Changelog: <https://docs.nvidia.com/cutlass/latest/CHANGELOG.html>
- PTX ISA: <https://docs.nvidia.com/cuda/parallel-thread-execution/>
