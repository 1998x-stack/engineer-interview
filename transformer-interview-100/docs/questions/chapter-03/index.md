# 第 3 章 · 位置编码与 RoPE

> 从 permutation equivariance 出发，理解 absolute/relative position、RoPE 几何、ALiBi、插值和有效长上下文。

## 本章完成标准

- 推导 RoPE 相对旋转
- 解释 Q/K 而非 V
- 区分技术 max context 与有效 context
- 设计长度外推评测

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q026 为什么原始 Transformer 使用固定 Sin/Cos？](Q026.md) | position |
| [Q027 Learned Position Embedding 有什么限制？](Q027.md) | position |
| [Q028 Absolute Position 与 Relative Position 的区别是什么？](Q028.md) | position |
| [Q029 RoPE 的核心数学是什么？](Q029.md) | position |
| [Q030 为什么 RoPE 通常作用在 Q/K 而不是 V？](Q030.md) | position |
| [Q031 RoPE 为什么会遇到长上下文外推问题？](Q031.md) | position, systems |
| [Q032 ALiBi 与 RoPE 的思想有什么区别？](Q032.md) | position |
| [Q033 Position Interpolation 的基本思想是什么？](Q033.md) | position |
| [Q034 技术上支持 64K 与真正有效 64K 有什么区别？](Q034.md) | transformer |
| [Q035 Pre-LN 与 Post-LN 有什么区别？](Q035.md) | normalization |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-02/index.md) · [下一学习节点](../chapter-04/index.md)
