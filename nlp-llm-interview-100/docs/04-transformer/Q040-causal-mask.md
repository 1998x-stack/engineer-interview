---
id: Q040
title: "Causal Mask 是怎么工作的？"
chapter: "Transformer 核心原理"
difficulty: "★★"
frequency: "★★★★★"
tags:
  - transformer
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q040 Causal Mask 是怎么工作的？

[← Q039](Q039-attention-complexity.md) | **第 4 章 · Transformer 核心原理** | [Q041 →](Q041-position-information.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q040.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

GPT 的 causal mask 应屏蔽哪一半矩阵？为什么是在 softmax 前加 -∞？

## 2. 面试官到底在考什么

实现必会，方向错一行就泄漏未来。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

第 i 个 query 只能访问位置 ≤i 的 key，未来位置 logit 加 -∞，softmax 后概率变为 0。实际实现 需同时处理 padding、cache offset 与 batch shape。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：常见矩阵约定 row=query、col=key，因此是上三角 future 区域被屏蔽。
- **PDF 基线要点**：prefill 时是完整三角 mask；单 token decode 配合 cache 时通常无需显式大三角矩阵。
- **PDF 基线要点**：mask dtype 与极小值选择需兼顾 FP16/BF16。
- **扩展理解**：Causal mask 保证位置 t 只能看 <=t 的 key，从结构上实现自回归因果因子分解。
- **扩展理解**：mask 应在 softmax 前施加，注意 bool/additive mask 的语义差异。
- **扩展理解**：KV cache decode 时 mask 形状会与 prefill 不同。

## 6. 专业深挖：原理、边界与工程

### Causal Mask 让训练并行但不泄漏未来
- Decoder LM 的第 i 个 token 只能依赖 $x_{<i}$；Causal Mask 在矩阵中把未来 key logits 置为 $-\infty$，Softmax 后权重严格为 0。
- 因此训练时可以一次矩阵化算全序列，而逻辑上每个位置仍满足自回归条件分布。
- Padding Mask 是“这个 token 是否有效”，Causal Mask 是“这个位置是否已经发生”，二者语义不同但常合并广播。
### 边界与工程
- 上三角/下三角取决于 row=query、col=key 约定，死记图形非常容易写反。
- Packed sequence 还需要 block-diagonal/segment mask，否则后一个样本会看到前一个样本内容。
- cached decode 与 full forward logits 对拍是验证 mask + position offset 正确性的黄金测试。

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

- 方向反了导致训练 label leakage。
- mask broadcast shape 错。

## 9. 追问树

1. padding mask 与 causal mask 如何合并？
2. KV cache 时 position offset 如何影响 mask？

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

- [Q039 Self‑Attention 的复杂度到底是多少？](Q039-attention-complexity.md)
- [Q041 为什么 Transformer 必须注入位置信息？](Q041-position-information.md)
- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **Causal Mask 让训练并行但不泄漏未来**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
