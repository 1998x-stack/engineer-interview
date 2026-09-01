# 使用说明：如何把 100 题刷成真正的面试能力

这套仓库不是“答案库”，而是一套 **retrieval practice + derivation + implementation + verification** 的训练系统。

## 1. 一道题的正确刷法

### Pass A · 30 秒

只看题目，不看正文。说：

1. 一句话结论；
2. 一个核心公式/shape；
3. 一个 trade-off。

如果超过 60 秒仍找不到主线，说明知识还没有压缩。

### Pass B · 3 分钟

必须展开：

`Definition → Formula → Why → Cost → Gotcha → Verify`

参考 [六层回答法](six-layer-answer.md)。

### Pass C · Whiteboard

关闭答案，手写：

- 符号定义；
- tensor shape；
- 参数/FLOPs；
- 边界条件；
- 一个数值例子。

### Pass D · Coding

能写的题必须写：

- reference attention；
- causal mask；
- KV cache；
- full-vs-cache parity；
- tiny overfit；
- shape assertion。

“看懂代码”不等于“能在面试中实现”。

### Pass E · Experiment

至少设计一个可证伪实验：

- 为什么 mask 错？→ future perturbation；
- 为什么 cache 错？→ logits parity；
- 为什么优化有效？→ profiler + length sweep；
- 为什么长上下文有效？→ position-bucket eval。

## 2. 必须脱稿的 12 个对象

1. Attention 公式；
2. `[B,T,D] ↔ [B,H,T,Dh]`；
3. $O(Td^2+T^2d)$；
4. causal/padding mask；
5. stable softmax；
6. RoPE 相对旋转；
7. Pre-Norm / RMSNorm；
8. SwiGLU；
9. CLM objective / label shift；
10. KV cache memory；
11. GQA/MQA；
12. online softmax / FlashAttention。

## 3. 错题记录模板

建议维护自己的 `mistakes.md`：

```markdown
## Q069 KV Cache
- 我答错的点：忘记 K/V 两份
- 正确公式：2LBTHkvDh·bytes
- 为什么会错：只记了单 tensor
- 反例：32K GQA 手算
- 下次回答第一句：...
```

记录“为什么错”比复制标准答案更有效。

## 4. 难度分级

| 难度 | 达标标准 |
|---|---|
| 1–2/5 | 定义、公式、shape 不错 |
| 3/5 | 能推 Why / complexity / Gotcha |
| 4/5 | 能区分训练、prefill、decode，并给实验 |
| 5/5 | 面对陌生变体能现场建模、算账、找反例 |

## 5. Mock Interview 规则

每轮 45–60 分钟：

- 5 分钟：基础快问 5 道；
- 15 分钟：数学/推导 2 道；
- 20 分钟：Coding/Debug 1 道；
- 15 分钟：Serving/System 1 道。

面试官必须继续追问至少三层：

`Why? → What if T×4? → How do you verify?`

## 6. 如何判断“真的会了”

满足全部：

- 不看答案能写公式；
- 能给一个反例；
- 能算一个具体数字；
- 能写测试；
- 能说明训练/推理是否不同；
- 能指出一个系统瓶颈。

只会复述定义不算掌握。
