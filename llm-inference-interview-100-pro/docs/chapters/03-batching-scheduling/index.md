# 03 Batching 与 Scheduling

把 scheduler 看作受 KV、token budget 与 SLO 约束的在线资源分配器。

## 本章学习方法

- **问题范围**：Q021 - Q030
- **核心实验**：用 Poisson/突发流量分别压测，比较 FCFS、cache-aware、chunked prefill 或不同 token budget。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q021 Static Batching 和 Continuous Batching 有什么区别？](q021-continuous-batching-scheduler.md) - ★★★★★ - `continuous-batching, scheduler`
- [Q022 Orca 的 Iteration-level Scheduling 为什么重要？](q022-orca-scheduling.md) - ★★★★☆ - `Orca, scheduling`
- [Q023 为什么 Prefill 会干扰 Decode？](q023-prefill-interference-itl.md) - ★★★★★ - `prefill-interference, ITL`
- [Q024 Chunked Prefill 为什么能解决这个问题？](q024-chunked-prefill-sarathi.md) - ★★★★★ - `chunked-prefill, Sarathi`
- [Q025 Scheduler 中的 max_num_batched_tokens 本质是什么？](q025-vllm-token-budget.md) - ★★★★★ - `vLLM, token-budget`
- [Q026 FCFS 和 Cache-aware Scheduling 怎么选？](q026-scheduling-cache-aware.md) - ★★★★☆ - `scheduling, cache-aware`
- [Q027 如何解决调度中的 Starvation？](q027-fairness-starvation.md) - ★★★★☆ - `fairness, starvation`
- [Q028 KV Cache 不够时应该 Swap、Recompute 还是 Reject？](q028-preemption-kv.md) - ★★★★★ - `preemption, KV`
- [Q029 为什么生产系统应该优化 Goodput，而不是最高 Throughput？](q029-goodput-production.md) - ★★★★★ - `goodput, production`
- [Q030 什么是 Prefill–Decode Disaggregation？](q030-pd-disaggregation-distserve.md) - ★★★★★ - `PD-disaggregation, DistServe`
