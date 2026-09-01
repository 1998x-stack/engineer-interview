# Transformer 论文地图与阅读顺序

> 正文以项目 PDF 为基线；本页是 Professional Expansion 的外部阅读地图。论文结论都有实验条件，不把单篇结果写成普遍定律。

## Tier 0 · 必须精读：Transformer 主干

| 主题 | 论文 | 对应题 |
|---|---|---|
| Transformer | Vaswani et al., 2017, [Attention Is All You Need](https://arxiv.org/abs/1706.03762) | Q001–Q025 |
| BERT | Devlin et al., 2018, [BERT](https://arxiv.org/abs/1810.04805) | Q045–Q048 |
| Pre-LN | Xiong et al., 2020, [On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745) | Q035–Q036 |
| RMSNorm | Zhang & Sennrich, 2019, [RMSNorm](https://arxiv.org/abs/1910.07467) | Q038 |
| GLU/SwiGLU | Shazeer, 2020, [GLU Variants Improve Transformer](https://arxiv.org/abs/2002.05202) | Q042 |
| RoPE | Su et al., 2021, [RoFormer](https://arxiv.org/abs/2104.09864) | Q029–Q031 |

### 读法

每篇只回答五个问题：

1. baseline 是什么？
2. 改了哪一个计算图节点？
3. 参数/FLOPs/Memory 是否可比？
4. 实验在哪个规模/任务成立？
5. 如何用 10 行伪代码复现核心？

## Tier 1 · 现代训练与容量

- Liu et al., 2019, [RoBERTa](https://arxiv.org/abs/1907.11692) — BERT recipe / NSP 讨论。
- Fedus et al., 2021, [Switch Transformers](https://arxiv.org/abs/2101.03961) — sparse MoE。
- Wang et al., 2022, [DeepNet / DeepNorm](https://arxiv.org/abs/2203.00555) — 深层 Transformer 稳定性。
- Hoffmann et al., 2022, [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556) — compute/data scaling。

## Tier 2 · 长上下文与位置

- Press et al., 2021, [ALiBi](https://arxiv.org/abs/2108.12409) — attention linear bias。
- Chen et al., 2023, [Extending Context Window via Positional Interpolation](https://arxiv.org/abs/2306.15595) — position interpolation。
- Beltagy et al., 2020, [Longformer](https://arxiv.org/abs/2004.05150) — local/global sparse attention。
- Dai et al., 2019, [Transformer-XL](https://arxiv.org/abs/1901.02860) — recurrence/memory + relative position。

## Tier 3 · Attention Kernel / Serving

- Dao et al., 2022, [FlashAttention](https://arxiv.org/abs/2205.14135) — IO-aware exact attention。
- Dao, 2023, [FlashAttention-2](https://arxiv.org/abs/2307.08691) — work partition / parallelism。
- Ainslie et al., 2023, [GQA](https://arxiv.org/abs/2305.13245) — KV heads trade-off。
- Kwon et al., 2023, [PagedAttention / vLLM](https://arxiv.org/abs/2309.06180) — KV memory management。
- Leviathan et al., 2023, [Speculative Decoding](https://arxiv.org/abs/2211.17192) — exact-distribution decode acceleration。

## Tier 4 · 解释与替代 Attention

- Jain & Wallace, 2019, [Attention is not Explanation](https://arxiv.org/abs/1902.10186) — attention weight 与解释性的边界。
- Katharopoulos et al., 2020, [Transformers are RNNs](https://arxiv.org/abs/2006.16236) — linear attention 的一个代表视角。

## 推荐阅读路线

### 算法岗

`Transformer → BERT → Pre-LN → RoPE → SwiGLU → GQA → FlashAttention`

### LLM Infra

`Transformer → Attention Complexity → FlashAttention → GQA → PagedAttention → Speculative Decoding → MoE`

### 长上下文

`RoPE → ALiBi → Positional Interpolation → Sparse Attention → FlashAttention → Context Parallel`

## 如何引用论文结论

面试推荐说：

> “在 X 工作的 Y 设置里，他们观察到……；机制上我理解为……；如果换到更长 T / 不同 GPU，我会重新 benchmark。”

避免：

> “论文证明 X 永远比 Y 好。”

## 关键已核验事实提示

- FlashAttention/FlashAttention-2 属于 **exact attention 的 IO/work-partition 优化**，不是线性 attention。
- PagedAttention 解决 KV cache 的动态内存管理与共享问题，而不改变模型 attention 数学定义。
- 严格 speculative decoding 的目标是加速采样，同时保持 target model 的输出分布。

这些事实应与具体论文版本和实现条件一起理解。
