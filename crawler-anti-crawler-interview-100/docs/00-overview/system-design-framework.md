# 系统设计答题框架

## 1. 澄清目标

- 页面/域名规模？
- 一次性抓取还是持续 recrawl？
- Freshness SLO？
- 允许多少 Browser rendering？
- 是否需要保留 raw response？

## 2. 容量估算

```text
avg_qps = pages_per_day / 86400
peak_qps = avg_qps * peak_factor
raw_storage/day = pages/day * avg_response_bytes
```

再加入 retry ratio、compression ratio、browser fallback ratio、parse CPU ms/page。

## 3. 三平面

```text
Control Plane: config / policy / deploy / schema / budgets
State Plane: frontier / dedup / host state / lease / recrawl
Data Plane: fetch / render / parse / validate / store
```

## 4. 关键不变量

- 每个 host 的总访问预算不能因 worker 扩容而扩大。
- 任务可以重复，但结果写入必须幂等。
- Parser 失败不能静默变成合法空数据。
- Raw 与派生数据必须可追踪。

## 5. 最后讨论

失败模式、降级、成本、观测、合规与演进路线。
