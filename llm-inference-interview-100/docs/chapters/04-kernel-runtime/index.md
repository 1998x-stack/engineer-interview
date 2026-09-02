# 04 CUDA、Attention Kernel 与 Runtime

从“GPU 很忙”深入到 IO、tile、launch、shape 与 kernel critical path。

## 本章学习方法

- **问题范围**：Q031 - Q040
- **核心实验**：固定请求，逐项关闭 CUDA Graph、compile、fusion/attention backend，做 controlled A/B。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q031 FlashAttention 为什么更快？](q031-flashattention-io.md) - ★★★★★ - `FlashAttention, IO`
- [Q032 FlashAttention-2 与 FlashAttention-3 的思路有什么差异？](q032-flashattention3-hopper.md) - ★★★★★ - `FlashAttention3, Hopper`
- [Q033 FlashAttention 与 FlashInfer 有什么区别？](q033-flashinfer-attention-backend.md) - ★★★★☆ - `FlashInfer, attention-backend`
- [Q034 Kernel Fusion 为什么能提升性能？](q034-kernel-fusion-cuda.md) - ★★★★☆ - `kernel-fusion, CUDA`
- [Q035 CUDA Graph 为什么适合 Decode？](q035-cuda-graph-decode.md) - ★★★★★ - `CUDA-Graph, decode`
- [Q036 torch.compile / Triton 在推理优化中解决什么？](q036-torch-compile-triton.md) - ★★★★☆ - `torch.compile, Triton`
- [Q037 什么情况下 Kernel Launch Overhead 会成为瓶颈？](q037-launch-overhead-cuda.md) - ★★★☆☆ - `launch-overhead, CUDA`
- [Q038 为什么 Prefill GEMM 和 Decode GEMM 优化完全不同？](q038-gemm-prefill-decode.md) - ★★★★★ - `GEMM, prefill-decode`
- [Q039 为什么 Tensor Core 对矩阵 Shape 很敏感？](q039-tensor-core-shape.md) - ★★★★☆ - `Tensor-Core, shape`
- [Q040 Nsight 里看到 GPU Util=100%，为什么模型仍可能很慢？](q040-nsight-profiling.md) - ★★★★★ - `Nsight, profiling`
