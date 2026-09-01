---
id: Q047
title: "Transformer 为什么 Attention 后还需要 FFN？"
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

# Q047 Transformer 为什么 Attention 后还需要 FFN？

[← Q046](Q046-preln-vs-postln.md) | **第 4 章 · Transformer 核心原理** | [Q048 →](Q048-activation-functions.md)

> **难度**：★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q047.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

如果 Attention 已经让所有 token 交互，为什么每层还要大 FFN？

## 2. 面试官到底在考什么

区分 token mixing 与 channel mixing。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

Attention 主要在序列维度路由/混合 token 信息；FFN 对每个位置独立进行高容量非线性特征变 换，在 hidden/channel 维度完成表示重组。两者互补。

## 4. 白板核心公式

- $\mathrm{FFN}(x)=W_2\,\phi(W_1x)$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：经典 FFN 是升维 → 激活 → 降维。
- **PDF 基线要点**：现代 LLM 中 FFN 参数量常占 block 很大比例。
- **PDF 基线要点**：MoE 主要替换/扩展的正是 FFN 子层。
- **扩展理解**：Attention 主要做 token mixing，FFN 做每个位置的 channel-wise 非线性变换。
- **扩展理解**：FFN 通常占 Transformer 参数大头之一，因此 MoE 常替换的就是 FFN。
- **扩展理解**：可以从“通信/路由”和“局部计算”两个角色解释二者互补。

## 6. 专业深挖：原理、边界与工程

### Attention 做 Token Mixing，FFN 做 Channel Mixing
- Attention 的主要作用是跨 token 聚合信息；FFN 在每个位置独立对 feature channels 做非线性变换。
- 标准 FFN 先扩到 $d_{ff}$、经过非线性，再压回 d_model，为每个 token 提供高容量非线性计算。
- 现代 LLM 很大比例参数位于 FFN/MoE Experts，说明它不仅是“辅助层”，而是模型容量核心。
### 边界与工程
- FFN 虽然 position-wise，但输入已经经过 Attention，所以它处理的是上下文化 token 表示。
- $d_{ff}=4d$ 只是经典配置；SwiGLU 三矩阵结构通常使用不同中间宽度匹配参数预算。
- MoE 通常替换 FFN，正是因为逐 token 独立的大参数计算很适合条件路由到不同 Experts。

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

- 说 FFN 只是“增加非线性”不够。

## 9. 追问树

1. d_ff 为什么常大于 d_model？
2. SwiGLU 为什么通常需要三组投影？

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

- [Q046 Pre‑LN 与 Post‑LN：为什么深层模型更偏 Pre‑Norm？](Q046-preln-vs-postln.md)
- [Q048 GELU、ReLU 与 SiLU/SwiGLU 怎么比较？](Q048-activation-functions.md)
- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **Attention 做 Token Mixing，FFN 做 Channel Mixing**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
