---
id: Q098
title: "手写 Multi‑Head Attention：Shape、Mask、Contiguous"
chapter: "手写代码与 Debug"
difficulty: "★★★★"
frequency: "★★★★★"
tags:
  - coding-debug
  - attention
source: "NLP / LLM 算法岗面试 100 题 - 2026 专业版"
status: expanded
version: "2.0"
last_updated: "2026-09-01"
reading_time: "5 min"
answer_depth: "professional"
---

# Q098 手写 Multi‑Head Attention：Shape、Mask、Contiguous

[← Q097](Q097-stable-softmax.md) | **第 10 章 · 手写代码与 Debug** | [Q099 →](Q099-vectorized-1nn.md)

> **难度**：★★★★  ·  **频率**：★★★★★  ·  **标签**：`coding-debug`, `attention`

> 本页以 PDF v1.0 为基线扩写。PDF 原始文本保存在 [`sources/questions_raw`](../../sources/questions_raw/Q098.txt)，原始 PDF 见 [`assets/pdf`](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)。

## 1. 题目

不调用 nn.MultiheadAttention，实现 self-attention。列出关键 shape。

## 2. 面试官到底在考什么

高频白板/现场 coding。

### 评分维度

- 先写 invariant/shape，再写代码。
- 覆盖边界测试、数值稳定性与复杂度。
- 能指出生产级实现与白板版本的差距。

## 3. 30-60 秒标准回答

输入 [B,T,D] 线性投影后 reshape 为 [B,H,T,Dh]；score 为 q @ k^T → [B,H,T,T]；scale、mask、 softmax 后乘 v，再 transpose/contiguous/reshape 回 [B,T,D] 并过输出投影。

## 4. 白板核心结构

本题更强调概念结构与工程权衡。面试时优先画出数据流、状态转移或模块关系，再补充必要公式。

## 5. 第一性原理与 Know-Why

- **PDF 基线要点**：transpose 后 tensor 可能 non-contiguous，view 前需 contiguous 或使用 reshape。
- **PDF 基线要点**：padding mask、causal mask 的 broadcast shape 要验证。
- **PDF 基线要点**：生产实现要考虑 fused QKV、FlashAttention 与 dropout。
- **扩展理解**：手写 MHA 首先写清 shape：B,T,D -> B,H,T,Dh；然后 score、mask、softmax、V 聚合、merge heads。
- **扩展理解**：常见 bug 包括 transpose 轴错、mask 方向、softmax dim、non-contiguous view。
- **扩展理解**：进一步应比较手写实现与 fused SDPA/FlashAttention 的内存行为。

## 6. 专业深挖：原理、边界与工程

### 手写 MHA 的难点是 Shape/Mask，不是矩阵乘法
- 从 `[B,T,d]` 投影 Q/K/V 后 reshape+transpose 到 `[B,H,T,D_h]`；score 为 `[B,H,Tq,Tk]`，Softmax 沿最后的 key 维。
- Causal/Padding Mask 必须在 Softmax 前作用 logits；Multi-Head 输出再 transpose 回 `[B,T,H,D_h]`，concat 为 `[B,T,d]` 经 $W_O$。
- `transpose` 后张量可能 non-contiguous，直接 `view` 是经典 PyTorch bug，应 `.contiguous().view(...)` 或安全 `reshape`。
### 边界与工程
- 写完先和 `torch.nn.functional.scaled_dot_product_attention`/naive reference 对拍输出与梯度。
- GQA 扩展时 Q head 数与 KV head 数不同，不能沿用 MHA 的一一 reshape 假设。
- Cached Decode 扩展还要处理 $T_q=1$、KV append、RoPE position offset 和不同 batch sequence length。

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

- softmax dim 错。
- 忘 scale/mask。
- head 维与 seq 维调换。

## 9. 追问树

1. 如果从 MHA 改成 GQA，Q/K/V 的 head shape 分别怎么变化？
2. 加入 causal mask、padding mask 与 KV cache 后，query length 和 key length 分别是多少？
3. 为什么 transpose 之后直接 view 可能出错？contiguous/reshape 的差异是什么？
4. 如何用 PyTorch SDPA 作为 reference implementation 做数值对齐测试？

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

- [PyTorch scaled dot product attention docs](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html)
- [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)
- [本项目原始 PDF](../../assets/pdf/NLP_LLM_Interview_100_Professional_2026.pdf)

## 12. 关联题目与知识网络

- [Q097 手写 Numerical Stable Softmax](Q097-stable-softmax.md)
- [Q099 Vectorized 1‑NN：禁止 Python For‑loop](Q099-vectorized-1nn.md)
- [Q100 Transformer Debug + 实现 KV Cache：综合终局题](Q100-transformer-debug-kv-cache.md)

## 13. 一句话收束

> **手写 MHA 的难点是 Shape/Mask，不是矩阵乘法**：先给出核心结论，再用公式/结构证明它，最后补充边界条件与工程验证。

---

**复习动作**：60 秒标准回答 → 白板公式/shape → 专业深挖 → 回答原题追问 → 给一个失败模式 → 给一个工程验证方案。
