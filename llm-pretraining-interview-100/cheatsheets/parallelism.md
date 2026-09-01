# LLM 并行策略速查

| 维度 | 切什么 | 典型通信 | 主要解决 |
|---|---|---|---|
| DP | batch | gradient All-Reduce / Reduce-Scatter | 数据吞吐 |
| TP | layer tensor | All-Reduce / All-Gather / Reduce-Scatter | 单层太大 |
| PP | depth | P2P activation | 模型太深 |
| SP | 局部算子 sequence activation | 与 TP 相关 AG/RS | activation/TP 配套 |
| CP | 全网络 sequence/context | attention KV 交换 | 长上下文 activation |
| EP | experts | token All-to-All | MoE expert 分布 |
| FSDP/ZeRO | model states | parameter gather / grad RS 等 | model-state memory |

## 面试画图模板

每种并行都回答五问：

1. 哪个维度被切？
2. 每个 rank 长期保存什么？
3. forward 在哪里通信？
4. backward 在哪里通信？
5. 最优映射为什么依赖 NVLink/NVSwitch/跨节点网络？
