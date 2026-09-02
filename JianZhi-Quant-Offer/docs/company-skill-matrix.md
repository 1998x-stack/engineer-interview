# 公司 / 岗位能力矩阵

> 本页是依据仓库中记录的**官方公开面试说明和岗位要求**做的能力映射，不是公司内部评分表，也不表示某一道题一定会被某家公司问到。原始依据见 [official-sources.md](../references/official-sources.md)。

## 1. 总体矩阵

| 公司 / 岗位类型 | 最高优先级 | 第二优先级 | 第三优先级 | 推荐题号 |
|---|---|---|---|---|
| Jane Street QR / Trading-Research | A 概率、条件期望、Problem Solving | J Coding | B/G 统计与研究可信度 | 001-020, 061-070, 091-100 |
| Two Sigma QR / Modeling | B/G Statistics & Open-ended Data Analysis | J Coding/Algorithms | D/E Time Series & ML | 011-020, 031-050, 061-070, 091-100 |
| Citadel QR | B/E Statistics & ML | J DSA/Coding | G Research methodology | 011-020, 041-050, 061-070, 091-100 |
| HRT Algorithm Developer | B/D/F 数据、统计、市场状态 | J C++/Python/Systems | G Research-to-production | 011-020, 031-040, 051-070, 091-100 |
| Optiver QR | A/B Probability & Statistics | D/E Forecasting & ML | H Optimization | 001-020, 031-050, 071-080 |
| IMC QR | B/D/E Statistics/ML | F Microstructure | G Backtest/Simulation/Production | 011-020, 031-070 |
| DRW ML Quant | E ML | D Noisy forecasting | J Production ML | 031-050, 091-100 |
| Options / Derivatives Quant | A/C/I Probability, SDE, Derivatives | H Risk/Optimization | J Numerical implementation | 001-010, 021-030, 071-100 |

## 2. 如何使用这个矩阵

### 不要按“公司题库”刷题

官方公开材料能支持的是**能力范围**，而不是未公开题目清单。更稳健的准备方式是：

1. 根据目标岗位选 3–5 个最高权重模块；
2. 每个模块先做到 Level 2（会解释）；
3. 再用目标公司的能力特点调整表达：
   - 更偏 problem solving：强调简洁推导；
   - 更偏 research：强调 hypothesis/OOS/robustness；
   - 更偏 HFT/system：强调 event state/latency/replay；
   - 更偏 derivatives：强调 no-arbitrage/replication/model risk。

## 3. 岗位类型而非公司名更重要

同一家公司不同团队的工作可能差异很大。因此准备优先级更应该由**岗位问题类型**决定：

| 岗位问题类型 | 核心模块 |
|---|---|
| General Quant Research | A + B + D + G + J |
| Financial ML | B + D + E + G + J |
| HFT / Microstructure Research | A + B + F + G + J |
| Systematic Portfolio Research | B + D + G + H + E |
| Derivatives / Vol Research | A + C + I + H + J |
| Low-latency Algorithm Developer | F + J + A/B |

## 4. 面试前一周如何定向

- 先从 [100 题总索引](100-question-index.md) 标记目标模块；
- 把每题 `30 秒版本` 练成无笔记口述；
- 对目标岗位最相关的 20–30 题，完整回答追问树；
- 至少做两次开放研究题和一次系统 debug mock；
- 不在最后一周继续无限扩充题库。
