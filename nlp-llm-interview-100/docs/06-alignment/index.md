# 第 6 章 · SFT、PEFT 与对齐

> **章节目标**：理解后训练数据形态、参数高效微调、偏好优化与在线 RL 的统计和系统差异。

## 1. 先修知识

LM loss、优化器、KL、基础强化学习。

## 2. 本章知识路线

Q065–Q069 适配/蒸馏 → Q070–Q074 偏好与 RL。

## 3. 必须白板掌握

- Pretraining vs SFT loss mask
- LoRA ΔW=BA
- QLoRA memory accounting
- Distillation 层级
- RLHF pipeline
- REINFORCE baseline
- DPO objective
- PPO/DPO/GRPO 选择

## 4. 高频失分模式

- LoRA=低精度
- RLHF=人类打分+RL
- DPO=不需要 reference
- GRPO 永远优于 PPO
- 忽略 reward/judge bias

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q065 | [Pretraining 与 SFT 的本质区别](Q065-pretraining-vs-sft.md) | ★★ | ★★★★★ |
| Q066 | [LoRA 的低秩假设到底是什么？](Q066-lora.md) | ★★★ | ★★★★★ |
| Q067 | [LoRA 应该加 Q/V 还是加所有 Linear？](Q067-lora-target-modules.md) | ★★★ | ★★★★ |
| Q068 | [QLoRA 为什么能在更小显存上微调大模型？](Q068-qlora.md) | ★★★★ | ★★★★★ |
| Q069 | [知识蒸馏有哪些层级？](Q069-knowledge-distillation.md) | ★★★ | ★★★★ |
| Q070 | [RLHF 的经典 Pipeline 与 KL 约束](Q070-rlhf.md) | ★★★★ | ★★★★★ |
| Q071 | [REINFORCE 是 On‑policy 还是 Off‑policy？](Q071-reinforce-on-policy.md) | ★★★ | ★★★★ |
| Q072 | [REINFORCE 为什么加 Baseline 不引入偏差？](Q072-reinforce-baseline.md) | ★★★★ | ★★★★ |
| Q073 | [DPO 为什么不需要显式 Reward Model？](Q073-dpo.md) | ★★★★ | ★★★★★ |
| Q074 | [PPO、DPO、GRPO：什么时候选哪一个？](Q074-ppo-dpo-grpo.md) | ★★★★★ | ★★★★★ |

## 6. 本章训练方法

1. **第一遍：60 秒回答**——每题只看“标准回答”，建立概念地图。
2. **第二遍：闭卷白板**——公式题必须从定义推导；系统题必须画数据流/资源账本。
3. **第三遍：追问链**——每题至少回答两个“为什么”和一个“不适用条件”。
4. **第四遍：工程化**——写最小代码/复杂度，或者设计一个可验证的实验。
5. **随机复习**——不要按题号形成顺序记忆，使用索引随机抽题。

## 7. 章节完成标准

- [ ] 能不看答案完成本章所有 ★★★★/★★★★★ 题的 2–3 分钟回答。
- [ ] 关键公式能从假设推到结论，而不是只背最终式。
- [ ] 每题至少能说一个边界条件、失败模式或工程 trade-off。
- [ ] 能把相邻题串成连续知识链，而不是 100 个孤立答案。
