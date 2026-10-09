---
id: Q007
title: "robots.txt 到底是什么？是不是访问授权文件？"
chapter: 1
difficulty: "★★☆☆☆"
source: "《爬虫与反爬虫面试100题_专业详解》"
---

# Q007 robots.txt 到底是什么？是不是访问授权文件？

> **难度：** ★★☆☆☆  
> **章节：** 第一章  HTTP、URL、Robots 与缓存  
> **定位：** 面试回答 + 原理理解 + 生产工程。

## 考察点

- RFC 9309
- 爬虫协商
- 认证/授权与 robots 的边界

## 60-90 秒推荐回答

robots.txt 是 Robots Exclusion Protocol，用于站点向自动化爬虫表达哪些 URI 应被访问或排除。它是协议层的爬虫协商机制，不是认证或授权系统。

专业 crawler 应在 host 首次进入 frontier 时获取并缓存 robots policy，把策略检查置于请求调度之前，同时记录策略版本、获取时间与失败行为。

## 原理深挖

robots.txt 与法律许可、合同条款、登录授权并不等价。企业采集系统应把 robots policy、业务授权、数据许可和站点条款拆成不同治理信号。

### 策略与授权分离

- robots 是 crawler 协议；登录、API key、合同许可、站点 ToS 是另外的边界。工程上应把这些状态作为独立 policy inputs。
- 对 robots fetch 失败应按规范和组织政策定义明确行为，不要“失败即无限制”。

### GitHub 增强版：进一步理解

1. 把 HTTP 看成“语义层”而不是某个客户端库的 API：方法、安全性、幂等性、缓存验证器、重定向语义与认证状态决定了 Retry、增量抓取和数据血缘的正确性。
2. 生产排障建议把一次 Fetch 拆成 DNS、Connect、TLS、TTFB、Download、Decode、Parse、Store 八段时间；只记录 total_latency 会让根因分析失去抓手。
3. 站点策略至少分四层保存：robots policy、业务授权、访问预算、数据许可。它们互相关联但不能互相替代。

## 高级面试扩展

### 1. 核心边界

协议层题目的高分答案必须先讲 **语义**，再讲客户端实现。状态码、缓存、Cookie、robots 都存在“协议语义”和“库默认行为”两层；面试中应主动区分它们，避免把某个 Python 库的默认动作说成 HTTP 标准本身。

针对 **robots.txt 到底是什么？是不是访问授权文件？**，面试时建议先明确讨论边界：RFC 9309、爬虫协商、认证/授权与 robots 的边界。如果不先定义这些边界，后面的“最佳实践”很容易变成只对某个库、某个站点或某个规模成立的经验。

### 2. 机制链路

`URL/Request → DNS/连接/TLS → HTTP 语义 → 重定向/缓存/状态 → Policy → Response`。任何优化都要回答两个问题：**是否改变语义正确性**，以及 **失败时是否可安全重试/回退**。

### 3. 本题进一步深挖

1. robots 是自动抓取协商协议而非授权机制。实现时要关注 robots fetch 的状态码处理、缓存 TTL、User-agent group 选择、路径匹配与 percent-encoding；站点授权、登录权限和数据使用条款属于另一层。

### 4. Trade-off 矩阵

| 决策维度 | 收益 | 代价 / 风险 |
|---|---|---|
| 正确性 | 严格遵循协议语义、状态隔离 | 实现复杂度更高 |
| 效率 | 连接复用、条件请求、缓存 | 需要维护 validator / session 状态 |
| 礼貌性 | 限速、退避、robots 协商 | 降低峰值吞吐但提高长期稳定性 |

面试中不要只说“方案 A 更好”。更专业的表达是：**在什么约束下 A 优于 B；规模、延迟、准确性或合规约束变化后，决策是否需要反转。**

### 5. 典型失败模式（FMEA）

| Failure Mode | 常见原因 | 检测 / 缓解 |
|---|---|---|
| 语义误判 | 把 302/307、safe/idempotent 混为一谈 | 记录 method/redirect chain，并做协议级测试 |
| 状态污染 | 跨账号共享 Cookie/Token | 按 identity 隔离 CookieJar/Session |
| 缓存陈旧 | 错误复用响应或 validator | 保存 ETag/Last-Modified、Age/Cache-Control 和抓取时间 |

### 6. 如何验证方案

用本地测试服务器覆盖 2xx/3xx/4xx/5xx、重定向链、条件请求、Cookie 隔离、超时与 Retry-After；不要只做 happy-path 单元测试。

建议至少覆盖三类验证：

- **Correctness**：协议/算法/业务语义是否正确；
- **Resilience**：超时、重试、进程崩溃、依赖变慢时是否可恢复；
- **Scale**：数据量或并发扩大 10 倍时，状态、内存、网络和远端预算哪个先成为瓶颈。

### 7. 高级候选人的回答结构

1. **先给定义/结论**：20 秒内回答题面，不绕圈。
2. **讲机制**：用状态机、数据流或关键公式解释为什么。
3. **讲 Trade-off**：至少指出一个“收益 ↔ 代价”。
4. **落到生产**：给出一个指标、一个失败模式、一个验证方式。
5. **主动给边界**：说明什么规模/场景下需要换方案。

### 8. 实战演练

> 给定一个站点出现重定向、缓存验证器和偶发 429，设计一次“可安全重试且不重复产生副作用”的抓取状态机。要求说明状态字段、超时、退避和日志。

完成后尝试用 **3 分钟口述 + 1 张架构/状态图 + 3 个指标** 复盘。如果只能写代码却说不清约束、失败模式和验证方法，通常还没有达到高级面试要求。

## 工程化落地

### 设计 / Review Checklist

- [ ] 明确请求语义与副作用
- [ ] 保存重定向/缓存验证器/状态上下文
- [ ] 定义 per-host budget 与失败行为
- [ ] 为网络各阶段做可观测性

### 建议监控的指标

- `dns/connect/tls/ttfb/download latency`
- `redirect rate`
- `304 hit rate`
- `429/503 rate`
- `bytes per response`
## 常见误区与 Gotchas

- 把“robots 允许”理解成“法律上当然允许”。
- 把“robots 不可达”默认解释成无限制访问。

补充检查：

- 不要把单机可运行等同于生产可扩展。
- 不要只描述“怎么做”，还要说明 **为什么、代价、失败时如何观测**。
- 涉及站点侧风控/挑战时，本仓库以防守与合规设计为边界，不提供规避访问控制或验证码的操作步骤。

## 面试追问拆解
### 追问 1：robots.txt 返回 5xx 时如何处理？

**参考回答：** robots 获取遇到 5xx 时不应简单当作“允许全部”。实现应遵循 RFC/所用 parser 的故障语义，并采用短 TTL 缓存避免每个 URL 都重复请求；同时明确 robots 与授权是两层概念。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

### 追问 2：为什么 robots parser 的缓存也要有 TTL？

**参考回答：** robots 内容会变化，永久缓存会造成旧规则长期生效；过短 TTL 又会增加站点负载。TTL 应结合 HTTP cache headers、抓取失败状态和站点规模，并记录 robots version/hash。

**面试展开：** 说明关键假设 → 给机制/数据结构或状态机 → 指出一个 trade-off → 补一个生产指标或失败模式。

标或失败模式。


## 面试官评分参考

| 层级 | 面试表现 |
|---|---|
| 基础 | 能准确回答题面，不混淆核心术语。 |
| 中级 | 能解释机制、边界与至少一个工程权衡，并能关联 RFC 9309。 |
| 高级 | 能给出生产化设计、指标/失败模式/容量意识，并说明方案在不同规模或约束下为何变化。 |

## 一句话记忆

> robots.txt 是 crawler 协商，不是权限系统。

## 延伸阅读

- [RFC 9110 - HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html)
- [RFC 9111 - HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111.html)
- [RFC 9309 - Robots Exclusion Protocol](https://www.rfc-editor.org/rfc/rfc9309.html)

---

> 来源说明：本页“推荐回答 / 深度解析 / 易错点 / 原始追问 / 一句话记忆”来自项目 PDF 内容基线；其余“工程化增强”是仓库版扩展。

← [Q006 Cookie、Session、Token 三者是什么关系？](Q006-Cookie、Session、Token-三者是什么关系.md) | [Q008 robots.txt 的 Allow 与 Disallow 冲突怎么办？](Q008-robots.txt-的-Allow-与-Disallow-冲突怎么办.md) →
