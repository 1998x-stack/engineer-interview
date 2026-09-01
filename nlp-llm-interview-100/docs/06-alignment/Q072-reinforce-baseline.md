---
id: Q072
title: "REINFORCE 为什么加 Baseline 不引入偏差？"
chapter: "SFT、PEFT 与对齐"
difficulty: "★★★★"
frequency: "★★★★"
tags:
  - alignment
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q072 REINFORCE 为什么加 Baseline 不引入偏差？

[← Q071](Q071-reinforce-on-policy.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q073 →](Q073-dpo.md)

> **难度**：★★★★  ·  **频率**：★★★★  ·  **标签**：`alignment`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q072.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

为什么可以把 R 换成 R-b(s)？baseline 有什么约束？

## 2. 面试官到底在考什么

考察期望推导。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

若 baseline 不依赖当前 action，则 E[b(s)∇logπ(a|s)]=0，因此不改变梯度期望，却可降低 return 的方差。

## 4. 白板核心公式

- $\mathbb E[(R-b(s))\nabla\log\pi(a|s)]$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：最佳 baseline 与条件期望/价值函数相关。
- **PDF 基线要点**：Advantage A=Q-V 可视为中心化后的相对好坏。
- **PDF 基线要点**：baseline 如果偷偷依赖 action，可能引入偏差。
- **扩展理解**：baseline 只要不依赖当前 action，其期望项为零，因此不改变梯度期望却能降方差。
- **扩展理解**：常见 baseline 是 state-value function 或 group mean reward。
- **扩展理解**：方差降低是 RL 训练可行性的核心，而不只是“让数值更小”。

## 6. 专业深挖：原理、边界与工程

### Baseline 为什么能降方差而不改期望
- REINFORCE 将回报 R 换成 $R-b(s)$；只要 baseline 不依赖当前 action，就有 $E[b(s)\nabla\log\pi(a|s)]=b(s)\nabla\sum_a\pi(a|s)=0$。
- 因而梯度期望不变，但如果 baseline 近似 $E[R|s]$，就能把大部分公共回报尺度移除，显著降低 variance。
- Advantage $A(s,a)=Q(s,a)-V(s)$ 正是这种“相对当前状态平均水平”的信号。
### 边界与工程
- Baseline 估计很差不会引入上述意义的偏差，但可能几乎不降方差；若错误地依赖 action，则需要重新分析。
- Value model 本身也要训练，会带来额外显存、计算和 bootstrap error。
- LLM group-relative 方法可用同一 prompt 多个 sample 的组内平均 reward 作为相对基线，减少独立 critic 需求。

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

- 只说“减均值所以方差小”。

## 9. 追问树

1. Actor-Critic 如何学习 baseline？
2. GAE 在做什么？

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

- [Q071 REINFORCE 是 On‑policy 还是 Off‑policy？](Q071-reinforce-on-policy.md)
- [Q073 DPO 为什么不需要显式 Reward Model？](Q073-dpo.md)
- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md)

## 13. 一句话收束

> **Baseline 为什么能降方差而不改期望**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
