# 06 分布式推理与通信

从模型切分上升到拓扑感知的通信成本模型。

## 本章学习方法

- **问题范围**：Q051 - Q060
- **核心实验**：运行 `nvidia-smi topo -m`，对比单机 TP 与跨节点 TP 的延迟/吞吐，并关联 NCCL timeline。
- **推荐顺序**：先口述 30 秒答案，再手算公式/成本模型，最后按追问链进行模拟面试。

## 题目导航

- [Q051 Tensor Parallelism 是什么？](q051-tp-distributed.md) - ★★★★★ - `TP, distributed`
- [Q052 Pipeline Parallelism 是什么？](q052-pp-pipeline.md) - ★★★★☆ - `PP, pipeline`
- [Q053 Data Parallel inference 有什么意义？](q053-dp-replica.md) - ★★★★☆ - `DP, replica`
- [Q054 Expert Parallelism 是什么？](q054-ep-moe.md) - ★★★★★ - `EP, MoE`
- [Q055 Context Parallelism 为什么越来越重要？](q055-cp-long-context.md) - ★★★★★ - `CP, long-context`
- [Q056 TP 和 PP 怎么选？](q056-tp-pp-topology.md) - ★★★★★ - `TP, PP, topology`
- [Q057 LLM Tensor Parallel 最常出现哪些 collective？](q057-nccl-collectives.md) - ★★★★☆ - `NCCL, collectives`
- [Q058 为什么 NVLink、PCIe、InfiniBand 拓扑会直接改变最优Parallelism？](q058-topology-nvlink-ib.md) - ★★★★★ - `topology, NVLink, IB`
- [Q059 Communication/Computation Overlap 怎么做？](q059-overlap-communication.md) - ★★★★★ - `overlap, communication`
- [Q060 一个 671B MoE 模型如何做多节点部署规划？](q060-moe-system-design.md) - ★★★★★ - `MoE, system-design`
