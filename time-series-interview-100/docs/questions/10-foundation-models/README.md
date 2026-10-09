# 第 10 章：Time-Series Foundation Models

> TimesFM、Chronos、Moirai、zero-shot、多变量、协变量与概率预测

## 本章学习目标

TSFM 的关键不是‘更大’，而是跨域预训练、zero-shot/few-shot、统一概率输出，以及对多变量和协变量的原生支持。

## 题目索引

- [Q097 什么叫 Time-Series Foundation Model？](q097-time-series-foundation-model.md) - ★★★★★ / ★★★★★
- [Q098 TimesFM、Chronos、Moirai 的思想有什么不同？](q098-timesfm-chronos-moirai.md) - ★★★★★ / ★★★★★
- [Q099 Foundation Model 会不会淘汰 ARIMA / LightGBM？](q099-will-foundation-models-replace-classical.md) - ★★★★★ / ★★★★★
- [Q100 2026 前沿：TimesFM-3 相比 TimesFM-2.5 真正解决了什么？](q100-timesfm3-vs-timesfm25.md) - ★★★★★ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- Patch/Transformer/global model
- 概率预测
- 严格 zero-shot evaluation

### 本章统一答题框架

1. 区分 family history 与当前 checkpoint capability
2. 审查 pretraining leakage
3. 在同一 rolling protocol 下比较 classical/GBDT/DL/TSFM

### 本章综合 Case

> **给你一个新的多变量零售数据集，不能训练大模型，只能 zero-shot：设计 Chronos-2 / TimesFM-3 / classical baseline 的公平评估。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- TSFM 必须检查预训练数据与 benchmark 的污染风险。
- zero-shot、fine-tuned、task-specific baseline 在同一回测协议下比较。
- 比较模型时同时记录 context length、covariate support、probabilistic outputs、latency 和显存。
