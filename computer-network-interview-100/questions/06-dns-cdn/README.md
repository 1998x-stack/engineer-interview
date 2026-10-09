# 第六章 DNS、全局调度与 CDN

掌握域名解析、缓存、一致性与边缘加速。

## 本章能力目标

- DNS 是分布式缓存系统：任何“为什么不立即生效”的答案都要把 TTL、递归 Resolver 和权威服务器分层。
- 客户端看到的 DNS 路径经常是“应用 → stub resolver → recursive resolver”，不是客户端逐级直接问 Root/TLD。
- CDN 加速由调度、连接复用、边缘缓存、回源链路、压缩和协议栈共同决定，不能只看 cache hit ratio。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **DNS 是缓存化的委派数据库**：Recursive/Iterative、Referral、TTL/negative cache、CNAME 链必须连成一条解析路径。
- **DNSSEC 与加密 DNS 分工不同**：前者验证 data，DoH/DoT 保护 Client↔Resolver transport。
- **CDN 是全局调度 + 边缘连接 + 缓存体系**：hit ratio 只是结果指标，不代表所有性能收益。

### 本章白板题

1. 画 stub→recursive→root→TLD→authoritative 完整链，并插入 cache/CNAME。
2. 解释为什么 DNS 改记录不能保证 TTL 秒后所有流量立即切换。
3. 设计 CDN cache key，列出 Cookie/Query/Vary 造成的缓存碎片化与泄漏风险。

### 最小实验组合

`dig +trace`、`dig +tcp`、指定 resolver/authoritative 查询、`curl -I` 查看 Age/Via/Cache-Status（若提供）。要求能区分 DNS cache、连接复用和 CDN object cache。
<!-- CHAPTER-V2-END -->

## 题目目录

- [053. 输入域名后，DNS 完整解析链路是什么？](053-dns-resolution-path.md) · 基础 · ★★★★★
- [054. DNS 递归查询与迭代查询有什么区别？](054-dns-recursive-vs-iterative.md) · 基础 · ★★★★☆
- [055. 为什么“DNS 使用 UDP”是错误或不完整答案？](055-dns-udp-and-tcp.md) · 基础 · ★★★★★
- [056. A、AAAA、CNAME、MX、NS、TXT 分别表达什么？](056-dns-record-types.md) · 基础 · ★★★★☆
- [057. DNS TTL 与 Negative Caching 是什么？](057-dns-ttl-negative-cache.md) · 进阶 · ★★★★☆
- [058. DNS 如何做负载均衡？它的局限是什么？](058-dns-load-balancing.md) · 进阶 · ★★★★☆
- [059. DNS Cache Poisoning 是什么？DNSSEC、DoH/DoT 分别保护什么？](059-dns-cache-poisoning-dnssec-doh-dot.md) · 进阶 · ★★★★☆
- [060. CDN 为什么能加速？缓存命中率为什么只是其中一部分？](060-cdn-acceleration.md) · 进阶 · ★★★★★

## 推荐实践工具

- `dig`
- `dig +trace`
- `resolvectl statistics`
- `curl -w`

[← 返回全书目录](../../README.md)
