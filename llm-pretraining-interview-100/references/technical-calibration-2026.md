# 2026 技术校准笔记

> 本页记录本 Repo 相对原书稿新增的“当前官方实现语义”校准；不替代各题原始论文。

## Megatron Core 并行语义

当前 Megatron Core 官方文档将常见并行策略按目标区分为：

- DP：batch dimension；
- TP：individual layers；
- PP：model depth；
- CP：sequence/context length；
- EP：MoE experts；
- Megatron-FSDP：parameters/gradients/optimizer states 等 model state sharding。

官方策略指南强调先满足内存约束，再尽量降低高频 model-parallel 通信并扩大 DP；实际配置需要结合 topology 与具体模型。

来源：<https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html>

## Context Parallel

CP 与传统 SP 不同：CP 沿 sequence 维切分网络输入和全层 activation；Attention 因 Query 需要全局 KV 而引入额外通信。长上下文下 CP 的核心价值是按 CP degree 降低 per-rank activation footprint。

来源：<https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/context_parallel.html>

## MoE

当前 Megatron Core 文档把 MoE 性能瓶颈明确拆为 Memory Wall、Communication Wall 与 Compute Efficiency Wall，并提供 EP communication overlap、grouped GEMM、parallel folding 等实现方向。它说明“active FLOPs 下降”并不自动等于端到端更快。

来源：<https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/features/moe.html>

## DeepSeek-V3

DeepSeek-V3 技术报告给出的关键预训练设计包括 DeepSeekMoE、MLA、auxiliary-loss-free load balancing 与 multi-token prediction；报告给出 671B total / 37B activated per token 的架构规模。

来源：<https://arxiv.org/abs/2412.19437>

## Qwen3

Qwen3 技术报告覆盖 dense 与 MoE 模型族，项目中的数据、MoE、长上下文题会将其作为技术校准材料之一。

来源：<https://arxiv.org/abs/2505.09388>

## FlashAttention

FlashAttention 是 IO-aware 的 exact attention：通过 tiling 与更少的 HBM↔SRAM 数据搬运改善速度与显存，而不是把 dense exact attention 的数学二次复杂度改成线性。

来源：<https://arxiv.org/abs/2205.14135>
