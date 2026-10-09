# 100 题总览

| 编号 | 章节 | 题目 | 难度 | PDF 页 |
|---:|---|---|---|---:|
| 001 | HTTP、浏览器与 Web 安全基础 | [Q001 HTTP 是无状态协议，为什么 Web 应用还能维持登录状态？](../questions/01-http-browser/Q001.md) | 基础-中级 | 8 |
| 002 | HTTP、浏览器与 Web 安全基础 | [Q002 Cookie 的 Secure、HttpOnly、SameSite 分别防什么？](../questions/01-http-browser/Q002.md) | 基础-中级 | 10 |
| 003 | HTTP、浏览器与 Web 安全基础 | [Q003 Same-Origin Policy 到底限制了什么？](../questions/01-http-browser/Q003.md) | 基础-中级 | 12 |
| 004 | HTTP、浏览器与 Web 安全基础 | [Q004 CORS 是浏览器的安全机制还是服务器的安全机制？](../questions/01-http-browser/Q004.md) | 中高级 | 14 |
| 005 | HTTP、浏览器与 Web 安全基础 | [Q005 认证 Authentication 和授权 Authorization 的区别是什么？](../questions/01-http-browser/Q005.md) | 基础-中级 | 16 |
| 006 | HTTP、浏览器与 Web 安全基础 | [Q006 URL 中哪些部分安全边界不同？](../questions/01-http-browser/Q006.md) | 基础-中级 | 18 |
| 007 | HTTP、浏览器与 Web 安全基础 | [Q007 为什么 HTTPS 不能解决所有 Web 安全问题？](../questions/01-http-browser/Q007.md) | 基础-中级 | 20 |
| 008 | HTTP、浏览器与 Web 安全基础 | [Q008 什么是 Trust Boundary？](../questions/01-http-browser/Q008.md) | 基础-中级 | 22 |
| 009 | HTTP、浏览器与 Web 安全基础 | [Q009 什么是攻击面 Attack Surface？](../questions/01-http-browser/Q009.md) | 基础-中级 | 24 |
| 010 | HTTP、浏览器与 Web 安全基础 | [Q010 漏洞、威胁、风险三个概念有什么区别？](../questions/01-http-browser/Q010.md) | 基础-中级 | 26 |
| 011 | 访问控制、越权与 IDOR/BOLA | [Q011 什么是 IDOR？它与 BOLA 的关系是什么？](../questions/02-access-control/Q011.md) | 基础-中级 | 28 |
| 012 | 访问控制、越权与 IDOR/BOLA | [Q012 把数据库 ID 换成 UUID 能解决 IDOR 吗？](../questions/02-access-control/Q012.md) | 基础-中级 | 30 |
| 013 | 访问控制、越权与 IDOR/BOLA | [Q013 水平越权和垂直越权分别是什么？](../questions/02-access-control/Q013.md) | 基础-中级 | 32 |
| 014 | 访问控制、越权与 IDOR/BOLA | [Q014 前端隐藏管理员按钮能否实现权限控制？](../questions/02-access-control/Q014.md) | 基础-中级 | 34 |
| 015 | 访问控制、越权与 IDOR/BOLA | [Q015 RBAC 和 ABAC 有什么区别？](../questions/02-access-control/Q015.md) | 中高级 | 36 |
| 016 | 访问控制、越权与 IDOR/BOLA | [Q016 为什么管理员接口单独放 /admin/* 还不够？](../questions/02-access-control/Q016.md) | 基础-中级 | 38 |
| 017 | 访问控制、越权与 IDOR/BOLA | [Q017 什么是 Broken Function Level Authorization？](../questions/02-access-control/Q017.md) | 基础-中级 | 40 |
| 018 | 访问控制、越权与 IDOR/BOLA | [Q018 什么是 Broken Object Property Level Authorization？](../questions/02-access-control/Q018.md) | 基础-中级 | 42 |
| 019 | 访问控制、越权与 IDOR/BOLA | [Q019 多租户 SaaS 应该怎样设计权限边界？](../questions/02-access-control/Q019.md) | 中高级 | 44 |
| 020 | 访问控制、越权与 IDOR/BOLA | [Q020 如何做访问控制的系统化安全测试？](../questions/02-access-control/Q020.md) | 基础-中级 | 46 |
| 021 | 认证、Session、JWT 与 OAuth | [Q021 为什么登录成功后要 rotate Session ID？](../questions/03-auth-session-oauth/Q021.md) | 基础-中级 | 48 |
| 022 | 认证、Session、JWT 与 OAuth | [Q022 Session Fixation 和 Session Hijacking 有什么区别？](../questions/03-auth-session-oauth/Q022.md) | 中高级 | 50 |
| 023 | 认证、Session、JWT 与 OAuth | [Q023 密码为什么不能直接 SHA-256 后保存？](../questions/03-auth-session-oauth/Q023.md) | 基础-中级 | 52 |
| 024 | 认证、Session、JWT 与 OAuth | [Q024 为什么登录接口不能只靠账户锁定抵抗爆破？](../questions/03-auth-session-oauth/Q024.md) | 基础-中级 | 54 |
| 025 | 认证、Session、JWT 与 OAuth | [Q025 JWT 最大的安全误区是什么？](../questions/03-auth-session-oauth/Q025.md) | 中高级 | 56 |
| 026 | 认证、Session、JWT 与 OAuth | [Q026 JWT 放 localStorage 还是 HttpOnly Cookie？](../questions/03-auth-session-oauth/Q026.md) | 中高级 | 58 |
| 027 | 认证、Session、JWT 与 OAuth | [Q027 Access Token 和 Refresh Token 为什么应该区分？](../questions/03-auth-session-oauth/Q027.md) | 基础-中级 | 60 |
| 028 | 认证、Session、JWT 与 OAuth | [Q028 OAuth 2.0 Authorization Code + PKCE 解决什么问题？](../questions/03-auth-session-oauth/Q028.md) | 进阶 | 62 |
| 029 | 认证、Session、JWT 与 OAuth | [Q029 OAuth redirect URI 为什么必须严格校验？](../questions/03-auth-session-oauth/Q029.md) | 进阶 | 64 |
| 030 | 认证、Session、JWT 与 OAuth | [Q030 为什么改密码、绑定 MFA 等高风险操作通常要求重新认证？](../questions/03-auth-session-oauth/Q030.md) | 基础-中级 | 66 |
| 031 | Injection 家族 | [Q031 SQL Injection 的根本原因是什么？](../questions/04-injection/Q031.md) | 基础-中级 | 68 |
| 032 | Injection 家族 | [Q032 参数化查询为什么可以阻止 SQL Injection？](../questions/04-injection/Q032.md) | 基础-中级 | 70 |
| 033 | Injection 家族 | [Q033 ORM 能不能自动消灭 SQL Injection？](../questions/04-injection/Q033.md) | 基础-中级 | 72 |
| 034 | Injection 家族 | [Q034 Blind SQL Injection 是什么？](../questions/04-injection/Q034.md) | 中高级 | 74 |
| 035 | Injection 家族 | [Q035 NoSQL Injection 为什么也存在？](../questions/04-injection/Q035.md) | 基础-中级 | 76 |
| 036 | Injection 家族 | [Q036 Command Injection 的根因是什么？](../questions/04-injection/Q036.md) | 基础-中级 | 78 |
| 037 | Injection 家族 | [Q037 SSTI 是什么？](../questions/04-injection/Q037.md) | 中高级 | 80 |
| 038 | Injection 家族 | [Q038 XXE 为什么不仅仅是读取本地文件？](../questions/04-injection/Q038.md) | 中高级 | 82 |
| 039 | Injection 家族 | [Q039 LDAP Injection / XPath Injection 与 SQLi 有何共同点？](../questions/04-injection/Q039.md) | 基础-中级 | 84 |
| 040 | Injection 家族 | [Q040 CRLF Injection / HTTP Response Splitting 是什么？](../questions/04-injection/Q040.md) | 基础-中级 | 86 |
| 041 | Injection 家族 | [Q041 为什么黑名单过滤 Injection 往往不可靠？](../questions/04-injection/Q041.md) | 基础-中级 | 88 |
| 042 | Injection 家族 | [Q042 什么是二阶 SQL Injection？](../questions/04-injection/Q042.md) | 基础-中级 | 90 |
| 043 | XSS、CSRF、CORS 与浏览器安全 | [Q043 Stored、Reflected、DOM XSS 有什么区别？](../questions/05-browser-security/Q043.md) | 基础-中级 | 92 |
| 044 | XSS、CSRF、CORS 与浏览器安全 | [Q044 为什么 XSS 不能靠统一 HTML Escape 完全解决？](../questions/05-browser-security/Q044.md) | 基础-中级 | 94 |
| 045 | XSS、CSRF、CORS 与浏览器安全 | [Q045 React/Vue 会不会天然消灭 XSS？](../questions/05-browser-security/Q045.md) | 基础-中级 | 96 |
| 046 | XSS、CSRF、CORS 与浏览器安全 | [Q046 innerHTML 和 textContent 的安全差异？](../questions/05-browser-security/Q046.md) | 基础-中级 | 98 |
| 047 | XSS、CSRF、CORS 与浏览器安全 | [Q047 CSP 能不能替代 XSS 修复？](../questions/05-browser-security/Q047.md) | 基础-中级 | 100 |
| 048 | XSS、CSRF、CORS 与浏览器安全 | [Q048 CSP nonce 有什么意义？](../questions/05-browser-security/Q048.md) | 进阶 | 102 |
| 049 | XSS、CSRF、CORS 与浏览器安全 | [Q049 什么是 Trusted Types？](../questions/05-browser-security/Q049.md) | 进阶 | 104 |
| 050 | XSS、CSRF、CORS 与浏览器安全 | [Q050 CSRF 的成立条件是什么？](../questions/05-browser-security/Q050.md) | 中高级 | 106 |
| 051 | XSS、CSRF、CORS 与浏览器安全 | [Q051 为什么 POST 请求不能防 CSRF？](../questions/05-browser-security/Q051.md) | 中高级 | 108 |
| 052 | XSS、CSRF、CORS 与浏览器安全 | [Q052 为什么 SameSite 不能完全替代 CSRF Token？](../questions/05-browser-security/Q052.md) | 中高级 | 110 |
| 053 | XSS、CSRF、CORS 与浏览器安全 | [Q053 CORS 中为什么 Credentials 与 Origin 校验是关键？](../questions/05-browser-security/Q053.md) | 中高级 | 112 |
| 054 | XSS、CSRF、CORS 与浏览器安全 | [Q054 什么是 XS-Leaks？](../questions/05-browser-security/Q054.md) | 进阶 | 114 |
| 055 | SSRF、文件、路径与反序列化 | [Q055 什么是 SSRF？](../questions/06-server-side/Q055.md) | 中高级 | 116 |
| 056 | SSRF、文件、路径与反序列化 | [Q056 SSRF 为什么不能仅检查字符串是否包含 127.0.0.1？](../questions/06-server-side/Q056.md) | 中高级 | 118 |
| 057 | SSRF、文件、路径与反序列化 | [Q057 云环境为什么特别重视 SSRF？](../questions/06-server-side/Q057.md) | 中高级 | 120 |
| 058 | SSRF、文件、路径与反序列化 | [Q058 Path Traversal 的根因是什么？](../questions/06-server-side/Q058.md) | 基础-中级 | 122 |
| 059 | SSRF、文件、路径与反序列化 | [Q059 文件上传应该检查扩展名、MIME 还是 magic bytes？](../questions/06-server-side/Q059.md) | 基础-中级 | 124 |
| 060 | SSRF、文件、路径与反序列化 | [Q060 为什么上传文件最好不要保存在 Web Root？](../questions/06-server-side/Q060.md) | 基础-中级 | 126 |
| 061 | SSRF、文件、路径与反序列化 | [Q061 什么是不安全反序列化？](../questions/06-server-side/Q061.md) | 进阶 | 128 |
| 062 | SSRF、文件、路径与反序列化 | [Q062 给序列化数据加签名能解决所有反序列化问题吗？](../questions/06-server-side/Q062.md) | 进阶 | 130 |
| 063 | SSRF、文件、路径与反序列化 | [Q063 什么是 LFI 和 RFI？](../questions/06-server-side/Q063.md) | 基础-中级 | 132 |
| 064 | SSRF、文件、路径与反序列化 | [Q064 Zip Slip 属于什么问题？](../questions/06-server-side/Q064.md) | 基础-中级 | 134 |
| 065 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q065 什么是 HTTP Request Smuggling？](../questions/07-http-infrastructure/Q065.md) | 进阶 | 136 |
| 066 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q066 为什么 Request Smuggling 属于协议解析差异问题？](../questions/07-http-infrastructure/Q066.md) | 进阶 | 138 |
| 067 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q067 HTTP/2 出现后 Request Smuggling 是否消失？](../questions/07-http-infrastructure/Q067.md) | 进阶 | 140 |
| 068 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q068 什么是 Web Cache Poisoning？](../questions/07-http-infrastructure/Q068.md) | 进阶 | 142 |
| 069 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q069 Web Cache Poisoning 和 Web Cache Deception 有什么区别？](../questions/07-http-infrastructure/Q069.md) | 进阶 | 144 |
| 070 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q070 什么是 Host Header Injection？](../questions/07-http-infrastructure/Q070.md) | 基础-中级 | 146 |
| 071 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q071 X-Forwarded-For 为什么经常产生安全问题？](../questions/07-http-infrastructure/Q071.md) | 基础-中级 | 148 |
| 072 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q072 什么是 HTTP Parameter Pollution？](../questions/07-http-infrastructure/Q072.md) | 进阶 | 150 |
| 073 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q073 CDN、WAF 和 Backend 为什么必须尽量统一规范化逻辑？](../questions/07-http-infrastructure/Q073.md) | 基础-中级 | 152 |
| 074 | HTTP 解析、反向代理、缓存与高级漏洞 | [Q074 Race Condition 为什么属于 Web 漏洞？](../questions/07-http-infrastructure/Q074.md) | 进阶 | 154 |
| 075 | REST API、GraphQL、WebSocket | [Q075 REST API 最容易犯的授权错误是什么？](../questions/08-api-graphql-websocket/Q075.md) | 基础-中级 | 156 |
| 076 | REST API、GraphQL、WebSocket | [Q076 什么是 Mass Assignment？](../questions/08-api-graphql-websocket/Q076.md) | 中高级 | 158 |
| 077 | REST API、GraphQL、WebSocket | [Q077 API Rate Limit 应该按 IP 还是按 User？](../questions/08-api-graphql-websocket/Q077.md) | 基础-中级 | 160 |
| 078 | REST API、GraphQL、WebSocket | [Q078 什么是 Unrestricted Access to Sensitive Business Flows？](../questions/08-api-graphql-websocket/Q078.md) | 基础-中级 | 162 |
| 079 | REST API、GraphQL、WebSocket | [Q079 为什么 API Inventory 是安全问题？](../questions/08-api-graphql-websocket/Q079.md) | 基础-中级 | 164 |
| 080 | REST API、GraphQL、WebSocket | [Q080 什么是 Unsafe Consumption of APIs？](../questions/08-api-graphql-websocket/Q080.md) | 基础-中级 | 166 |
| 081 | REST API、GraphQL、WebSocket | [Q081 GraphQL 为什么容易发生授权问题？](../questions/08-api-graphql-websocket/Q081.md) | 进阶 | 168 |
| 082 | REST API、GraphQL、WebSocket | [Q082 GraphQL 为什么需要 query complexity 限制？](../questions/08-api-graphql-websocket/Q082.md) | 进阶 | 170 |
| 083 | REST API、GraphQL、WebSocket | [Q083 WebSocket 握手认证后，还需要对每条消息授权吗？](../questions/08-api-graphql-websocket/Q083.md) | 中高级 | 172 |
| 084 | REST API、GraphQL、WebSocket | [Q084 什么是 Cross-Site WebSocket Hijacking？](../questions/08-api-graphql-websocket/Q084.md) | 中高级 | 174 |
| 085 | 配置、密码学、供应链、日志与异常处理 | [Q085 Security Misconfiguration 包括哪些问题？](../questions/09-config-supplychain-logging/Q085.md) | 基础-中级 | 176 |
| 086 | 配置、密码学、供应链、日志与异常处理 | [Q086 为什么 Dependency Vulnerability 不再只是“跑个 SCA”？](../questions/09-config-supplychain-logging/Q086.md) | 基础-中级 | 178 |
| 087 | 配置、密码学、供应链、日志与异常处理 | [Q087 SBOM 能解决供应链安全吗？](../questions/09-config-supplychain-logging/Q087.md) | 进阶 | 180 |
| 088 | 配置、密码学、供应链、日志与异常处理 | [Q088 为什么密码学漏洞往往是“使用错误”而不是算法被破解？](../questions/09-config-supplychain-logging/Q088.md) | 基础-中级 | 182 |
| 089 | 配置、密码学、供应链、日志与异常处理 | [Q089 为什么 secrets 不应该硬编码进 Git？](../questions/09-config-supplychain-logging/Q089.md) | 基础-中级 | 184 |
| 090 | 配置、密码学、供应链、日志与异常处理 | [Q090 Security Logging 应该记录什么？](../questions/09-config-supplychain-logging/Q090.md) | 基础-中级 | 186 |
| 091 | 配置、密码学、供应链、日志与异常处理 | [Q091 为什么只“记录日志”仍然属于 Logging & Alerting Failure？](../questions/09-config-supplychain-logging/Q091.md) | 基础-中级 | 188 |
| 092 | 配置、密码学、供应链、日志与异常处理 | [Q092 为什么异常处理在 OWASP 2025 中单独成为 A10？](../questions/09-config-supplychain-logging/Q092.md) | 进阶 | 190 |
| 093 | 代码审计、SDL 与综合架构设计 | [Q093 给你一个陌生 Web 项目，代码审计第一小时看什么？](../questions/10-code-review-sdl/Q093.md) | 基础-中级 | 192 |
| 094 | 代码审计、SDL 与综合架构设计 | [Q094 如何系统审计 SQL Injection，而不是只搜索 SQL 字符串？](../questions/10-code-review-sdl/Q094.md) | 基础-中级 | 194 |
| 095 | 代码审计、SDL 与综合架构设计 | [Q095 如何审计整个项目里的 Access Control？](../questions/10-code-review-sdl/Q095.md) | 基础-中级 | 196 |
| 096 | 代码审计、SDL 与综合架构设计 | [Q096 一个系统已经有 WAF，为什么仍然需要修代码？](../questions/10-code-review-sdl/Q096.md) | 基础-中级 | 198 |
| 097 | 代码审计、SDL 与综合架构设计 | [Q097 如何给一个 Web 漏洞排修复优先级？](../questions/10-code-review-sdl/Q097.md) | 基础-中级 | 200 |
| 098 | 代码审计、SDL 与综合架构设计 | [Q098 如何设计一套 Web Security Testing Pipeline？](../questions/10-code-review-sdl/Q098.md) | 基础-中级 | 202 |
| 099 | 代码审计、SDL 与综合架构设计 | [Q099 SAST、DAST、IAST、SCA 分别解决什么？](../questions/10-code-review-sdl/Q099.md) | 基础-中级 | 204 |
| 100 | 代码审计、SDL 与综合架构设计 | [Q100 设计一个“默认安全”的 Web 系统，你会抓哪十条原则？](../questions/10-code-review-sdl/Q100.md) | 基础-中级 | 206 |
