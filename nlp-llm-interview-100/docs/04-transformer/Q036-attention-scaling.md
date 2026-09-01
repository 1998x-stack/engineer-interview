---
id: Q036
title: "为什么 Attention 要除以 sqrt(d_k)？"
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

# Q036 为什么 Attention 要除以 sqrt(d_k)？

[← Q035](Q035-self-attention.md) | **第 4 章 · Transformer 核心原理** | [Q037 →](Q037-qkv-projections.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q036.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

如果 Q、K 分量方差约为 1，点积的方差随 d_k 如何变化？

## 2. 面试官到底在考什么

经典“Know-Why”题。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

点积是 d_k 项随机变量之和，方差约随 d_k 增长。logit 过大使 softmax 饱和，梯度集中甚至接近 0。除以 √d_k 将尺度稳定在 O(1)。

## 4. 白板核心公式

- $\mathrm{Var}(q^\top k)\approx d_k$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：这是 variance control，不是为了“让结果小于 1”。
- **PDF 基线要点**：若初始化/归一化方式改变，实际分布会不同，但 scale 仍是稳健设计。
- **PDF 基线要点**：FlashAttention 不改变这个数学定义。
- **扩展理解**：缩放因子来自点积方差随 d_k 增长；除以 sqrt(d_k) 把 logits 的尺度控制在较稳定范围。
- **扩展理解**：如果 logits 过大，softmax 过度尖锐，梯度集中在少数位置。
- **扩展理解**：不要把它解释成“防止 overflow”这么单一。

## 6. 专业深挖：原理、边界与工程

### 为什么是 $1/\sqrt{d_k}$
- 若 q/k 每维零均值、方差约 1，则点积是 $d_k$ 项求和，方差约 $d_k$、标准差约 $\sqrt{d_k}$。
- 不缩放时维度越大 logits 越大，Softmax 越尖锐，容易进入近 one-hot 的饱和区；缩放把不同 head dimension 的 logit 温度拉回近似 O(1)。
- 这与 Xavier/He 初始化的思想一致：控制中间信号方差，使优化尺度不随维度自动漂移。
### 边界与工程
- 缩放应使用每头 $D_h$，不是总 d_model。
- 若采用 QK normalization、cosine attention 或 learnable temperature，scale 的具体形式会变化，但核心仍是控制 logit 范围。
- 一个很好的实验是随机采 q/k，画未缩放与缩放后 dot-product std 随 $d_k$ 的变化。

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

- 说“防止梯度爆炸”但没有 softmax 饱和链路。

## 9. 追问树

1. 为什么不是除 d_k？
2. cosine attention 是否还需要类似温度？

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

- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q037 为什么 Q、K、V 要用不同投影？](Q037-qkv-projections.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **为什么是 $1/\sqrt{d_k}$**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
