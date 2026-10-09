# 第八章 HTTPS、TLS 1.3 与 PKI

掌握握手、证书、密钥协商与 0-RTT 风险。

## 本章能力目标

- TLS 的三个核心属性是机密性、完整性和对端认证；握手的目的不是“加密每个包”，而是安全建立会话密钥和身份。
- 证书验证与密钥协商是两条逻辑：证书证明“对方是谁/其公钥可信”，(EC)DHE 建立前向安全的共享密钥。
- 0-RTT 的性能收益来自提前发送 early data，但 replay 风险决定它只适合可安全重放的业务语义。

<!-- CHAPTER-V2-START -->
## V2 本章深度训练框架

### 必须形成的心智模型

- **认证、密钥建立、数据保护分工明确**：Certificate/CertificateVerify、(EC)DHE、HKDF、AEAD 各自解决不同问题。
- **证书可信 ≠ hostname 正确**：chain、trust anchor、SAN、validity、usage、CT/revocation 是多个独立检查。
- **0-RTT 用历史状态换延迟**：Replay Risk 必须由应用幂等/anti-replay 共同治理。

### 本章白板题

1. 画 TLS 1.3 full handshake，标明从何时开始加密、CertificateVerify/Finished 各证明什么。
2. 画 Root→Intermediate→Leaf 验证链，并解释为什么 Server 不应把“自己发的 Root”当信任来源。
3. 给出转账、静态 GET、幂等查询三种请求，判断是否适合 0-RTT。

### 规范更新（2026）

TLS 1.3 现行规范为 **RFC 9846**，它兼容地取代 RFC 8446，并收紧 key-share reuse、旧版本协商等要求；学习资料若仍引用 RFC 8446，应以 RFC 9846 为当前规范对照更新。
<!-- CHAPTER-V2-END -->

## 题目目录

- [074. HTTP 与 HTTPS 的本质区别是什么？TLS 提供了哪些安全属性？](074-http-vs-https.md) · 基础 · ★★★★★
- [075. TLS 1.3 Handshake 需要掌握到什么程度？](075-tls13-handshake.md) · 进阶 · ★★★★★
- [076. 浏览器如何验证 HTTPS 证书？证书链、主机名、有效期各自是什么作用？](076-certificate-validation.md) · 进阶 · ★★★★★
- [077. TLS 为什么同时使用非对称密码学和对称加密？](077-asymmetric-vs-symmetric-crypto.md) · 基础 · ★★★★☆
- [078. 什么是 Forward Secrecy？为什么 ECDHE 很重要？](078-forward-secrecy-ecdhe.md) · 进阶 · ★★★★☆
- [079. SNI 与 ALPN 分别解决什么问题？](079-sni-vs-alpn.md) · 进阶 · ★★★★☆
- [080. TLS 1.3 0-RTT 为什么有 Replay Risk？哪些业务不适合？](080-tls13-0rtt-replay.md) · 进阶 · ★★★★★

## 推荐实践工具

- `openssl s_client`
- `curl -vk`
- `openssl x509 -text`
- `Wireshark TLS`

[← 返回全书目录](../../README.md)
