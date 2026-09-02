# 100 题总索引

## A. 概率论、条件概率与期望

建立不确定性推理的原子能力：样本空间、条件概率、期望、停止时间与依赖结构。

- [001. 两枚公平六面骰子的点数和为 10，概率是多少？](../questions/01-probability-expectation/q001-两枚公平六面骰子的点数和为-10-概率是多少.md) - ★☆☆ - 概率｜计数｜Jane Street 公开题型
- [002. 抛 3 枚公平硬币，已知至少一个反面，恰好两个正面的概率？](../questions/01-probability-expectation/q002-抛-3-枚公平硬币-已知至少一个反面-恰好两个正面的概率.md) - ★☆☆ - 条件概率｜样本空间｜Jane Street 公开题型
- [003. 连续抽两张牌：有放回与无放回的本质区别是什么？](../questions/01-probability-expectation/q003-连续抽两张牌-有放回与无放回的本质区别是什么.md) - ★☆☆ - 独立性｜条件概率｜抽样
- [004. 证明线性期望不要求随机变量独立。](../questions/01-probability-expectation/q004-证明线性期望不要求随机变量独立.md) - ★★☆ - 期望｜indicator trick｜证明
- [005. 一直抛公平硬币，直到第一次出现 HH，期望抛多少次？](../questions/01-probability-expectation/q005-一直抛公平硬币-直到第一次出现-HH-期望抛多少次.md) - ★★☆ - Stopping time｜状态递推｜模式重叠
- [006. Coupon Collector：集齐 n 种卡片平均需要抽多少次？](../questions/01-probability-expectation/q006-Coupon-Collector-集齐-n-种卡片平均需要抽多少次.md) - ★★☆ - 几何分布｜调和级数｜渐近
- [007. X 与 Y 不相关，是否意味着独立？](../questions/01-probability-expectation/q007-X-与-Y-不相关-是否意味着独立.md) - ★☆☆ - 相关性｜依赖｜反例
- [008. X,Y 独立且服从 U(0,1)，求 E[max(X,Y)]。](../questions/01-probability-expectation/q008-X-Y-独立且服从-U-0-1-求-E-max-X-Y.md) - ★★☆ - Order statistics｜CDF
- [009. 低基准率事件：阳性测试后真正为阳性的后验概率怎么算？](../questions/01-probability-expectation/q009-低基准率事件-阳性测试后真正为阳性的后验概率怎么算.md) - ★★☆ - Bayes｜base rate｜posterior
- [010. 如何构造相同边缘分布、但联合行为完全不同的随机变量？](../questions/01-probability-expectation/q010-如何构造相同边缘分布-但联合行为完全不同的随机变量.md) - ★★☆ - Joint distribution｜copula 直觉

## B. 数理统计与统计推断

把“看见效果”升级为“知道效果是否可信”：估计、显著性、稳健标准误与多重检验。

- [011. Bernoulli 参数 p 的 MLE 是什么？](../questions/02-statistical-inference/q011-Bernoulli-参数-p-的-MLE-是什么.md) - ★☆☆ - MLE｜Bernoulli｜一致性
- [012. 正态分布均值/方差的 MLE 是什么？为什么样本方差常除以 n-1？](../questions/02-statistical-inference/q012-正态分布均值-方差的-MLE-是什么-为什么样本方差常除以-n-1.md) - ★★☆ - MLE｜无偏性｜自由度
- [013. Bias-Variance Tradeoff 如何从预测误差分解理解？](../questions/02-statistical-inference/q013-Bias-Variance-Tradeoff-如何从预测误差分解理解.md) - ★★☆ - 泛化｜正则化｜噪声
- [014. p-value 到底表示什么？](../questions/02-statistical-inference/q014-p-value-到底表示什么.md) - ★☆☆ - 假设检验｜p-value｜解释
- [015. 测试 10,000 个特征，总会出现显著结果，怎么处理？](../questions/02-statistical-inference/q015-测试-10-000-个特征-总会出现显著结果-怎么处理.md) - ★★☆ - Multiple testing｜FDR｜研究过拟合
- [016. 为什么普通 OLS t-stat 在金融时间序列里常失真？](../questions/02-statistical-inference/q016-为什么普通-OLS-t-stat-在金融时间序列里常失真.md) - ★★☆ - OLS｜HAC｜序列相关
- [017. Ridge 与 Lasso 的本质区别？](../questions/02-statistical-inference/q017-Ridge-与-Lasso-的本质区别.md) - ★★☆ - Regularization｜高维特征｜共线性
- [018. Bootstrap 为什么不能直接 IID resample 金融时间序列？](../questions/02-statistical-inference/q018-Bootstrap-为什么不能直接-IID-resample-金融时间序列.md) - ★★☆ - Bootstrap｜依赖｜block resampling
- [019. Mean、Median、Trimmed Mean 在异常值下如何权衡？](../questions/02-statistical-inference/q019-Mean-Median-Trimmed-Mean-在异常值下如何权衡.md) - ★☆☆ - Robust statistics｜异常值
- [020. 95% Confidence Interval 的正确频率学解释是什么？](../questions/02-statistical-inference/q020-95%-Confidence-Interval-的正确频率学解释是什么.md) - ★★☆ - 置信区间｜coverage｜calibration

## C. 随机过程

掌握连续时间与隐状态建模语言：Brownian motion、martingale、OU、Poisson、Markov/HMM/Kalman。

- [021. Brownian Motion 的核心性质是什么？](../questions/03-stochastic-processes/q021-Brownian-Motion-的核心性质是什么.md) - ★★☆ - 随机过程｜Brownian Motion
- [022. 为什么 Brownian Motion 几乎处处不可微？](../questions/03-stochastic-processes/q022-为什么-Brownian-Motion-几乎处处不可微.md) - ★★★ - 尺度分析｜quadratic variation｜Itô 直觉
- [023. 什么是 Martingale？](../questions/03-stochastic-processes/q023-什么是-Martingale.md) - ★★☆ - 条件期望｜公平游戏｜过滤
- [024. Optional Stopping Theorem 为什么不能随便套？](../questions/03-stochastic-processes/q024-Optional-Stopping-Theorem-为什么不能随便套.md) - ★★★ - Stopping time｜martingale｜条件
- [025. 几何布朗运动为什么保持价格为正？](../questions/03-stochastic-processes/q025-几何布朗运动为什么保持价格为正.md) - ★★☆ - SDE｜GBM｜Itô
- [026. Ornstein-Uhlenbeck Process 的长期均值是什么？](../questions/03-stochastic-processes/q026-Ornstein-Uhlenbeck-Process-的长期均值是什么.md) - ★★☆ - Mean reversion｜OU｜SDE
- [027. Poisson Process 的 inter-arrival time 为什么是指数分布？](../questions/03-stochastic-processes/q027-Poisson-Process-的-inter-arrival-time-为什么是指数分布.md) - ★★☆ - Poisson｜Exponential｜memoryless
- [028. 给定 Markov transition matrix，如何求 stationary distribution？](../questions/03-stochastic-processes/q028-给定-Markov-transition-matrix-如何求-stationary-distribution.md) - ★★☆ - Markov chain｜stationary｜ergodicity
- [029. Kalman Filter 的本质是什么？](../questions/03-stochastic-processes/q029-Kalman-Filter-的本质是什么.md) - ★★★ - State space｜Bayesian filtering｜线性高斯
- [030. HMM 与普通 Markov Chain 的区别？](../questions/03-stochastic-processes/q030-HMM-与普通-Markov-Chain-的区别.md) - ★★☆ - HMM｜latent state｜EM

## D. 时间序列与计量

处理量化数据最根本的时间依赖、非平稳、波动聚类与异步采样。

- [031. 什么叫弱平稳（weak stationarity）？](../questions/04-time-series-econometrics/q031-什么叫弱平稳-weak-stationarity.md) - ★☆☆ - 时间序列｜stationarity
- [032. AR(1) 什么时候平稳？长期方差和 ACF 是什么？](../questions/04-time-series-econometrics/q032-AR-1-什么时候平稳-长期方差和-ACF-是什么.md) - ★★☆ - AR(1)｜ACF｜稳定性
- [033. Random Walk 为什么 non-stationary？](../questions/04-time-series-econometrics/q033-Random-Walk-为什么-non-stationary.md) - ★☆☆ - Unit root｜随机游走
- [034. 什么是 Unit Root？ADF test 在检验什么？](../questions/04-time-series-econometrics/q034-什么是-Unit-Root-ADF-test-在检验什么.md) - ★★☆ - ADF｜unit root｜检验方向
- [035. 为什么两个独立 Random Walk 回归会产生 Spurious Regression？](../questions/04-time-series-econometrics/q035-为什么两个独立-Random-Walk-回归会产生-Spurious-Regression.md) - ★★☆ - 伪回归｜非平稳｜t-stat
- [036. 什么是 Cointegration？](../questions/04-time-series-econometrics/q036-什么是-Cointegration.md) - ★★★ - Cointegration｜ECM｜长期关系
- [037. Granger Causality 是真正的因果吗？](../questions/04-time-series-econometrics/q037-Granger-Causality-是真正的因果吗.md) - ★★☆ - 预测因果｜时序｜混杂
- [038. 为什么收益自相关低，但平方收益自相关高？](../questions/04-time-series-econometrics/q038-为什么收益自相关低-但平方收益自相关高.md) - ★★☆ - Volatility clustering｜GARCH
- [039. 为什么金融时间序列不能随机 train/test split？](../questions/04-time-series-econometrics/q039-为什么金融时间序列不能随机-train-test-split.md) - ★☆☆ - 时间泄漏｜walk-forward｜validation
- [040. Tick data 中两个资产的相关性如何估计？直接时间戳对齐有什么问题？](../questions/04-time-series-econometrics/q040-Tick-data-中两个资产的相关性如何估计-直接时间戳对齐有什么问题.md) - ★★★ - 异步数据｜Epps effect｜sampling

## E. 机器学习与 Financial ML

围绕低信噪比、漂移和 research-to-production，理解模型选择、校准与线上诊断。

- [041. 训练准确率 99%，测试 52%，你首先检查什么？](../questions/05-financial-ml/q041-训练准确率-99%-测试-52%-你首先检查什么.md) - ★★☆ - Debugging｜leakage｜overfit
- [042. 为什么线性模型在金融预测中仍然重要？](../questions/05-financial-ml/q042-为什么线性模型在金融预测中仍然重要.md) - ★★☆ - Linear model｜inductive bias｜鲁棒性
- [043. Random Forest 与 Gradient Boosting 的根本区别？](../questions/05-financial-ml/q043-Random-Forest-与-Gradient-Boosting-的根本区别.md) - ★★☆ - Tree ensemble｜bagging｜boosting
- [044. Feature scaling 为什么会造成未来信息泄漏？](../questions/05-financial-ml/q044-Feature-scaling-为什么会造成未来信息泄漏.md) - ★☆☆ - Preprocessing｜pipeline｜leakage
- [045. 一个 feature 的 IC 很低，是否一定没有价值？](../questions/05-financial-ml/q045-一个-feature-的-IC-很低-是否一定没有价值.md) - ★★☆ - Signal evaluation｜interaction｜nonlinearity
- [046. 如何判断分类概率是否 calibrated？](../questions/05-financial-ml/q046-如何判断分类概率是否-calibrated.md) - ★★☆ - Calibration｜Brier｜reliability
- [047. Finance 中为什么 accuracy 往往不是好指标？](../questions/05-financial-ml/q047-Finance-中为什么-accuracy-往往不是好指标.md) - ★☆☆ - Imbalanced data｜metric｜utility
- [048. 什么时候 Transformer 可能优于传统时间序列模型？](../questions/05-financial-ml/q048-什么时候-Transformer-可能优于传统时间序列模型.md) - ★★★ - Transformer｜长序列｜多变量
- [049. 什么是 Concept Drift？](../questions/05-financial-ml/q049-什么是-Concept-Drift.md) - ★★☆ - Distribution shift｜drift｜monitoring
- [050. 模型 offline 很好，上线立即下降，如何系统排查？](../questions/05-financial-ml/q050-模型-offline-很好-上线立即下降-如何系统排查.md) - ★★★ - Research-to-production｜debug｜MLOps

## F. 市场微观结构

理解盘口、成交、队列、adverse selection、execution 与 latency 对研究结果的约束。

- [051. Bid、Ask、Mid、Spread 分别是什么？为什么 last price 可能不如 mid？](../questions/06-market-microstructure/q051-Bid-Ask-Mid-Spread-分别是什么-为什么-last-price-可能不如-mid.md) - ★☆☆ - Microstructure｜quote｜price
- [052. 什么是 Bid-Ask Bounce？](../questions/06-market-microstructure/q052-什么是-Bid-Ask-Bounce.md) - ★★☆ - Microstructure noise｜短期自相关
- [053. 什么是 Adverse Selection？](../questions/06-market-microstructure/q053-什么是-Adverse-Selection.md) - ★★☆ - Conditional probability｜information｜microstructure
- [054. Order Book Imbalance 如何定义？为什么不能把它当永恒预测信号？](../questions/06-market-microstructure/q054-Order-Book-Imbalance-如何定义-为什么不能把它当永恒预测信号.md) - ★★☆ - LOB｜imbalance｜state feature
- [055. Price-Time Priority 是什么？](../questions/06-market-microstructure/q055-Price-Time-Priority-是什么.md) - ★☆☆ - Matching engine｜queue｜priority
- [056. 为什么 Fill Probability 是 execution simulation 的关键？](../questions/06-market-microstructure/q056-为什么-Fill-Probability-是-execution-simulation-的关键.md) - ★★☆ - Execution model｜queue｜simulation bias
- [057. Market Impact 的 temporary 与 permanent 如何理解？](../questions/06-market-microstructure/q057-Market-Impact-的-temporary-与-permanent-如何理解.md) - ★★☆ - Impact｜execution cost｜information
- [058. Tick Size 为什么会改变市场行为？](../questions/06-market-microstructure/q058-Tick-Size-为什么会改变市场行为.md) - ★★☆ - Tick size｜queue competition｜liquidity
- [059. 什么是 Microprice？为什么可能不同于 Mid？](../questions/06-market-microstructure/q059-什么是-Microprice-为什么可能不同于-Mid.md) - ★★☆ - Microprice｜imbalance｜short-horizon state
- [060. Latency 为什么既是系统问题，也是统计问题？](../questions/06-market-microstructure/q060-Latency-为什么既是系统问题-也是统计问题.md) - ★★☆ - Latency｜signal decay｜distribution

## G. 数据、回测与研究方法论

最重要的一章：时间戳、PIT、survivorship、cost model、walk-forward、研究过拟合与可复现。

- [061. 什么是 Look-Ahead Bias？](../questions/07-backtesting-research-methodology/q061-什么是-Look-Ahead-Bias.md) - ★☆☆ - Backtest｜leakage｜timestamp
- [062. 什么是 Survivorship Bias？](../questions/07-backtesting-research-methodology/q062-什么是-Survivorship-Bias.md) - ★☆☆ - Universe｜delisting｜历史数据
- [063. Corporate Actions 为什么会把回测搞坏？](../questions/07-backtesting-research-methodology/q063-Corporate-Actions-为什么会把回测搞坏.md) - ★★☆ - Adjusted data｜split｜dividend
- [064. Point-in-Time Data 是什么？](../questions/07-backtesting-research-methodology/q064-Point-in-Time-Data-是什么.md) - ★★☆ - PIT｜revision｜data lineage
- [065. 为什么 transaction cost 不能简单固定减 1bp？](../questions/07-backtesting-research-methodology/q065-为什么-transaction-cost-不能简单固定减-1bp.md) - ★★☆ - Cost model｜spread｜impact
- [066. 一个 backtest Sharpe=3，你信吗？第一步做什么？](../questions/07-backtesting-research-methodology/q066-一个-backtest-Sharpe=3-你信吗-第一步做什么.md) - ★★★ - Research skepticism｜audit｜Sharpe
- [067. Walk-Forward Validation 怎么做？](../questions/07-backtesting-research-methodology/q067-Walk-Forward-Validation-怎么做.md) - ★★☆ - OOS｜rolling｜expanding
- [068. Alternative Data 有大量 missing values，怎么处理？](../questions/07-backtesting-research-methodology/q068-Alternative-Data-有大量-missing-values-怎么处理.md) - ★★☆ - Missingness｜MNAR｜数据质量
- [069. 如何判断 improvement 是真 signal 还是 research overfitting？](../questions/07-backtesting-research-methodology/q069-如何判断-improvement-是真-signal-还是-research-overfitting.md) - ★★★ - OOS｜ablation｜robustness
- [070. 一个可复现 Quant Research Experiment 应保存什么？](../questions/07-backtesting-research-methodology/q070-一个可复现-Quant-Research-Experiment-应保存什么.md) - ★★☆ - Reproducibility｜lineage｜MLOps

## H. 组合、风险与优化

从 covariance estimation 到稳定化优化：risk decomposition、shrinkage、constraints 与 turnover。

- [071. 推导 Minimum-Variance Portfolio。](../questions/08-portfolio-risk-optimization/q071-推导-Minimum-Variance-Portfolio.md) - ★★★ - Portfolio optimization｜Lagrange
- [072. 为什么直接使用 sample covariance matrix 很危险？](../questions/08-portfolio-risk-optimization/q072-为什么直接使用-sample-covariance-matrix-很危险.md) - ★★☆ - Covariance｜high-dimensional｜conditioning
- [073. 什么是 Covariance Shrinkage？](../questions/08-portfolio-risk-optimization/q073-什么是-Covariance-Shrinkage.md) - ★★☆ - Shrinkage｜bias-variance｜risk model
- [074. PCA 在风险模型里是什么意思？](../questions/08-portfolio-risk-optimization/q074-PCA-在风险模型里是什么意思.md) - ★★☆ - PCA｜eigenportfolio｜factor
- [075. VaR 与 Expected Shortfall 有什么区别？](../questions/08-portfolio-risk-optimization/q075-VaR-与-Expected-Shortfall-有什么区别.md) - ★★☆ - Tail risk｜VaR｜ES
- [076. 为什么 Volatility Targeting 不等于风险恒定？](../questions/08-portfolio-risk-optimization/q076-为什么-Volatility-Targeting-不等于风险恒定.md) - ★★☆ - Vol targeting｜estimation lag｜risk
- [077. 什么是 Marginal Contribution to Risk？](../questions/08-portfolio-risk-optimization/q077-什么是-Marginal-Contribution-to-Risk.md) - ★★☆ - Risk decomposition｜gradient
- [078. 为什么 Portfolio Optimization 容易产生极端权重？](../questions/08-portfolio-risk-optimization/q078-为什么-Portfolio-Optimization-容易产生极端权重.md) - ★★☆ - Estimation error｜inverse problem｜constraints
- [079. 如何把 turnover/transaction-cost penalty 放入优化？](../questions/08-portfolio-risk-optimization/q079-如何把-turnover-transaction-cost-penalty-放入优化.md) - ★★☆ - Convex optimization｜turnover｜regularization
- [080. Factor Neutralization 怎么理解？](../questions/08-portfolio-risk-optimization/q080-Factor-Neutralization-怎么理解.md) - ★★☆ - Residualization｜exposure｜confounding

## I. 衍生品与定价

面向 options/derivatives quant 的无套利、Black-Scholes、Greeks、IV 与离散对冲基础。

- [081. Put-Call Parity 是什么？如何从无套利推导？](../questions/09-derivatives-pricing/q081-Put-Call-Parity-是什么-如何从无套利推导.md) - ★★☆ - Options｜no-arbitrage｜parity
- [082. Black-Scholes 的核心假设是什么？哪些明显不现实？](../questions/09-derivatives-pricing/q082-Black-Scholes-的核心假设是什么-哪些明显不现实.md) - ★★☆ - Black-Scholes｜assumptions｜model risk
- [083. 为什么 Black-Scholes PDE 中真实 drift μ 消失？](../questions/09-derivatives-pricing/q083-为什么-Black-Scholes-PDE-中真实-drift-μ-消失.md) - ★★★ - Risk-neutral pricing｜delta hedge｜PDE
- [084. Delta 是什么？它是不是“期权上涨概率”？](../questions/09-derivatives-pricing/q084-Delta-是什么-它是不是“期权上涨概率”.md) - ★★☆ - Greeks｜Delta｜sensitivity
- [085. Gamma 为什么重要？](../questions/09-derivatives-pricing/q085-Gamma-为什么重要.md) - ★★☆ - Greeks｜convexity｜hedging error
- [086. Vega 是什么？为什么 vanilla option 通常 Vega>0？](../questions/09-derivatives-pricing/q086-Vega-是什么-为什么-vanilla-option-通常-Vega-0.md) - ★★☆ - Greeks｜volatility｜convexity
- [087. Implied Volatility 如何从期权价格反求？](../questions/09-derivatives-pricing/q087-Implied-Volatility-如何从期权价格反求.md) - ★★☆ - Numerical methods｜IV｜root finding
- [088. 为什么存在 Volatility Smile/Skew？](../questions/09-derivatives-pricing/q088-为什么存在-Volatility-Smile-Skew.md) - ★★☆ - Vol surface｜fat tails｜model misspecification
- [089. American 与 European Option 最大区别是什么？](../questions/09-derivatives-pricing/q089-American-与-European-Option-最大区别是什么.md) - ★★☆ - Early exercise｜optimal stopping
- [090. 为什么离散 Delta Hedging 不能完全复制连续理论？](../questions/09-derivatives-pricing/q090-为什么离散-Delta-Hedging-不能完全复制连续理论.md) - ★★★ - Discrete hedging｜model risk｜P&L

## J. Coding、算法与量化系统

将研究落到可扩展代码：streaming、top-k、order book、as-of join、cache locality 与 parity debugging。

- [091. 长度 N 的序列，如何 O(N) 计算 rolling mean？](../questions/10-coding-quant-systems/q091-长度-N-的序列-如何-O-N-计算-rolling-mean.md) - ★☆☆ - Sliding window｜算法｜streaming
- [092. Streaming 数据中实时维护 median 怎么做？](../questions/10-coding-quant-systems/q092-Streaming-数据中实时维护-median-怎么做.md) - ★★☆ - Heap｜streaming median｜DSA
- [093. 十亿行数据只找最大的 1000 个元素，如何做？](../questions/10-coding-quant-systems/q093-十亿行数据只找最大的-1000-个元素-如何做.md) - ★☆☆ - Top-K｜heap｜large data
- [094. 如何实现 event-driven order-book reconstruction？](../questions/10-coding-quant-systems/q094-如何实现-event-driven-order-book-reconstruction.md) - ★★★ - State machine｜hash map｜ordered map
- [095. 给无序 trade events，如何检测 timestamp 问题？](../questions/10-coding-quant-systems/q095-给无序-trade-events-如何检测-timestamp-问题.md) - ★★☆ - Timestamp｜clock｜data QA
- [096. SQL 中如何做 As-Of Join？](../questions/10-coding-quant-systems/q096-SQL-中如何做-As-Of-Join.md) - ★★☆ - SQL｜time series join｜point-in-time
- [097. 为什么 NumPy 通常比 Python for-loop 快？](../questions/10-coding-quant-systems/q097-为什么-NumPy-通常比-Python-for-loop-快.md) - ★★☆ - Vectorization｜memory｜Python runtime
- [098. C++ Quant/HFT 面试为什么常问 cache locality？](../questions/10-coding-quant-systems/q098-C++-Quant-HFT-面试为什么常问-cache-locality.md) - ★★☆ - CPU cache｜data layout｜latency
- [099. Research code 与 production code 最大区别是什么？](../questions/10-coding-quant-systems/q099-Research-code-与-production-code-最大区别是什么.md) - ★★☆ - Software engineering｜research-to-prod
- [100. 压轴：Backtest 与 Live 表现差异巨大，如何系统定位？](../questions/10-coding-quant-systems/q100-压轴-Backtest-与-Live-表现差异巨大-如何系统定位.md) - ★★★ - 系统诊断｜research parity｜distribution shift
