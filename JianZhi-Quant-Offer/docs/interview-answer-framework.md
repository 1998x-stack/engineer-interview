# Quant Interview Answer Framework

这是一套适用于概率、统计、ML、市场微观结构、回测和系统设计的统一回答框架。目标不是让答案模板化，而是在压力环境下避免漏掉最重要的层次。

## 1. 30 秒回答：D-C-A-R

| 步骤 | 含义 | 你应该说什么 |
|---|---|---|
| D | Define | 定义随机变量、状态、时间信息集或输入输出 |
| C | Conclusion | 直接给核心结论/公式/复杂度 |
| A | Assumption | 指出最关键的一个假设 |
| R | Risk | 点出最容易犯的一个错误或失效条件 |

示例结构：

> “我先把状态定义成……。在这个假设下，核心递推/优化目标是……，所以答案是……。这里最重要的条件是……；如果它不成立，我不会直接套这个结论。”

## 2. 3 分钟回答：F-D-W-B-V

### F — Formalize

把口头题变成数学/系统对象：

- random variables / filtration；
- state machine / invariants；
- objective / constraints；
- feature / label / available-at timestamp。

### D — Derive

只走一条主线。优先选择现场最稳的方法，而不是最炫的方法：

- probability：conditioning / indicator / recursion / CDF；
- statistics：likelihood / sampling distribution / robust SE；
- optimization：Lagrangian / KKT / convexity；
- systems：data structure / state transition / complexity。

### W — Why

回答“为什么这个结构成立”。这是最能体现理解深度的一层。

### B — Boundary

主动说一个边界：

- independence 被破坏；
- distribution shift；
- singular covariance；
- incomplete market；
- missing sequence；
- latency 与 signal horizon 同量级。

### V — Verify

给出验证策略：

- simulation / Monte Carlo；
- walk-forward / untouched holdout；
- block bootstrap / HAC；
- replay / golden dataset；
- shadow deployment / parity test。

## 3. 开放研究题：Research Loop

```text
Question
  ↓
Target / label / horizon
  ↓
Point-in-time information set
  ↓
Simple baseline
  ↓
Leakage-safe validation
  ↓
Incremental model / feature
  ↓
Ablation + placebo + sensitivity
  ↓
Cost / fill / latency / capacity
  ↓
Reproducibility + production parity
```

### 面试中优先问清的五件事

1. 预测 horizon 是什么？
2. feature 在什么时间真正可获得？
3. 样本是 time-series、cross-sectional 还是 panel？
4. metric 是统计 metric 还是真实 utility？
5. production 中有哪些成本/延迟/约束？

## 4. Coding / Systems 题：C-S-I-F

- **Correctness**：状态和输出到底什么才算正确？
- **State & invariants**：维护什么状态，不变量是什么？
- **Implementation complexity**：time / space / cache / I/O。
- **Failure recovery**：duplicate、gap、out-of-order、replay、idempotency。

只回答 Big-O 而不回答状态正确性，通常不是 Quant Systems 的完整答案。

## 5. 面试官在听的五层能力

| 层级 | 能力 | 典型正向信号 | 典型失败 |
|---|---|---|---|
| L1 | 定义 | 主动澄清对象和条件 | 直接套公式 |
| L2 | 正确性 | 推导/代码可验证 | 条件方向、边界、复杂度错 |
| L3 | 模型意识 | 明确结论依赖哪些假设 | 把模型当现实 |
| L4 | 研究可信度 | OOS、ablation、robustness | 只报一个最好分数 |
| L5 | 生产意识 | PIT、cost、latency、replay、parity | 把 notebook 结果等同 live |

## 6. 不推荐的表达习惯

- “这个公式就是……”——没有说明条件；
- “一般都用 Transformer/XGBoost”——没有 baseline 和数据条件；
- “市场变了”——没有先排除 parity/data bug；
- “Sharpe 很高所以有效”——没有 multiple testing 和 cost audit；
- “价格碰到限价就成交”——没有 queue/fill model。

## 7. 最终检查

回答结束前快速问自己：

> 我有没有说清楚 **对象、结论、假设、边界、验证**？

如果五项都覆盖，通常已经是一份结构成熟的 Quant 面试答案。
