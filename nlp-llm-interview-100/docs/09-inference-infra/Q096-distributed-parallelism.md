---
id: Q096
title: "DP、TP、PP、EP：四种并行怎么组合？"
chapter: "推理、分布式与 AI Infra"
difficulty: "★★★★★"
frequency: "★★★★★"
tags:
  - inference-infra
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q096 DP、TP、PP、EP：四种并行怎么组合？

[← Q095](Q095-speculative-decoding.md) | **第 9 章 · 推理、分布式与 AI Infra** | [Q097 →](../10-coding-debug/Q097-stable-softmax.md)

> **难度**：★★★★★  ·  **频率**：★★★★★  ·  **标签**：`inference-infra`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q096.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

解释 Data/Tensor/Pipeline/Expert Parallel，各自主要通信是什么？

## 2. 面试官到底在考什么

大模型核心工程题。

### 评分维度

- 先从 FLOPs、memory、bandwidth、communication 四个资源维度分析。
- 区分 prefill/decode、training/serving。
- 给出可计算的复杂度或显存公式。

## 3. 30-60 秒标准回答

DP 复制模型分数据，梯度需 all-reduce/reduce-scatter；TP 切单层矩阵，层内频繁通信；PP 按 层切 stage，产生 pipeline bubbles；EP 把 MoE experts 分设备，token routing 需要 all-to-all。 大规模训练常多维组合。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：ZeRO/FSDP 属于数据并行下参数/梯度/optimizer state 分片。
- **PDF 基线要点**：TP 通信频率高，偏好高速互联。
- **PDF 基线要点**：PP microbatch 数影响 bubble 比例。
- **扩展理解**：DP 复制模型分数据；TP 拆单层张量算子；PP 拆层；EP 拆 MoE experts。
- **扩展理解**：并行维度本质是在显存、计算、通信、气泡和容错之间切分。
- **扩展理解**：大规模训练通常组合多维并行，并配 sequence/context parallel、ZeRO/FSDP。

## 6. 专业深挖：原理、边界与工程

### 四种并行是在不同维度切同一个训练图
- Data Parallel：每组设备有完整模型，处理不同 data batch，梯度需要 all-reduce/reduce-scatter。
- Tensor Parallel：把单层矩阵按行/列切到设备，单层内频繁通信；Pipeline Parallel：把不同 layers 分 stage，存在 micro-batch pipeline bubble。
- Expert Parallel：MoE 的 experts 分到不同设备，router 后 token 通过 all-to-all 发往对应 experts。
### 边界与工程
- 真实大模型常组合 DP×TP×PP×EP；并行度不是越大越好，通信、bubble、显存和拓扑决定最佳配置。
- TP 适合 NVLink/NVSwitch 等高带宽域，跨节点低带宽通信成本会迅速放大；PP 更容易跨节点但受 bubble 影响。
- 面试中最好能说明 all-reduce、all-gather、reduce-scatter、all-to-all 分别在哪些并行模式出现。

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

- 把 ZeRO 当第五种完全独立并行。

## 9. 追问树

1. 为什么 TP 通常限制在单节点高速互联？
2. all-reduce 与 reduce-scatter+all-gather 的关系？

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

- [Megatron-LM](https://arxiv.org/abs/1909.08053)
- [DeepSpeed ZeRO](https://arxiv.org/abs/1910.02054)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q095 Speculative Decoding 为什么能“保证分布”又加速？](Q095-speculative-decoding.md)
- [Q097 手写 Numerical Stable Softmax](../10-coding-debug/Q097-stable-softmax.md)
- [Q091 KV Cache 为什么能显著加速自回归 Decode？](Q091-kv-cache.md)

## 13. 一句话收束

> **四种并行是在不同维度切同一个训练图**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
