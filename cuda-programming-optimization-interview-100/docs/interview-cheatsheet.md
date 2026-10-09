# CUDA 面试速查

## 五条最重要的因果链

### 1. Coalescing
`warp addresses → sectors/transactions → useful bytes / transferred bytes → effective bandwidth`

### 2. Bank Conflict
`lane shared addresses → bank mapping → conflicts/broadcast → shared throughput`

### 3. Occupancy
`register/shared/block size → resident blocks/warps → eligible warps → latency hiding`

### 4. Roofline
`FLOPs / bytes → arithmetic intensity → memory roof or compute roof → optimization direction`

### 5. Modern GEMM
`HBM → TMA/async copy → shared → register/TMEM → Tensor Core → epilogue`

## 30 秒答题模板

> 先给结论；再给 3 个硬件因果点；最后补一句 trade-off 和 profiler 验证方式。

## 常见错误

- Occupancy 越高越快。
- Shared memory 一定更快。
- 有 `if` 就一定 divergence。
- Atomic 一定慢。
- `cudaMemcpyAsync` 一定异步。
- Local memory 是片上内存。
- Tensor Core 只要用了就一定快。
