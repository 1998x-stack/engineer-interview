# 复习路线与冲刺计划

## 7 天冲刺

- **Day 1**：Q001-Q020 - 时间依赖、平稳、差分、STL。
- **Day 2**：Q021-Q035 - ARIMA/ETS/状态空间。
- **Day 3**：Q036-Q050 - Lag/Rolling、GBDT、Global Model。
- **Day 4**：Q051-Q065 - DeepAR/TFT/PatchTST/iTransformer。
- **Day 5**：Q066-Q078 - 回测、泄漏、概率预测与业务 loss。
- **Day 6**：Q079-Q096 - VAR/协整/层级/漂移/系统设计。
- **Day 7**：Q097-Q100 + 30 题高频复盘 + 两次模拟系统设计。

## 30 道最高优先级

- [Q001 什么是时间序列？它与普通 IID 数据最大的区别是什么？](docs/questions/01-foundations/q001-time-series-vs-iid.md)
- [Q003 White Noise 和 Random Walk 有什么区别？](docs/questions/01-foundations/q003-white-noise-vs-random-walk.md)
- [Q005 ACF 和 PACF 有什么区别？](docs/questions/01-foundations/q005-acf-vs-pacf.md)
- [Q007 什么叫平稳？](docs/questions/01-foundations/q007-stationarity.md)
- [Q011 什么是 Unit Root？](docs/questions/02-stationarity/q011-unit-root.md)
- [Q012 ADF Test 在检验什么？](docs/questions/02-stationarity/q012-adf-test.md)
- [Q014 为什么做 Differencing？](docs/questions/02-stationarity/q014-differencing.md)
- [Q021 推导 AR(1) 的均值、方差和 ACF。](docs/questions/03-classical-models/q021-ar1-derivation.md)
- [Q025 解释 ARIMA(p,d,q)。](docs/questions/03-classical-models/q025-arima-pdq.md)
- [Q026 如何选择 p,d,q？](docs/questions/03-classical-models/q026-select-pdq.md)
- [Q027 SARIMA 是什么？](docs/questions/03-classical-models/q027-sarima.md)
- [Q028 ARIMAX / SARIMAX 中 X 是什么？](docs/questions/03-classical-models/q028-arimax-sarimax.md)
- [Q029 如何判断 ARIMA 拟合完成？](docs/questions/03-classical-models/q029-arima-residual-diagnostics.md)
- [Q031 ETS 是什么？](docs/questions/03-classical-models/q031-ets.md)
- [Q036 如何把时间序列转换成监督学习问题？](docs/questions/04-machine-learning/q036-time-series-to-supervised-learning.md)
- [Q037 Lag Features 怎么选择？](docs/questions/04-machine-learning/q037-lag-feature-selection.md)
- [Q038 Rolling Features 最大的 leakage trap 是什么？](docs/questions/04-machine-learning/q038-rolling-feature-leakage.md)
- [Q042 Recursive、Direct、MIMO 多步预测有什么区别？](docs/questions/04-machine-learning/q042-recursive-direct-mimo.md)
- [Q043 Random Forest 和 ARIMA 做趋势外推时有什么区别？](docs/questions/04-machine-learning/q043-random-forest-vs-arima-extrapolation.md)
- [Q045 Local Model 和 Global Model 有什么区别？](docs/questions/04-machine-learning/q045-local-vs-global-model.md)
- [Q050 为什么 Ensemble 经常有效？](docs/questions/04-machine-learning/q050-forecast-ensembles.md)
- [Q066 为什么不能 Random K-Fold？](docs/questions/06-evaluation-probabilistic/q066-why-not-random-kfold.md)
- [Q069 常见 Data Leakage 有哪些？](docs/questions/06-evaluation-probabilistic/q069-time-series-data-leakage.md)
- [Q070 RMSE 和 MAE 有什么区别？](docs/questions/06-evaluation-probabilistic/q070-rmse-vs-mae.md)
- [Q071 MAPE 有什么致命问题？](docs/questions/06-evaluation-probabilistic/q071-mape-problems.md)
- [Q073 为什么 MASE 很重要？](docs/questions/06-evaluation-probabilistic/q073-mase.md)
- [Q077 Prediction Interval 怎么评价？](docs/questions/06-evaluation-probabilistic/q077-prediction-interval-evaluation.md)
- [Q078 如果缺货成本比库存成本高 5 倍，该用什么 loss？](docs/questions/06-evaluation-probabilistic/q078-asymmetric-business-loss.md)
- [Q094 设计一个完整的销量预测系统。](docs/questions/09-system-design/q094-sales-forecasting-system-design.md)
- [Q096 如何 Debug 一个“离线 RMSE 极好，上线完全失效”的 forecasting pipeline？](docs/questions/09-system-design/q096-debug-offline-good-online-bad.md)

## 每题复习动作

1. 关掉答案，用 20 秒口述。
2. 写出核心公式或流程。
3. 说出至少一个 failure mode。
4. 说明如何做 rolling backtest。
5. 说明线上 feature availability。
6. 若是概率预测，说明 calibration 与 decision loss。
