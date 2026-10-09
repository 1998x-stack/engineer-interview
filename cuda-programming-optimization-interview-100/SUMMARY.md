# CUDA 编程优化面试 100 题 - SUMMARY

## 第 1 章｜CUDA 执行模型与 SIMT

- [Q001｜Thread、Warp、Block、Grid、SM 分别是什么？](questions/01-CUDA-执行模型与-SIMT/q001.md)
- [Q002｜CUDA 为什么称 SIMT，而不是传统 SIMD？](questions/01-CUDA-执行模型与-SIMT/q002.md)
- [Q003｜为什么 Warp 是 CUDA 性能分析最重要的单位？](questions/01-CUDA-执行模型与-SIMT/q003.md)
- [Q004｜Kernel launch 后，Block 是如何调度到 SM 的？](questions/01-CUDA-执行模型与-SIMT/q004.md)
- [Q005｜为什么 block size 常从 128/256 开始，而不是随便选？](questions/01-CUDA-执行模型与-SIMT/q005.md)
- [Q006｜什么是 Grid-Stride Loop？为什么它是 CUDA 常用模式？](questions/01-CUDA-执行模型与-SIMT/q006.md)
- [Q007｜`__syncthreads()` 到底同步什么？](questions/01-CUDA-执行模型与-SIMT/q007.md)
- [Q008｜CUDA 有哪些同步层级？](questions/01-CUDA-执行模型与-SIMT/q008.md)
- [Q009｜为什么 kernel launch 通常是异步的？如何正确计时？](questions/01-CUDA-执行模型与-SIMT/q009.md)
- [Q010｜为什么 GPU 更偏 throughput，而 CPU 更偏 latency？](questions/01-CUDA-执行模型与-SIMT/q010.md)

## 第 2 章｜GPU Memory Hierarchy

- [Q011｜请完整描述 GPU Memory Hierarchy。](questions/02-GPU-Memory-Hierarchy/q011.md)
- [Q012｜Register 为什么快？为什么又不能无限使用？](questions/02-GPU-Memory-Hierarchy/q012.md)
- [Q013｜什么情况下变量会 Spill 到 Local Memory？如何发现？](questions/02-GPU-Memory-Hierarchy/q013.md)
- [Q014｜Shared Memory 为什么快？它解决的三个核心问题是什么？](questions/02-GPU-Memory-Hierarchy/q014.md)
- [Q015｜L1 Cache 与 Shared Memory 的区别是什么？](questions/02-GPU-Memory-Hierarchy/q015.md)
- [Q016｜L2 Cache 为什么对多 Block / 多 SM 工作负载重要？](questions/02-GPU-Memory-Hierarchy/q016.md)
- [Q017｜Constant Memory 什么访问模式最快？](questions/02-GPU-Memory-Hierarchy/q017.md)
- [Q018｜Texture / Read-Only Cache 什么时候有价值？](questions/02-GPU-Memory-Hierarchy/q018.md)
- [Q019｜`cudaMalloc` 与 Unified Memory / `cudaMallocManaged` 怎么选？](questions/02-GPU-Memory-Hierarchy/q019.md)
- [Q020｜Pinned Host Memory 为什么能提高 H2D/D2H 吞吐？](questions/02-GPU-Memory-Hierarchy/q020.md)

## 第 3 章｜Global Memory 与 Coalescing

- [Q021｜什么叫 Global Memory Coalescing？](questions/03-Global-Memory-与-Coalescing/q021.md)
- [Q022｜32 个线程连续读 32 个 float，理想需要多少 transaction？](questions/03-Global-Memory-与-Coalescing/q022.md)
- [Q023｜什么是 Misaligned Access？现代 GPU 上为什么仍要关注？](questions/03-Global-Memory-与-Coalescing/q023.md)
- [Q024｜为什么 Strided Access 很危险？](questions/03-Global-Memory-与-Coalescing/q024.md)
- [Q025｜AoS 与 SoA 哪个更适合 CUDA？](questions/03-Global-Memory-与-Coalescing/q025.md)
- [Q026｜Vectorized Load/Store（如 float4）什么时候有收益？](questions/03-Global-Memory-与-Coalescing/q026.md)
- [Q027｜为什么 Matrix Transpose 是经典 CUDA 优化题？](questions/03-Global-Memory-与-Coalescing/q027.md)
- [Q028｜Effective Bandwidth 怎么计算？](questions/03-Global-Memory-与-Coalescing/q028.md)
- [Q029｜Requested Bandwidth 与 Actual DRAM Bandwidth 有什么区别？](questions/03-Global-Memory-与-Coalescing/q029.md)
- [Q030｜一个 Memory-Bound Kernel 最常见的优化方向有哪些？](questions/03-Global-Memory-与-Coalescing/q030.md)

## 第 4 章｜Shared Memory、Warp 与 Divergence

- [Q031｜Shared Memory Bank 是什么？](questions/04-Shared-Memory-Warp-与-Divergence/q031.md)
- [Q032｜什么是 Bank Conflict？Broadcast 为什么是例外？](questions/04-Shared-Memory-Warp-与-Divergence/q032.md)
- [Q033｜为什么 `tile[32][32]` 的列访问会出现 32-Way Bank Conflict？](questions/04-Shared-Memory-Warp-与-Divergence/q033.md)
- [Q034｜为什么 `tile[32][33]` 能消除典型 Transpose Bank Conflict？](questions/04-Shared-Memory-Warp-与-Divergence/q034.md)
- [Q035｜什么是 Warp Divergence？](questions/04-Shared-Memory-Warp-与-Divergence/q035.md)
- [Q036｜`if` 一定产生 Divergence 吗？如何重构控制流？](questions/04-Shared-Memory-Warp-与-Divergence/q036.md)
- [Q037｜Predication 是什么？为什么“消灭 if”不一定更快？](questions/04-Shared-Memory-Warp-与-Divergence/q037.md)
- [Q038｜`__shfl_sync` 为什么可能比 Shared Memory 交换更快？](questions/04-Shared-Memory-Warp-与-Divergence/q038.md)
- [Q039｜`__syncwarp()` 什么时候必须用？](questions/04-Shared-Memory-Warp-与-Divergence/q039.md)
- [Q040｜如何写一个 Warp-Level Reduction？](questions/04-Shared-Memory-Warp-与-Divergence/q040.md)

## 第 5 章｜Occupancy、Register 与 Latency Hiding

- [Q041｜什么是 Occupancy？](questions/05-Occupancy-Register-与-Latency-Hiding/q041.md)
- [Q042｜为什么 100% Occupancy 不一定最快？](questions/05-Occupancy-Register-与-Latency-Hiding/q042.md)
- [Q043｜哪些资源会限制 Resident Blocks / Occupancy？](questions/05-Occupancy-Register-与-Latency-Hiding/q043.md)
- [Q044｜什么是 Register Pressure？如何权衡？](questions/05-Occupancy-Register-与-Latency-Hiding/q044.md)
- [Q045｜如何查看 Kernel 使用多少 Registers / Shared Memory / Spills？](questions/05-Occupancy-Register-与-Latency-Hiding/q045.md)
- [Q046｜`-maxrregcount` 是不是越小越好？](questions/05-Occupancy-Register-与-Latency-Hiding/q046.md)
- [Q047｜`__launch_bounds__` 用来解决什么问题？](questions/05-Occupancy-Register-与-Latency-Hiding/q047.md)
- [Q048｜ILP 与 TLP 有什么区别？](questions/05-Occupancy-Register-与-Latency-Hiding/q048.md)
- [Q049｜GPU 如何用 Warp Scheduling 隐藏 Memory Latency？](questions/05-Occupancy-Register-与-Latency-Hiding/q049.md)
- [Q050｜Block Size 应该如何系统调优，而不是猜 256？](questions/05-Occupancy-Register-与-Latency-Hiding/q050.md)

## 第 6 章｜经典 CUDA Kernel 现场编程

- [Q051｜现场手写一个高性能 Reduction：你会如何逐版优化？](questions/06-经典-CUDA-Kernel-现场编程/q051.md)
- [Q052｜为什么最原始 Interleaved Reduction 很慢？](questions/06-经典-CUDA-Kernel-现场编程/q052.md)
- [Q053｜Reduction 最后一 Warp 为什么适合用 Shuffle？](questions/06-经典-CUDA-Kernel-现场编程/q053.md)
- [Q054｜手写 Parallel Scan / Prefix Sum：Hillis-Steele 与 Blelloch 如何比较？](questions/06-经典-CUDA-Kernel-现场编程/q054.md)
- [Q055｜Parallel Histogram 如何优化 Atomic Contention？](questions/06-经典-CUDA-Kernel-现场编程/q055.md)
- [Q056｜现场写 Optimized Matrix Transpose。](questions/06-经典-CUDA-Kernel-现场编程/q056.md)
- [Q057｜手写 Tiled Matrix Multiplication，并解释为什么快。](questions/06-经典-CUDA-Kernel-现场编程/q057.md)
- [Q058｜为什么 GEMM Tile 越大不一定越快？](questions/06-经典-CUDA-Kernel-现场编程/q058.md)
- [Q059｜如何实现 Stream Compaction？](questions/06-经典-CUDA-Kernel-现场编程/q059.md)
- [Q060｜Top-K / Sort / Selection 什么时候不应该自己写 CUDA？](questions/06-经典-CUDA-Kernel-现场编程/q060.md)

## 第 7 章｜Stream、异步拷贝与 Software Pipeline

- [Q061｜CUDA Stream 是什么？不同 Stream 真的能并发吗？](questions/07-Stream-异步拷贝与-Software-Pipeline/q061.md)
- [Q062｜`cudaMemcpyAsync` 为什么不一定真的异步？](questions/07-Stream-异步拷贝与-Software-Pipeline/q062.md)
- [Q063｜如何设计 H2D - Kernel - D2H 的流水重叠？](questions/07-Stream-异步拷贝与-Software-Pipeline/q063.md)
- [Q064｜CUDA Event 与 `cudaDeviceSynchronize()` 有什么区别？](questions/07-Stream-异步拷贝与-Software-Pipeline/q064.md)
- [Q065｜Ampere 的 Async Global→Shared Copy 解决什么问题？](questions/07-Stream-异步拷贝与-Software-Pipeline/q065.md)
- [Q066｜什么是 Software Pipelining？](questions/07-Stream-异步拷贝与-Software-Pipeline/q066.md)
- [Q067｜什么是 Double Buffering / Multi-Stage Pipeline？](questions/07-Stream-异步拷贝与-Software-Pipeline/q067.md)
- [Q068｜Hopper TMA 解决什么问题？](questions/07-Stream-异步拷贝与-Software-Pipeline/q068.md)
- [Q069｜`cuda::pipeline` / `cuda::barrier` 在 Async Pipeline 中做什么？](questions/07-Stream-异步拷贝与-Software-Pipeline/q069.md)
- [Q070｜Kernel Fusion 为什么经常有效？什么时候会适得其反？](questions/07-Stream-异步拷贝与-Software-Pipeline/q070.md)

## 第 8 章｜Nsight、Roofline 与性能诊断

- [Q071｜优化 CUDA Kernel 的第一步是什么？](questions/08-Nsight-Roofline-与性能诊断/q071.md)
- [Q072｜如何判断 Memory-Bound 还是 Compute-Bound？](questions/08-Nsight-Roofline-与性能诊断/q072.md)
- [Q073｜Roofline Model 如何指导具体优化？](questions/08-Nsight-Roofline-与性能诊断/q073.md)
- [Q074｜Nsight Systems 与 Nsight Compute 怎么分工？](questions/08-Nsight-Roofline-与性能诊断/q074.md)
- [Q075｜SM Throughput 95% 是否说明 Kernel 已经最优？](questions/08-Nsight-Roofline-与性能诊断/q075.md)
- [Q076｜DRAM Throughput 95% 意味着什么？](questions/08-Nsight-Roofline-与性能诊断/q076.md)
- [Q077｜常见 Warp Stall Reasons 应如何解释？](questions/08-Nsight-Roofline-与性能诊断/q077.md)
- [Q078｜为什么很短或 Block 很少的 Kernel，Occupancy 指标可能没意义？](questions/08-Nsight-Roofline-与性能诊断/q078.md)
- [Q079｜什么是 Speed of Light（SOL）分析？](questions/08-Nsight-Roofline-与性能诊断/q079.md)
- [Q080｜如何证明一个 CUDA 优化“真的有效”？](questions/08-Nsight-Roofline-与性能诊断/q080.md)

## 第 9 章｜GEMM、Tensor Core 与 CUTLASS

- [Q081｜为什么 GEMM 是 CUDA 性能优化的“综合大题”？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q081.md)
- [Q082｜GEMM 为什么 Arithmetic Intensity 很高？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q082.md)
- [Q083｜GEMM 为什么需要多级 Tiling？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q083.md)
- [Q084｜Tensor Core 与普通 CUDA Core 的区别是什么？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q084.md)
- [Q085｜FP32、TF32、FP16、BF16、FP8、FP4 怎么选？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q085.md)
- [Q086｜WMMA、PTX MMA、CUTLASS、cuBLAS 各处于什么抽象层？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q086.md)
- [Q087｜CUTLASS 的核心设计思想是什么？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q087.md)
- [Q088｜什么是 Warp Specialization？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q088.md)
- [Q089｜什么是 Persistent Kernel？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q089.md)
- [Q090｜什么是 Split-K / Stream-K？什么时候能解决 GEMM 利用率问题？](questions/09-GEMM-Tensor-Core-与-CUTLASS/q090.md)

## 第 10 章｜Hopper、Blackwell 与 CUDA 13.x

- [Q091｜Hopper Thread Block Cluster 是什么？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q091.md)
- [Q092｜什么是 Distributed Shared Memory（DSM）？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q092.md)
- [Q093｜TMA 与 `cp.async` 的核心差别是什么？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q093.md)
- [Q094｜为什么 Hopper GEMM 适合 Producer-Consumer Warp Specialization？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q094.md)
- [Q095｜Blackwell Tensor Memory（TMEM）是什么？与 TMA 有什么区别？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q095.md)
- [Q096｜为什么 Blackwell 的 Warp Specialization 不能简单照搬 Hopper？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q096.md)
- [Q097｜CUDA Graph 什么时候能明显提升性能？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q097.md)
- [Q098｜为什么 `cudaMallocAsync` / Stream-Ordered Allocator 更适合高性能程序？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q098.md)
- [Q099｜CUDA Tile C++ / Tile Programming 为什么值得关注？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q099.md)
- [Q100｜给你一个比理论峰值慢 20 倍的 CUDA Kernel，你如何系统优化？](questions/10-Hopper-Blackwell-与-CUDA-13-x/q100.md)
