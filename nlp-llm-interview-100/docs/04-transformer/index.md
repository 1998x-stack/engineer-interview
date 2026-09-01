# 第 4 章 · Transformer 核心原理

> **章节目标**：达到可以白板推导、手写实现、定位数值/shape bug，并连接训练与推理系统。

## 1. 先修知识

矩阵 calculus、Softmax、PyTorch tensor shape。

## 2. 本章知识路线

Q035–Q040 Attention 数学/复杂度 → Q041–Q046 位置与 Norm → Q047–Q050 FFN/激活/GQA。

## 3. 必须白板掌握

- Self-Attention 全流程与 shape
- 1/√d_k 方差解释
- Causal Mask
- Permutation Equivariance
- RoPE 推导
- Pre-LN
- SwiGLU
- GQA→KV Cache

## 4. 高频失分模式

- 只会背架构图
- Softmax axis/mask 方向写错
- 把 FlashAttention 说成线性复杂度
- RoPE 只会画旋转不推 RmᵀRn

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q035 | [Self‑Attention 的完整计算流程](Q035-self-attention.md) | ★★★ | ★★★★★ |
| Q036 | [为什么 Attention 要除以 sqrt(d_k)？](Q036-attention-scaling.md) | ★★★ | ★★★★★ |
| Q037 | [为什么 Q、K、V 要用不同投影？](Q037-qkv-projections.md) | ★★★ | ★★★★★ |
| Q038 | [Multi‑Head Attention 为什么不是一个大 Head？](Q038-multi-head-attention.md) | ★★★ | ★★★★★ |
| Q039 | [Self‑Attention 的复杂度到底是多少？](Q039-attention-complexity.md) | ★★★★ | ★★★★★ |
| Q040 | [Causal Mask 是怎么工作的？](Q040-causal-mask.md) | ★★ | ★★★★★ |
| Q041 | [为什么 Transformer 必须注入位置信息？](Q041-position-information.md) | ★★★ | ★★★★★ |
| Q042 | [Sinusoidal Positional Encoding 的设计直觉](Q042-sinusoidal-position.md) | ★★★ | ★★★★ |
| Q043 | [RoPE：如何把相对位置写进 QK 点积？](Q043-rope.md) | ★★★★ | ★★★★★ |
| Q044 | [为什么 RoPE 通常只作用于 Q/K，不作用于 V？](Q044-rope-qk-not-v.md) | ★★★ | ★★★★ |
| Q045 | [RoPE 为什么会有长度外推问题？YaRN/PI 在解决什么？](Q045-rope-context-extension.md) | ★★★★★ | ★★★★★ |
| Q046 | [Pre‑LN 与 Post‑LN：为什么深层模型更偏 Pre‑Norm？](Q046-preln-vs-postln.md) | ★★★★ | ★★★★★ |
| Q047 | [Transformer 为什么 Attention 后还需要 FFN？](Q047-transformer-ffn.md) | ★★★ | ★★★★★ |
| Q048 | [GELU、ReLU 与 SiLU/SwiGLU 怎么比较？](Q048-activation-functions.md) | ★★★ | ★★★★ |
| Q049 | [SwiGLU 为什么成了现代 LLM 常客？](Q049-swiglu.md) | ★★★ | ★★★★ |
| Q050 | [MHA、MQA、GQA：为什么共享 K/V 能省 KV Cache？](Q050-mha-mqa-gqa.md) | ★★★★ | ★★★★★ |

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
