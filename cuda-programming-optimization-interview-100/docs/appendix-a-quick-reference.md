# 附录 A｜100 题一页速查

| 题号 | 问题 | 面试核心 |
|---:|---|---|
| 001 | [Thread、Warp、Block、Grid、SM 分别是什么？](../questions/01-CUDA-执行模型与-SIMT/q001.md) | 编程层级是 Grid→Block→Thread；硬件调度核心是 SM→Warp，warp=32 threads。 |
| 002 | [CUDA 为什么称 SIMT，而不是传统 SIMD？](../questions/01-CUDA-执行模型与-SIMT/q002.md) | SIMT 允许每个 thread 拥有独立逻辑状态，而硬件按 warp 共同发射指令。 |
| 003 | [为什么 Warp 是 CUDA 性能分析最重要的单位？](../questions/01-CUDA-执行模型与-SIMT/q003.md) | coalescing、divergence、shuffle、scheduler issue、active mask 都天然以 warp 为分析粒度。 |
| 004 | [Kernel launch 后，Block 是如何调度到 SM 的？](../questions/01-CUDA-执行模型与-SIMT/q004.md) | Block 调度受 registers、shared memory、threads/warps、block slot 等多个上限共同约束。 |
| 005 | [为什么 block size 常从 128/256 开始，而不是随便选？](../questions/01-CUDA-执行模型与-SIMT/q005.md) | 128/256 只是实验起点：warp 整数倍减少空 lane，同时常能在 occupancy、调度开销和每 block 资源之间取得平衡。 |
| 006 | [什么是 Grid-Stride Loop？为什么它是 CUDA 常用模式？](../questions/01-CUDA-执行模型与-SIMT/q006.md) | Grid-stride loop 把“问题规模”与“launch 规模”解耦，便于限制 blocks 数、复用线程、实现 persistent 风格，也便于用 1 block/1 thread 调试同一 kernel。 |
| 007 | [`__syncthreads()` 到底同步什么？](../questions/01-CUDA-执行模型与-SIMT/q007.md) | `__syncthreads()` 是 block barrier，并带有对 block participating threads 有意义的内存可见性语义。 |
| 008 | [CUDA 有哪些同步层级？](../questions/01-CUDA-执行模型与-SIMT/q008.md) | 同步要区分作用域（warp/block/cluster/grid/host）与语义（barrier、event、fence、atomic order）。 |
| 009 | [为什么 kernel launch 通常是异步的？如何正确计时？](../questions/01-CUDA-执行模型与-SIMT/q009.md) | 默认 kernel launch 对 host 异步，因此 CPU wall-clock 若不同步通常只量到 enqueue。 |
| 010 | [为什么 GPU 更偏 throughput，而 CPU 更偏 latency？](../questions/01-CUDA-执行模型与-SIMT/q010.md) | GPU 用大量 resident warps 与宽吞吐资源隐藏长 latency；CPU 则投入更复杂的缓存、预测、乱序与少量强核心降低单线程 latency。 |
| 011 | [请完整描述 GPU Memory Hierarchy。](../questions/02-GPU-Memory-Hierarchy/q011.md) | Register/Shared 在片上；Global/Local/Constant/Texture 主要驻留 device memory；L1/L2 是硬件 cache。 |
| 012 | [Register 为什么快？为什么又不能无限使用？](../questions/02-GPU-Memory-Hierarchy/q012.md) | register 快但稀缺。 |
| 013 | [什么情况下变量会 Spill 到 Local Memory？如何发现？](../questions/02-GPU-Memory-Hierarchy/q013.md) | spill 常由高 register pressure、大局部数组或动态索引触发。 |
| 014 | [Shared Memory 为什么快？它解决的三个核心问题是什么？](../questions/02-GPU-Memory-Hierarchy/q014.md) | shared memory 的三个核心用法：跨线程协作、重用 global data、重排访问以获得 coalescing。 |
| 015 | [L1 Cache 与 Shared Memory 的区别是什么？](../questions/02-GPU-Memory-Hierarchy/q015.md) | L1 是硬件自动管理，shared 是软件显式管理。 |
| 016 | [L2 Cache 为什么对多 Block / 多 SM 工作负载重要？](../questions/02-GPU-Memory-Hierarchy/q016.md) | L2 是全 GPU 共享缓存，能承接跨 SM 的复用与写回。 |
| 017 | [Constant Memory 什么访问模式最快？](../questions/02-GPU-Memory-Hierarchy/q017.md) | constant memory 最理想是 warp 内 broadcast 同一地址；若每个 lane 访问不同 constant 地址，访问可能被序列化，优势会消失。 |
| 018 | [Texture / Read-Only Cache 什么时候有价值？](../questions/02-GPU-Memory-Hierarchy/q018.md) | texture/read-only path 适合某些只读、空间局部或不规则访问。 |
| 019 | [`cudaMalloc` 与 Unified Memory / `cudaMallocManaged` 怎么选？](../questions/02-GPU-Memory-Hierarchy/q019.md) | 显式 `cudaMalloc` 给你更可控的数据放置；Unified Memory 提供统一地址与迁移便利。 |
| 020 | [Pinned Host Memory 为什么能提高 H2D/D2H 吞吐？](../questions/02-GPU-Memory-Hierarchy/q020.md) | pinned host memory 允许 DMA 更直接地搬运，且是高质量 async H2D/D2H overlap 的常见前提；但 pinned memory 会占用受限系统资源，不能无上限使用。 |
| 021 | [什么叫 Global Memory Coalescing？](../questions/03-Global-Memory-与-Coalescing/q021.md) | coalescing 的本质是把 warp 的多个 lane 请求合并成尽量少的内存 transaction/sector。 |
| 022 | [32 个线程连续读 32 个 float，理想需要多少 transaction？](../questions/03-Global-Memory-与-Coalescing/q022.md) | 32×4B=128B；理想对齐时通常覆盖 4 个 32B sector。 |
| 023 | [什么是 Misaligned Access？现代 GPU 上为什么仍要关注？](../questions/03-Global-Memory-与-Coalescing/q023.md) | misalignment 可能让原本 4 个 sector 变成更多 sector；缓存复用可能缓和代价，但 requested/actual byte ratio 会恶化。 |
| 024 | [为什么 Strided Access 很危险？](../questions/03-Global-Memory-与-Coalescing/q024.md) | stride 让相邻 lane 请求落到分散的 cache line/sector，导致每个 transaction 只有少量有效字节。 |
| 025 | [AoS 与 SoA 哪个更适合 CUDA？](../questions/03-Global-Memory-与-Coalescing/q025.md) | AoS/SoA 没有绝对优劣：关键是 warp 同时访问哪些字段。 |
| 026 | [Vectorized Load/Store（如 float4）什么时候有收益？](../questions/03-Global-Memory-与-Coalescing/q026.md) | vectorized load/store 的收益来自更少指令、更宽 memory op 与更好的 copy throughput；前提是满足 alignment、连续性和编译器 codegen，且不能因为 padding/overfetch 反而搬更多数据。 |
| 027 | [为什么 Matrix Transpose 是经典 CUDA 优化题？](../questions/03-Global-Memory-与-Coalescing/q027.md) | transpose 同时暴露 global coalescing 与 shared bank conflict：先用 shared tile 把读写都变连续，再用 padding/swizzle 消除列访问冲突。 |
| 028 | [Effective Bandwidth 怎么计算？](../questions/03-Global-Memory-与-Coalescing/q028.md) | Effective bandwidth 要用“算法有效字节/实际时间”计算，并和峰值/实测 memcpy bandwidth 对比。 |
| 029 | [Requested Bandwidth 与 Actual DRAM Bandwidth 有什么区别？](../questions/03-Global-Memory-与-Coalescing/q029.md) | requested bandwidth 是有效负载，actual DRAM bandwidth 是硬件真实搬运。 |
| 030 | [一个 Memory-Bound Kernel 最常见的优化方向有哪些？](../questions/03-Global-Memory-与-Coalescing/q030.md) | memory-bound 优化优先减少 bytes：coalescing、reuse、fusion、低精度、vectorization、cache/shared tiling；必要时用 recompute 换 memory traffic。 |
| 031 | [Shared Memory Bank 是什么？](../questions/04-Shared-Memory-Warp-与-Divergence/q031.md) | shared bank 可理解为并行服务的地址分片。 |
| 032 | [什么是 Bank Conflict？Broadcast 为什么是例外？](../questions/04-Shared-Memory-Warp-与-Divergence/q032.md) | bank conflict 指同一 warp 对同一 bank 的不同地址产生冲突，需要拆分服务；多个 lane 读取完全相同地址可广播，因此是重要例外。 |
| 033 | [为什么 `tile[32][32]` 的列访问会出现 32-Way Bank Conflict？](../questions/04-Shared-Memory-Warp-与-Divergence/q033.md) | `[32][32]` 按列访问时相邻 lane 的 word index 相差 32，模 32 后全落同一 bank，因此形成典型 32-way conflict。 |
| 034 | [为什么 `tile[32][33]` 能消除典型 Transpose Bank Conflict？](../questions/04-Shared-Memory-Warp-与-Divergence/q034.md) | padding 到 33 后 stride 从 32 变 33，`33 mod 32 = 1`，相邻 lane 轮转到不同 bank。 |
| 035 | [什么是 Warp Divergence？](../questions/04-Shared-Memory-Warp-与-Divergence/q035.md) | divergence 是同一 warp 的 lane 走不同控制流路径。 |
| 036 | [`if` 一定产生 Divergence 吗？如何重构控制流？](../questions/04-Shared-Memory-Warp-与-Divergence/q036.md) | `if` 的条件若在 warp 内一致就没有 divergence。 |
| 037 | [Predication 是什么？为什么“消灭 if”不一定更快？](../questions/04-Shared-Memory-Warp-与-Divergence/q037.md) | predication 让指令执行但用 predicate 控制结果提交，适合短分支；长分支全 predication 会浪费大量指令，因此“去掉 branch”不是目标。 |
| 038 | [`__shfl_sync` 为什么可能比 Shared Memory 交换更快？](../questions/04-Shared-Memory-Warp-与-Divergence/q038.md) | shuffle 直接在 warp lanes 的 register 值之间交换，省掉 shared store/load 与 block barrier。 |
| 039 | [`__syncwarp()` 什么时候必须用？](../questions/04-Shared-Memory-Warp-与-Divergence/q039.md) | Volta+ independent scheduling 下，不能依赖“warp 天然 lockstep”完成 shared-memory producer/consumer。 |
| 040 | [如何写一个 Warp-Level Reduction？](../questions/04-Shared-Memory-Warp-与-Divergence/q040.md) | warp reduction 通常做 log2(32)=5 轮 shuffle-down。 |
| 041 | [什么是 Occupancy？](../questions/05-Occupancy-Register-与-Latency-Hiding/q041.md) | Occupancy 只回答“SM 上有多少 active warps”，不是“这些 warps 做得是否高效”。 |
| 042 | [为什么 100% Occupancy 不一定最快？](../questions/05-Occupancy-Register-与-Latency-Hiding/q042.md) | 高 occupancy 可能迫使每线程 register 太少、tile 太小、reuse 下降。 |
| 043 | [哪些资源会限制 Resident Blocks / Occupancy？](../questions/05-Occupancy-Register-与-Latency-Hiding/q043.md) | resident blocks 取 registers、shared memory、threads、warps、block slots 等限制的最小值。 |
| 044 | [什么是 Register Pressure？如何权衡？](../questions/05-Occupancy-Register-与-Latency-Hiding/q044.md) | register pressure 是“每线程活跃值太多”导致寄存器需求高。 |
| 045 | [如何查看 Kernel 使用多少 Registers / Shared Memory / Spills？](../questions/05-Occupancy-Register-与-Latency-Hiding/q045.md) | 编译期用 `-Xptxas=-v`/资源报告，运行期看 Nsight Occupancy/Memory，必要时下钻 SASS。 |
| 046 | [`-maxrregcount` 是不是越小越好？](../questions/05-Occupancy-Register-与-Latency-Hiding/q046.md) | `-maxrregcount` 只是强制预算。 |
| 047 | [`__launch_bounds__` 用来解决什么问题？](../questions/05-Occupancy-Register-与-Latency-Hiding/q047.md) | `__launch_bounds__` 给编译器 launch 约束，使寄存器分配能围绕目标 block size/residency 优化；它是编译提示，不是性能保证。 |
| 048 | [ILP 与 TLP 有什么区别？](../questions/05-Occupancy-Register-与-Latency-Hiding/q048.md) | TLP 用更多 warps/threads 隐藏延迟，ILP 用同一 thread/warp 内的独立指令填充流水。 |
| 049 | [GPU 如何用 Warp Scheduling 隐藏 Memory Latency？](../questions/05-Occupancy-Register-与-Latency-Hiding/q049.md) | warp 等 memory 时 scheduler 可选择其他 eligible warp 发射。 |
| 050 | [Block Size 应该如何系统调优，而不是猜 256？](../questions/05-Occupancy-Register-与-Latency-Hiding/q050.md) | 系统调 block size：先看每 block 资源与 occupancy limiter，再扫 64/128/256/512，最后以真实 workload 的 time + stall + resource 证据选值。 |
| 051 | [现场手写一个高性能 Reduction：你会如何逐版优化？](../questions/06-经典-CUDA-Kernel-现场编程/q051.md) | Reduction 的优化主线：减少 global atomics、减少 barriers/shared traffic、提高每线程工作量，最后用 warp shuffle。 |
| 052 | [为什么最原始 Interleaved Reduction 很慢？](../questions/06-经典-CUDA-Kernel-现场编程/q052.md) | interleaved addressing 让 active lane 稀疏、控制流效率差，还可能带来多余 modulo/地址计算。 |
| 053 | [Reduction 最后一 Warp 为什么适合用 Shuffle？](../questions/06-经典-CUDA-Kernel-现场编程/q053.md) | 最后 <=32 个 partials 已处于单 warp 范围，用 shuffle 省去 shared round trip 和 block barrier；但 partial warp mask 和数值顺序仍要处理。 |
| 054 | [手写 Parallel Scan / Prefix Sum：Hillis-Steele 与 Blelloch 如何比较？](../questions/06-经典-CUDA-Kernel-现场编程/q054.md) | Hillis-Steele 结构简单但 work 为 O(N log N)；Blelloch 可做到 O(N) work，通过 upsweep/downsweep 适合并行 prefix。 |
| 055 | [Parallel Histogram 如何优化 Atomic Contention？](../questions/06-经典-CUDA-Kernel-现场编程/q055.md) | histogram 的关键是降低对同一地址的 atomic contention。 |
| 056 | [现场写 Optimized Matrix Transpose。](../questions/06-经典-CUDA-Kernel-现场编程/q056.md) | optimized transpose 的经典链：coalesced global read → shared tile → sync → transposed read → coalesced write；再用 `TILE_DIM+1` 或 swizzle 去 bank conflict。 |
| 057 | [手写 Tiled Matrix Multiplication，并解释为什么快。](../questions/06-经典-CUDA-Kernel-现场编程/q057.md) | tiled GEMM 的加速来源是 A/B tile 被多个线程/多个 FMA 重用，提高 arithmetic intensity。 |
| 058 | [为什么 GEMM Tile 越大不一定越快？](../questions/06-经典-CUDA-Kernel-现场编程/q058.md) | tile 变大提高 reuse，却同步增加 shared/register/live state，可能减少 resident CTAs、增加 bank/fragment 管理开销。 |
| 059 | [如何实现 Stream Compaction？](../questions/06-经典-CUDA-Kernel-现场编程/q059.md) | stream compaction 的标准分解是 predicate → prefix sum → scatter。 |
| 060 | [Top-K / Sort / Selection 什么时候不应该自己写 CUDA？](../questions/06-经典-CUDA-Kernel-现场编程/q060.md) | Top-K/sort/selection 是成熟库高度优化的 primitive。 |
| 061 | [CUDA Stream 是什么？不同 Stream 真的能并发吗？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q061.md) | stream 保证同一 stream 内顺序，不同 stream 是否并发取决于依赖、资源和硬件能力。 |
| 062 | [`cudaMemcpyAsync` 为什么不一定真的异步？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q062.md) | 真正 async H2D/D2H 常需要 pinned memory、非阻塞 stream 和可用 copy engine。 |
| 063 | [如何设计 H2D - Kernel - D2H 的流水重叠？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q063.md) | 把输入切 chunk 后做双/三缓冲：下一块 H2D 与当前块 compute、上一块 D2H 重叠。 |
| 064 | [CUDA Event 与 `cudaDeviceSynchronize()` 有什么区别？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q064.md) | device synchronize 是粗粒度全设备等待；event 是 stream 时间点，可用于计时与跨 stream dependency。 |
| 065 | [Ampere 的 Async Global→Shared Copy 解决什么问题？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q065.md) | Ampere async copy 允许 global→shared 搬运与计算重叠，并减少 register 作为中转的需求。 |
| 066 | [什么是 Software Pipelining？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q066.md) | Software pipelining = 把不同迭代的 load/compute 重叠，用额外 buffer/stage 换 latency hiding。 |
| 067 | [什么是 Double Buffering / Multi-Stage Pipeline？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q067.md) | double buffering 用 A/B 两组 buffer 交替生产/消费；multi-stage 将深度扩展到 3+。 |
| 068 | [Hopper TMA 解决什么问题？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q068.md) | TMA 把多维 tensor 的地址生成和 bulk copy 卸载给硬件，适合 Hopper producer/consumer pipeline；它尤其降低大量线程用于搬运数据的指令开销。 |
| 069 | [`cuda::pipeline` / `cuda::barrier` 在 Async Pipeline 中做什么？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q069.md) | pipeline/barrier 管理 stage 状态：producer 何时可写、consumer 何时可读、buffer 何时可复用。 |
| 070 | [Kernel Fusion 为什么经常有效？什么时候会适得其反？](../questions/07-Stream-异步拷贝与-Software-Pipeline/q070.md) | fusion 减少 launch 与中间 HBM traffic，却会扩大 kernel live state，提升 register/shared pressure，甚至降低 occupancy。 |
| 071 | [优化 CUDA Kernel 的第一步是什么？](../questions/08-Nsight-Roofline-与性能诊断/q071.md) | 先测量，再定位，再改；没有 baseline 的“优化”不可证伪。 |
| 072 | [如何判断 Memory-Bound 还是 Compute-Bound？](../questions/08-Nsight-Roofline-与性能诊断/q072.md) | 先算 arithmetic intensity 并看 Roofline/SOL，再结合 DRAM/SM throughput。 |
| 073 | [Roofline Model 如何指导具体优化？](../questions/08-Nsight-Roofline-与性能诊断/q073.md) | Roofline 只告诉你性能上限受 compute 还是 bandwidth 主导；具体怎么改要结合 bytes、reuse、instruction mix、Tensor Core 使用和 scheduler counters。 |
| 074 | [Nsight Systems 与 Nsight Compute 怎么分工？](../questions/08-Nsight-Roofline-与性能诊断/q074.md) | Systems 看端到端 timeline/CPU-GPU/streams/copy/NCCL；Compute 对单 kernel 做深度计数器分析。 |
| 075 | [SM Throughput 95% 是否说明 Kernel 已经最优？](../questions/08-Nsight-Roofline-与性能诊断/q075.md) | SM throughput 高只说明某些 SM pipeline 很忙，不保证做的是最少指令/最有用工作。 |
| 076 | [DRAM Throughput 95% 意味着什么？](../questions/08-Nsight-Roofline-与性能诊断/q076.md) | DRAM 接近峰值说明很可能触到带宽 roof；下一步通常不是“再提高带宽利用率”，而是减少 bytes、提高 reuse、压缩精度或 fusion。 |
| 077 | [常见 Warp Stall Reasons 应如何解释？](../questions/08-Nsight-Roofline-与性能诊断/q077.md) | stall reason 是“为什么某 warp 当前不能 issue”的采样/统计视角。 |
| 078 | [为什么很短或 Block 很少的 Kernel，Occupancy 指标可能没意义？](../questions/08-Nsight-Roofline-与性能诊断/q078.md) | 小 grid/短 kernel 可能根本没有足够 blocks 形成稳定 occupancy，主要瓶颈是 launch、wave/tail 或并行度不足。 |
| 079 | [什么是 Speed of Light（SOL）分析？](../questions/08-Nsight-Roofline-与性能诊断/q079.md) | SOL 将 achieved throughput 相对硬件理论峰值归一化，快速告诉你 compute/memory 哪个单元最接近上限。 |
| 080 | [如何证明一个 CUDA 优化“真的有效”？](../questions/08-Nsight-Roofline-与性能诊断/q080.md) | 证明优化需要 correctness + 统计稳定的 timing + before/after counters。 |
| 081 | [为什么 GEMM 是 CUDA 性能优化的“综合大题”？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q081.md) | GEMM 把 coalescing、shared/register reuse、tiling、Tensor Core、pipeline、occupancy、epilogue 全部集中在一个 kernel，是最典型的综合性能题。 |
| 082 | [GEMM 为什么 Arithmetic Intensity 很高？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q082.md) | GEMM 的每个 A/B 元素通过 tiling 被多次用于 FMA，计算量 O(MNK) 而必要数据量增长更慢，因此可达到高 arithmetic intensity。 |
| 083 | [GEMM 为什么需要多级 Tiling？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q083.md) | 多级 tiling 对应不同硬件层级：CTA tile 管 shared reuse，warp tile 管 warp-level MMA，thread/register tile 管寄存器复用；每层都在减少下一级数据搬运。 |
| 084 | [Tensor Core 与普通 CUDA Core 的区别是什么？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q084.md) | CUDA Core 执行通用标量/向量算术，Tensor Core 针对小矩阵 MMA 提供极高吞吐。 |
| 085 | [FP32、TF32、FP16、BF16、FP8、FP4 怎么选？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q085.md) | 精度选择是 range、mantissa、带宽、Tensor Core throughput 与数值稳定性的权衡。 |
| 086 | [WMMA、PTX MMA、CUTLASS、cuBLAS 各处于什么抽象层？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q086.md) | cuBLAS 最高抽象且通常首选；CUTLASS/CuTe 允许组合高性能 kernel；WMMA/PTX MMA 更接近指令层。 |
| 087 | [CUTLASS 的核心设计思想是什么？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q087.md) | CUTLASS 的核心不是“模板很多”，而是把布局、tile、copy、MMA、pipeline、scheduler、epilogue 模块化，让架构特化策略可组合。 |
| 088 | [什么是 Warp Specialization？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q088.md) | Warp specialization = 在同一 CTA 中让不同 warp/warp-group 承担不同 pipeline 角色，例如 TMA producer 与 MMA consumer。 |
| 089 | [什么是 Persistent Kernel？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q089.md) | persistent kernel 让少量 CTA 长驻 SM，不断领取 tiles/work items，减少 launch/调度开销并改善不均匀工作负载的负载均衡；代价是自定义调度复杂。 |
| 090 | [什么是 Split-K / Stream-K？什么时候能解决 GEMM 利用率问题？](../questions/09-GEMM-Tensor-Core-与-CUTLASS/q090.md) | Split-K 把 K 维拆成多个 partial sums 并归约；Stream-K 更强调把总工作均匀切成连续工作单元以减少 tile quantization。 |
| 091 | [Hopper Thread Block Cluster 是什么？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q091.md) | Thread Block Cluster 在 block 与 grid 之间提供协作层级，使 cluster 内 blocks 可同步并使用 DSM。 |
| 092 | [什么是 Distributed Shared Memory（DSM）？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q092.md) | DSM 让 cluster 内 block 可以访问彼此的 shared-memory address space，适合跨 CTA reduction/producer-consumer；它不是 L2，也不是把所有 shared memory 变成全局共享。 |
| 093 | [TMA 与 `cp.async` 的核心差别是什么？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q093.md) | `cp.async` 仍以线程发起 copy 为主；TMA 用 tensor descriptor + 硬件地址生成做 bulk multidimensional transfer，显著降低搬运线程和地址计算开销。 |
| 094 | [为什么 Hopper GEMM 适合 Producer-Consumer Warp Specialization？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q094.md) | Hopper producer warps 负责 TMA/管线控制，consumer warps 专注 WGMMA/MMA；通过 async barrier 交换 buffer ownership，使 memory engine 与 Tensor Core 并行。 |
| 095 | [Blackwell Tensor Memory（TMEM）是什么？与 TMA 有什么区别？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q095.md) | TMEM 是 Blackwell 的 tensor memory locale，主要承接 Tensor Core accumulator/相关数据路径；TMA 是搬运引擎。 |
| 096 | [为什么 Blackwell 的 Warp Specialization 不能简单照搬 Hopper？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q096.md) | Blackwell 引入 TCGen05、TMEM、Cluster Launch Control 等机制，导致 producer/consumer 角色、accumulator buffering、scheduler 结构变化。 |
| 097 | [CUDA Graph 什么时候能明显提升性能？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q097.md) | CUDA Graph 适合重复执行、拓扑较稳定、包含许多短 kernel/API 操作的 workload，可摊薄 launch overhead。 |
| 098 | [为什么 `cudaMallocAsync` / Stream-Ordered Allocator 更适合高性能程序？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q098.md) | stream-ordered allocator 让 allocation/free 进入 stream dependency，并通过 memory pool 重用资源，减少频繁 `cudaMalloc/cudaFree` 的昂贵管理/同步成本。 |
| 099 | [CUDA Tile C++ / Tile Programming 为什么值得关注？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q099.md) | CUDA Tile C++ 将编程中心从 thread-centric 提升到 tile-centric，让编译器/runtime 承担更多 thread mapping 与专用硬件调度。 |
| 100 | [给你一个比理论峰值慢 20 倍的 CUDA Kernel，你如何系统优化？](../questions/10-Hopper-Blackwell-与-CUDA-13-x/q100.md) | 正确性→Systems 定位→Compute/Roofline 分类→Memory/Execution/Resource 因果链→单变量优化→重新测 量。 |
