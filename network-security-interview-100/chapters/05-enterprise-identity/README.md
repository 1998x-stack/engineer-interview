# 第 5 章：内网、身份与 Active Directory

> 企业攻防的核心越来越接近 Identity & Trust

**关键词：** Kerberos / NTLM / 凭证安全 / 横向移动 / Zero Trust / Secrets

## 本章学习目标

- 考察企业安全中“身份即控制面”的理解，包括票据、凭证、机器身份、权限和信任关系。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- 身份如何被证明？
- 权限如何被授予和撤销？
- 凭证可否重放、转移或长期复用？
- 信任关系失陷后影响半径有多大？

## 题目索引

- [Q41 Kerberos 的基本认证流程是什么？](../../questions/05-enterprise-identity/q41-kerberos.md) - 难度 4/5 - Kerberos
- [Q42 NTLM 与 Kerberos 有什么区别？](../../questions/05-enterprise-identity/q42-windows-authentication.md) - 难度 4/5 - Windows Authentication
- [Q43 为什么 Credential Access 是企业攻击的重要阶段？](../../questions/05-enterprise-identity/q43-mitre-credential-access.md) - 难度 4/5 - MITRE Credential Access
- [Q44 什么是 Lateral Movement？](../../questions/05-enterprise-identity/q44-mitre-lateral-movement.md) - 难度 3/5 - MITRE Lateral Movement
- [Q45 网络分区和 Zero Trust 有什么区别？](../../questions/05-enterprise-identity/q45-nist-sp-800-207.md) - 难度 4/5 - NIST SP 800-207
- [Q46 什么是 Least Privilege？](../../questions/05-enterprise-identity/q46-authorization.md) - 难度 2/5 - Authorization
- [Q47 如果域管理员账号疑似泄露，你怎么处理？](../../questions/05-enterprise-identity/q47-identity-incident.md) - 难度 5/5 - Identity Incident
- [Q48 企业内部资产发现为什么重要？](../../questions/05-enterprise-identity/q48-asset-management.md) - 难度 3/5 - Asset Management
- [Q49 Secrets 应该如何管理？](../../questions/05-enterprise-identity/q49-secrets-management.md) - 难度 3/5 - Secrets Management
- [Q50 为什么企业现在越来越需要关注证书身份安全？](../../questions/05-enterprise-identity/q50-machine-identity-pki.md) - 难度 5/5 - Machine Identity / PKI

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q41](../../questions/05-enterprise-identity/q41-kerberos.md) | 用可信 KDC 和短期票据完成域内服务认证。 | KDC/服务账户保护 + 委派治理 + 票据监控。 | KDC tickets + SPN/config + endpoint auth。 |
| [Q42](../../questions/05-enterprise-identity/q42-windows-authentication.md) | 两种 Windows 认证模型不同，legacy 协议扩大可滥用面。 | inventory→灰度减少→强认证。 | 域控协议使用日志。 |
| [Q43](../../questions/05-enterprise-identity/q43-mitre-credential-access.md) | 攻击者获得可复用身份凭据后可模拟合法主体。 | 短期凭据 + JIT/MFA + secret 生命周期治理。 | IdP/secret/token/cert/EDR。 |
| [Q44](../../questions/05-enterprise-identity/q44-mitre-lateral-movement.md) | 利用身份/远程服务/信任从一个资产移动到另一个。 | 分段 + JIT 管理身份 + 凭据隔离。 | remote auth/process/flow/cloud API。 |
| [Q45](../../questions/05-enterprise-identity/q45-nist-sp-800-207.md) | 不因位置隐式信任，资源访问需显式决策。 | identity+device+resource policy + segmentation。 | policy/IdP/device/flow。 |
| [Q46](../../questions/05-enterprise-identity/q46-authorization.md) | 主体拥有超出任务所需的能力会扩大错误/compromise 影响。 | default deny + JIT + 定期 review。 | grant/use/revoke audit。 |
| [Q47](../../questions/05-enterprise-identity/q47-identity-incident.md) | 高权身份泄露可能演变为身份控制平面失信。 | 重大 IR + trusted recovery + privileged isolation。 | DC/IdP/admin endpoint/config。 |
| [Q48](../../questions/05-enterprise-identity/q48-asset-management.md) | 未知资产造成安全控制盲区和错误指标。 | 多源发现 + canonical ID + owner/lifecycle。 | last-seen/source/owner/exposure。 |
| [Q49](../../questions/05-enterprise-identity/q49-secrets-management.md) | 长期敏感凭据易泄露且滥用范围大。 | workload identity + secret manager + rotation + audit。 | manager/Git/CI/auth logs。 |
| [Q50](../../questions/05-enterprise-identity/q50-machine-identity-pki.md) | 机器身份依赖大量证书/私钥，生命周期失控会形成高影响信任风险。 | inventory + automated short-lived cert + protected keys。 | CA/KMS/TLS lifecycle logs。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
