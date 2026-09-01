---
id: Q035
title: "Self‑Attention 的完整计算流程"
chapter: "Transformer 核心原理"
difficulty: "★★★"
frequency: "★★★★★"
tags:
  - transformer
  - attention
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q035 Self‑Attention 的完整计算流程

[← Q034](../03-representation-sequence/Q034-seq2seq-attention.md) | **第 4 章 · Transformer 核心原理** | [Q036 →](Q036-attention-scaling.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q035.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

从 X 到 Q/K/V、score、softmax、output，完整写出 Self-Attention。

## 2. 面试官到底在考什么

Transformer 第一必答题。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

线性投影得到 Q=XW_Q、 K=XW_K、 V=XW_V；计算缩放点积 QK^T/√d_k， 加入 mask 后 softmax 得到注意力权重，再乘 V 聚合内容。

## 4. 白板核心公式

- $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：Q/K 决定匹配，V 提供被读取内容。
- **PDF 基线要点**：mask 应在 softmax 前加到 logits。
- **PDF 基线要点**：实现时最常见错误是 shape、transpose、softmax dimension。
- **扩展理解**：完整 Self-Attention 要从 shape 出发：X->[Q,K,V]->score->[mask]->softmax->weighted sum->projection。
- **扩展理解**：工程实现中 mask、dtype、softmax 维度与数值稳定性经常比公式本身更容易出错。
- **扩展理解**：现代实现通常使用 fused scaled_dot_product_attention/FlashAttention 降低 IO。

## 6. 专业深挖：原理、边界与工程

### Self-Attention 必须能写清 Shape
- 输入 `[B,T,d]` 经 Q/K/V projection 后通常 reshape 为 `[B,H,T,D_h]`；score 为 `[B,H,T_q,T_k]`，Softmax 必须沿 key 维。
- 先在 logits 上加入 causal/padding mask，再 Softmax，最后权重乘 V。Softmax 后再简单乘 mask 会破坏归一化。
- 多头输出 transpose+concat 回 `[B,T,H·D_h]`，再经 $W_O$ 跨头混合；忘记 $W_O$ 是常见白板遗漏。
### 边界与工程
- `transpose` 后张量可能 non-contiguous，若用 `view` 需注意 `.contiguous()`；这类实现细节在现场代码题很常见。
- FlashAttention 优化的是 IO/中间显存，不改变精确 Attention 数学定义，也不是把 O(T²) 变 O(T)。
- 最可靠的 Debug 方法是 naive reference 与 fused kernel 做输出/梯度对拍，并检查 mask 区域权重严格为 0。

## 7. 实现、复杂度与工程验证

- 明确 `[B,T,H,D]` 等 tensor shape、softmax axis、mask broadcast 与 dtype。
- 区分训练全序列、prefill 与 decode；后两者的资源瓶颈不同。
- 用 reference implementation 对拍 fused/optimized kernel，确保优化不改变语义。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 忘记 scale。
- 把 softmax 做在 query 维。

## 9. 追问树

1. cross-attention 时 Q/K/V 来自哪里？
2. 为什么可以把 attention 看成 content-addressable memory？

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

### 回答追问时的升级原则

1. 先给结论，再写一个关键公式 / shape / 数据流。
2. 主动说清 trade-off：质量、计算、显存、延迟、数据或偏差至少一个。
3. 给出一个“不适用”的条件，证明不是机械背诵。
4. 若追问工程实现，优先说明验证方法和可观测指标。

## 10. 面试现场自检

- [ ] 30-60 秒能给出结论，不绕弯。
- [ ] 能写出关键公式、shape 或状态转移。
- [ ] 至少能解释一个 Why 和一个 trade-off。
- [ ] 能举出一个失败模式或反例。
- [ ] 能回答两层追问。
- [ ] 能把答案连接到真实训练/检索/服务系统。

## 11. 参考资料

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [RoFormer / RoPE](https://arxiv.org/abs/2104.09864)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q034 Seq2Seq 为什么需要 Attention？](../03-representation-sequence/Q034-seq2seq-attention.md)
- [Q036 为什么 Attention 要除以 sqrt(d_k)？](Q036-attention-scaling.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **Self-Attention 必须能写清 Shape**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
