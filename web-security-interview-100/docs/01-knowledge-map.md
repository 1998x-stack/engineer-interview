# 知识地图

```text
Web Security
├── HTTP / Browser Security
│   ├── Cookie / Session
│   ├── SOP / CORS / SameSite
│   └── URL / TLS / Trust Boundary
├── Identity & Access Control
│   ├── AuthN / AuthZ
│   ├── BOLA / BFLA / BOPLA
│   ├── RBAC / ABAC
│   └── Multi-tenancy
├── Injection
│   ├── SQL / NoSQL
│   ├── Command / Template
│   ├── XML / LDAP / XPath
│   └── Protocol / CRLF / second-order
├── Browser Vulnerabilities
│   ├── XSS / CSP / Trusted Types
│   ├── CSRF / SameSite
│   └── CORS / XS-Leaks
├── Server-side Capabilities
│   ├── SSRF
│   ├── Path / Upload / Archive
│   └── Deserialization
├── HTTP Infrastructure
│   ├── Request Smuggling
│   ├── Cache Poisoning / Deception
│   ├── Proxy Trust / Parameter Pollution
│   └── Race Conditions
├── Modern API
│   ├── REST authorization
│   ├── Business flow / Resource budget
│   ├── Inventory / Third-party APIs
│   ├── GraphQL
│   └── WebSocket
└── AppSec Engineering
    ├── Misconfiguration
    ├── Supply Chain / SBOM / Secrets
    ├── Cryptographic Engineering
    ├── Logging / Alerting / Error Handling
    └── Code Review / SDL / Security Testing
```

## 最重要的五个抽象

1. **Trust Boundary**：数据或身份从低信任区域进入高信任区域时，必须重新验证。
2. **Code vs Data Separation**：Injection 的共同根因是数据被解释成代码/查询结构。
3. **Server-side Enforcement**：浏览器/UI 控制不能替代服务端认证与授权。
4. **Parser Consistency**：WAF、CDN、代理、框架和后端必须对同一输入形成一致语义。
5. **Security Invariant**：把“安全建议”写成系统任何状态下都必须成立、可自动验证的规则。


## 从漏洞树升级为能力树

真正适合中高级面试的知识结构，不应只按漏洞名称分类，还应按“安全能力”横向连接：

| 能力 | 典型问题 | 关键证据 |
|---|---|---|
| Identity | 登录、Session、OAuth、MFA | 认证状态机与令牌生命周期测试 |
| Authorization | BOLA/BFLA/BOPLA、多租户 | Subject×Action×Resource×Context 权限矩阵 |
| Interpreter Safety | SQL/NoSQL/Command/SSTI/XXE | Source→Sink 数据流与结构化 API |
| Browser Isolation | SOP/CORS/XSS/CSRF/CSP | Origin/Site/DOM context 测试 |
| Capability Control | SSRF、文件、反序列化 | egress、文件根、parser capability 限制 |
| Protocol Consistency | Smuggling、缓存、代理头 | 多组件端到端语义一致性测试 |
| Software Supply Chain | 依赖、构建、SBOM、Secrets | provenance、锁定、签名、轮换 |
| Detection & Response | 日志、告警、异常 | 事件生成→检测→响应演练 |

复习时应不断把某一道题映射回上述能力，而不是把 100 个答案当成互不相关的记忆单元。
