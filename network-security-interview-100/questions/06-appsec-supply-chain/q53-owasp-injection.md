---
id: Q53
title: "做 SQL 注入代码审计时，你会怎么看？"
chapter: 6
difficulty: 4
roles: "AppSec / Code Review"
framework: "OWASP Injection"
pdf_page: 63
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q52](q52-static-analysis.md) | [章节首页](../../chapters/06-appsec-supply-chain/README.md) | [Q54](q54-serialization-review.md) →

# Q53 · 做 SQL 注入代码审计时，你会怎么看？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 4/5 |
| 适用岗位 | AppSec / Code Review |
| Framework / 对标 | OWASP Injection |
| PDF 页码 | 第 63 页 |
| 所属章节 | 第 6 章 · 代码审计、漏洞研究与软件供应链 |

## 面试官为什么问这题

考察代码级数据流思维和软件供应链全链路风险，而不是仅会运行扫描器。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- Source/Propagation/Sanitizer/Sink 在哪里？
- 问题发生在自研代码、依赖、构建还是发布链？
- 工具结果是否可达、可利用、影响关键资产？
- 如何把修复变成 SDLC 的可重复控制？

## 30 秒回答

**一句话结论：** 代码审计要从数据流和统一工程约束入手，而不是一次性找字符串。

展开时优先抓住以下三点：

1. 识别所有输入 source、SQL 构造点、ORM/raw query 和执行 sink。
1. 确认是否真正参数化、动态结构是否 allowlist。
1. 继续看 DB 账号权限和错误信息暴露。

## 2-3 分钟标准回答

首先，识别所有输入 source、SQL 构造点、ORM/raw query 和执行 sink。
其次，确认是否真正参数化、动态结构是否 allowlist。
代码审计不能只 grep SELECT。很多风险隐藏在 query builder、字符串格式化、存储过程、动态过滤和第三方 ORM escape hatch 中。
优秀审计会同时给出“可达路径、业务条件、最小修复点和长期工程方案”，例如统一 DAO API 与静态规则阻止 raw query。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- 识别所有输入 source、SQL 构造点、ORM/raw query 和执行 sink。
- 确认是否真正参数化、动态结构是否 allowlist。
- 继续看 DB 账号权限和错误信息暴露。

### 02 · 面试答题主线

1. 识别所有输入 source、SQL 构造点、ORM/raw query 和执行 sink。
2. 确认是否真正参数化、动态结构是否 allowlist。
3. 继续看 DB 账号权限和错误信息暴露。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

代码审计不能只 grep SELECT。很多风险隐藏在 query builder、字符串格式化、存储过程、动态过滤和第三方 ORM escape hatch 中。

优秀审计会同时给出“可达路径、业务条件、最小修复点和长期工程方案”，例如统一 DAO API 与静态规则阻止 raw query。

### 04 · 高频追问

- 如何审计二阶 SQL 注入？
- 怎样建立可持续的 SQLi 防回归规则？

### 05 · 易错点

- 只看 Controller 参数。
- 只修当前一处拼接。

### 06 · 工程实践

- 建立 raw SQL 使用清单。
- 为数据库执行封装安全 API 并加入 code review gate。

### 07 · 一句话记忆

> 代码审计要从数据流和统一工程约束入手，而不是一次性找字符串。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

统一用“数据是否进入 SQL grammar”判断风险，避免把单引号或特定数据库语法当成漏洞定义。

参数化解决 value 绑定；动态 identifier/排序结构应由固定映射控制。

代码审计应从 sink 反向找 source，或从暴露入口向下追 dataflow；两种方向可交叉验证。

结论要包含可达性、权限条件、数据转换和真实修复点。

### 2. 边界条件与面试高分点

- **先定义边界**：明确主体、资产、数据/状态和信任边界，避免把问题描述成绝对结论。
- **区分根治与纵深**：根治方案应消除不安全的数据流、权限或协议状态；WAF、告警、限流等通常属于补充控制。
- **考虑失败模式**：不仅说明正常路径，还要考虑配置漂移、解析差异、权限过宽、依赖升级和异常条件。
- **给验证方式**：安全设计必须能被单元测试、集成测试、审计日志、检测规则或演练验证。

### 3. 工程化检查清单

- [ ] 把安全检查前移且与 owner/门禁联动
- [ ] 依赖/SBOM 解决可见性，风险仍需上下文判断
- [ ] Secrets 不进入源代码和长期日志
- [ ] 补丁分析聚焦根因和回归测试
- [ ] 建立 raw SQL 使用清单。
- [ ] 为数据库执行封装安全 API 并加入 code review gate。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- 代码仓与审计记录
- CI/CD 日志
- 依赖与制品元数据
- 扫描结果与代码 owner
- 构建 provenance/签名

### 5. 追问怎么接

#### 追问：如何审计二阶 SQL 注入？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

#### 追问：怎样建立可持续的 SQLi 防回归规则？

**回答要点：** 先给一句话结论，再用本题的核心原理解释边界条件；最后补充检测/修复/验证三个工程点。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 OWASP Injection 的边界，而不是只相信配置名称？
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

- SQLi 代码审计不是 grep SELECT，而是从 HTTP/message/file source 追到 query builder/execute sink。
- 重点识别字符串拼接、raw query、动态 identifier 和“安全 helper 被错误使用”。
- 还需评估 DB account privilege 与事务上下文，形成影响判断。

### B. 成立条件、边界与典型失效模式

- ORM/raw native query、stored procedure、reporting DSL 都可能隐藏 SQL 构造。
- 跨层 wrapper 会让 sink 不在业务代码中。
- 二阶数据流可能来自数据库中已存内容。

### C. 工程设计：从“修一个点”到“设计控制面”

- 建立 SQL sink inventory 和 data-access approved API。
- SAST taint + code review 针对动态 query hotspot。
- 动态字段固定映射，DB 最小权限。
- 修复必须配安全 regression test。

### D. Detection & Evidence：如何证明你的判断

- code path/source-sink trace。
- ORM/query builder generated SQL template。
- DB audit 与 service account privilege。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- review 修复 commit 是否真正删除结构拼接。
- 正负测试覆盖动态排序/搜索/报表。
- 检查 sibling endpoints/相同 helper 是否同类缺陷。

### F. 面试追问树：把一题答成一棵知识树

1. 如何审计被多层 wrapper 包装的数据库 sink？
2. 为什么修一个 endpoint 后还要横向搜索同类模式？
3. DB privilege 如何进入漏洞风险评级？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

SQLi code-review checklist + sink map + SAST query + regression tests + privilege review。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 不可信数据可达 SQL 结构构造。 |
| 边界 | ORM/raw/procedure/二阶。 |
| 主要控制 | 安全 data-access API + taint review + DB least privilege。 |
| 关键证据 | source-sink/code/query/DB audit。 |
| 验证 | 横向同类搜索与 regression。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：OWASP Injection
- **一句话**：代码审计要从数据流和统一工程约束入手，而不是一次性找字符串。
- **最容易答错**：只看 Controller 参数。
- **工程动作**：建立 raw SQL 使用清单。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q52 什么是 Taint Analysis？](q52-static-analysis.md)
- [Q54 Java 反序列化代码审计应该关注什么？](q54-serialization-review.md)
- [Q13 使用 Prepared Statement 后是否绝对没有 SQL 注入？](../02-web-security/q13-owasp-a05-asvs.md)
- [Q12 SQL 注入的本质是什么？](../02-web-security/q12-owasp-a05-injection.md)

## 参考标准 / 延伸阅读

- [OWASP Top 10:2025](https://owasp.org/Top10/2025/) - 2025 Web 应用风险总览；A01 Broken Access Control，A03 Software Supply Chain Failures，A05 Injection。
- [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) - 2025-05-30 发布；用于 Web 应用技术安全控制验证与安全开发要求。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q52](q52-static-analysis.md) | [章节首页](../../chapters/06-appsec-supply-chain/README.md) | [Q54](q54-serialization-review.md) →
