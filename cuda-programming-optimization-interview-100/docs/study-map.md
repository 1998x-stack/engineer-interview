# 学习地图：四轮掌握 100 题

| 轮次 | 题号 | 主题 | 通过标准 |
|---|---:|---|---|
| 第一轮 | 1-40 | 执行模型 + Memory | 30-60 秒准确回答核心概念；能手算 coalescing / bank mapping。 |
| 第二轮 | 41-60 | 资源模型 + Coding | 能解释 occupancy/register trade-off，并现场写 Reduction/Transpose/Scan/GEMM。 |
| 第三轮 | 61-80 | Async + Profiling | 能用 pipeline、Roofline、Nsight 从指标定位瓶颈。 |
| 第四轮 | 81-100 | 现代高性能 CUDA | 能解释 CUTLASS、Tensor Core、TMA、warp specialization、TMEM、CUDA Tile。 |

## 十章

1. CUDA 执行模型与 SIMT
2. GPU Memory Hierarchy
3. Global Memory 与 Coalescing
4. Shared Memory、Warp 与 Divergence
5. Occupancy、Register 与 Latency Hiding
6. 经典 CUDA Kernel 现场编程
7. Stream、异步拷贝与 Software Pipeline
8. Nsight、Roofline 与性能诊断
9. GEMM、Tensor Core 与 CUTLASS
10. Hopper、Blackwell 与 CUDA 13.x
