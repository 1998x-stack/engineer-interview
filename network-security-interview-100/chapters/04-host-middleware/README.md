# 第 4 章：Linux、Windows、主机与中间件安全

> 主机不是命令集合，而是进程、身份、网络、持久化与证据的系统

**关键词：** Linux/Windows IR / EDR/NDR/WAF / 中间件 / WebShell / 安全基线

## 本章学习目标

- 考察主机调查、证据意识、进程/身份/网络关联能力，以及对中间件与配置风险的理解。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- 主机角色是什么？
- 哪些证据易失、应先保全？
- 异常行为如何与身份和网络关联？
- 处置动作会不会破坏证据或业务？

## 题目索引

- [Q31 Linux 主机疑似入侵，你第一时间看什么？](../../questions/04-host-middleware/q31-host-ir.md) - 难度 4/5 - Host IR
- [Q32 Windows 主机应重点关注哪些日志？](../../questions/04-host-middleware/q32-windows-telemetry.md) - 难度 3/5 - Windows Telemetry
- [Q33 如何判断一个异常进程是否值得调查？](../../questions/04-host-middleware/q33-process-analysis.md) - 难度 3/5 - Process Analysis
- [Q34 什么是 Persistence？蓝队如何理解它？](../../questions/04-host-middleware/q34-mitre-att-and-ck-persistence.md) - 难度 3/5 - MITRE ATT&CK Persistence
- [Q35 Linux/Windows 提权问题应该怎样回答才专业？](../../questions/04-host-middleware/q35-privilege-boundary.md) - 难度 4/5 - Privilege Boundary
- [Q36 Java 中间件安全为什么长期是面试重点？](../../questions/04-host-middleware/q36-java-enterprise.md) - 难度 4/5 - Java Enterprise
- [Q37 Redis 未授权访问为什么危险？正确修复方式是什么？](../../questions/04-host-middleware/q37-service-exposure.md) - 难度 3/5 - Service Exposure
- [Q38 WebShell 检测有哪些思路？](../../questions/04-host-middleware/q38-webshell-detection.md) - 难度 4/5 - WebShell Detection
- [Q39 IDS、IPS、EDR、NDR、WAF 有什么区别？](../../questions/04-host-middleware/q39-security-controls.md) - 难度 3/5 - Security Controls
- [Q40 主机安全基线应该包含什么？](../../questions/04-host-middleware/q40-hardening-baseline.md) - 难度 3/5 - Hardening Baseline

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q31](../../questions/04-host-middleware/q31-host-ir.md) | 事件调查需要围绕易失证据、范围和持续活动建立时间线。 | 预置 telemetry、playbook、隔离与可信取证。 | process/network/auth/persistence/file/app。 |
| [Q32](../../questions/04-host-middleware/q32-windows-telemetry.md) | Windows 行为需要多日志语义关联。 | Advanced Audit + PowerShell + EDR + 集中转发。 | Security/System/PowerShell/EDR/IdP。 |
| [Q33](../../questions/04-host-middleware/q33-process-analysis.md) | 进程风险来自行为与上下文组合。 | 行为关联 + 基线 + 处置审批。 | lineage/command/network/file/prevalence。 |
| [Q34](../../questions/04-host-middleware/q34-mitre-att-and-ck-persistence.md) | 对手建立可持续访问能力。 | 变更审计 + 高权限治理 + 多面 hunting。 | startup/account/key/config lifecycle。 |
| [Q35](../../questions/04-host-middleware/q35-privilege-boundary.md) | 错误信任、配置、凭据或漏洞使主体跨越权限边界。 | 最小权限 + 配置治理 + JIT/PAM + secret 隔离。 | token/UID、privileged process、ACL/group changes。 |
| [Q36](../../questions/04-host-middleware/q36-java-enterprise.md) | 复杂框架能力让不可信输入可能到达高影响 sink。 | 依赖/功能最小化 + 管理面隔离 + 进程最小权限。 | SBOM/runtime/admin/JVM/EDR。 |
| [Q37](../../questions/04-host-middleware/q37-service-exposure.md) | 高能力数据服务被错误暴露或缺乏身份控制。 | 无公网 + ACL/身份 + 最小权限 + inventory。 | flow/auth/config audit。 |
| [Q38](../../questions/04-host-middleware/q38-webshell-detection.md) | Web 入口导致异常代码/行为驻留或执行。 | 最小进程权限 + FIM + EDR 行为关联。 | HTTP→process→file/network chain。 |
| [Q39](../../questions/04-host-middleware/q39-security-controls.md) | 不同控制在不同位置观察/阻断不同语义。 | use-case driven layered telemetry + health monitoring。 | network/app/endpoint/identity 多源。 |
| [Q40](../../questions/04-host-middleware/q40-hardening-baseline.md) | 缺乏统一最小安全状态导致攻击面和配置漂移。 | role-based baseline + automation + exception governance。 | compliance/drift/coverage/backup test。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
