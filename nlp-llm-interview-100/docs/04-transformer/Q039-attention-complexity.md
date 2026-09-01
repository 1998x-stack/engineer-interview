---
id: Q039
title: "Self‑Attention 的复杂度到底是多少？"
chapter: "Transformer 核心原理"
difficulty: "★★★★"
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

# Q039 Self‑Attention 的复杂度到底是多少？

[← Q038](Q038-multi-head-attention.md) | **第 4 章 · Transformer 核心原理** | [Q040 →](Q040-causal-mask.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q039.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

给定序列长 n、hidden d，Transformer block 的主要计算复杂度有哪些？

## 2. 面试官到底在考什么

要求拆出 projection、attention、FFN 而非只背 O(n²)。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

QKV/输出投影约 O(nd²)，attention score 与加权约 O(n²d)，FFN 约 O(nd d_ff)。长序列时 n² 项 主导；大 d、短序列时矩阵投影/FFN 也可能主导。

## 4. 白板核心公式

- $\mathrm{time}=O(T^2d),\quad \mathrm{attention\ memory}=O(T^2)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：Attention memory 传统实现需要存 n×n score/概率。
- **PDF 基线要点**：FlashAttention 降低 HBM IO 和中间内存，但数学复杂度仍是 quadratic。
- **PDF 基线要点**：KV cache 改变的是自回归 decode 的重复计算结构。
- **扩展理解**：标准 attention 的 score matrix 是 T×T，时间常写 O(T²d)，显存热点来自 O(T²) 中间矩阵。
- **扩展理解**：训练时 QKV projection O(Td²) 也可能占主导，不能脱离 d/T 比例只喊 O(T²)。
- **扩展理解**：FlashAttention 降低的是 IO/中间存储，不改变精确 attention 的理论算术复杂度。

## 6. 专业深挖：原理、边界与工程

### “Attention 是 O(T²)”只是第一层答案
- 完整 Transformer 每层还包含 QKV/O projection 的 $O(Td^2)$ 与 FFN 的 $O(Td·d_{ff})$；Attention score/AV 才是 $O(T^2d)$。
- 当 T 超大时平方项主导；当 d 很大但上下文中短时，大 GEMM/FFN 反而可能占主要 FLOPs。
- Naive attention 的中间 score/prob matrix 还带来 $O(HT^2)$ activation/HBM I/O，FlashAttention 主要优化的正是这一部分。
### 边界与工程
- Decode 时 query length≈1，单步 attention 对历史长度约线性 O(Td)，但每一步仍需读越来越长的 KV cache。
- KV Cache 避免历史 token 的 QKV/层前向重算，但没有把“读取历史”变成 O(1)。
- 系统题应同时报告 FLOPs、峰值显存、HBM bandwidth 和 prefill/decode 两阶段 profile。

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

- 只写 O(n²) 不说明 d。
- 把 FlashAttention 说成线性 attention。

## 9. 追问树

1. 什么时候 FFN FLOPs 比 attention 更大？
2. 长上下文有哪些稀疏/线性近似路线？

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

- [Q038 Multi‑Head Attention 为什么不是一个大 Head？](Q038-multi-head-attention.md)
- [Q040 Causal Mask 是怎么工作的？](Q040-causal-mask.md)
- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **“Attention 是 O(T²)”只是第一层答案**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
