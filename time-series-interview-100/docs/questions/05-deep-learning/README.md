# 第 5 章：深度学习预测模型

> RNN/LSTM、DeepAR、N-BEATS、TFT、PatchTST、iTransformer、TimeMixer

## 本章学习目标

深度模型要从 inductive bias 解释：它在时间、变量、尺度、概率分布中的哪一维增加了表达能力，代价是什么。

## 题目索引

- [Q051 RNN 为什么适合时序？](q051-rnn-for-time-series.md) - ★★☆☆☆ / ★★★★☆
- [Q052 LSTM 比 RNN 改进了什么？](q052-lstm-improvements.md) - ★★★☆☆ / ★★★★★
- [Q053 DeepAR 的核心思想是什么？](q053-deepar.md) - ★★★★☆ / ★★★★★
- [Q054 N-BEATS 为什么特殊？](q054-nbeats.md) - ★★★★☆ / ★★★★☆
- [Q055 N-HiTS 相比 N-BEATS 改了什么？](q055-nhits.md) - ★★★★☆ / ★★★★☆
- [Q056 Temporal Fusion Transformer 为什么适合工业 forecasting？](q056-temporal-fusion-transformer.md) - ★★★★★ / ★★★★★
- [Q057 Transformer 做时间序列一定比简单模型好吗？](q057-transformer-vs-simple-models.md) - ★★★★☆ / ★★★★★
- [Q058 DLinear 的思想是什么？](q058-dlinear.md) - ★★★☆☆ / ★★★★☆
- [Q059 PatchTST 为什么 Patch？](q059-patchtst.md) - ★★★★☆ / ★★★★★
- [Q060 iTransformer 的 “Inverted” 是什么？](q060-itransformer.md) - ★★★★☆ / ★★★★★
- [Q061 Autoformer 解决什么问题？](q061-autoformer.md) - ★★★★☆ / ★★★★☆
- [Q062 FEDformer 为什么进入频域？](q062-fedformer.md) - ★★★★☆ / ★★★★☆
- [Q063 TSMixer / TiDE 告诉我们什么？](q063-tsmixer-tide.md) - ★★★☆☆ / ★★★★☆
- [Q064 TimeMixer 的核心思想是什么？](q064-timemixer.md) - ★★★★☆ / ★★★★☆
- [Q065 为什么时序 normalization 比普通 ML 更棘手？](q065-time-series-normalization.md) - ★★★★☆ / ★★★★★

<!-- CHAPTER_V2_START -->
## 深度学习路线

### 先修知识

- RNN/attention/MLP 基础
- 概率预测与 quantile
- global forecasting

### 本章统一答题框架

1. 先问模型的 inductive bias
2. 再问数据量与 context/horizon
3. 最后比较 accuracy/calibration/cost

### 本章综合 Case

> **同一数据上 PatchTST 比 DLinear 只好 0.5%，但推理慢 8 倍：说明你如何做上线决策。**

建议完成本章后，用 10～15 分钟口述这个 case；要求至少包含：假设、baseline、验证协议、失败模式和生产 fallback。

### 章节掌握标准

- **初级：** 能准确给出定义和核心公式。
- **中级：** 能比较方法、解释假设和常见失败模式。
- **高级：** 能把统计/模型结论落到 point-in-time backtest、业务 loss 与生产约束。
- **Staff/Research：** 能给出替代方案、反例、消融设计，并解释为什么某个复杂模型不一定值得上线。
<!-- CHAPTER_V2_END -->

## 本章工程检查

- 先建立强简单 baseline，再比较深度模型。
- 报告参数量、上下文长度、推理 latency 与 horizon-specific error。
- 概率模型要同时评估 calibration 与 sharpness。
