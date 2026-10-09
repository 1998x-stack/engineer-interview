---
id: Q25
title: "什么是 IDOR / BOLA？为什么它如此常见？"
chapter: 3
difficulty: 3
roles: "AppSec / API安全"
framework: "OWASP API1 BOLA / A01"
pdf_page: 32
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q24](q24-http-parser-differential.md) | [章节首页](../../chapters/03-api-identity/README.md) | [Q26](q26-access-control.md) →

# Q25 · 什么是 IDOR / BOLA？为什么它如此常见？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 3/5 |
| 适用岗位 | AppSec / API安全 |
| Framework / 对标 | OWASP API1 BOLA / A01 |
| PDF 页码 | 第 32 页 |
| 所属章节 | 第 3 章 · 高级 Web、API 与身份安全 |

## 面试官为什么问这题

判断候选人是否从“漏洞点”升级到浏览器安全模型、对象级授权、会话与联合身份的系统视角。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- 谁是主体？访问哪个对象/能力？
- 认证完成后授权在哪里执行？
- Token/Cookie 的生命周期和绑定关系是什么？
- 浏览器、Gateway 与后端分别承担什么安全责任？

## 30 秒回答

**一句话结论：** Authentication 证明“你是谁”；Authorization 决定“你能碰哪个对象、做什么动作”。

展开时优先抓住以下三点：

1. 用户已登录不等于有权访问任意对象。
1. 每个使用用户可控 ID 访问数据的功能都必须做 object-level authorization。
1. 前端隐藏、随机 ID、UUID 都不是授权。

## 2-3 分钟标准回答

首先，用户已登录不等于有权访问任意对象。
其次，每个使用用户可控 ID 访问数据的功能都必须做 object-level authorization。
API 天然大量暴露对象标识符，因此 BOLA 是 API 安全最高频问题之一。真正的修复应把“当前主体是否可对目标对象执行该动作”作为数据访问条件的一部分。
最好在 domain/service/repository 层形成统一授权策略，避免每个 Controller 手写 if 造成遗漏。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- 用户已登录不等于有权访问任意对象。
- 每个使用用户可控 ID 访问数据的功能都必须做 object-level authorization。
- 前端隐藏、随机 ID、UUID 都不是授权。

### 02 · 面试答题主线

1. 用户已登录不等于有权访问任意对象。
2. 每个使用用户可控 ID 访问数据的功能都必须做 object-level authorization。
3. 前端隐藏、随机 ID、UUID 都不是授权。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

API 天然大量暴露对象标识符，因此 BOLA 是 API 安全最高频问题之一。真正的修复应把“当前主体是否可对目标对象执行该动作”作为数据访问条件的一部分。

最好在 domain/service/repository 层形成统一授权策略，避免每个 Controller 手写 if 造成遗漏。

### 04 · 高频追问

- UUID 能否防止 BOLA？
- GraphQL 如何做对象级授权？

### 05 · 易错点

- 把不可猜 ID 当授权。
- 只在前端做权限控制。

### 06 · 工程实践

- 为每个资源定义 owner/tenant/role policy。
- 编写跨用户/跨租户的授权回归测试。

### 07 · 一句话记忆

> Authentication 证明“你是谁”；Authorization 决定“你能碰哪个对象、做什么动作”。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

IDOR/BOLA 的根因是服务端缺少对象级授权，不是 ID 是否容易猜。

最可靠的做法是每次对象访问都用当前主体+对象+动作做授权决策。

### 2. 边界条件与面试高分点

- **先定义边界**：明确主体、资产、数据/状态和信任边界，避免把问题描述成绝对结论。
- **区分根治与纵深**：根治方案应消除不安全的数据流、权限或协议状态；WAF、告警、限流等通常属于补充控制。
- **考虑失败模式**：不仅说明正常路径，还要考虑配置漂移、解析差异、权限过宽、依赖升级和异常条件。
- **给验证方式**：安全设计必须能被单元测试、集成测试、审计日志、检测规则或演练验证。

### 3. 工程化检查清单

- [ ] 认证与授权明确分离
- [ ] 对象级授权靠后端业务上下文完成
- [ ] Token 最小权限、短生命周期、严格受众/签发方校验
- [ ] 浏览器策略作为边界的一部分但不替代服务端控制
- [ ] 为每个资源定义 owner/tenant/role policy。
- [ ] 编写跨用户/跨租户的授权回归测试。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- IdP/认证日志
- API Gateway/应用访问日志
- 对象级授权拒绝事件
- Session/Token 生命周期事件

### 5. 追问怎么接

#### 追问：UUID 能否防止 BOLA？

**回答要点：** 先给一句话结论，再用本题的核心原理解释边界条件；最后补充检测/修复/验证三个工程点。

#### 追问：GraphQL 如何做对象级授权？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 OWASP API1 BOLA / A01 的边界，而不是只相信配置名称？
- 如果修复会影响兼容性或业务性能，你会如何设计灰度、监控和回滚方案？

### 7. 常见回答层级

| 层级 | 表现 |
|---|---|
| 1/5 | 只能给出名词定义 |
| 2/5 | 能解释基本原理 |
| 3/5 | 能说明成立条件、边界和真实影响 |
| 4/5 | 能给出工程修复、检测和验证 |
| 5/5 | 能处理复杂追问、权衡与系统设计 |

<!-- BEGIN PROFESSIONAL_V2 -->
## 专业深化 v2：面向高级工程师的题解

> 这一节是在 PDF 基线与第一轮扩展之上的第二层深化，重点补齐 **机制、边界、工程决策、证据、验证与追问树**。它不是利用手册，而是面向合法授权的安全工程与面试表达。

### A. 机制模型：先把问题抽象对

- BOLA/IDOR 是对象级授权缺失：用户通过合法接口操作了自己无权访问的 object。
- 认证只回答“你是谁”，对象授权回答“你能否对这个具体对象执行这个动作”。
- API 容易出现 BOLA，因为 object ID 常直接暴露且服务端开发容易只检查登录状态。

### B. 成立条件、边界与典型失效模式

- 不可猜测 UUID 只是降低枚举便利度，不是授权控制。
- 列表接口、批量接口、导出、异步任务和子资源都需独立对象授权。
- 缓存层/搜索索引也可能绕过主数据库授权策略。

### C. 工程设计：从“修一个点”到“设计控制面”

- 授权策略以 subject-action-resource-context 建模并在服务端集中执行。
- 资源查询尽量带上 owner/tenant scope，而不是查到对象后再“顺便判断”。
- 多租户场景把 tenant boundary 作为强约束贯穿数据层。
- 建立角色×对象×动作的 authorization tests。

### D. Detection & Evidence：如何证明你的判断

- 审计日志记录 actor、tenant、resource type/id、action、decision、policy。
- 异常跨 tenant/object access 是重要检测信号。
- 代码审计关注 getById 后缺少 policy check 的路径。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- 使用两个不同租户/用户的对象做系统化 cross-access tests。
- 测试批量、导出、缓存、异步和 GraphQL 等不同入口。
- 授权失败必须默认拒绝且不泄露敏感 object existence。

### F. 面试追问树：把一题答成一棵知识树

1. 为什么 UUID 不能替代授权？
2. 对象授权应该在 controller、service 还是 data layer 做？
3. GraphQL/批量 API 如何避免遗漏对象级授权？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

Authorization matrix + policy enforcement library + cross-tenant regression suite + audit schema。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 对象访问缺少服务端 subject-resource-action 授权。 |
| 边界 | UUID、缓存、批量/异步入口不能替代控制。 |
| 主要控制 | 集中策略 + tenant scoped query + default deny。 |
| 关键证据 | authorization decision audit。 |
| 验证 | 跨用户/跨租户系统回归。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：OWASP API1 BOLA / A01
- **一句话**：Authentication 证明“你是谁”；Authorization 决定“你能碰哪个对象、做什么动作”。
- **最容易答错**：把不可猜 ID 当授权。
- **工程动作**：为每个资源定义 owner/tenant/role policy。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q24 Request Smuggling / HTTP Desync 的本质是什么？](q24-http-parser-differential.md)
- [Q26 水平越权、垂直越权、未授权访问分别是什么？](q26-access-control.md)
- [Q23 什么是反序列化漏洞？](q23-serialization-security.md)
- [Q27 JWT 是什么？最常见的设计错误有哪些？](q27-jwt-jose.md)

## 参考标准 / 延伸阅读

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/) - 2025 Web 应用风险总览；A01 Broken Access Control，A03 Software Supply Chain Failures，A05 Injection。
- [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) - 2025-05-30 发布；用于 Web 应用技术安全控制验证与安全开发要求。
- [OWASP API Security Top 10:2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/) - API1 BOLA、API7 SSRF 等 API 风险。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q24](q24-http-parser-differential.md) | [章节首页](../../chapters/03-api-identity/README.md) | [Q26](q26-access-control.md) →
