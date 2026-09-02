# vLLM / SGLang / TensorRT-LLM 选型矩阵

> 这是工程决策框架，不是绝对排名。feature/status 更新快，最终以目标版本文档 + 实测为准。

| 维度 | vLLM | SGLang | TensorRT-LLM |
|---|---|---|---|
| 定位 | 通用高吞吐 serving/runtime | cache/program-aware serving | NVIDIA 深度优化 inference stack |
| KV / Prefix | PagedAttention、prefix caching | Radix/Unified Radix、HiCache | paged KV、reuse/offload/connector |
| Scheduler | continuous batching、chunked prefill、V1 unified token budget | cache-aware / radix-aware、多种调度 | IFB/overlap scheduler |
| Kernel | 多 backend：FA/FlashInfer/TRTLLM-GEN/Triton 等 | FlashInfer/Triton/CuTe 等 | NVIDIA 专用 kernels / compiler stack |
| Quant | 多格式 | 多 backend，依模型/硬件 | FP8/FP4/AWQ/GPTQ/KV quant 深度支持 |
| P/D | 支持 disaggregated serving | 支持 PD + hierarchical KV | 支持 disaggregated serving + KV transmission |
| 适合 | 快速模型覆盖、研究到生产 | prefix reuse、agent/structured、高级 cache | NVIDIA 平台极致优化/产品化 |

## 决策顺序

1. 模型结构：Dense / MoE / MLA / VLM；
2. GPU 与拓扑：A100/H100/B200、单机/多机；
3. workload：Chat/RAG/Reasoning/offline；
4. SLO：TTFT/TPOT/p99；
5. cache reuse 与 context length；
6. quantization；
7. parallelism；
8. 运维与可观测性；
9. 最终统一 benchmark。
