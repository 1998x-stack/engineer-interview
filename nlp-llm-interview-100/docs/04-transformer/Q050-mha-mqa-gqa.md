---
id: Q050
title: "MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？"
chapter: "Transformer 核心原理"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - transformer
  - kv-cache
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q050 MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？

[← Q049](Q049-swiglu.md) | **第 4 章 · Transformer 核心原理** | [Q051 →](../05-pretraining/Q051-bert-mlm-nsp.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`transformer`, `kv-cache`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q050.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

MHA、MQA、GQA 的 Q head 与 KV head 数量关系是什么？

## 2. 面试官到底在考什么

连接模型结构与推理内存。

### 评分维度

- 先写 shape 与核心公式，避免只背架构图。
- 从优化/数值/复杂度解释 Why。
- 必须能回答训练与推理实现差异。

## 3. 30-60 秒标准回答

MHA 每个 Q head 对应独立 K/V head；MQA 所有 Q heads 共用一组 K/V；GQA 多个 Q heads 共享一组 KV，在质量与 cache/带宽之间折中。KV cache 大小与 KV head 数近似线性相关。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：Decode 阶段常 memory-bandwidth bound，因此减少 K/V 很有价值。
- **PDF 基线要点**：GQA 不直接减少 Q/O 投影或 FFN 参数。
- **PDF 基线要点**：训练质量损失与共享粒度有关。
- **扩展理解**：MHA 每个 Q head 独立 K/V；MQA 全共享；GQA 在组内共享，是质量与 KV memory/bandwidth 的折中。
- **扩展理解**：KV cache 大小与 KV head 数线性相关，因此 GQA 对长上下文 decode 特别关键。
- **扩展理解**：需要同时考虑模型转换兼容性、训练质量与硬件 kernel。

## 6. 专业深挖：原理、边界与工程

### GQA 是典型“模型结构为推理系统服务”
- MHA 有 $H_q=H_{kv}$；MQA 所有 Q Heads 共用一组 KV；GQA 介于二者，多组 Q Heads 共享一个 KV Head。
- KV Cache 大小近似与 $H_{kv}$ 线性相关。32 Q / 8 KV 的配置意味着每 4 个 Q Heads 共用一个 KV Head，Cache K/V 约降到 MHA 的 1/4。
- Decode 常受 KV Cache 容量与 HBM 读带宽约束，因此减少 KV Heads 同时提升可容纳并发和每步带宽效率。
### 边界与工程
- GQA 不会等比例减少 Q/O projection 或 FFN 参数；收益主要集中在 K/V 参数、Cache 与相关 Attention 读带宽。
- MQA 共享最激进，可能牺牲 K/V 表示多样性；GQA 是质量–效率折中。
- Tensor Parallel 划分时 Q Head 与 KV Group 的设备映射必须可整除或合理 replication，这是生产实现常见约束。

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

- 说 GQA 是“减少 attention heads”不准确。

## 9. 追问树

1. 给定 32 Q heads、8 KV heads，group size 是多少？
2. MQA 为什么可能损失质量？

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

- [GQA](https://arxiv.org/abs/2305.13245)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q049 SwiGLU 为什么成了现代 LLM 常客？](Q049-swiglu.md)
- [Q051 BERT 原始预训练任务：MLM 与 NSP](../05-pretraining/Q051-bert-mlm-nsp.md)
- [Q035 Self‑Attention 的完整计算流程](Q035-self-attention.md)
- [Q043 RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md)

## 13. 一句话收束

> **GQA 是典型“模型结构为推理系统服务”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
