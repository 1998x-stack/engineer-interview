---
id: Q095
title: "Speculative Decoding 为什么能“保证分布”又加速？"
chapter: "推理、分布式与 AI Infra"
difficulty: "★★★★★"
frequency: "★★★★"
tags:
  - inference-infra
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q095 Speculative Decoding 为什么能“保证分布”又加速？

[← Q094](Q094-continuous-batching-pagedattention.md) | **第 9 章 · 推理、分布式与 AI Infra** | [Q096 →](Q096-distributed-parallelism.md)

> **难度**：★★★★★  ·  **频率**：★★★★  ·  **标签**：`inference-infra`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q095.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

draft model 一次提议多个 token，target model 如何验证？什么时候反而不快？

## 2. 面试官到底在考什么

考察 sampling correctness 与系统收益。

### 评分维度

- 先从 FLOPs、memory、bandwidth、communication 四个资源维度分析。
- 区分 prefill/decode、training/serving。
- 给出可计算的复杂度或显存公式。

## 3. 30-60 秒标准回答

小模型先生成候选序列，大模型用一次并行前向验证多个位置，通过接受/拒绝规则保持目标分布。 若接受率高，一次 target forward 确认多个 token；若 draft 慢或接受率低，收益会消失。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：收益取决于 draft-target 匹配、batch、硬件与输出长度。
- **PDF 基线要点**：可用同模型小头/Medusa 类多 token head 作为 draft。
- **PDF 基线要点**：验证阶段是并行的，但最终依然尊重自回归分布。
- **扩展理解**：Speculative decoding 用 draft model 提议多个 token，再由 target model 批量验证；正确算法可保持 target distribution。
- **扩展理解**：加速取决于 acceptance rate、draft 成本与验证长度。
- **扩展理解**：不是所有模型/温度/任务都能获益，工程上要测端到端 wall-clock。

## 6. 专业深挖：原理、边界与工程

### Speculative Decoding 用便宜模型提案、昂贵模型批量验证
- Draft Model 先快速提出多个 token，Target Model 一次前向对这段候选计算概率，并按接受–拒绝规则决定可以一次提交多少 token。
- 正确算法会对拒绝位置从修正分布重采样，因此最终生成分布与 Target Model 保持一致，而不是简单“草稿错了就回滚”的启发式。
- 加速来自提高每次 Target 前向确认的 token 数；只有 Draft 足够快且 acceptance rate 高时才有实际收益。
### 边界与工程
- Draft 太弱 → 接受率低；Draft 太大 → 自己成本太高。最佳点是速度与分布接近度的折中。
- Batch、大上下文、采样参数会改变收益；Target decode 已被其他 kernel/parallel 优化后，Speculative 的边际收益也会变化。
- 需要测 effective accepted tokens / target forward、end-to-end TPOT，而不是只看 Draft accuracy。

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

- 说“先小模型生成，直接让大模型纠错”太粗。

## 9. 追问树

1. 接受率如何估计？
2. 为什么 temperature 越高可能影响 acceptance？

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

- [Speculative Decoding](https://arxiv.org/abs/2211.17192)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q094 Continuous Batching 与 PagedAttention 解决什么？](Q094-continuous-batching-pagedattention.md)
- [Q096 DP、TP、PP、EP：四种并行怎么组合？](Q096-distributed-parallelism.md)
- [Q091 KV Cache 为什么能显著加速自回归 Decode？](Q091-kv-cache.md)

## 13. 一句话收束

> **Speculative Decoding 用便宜模型提案、昂贵模型批量验证**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
