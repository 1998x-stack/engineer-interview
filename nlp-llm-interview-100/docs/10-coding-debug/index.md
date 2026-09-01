# 第 10 章 · 手写代码与 Debug

> **章节目标**：用少量代码检验数值稳定性、向量化能力、Tensor shape 与系统级 Debug 方法。

## 1. 先修知识

NumPy/PyTorch、矩阵运算、单元测试。

## 2. 本章知识路线

Q097 数值 → Q098 Tensor 实现 → Q099 向量化 → Q100 综合 Transformer/KV Debug。

## 3. 必须白板掌握

- Stable Softmax/LogSumExp
- MHA shape/mask
- 1-NN 距离展开
- Cached vs Full logits consistency

## 4. 高频失分模式

- 先优化后验证
- broadcast 静默错误
- transpose 后 view
- torch.cat cache O(T²) copy
- 只修语法 bug

## 5. 题目清单

| 题号 | 题目 | 难度 | 频率 |
|---|---|:---:|:---:|
| Q097 | [手写 Numerical Stable Softmax](Q097-stable-softmax.md) | ★★★ | ★★★★★ |
| Q098 | [手写 Multi‑Head Attention：Shape、Mask、Contiguous](Q098-implement-mha.md) | ★★★★ | ★★★★★ |
| Q099 | [Vectorized 1‑NN：禁止 Python For‑loop](Q099-vectorized-1nn.md) | ★★★★ | ★★★★ |
| Q100 | [Transformer Debug + 实现 KV Cache：综合终局题](Q100-transformer-debug-kv-cache.md) | ★★★★★ | ★★★★★ |

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
