---
id: Q069
title: "知识蒸馏有哪些层级？"
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

# Q069 知识蒸馏有哪些层级？

[← Q068](Q068-qlora.md) | **第 6 章 · SFT、PEFT 与对齐** | [Q070 →](Q070-rlhf.md)

> **难度**：★★★  ·  **频率**：★★★★  ·  **标签**：`alignment`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q069.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

Response、Feature、Relation Distillation 分别蒸馏什么？LLM 时代又出现哪些新形态？

## 2. 面试官到底在考什么

从 logits 到 reasoning/data distillation。

### 评分维度

- 先区分数据、目标函数与在线/离线优化。
- 能解释 reference/reward/preference 的角色。
- 讨论稳定性、成本、reward hacking 与数据偏差。

## 3. 30-60 秒标准回答

Response distillation 对齐教师输出分布/文本，Feature distillation 对齐中间表示，Relation distillation 对齐样本/注意力关系。LLM 时代还大量使用教师生成的 SFT、偏好、推理轨迹作为数 据蒸馏。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：soft target 的 temperature 可暴露类别相似性。
- **PDF 基线要点**：生成式数据蒸馏更依赖教师错误与风格偏差控制。
- **PDF 基线要点**：学生容量决定能否吸收教师全部知识。
- **扩展理解**：蒸馏可分 logits/response、feature、relation、sequence/reasoning 等层级。
- **扩展理解**：teacher 更强不保证 student 数据一定更有 utility，需考虑容量匹配与错误继承。
- **扩展理解**：LLM 时代还要区分生成式数据蒸馏与在线 soft-target distillation。

## 6. 专业深挖：原理、边界与工程

### Distillation 不只是“教师给答案”
- Response/Logit Distillation 让 student 拟合 teacher soft distribution；温度升高可暴露类别间“暗知识”，比 hard label 更丰富。
- Feature Distillation 对齐中间 hidden/attention；Relation Distillation 对齐样本/Token 间关系；LLM 时代还有生成式 data distillation、reasoning trace distillation。
- 核心目标是把 teacher 的函数/行为压缩到更小或更便宜的 student，而不是简单复制训练集答案。
### 边界与工程
- Teacher 不是 oracle，错误和风格偏差会被蒸馏；可验证任务应优先用执行器/规则过滤生成轨迹。
- Student capacity 太小或 tokenizer/architecture 差异大时，逐层 feature 对齐未必合理。
- 评估必须看 student latency/成本与质量 Pareto，而不是只看相对 teacher 的分数。

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

- 认为学生一定能达到教师。

## 9. 追问树

1. temperature 对 KL 有什么作用？
2. reasoning distillation 的隐藏风险？

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

- [Q068 QLoRA 为什么能在更小显存上微调大模型？](Q068-qlora.md)
- [Q070 RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md)
- [Q066 LoRA 的低秩假设到底是什么？](Q066-lora.md)
- [Q074 PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md)

## 13. 一句话收束

> **Distillation 不只是“教师给答案”**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
