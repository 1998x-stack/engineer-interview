# Web Security Interview 100 · 2026

> 一套面向 Web Security / AppSec / 安全研发 / 渗透测试面试的 **100 道系统化题解仓库**。  
> 母版来自 209 页《Web 漏洞面试 100 题 · 2026 专业题解手册》，并扩展为一题一 Markdown 的工程化知识库。

## 仓库定位

这不是 Payload 速查表。核心目标是把每道题从“会背漏洞”升级为：

```text
定义 / 边界
  -> 根因 / 机制
  -> 错误防御为什么失效
  -> 工程控制
  -> Security Invariant
  -> 代码审计 / 设计评审 / 测试
  -> 监控 / 回归
```

## 规模

- **100 道题**，每题一个 Markdown。
- **10 个章节**，覆盖浏览器、认证授权、Injection、SSRF、HTTP 高阶、API、供应链与 SDL。
- **209 页母版 PDF** 保存在 [`docs/pdf/`](docs/pdf/web-security-interview-100-2026.pdf)。
- 每题包含 **PDF 母版题解 + GitHub 增强版**。
- 增强版新增安全不变量、审计清单、防御性示例、2026 标准映射与交叉链接。

## 目录

| 章节 | 范围 | 主题 |
|---|---:|---|
| [HTTP、浏览器与 Web 安全基础](questions/01-http-browser/) | Q001-Q010 | HTTP / Cookie / SOP / CORS / TLS / Trust Boundary |
| [访问控制、越权与 IDOR/BOLA](questions/02-access-control/) | Q011-Q020 | BOLA / BFLA / BOPLA / RBAC / ABAC / Multi-tenant |
| [认证、Session、JWT 与 OAuth](questions/03-auth-session-oauth/) | Q021-Q030 | Session / Password / JWT / Token / OAuth / PKCE |
| [Injection 家族](questions/04-injection/) | Q031-Q042 | SQL / NoSQL / Command / SSTI / XXE / LDAP / CRLF |
| [浏览器安全](questions/05-browser-security/) | Q043-Q054 | XSS / CSP / Trusted Types / CSRF / SameSite / XS-Leaks |
| [服务端能力](questions/06-server-side/) | Q055-Q064 | SSRF / Path / Upload / Deserialization / Archive |
| [HTTP 基础设施与高级漏洞](questions/07-http-infrastructure/) | Q065-Q074 | Smuggling / Cache / Host / Proxy / Parser / Race |
| [API / GraphQL / WebSocket](questions/08-api-graphql-websocket/) | Q075-Q084 | API AuthZ / Resource / Business Flow / GraphQL / WebSocket |
| [配置、供应链、日志与异常](questions/09-config-supplychain-logging/) | Q085-Q092 | Misconfiguration / Supply Chain / SBOM / Secrets / Logging |
| [代码审计、SDL 与综合架构](questions/10-code-review-sdl/) | Q093-Q100 | Code Review / WAF / Risk / Testing Pipeline / Secure by Default |

完整索引见 [`questions/README.md`](questions/README.md)。

## 推荐阅读路径

1. [前言与使用方法](docs/00-preface.md)
2. [知识地图](docs/01-knowledge-map.md)
3. [面试评分尺](docs/02-interview-rubric.md)
4. [100 题总览](docs/03-100-question-overview.md)
5. [OWASP Top 10:2025 映射](docs/04-owasp-top10-2025-mapping.md)
6. [API Security Top 10:2023 映射](docs/05-api-security-mapping.md)
7. [2025 CWE Top 25 映射](docs/06-cwe-top25-mapping.md)
8. [7 天冲刺计划](docs/07-7-day-sprint.md)
9. [参考资料与版本说明](docs/08-references.md)
10. [母版与增强内容边界](docs/09-source-and-enrichment.md)
11. [术语表](docs/10-glossary.md)

## 每题 Markdown 的固定结构

```text
Qxxx
├── 母版一句话结论
├── 元信息
├── PDF 母版题解
│   ├── 面试官在考什么
│   ├── 原理与机制
│   ├── 工程防御
│   ├── Gotchas
│   ├── 面试追问
│   ├── 一分钟回答模板
│   └── 复习检查
└── GitHub 增强版
    ├── 深度展开
    ├── Security Invariants
    ├── 代码审计 / 设计评审 / 测试视角
    ├── 防御性示例（部分题）
    ├── 新增 Gotchas
    ├── 高阶追问
    ├── 标准映射
    └── 关联题目
```

## 2026 基线

仓库按以下公开标准校准：

- OWASP Top 10:2025
- OWASP ASVS 5.0.0
- OWASP API Security Top 10:2023
- OWASP Web Security Testing Guide
- 2025 CWE Top 25
- OWASP Cheat Sheet Series
- RFC 9700 OAuth 2.0 Security BCP
- PortSwigger Web Security Academy（用于主题覆盖参考）

详见 [`docs/08-references.md`](docs/08-references.md)。

## Review Checklists

- [Access Control Review](checklists/access-control-review.md)
- [Injection Review](checklists/injection-review.md)
- [Browser Security Review](checklists/browser-security-review.md)
- [Server-side Capability Review](checklists/server-side-review.md)
- [HTTP Infrastructure Review](checklists/http-infrastructure-review.md)
- [SDL / AppSec Program Review](checklists/sdl-review.md)

## 仓库自检

```bash
python scripts/validate_repo.py
```

它会检查：

- Q001-Q100 是否全部存在；
- 是否严格一题一 Markdown；
- front matter 中的 `id/title/source_pdf_page` 是否完整；
- 每题是否包含 PDF 母版题解与 GitHub 增强版；
- 题目索引链接是否存在。

## 内容边界

本仓库只用于合法、授权的安全学习、面试与防御性工程实践。重点是安全原理、代码审计、设计评审、验证与治理，不提供针对真实目标的破坏性操作步骤。

## 版权说明

“剑指 Offer 式”仅指 **题解型组织思路**：题目 → 考察点 → 原理 → 工程实践 → 追问 → 复习。仓库不复制《剑指 Offer》原文、题目或具体受版权保护的表达。

## License

- 文档与题解：建议按 **CC BY 4.0** 使用。
- `scripts/` 中的辅助脚本：建议按 **MIT** 使用。

见 [`LICENSE.md`](LICENSE.md)。


## V2 深度增强说明

第二轮增强将每道题从“面试题解”扩展为可独立用于 AppSec 实践的学习单元。Q001–Q100 均新增：

- Threat Modeling：资产、主体、信任边界与能力面；
- Security Invariants：把最佳实践写成可测试的规则；
- Failure Chain：从入口到敏感资产的因果链；
- Code Review：入口、安全上下文、控制点和 sink 的审计方法；
- Architecture Review：控制在 Edge / Application / Domain / Runtime 四层的职责；
- Verification Matrix：Unit / Integration / Negative Regression / Runtime Evidence；
- 防御性案例推演、异常路径与并发/旧版本回归；
- 30 秒 / 2 分钟 / 5 分钟三级面试表达；
- Senior/Staff 级设计权衡与平台化治理讨论。

这意味着本仓库既可以作为面试题库，也可以作为代码审计、设计评审和安全测试的复习手册。
