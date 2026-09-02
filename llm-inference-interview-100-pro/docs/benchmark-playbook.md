# Benchmark Playbook

## 1. Manifest：先固定实验条件

必须记录：模型/commit、dtype/quant、runtime/commit、GPU、driver/CUDA、TP/PP/EP/CP、attention backend、KV 配置、sampling 参数、input/output length 分布、arrival pattern、concurrency、prefix reuse。

## 2. 不要只测 512→512

至少包含：

| Workload | 输入 | 输出 | 典型瓶颈 |
|---|---:|---:|---|
| Chat | 1K-4K | 200-800 | mixed |
| RAG | 8K-64K | 200-800 | prefill/KV |
| Reasoning | 1K-8K | 2K-32K | decode/KV |
| Batch offline | mixed | mixed | throughput |

## 3. 指标

请求层：TTFT/TPOT/E2E p50/p95/p99、req/s、tokens/s、Goodput。  
Scheduler：queue、running/waiting、batch size、batched tokens、preemption。  
KV：usage、hit、eviction、page waste。  
GPU/网络：SM/Tensor/HBM、kernel、NCCL、NVLink/IB、CPU launch gaps。

## 4. 方法

- warm-up 与 steady state 分开；
- open-loop 与 closed-loop 含义分清；
- 使用多个负载档位画完整曲线；
- 所有 feature 通过 on/off controlled A/B；
- 结果优先报告 SLO 约束下 Goodput，不以峰值吞吐替代生产结论。
