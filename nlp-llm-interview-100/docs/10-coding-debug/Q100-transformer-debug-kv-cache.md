---
id: Q100
title: "Transformer Debug + 实现 KV Cache：综合终局题"
chapter: "手写代码与 Debug"
difficulty: "★★★★★"
frequency: "★★★★★"
tags:
  - coding-debug
  - kv-cache
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q100 Transformer Debug + 实现 KV Cache：综合终局题

[← Q099](Q099-vectorized-1nn.md) | **第 10 章 · 手写代码与 Debug**

> **难度**：★★★★★  ·  **频率**：★★★★★  ·  **标签**：`coding-debug`, `kv-cache`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q100.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

给数百行 Transformer，找四处 bug，再加 KV cache。你先检查什么？

## 2. 面试官到底在考什么

用一题检验模型原理、PyTorch 正确性与系统意识。

### 评分维度

- 先写 invariant/shape，再写代码。
- 覆盖边界测试、数值稳定性与复杂度。
- 能指出生产级实现与白板版本的差距。

## 3. 30-60 秒标准回答

先按不变量排查：shape、causal mask、scale、softmax dim、residual/norm、position offset、 dtype/device；再把历史 K/V 变成显式 state。prefill 写入整段 cache；decode 只追加新 K/V，新 Q 读取历史 + 当前 K/V。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：最危险 bug 是“代码能跑但数学错”：mask 方向、softmax axis、position offset。
- **PDF 基线要点**：直接 torch.cat 每步会反复复制 cache，生产应预分配或 paged blocks。
- **PDF 基线要点**：cache state 必须与 batch reorder、beam、sequence length、RoPE position 保持一致。
- **扩展理解**：综合 Debug 题要按 invariant 排查：shape、mask、scale、normalization、residual、dtype、cache position。
- **扩展理解**：KV cache 实现要区分 prefill/decode，并避免每 token torch.cat 导致反复拷贝。
- **扩展理解**：高阶回答应讨论 paged cache、GQA、beam/speculative decoding 下 cache ownership。

## 6. 专业深挖：原理、边界与工程

### Debug Transformer 要按“不变量”而不是逐行盯代码
- 第一层检查数学不变量：Q/K/V shape、$1/\sqrt{D_h}$、mask 方向、Softmax axis、residual/norm 顺序、position id、dtype/device；这些 bug 很多都“能跑但模型学错”。
- KV Cache 改造要把 state 显式化：Prefill 写入整段 K/V，Decode 每步只计算新 K/V 并追加；历史 Q 不缓存。
- RoPE 模型必须保证 cached K 与 position convention 一致，新 token 的 absolute position 不能重置；GQA 则要求 cache shape 使用 $H_{kv}$。
### 边界与工程
- 不要每步 `torch.cat` 复制整段 Cache；生产用预分配或 paged blocks，并支持 batch reorder/beam/prefix sharing。
- 黄金单测：同一 tokens 做 full forward，与逐 token cached forward 拼接 logits，`allclose`；再对 padding、不同 prefix length、GQA/RoPE 做参数化测试。
- 优化顺序必须是 Reference Correctness → Cache Correctness → Memory Layout → Fused Kernel/Batching；不要在错误数学上做性能优化。

## 7. 实现、复杂度与工程验证

- 先写 reference 版本和不变量，再写向量化/缓存/融合优化。
- 测试 shape、axis、dtype、device、极端值、padding/mask 与 cached/full consistency。
- “代码能跑”不是正确性标准；必须有可自动化的数值对拍。

### 推荐验证清单

- **Correctness**：与最小 reference/手算结果对拍。
- **Numerics**：加入极端输入、低精度与长序列测试。
- **Complexity**：同时写时间、空间以及关键系统资源。
- **Ablation**：只改变一个设计变量，固定数据/compute/评测口径。
- **Slices**：不要只看总体均值，检查长尾、长度、语言/领域或 hard cases。

## 8. 高频失分点

- 只修语法错误。
- 缓存了历史 Q。
- 忘记 cache 中 RoPE 后/前的表示约定。

## 9. 追问树

1. 如何为 KV cache 写单元测试，使 cached decode 与 full forward logits 对齐？
2. RoPE position offset、causal mask 和 cache length 三者如何保持一致？
3. 如何扩展到 GQA、beam search、prefix caching 与 speculative decoding？
4. 为什么每步 torch.cat cache 会产生额外复制？生产系统如何用预分配或 paged blocks 避免？
5. 如果代码“能跑但答案错”，你会按什么 invariant 顺序定位？

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

- [vLLM / PagedAttention](https://arxiv.org/abs/2309.06180)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q099 Vectorized 1‑NN：禁止 Python For‑loop](Q099-vectorized-1nn.md)
- [Q097 手写 Numerical Stable Softmax](Q097-stable-softmax.md)

## 13. 一句话收束

> **Debug Transformer 要按“不变量”而不是逐行盯代码**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
