# 第 5 章 · BERT、GPT 与 Encoder-Decoder

> 用 attention 可见性与概率分解统一理解 encoder-only、decoder-only、encoder-decoder，而不是背模型名。

## 本章完成标准

- MLM vs CLM
- bidirectional vs causal
- Teacher Forcing
- Exposure Bias
- Cross-Attention

## 建议学习顺序

1. 第一遍只看题目和 30 秒答案；
2. 第二遍关闭答案，手写公式/shape；
3. 第三遍完成至少一个数值或 coding 实验；
4. 最后随机抽本章 3 题，连续追问 Why → Cost → Gotcha → Verify。

## 本章题目

| 题目 | Tags |
|---|---|
| [Q045 Encoder-only、Decoder-only、Encoder-Decoder 的本质区别？](Q045.md) | inference |
| [Q046 BERT 为什么可以双向？](Q046.md) | bert-gpt |
| [Q047 BERT 为什么用 MLM，而 GPT 用 CLM？](Q047.md) | bert-gpt |
| [Q048 BERT 的 NSP 是什么，为什么后来常被移除？](Q048.md) | bert-gpt |
| [Q049 GPT 的 Causal LM 训练目标是什么？](Q049.md) | bert-gpt |
| [Q050 为什么自回归模型训练时还能并行？](Q050.md) | transformer |
| [Q051 为什么 Decoder-only 成为通用 LLM 主流之一？](Q051.md) | inference |
| [Q052 Cross-Attention 为什么适合机器翻译？](Q052.md) | attention |
| [Q053 Teacher Forcing 是什么？](Q053.md) | bert-gpt |
| [Q054 Exposure Bias 是什么？](Q054.md) | bert-gpt |

## 本章自测

- 能否不看资料画出本章最关键的计算图？
- 能否给出至少一个“看起来对但其实错”的实现？
- 能否把一个超参数扩大 4 倍并预测参数/FLOPs/显存/latency 哪个先变化？
- 能否设计 reference parity 或 ablation 证伪自己的观点？

## 章节连接

[上一学习节点](../chapter-04/index.md) · [下一学习节点](../chapter-06/index.md)
