# 六层面试回答法：从“知道”到 Strong Hire

## Layer 1 · Definition：先把对象说清楚

模板：

> X 是一个……，输入是……，输出是……，它主要解决……。

禁止一上来讲历史或堆论文名。

## Layer 2 · Formula + Shape：建立可检查对象

例如 Attention：

\[
Q:[B,H,T_q,D_h],\quad K:[B,H,T_k,D_h]
\]

\[
QK^T:[B,H,T_q,T_k]
\]

一旦 shape 清楚，softmax 轴、mask broadcast、复杂度就容易推。

## Layer 3 · Why：没有它会怎样？

比“它有什么优点”更重要。

例：为什么除 $\sqrt{d_k}$？如果不除，logit 标准差随 $\sqrt{d_k}$ 增大，softmax 更容易饱和。

## Layer 4 · Cost：不要只写 Big-O

至少分：

- parameters；
- FLOPs；
- activation memory；
- KV memory；
- HBM IO；
- communication；
- latency/throughput。

高级题要分 train / prefill / decode。

## Layer 5 · Gotcha / Boundary：主动证明你做过

好的 Gotcha 不是“可能出 bug”，而是：

> fully-masked row 全是 $-\infty$，softmax 可能 NaN；我会写一个 padding+causal 的参数化单测。

## Layer 6 · Verify + Trade-off：把观点变成实验

提出：

- reference parity；
- future leakage test；
- tiny overfit；
- profiler；
- length/concurrency sweep；
- quality regression。

最后收束：

> 所以在条件 A 下我会选 X；如果条件变成 B，瓶颈转移，我会重新评估 Y。

## 30 秒 / 3 分钟 / 15 分钟三个版本

### 30 秒

`结论 + 公式 + trade-off`

### 3 分钟

`六层完整走一遍`

### 15 分钟

加入：

- 数值例子；
- 手写代码；
- profiler/ablation；
- 邻近方案对比。

## Strong Hire 自检

回答后问自己：

- 我有没有说明假设？
- 有没有量化？
- 有没有反例？
- 有没有测试？
- 有没有把训练/推理分开？

五个“有”，通常比背更多名词更有区分度。
