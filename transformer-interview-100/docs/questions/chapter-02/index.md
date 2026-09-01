# 第 2 章 · Attention 数学与实现细节

> 把 Attention 当作一个数值算法而不是公式记忆：score、scale、mask、softmax、多头、复杂度、解释性与替代方案。

## 本章完成标准

- 手推 sqrt(dk)
- 写 stable softmax
- 组合 causal/padding mask
- 算参数/FLOPs
- 解释 Linear vs Softmax Attention

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q011 写出 Scaled Dot-Product Attention，并逐项解释](Q011.md) | attention |
| [Q012 为什么必须除以 √d_k？](Q012.md) | transformer |
| [Q013 为什么 Mask 要加在 Softmax 之前？](Q013.md) | attention |
| [Q014 Softmax 如何避免数值溢出？](Q014.md) | attention |
| [Q015 为什么需要 Multi-Head Attention？](Q015.md) | attention |
| [Q016 为什么通常设置 d_head=d_model/H？](Q016.md) | attention |
| [Q017 Q、K、V 为什么使用不同投影？](Q017.md) | attention |
| [Q018 为什么使用 Dot-Product Attention，而不是任意 MLP 相似度？](Q018.md) | attention |
| [Q019 Self-Attention 的时间复杂度到底是多少？](Q019.md) | attention |
| [Q020 Causal Mask 的矩阵结构是什么？](Q020.md) | attention |
| [Q021 Padding Mask 与 Causal Mask 如何组合？](Q021.md) | attention |
| [Q022 Attention Dropout 通常加在哪里？](Q022.md) | attention |
| [Q023 Attention Weight 能否直接作为模型解释？](Q023.md) | attention |
| [Q024 为什么 Linear Attention 不能简单替代 Softmax Attention？](Q024.md) | attention, systems |
| [Q025 写出经典 Sinusoidal Position Encoding](Q025.md) | position, coding |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-01/index.md) · [下一学习节点](../chapter-03/index.md)
