# References

PDF 使用 R1-R18 作为引用编号；仓库保留相同映射。

- **R1** - [NVIDIA CUDA Programming Guide](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- **R2** - [NVIDIA CUDA C++ Best Practices Guide 13.3](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/)
- **R3** - [CUDA Programming Guide - Distributed Shared Memory / Thread Block Clusters](https://docs.nvidia.com/cuda/cuda-programming-guide/)
- **R4** - [NVIDIA Nsight Compute - Kernel Profiling Guide](https://docs.nvidia.com/nsight-compute/)
- **R5** - [NVIDIA Hopper Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/)
- **R6** - [NVIDIA CUTLASS - Efficient GEMM](https://docs.nvidia.com/cutlass/latest/media/docs/cpp/efficient_gemm.html)
- **R7** - [CUDA C++ Language Extensions](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/cpp-language-extensions.html)
- **R8** - [NVIDIA - Using CUDA Warp-Level Primitives](https://developer.nvidia.com/blog/using-cuda-warp-level-primitives/)
- **R9** - [CUDA C++ Memory Model](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/cuda-cpp-memory-model.html)
- **R10** - [CUDA Runtime API - Streams / Events](https://docs.nvidia.com/cuda/cuda-runtime-api/)
- **R11** - [CUDA Runtime API - Stream Ordered Memory Allocator](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__MEMORY__POOLS.html)
- **R12** - [Public NVIDIA interview reports - CUDA question types](https://www.glassdoor.com/Interview/cuda-interview-questions-SRCH_KO0%2C4.htm)
- **R13** - [CUDA Programming Guide - Advanced Kernel Programming / Async Operations and TMA](https://docs.nvidia.com/cuda/cuda-programming-guide/03-advanced/advanced-kernel-programming.html)
- **R14** - [NVIDIA PTX ISA - TCGen05 and Tensor Memory](https://docs.nvidia.com/cuda/parallel-thread-execution/)
- **R15** - [NVIDIA CUTLASS Changelog - Blackwell SM100 / TMEM / TCGen05](https://docs.nvidia.com/cutlass/latest/CHANGELOG.html)
- **R16** - [CUDA Tile C++ API Reference 13.3 - General Principles](https://docs.nvidia.com/cuda/cuda-tile-cpp-api-reference/general_principles.html)
- **R17** - [NVIDIA NVCC 13.3 - Tile Compilation in CUDA](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/tile-compilation-in-cuda.html)
- **R18** - [NVIDIA Tile IR 13.3 - Introduction](https://docs.nvidia.com/cuda/tile-ir/13.3/sections/introduction.html)

## Current ecosystem note

- CUDA Toolkit 文档首页：<https://docs.nvidia.com/cuda/>
- CUTLASS 文档首页：<https://docs.nvidia.com/cutlass/latest/>

版本变化时，优先更新这里，再检查第 9-10 章的架构特定内容。
## 2026-09 verification notes

Professional V2 对快速演进部分做了额外官方资料核验：

- CUDA Toolkit 13.3 文档首页明确列出 **CUDA Tile C++**，并说明 NVCC/NVRTC 支持；
- CUDA Programming Guide 说明 **Compute Capability 9.0+** 支持 Thread Block Cluster，并可在 cluster 内使用 Distributed Shared Memory；
- CUTLASS **4.8.0（2026-08-25）** changelog 包含 Blackwell SM100 的 TCGen05、TMEM、Blackwell-specific warp specialization、CLC/Stream-K，并开始加入 Rubin 支持；
- CUTLASS 文档明确区分 **Tensor Memory (`tmem`)** 与 **Tensor Memory Accelerator (TMA)**。

这些属于仓库扩展的外部核验信息，不属于 PDF 基线正文。快速演进功能应以链接中的当前官方版本为准。
