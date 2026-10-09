# 附录 C｜参考资料与题源说明

正文技术事实优先依据 NVIDIA 官方 CUDA / Nsight / CUTLASS / PTX 文档；公开面经仅用于核验“题型确实出现过”，不把匿名面经答案当技术权威。

完整 R1-R18 映射见 [references.md](references.md)。

## 公开面经可核验题型

- CUDA synchronization、reduction 实现、memory hierarchy：对应 Q007/Q008、Q051-Q053、Q011。
- software pipelining、warp specialization：对应 Q066、Q088。
- 其余题目按 NVIDIA 官方性能指南、现代 CUDA/CUTLASS 能力与 GPU 岗常见深挖方式构造成高频真题型。

## 版本说明

PDF 技术口径更新至 2026-09：CUDA 13.3 文档、CUDA Tile C++、当前 CUTLASS/Hopper/Blackwell 文档。GPU 微架构细节会随 Toolkit/driver/architecture 演进，面试时应优先解释稳定的性能原理，再补充具体架构能力。

## 最终自检

如果你能在没有 PPT 的情况下：

- 从 warp 地址模式解释 coalescing；
- 从 bank mapping 解释 padding；
- 从 resource equation 解释 occupancy；
- 从 Roofline + stall counters 解释瓶颈；
- 从 HBM → shared → register/TMEM → Tensor Core 解释现代 GEMM；

就已经跨过“只会写 CUDA”到“会做 GPU 性能工程”的门槛。
