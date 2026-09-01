---
id: "Q040"
title: "写出 Scaled Dot-Product Attention，并解释每一步。"
chapter: 5
chapter_name: "Transformer 核心"
difficulty: "★★☆"
frequency: "极高频"
priority: "S"
pdf_page: 30
tags:
  - deep-learning
  - interview
  - transformer
  - attention
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q040 · 写出 Scaled Dot-Product Attention，并解释每一步。

> **章节：** Transformer 核心
> **难度：** ★★☆ ｜ **频度：** 极高频 ｜ **优先级：** S（Top 30）
> **PDF 对应：** 第 30 页附近

## 面试官在考什么

Attention 公式、shape 与语义。

**高质量回答标准：** 能写公式与 shape；能给复杂度；能把训练、显存、kernel 与 serving 影响串起来。

## 一句话结论

先用 QK^T 计算每个 query 对所有 key 的相似度，除以 sqrt(d_k) 控制尺度，加 mask 后 softmax 得到权重，最后对 V 加权求和。

## 60–90 秒面试回答

先用 QK^T 计算每个 query 对所有 key 的相似度，除以 sqrt(d_k) 控制尺度，加 mask 后 softmax 得到权重，最后对 V 加权求和。
Attention(Q,K,V)=softmax(QKᵀ/√d_k)V

## 深度解析

- Q:[B,H,Tq,Dh]，K:[B,H,Tk,Dh]，score:[B,H,Tq,Tk]。
- softmax 通常沿 key 维。
- V 决定真正被聚合的内容，K 决定如何被匹配。



## 数学、Shape 与复杂度

Scaled dot-product attention：

$$
\mathrm{Attn}(Q,K,V)=\mathrm{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}+M\right)V.
$$

典型 shape：`Q,K,V=[B,H,T,Dh]`，score 为 `[B,H,T,T]`。

## 工程实现 / PyTorch 验证

```python
import math
import torch

def attention(q, k, v, mask=None):
    scores = q @ k.transpose(-2, -1) / math.sqrt(q.size(-1))
    if mask is not None:
        scores = scores.masked_fill(~mask, torch.finfo(scores.dtype).min)
    probs = torch.softmax(scores.float(), dim=-1).to(q.dtype)
    return probs @ v
```

### 推荐验证协议

手写 attention 与 `torch.nn.functional.scaled_dot_product_attention` 对拍，覆盖 causal/padding、fp16、极端 logits。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- Transformer 题默认同时回答：公式、shape、复杂度、数值稳定和 serving 影响。
- 区分“计算优化”和“内存管理”：FlashAttention、GQA、KV Cache、PagedAttention 分别解决不同瓶颈。

### 边界条件与反例

- 注意 mask 的广播 shape、全 mask 行、长序列 OOM、softmax 精度和 causal/padding mask 组合。

## 面试官连续追问

- cross-attention 时 Q/K/V 来自哪里？
- 如果 softmax 温度变化会怎样？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** softmax 维度写错。
- **易错：** K 转置维度不正确。

### 3 分钟展开框架

1. **数学**：公式与 `[B,H,T,Dh]` shape；
2. **复杂度**：$T^2D$、$TD^2$ 和显存项；
3. **数值**：mask、softmax、precision；
4. **系统**：KV、kernel、prefill/decode、serving。

## 实战练习

- **Shape drill**：从 `[B,T,D]` 写到 QKV、score、output 的每一步 shape。
- **性能**：用 profiler 对比标准 attention / SDPA（环境支持时），记录峰值显存和时间。
- **系统题**：固定模型，分别增大 batch、context、KV heads，预测哪一项先成为瓶颈。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

Attention 可分为 similarity、normalization、weighted aggregation 三步；mask 在 softmax 前作用于 logits，数值稳定通常使用 fp32 accumulation/融合 kernel。

### 工程与实验抓手

手写 attention 与 `torch.nn.functional.scaled_dot_product_attention` 对拍，覆盖 causal/padding、fp16、极端 logits。

### 失败边界 / 反例

不能把 `QK^T` 当最终结果；softmax 的归一化维度、scale 和 mask 任一错都可能 silent bug。

### 白板专项练习

从 `[B,H,T,Dh]` 写出每一步 shape、广播关系与复杂度。

> **本章 90 分标准：** Transformer 题默认要求公式、shape、复杂度、数值稳定、GPU/serving 影响五层都能展开。

## 面试官评分拆解

| 档位 | 典型表现 |
|---|---|
| 40–50 分 | 只会给定义或背结论，缺公式/机制，追问一层就断。 |
| 60–70 分 | 能解释主机制并写关键公式，但缺边界条件和工程证据。 |
| 80–90 分 | 能定量推导、比较替代方案，主动说明失败场景并给验证方法。 |
| 90+ 分 | 能把数学、实现、系统成本和项目决策串成完整证据链，并能反向设计实验验证假设。 |

### 面试表达建议

建议用 **结论 → 机制 → 定量 → trade-off → 边界 → 验证** 六步法回答。先在 60–90 秒内给主线；只有面试官继续追问时再展开公式、代码或系统细节。这样既显示深度，也避免一上来堆知识点失去重点。

## 项目化证据链：如何证明你真的做过

只讲原理只能证明“学过”，项目面试还要证明“做过、量过、复盘过”。针对本题，建议准备一张实验卡：**问题/假设 → baseline → 改动 → 指标 → 结果 → 失败 slice → 结论**。

### 建议报告的指标

- **核心观测：** attention entropy、tokens/s、peak memory、TTFT/TPOT、KV bytes、kernel/backend。
- **证据原则：** Transformer 优化必须说明是改数学连接、改 IO、改 KV，还是改 scheduler，避免概念混淆。
- **本题特定证据：** 手写 attention 与 `torch.nn.functional.scaled_dot_product_attention` 对拍，覆盖 causal/padding、fp16、极端 logits。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**不能把 `QK^T` 当最终结果；softmax 的归一化维度、scale 和 mask 任一错都可能 silent bug。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先画 `[B,T,D]` 数据流 → 写 attention/FFN 公式 → 算复杂度/显存 → 讲数值与 kernel → 讲 serving。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q041 · 为什么 Attention 要除以 √d_k？](../05-transformer/Q041-attention-scaling.md)
- [Q042 · Q、K、V 从语义和线性代数上分别是什么？](../05-transformer/Q042-qkv.md)
- [Q043 · Self-Attention 的时间和显存复杂度是多少？](../05-transformer/Q043-attention-complexity.md)
- [Q044 · Multi-Head Attention 为什么比单头更有表达力？](../05-transformer/Q044-multi-head-attention.md)
- [Q055 · 请手写 Multi-Head Attention，必须处理 shape、mask 与数值稳定。](../05-transformer/Q055-implement-mha.md)

## 参考资料

- [Vaswani et al., Attention Is All You Need](https://arxiv.org/abs/1706.03762)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
