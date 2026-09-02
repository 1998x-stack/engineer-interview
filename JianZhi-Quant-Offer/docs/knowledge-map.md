# Knowledge Map

这 100 道题不是十个孤立章节，而是一张从**不确定性推理 → 统计可信度 → 时间依赖 → 预测 → 市场机制 → 回测 → 优化 → 定价 → 系统**逐步展开的能力图。

```text
A Probability ──→ B Statistical Inference
      │                   │
      ↓                   ↓
C Stochastic ──→ D Time Series ──→ E Financial ML
                                      │
F Microstructure ─────────────────────┤
      │                               ↓
      └────────────→ G Research / Backtest
                         │       │
                         ↓       ↓
                    H Portfolio  J Systems
                         │
                         ↓
                    I Derivatives
```

## A. 概率论、条件概率与期望 (001–010)

**核心问题：** 在不确定条件下，正确的样本空间、依赖与条件信息是什么？

主工具：counting、Bayes、linearity of expectation、stopping recursion、order statistics、joint dependence。

**通向后续：** A 是 C 的基础，也是 F 中 adverse selection、E 中概率校准的底层语言。

## B. 数理统计与统计推断 (011–020)

**核心问题：** 一个观察到的效果，有多大可能只是估计噪声和研究选择？

主工具：MLE、bias-variance、hypothesis testing、HAC、regularization、bootstrap、robust statistics、coverage。

**通向后续：** B 直接支撑 D/E/G/H 的可信度评估。

## C. 随机过程 (021–030)

**核心问题：** 随机状态如何随时间演化，当前信息如何约束未来条件分布？

主工具：Brownian motion、martingale、stopping time、SDE、OU、Poisson、Markov/HMM/Kalman。

**通向后续：** C 是 I 衍生品连续时间定价的基础，也为 D 的状态空间建模提供语言。

## D. 时间序列与计量 (031–040)

**核心问题：** 时间顺序、非平稳、波动和异步采样如何改变统计推断？

主工具：stationarity、AR、unit root、cointegration、Granger、GARCH、time-aware validation、Hayashi–Yoshida 直觉。

**通向后续：** D 是 E Financial ML 和 G 回测的时间协议基础。

## E. 机器学习与 Financial ML (041–050)

**核心问题：** 在低信噪比、漂移和时间约束下，模型是否真的有增量价值？

主工具：baseline、regularized linear models、tree ensemble、pipeline leakage、IC、calibration、metric design、Transformer、drift、offline-online parity。

**核心原则：** 模型复杂度只是一个维度；数据协议和验证协议往往决定结论是否存在。

## F. 市场微观结构 (051–060)

**核心问题：** 报价、订单、队列、成交和延迟如何共同生成短周期价格数据？

主工具：mid/spread、bid-ask bounce、adverse selection、LOB imbalance、priority、fill probability、market impact、tick、microprice、latency。

**通向后续：** F 与 G/J 必须联读：没有 execution model 的短周期 backtest 通常不完整。

## G. 数据、回测与研究方法论 (061–070)

**核心问题：** 如何证明一个历史结果不是数据错误、选择偏差或仿真假象？

主工具：look-ahead、survivorship、corporate actions、PIT、cost model、Sharpe audit、walk-forward、missingness、research overfitting、lineage。

**核心原则：** 这是全书研究纪律的中心。任何模型进入真实研究前，都应该通过 G 的审计。

## H. 组合、风险与优化 (071–080)

**核心问题：** 当输入参数本身有噪声时，优化器会如何放大误差？

主工具：minimum variance、covariance conditioning、shrinkage、PCA、VaR/ES、vol targeting、risk contribution、regularized optimization、turnover、neutralization。

**核心原则：** 闭式最优通常不是部署最优；稳定、约束和估计误差同样重要。

## I. 衍生品与定价 (081–090)

**核心问题：** 无套利和复制如何决定价格，现实摩擦又如何破坏理想模型？

主工具：put-call parity、Black-Scholes、risk-neutral pricing、Greeks、IV、smile/skew、American optimal stopping、discrete hedging。

**核心原则：** 先理解 replication，再记公式；先理解 model risk，再解释 Greek/PnL。

## J. Coding、算法与量化系统 (091–100)

**核心问题：** 如何让研究逻辑在数据规模、状态复杂度和实时约束下仍然正确、可重放、可观测？

主工具：sliding window、heap/top-k、LOB state machine、timestamp QA、as-of join、vectorization、cache locality、research-to-prod、parity debugging。

**核心原则：** 正确性和可重现优先于微优化；性能优化必须建立在正确状态语义上。

## 最重要的四条跨章节主线

1. **Information Set**：A → D → G → J
2. **Estimation Risk**：B → E → H
3. **State & Dynamics**：C → D → F → J
4. **No-Arbitrage / Replication / Risk**：A → C → H → I

如果能沿四条主线把不同章节连接起来，面试中的陌生问题就不再是“没见过的题”，而只是熟悉结构的新表述。
