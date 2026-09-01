---
id: Q071
title: "REINFORCE 是 On‑policy 还是 Off‑policy？"
chapter: "SFT、PEFT 与对齐"
difficulty: "★★★"
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

# Q071 REINFORCE 是 On‑policy 还是 Off‑policy？

[← Q070](Q070-rlhf.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q072 →](Q072-reinforce-baseline.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`alignment`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q071.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

写出 REINFORCE 梯度估计，并说明为什么经典形式是 on-policy。

## 2. 面试官到底在考什么

RL 基础真假题。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

REINFORCE 用当前策略采样 trajectory，并用 return 乘 log-policy gradient，因此经典形式是 on-policy Monte Carlo policy gradient。

## 4. 白板核心公式

- $\nabla_\theta J=\mathbb E[R\nabla_\theta\log\pi_\theta(a|s)]$

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：无 value function 的原始 REINFORCE 方差很大。
- **PDF 基线要点**：可以加入 baseline 不改变期望梯度。
- **PDF 基线要点**：off-policy 需要 importance sampling 等修正。
- **扩展理解**：原始 REINFORCE 使用当前策略采样轨迹并更新当前策略，是典型 on-policy estimator。
- **扩展理解**：off-policy 复用需要 importance sampling 等修正，否则梯度估计偏。
- **扩展理解**：要能解释 policy gradient theorem 中 log-prob trick。

## 6. 专业深挖：原理、边界与工程

### 为什么经典 REINFORCE 是 On-policy
- Policy Gradient 期望 $E_{\tau\sim\pi_\theta}[R(\tau)\nabla\log\pi_\theta(\tau)]$ 中的轨迹分布就是当前 policy，因此标准 REINFORCE 需要从当前/足够接近的策略采样。
- 若直接用旧策略/offline 数据而不做 importance correction，梯度期望对应的是错误状态–动作分布。
- On-policy 的代价是样本利用率低，每轮 policy 更新后旧 rollout 很快变 stale。
### 边界与工程
- 可以通过 importance sampling 构造 off-policy 修正，但方差可能很高；这已经不是最朴素的 REINFORCE。
- LLM RL 中生成 rollout 本身非常贵，因此 rollout reuse、batching 和 inference-training 协同是核心系统问题。
- “PPO 也是 on-policy”更准确说是近似 on-policy/有限步复用新鲜数据，不能无限复用旧样本。

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

- 把“使用历史 buffer”默认当 REINFORCE。

## 9. 追问树

1. 为什么 log-derivative trick 成立？
2. Monte Carlo 与 TD 的差异？

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

- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)
- [Q072 REINFORCE 为什么加 Baseline 不引入偏差？](Q072-reinforce-baseline.md)
- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md)

## 13. 一句话收束

> **为什么经典 REINFORCE 是 On-policy**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
