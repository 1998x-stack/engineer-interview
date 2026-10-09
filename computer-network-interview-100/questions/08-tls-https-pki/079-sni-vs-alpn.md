---
id: 79
title: "SNI 与 ALPN 分别解决什么问题？"
chapter: "第八章 HTTPS、TLS 1.3 与 PKI"
difficulty: "进阶"
frequency: "★★★★☆"
tags: ["TLS Extension", "Virtual Hosting"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 079. SNI 与 ALPN 分别解决什么问题？

> **定位**：进阶 · **面试频率**：★★★★☆ · **标签**：TLS Extension / Virtual Hosting  
> **本章**：[第八章 HTTPS、TLS 1.3 与 PKI](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **TLS Extension / Virtual Hosting** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> SNI 在 TLS 握手早期告诉服务器客户端想访问哪个域名，使一个 IP 上可选择正确证书/虚拟主机；ALPN 让双方协商 TLS 上层应用协议，例如 `h2` 或 `http/1.1`。一个解决“哪个主机”，一个解决“说哪种协议”。

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. 传统 SNI 通常可被路径观察者看到，ECH 旨在加密 ClientHello 中的敏感部分。
2. ALPN 是 HTTP/2 over TLS 部署的关键协商机制。
3. 同一证书可覆盖多个 SAN，所以 SNI 与证书并非一对一。

## 二次深化：工程上还必须知道什么

本题的高级回答应主动说明适用范围和观测边界：协议规范描述的是语义与状态机，真实 Linux/云网络实现还会受到内核版本、offload、中间盒、代理和应用框架的影响。面试中若无法确定实现细节，应明确“规范保证”和“常见实现”分别是什么。

### 本章共同的工程视角

- TLS 的三个核心属性是机密性、完整性和对端认证；握手的目的不是“加密每个包”，而是安全建立会话密钥和身份。
- 证书验证与密钥协商是两条逻辑：证书证明“对方是谁/其公钥可信”，(EC)DHE 建立前向安全的共享密钥。
- 0-RTT 的性能收益来自提前发送 early data，但 replay 风险决定它只适合可安全重放的业务语义。

<!-- V2-ENRICHMENT-START -->
## V2 深入：SNI 选择“你要哪个虚拟服务”，ALPN 选择“这个 TLS 连接上跑哪个应用协议”

### 第一性原理

- SNI 是 ClientHello extension，告诉 shared IP 上的 TLS endpoint 目标 server name，以便选择正确 certificate/virtual host。
- ALPN 在 TLS handshake 中协商应用协议，如 `h2`、`http/1.1`，避免握手后再猜协议。
- 一个是 host identity/routing hint，一个是 application protocol negotiation，不能混为一谈。

### 没有 SNI

共享 IP 仍可配置 default certificate/site，或不同 IP 分配不同域名；但大规模 virtual hosting 会很受限。证书 SAN 多域名也不能完全替代正确 SNI routing。

### ECH 与可见性

ECH 目标是保护 ClientHello 中包括真实 SNI 在内的敏感信息，但 destination IP 仍需路由；DNS/流量特征也可能泄露信息。因此 ECH 不是“隐藏访问目标的一切”。

### 线上案例推演

TLS handshake 成功却协商成 `http/1.1` 而非 `h2`，应查 ALPN/client/server/proxy support；证书选错域名则优先查 SNI/vhost，而不是把两种错误混在一起。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“SNI 与 ALPN 分别解决什么问题？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 TLS Extension、Virtual Hosting 说明关键状态、字段或数据路径。
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

### 追问 1：没有 SNI 时共享 IP HTTPS 如何工作？

**参考回答**：TLS通常隐藏HTTP路径和内容，但目标IP仍可见，传统SNI也可能泄露主机名；ECH旨在加密ClientHello中的敏感信息。企业代理若把自有根CA安装到客户端信任库，可做受控TLS中间代理。 SNI告诉服务器客户端要访问的主机名，便于同IP多证书虚拟主机；ALPN协商应用协议（如 h2、http/1.1）。它们解决的问题不同，ALPN失败通常会回退或终止，取决于双方可接受协议集合。

### 追问 2：ALPN 协商失败会怎样？

**参考回答**：SNI告诉服务器客户端要访问的主机名，便于同IP多证书虚拟主机；ALPN协商应用协议（如 h2、http/1.1）。它们解决的问题不同，ALPN失败通常会回退或终止，取决于双方可接受协议集合。

### 追问 3：ECH 是否隐藏目标 IP？

**参考回答**：TLS通常隐藏HTTP路径和内容，但目标IP仍可见，传统SNI也可能泄露主机名；ECH旨在加密ClientHello中的敏感信息。企业代理若把自有根CA安装到客户端信任库，可做受控TLS中间代理。

## 高频易错点（PDF 原内容）

- ❌ 把 SNI 当作 DNS。
- ❌ 把 ALPN 说成 TLS cipher negotiation。

## 动手验证 / 抓包实验（PDF 原内容）

用 `openssl s_client -servername` 对同一 CDN IP 测不同域名；查看 ALPN negotiated protocol。

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
- [RFC 6066 - TLS Extensions (includes SNI)](https://www.rfc-editor.org/rfc/rfc6066.html)
- [RFC 7301 - Application-Layer Protocol Negotiation (ALPN)](https://www.rfc-editor.org/rfc/rfc7301.html)

> 资料使用建议：不要把 RFC 当教科书顺读。先带着本题中的具体问题定位相关章节，再回到抓包或最小实验验证。

## 关联题目

- [075. TLS 1.3 Handshake 需要掌握到什么程度？](075-tls13-handshake.md)
- [076. 浏览器如何验证 HTTPS 证书？证书链、主机名、有效期各自是什么作用？](076-certificate-validation.md)
- [091. 浏览器输入 https://www.example.com 到页面显示，完整发生了什么？](../10-troubleshooting-system-design/091-url-to-page-full-path.md)

## 复习卡片

- **一句话**：SNI 在 TLS 握手早期告诉服务器客户端想访问哪个域名，使一个 IP 上可选择正确证书/虚拟主机；ALPN 让双方协商 TLS 上层应用协议，例如 `h2` 或 `http/1.1`。一个解决“哪个主机”，一个解决“说哪种协议”。
- **必须会解释**：TLS Extension / Virtual Hosting。
- **必须避免**：把 SNI 当作 DNS。
- **必须会验证**：用 `openssl s_client -servername` 对同一 CDN IP 测不同域名；查看 ALPN negotiated protocol。
