# 100 题总索引

| ID | 题目 | 章节 | 难度 | 岗位 | Framework | PDF 页 |
|---|---|---:|---:|---|---|---:|
| [Q01](../questions/01-network-protocols/q01-network-fundamentals.md) | OSI 七层模型与 TCP/IP 模型分别是什么？安全设备工作在哪一层？ | 1 | 2/5 | 安全研发 / 蓝队 / 渗透 | Network Fundamentals | 6 |
| [Q02](../questions/01-network-protocols/q02-tcp-ip.md) | TCP 为什么三次握手，而不是两次？ | 1 | 2/5 | 全岗位 | TCP/IP | 7 |
| [Q03](../questions/01-network-protocols/q03-tcp-ip.md) | TCP 如何保证可靠传输？ | 1 | 2/5 | 全岗位 | TCP/IP | 8 |
| [Q04](../questions/01-network-protocols/q04-tcp-udp-quic.md) | TCP 与 UDP 的区别？为什么 DNS、QUIC 等会使用 UDP？ | 1 | 2/5 | 全岗位 | TCP/UDP/QUIC | 9 |
| [Q05](../questions/01-network-protocols/q05-dns.md) | DNS 完整解析过程是什么？DNS 有哪些安全问题？ | 1 | 3/5 | 渗透 / 蓝队 / 云安全 | DNS | 10 |
| [Q06](../questions/01-network-protocols/q06-http.md) | HTTP/1.1、HTTP/2、HTTP/3 的主要区别，以及安全影响是什么？ | 1 | 3/5 | 安全研发 / AppSec / 蓝队 | HTTP | 11 |
| [Q07](../questions/01-network-protocols/q07-end-to-end-web-request.md) | 从输入 https://example.com 到页面出现，中间发生了什么？ | 1 | 3/5 | 全岗位 | 综合网络栈 | 12 |
| [Q08](../questions/01-network-protocols/q08-tls.md) | HTTP 与 HTTPS 的区别是什么？ | 1 | 2/5 | 全岗位 | TLS | 13 |
| [Q09](../questions/01-network-protocols/q09-edge-architecture.md) | CDN、反向代理、Load Balancer、WAF 分别解决什么问题？ | 1 | 3/5 | AppSec / 蓝队 / 架构 | Edge Architecture | 14 |
| [Q10](../questions/01-network-protocols/q10-lan-security.md) | ARP 的工作原理是什么？ARP 欺骗为什么成立？ | 1 | 2/5 | 网络安全 / 蓝队 | LAN Security | 15 |
| [Q11](../questions/02-web-security/q11-owasp-wstg-asvs.md) | 给你一个 Web 系统，你的安全测试总体思路是什么？ | 2 | 3/5 | 渗透 / AppSec | OWASP WSTG / ASVS | 17 |
| [Q12](../questions/02-web-security/q12-owasp-a05-injection.md) | SQL 注入的本质是什么？ | 2 | 2/5 | 渗透 / AppSec / 安全研发 | OWASP A05 Injection | 18 |
| [Q13](../questions/02-web-security/q13-owasp-a05-asvs.md) | 使用 Prepared Statement 后是否绝对没有 SQL 注入？ | 2 | 4/5 | AppSec / 安全研发 | OWASP A05 / ASVS | 19 |
| [Q14](../questions/02-web-security/q14-owasp-injection-browser-security.md) | XSS 的本质与三种主要类型是什么？ | 2 | 2/5 | 渗透 / AppSec / 前端安全 | OWASP Injection / Browser Security | 20 |
| [Q15](../questions/02-web-security/q15-csp-defense-in-depth.md) | CSP 能不能彻底解决 XSS？ | 2 | 3/5 | AppSec / 前端安全 | CSP / Defense in Depth | 21 |
| [Q16](../questions/02-web-security/q16-owasp-a01-browser-security.md) | CSRF 的本质是什么？如何修复？ | 2 | 2/5 | 渗透 / AppSec | OWASP A01 / Browser Security | 22 |
| [Q17](../questions/02-web-security/q17-owasp-a01-2025-api7-2023.md) | SSRF 的本质是什么？ | 2 | 3/5 | AppSec / 云安全 / 渗透 | OWASP A01 2025 / API7:2023 | 23 |
| [Q18](../questions/02-web-security/q18-ssrf-defense.md) | SSRF 为什么不能只过滤 127.0.0.1？ | 2 | 4/5 | AppSec / 云安全 | SSRF Defense | 24 |
| [Q19](../questions/02-web-security/q19-xml-parser-security.md) | XXE 是什么？为什么现代环境中出现得比以前少？ | 2 | 3/5 | AppSec / 安全研发 | XML Parser Security | 25 |
| [Q20](../questions/02-web-security/q20-file-handling.md) | 文件上传漏洞应该如何分析？ | 2 | 3/5 | AppSec / 渗透 / 安全研发 | File Handling | 26 |
| [Q21](../questions/03-api-identity/q21-file-path-security.md) | Path Traversal 与 File Inclusion 有什么区别？ | 3 | 3/5 | AppSec / 渗透 | File Path Security | 28 |
| [Q22](../questions/03-api-identity/q22-owasp-injection-asvs.md) | OS Command Injection 的本质是什么？ | 3 | 3/5 | AppSec / 安全研发 | OWASP Injection / ASVS | 29 |
| [Q23](../questions/03-api-identity/q23-serialization-security.md) | 什么是反序列化漏洞？ | 3 | 4/5 | AppSec / Java安全 / 安全研发 | Serialization Security | 30 |
| [Q24](../questions/03-api-identity/q24-http-parser-differential.md) | Request Smuggling / HTTP Desync 的本质是什么？ | 3 | 5/5 | AppSec / 协议安全 / 架构 | HTTP Parser Differential | 31 |
| [Q25](../questions/03-api-identity/q25-owasp-api1-bola-a01.md) | 什么是 IDOR / BOLA？为什么它如此常见？ | 3 | 3/5 | AppSec / API安全 | OWASP API1 BOLA / A01 | 32 |
| [Q26](../questions/03-api-identity/q26-access-control.md) | 水平越权、垂直越权、未授权访问分别是什么？ | 3 | 2/5 | AppSec / API安全 | Access Control | 33 |
| [Q27](../questions/03-api-identity/q27-jwt-jose.md) | JWT 是什么？最常见的设计错误有哪些？ | 3 | 3/5 | AppSec / 后端 / 身份安全 | JWT / JOSE | 34 |
| [Q28](../questions/03-api-identity/q28-web-identity.md) | Cookie、Session、JWT 的区别是什么？ | 3 | 3/5 | AppSec / 后端 | Web Identity | 35 |
| [Q29](../questions/03-api-identity/q29-oauth2-oidc.md) | OAuth 2.0 与 OpenID Connect 有什么区别？ | 3 | 4/5 | AppSec / 身份 / 云安全 | OAuth2 / OIDC | 36 |
| [Q30](../questions/03-api-identity/q30-browser-security.md) | CORS 与 Same-Origin Policy 的关系是什么？ | 3 | 3/5 | AppSec / 前端 / API安全 | Browser Security | 37 |
| [Q31](../questions/04-host-middleware/q31-host-ir.md) | Linux 主机疑似入侵，你第一时间看什么？ | 4 | 4/5 | 蓝队 / 应急响应 / 安全运维 | Host IR | 39 |
| [Q32](../questions/04-host-middleware/q32-windows-telemetry.md) | Windows 主机应重点关注哪些日志？ | 4 | 3/5 | 蓝队 / 应急响应 | Windows Telemetry | 40 |
| [Q33](../questions/04-host-middleware/q33-process-analysis.md) | 如何判断一个异常进程是否值得调查？ | 4 | 3/5 | 蓝队 / EDR | Process Analysis | 41 |
| [Q34](../questions/04-host-middleware/q34-mitre-att-and-ck-persistence.md) | 什么是 Persistence？蓝队如何理解它？ | 4 | 3/5 | 蓝队 / 安全运营 | MITRE ATT&CK Persistence | 42 |
| [Q35](../questions/04-host-middleware/q35-privilege-boundary.md) | Linux/Windows 提权问题应该怎样回答才专业？ | 4 | 4/5 | 渗透 / 蓝队 / 主机安全 | Privilege Boundary | 43 |
| [Q36](../questions/04-host-middleware/q36-java-enterprise.md) | Java 中间件安全为什么长期是面试重点？ | 4 | 4/5 | AppSec / Java安全 | Java Enterprise | 44 |
| [Q37](../questions/04-host-middleware/q37-service-exposure.md) | Redis 未授权访问为什么危险？正确修复方式是什么？ | 4 | 3/5 | 安全运维 / 云安全 / AppSec | Service Exposure | 45 |
| [Q38](../questions/04-host-middleware/q38-webshell-detection.md) | WebShell 检测有哪些思路？ | 4 | 4/5 | 蓝队 / 应急响应 / AppSec | WebShell Detection | 46 |
| [Q39](../questions/04-host-middleware/q39-security-controls.md) | IDS、IPS、EDR、NDR、WAF 有什么区别？ | 4 | 3/5 | 蓝队 / 安全架构 | Security Controls | 47 |
| [Q40](../questions/04-host-middleware/q40-hardening-baseline.md) | 主机安全基线应该包含什么？ | 4 | 3/5 | 安全运维 / 蓝队 | Hardening Baseline | 48 |
| [Q41](../questions/05-enterprise-identity/q41-kerberos.md) | Kerberos 的基本认证流程是什么？ | 5 | 4/5 | 企业安全 / 蓝队 / 身份 | Kerberos | 50 |
| [Q42](../questions/05-enterprise-identity/q42-windows-authentication.md) | NTLM 与 Kerberos 有什么区别？ | 5 | 4/5 | 企业安全 / 身份 | Windows Authentication | 51 |
| [Q43](../questions/05-enterprise-identity/q43-mitre-credential-access.md) | 为什么 Credential Access 是企业攻击的重要阶段？ | 5 | 4/5 | 蓝队 / 企业安全 | MITRE Credential Access | 52 |
| [Q44](../questions/05-enterprise-identity/q44-mitre-lateral-movement.md) | 什么是 Lateral Movement？ | 5 | 3/5 | 蓝队 / 企业安全 | MITRE Lateral Movement | 53 |
| [Q45](../questions/05-enterprise-identity/q45-nist-sp-800-207.md) | 网络分区和 Zero Trust 有什么区别？ | 5 | 4/5 | 安全架构 / 云安全 | NIST SP 800-207 | 54 |
| [Q46](../questions/05-enterprise-identity/q46-authorization.md) | 什么是 Least Privilege？ | 5 | 2/5 | 全岗位 | Authorization | 55 |
| [Q47](../questions/05-enterprise-identity/q47-identity-incident.md) | 如果域管理员账号疑似泄露，你怎么处理？ | 5 | 5/5 | 蓝队 / 应急响应 | Identity Incident | 56 |
| [Q48](../questions/05-enterprise-identity/q48-asset-management.md) | 企业内部资产发现为什么重要？ | 5 | 3/5 | 安全运营 / 云安全 | Asset Management | 57 |
| [Q49](../questions/05-enterprise-identity/q49-secrets-management.md) | Secrets 应该如何管理？ | 5 | 3/5 | 安全研发 / 云安全 / DevSecOps | Secrets Management | 58 |
| [Q50](../questions/05-enterprise-identity/q50-machine-identity-pki.md) | 为什么企业现在越来越需要关注证书身份安全？ | 5 | 5/5 | 身份 / 云安全 / 架构 | Machine Identity / PKI | 59 |
| [Q51](../questions/06-appsec-supply-chain/q51-appsec-tooling.md) | SAST、DAST、IAST、SCA 有什么区别？ | 6 | 3/5 | AppSec / 安全研发 | AppSec Tooling | 61 |
| [Q52](../questions/06-appsec-supply-chain/q52-static-analysis.md) | 什么是 Taint Analysis？ | 6 | 4/5 | AppSec / 安全研发 | Static Analysis | 62 |
| [Q53](../questions/06-appsec-supply-chain/q53-owasp-injection.md) | 做 SQL 注入代码审计时，你会怎么看？ | 6 | 4/5 | AppSec / Code Review | OWASP Injection | 63 |
| [Q54](../questions/06-appsec-supply-chain/q54-serialization-review.md) | Java 反序列化代码审计应该关注什么？ | 6 | 5/5 | Java安全 / AppSec | Serialization Review | 64 |
| [Q55](../questions/06-appsec-supply-chain/q55-owasp-a03-2025.md) | 软件供应链攻击是什么？ | 6 | 4/5 | AppSec / DevSecOps / 架构 | OWASP A03:2025 | 65 |
| [Q56](../questions/06-appsec-supply-chain/q56-sbom.md) | 什么是 SBOM？SBOM 能解决所有供应链问题吗？ | 6 | 3/5 | DevSecOps / AppSec | SBOM | 66 |
| [Q57](../questions/06-appsec-supply-chain/q57-secrets-incident.md) | Git 仓库泄露密钥为什么严重？ | 6 | 3/5 | DevSecOps / 安全研发 | Secrets Incident | 67 |
| [Q58](../questions/06-appsec-supply-chain/q58-ci-cd-security.md) | CI/CD Pipeline 有哪些典型安全风险？ | 6 | 4/5 | DevSecOps / 云安全 | CI/CD Security | 68 |
| [Q59](../questions/06-appsec-supply-chain/q59-root-cause-analysis.md) | 为什么安全研究员喜欢分析补丁 diff？ | 6 | 4/5 | 漏洞研究 / AppSec | Root Cause Analysis | 69 |
| [Q60](../questions/06-appsec-supply-chain/q60-memory-safety.md) | Buffer Overflow 的本质和现代防护是什么？ | 6 | 4/5 | 系统安全 / 安全研发 | Memory Safety | 70 |
| [Q61](../questions/07-blue-team-ir/q61-soc-triage.md) | 收到一个 SIEM 高危告警，你怎么处理？ | 7 | 4/5 | SOC / 蓝队 | SOC Triage | 72 |
| [Q62](../questions/07-blue-team-ir/q62-detection-concepts.md) | IOC、IOA、TTP 有什么区别？ | 7 | 3/5 | 蓝队 / Threat Hunting | Detection Concepts | 73 |
| [Q63](../questions/07-blue-team-ir/q63-siem-architecture.md) | SIEM 的基本数据链路是什么？ | 7 | 3/5 | SOC / 安全平台 | SIEM Architecture | 74 |
| [Q64](../questions/07-blue-team-ir/q64-nist-sp-800-61r3-csf-2-0.md) | Incident Response 的核心阶段是什么？ | 7 | 3/5 | 蓝队 / 应急响应 / 管理 | NIST SP 800-61r3 / CSF 2.0 | 75 |
| [Q65](../questions/07-blue-team-ir/q65-ransomware-ir.md) | 公司遭遇勒索事件，第一小时你做什么？ | 7 | 5/5 | 应急响应 / 蓝队 / 管理 | Ransomware IR | 76 |
| [Q66](../questions/07-blue-team-ir/q66-timeline-analysis.md) | Web 服务器疑似被入侵，你如何构建时间线？ | 7 | 4/5 | 蓝队 / AppSec / IR | Timeline Analysis | 77 |
| [Q67](../questions/07-blue-team-ir/q67-phishing-triage.md) | 钓鱼邮件告警如何分析？ | 7 | 4/5 | SOC / 邮件安全 / IR | Phishing Triage | 78 |
| [Q68](../questions/07-blue-team-ir/q68-cisa-kev-risk.md) | 漏洞优先级应该只看 CVSS 吗？ | 7 | 4/5 | 漏洞管理 / 安全平台 | CISA KEV / Risk | 79 |
| [Q69](../questions/07-blue-team-ir/q69-telemetry-strategy.md) | 什么日志最有价值？ | 7 | 4/5 | 蓝队 / 安全架构 | Telemetry Strategy | 80 |
| [Q70](../questions/07-blue-team-ir/q70-mitre-att-and-ck.md) | MITRE ATT&CK 在蓝队中怎么使用？ | 7 | 4/5 | 蓝队 / Threat Hunting / Purple Team | MITRE ATT&CK | 81 |
| [Q71](../questions/08-cloud-native/q71-cloud-security.md) | 什么是 Cloud Shared Responsibility Model？ | 8 | 3/5 | 云安全 / 架构 | Cloud Security | 83 |
| [Q72](../questions/08-cloud-native/q72-cloud-iam.md) | Cloud IAM 为什么是云安全最重要的领域之一？ | 8 | 4/5 | 云安全 / 身份 | Cloud IAM | 84 |
| [Q73](../questions/08-cloud-native/q73-object-storage.md) | 对象存储桶公开访问问题应该怎样治理？ | 8 | 3/5 | 云安全 | Object Storage | 85 |
| [Q74](../questions/08-cloud-native/q74-ssrf-cloud-identity.md) | 云环境 SSRF 为什么尤其值得关注？ | 8 | 4/5 | 云安全 / AppSec | SSRF + Cloud Identity | 86 |
| [Q75](../questions/08-cloud-native/q75-container-security.md) | Container 和 VM 的安全边界有什么不同？ | 8 | 3/5 | 云安全 / K8s | Container Security | 87 |
| [Q76](../questions/08-cloud-native/q76-kubernetes.md) | Kubernetes 最常见的安全风险有哪些？ | 8 | 4/5 | K8s / 云安全 / DevSecOps | Kubernetes | 88 |
| [Q77](../questions/08-cloud-native/q77-image-supply-chain.md) | Container Image 安全怎么做？ | 8 | 3/5 | DevSecOps / 云安全 | Image Supply Chain | 89 |
| [Q78](../questions/08-cloud-native/q78-iac-policy-as-code.md) | IaC 为什么有利于安全？ | 8 | 3/5 | DevSecOps / 云安全 | IaC / Policy as Code | 90 |
| [Q79](../questions/08-cloud-native/q79-serverless-security.md) | Serverless 是否意味着“不需要做服务器安全”？ | 8 | 3/5 | 云安全 / AppSec | Serverless Security | 91 |
| [Q80](../questions/08-cloud-native/q80-cloud-ir.md) | Cloud Incident Response 与传统机房 IR 最大差异是什么？ | 8 | 4/5 | 云安全 / IR | Cloud IR | 92 |
| [Q81](../questions/09-crypto-architecture/q81-cryptography-basics.md) | 对称加密和非对称加密有什么区别？ | 9 | 2/5 | 全岗位 | Cryptography Basics | 94 |
| [Q82](../questions/09-crypto-architecture/q82-crypto-basics.md) | Hash、Encryption、Encoding 有什么区别？ | 9 | 2/5 | 全岗位 | Crypto Basics | 95 |
| [Q83](../questions/09-crypto-architecture/q83-password-storage.md) | 密码应该怎么存？ | 9 | 3/5 | 安全研发 / AppSec | Password Storage | 96 |
| [Q84](../questions/09-crypto-architecture/q84-tls-1-3.md) | TLS 1.3 握手过程中解决了什么问题？ | 9 | 4/5 | 安全研发 / 网络 / 云安全 | TLS 1.3 | 97 |
| [Q85](../questions/09-crypto-architecture/q85-pki.md) | 如何保证你拿到的公钥确实属于目标网站？ | 9 | 4/5 | 网络 / 安全研发 | PKI | 98 |
| [Q86](../questions/09-crypto-architecture/q86-mtls.md) | mTLS 和普通 TLS 有什么区别？ | 9 | 3/5 | 云安全 / 微服务 / 身份 | mTLS | 99 |
| [Q87](../questions/09-crypto-architecture/q87-crypto-construction.md) | IV、Nonce 为什么经常是密码学实现漏洞来源？ | 9 | 4/5 | 安全研发 / 密码学 | Crypto Construction | 100 |
| [Q88](../questions/09-crypto-architecture/q88-kms-data-security.md) | Encryption at Rest 做了以后数据是不是安全了？ | 9 | 3/5 | 云安全 / 数据安全 | KMS / Data Security | 101 |
| [Q89](../questions/09-crypto-architecture/q89-nist-sp-800-207.md) | 什么是 Zero Trust？最常见的错误理解是什么？ | 9 | 4/5 | 安全架构 / 身份 / 云安全 | NIST SP 800-207 | 102 |
| [Q90](../questions/09-crypto-architecture/q90-nist-csf-2-0.md) | NIST CSF 2.0 六大 Function 是什么？ | 9 | 4/5 | 安全治理 / 架构 | NIST CSF 2.0 | 103 |
| [Q91](../questions/10-system-design/q91-authentication-surface.md) | 如果目标只有一个登录页面，你会怎么评估安全性？ | 10 | 5/5 | AppSec / 渗透 / 架构 | Authentication Surface | 105 |
| [Q92](../questions/10-system-design/q92-account-recovery.md) | 让你设计“忘记密码”功能，如何确保安全？ | 10 | 5/5 | AppSec / 身份 / 安全研发 | Account Recovery | 106 |
| [Q93](../questions/10-system-design/q93-api-security.md) | 设计一个 API Gateway 安全体系，你会考虑什么？ | 10 | 5/5 | AppSec / 架构 / 云安全 | API Security | 107 |
| [Q94](../questions/10-system-design/q94-secure-upload-architecture.md) | 设计一个安全文件上传系统。 | 10 | 5/5 | AppSec / 架构 | Secure Upload Architecture | 108 |
| [Q95](../questions/10-system-design/q95-nist-ssdf-secure-sdlc.md) | 你如何把安全加入 SDLC？ | 10 | 5/5 | AppSec / 安全研发 / 管理 | NIST SSDF / Secure SDLC | 109 |
| [Q96](../questions/10-system-design/q96-risk-based-vm.md) | 如果让你设计企业漏洞管理平台，你怎么设计？ | 10 | 5/5 | 安全平台 / 漏洞管理 | Risk-based VM | 110 |
| [Q97](../questions/10-system-design/q97-python-data-processing.md) | 面试现场让你写一个日志分析脚本，重点考什么？ | 10 | 4/5 | 安全研发 / 蓝队 | Python / Data Processing | 111 |
| [Q98](../questions/10-system-design/q98-postmortem.md) | 安全事故复盘应该包含什么？ | 10 | 4/5 | 蓝队 / 管理 / SRE | Postmortem | 112 |
| [Q99](../questions/10-system-design/q99-behavioral-technical.md) | “讲一个你发现过的漏洞/安全问题”应该怎么回答？ | 10 | 5/5 | 全岗位 | Behavioral + Technical | 113 |
| [Q100](../questions/10-system-design/q100-security-program-csf-2-0.md) | 终极综合题：你入职一家 3000 人互联网公司负责安全，前 30 天做什么？ | 10 | 5/5 | 安全负责人 / 架构 / 高级工程师 | Security Program / CSF 2.0 | 114 |
