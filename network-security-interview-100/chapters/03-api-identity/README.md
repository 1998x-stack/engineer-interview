# 第 3 章：高级 Web、API 与身份安全

> 从单点漏洞升级到访问控制、会话、OAuth/OIDC 与 API 设计

**关键词：** BOLA/IDOR / JWT / Session / OAuth/OIDC / CORS/SOP / HTTP Desync

## 本章学习目标

- 判断候选人是否从“漏洞点”升级到浏览器安全模型、对象级授权、会话与联合身份的系统视角。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- 谁是主体？访问哪个对象/能力？
- 认证完成后授权在哪里执行？
- Token/Cookie 的生命周期和绑定关系是什么？
- 浏览器、Gateway 与后端分别承担什么安全责任？

## 题目索引

- [Q21 Path Traversal 与 File Inclusion 有什么区别？](../../questions/03-api-identity/q21-file-path-security.md) - 难度 3/5 - File Path Security
- [Q22 OS Command Injection 的本质是什么？](../../questions/03-api-identity/q22-owasp-injection-asvs.md) - 难度 3/5 - OWASP Injection / ASVS
- [Q23 什么是反序列化漏洞？](../../questions/03-api-identity/q23-serialization-security.md) - 难度 4/5 - Serialization Security
- [Q24 Request Smuggling / HTTP Desync 的本质是什么？](../../questions/03-api-identity/q24-http-parser-differential.md) - 难度 5/5 - HTTP Parser Differential
- [Q25 什么是 IDOR / BOLA？为什么它如此常见？](../../questions/03-api-identity/q25-owasp-api1-bola-a01.md) - 难度 3/5 - OWASP API1 BOLA / A01
- [Q26 水平越权、垂直越权、未授权访问分别是什么？](../../questions/03-api-identity/q26-access-control.md) - 难度 2/5 - Access Control
- [Q27 JWT 是什么？最常见的设计错误有哪些？](../../questions/03-api-identity/q27-jwt-jose.md) - 难度 3/5 - JWT / JOSE
- [Q28 Cookie、Session、JWT 的区别是什么？](../../questions/03-api-identity/q28-web-identity.md) - 难度 3/5 - Web Identity
- [Q29 OAuth 2.0 与 OpenID Connect 有什么区别？](../../questions/03-api-identity/q29-oauth2-oidc.md) - 难度 4/5 - OAuth2 / OIDC
- [Q30 CORS 与 Same-Origin Policy 的关系是什么？](../../questions/03-api-identity/q30-browser-security.md) - 难度 3/5 - Browser Security

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q21](../../questions/03-api-identity/q21-file-path-security.md) | 用户输入影响最终文件资源或解释路径。 | 对象映射 + canonical root + 最小文件权限。 | normalized/resolved path 与文件审计。 |
| [Q22](../../questions/03-api-identity/q22-owasp-injection-asvs.md) | 不可信数据被命令解释器/外部程序当成控制语义。 | 避免 shell + 固定 executable + 参数 schema + 最小权限。 | process tree/command line/code path。 |
| [Q23](../../questions/03-api-identity/q23-serialization-security.md) | 不可信数据驱动对象构造与副作用。 | 简单 schema + 类型 allowlist + 最小能力。 | deserialize entry + producer/schema + runtime side effects。 |
| [Q24](../../questions/03-api-identity/q24-http-parser-differential.md) | 链路 parser 对请求边界理解不一致。 | 严格解析 + 减少转换 + 兼容性回归。 | edge-origin request 对齐与 framing errors。 |
| [Q25](../../questions/03-api-identity/q25-owasp-api1-bola-a01.md) | 对象访问缺少服务端 subject-resource-action 授权。 | 集中策略 + tenant scoped query + default deny。 | authorization decision audit。 |
| [Q26](../../questions/03-api-identity/q26-access-control.md) | 服务端权限决策缺失或模型错误。 | default deny + central policy + JIT 敏感权限。 | authn + authz decision + permission change logs。 |
| [Q27](../../questions/03-api-identity/q27-jwt-jose.md) | JWT 只是承载 claims 的格式，安全取决于严格验证与生命周期。 | 固定算法 + claims 校验 + 短生命周期 + 密钥治理。 | validation result/key id/issuer audit。 |
| [Q28](../../questions/03-api-identity/q28-web-identity.md) | Cookie/Session/JWT 是不同层次概念，不能二选一比较。 | 安全 Cookie + session rotation + 生命周期/撤销设计。 | session/token lifecycle audit。 |
| [Q29](../../questions/03-api-identity/q29-oauth2-oidc.md) | OAuth 授权，OIDC 认证身份层；不同 token 有不同受众。 | Code+PKCE + 严格 redirect/claims + scope 最小化。 | AS/RS token lifecycle audit。 |
| [Q30](../../questions/03-api-identity/q30-browser-security.md) | SOP 默认隔离，CORS 由服务器声明允许的跨源读取。 | 精确 origin allowlist + credential/CSRF 协同。 | CORS headers + browser/network + gateway config。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
