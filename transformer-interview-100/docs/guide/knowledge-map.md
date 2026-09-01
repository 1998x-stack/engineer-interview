# 知识地图：把 100 题连成 6 条因果链

> Transformer 面试不是 100 个孤岛。真正稳定的知识结构是“一个设计为什么产生下一个设计”。

## 链 1 · Attention 数学 → GPU Kernel

```text
Dot Product Variance
    ↓
1/sqrt(dk)
    ↓
Stable Softmax
    ↓
Mask Semantics
    ↓
Multi-Head
    ↓
O(Td² + T²d)
    ↓
HBM IO Bottleneck
    ↓
Online Softmax / FlashAttention
```

核心题：Q011–Q024、Q080–Q084、Q090–Q091。

**关键迁移能力**：给你一个新 attention 公式，能立刻写 shape、归一化轴、复杂度和数值边界。

## 链 2 · “集合” → 序列 → 长上下文

```text
Permutation Equivariance
    ↓
Absolute Position
    ↓
Relative Position
    ↓
RoPE / ALiBi
    ↓
Interpolation / Scaling
    ↓
Technical Context != Effective Context
```

核心题：Q010、Q025–Q034。

**关键迁移能力**：任何 position 技术都问“位置进入哪里、训练外如何验证、cache offset 是否一致”。

## 链 3 · 深度 → 稳定训练

```text
Residual Identity Path
    ↓
LayerNorm
    ↓
Pre-LN / RMSNorm
    ↓
Initialization
    ↓
Warmup / AdamW
    ↓
BF16 / Grad Clip
```

核心题：Q004–Q005、Q035–Q043、Q057–Q064。

**关键迁移能力**：loss spike 时能从 layer-wise activation/gradient 找首个异常，而不是只会调 LR。

## 链 4 · Token Mixing → Channel Compute → Sparse Capacity

```text
Attention = Token Mixing
FFN = Channel Mixing
    ↓
Expansion Ratio
    ↓
GELU / SiLU
    ↓
SwiGLU
    ↓
MoE
    ↓
Router + All-to-All
```

核心题：Q009、Q039–Q042、Q087–Q088。

**关键迁移能力**：比较 FFN 变体时先对齐参数/FLOPs，再谈质量。

## 链 5 · CLM → Incremental Decode → Serving

```text
Causal LM
    ↓
Training Parallel / Decode Serial
    ↓
KV Cache
    ↓
KV Memory
    ↓
GQA / MQA
    ↓
Paged KV
    ↓
Continuous Batching
    ↓
Speculative Decoding
```

核心题：Q049–Q050、Q067–Q079。

**关键迁移能力**：任何 serving 优化都分 TTFT 与 TPOT，并同时算 KV 与 scheduler。

## 链 6 · 单卡公式 → 分布式系统

```text
Params / FLOPs / Activation
    ↓
TP / DP / PP / CP
    ↓
HBM / NVLink / Network
    ↓
Quantization
    ↓
SLA / Goodput / P99
```

核心题：Q065–Q066、Q076、Q085、Q089、System Design。

## 一个统一的分析坐标系

遇到任何 Transformer 问题都可以填这张表：

| 层 | 问题 |
|---|---|
| Math | 函数到底是什么？ |
| Shape | 哪些轴交互？ |
| Params | 哪些矩阵带参数？ |
| FLOPs | train/prefill/decode 各多少？ |
| Memory | activation / KV / weights？ |
| IO | HBM 读写是否主导？ |
| Communication | TP/DP/EP collective？ |
| Numerical | softmax/norm/dtype 边界？ |
| Quality | 是否改变模型函数/归纳偏置？ |
| Verify | 用什么反例/benchmark 证伪？ |

能用这张表分析陌生论文，才是这套题库的最终目标。
