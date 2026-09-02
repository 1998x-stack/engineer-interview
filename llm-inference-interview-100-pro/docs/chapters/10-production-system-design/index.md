# 10 Benchmark、生产部署与系统设计

把所有局部优化放到 SLO、容量、成本、可观测性与故障证据链中。

## 本章学习方法

- **问题范围**：Q091 - Q100
- **核心实验**：建立可重复的 benchmark manifest：模型 revision、runtime commit、driver/CUDA、拓扑、参数、流量分布与结果。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q091 你会如何 Benchmark 一个 LLM Serving Engine？](q091-benchmark-serving.md) - ★★★★★ - `benchmark, serving`
- [Q092 为什么用固定 512→512 benchmark 很危险？](q092-benchmark-workload.md) - ★★★★☆ - `benchmark, workload`
- [Q093 为什么 p99 比平均 latency 更重要？](q093-p99-tail-latency.md) - ★★★★★ - `p99, tail-latency`
- [Q094 Throughput 和 Goodput 的区别是什么？](q094-goodput-slo.md) - ★★★★★ - `goodput, SLO`
- [Q095 如何计算每百万输出 token 成本？](q095-cost-tco.md) - ★★★★☆ - `cost, TCO`
- [Q096 LLM Serving 如何做 Admission Control 和 Autoscaling？](q096-admission-control-autoscaling.md) - ★★★★★ - `admission-control, autoscaling`
- [Q097 线上发生 KV Cache OOM，你怎么处理？](q097-oom-kv-operations.md) - ★★★★★ - `OOM, KV, operations`
- [Q098 生产 LLM Server 最重要的监控指标有哪些？](q098-observability-metrics.md) - ★★★★★ - `observability, metrics`
- [Q099 系统设计题：8×H100，部署一个 70B Chat Model，你怎么设计？](q099-system-design-h100-70b.md) - ★★★★★ - `system-design, H100, 70B`
- [Q100 终极综合题：线上模型突然慢了 30%，你如何定位？](q100-debugging-production-systematic.md) - ★★★★★ - `debugging, production, systematic`
