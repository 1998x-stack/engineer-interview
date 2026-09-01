---
id: Q065
title: "Pretraining 与 SFT 的本质区别"
chapter: "SFT、PEFT 与对齐"
difficulty: "★★"
frequency: "★★★★★"
tags:
  - alignment
  - sft
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q065 Pretraining 与 SFT 的本质区别

[← Q064](../05-pretraining/Q064-moe.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q066 →](Q066-lora.md)

> **难度**：★★  ·  **频率**：★★★★★  ·  **标签**：`alignment`, `sft`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q065.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

Pretraining 和 SFT 的数据形态、loss mask、目标分别是什么？

## 2. 面试官到底在考什么

区分世界建模与行为监督。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

预训练主要对自然文本做 next-token modeling，学习语言/知识分布；SFT 用 instruction- response 等行为数据教模型如何按期望方式响应，常只对 assistant tokens 计算 loss。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：SFT 数据量通常远小于预训练，但监督密度更高。
- **PDF 基线要点**：把 QA 全文当普通 LM 训练更接近 mid-training；只训 answer 更接近 SFT。
- **PDF 基线要点**：SFT 会塑造风格，也可能造成能力遗忘，需要数据混合与学习率控制。
- **扩展理解**：Pretraining 学通用 token distribution；SFT 用高质量 instruction-response 数据塑造行为接口。
- **扩展理解**：两者都可用 next-token CE，但数据组织、loss mask 与能力目标不同。
- **扩展理解**：SFT 不能凭空创造模型完全没有的底层知识，更多是在重排/显化能力。

## 6. 专业深挖：原理、边界与工程

### Pretraining 与 SFT 的差别首先是数据语义
- Pretraining 通常把任意自然文本当 next-token 序列，目标是学习广泛语言/世界分布；SFT 数据显式包含 instruction/context 与 desired assistant behavior。
- SFT 经常只对 assistant response token 计算 loss，用户 prompt 不作为要模仿的输出；这使训练目标从“建模文本”转向“在条件下产生指定行为”。
- Pretraining 决定大部分知识和基础能力，SFT 更像行为/接口塑形；少量 SFT 很难可靠注入海量新知识。
### 边界与工程
- Continued Pretraining/Mid-training 与 SFT 边界有时模糊：同一 QA 数据若整段做 LM loss 更像能力训练，只对 answer 做 response loss 更像 SFT。
- SFT 数据质量问题通常直接转成行为错误，因此重复模板、拒答风格、教师偏差会被强监督复制。
- 训练时必须明确 chat template、loss mask、packing 与 EOS 规则，否则同一数据可产生完全不同梯度。

## 7. 实现、复杂度与工程验证

- 先明确 demonstration、preference、reward、rollout 分别来自哪里。
- 所有 reward/judge 都是代理目标，要讨论偏差、KL、reward hacking 和覆盖。
- 比较方法时同时算训练稳定性、采样成本、显存和在线数据需求。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 把 SFT 说成“继续预训练”而不区分监督掩码。

## 9. 追问树

1. 为什么 SFT 后模型更会遵循指令？
2. SFT 数据重复会有什么风险？

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

- [LoRA](https://arxiv.org/abs/2106.09685)
- [QLoRA](https://arxiv.org/abs/2305.14314)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q064 MoE：为什么参数变大但每 token 计算不同比例增长？](../05-pretraining/Q064-moe.md)
- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md)

## 13. 一句话收束

> **Pretraining 与 SFT 的差别首先是数据语义**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
