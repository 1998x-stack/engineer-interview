---
id: Q094
title: "Continuous Batching 与 PagedAttention 解决什么？"
chapter: "推理、分布式与 AI Infra"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - inference-infra
  - attention
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q094 Continuous Batching 与 PagedAttention 解决什么？

[← Q093](Q093-quantization.md) | **第 9 章 · 推理、分布式与 AI Infra** | [Q095 →](Q095-speculative-decoding.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`inference-infra`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q094.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

静态 batch 对变长生成为什么浪费？Paged KV memory 有什么作用？

## 2. 面试官到底在考什么

大模型服务核心。

### 评分维度

- 先从 FLOPs、memory、bandwidth、communication 四个资源维度分析。
- 区分 prefill/decode、training/serving。
- 给出可计算的复杂度或显存公式。

## 3. 30-60 秒标准回答

Continuous batching 在请求完成后即时补入新请求，提高 GPU occupancy；PagedAttention 将 KV cache 分块管理，避免为每个请求预留连续最大长度空间，降低碎片与动态扩容成本。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：调度还要考虑 prefill/decode 混部和长请求公平性。
- **PDF 基线要点**：page/block 太小 metadata 多，太大内部碎片多。
- **PDF 基线要点**：prefix caching 可复用相同前缀 KV。
- **扩展理解**：Continuous batching 动态插入/移除请求，提高 GPU occupancy；PagedAttention 用分页式 KV 管理降低碎片。
- **扩展理解**：两者共同解决变长请求导致的静态 batch 低利用率和 KV 内存分配问题。
- **扩展理解**：吞吐提升同时要关注 tail latency 与调度公平性。

## 6. 专业深挖：原理、边界与工程

### Continuous Batching 解决 GPU 空洞，PagedAttention 解决 KV 内存碎片
- 静态 Batch 中不同请求生成长度不同，短请求结束后槽位可能空闲；Continuous Batching 可以在 decode step 边界动态加入新请求，提高 GPU 利用率。
- KV Cache 长度动态、请求随时结束/增长，若每条请求预留连续最大空间会产生严重浪费；PagedAttention 用固定 block/page 管理非连续物理 KV。
- Block table 让逻辑 sequence 对应多个物理 KV blocks，也方便 prefix sharing、copy-on-write 等能力。
### 边界与工程
- 更激进 batching 会提高 throughput，但可能恶化单请求 TPOT/queueing latency，需要调 scheduler policy。
- PagedAttention 不是减少数学 KV 数据量，而是让分配与访问更接近虚拟内存式分页管理。
- Production 还要处理 prefill chunking、priority、SLO、multi-tenant fairness，而不仅是“batch 越大越好”。

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

- 把 PagedAttention 说成改变 attention 数学。

## 9. 追问树

1. chunked prefill 是什么？
2. 如何避免长 prompt 阻塞短请求？

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
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q093 Quantization 为什么能提升 LLM 推理吞吐？](Q093-quantization.md)
- [Q095 Speculative Decoding 为什么能“保证分布”又加速？](Q095-speculative-decoding.md)
- [Q091 KV Cache 为什么能显著加速自回归 Decode？](Q091-kv-cache.md)
- [Q096 DP、TP、PP、EP：四种并行怎么组合？](Q096-distributed-parallelism.md)

## 13. 一句话收束

> **Continuous Batching 解决 GPU 空洞，PagedAttention 解决 KV 内存碎片**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
