---
id: 75
title: "TLS 1.3 Handshake 需要掌握到什么程度？"
chapter: "第八章 HTTPS、TLS 1.3 与 PKI"
difficulty: "进阶"
frequency: "★★★★★"
tags: ["TLS 1.3", "Handshake"]
source: "计算机网络面试100题_专业详解版_2026.pdf"
edition: "2.0-deep"
updated: "2026-09-02"
---
# 075. TLS 1.3 Handshake 需要掌握到什么程度？

> **定位**：进阶 · **面试频率**：★★★★★ · **标签**：TLS 1.3 / Handshake  
> **本章**：[第八章 HTTPS、TLS 1.3 与 PKI](README.md) · [返回总目录](../../README.md)

## 面试官到底在考什么

这道题不只考定义。面试官通常希望确认你能否把 **TLS 1.3 / Handshake** 放进真实协议栈/系统调用/故障场景中解释，并且在追问发生时仍保持同一个心智模型，而不是切换成互相矛盾的八股结论。

## 30 秒标准回答（PDF 原内容）

> 面试应能说明 ClientHello 携带版本、cipher suites、key share、SNI/ALPN 等；ServerHello 选择参数并给出 key share，双方基于 (EC)DHE 派生 handshake keys；随后服务器发送加密的证书/签名/Finished，客户端验证并返回 Finished，之后进入 application data。

## 核心时序 / 心智模型（PDF 原内容）

```text
ClientHello + key_share
          ↓
ServerHello + key_share
          ↓
Handshake keys derived
          ↓
Certificate / Verify / Finished
          ↓
Client Finished
          ↓
Encrypted Application Data
```

## 深度解析：Know-How + Know-Why（PDF 原内容）

1. TLS 1.3 大幅移除旧式静态 RSA key exchange 与许多不安全/复杂算法。
2. ServerHello 后大部分握手内容已被加密。
3. 证书签名用于身份认证，ECDHE 用于会话密钥协商，两者角色不同。

## 二次深化：工程上还必须知道什么

TLS 1.3 的重点是 ClientHello/ServerHello、Key Share、证书与 CertificateVerify、Finished，以及何时派生 handshake/application traffic keys；不必现场背每个扩展字段，但必须能解释认证与密钥协商分别在做什么。

### 本章共同的工程视角

- TLS 的三个核心属性是机密性、完整性和对端认证；握手的目的不是“加密每个包”，而是安全建立会话密钥和身份。
- 证书验证与密钥协商是两条逻辑：证书证明“对方是谁/其公钥可信”，(EC)DHE 建立前向安全的共享密钥。
- 0-RTT 的性能收益来自提前发送 early data，但 replay 风险决定它只适合可安全重放的业务语义。

<!-- V2-ENRICHMENT-START -->
## V2 深入：TLS 1.3 面试要掌握消息流、Key Schedule 与“谁证明了什么”

### 第一性原理

- ClientHello 提供 supported_versions、cipher suites、key_share、signature algorithms、SNI/ALPN 等；ServerHello 选择参数与 key_share 后，双方可基于 (EC)DHE 派生 handshake secrets。
- ServerHello 后大部分 handshake message 已加密；Server 通过 Certificate + CertificateVerify 证明对证书私钥的控制，Finished 用 transcript-derived MAC 证明握手 transcript 与 secrets 一致。
- Client 验证证书链/身份后发送自己的 Finished，随后双方使用 application traffic secrets 保护数据。

### Key Schedule 心智模型

TLS 1.3 使用 HKDF 做强 key separation：early/handshake/application 等不同阶段 secret 分离，并结合 transcript hash。不要背每个 label 字符串，但要理解“不是直接把 ECDHE shared secret 当 AES key”。

### 1-RTT 与 TLS 1.2

TLS 1.3 移除了 static RSA key exchange、精简 cipher suite，使 full handshake 通常更少往返并默认具备 public-key forward secrecy；0-RTT 属于恢复连接的额外模式，不是所有 TLS 1.3 第一次连接都 0 RTT。

### 2026 规范提示

RFC 9846 是 TLS 1.3 当前规范，保持协议版本 1.3 与 RFC 8446 wire compatibility，但收紧 key-share reuse、旧版本协商等要求。
<!-- V2-ENRICHMENT-END -->

## 面试现场推荐回答结构

1. **先给结论**：用 2-4 句话回答“TLS 1.3 Handshake 需要掌握到什么程度？”，避免一上来陷入历史背景。
2. **再给机制**：围绕 TLS 1.3、Handshake 说明关键状态、字段或数据路径。
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

### 追问 1：TLS 1.2 与 1.3 往返和密码套件结构差异？

**参考回答**：TLS 1.3把密钥协商与AEAD套件结构简化，通常1-RTT完成首次握手。CertificateVerify用证书私钥对握手上下文签名以证明持钥身份；Finished基于派生密钥校验完整握手 transcript；HKDF负责分阶段派生密钥材料。

### 追问 2：CertificateVerify 在证明什么？

**参考回答**：TLS 1.3把密钥协商与AEAD套件结构简化，通常1-RTT完成首次握手。CertificateVerify用证书私钥对握手上下文签名以证明持钥身份；Finished基于派生密钥校验完整握手 transcript；HKDF负责分阶段派生密钥材料。

### 追问 3：Finished 如何证明握手未被篡改？

**参考回答**：FIN表示一个方向“不会再发送更多字节”，支持半关闭和有序收尾；RST表示异常终止/立即重置连接，通常不提供优雅 half-close 语义。shutdown(SHUT_WR)只关闭发送方向，close()则释放文件描述符并进入完整关闭流程。 TLS 1.3把密钥协商与AEAD套件结构简化，通常1-RTT完成首次握手。CertificateVerify用证书私钥对握手上下文签名以证明持钥身份；Finished基于派生密钥校验完整握手 transcript；HKDF负责分阶段派生密钥材料。

## 高频易错点（PDF 原内容）

- ❌ 把服务器证书公钥直接当成最终 AES key。
- ❌ 把 cipher suite 中的签名算法理解成 TLS1.2 老模型。

## 动手验证 / 抓包实验（PDF 原内容）

用 Wireshark 抓 TLS1.3 握手并标注 ClientHello、ServerHello、EncryptedExtensions、Certificate、Finished。

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

- [074. HTTP 与 HTTPS 的本质区别是什么？TLS 提供了哪些安全属性？](074-http-vs-https.md)
- [077. TLS 为什么同时使用非对称密码学和对称加密？](077-asymmetric-vs-symmetric-crypto.md)
- [078. 什么是 Forward Secrecy？为什么 ECDHE 很重要？](078-forward-secrecy-ecdhe.md)

## 复习卡片

- **一句话**：面试应能说明 ClientHello 携带版本、cipher suites、key share、SNI/ALPN 等；ServerHello 选择参数并给出 key share，双方基于 (EC)DHE 派生 handshake keys；随后服务器发送加密的证书/签名/Finished，客户端验证并返回 Finished，之后进入 application data。
- **必须会解释**：TLS 1.3 / Handshake。
- **必须避免**：把服务器证书公钥直接当成最终 AES key。
- **必须会验证**：用 Wireshark 抓 TLS1.3 握手并标注 ClientHello、ServerHello、EncryptedExtensions、Certificate、Finished。
