# CUDA Programming Optimization Interview - 100 Questions

> 面向 CUDA / GPU Kernel Engineer / HPC / AI Infra / LLM Inference / GPU Compiler 的系统面试题库。

本仓库将《CUDA 编程优化面试 100 题 · 专业版》拆成 **100 个独立 Markdown**，并在 PDF 基线内容上加入两层性能工程化扩展：第一层是硬件因果链、架构差异、Profiler 证据、microbenchmark、评分 Rubric 与自测；第二层 **Professional V2** 为 100/100 题逐题加入专属定量模型、代码/白板片段、Nsight 证据链、架构迁移、可复现实验与深挖追问树。

## 为什么这个仓库不是“背答案题库”

CUDA 面试真正区分度高的部分，不是记住“shared memory 快”“occupancy 越高越好”之类口号，而是回答：

- 为什么？
- 在什么条件下？
- 代价是什么？
- 换 GPU 架构是否仍成立？
- 用什么 Nsight 指标证明？

统一心智模型：

```text
Performance = f(
  Memory Efficiency,
  Compute Efficiency,
  Parallelism,
  Latency Hiding,
  Resource Balance
)
```

## 目录

| 章 | 主题 | 题号 | 能力目标 |
|---:|---|---:|---|
| 1 | [CUDA 执行模型与 SIMT](questions/01-CUDA-执行模型与-SIMT/README.md) | 1-10 | 从线程层级映射到 warp/SM 调度与同步语义。 |
| 2 | [GPU Memory Hierarchy](questions/02-GPU-Memory-Hierarchy/README.md) | 11-20 | 理解 register/shared/L1/L2/HBM 与主机内存的数据移动成本。 |
| 3 | [Global Memory 与 Coalescing](questions/03-Global-Memory-与-Coalescing/README.md) | 21-30 | 把 warp 地址模式翻译成 memory transactions 与有效带宽。 |
| 4 | [Shared Memory、Warp 与 Divergence](questions/04-Shared-Memory-Warp-与-Divergence/README.md) | 31-40 | 掌握 bank mapping、warp-level primitive 与控制流效率。 |
| 5 | [Occupancy、Register 与 Latency Hiding](questions/05-Occupancy-Register-与-Latency-Hiding/README.md) | 41-50 | 理解资源约束、TLP/ILP、spill 与 occupancy 的真实关系。 |
| 6 | [经典 CUDA Kernel 现场编程](questions/06-经典-CUDA-Kernel-现场编程/README.md) | 51-60 | Reduction、Scan、Histogram、Transpose、GEMM、Compaction。 |
| 7 | [Stream、异步拷贝与 Software Pipeline](questions/07-Stream-异步拷贝与-Software-Pipeline/README.md) | 61-70 | 构建 copy/compute overlap、多 stage pipeline 与 fusion。 |
| 8 | [Nsight、Roofline 与性能诊断](questions/08-Nsight-Roofline-与性能诊断/README.md) | 71-80 | 从 timeline 到 counters 建立可证伪的性能工程闭环。 |
| 9 | [GEMM、Tensor Core 与 CUTLASS](questions/09-GEMM-Tensor-Core-与-CUTLASS/README.md) | 81-90 | 分层 tiling、Tensor Core、persistent/Stream-K 与 warp specialization。 |
| 10 | [Hopper、Blackwell 与 CUDA 13.x](questions/10-Hopper-Blackwell-与-CUDA-13-x/README.md) | 91-100 | Cluster/DSM/TMA/TMEM/CUDA Tile 与架构特化优化。 |

## 推荐学习路线

### Round 1 - 基础执行模型（Q001-Q040）
目标：能在 30-60 秒内讲清 warp、coalescing、bank conflict、divergence。

### Round 2 - 资源与现场编码（Q041-Q060）
目标：能解释 occupancy/register trade-off，并手写 Reduction、Scan、Histogram、Transpose、Tiled GEMM。

### Round 3 - Pipeline 与性能诊断（Q061-Q080）
目标：会用 Streams/Async/Pipeline，并能用 Nsight Systems → Nsight Compute → Roofline 建立因果链。

### Round 4 - 现代 CUDA（Q081-Q100）
目标：掌握 CUTLASS、Tensor Core、TMA、Warp Specialization、DSM、TMEM、CUDA Tile。

## Repository Layout

```text
cuda-programming-optimization-interview-100/
├── README.md
├── questions/                  # 10 chapters / 100 markdowns
├── examples/                   # 可编译 CUDA 示例与 microbenchmarks
├── docs/
│   ├── CUDA_编程优化面试100题_专业版.pdf
│   ├── pdf-transcript.txt
│   ├── preface.md / study-map.md
│   ├── references.md / appendices
│   ├── interview-cheatsheet.md
│   └── profiling-playbook.md
├── scripts/
│   ├── validate_repo.py
│   ├── build_summary.py
│   ├── enrich_questions_v2.py
│   └── enrich_chapter_readmes_v2.py
├── SUMMARY.md                  # 全 100 题索引
├── CONTRIBUTING.md
└── .github/workflows/validate.yml
```

## 如何使用每一道题

每个题解统一包含：

1. **PDF 基线题解**：保留原书的考察意图、思路、标准回答、Gotchas、追问和代码；
2. **深入分析**：解释底层性能因果；
3. **架构视角**：说明稳定原理与 Ampere/Hopper/Blackwell 差异；
4. **30 秒 / 2 分钟 / 深挖**：训练不同面试节奏；
5. **实战验证**：要求用 microbenchmark + Nsight 证明；
6. **评分 Rubric**：从背术语到专家级性能工程；
7. **自测题**：让每题可以独立复习；
8. **Professional V2 专属增强**：每题都有不同的硬件机制、公式、代码、Profiler 指标、实验和追问，不再使用通用模板代替内容。

## 原始 PDF

[下载 / 查看仓库内 PDF](docs/CUDA_编程优化面试100题_专业版.pdf)

## 技术口径

仓库以 CUDA 13.3 Programming/Best Practices 文档作为 PDF 的基础口径，并将 CUTLASS/Hopper/Blackwell 内容与现代官方资料连接。技术细节会随 GPU 架构、Toolkit 和 CUTLASS 版本演进，因此题解强调“稳定性能原理 + 目标架构验证”。

## 验证

```bash
python scripts/validate_repo.py
```

校验：100 个题目文件是否存在、题号是否连续、内部 Markdown 链接、PDF 是否包含在仓库、SUMMARY 是否覆盖全部题目。

## 内容来源与边界

- PDF 正文为本仓库内容基线。
- NVIDIA 官方 CUDA / Nsight / CUTLASS / PTX 文档用于技术参考与扩展。
- 公开面经只用于核验“题型出现过”，不把匿名面经回答当技术事实。
- `docs/pdf-transcript.txt` 保留 PDF 文本抽取版本，方便检索与差异检查。

## License

当前仓库未主动授予开源再分发许可；详见 [LICENSE](LICENSE)。如准备公开发布，可根据你的需要改为适合代码与教育内容的双许可证方案。


## V2 内容质量标准

详细规范：[Professional V2 Content Standard](docs/v2-content-standard.md)


每个 `qNNN.md` 至少满足：

- PDF 基线题解保留，可追溯原始内容；
- 一段**问题专属**的硬件机制解释；
- 至少一个定量关系/公式/数量级；
- 一个可在白板上讨论的代码或伪代码片段；
- 一组与问题直接相关的 Nsight / 编译器证据；
- Ampere/Hopper/Blackwell 中稳定原理与架构特定实现的边界；
- 一个可复现实验，而不是“建议 profile”这种空泛建议；
- 三个问题专属的深挖追问。

CI 会检查 V2 marker、必备小节、最低内容量与内部链接，防止后续贡献把题解退化成短答案。
