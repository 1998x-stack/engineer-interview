# 第 6 章：代码审计、漏洞研究与软件供应链

> 从 Source-Taint-Sink 到 CI/CD、依赖与构建完整性

**关键词：** SAST/DAST/IAST/SCA / Taint Analysis / 反序列化 / 供应链 / SBOM / CI/CD

## 本章学习目标

- 考察代码级数据流思维和软件供应链全链路风险，而不是仅会运行扫描器。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- Source/Propagation/Sanitizer/Sink 在哪里？
- 问题发生在自研代码、依赖、构建还是发布链？
- 工具结果是否可达、可利用、影响关键资产？
- 如何把修复变成 SDLC 的可重复控制？

## 题目索引

- [Q51 SAST、DAST、IAST、SCA 有什么区别？](../../questions/06-appsec-supply-chain/q51-appsec-tooling.md) - 难度 3/5 - AppSec Tooling
- [Q52 什么是 Taint Analysis？](../../questions/06-appsec-supply-chain/q52-static-analysis.md) - 难度 4/5 - Static Analysis
- [Q53 做 SQL 注入代码审计时，你会怎么看？](../../questions/06-appsec-supply-chain/q53-owasp-injection.md) - 难度 4/5 - OWASP Injection
- [Q54 Java 反序列化代码审计应该关注什么？](../../questions/06-appsec-supply-chain/q54-serialization-review.md) - 难度 5/5 - Serialization Review
- [Q55 软件供应链攻击是什么？](../../questions/06-appsec-supply-chain/q55-owasp-a03-2025.md) - 难度 4/5 - OWASP A03:2025
- [Q56 什么是 SBOM？SBOM 能解决所有供应链问题吗？](../../questions/06-appsec-supply-chain/q56-sbom.md) - 难度 3/5 - SBOM
- [Q57 Git 仓库泄露密钥为什么严重？](../../questions/06-appsec-supply-chain/q57-secrets-incident.md) - 难度 3/5 - Secrets Incident
- [Q58 CI/CD Pipeline 有哪些典型安全风险？](../../questions/06-appsec-supply-chain/q58-ci-cd-security.md) - 难度 4/5 - CI/CD Security
- [Q59 为什么安全研究员喜欢分析补丁 diff？](../../questions/06-appsec-supply-chain/q59-root-cause-analysis.md) - 难度 4/5 - Root Cause Analysis
- [Q60 Buffer Overflow 的本质和现代防护是什么？](../../questions/06-appsec-supply-chain/q60-memory-safety.md) - 难度 4/5 - Memory Safety

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q51](../../questions/06-appsec-supply-chain/q51-appsec-tooling.md) | 不同测试技术观察不同证据面。 | 组合工具 + 风险分层 + owner workflow。 | code/runtime/dependency/deploy context。 |
| [Q52](../../questions/06-appsec-supply-chain/q52-static-analysis.md) | 追踪不可信数据到危险 sink 的可达性。 | 精确 source/sink/sanitizer modeling。 | data-flow/call graph/runtime trace。 |
| [Q53](../../questions/06-appsec-supply-chain/q53-owasp-injection.md) | 不可信数据可达 SQL 结构构造。 | 安全 data-access API + taint review + DB least privilege。 | source-sink/code/query/DB audit。 |
| [Q54](../../questions/06-appsec-supply-chain/q54-serialization-review.md) | 对象恢复能力被不可信数据驱动。 | schema/allowlist + minimal classpath/privilege。 | callsite/config/SBOM/runtime。 |
| [Q55](../../questions/06-appsec-supply-chain/q55-owasp-a03-2025.md) | 软件生产链任一环节失信可把风险传播到发布物。 | least-privilege CI + provenance + signed artifact + admission。 | repo→build→registry→deploy lineage。 |
| [Q56](../../questions/06-appsec-supply-chain/q56-sbom.md) | 缺乏组件可见性导致供应链风险无法定位。 | build-time SBOM + provenance + vuln enrichment。 | SBOM/lock/provenance/deployment。 |
| [Q57](../../questions/06-appsec-supply-chain/q57-secrets-incident.md) | secret 被复制到不可控代码历史并可能被滥用。 | revoke/rotate 优先 + preventive scanning + short-lived identity。 | repo + credential usage + rotation logs。 |
| [Q58](../../questions/06-appsec-supply-chain/q58-ci-cd-security.md) | 自动化高权限流水线若失信可污染软件发布链。 | least privilege + isolated runner + provenance/admission。 | pipeline/runner/secret/artifact/deploy audit。 |
| [Q59](../../questions/06-appsec-supply-chain/q59-root-cause-analysis.md) | 补丁揭示被破坏的安全不变量。 | root-cause abstraction + sibling audit + regression。 | diff/advisory/version/deployment。 |
| [Q60](../../questions/06-appsec-supply-chain/q60-memory-safety.md) | 越界读写破坏内存安全。 | memory-safe language + bounds + hardening + fuzzing。 | crash/sanitizer/build/fuzz。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
