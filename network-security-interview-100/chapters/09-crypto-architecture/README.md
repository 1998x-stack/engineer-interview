# 第 9 章：密码学、安全架构与治理

> 从密码学原语到 PKI、KMS、Zero Trust、NIST CSF

**关键词：** Hash/Encryption / Password KDF / TLS 1.3 / PKI / mTLS / KMS / CSF 2.0

## 本章学习目标

- 考察是否理解密码学“正确组合和密钥管理”比背算法名称更重要，并能把技术控制放入架构与治理。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- 安全目标是机密性、完整性、真实性还是不可抵赖？
- 密钥如何生成、存储、轮换和吊销？
- 算法的 nonce/IV/参数有什么约束？
- 加密之后谁仍有解密权限？

## 题目索引

- [Q81 对称加密和非对称加密有什么区别？](../../questions/09-crypto-architecture/q81-cryptography-basics.md) - 难度 2/5 - Cryptography Basics
- [Q82 Hash、Encryption、Encoding 有什么区别？](../../questions/09-crypto-architecture/q82-crypto-basics.md) - 难度 2/5 - Crypto Basics
- [Q83 密码应该怎么存？](../../questions/09-crypto-architecture/q83-password-storage.md) - 难度 3/5 - Password Storage
- [Q84 TLS 1.3 握手过程中解决了什么问题？](../../questions/09-crypto-architecture/q84-tls-1-3.md) - 难度 4/5 - TLS 1.3
- [Q85 如何保证你拿到的公钥确实属于目标网站？](../../questions/09-crypto-architecture/q85-pki.md) - 难度 4/5 - PKI
- [Q86 mTLS 和普通 TLS 有什么区别？](../../questions/09-crypto-architecture/q86-mtls.md) - 难度 3/5 - mTLS
- [Q87 IV、Nonce 为什么经常是密码学实现漏洞来源？](../../questions/09-crypto-architecture/q87-crypto-construction.md) - 难度 4/5 - Crypto Construction
- [Q88 Encryption at Rest 做了以后数据是不是安全了？](../../questions/09-crypto-architecture/q88-kms-data-security.md) - 难度 3/5 - KMS / Data Security
- [Q89 什么是 Zero Trust？最常见的错误理解是什么？](../../questions/09-crypto-architecture/q89-nist-sp-800-207.md) - 难度 4/5 - NIST SP 800-207
- [Q90 NIST CSF 2.0 六大 Function 是什么？](../../questions/09-crypto-architecture/q90-nist-csf-2-0.md) - 难度 4/5 - NIST CSF 2.0

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q81](../../questions/09-crypto-architecture/q81-cryptography-basics.md) | 不同密码原语解决不同安全属性，现代系统组合使用。 | 标准协议 + AEAD + KMS/HSM + rotation。 | key lifecycle/config/API usage。 |
| [Q82](../../questions/09-crypto-architecture/q82-crypto-basics.md) | 不同变换提供完全不同安全属性。 | 按属性选标准 primitive。 | API/config/hash scheme。 |
| [Q83](../../questions/09-crypto-architecture/q83-password-storage.md) | 数据库泄露后需提高离线猜测成本。 | 专用 KDF + salt + 可选 pepper + MFA/rate limit。 | hash metadata/auth/KMS。 |
| [Q84](../../questions/09-crypto-architecture/q84-tls-1-3.md) | 握手建立认证的共享 traffic keys。 | modern TLS + cert automation + safe early-data policy。 | handshake/cert/key/edge-origin。 |
| [Q85](../../questions/09-crypto-architecture/q85-pki.md) | 受信 CA 把身份绑定到公钥。 | PKI + hostname validation + protected keys + monitoring。 | chain/CA/CT/KMS。 |
| [Q86](../../questions/09-crypto-architecture/q86-mtls.md) | 双方证书提供传输层双向身份认证。 | unique short-lived cert + explicit authz。 | client cert/CA/authz logs。 |
| [Q87](../../questions/09-crypto-architecture/q87-crypto-construction.md) | 密码模式依赖 nonce/IV 满足特定安全前提。 | 高层 AEAD + 规范化 nonce 管理。 | API/generation/key metadata。 |
| [Q88](../../questions/09-crypto-architecture/q88-kms-data-security.md) | 静态介质保护依赖密钥与数据访问分离。 | KMS/HSM + envelope + separated IAM。 | KMS/data/snapshot/key audit。 |
| [Q89](../../questions/09-crypto-architecture/q89-nist-sp-800-207.md) | 位置不是充分信任依据，资源访问需显式最小权限。 | identity/device/resource policy + segmentation/JIT。 | policy/posture/session/access。 |
| [Q90](../../questions/09-crypto-architecture/q90-nist-csf-2-0.md) | CSF 用六类 outcome 组织全生命周期网络安全风险管理。 | profiles + governance + risk-prioritized initiatives。 | profile/risk/metrics/owner。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
