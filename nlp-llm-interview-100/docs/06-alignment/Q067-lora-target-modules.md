---
id: Q067
title: "LoRA 应该加 Q/V 还是加所有 Linear？"
chapter: "SFT、PEFT 与对齐"
difficulty: "★★★"
frequency: "★★★★"
tags:
  - alignment
  - lora
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q067 LoRA 应该加 Q/V 还是加所有 Linear？

[← Q066](Q066-lora.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q068 →](Q068-qlora.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`alignment`, `lora`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q067.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

早期常只对 Q/V 加 LoRA，为什么今天也常覆盖 K/O/FFN？

## 2. 面试官到底在考什么

考察适配容量与成本选择。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

LoRA 本质适用于任何线性层。只加少数 attention 投影参数少、成本低；覆盖 FFN 与更多投影提 供更大适配容量。应由任务、预算和 ablation 决定。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：FFN 往往占大量参数，因此对领域迁移可能重要。
- **PDF 基线要点**：不同模块对 rank 敏感性不同。
- **PDF 基线要点**：QLoRA 中基座量化不改变 LoRA 的目标模块逻辑。
- **扩展理解**：只挂 Q/V 是早期常见配置；对更复杂适配，QKV/O 与 FFN 全线性层常能提高容量。
- **扩展理解**：目标模块越多，参数/显存/过拟合风险越高。
- **扩展理解**：应按任务规模与预算做 ablation，而不是把“Q/V 最优”当定律。

## 6. 专业深挖：原理、边界与工程

### LoRA 放哪里取决于“你想给哪些子模块自由度”
- 早期实践常只加 Q/V，成本低且能直接改变 Attention 路由与内容；现代 LLM 常对 Q/K/V/O 甚至 FFN gate/up/down 全部 Linear 加 LoRA，以获得更高适配容量。
- 若只改 Attention，FFN 中大量参数无法任务化；对复杂领域/风格迁移，全 Linear 往往更接近 Full Fine-tune 的能力。
- 代价是 trainable params、optimizer memory、通信和多 adapter Serving 开销增加。
### 边界与工程
- 选择 target modules 应做层/模块消融，而不是机械复制某个开源脚本。
- 不同模型模块命名不同，`q_proj/v_proj` 等字符串配置错误可能导致实际一个 LoRA 都没插入。
- 多 LoRA Serving 时 adapter weight 的 cache/切换成本和 batch 内多 adapter 混跑也需要系统设计。

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

- 把“Q/V 最优”当固定结论。

## 9. 追问树

1. 如何用 rank allocation 做自适应 LoRA？
2. adapter merge 后还能切换任务吗？

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

- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q068 QLoRA 为什么能在更小显存上微调大模型？](Q068-qlora.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md)

## 13. 一句话收束

> **LoRA 放哪里取决于“你想给哪些子模块自由度”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
