---
id: Q090
title: "离线指标涨了，为什么线上可能变差？"
chapter: "数据工程与 Evaluation"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - data-evaluation
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q090 离线指标涨了，为什么线上可能变差？

[← Q089](Q089-llm-as-judge.md) | **第 8 章 · 数据工程与 Evaluation** | [Q091 →](../09-inference-infra/Q091-kv-cache.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`data-evaluation`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q090.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

一个 reranker 离线 NDCG 上升，但线上 CTR/成功率下降，如何分析？

## 2. 面试官到底在考什么

真正工业算法岗必问。

### 评分维度

- 强调 provenance、可审计和实验消融。
- 把质量信号与最终训练 utility 分开。
- 讨论误删、污染、Judge 偏差和线上分布。

## 3. 30-60 秒标准回答

可能来自数据分布错配、 metric proxy 不对应业务、 延迟上升、 召回链路变化、 长尾 regression、 用户 行为反馈环等。应走 offline→shadow→A/B→monitoring，并建立可归因的 failure taxonomy。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：线上目标常是多目标：质量、延迟、成本、安全、留存。
- **PDF 基线要点**：离线测试集可能被迭代过拟合。
- **PDF 基线要点**：A/B 还需样本量、显著性与 guardrail 指标。
- **扩展理解**：离线集与线上流量存在 selection/distribution gap；指标代理也可能与业务目标错位。
- **扩展理解**：线上还受 latency、fallback、缓存、用户反馈循环和系统故障影响。
- **扩展理解**：成熟流程需要 offline -> shadow -> A/B -> monitoring 的闭环。

## 6. 专业深挖：原理、边界与工程

### Offline→Online Gap 的来源远不止“数据分布不同”
- 离线集可能随机切分导致时间泄漏、重复用户/文档泄漏、候选分布与线上不同；线上还存在反馈循环、冷启动和策略改变后的 distribution shift。
- 一个模型离线更准但更慢，可能引起超时、fallback、用户等待和上下游缓存 miss，从而让业务指标反而下降。
- Proxy Metric 也可能和真实目标错位：NDCG 上升不一定增加满意度，Judge 分数上升不一定减少错误答案。
### 边界与工程
- 成熟上线流程包括 time-based/off-policy eval → shadow/canary → A/B → continuous monitoring，并设置 guardrail metrics。
- 线上需要监控分布、latency、coverage、cost、calibration、slice regression，而不只一个 North Star。
- 出现 gap 时按“数据→候选→模型→系统→用户行为”分层归因，避免第一反应就是继续调模型。

## 7. 实现、复杂度与工程验证

- 为每次过滤保留 reason code、score、阈值、版本和 provenance。
- 质量信号不是 ground truth，必须估计误删/漏删和长尾分布损失。
- 最终用 proxy training/downstream utility 验证数据决策。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 认为线上下降说明离线指标“没用”。

## 9. 追问树

1. 如何设置 guardrail metric？
2. 怎样做 counterfactual/off-policy evaluation？

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

- [DataTrove](https://github.com/huggingface/datatrove)
- [Dolma](https://arxiv.org/abs/2402.00159)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q089 LLM‑as‑a‑Judge 有哪些系统性偏差？](Q089-llm-as-judge.md)
- [Q091 KV Cache 为什么能显著加速自回归 Decode？](../09-inference-infra/Q091-kv-cache.md)
- [Q085 预训练数据清洗 Pipeline 应如何设计？](Q085-pretraining-data-pipeline.md)
- [Q088 合成数据质量：Validity、Faithfulness、Diversity、Utility](Q088-synthetic-data-quality.md)

## 13. 一句话收束

> **Offline→Online Gap 的来源远不止“数据分布不同”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
