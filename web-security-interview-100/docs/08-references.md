# 参考资料与 2026 版本说明

仓库构建日期：**2026-09-02**。母版 PDF 的 S1-S8 引用体系全部保留；以下同时记录本次扩展时核验的当前版本。

| ID | 资料 | 状态/用途 |
|---|---|---|
| S1 | [OWASP Top 10:2025](https://owasp.org/Top10/2025/) | 2025 正式版；风险意识与宏观分类 |
| S2 | [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) | 2023 正式版；现代 API 安全风险 |
| S3 | [2025 CWE Top 25](https://cwe.mitre.org/top25/archive/2025/2025_cwe_top25.html) | 2025 Top 25；高频软件弱点根因 |
| S4 | [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) | 持续更新；工程防御实践 |
| S5 | [PortSwigger Web Security Academy](https://portswigger.net/web-security/all-topics) | 持续更新；现代 Web 主题学习地图 |
| S6 | [RFC 9700 - Best Current Practice for OAuth 2.0 Security](https://www.rfc-editor.org/info/rfc9700/) | OAuth 2.0 Security BCP；redirect-based flow 等现代安全建议 |
| S7 | [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) | 5.0.0 于 2025-05-30 发布；可验证应用安全要求 |
| S8 | [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/stable/) | 稳定版；测试方法与覆盖模型 |

## WSTG 最新内容

- [OWASP WSTG - Latest](https://owasp.org/www-project-web-security-testing-guide/latest/) 会持续变化，适合追踪新测试内容。
- 面试/工程基线建议在文档中固定版本，避免“latest”随时间变化导致不可复现。

## 版权与组织方式说明

本仓库借鉴的是“题目 → 考察点 → 原理 → 工程实践 → 追问 → 复习”的题解型组织方式，不复制《剑指 Offer》的原文、题目或受版权保护的具体表达。


## 如何使用参考标准

- **OWASP Top 10**：用于风险意识和面试分类，不应当作完整验收清单。
- **OWASP ASVS 5.0.0**：更适合作为应用安全控制要求与工程验收基线。
- **OWASP WSTG**：更适合作为测试方法和验证思路参考；仓库链接建议优先使用 stable 版本，阅读最新贡献时再使用 latest。
- **OWASP API Security Top 10:2023**：用于 API 授权、资源消耗、业务流、库存与第三方 API 风险。
- **CWE**：用于根因分类、缺陷归因和与工具/SAST 结果对齐。
- **RFC / 浏览器规范**：当问题涉及 OAuth、HTTP、Cookie、Origin 等精确协议语义时，应优先查规范而不是二手博客。
