---
id: Q074
title: "PPO、DPO、GRPO：什么时候选哪一个？"
chapter: "SFT、PEFT 与对齐"
difficulty: "★★★★★"
frequency: "★★★★★"
tags:
  - alignment
  - dpo
  - ppo
  - grpo
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q074 PPO、DPO、GRPO：什么时候选哪一个？

[← Q073](Q073-dpo.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q075 →](../07-retrieval-rag/Q075-sparse-vs-dense-retrieval.md)

> **难度**：★★★★★  ·  **频率**：★★★★★  ·  **标签**：`alignment`, `dpo`, `ppo`, `grpo`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q074.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

比较 PPO、DPO、GRPO 类方法的数据需求、在线采样、value model 与适用场景。

## 2. 面试官到底在考什么

考察方法选择而非名词堆砌。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

PPO 是在线 policy optimization，显式 reward/value，灵活但复杂；DPO 用离线偏好直接优化， 简单稳定；GRPO 类方法对同一问题采一组候选，基于组内相对奖励构造 advantage，可省 value model，适合有可验证 reward 的 reasoning。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：可验证任务能用 unit test/答案 checker 降低 Judge 偏差。
- **PDF 基线要点**：在线 RL 能探索新策略，但成本和 reward hacking 风险更高。
- **PDF 基线要点**：不存在“新方法一定替代旧方法”。
- **扩展理解**：PPO 适合在线 reward optimization；DPO 适合离线 preference；GRPO 类方法适合有可验证 reward、可多样本采样的 reasoning。
- **扩展理解**：选择标准包括 reward 可得性、采样成本、稳定性、是否需要 value model。
- **扩展理解**：不要把 GRPO 解释为“永远优于 PPO”。

## 6. 专业深挖：原理、边界与工程

### PPO、DPO、GRPO 先按“数据从哪里来”分类
- PPO：在线/近在线 rollout + Reward + Value/Critic + clipped policy update，灵活但系统复杂、样本昂贵。
- DPO：离线 chosen/rejected preference，省去显式 Reward Model/PPO rollout，稳定易实现，但探索能力受静态数据限制。
- GRPO 类方法：对同一 prompt 采多个响应，使用组内相对 reward 构造 advantage，通常省独立 value model，特别适合数学/代码等可验证奖励。
### 边界与工程
- 可验证任务有 deterministic reward 时在线 RL 更有价值；纯主观风格任务 reward/judge 偏差更难控制。
- 方法比较必须固定 rollout 数、token budget、reward cost 与训练 compute，否则只比最终 benchmark 不公平。
- 面试中不要把“GRPO=更先进所以总选它”作为结论；真正选择取决于 reward 可得性、在线采样成本和训练稳定性。

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

- 只比较公式，不谈数据/工程条件。

## 9. 追问树

1. GRPO 的组内标准化有什么作用？
2. 纯 outcome reward 会导致哪些过程错误？

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

- [DeepSeekMath / GRPO](https://arxiv.org/abs/2402.03300)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q073 DPO 为什么不需要显式 Reward Model？](Q073-dpo.md)
- [Q075 Sparse Retrieval 与 Dense Retrieval 的核心差异](../07-retrieval-rag/Q075-sparse-vs-dense-retrieval.md)
- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)

## 13. 一句话收束

> **PPO、DPO、GRPO 先按“数据从哪里来”分类**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
