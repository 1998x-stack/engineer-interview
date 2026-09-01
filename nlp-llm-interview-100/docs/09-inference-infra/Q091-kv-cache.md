---
id: Q091
title: "KV Cache 为什么能显著加速自回归 Decode？"
chapter: "推理、分布式与 AI Infra"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - inference-infra
  - kv-cache
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q091 KV Cache 为什么能显著加速自回归 Decode？

[← Q090](../08-data-evaluation/Q090-offline-online-gap.md) | **第 9 章 · 推理、分布式与 AI Infra** | [Q092 →](Q092-kv-cache-memory.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`inference-infra`, `kv-cache`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q091.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

生成第 t 个 token 时，过去 token 的哪些计算可以复用？

## 2. 面试官到底在考什么

公开高阶面经代表题。

### 评分维度

- 先从 FLOPs、memory、bandwidth、communication 四个资源维度分析。
- 区分 prefill/decode、training/serving。
- 给出可计算的复杂度或显存公式。

## 3. 30-60 秒标准回答

在 causal decoder 中，历史 token 的 K/V 在后续步骤不会改变。缓存每层历史 K/V 后，每次只 计算新 token 的 Q/K/V，并让新 Q 读取缓存 K/V，避免对整个 prefix 重复做投影与 attention 前 处理。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：prefill 仍是对 prompt 的批量计算。
- **PDF 基线要点**：decode 每步 query length≈1，但 key length 随上下文增长。
- **PDF 基线要点**：cache 带来巨大显存/带宽成本，促使 GQA、PagedAttention、KV quantization。
- **扩展理解**：KV cache 保存过去 token 的 K/V，使 decode 每步只计算新 token 的 projection，而不重复计算历史 K/V。
- **扩展理解**：它降低重复计算但显著增加显存，decode 常转为 memory-bandwidth bound。
- **扩展理解**：prefill 与 decode 是两种不同性能形态。

## 6. 专业深挖：原理、边界与工程

### KV Cache 省的是“历史重复计算”
- 自回归生成第 t 步时，历史 token 的 K/V 已经由固定前缀计算完成，未来不会改变；只需为新 token 计算 Q/K/V，再让新 Q 读取历史+当前 K/V。
- 不缓存时每一步都对整个 prefix 重算所有层，产生大量重复投影和 attention 前处理；缓存把 decode 前向缩成 query length≈1。
- 历史 Q 不需要缓存，因为过去位置的输出已经计算完，后续只需要它们作为 K/V 被新 query 访问。
### 边界与工程
- Prefill 仍要一次处理完整 prompt，通常 compute-bound；Decode 则常受 KV Cache HBM 读带宽和小 GEMM 利用率限制。
- 每步 `torch.cat` 整个 cache 会造成反复复制，生产系统使用预分配、paged blocks 或专用 cache manager。
- Beam search、batch reorder、prefix sharing、RoPE position 都要求 cache state 与 sequence 元数据严格一致。

## 7. 实现、复杂度与工程验证

- 把 prefill/decode 分开做 FLOPs、显存、HBM bandwidth 和通信量账本。
- 系统优化需同时报告 TTFT、TPOT、throughput、峰值显存和质量损失。
- 先定位瓶颈是 compute-bound、memory-bound 还是 communication-bound，再选优化。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 说缓存 Q/K/V 全部；通常历史 Q 不需要。
- 用 torch.cat 每步复制整个 cache。

## 9. 追问树

1. prefill 与 decode 的性能瓶颈为何不同？
2. beam search 如何复制/重排 KV cache？

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

- [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q090 离线指标涨了，为什么线上可能变差？](../08-data-evaluation/Q090-offline-online-gap.md)
- [Q092 KV Cache 大小怎么估算？](Q092-kv-cache-memory.md)
- [Q096 DP、TP、PP、EP：四种并行怎么组合？](Q096-distributed-parallelism.md)

## 13. 一句话收束

> **KV Cache 省的是“历史重复计算”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
