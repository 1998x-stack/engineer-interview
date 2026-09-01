---
id: Q043
title: "RoPE：如何把相对位置写进 QK 点积？"
chapter: "Transformer 核心原理"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - transformer
  - rope
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q043 RoPE：如何把相对位置写进 QK 点积？

[← Q042](Q042-sinusoidal-position.md) | **第 4 章 · Transformer 核心原理** | [Q044 →](Q044-rope-qk-not-v.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `rope`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q043.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

请用二维旋转说明 RoPE。为什么 q_m^T k_n 最终只与相对位置 m-n 有关？

## 2. 面试官到底在考什么

现代 LLM 核心必考。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

RoPE 将 Q/K 的二维通道成对旋转，位置 m 对应旋转 R_m。由于 R_m^T R_n=R_{n-m}，点积自 然只依赖相对旋转差，从而把相对位置信息编码进 attention score。

## 4. 白板核心公式

- $q_m^\top k_n=(R_m q)^\top(R_n k)=q^\top R_{n-m}k$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：不是给 embedding 直接加位置向量。
- **PDF 基线要点**：不同通道使用不同旋转频率。
- **PDF 基线要点**：RoPE 兼具绝对相位和相对点积性质，是现代 decoder LLM 常用方案。
- **扩展理解**：RoPE 对 Q/K 成对维度做位置相关旋转，使内积可写成相对位移函数。
- **扩展理解**：应能从 R_m^T R_n = R_{n-m} 推出相对位置性质。
- **扩展理解**：实际实现要关注 rotary_dim、频率 base、布局与 KV cache 中 position id。

## 6. 专业深挖：原理、边界与工程

### RoPE 的核心代数必须会推
- 把每两维视为二维向量，位置 m 对 Q/K 乘旋转矩阵 $R_m$。则 $(R_mq)^T(R_nk)=q^TR_m^TR_nk=q^TR_{n-m}k$。
- 因此 Attention Score 中位置只通过相对位移 n−m 进入；不同 channel pair 采用不同频率，使模型同时感知多尺度距离。
- 复数视角等价：二维 pair 乘 $e^{im\theta}$，内积中的相位自然只剩 $e^{i(n-m)\theta}$。
### 边界与工程
- 形式上 RoPE 可计算任意位置，但训练外相位组合未见过，所以仍会出现 extrapolation degradation。
- KV Cache 通常存 RoPE 后的 K；decode 新 token 必须使用真实绝对 position 旋转后再追加。
- 不同模型的 base、rotary_dim、interleaved/half-split 布局不同，checkpoint/serving 实现必须完全一致。

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

- 只会画旋转矩阵，不会解释 R_m^T R_n。
- 把 RoPE 当作可学习参数。

## 9. 追问树

1. RoPE 的 base/频率如何影响长上下文？
2. 为什么只旋转 Q/K？

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

- [RoFormer / RoPE](https://arxiv.org/abs/2104.09864)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q042 Sinusoidal Positional Encoding 的设计直觉](Q042-sinusoidal-position.md)
- [Q044 为什么 RoPE 通常只作用于 Q/K，不作用于 V？](Q044-rope-qk-not-v.md)
- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md)

## 13. 一句话收束

> **RoPE 的核心代数必须会推**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
