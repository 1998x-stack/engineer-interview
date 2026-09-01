# Transformer 高频公式速查 · Professional Cheatsheet

> 考前用来“快速恢复推导”，不是替代正文。

## 1. Attention

### Scaled Dot-Product

\[
Attention(Q,K,V)=softmax\left(\frac{QK^T}{\sqrt{d_k}}+M\right)V
\]

Shape：

\[
Q:[B,H_q,T_q,D_h],\quad K,V:[B,H_{kv},T_k,D_h]
\]

标准 MHA 时 $H_q=H_{kv}$。

### Score / Output

\[
S=QK^T:[B,H,T_q,T_k]
\]

softmax 通常沿最后的 key 轴 $T_k$。

### Attention Layer Cost

QKV/O projection：

\[
O(Td^2)
\]

score + weighted value：

\[
O(T^2d)
\]

合计主项：

\[
O(Td^2+T^2d)
\]

## 2. Multi-Head 参数量

标准：

\[
W_Q,W_K,W_V,W_O\in\mathbb R^{d\times d}
\]

主参数：

\[
\approx4d^2
\]

经典 FFN $d_{ff}=4d$：

\[
Params_{FFN}\approx 2dd_{ff}=8d^2
\]

## 3. Stable Softmax

\[
softmax(x_i)=\frac{e^{x_i-m}}{\sum_j e^{x_j-m}},\quad m=\max_jx_j
\]

**边界**：一整行全部被 mask 时需显式定义行为，避免 NaN。

## 4. Position

### Sinusoidal

\[
PE(pos,2i)=\sin(pos/10000^{2i/d})
\]

\[
PE(pos,2i+1)=\cos(pos/10000^{2i/d})
\]

### RoPE

\[
q_m'=R_mq,\quad k_n'=R_nk
\]

\[
(q_m')^Tk_n'=q^TR_{n-m}k
\]

### ALiBi

概念式：

\[
score_{ij}=q_i^Tk_j-m_h\cdot distance(i,j)
\]

### Position Interpolation

\[
p'=p\frac{T_{train}}{T_{new}}
\]

## 5. Norm / Residual

### LayerNorm

\[
LN(x)=\gamma\frac{x-\mu}{\sqrt{\sigma^2+\epsilon}}+\beta
\]

### RMSNorm

\[
RMS(x)=\sqrt{\frac1d\sum_i x_i^2+\epsilon}
\]

\[
RMSNorm(x)=\gamma\frac{x}{RMS(x)}
\]

### Pre-Norm

\[
x_{l+1}=x_l+F(Norm(x_l))
\]

### Residual Jacobian

\[
\frac{\partial(x+F(x))}{\partial x}=I+J_F
\]

## 6. FFN / SwiGLU

普通 FFN：

\[
FFN(x)=W_2\phi(W_1x)
\]

SwiGLU：

\[
FFN(x)=[SiLU(xW_g)\odot(xW_u)]W_d
\]

## 7. Language Modeling

Causal LM：

\[
P(x_{1:T})=\prod_{t=1}^{T}P(x_t\mid x_{<t})
\]

NLL：

\[
\mathcal L=-\sum_t\log P(x_t\mid x_{<t})
\]

Perplexity：

\[
PPL=\exp(\text{average NLL})
\]

## 8. KV Cache

\[
\boxed{M_{KV}=2LBTH_{kv}D_h\cdot bytes}
\]

手算顺序：

`K/V 两份 → layers → tokens → KV heads → head dim → dtype bytes → GiB`

### 示例

$L=32,T=32768,H_{kv}=8,D_h=128,B=1,BF16$：约 **4.0 GiB**。

## 9. Optimizer

### Gradient Clip

\[
g\leftarrow g\cdot\min(1,c/\|g\|)
\]

### AdamW 概念式

\[
\theta\leftarrow(1-\eta\lambda)\theta-\eta\cdot AdamUpdate
\]

## 10. Global Batch

\[
B_{global}=B_{micro}\times AccumSteps\times DP
\]

## 11. MoE

总专家 $E$，每 token 激活 top-$k$：总参数随 $E$ 扩大，但每 token expert compute 主要随 $k$ 变化；额外系统成本来自 router 与 all-to-all。

## 12. Online Softmax 合并

两块统计量 $(m_a,l_a)$、$(m_b,l_b)$：

\[
m=\max(m_a,m_b)
\]

\[
l=e^{m_a-m}l_a+e^{m_b-m}l_b
\]

这是 FlashAttention 分块 exact softmax 的关键基础。

## 面试公式自检

每个公式再补：

1. shape；
2. normalization axis；
3. parameter/FLOPs；
4. numerical edge；
5. train vs decode 差异。
