# 附录 A：7 天冲刺复习路线

| 天 | 主题 | 完成标准 |
|---|---|---|
| Day 1 | HTTP + URL + Robots + Cache | 能白板解释请求链路、304、幂等、robots。 |
| Day 2 | DOM + 抽取 + 数据质量 | 能设计稳定 selector、正文抽取与 schema validation。 |
| Day 3 | Scrapy + Async | 能画架构、解释 event loop、并发与 backpressure。 |
| Day 4 | JS + Browser | 能判断何时需要浏览器、设计 Browser Pool。 |
| Day 5 | 分布式 + 去重 + 存储 | 能设计 Frontier、Bloom、lease、raw/curated/serving。 |
| Day 6 | 反爬防护 | 能设计 rate limit、risk score、WAF/Bot Management。 |
| Day 7 | 系统设计 10 题 | 每题 15 分钟：估算→架构→状态→故障→SLO。 |

# 附录 B：高级面试回答模板

1. 先给结论：一句话说明你会怎么做。
1. 给原理：解释为什么这样做，指出关键协议/算法/系统约束。
1. 给工程实现：数据结构、组件、状态、指标和失败处理。
1. 给 Trade-off：成本、精度、延迟、误报、覆盖率之间如何权衡。
1. 主动指出边界：什么情况下该方案失效，如何演进。
> 系统设计题黄金顺序<br>• 1. 明确目标与约束：规模、freshness、站点预算、数据准确性。<br>• 2. 做量级估算：pages/s、带宽、存储、状态规模、浏览器比例。<br>• 3. 画数据流：Seed → Frontier → Fetch → Raw → Parse → Validate → Store。<br>• 4. 补控制平面：robots、per-host budget、priority、retry/circuit breaker。<br>• 5. 补状态平面：dedup、history、ETag、last_fetch、leases。<br>• 6. 最后讲 SLO、监控、故障恢复和成本。

# 附录 C：核心公式与速查

```text
Average throughput = pages_per_day / 86400
Bloom FPR: p = (1 - exp(-k*n/m))^k
Bloom optimal k ≈ (m/n) * ln(2)
Jaccard(A,B) = |A ∩ B| / |A ∪ B|
Retry delay_n = min(max_delay, base * 2^n) + jitter
Token Bucket: average rate <= r, burst <= B
Crawler objective: maximize Σ Value(u) * Freshness(u)
Constraint: RequestRate(host_i) <= Budget_i
```

# 参考资料

RFC 9309 - Robots Exclusion Protocol: https://www.rfc-editor.org/rfc/rfc9309.html

RFC 9110 - HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110.html

RFC 9111 - HTTP Caching: https://www.rfc-editor.org/rfc/rfc9111.html

Scrapy Architecture: https://docs.scrapy.org/en/latest/topics/architecture.html

Scrapy Downloader Middleware: https://docs.scrapy.org/en/latest/topics/downloader-middleware.html

Scrapy AutoThrottle: https://docs.scrapy.org/en/latest/topics/autothrottle.html

Playwright BrowserContext: https://playwright.dev/docs/api/class-browsercontext

Playwright Network: https://playwright.dev/docs/network

Selenium WebDriver: https://www.selenium.dev/documentation/webdriver/

Selenium Waits: https://www.selenium.dev/documentation/webdriver/waits/

Chrome DevTools Protocol: https://chromedevtools.github.io/devtools-protocol/

Cloudflare Bot Score Concepts: https://developers.cloudflare.com/bots/concepts/bot-score/

Cloudflare Challenges: https://developers.cloudflare.com/cloudflare-challenges/

注：本文引用资料主要用于协议、框架和防护概念的技术校准。具体产品版本、网站条款和法律要求可能变化，实际工程应以目标系统当前文档与授权为准。

