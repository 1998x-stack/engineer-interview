# 全书知识地图

```text
LLM Inference
│
├── Workload: Prefill / Decode / TTFT / TPOT
├── Memory: Weights / KV / Paging / Prefix / Hierarchical Cache
├── Scheduler: Continuous Batching / Chunked Prefill / Goodput / P-D
├── Kernel: Attention / GEMM / Fusion / CUDA Graph / compile
├── Precision: INT8/4 / FP8/4 / KV Quant
├── Distributed: TP / PP / DP / EP / CP / NCCL
├── Decode Accel: Spec Decode / N-Gram / Medusa / EAGLE / MTP
├── Model-System: MoE / MLA / Expert traffic
├── Runtime: vLLM / SGLang / TensorRT-LLM
└── Production: Benchmark / p99 / Cost / Observability / Debug
```

## 一条贯穿 100 题的推理链

**性能现象 → 指标分解 → 成本模型 → 关键路径 → 优化机制 → 代价/边界 → Controlled Experiment → SLO/Goodput 验收。**
