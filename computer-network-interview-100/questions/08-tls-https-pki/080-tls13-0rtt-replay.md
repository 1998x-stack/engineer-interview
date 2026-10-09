---
id: 80
title: "TLS 1.3 0-RTT 为什么有 Replay Risk？哪些业务不适合？"
chapter: "第八章 HTTPS、TLS 1.3 与 PKI"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["0-RTT", "Replay", "Idempotency"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 080. TLS 1.3 0-RTT 为什么有 Replay Risk？哪些业务不适合？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：0-RTT / Replay / Idempotency  
> **本章**：[第八章 HTTPS、TLS 1.3 与 PKI](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **0-RTT / Replay / Idempotency** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 0-RTT early data 在完整新握手确认前即可发送，攻击者可能复制并重放这段合法密文到服务器。即使攻击者不知道明文，也可能让非幂等操作被执行多次，因此支付、下单、发券、状态变更等操作通常不应无保护地接受 0-RTT。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 服务端 anti-replay 机制在多机/多区域下实现并不简单。
2. 0-RTT 的目标是省一个 RTT，而不是提高带宽。
3. 应用可只允许安全/幂等请求进入 early data，或要求幂等键。

## 二次深化：工程上还必须知道什么

0-RTT 的风险不是“加密不安全”这一句，而是 early data 可被网络攻击者重放。真正的工程问题是：服务端如何限制可重放请求、做 anti-replay，以及应用语义是否幂等。

### 本章共同的工程视角

- TLS 的三个核心属性是机密性、完整性和对端认证；握手的目的不是“加密每个包”，而是安全建立会话密钥和身份。
- 证书验证与密钥协商是两条逻辑：证书证明“对方是谁/其公钥可信”，(EC)DHE 建立前向安全的共享密钥。
- 0-RTT 的性能收益来自提前发送 early data，但 replay 风险决定它只适合可安全重放的业务语义。

<!-- V2-ENRICHMENT-START -->
## V2 深入：0-RTT 的核心矛盾是“数据在服务端证明连接新鲜性之前就可能被处理”

### 第一性原理

- Client 使用此前 resumption PSK/ticket 加密 early data；攻击者可以捕获并在可行条件下重放相同 early data，Server 必须自行判断是否安全接受。
- TLS 不能自动知道“这条 HTTP 请求是否会扣款”，所以 application protocol/Server 必须限制 early data 到 replay-safe 操作或实现 anti-replay/idempotency。
- 0-RTT early data 的 security properties 弱于普通 1-RTT data，且不具备本次 handshake DHE 后才产生的同等 forward secrecy。

### GET 也不自动安全

HTTP GET 语义应 safe，但现实系统可能错误地让 GET 触发 side effect；是否允许 0-RTT 应基于实际业务 semantics，而不是只检查 method string。

### 多机房 anti-replay

严格全局 replay cache 需要跨 POP 同步，成本高且增加 latency；系统常结合 ticket lifetime、single-use token、request idempotency、局部 anti-replay window 等做 trade-off。

### 2026 规范提示

TLS 1.3 的现行参考应更新到 RFC 9846；QUIC 0-RTT 使用 TLS 1.3 early-data 机制，但还要遵守 QUIC transport parameter/connection semantics。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TLS 1.3 0-RTT 为什么有 Replay Risk？哪些业务不适合？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 0-RTT、Replay、Idempotency 说明关键状态、字段或数据路径。
3. **补 Why**：解释为什么协议/内核这样设计，以及少一步或改一种设计会出现什么正确性/性能问题。
4. **落到证据**：至少给出一个可观察信号或实验，例如 `openssl s_client`。

## 可观测性：如何证明自己的判断

| 层次 | 工具 / 信号 |
|---|---|
| 首选 | `openssl s_client` |
| 辅助 | `curl -vk` |
| 性能/路径 | `openssl x509 -text` |
| 深挖 | `Wireshark TLS` |

**关键原则**：先用低成本指标定位层次，再用抓包/trace/内核指标证明。不要看到一个 `Retransmission`、`TIME_WAIT` 或 `5xx` 就直接宣布根因。

## 面试官常见追问（PDF 原题 + 回答方向）

### 追问 1：为什么 GET 也不一定绝对 safe？

**参考回答**：epoll把interest set保存在内核，不需要每轮重新提交全部fd；ET强调边沿变化，必须drain到EAGAIN。EPOLLONESHOT常用于多线程下保证一个fd一次只被一个worker处理。poll在fd数量不大时足够简单可靠，kqueue与epoll都属于事件通知接口但具体语义不同。

### 追问 2：多数据中心如何共享 anti-replay 状态？

**参考回答**：恢复连接使用先前建立的 PSK/session ticket，可让 early data 在握手完成前发送；代价是可重放风险和较弱安全属性，因此只应承载可安全重放/幂等的应用操作。

### 追问 3：QUIC 0-RTT 与 TLS 0-RTT 是什么关系？

**参考回答**：恢复连接使用先前建立的 PSK/session ticket，可让 early data 在握手完成前发送；代价是可重放风险和较弱安全属性，因此只应承载可安全重放/幂等的应用操作。

## 高频易错点（PDF 原内容）

- ❌ 说 0-RTT “没有加密”。
- ❌ 只依赖 HTTP method 名称判断是否绝对安全。

## 动手验证 / 抓包实验（PDF 原内容）

列出你系统中的 API，分类哪些允许 early data，哪些必须等待 1-RTT，并说明幂等设计。

### 实验验收标准

能说明握手阶段、证书链或协商结果，并从工具输出定位对应证据。

建议把实验结果记录成：**命令/抓包过滤器 → 观察到的字段/状态 → 与理论的对应关系 → 仍不能证明的部分**。这比只保存一张截图更接近线上排障习惯。

## 面试评分 Rubric

| 等级 | 表现 |
|---|---|
| 1/5 | 只会名词或结论，无法解释字段/状态/时序。 |
| 2/5 | 能复述主流程，但遇到异常路径或 Why 追问容易断。 |
| 3/5 | 能解释核心机制，并回答至少两个追问。 |
| 4/5 | 能说明设计取舍、边界条件，并结合 Linux/抓包证据。 |
| 5/5 | 能从业务现象反推协议/内核机制，主动指出不确定性并设计验证实验。 |

## 权威资料 / 延伸阅读

- [RFC 9846 - TLS 1.3 (current specification, obsoletes RFC 8446)](https://www.rfc-editor.org/rfc/rfc9846.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [051. QUIC 为什么能减少首次/恢复连接延迟？0-RTT 的收益与风险是什么？](../05-udp-quic-http3/051-quic-handshake-0rtt.md)
- [075. TLS 1.3 Handshake 需要掌握到什么程度？](075-tls13-handshake.md)
- [078. 什么是 Forward Secrecy？为什么 ECDHE 很重要？](078-forward-secrecy-ecdhe.md)

## 复习卡片

- **一句话**：0-RTT early data 在完整新握手确认前即可发送，攻击者可能复制并重放这段合法密文到服务器。即使攻击者不知道明文，也可能让非幂等操作被执行多次，因此支付、下单、发券、状态变更等操作通常不应无保护地接受 0-RTT。
- **必须会解释**：0-RTT / Replay / Idempotency。
- **必须避免**：说 0-RTT “没有加密”。
- **必须会验证**：列出你系统中的 API，分类哪些允许 early data，哪些必须等待 1-RTT，并说明幂等设计。
