# CUDA Examples

这些示例用于面试白板与 microbenchmark 起点，不声称替代 CUB/cuBLAS/CUTLASS 的生产实现。

- `reduction.cu` - Q051/Q053
- `transpose.cu` - Q027/Q033/Q034/Q056
- `tiled_gemm.cu` - Q057/Q058/Q081-Q083
- `grid_stride.cu` - Q006

建议自己补齐 host harness、CUDA Event timing 和 correctness check，再用 Nsight Compute 对照题解验证。

- `warp_reduce.cu` - Q038/Q040/Q053
- `blelloch_scan.cu` - Q054
- `histogram_shared.cu` - Q055
- `stream_overlap.cu` - Q061-Q063


## 与 100 题的对应关系

| Example | Questions | 验证目标 |
|---|---|---|
| `grid_stride.cu` | Q006, Q050 | grid-stride 与 block/grid 搜索 |
| `reduction.cu` | Q051-Q053 | shared/tree/warp reduction 演进 |
| `warp_reduce.cu` | Q038-Q040, Q053 | shuffle + active mask |
| `blelloch_scan.cu` | Q054, Q059 | work-efficient scan 与 compaction 基础 |
| `histogram_shared.cu` | Q055 | privatization 与 atomic contention |
| `transpose.cu` | Q027, Q033-Q034, Q056 | coalescing + bank conflict |
| `tiled_gemm.cu` | Q057-Q058, Q081-Q083 | tiling 与 arithmetic intensity |
| `stream_overlap.cu` | Q061-Q064 | streams、pinned memory、copy/compute overlap |

### 推荐实验记录模板

每次修改示例都建议同时记录：

```text
GPU / CC:
CUDA / Driver:
Compiler flags:
Shape / DType:
Warmup / Iterations:
Correctness tolerance:
Median / P95:
Key Nsight metrics:
Hypothesis:
Conclusion:
```

示例的目标不是“展示一个看起来优化过的 kernel”，而是为题解中的性能因果链提供可复现证据。
