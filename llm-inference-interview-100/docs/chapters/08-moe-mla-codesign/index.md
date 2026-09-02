# 08 MoE、MLA 与模型-系统协同

理解现代模型结构如何重写 KV、GEMM、routing 与通信的性能模型。

## 本章学习方法

- **问题范围**：Q071 - Q080
- **核心实验**：对 MoE workload 记录每 expert token histogram、All-to-All 时间和 grouped GEMM shape，随并发变化分析。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q071 为什么 MoE 理论 FLOPs 很低，线上 latency 却未必低？](q071-moe-latency.md) - ★★★★★ - `MoE, latency`
- [Q072 Expert Parallel 和 Tensor Parallel 的本质区别？](q072-ep-tp-moe.md) - ★★★★★ - `EP, TP, MoE`
- [Q073 MoE Expert Load Imbalance 为什么严重？](q073-load-balance-moe.md) - ★★★★★ - `load-balance, MoE`
- [Q074 All-to-All 为什么是 MoE 推理的关键瓶颈？](q074-alltoall-moe.md) - ★★★★★ - `AllToAll, MoE`
- [Q075 Shared Expert 有什么意义？](q075-shared-expert-moe.md) - ★★★★☆ - `shared-expert, MoE`
- [Q076 MLA 与 GQA 谁更省 KV Cache？](q076-mla-gqa-kv.md) - ★★★★★ - `MLA, GQA, KV`
- [Q077 DeepSeek 类模型为什么对推理框架提出新要求？](q077-deepseek-framework.md) - ★★★★★ - `DeepSeek, framework`
- [Q078 MoE 量化为什么比 Dense 模型更复杂？](q078-moe-quant-calibration.md) - ★★★★☆ - `MoE-quant, calibration`
- [Q079 Wide Expert Parallelism 为什么可能比大规模 TP 更适合 MoE？](q079-wide-ep-moe.md) - ★★★★☆ - `wide-EP, MoE`
- [Q080 MoE 为什么低并发和高并发性能差异特别大？](q080-moe-batching.md) - ★★★★★ - `MoE, batching`
