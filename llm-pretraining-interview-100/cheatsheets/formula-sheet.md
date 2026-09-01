# 预训练核心公式速查

> 用于面试前 15 分钟快速复盘。公式只提供“骨架”，完整解释回到对应题目。

## Attention

$$
\mathrm{Attention}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V
$$

- Q001：为什么缩放 $\sqrt{d_k}$
- Q071：为什么 attention pair 是 $O(S^2)$
- Q058/Q072：为什么 FlashAttention 优化 IO 而非把 exact dense attention 变成线性复杂度

## Causal LM

$$
L=-\sum_{t=1}^{T}\log p_\theta(x_t\mid x_{<t})
$$

## AdamW

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,\qquad
v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
$$

## Global Batch

$$
B_{global}=B_{micro}\times DP\times N_{acc}
$$

$$
Tokens/update=B_{global}\times S
$$

## Dense 训练 FLOPs 粗估

$$
C\approx 6ND
$$

其中 $N$ 是参数量，$D$ 是训练 tokens；这是量级估计而非精确 profiler 结果。

## KV Cache 粗估

$$
M_{KV}\approx B\times S\times L\times2\times h_{kv}\times d_h\times bytes(dtype)
$$

## 分布式 GPU 数

在常见独立并行轴配置的简化表达中：

$$
N_{GPU}=TP\times PP\times CP\times EP\times DP
$$

实际 process-group 关系需以框架约束为准。

## MFU

$$
MFU=\frac{\text{actual model FLOPs/s}}{\text{accelerator peak FLOPs/s}}
$$
