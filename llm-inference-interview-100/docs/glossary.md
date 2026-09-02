# 术语表

| 缩写/术语 | 解释 |
|---|---|
| TTFT | Time To First Token，首 token 延迟 |
| TPOT | Time Per Output Token，输出 token 平均时间 |
| ITL | Inter-Token Latency，token 间延迟 |
| Goodput | 满足 SLO 的有效吞吐 |
| KV Cache | 保存历史 Key/Value，避免自回归重复计算 |
| PagedAttention | 分页管理 KV Cache 的 serving 思想 |
| GQA | Grouped-Query Attention，多个 Q head 共享较少 KV head |
| MLA | Multi-head Latent Attention，低维 latent KV 表示 |
| TP/PP/DP | Tensor/Pipeline/Data Parallelism |
| EP | Expert Parallelism |
| CP | Context Parallelism |
| IFB | In-Flight Batching，动态/连续 batching 语境常见术语 |
| Spec Decode | Speculative Decoding，proposal + target verify |
| P/D | Prefill/Decode Disaggregation |
| HBM | High Bandwidth Memory |
| NCCL | NVIDIA Collective Communications Library |
