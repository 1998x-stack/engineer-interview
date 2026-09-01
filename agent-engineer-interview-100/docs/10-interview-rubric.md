# Agent Engineer 面试评分 Rubric

> GitHub Edition 扩展。用于自测、模拟面试或团队校准。

## 总分 100

| 维度 | 分值 | 看什么 |
|---|---:|---|
| Problem Framing | 15 | 能否先定义语义、目标和 invariant |
| Architecture / State | 20 | 控制流、状态所有权、接口设计 |
| Reliability | 25 | failure mode、idempotency、retry、recovery |
| Security / Observability | 20 | trust boundary、权限、trace、eval |
| Trade-off / Communication | 20 | 边界、成本、清晰度、追问稳定性 |

## 1. Problem Framing — 15 分

### 0–5

直接报技术方案，没有澄清“成功/失败/完成”的语义。

### 6–10

能识别主要约束，但 invariant 不够明确。

### 11–15

先定义不可违反条件，并能解释为什么这个条件决定后续架构。

## 2. Architecture / State — 20 分

高分答案应主动说明：

- run/task/step identity。
- durable state vs context。
- owner 与 source of truth。
- sync/async 边界。
- completion verifier。

只画 LLM / Vector DB / Tools，通常不超过 8–10 分。

## 3. Reliability — 25 分

考察是否能处理：

- timeout != failure。
- duplicate / out-of-order。
- crash window。
- partial success。
- retryability。
- checkpoint/resume。
- Saga/compensation。
- cancellation。

### 20+ 分表现

候选人会主动故障注入，而不是等面试官提醒。

## 4. Security / Observability — 20 分

至少需要：

- model is not authorization boundary。
- least privilege。
- resource-side auth。
- sensitive trace policy。
- trace/span correlation。
- failure attribution。
- regression / canary。

## 5. Trade-off / Communication — 20 分

高分答案不是“永远应该 X”，而是：

```text
默认方案 A
因为：...
如果条件 B 出现，则切换方案 C
代价：...
验证：metric/eval ...
```

## 分数解释

| 总分 | 水平 |
|---:|---|
| <60 | 主要停留在框架/API 层 |
| 60–74 | 能做 Agent 应用，但 Production 深度不足 |
| 75–84 | 合格的生产 Agent Engineer |
| 85–92 | Senior，能独立做可靠性/系统设计 |
| 93+ | Staff 倾向，能抽象 runtime、治理与组织级标准 |

## 一票否决型问题

在高风险系统设计中，如果出现以下表达且无法修正，应大幅扣分：

- “Prompt 里写了不能越权，所以安全。”
- “Timeout 就 retry 三次。”
- “模型说完成了就结束。”
- “所有上下文都塞给模型，窗口够大。”
- “Multi-Agent 肯定比 Single-Agent 强。”
- “Trace 只记最终 input/output 就行。”

## 模拟面试建议

配合 [评分模板](../templates/mock-interview-scorecard.md)；每次只挑 3–5 个维度给具体证据，避免用“感觉不错”打分。

---

## Expanded Edition 使用提示

阅读任何章节时，优先寻找三个东西：**Invariant、Failure Window、Verification Signal**。如果一个方案只有组件名而没有这三项，它通常还停留在 demo 级。完整方法见 [Expanded Edition 内容设计规范](12-expanded-edition-methodology.md)。
