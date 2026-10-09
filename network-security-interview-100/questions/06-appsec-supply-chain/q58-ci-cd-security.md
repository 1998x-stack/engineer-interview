---
id: Q58
title: "CI/CD Pipeline 有哪些典型安全风险？"
chapter: 6
difficulty: 4
roles: "DevSecOps / 云安全"
framework: "CI/CD Security"
pdf_page: 68
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q57](q57-secrets-incident.md) | [章节首页](../../chapters/06-appsec-supply-chain/README.md) | [Q59](q59-root-cause-analysis.md) →

# Q58 · CI/CD Pipeline 有哪些典型安全风险？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 4/5 |
| 适用岗位 | DevSecOps / 云安全 |
| Framework / 对标 | CI/CD Security |
| PDF 页码 | 第 68 页 |
| 所属章节 | 第 6 章 · 代码审计、漏洞研究与软件供应链 |

## 面试官为什么问这题

考察代码级数据流思维和软件供应链全链路风险，而不是仅会运行扫描器。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- Source/Propagation/Sanitizer/Sink 在哪里？
- 问题发生在自研代码、依赖、构建还是发布链？
- 工具结果是否可达、可利用、影响关键资产？
- 如何把修复变成 SDLC 的可重复控制？

## 30 秒回答

**一句话结论：** CI/CD 是软件供应链的“自动化超级管理员”，必须按控制面保护。

展开时优先抓住以下三点：

1. Runner 权限过大、Secrets 暴露、不可信 PR 执行、依赖/Action 被替换、Artifact 篡改、部署凭证过宽。
1. CI/CD 是高权限自动化控制面，应比业务系统更严格。
1. 需要隔离 runner、最小权限、环境级 secret、branch protection、签名与审计。

## 2-3 分钟标准回答

首先，Runner 权限过大、Secrets 暴露、不可信 PR 执行、依赖/Action 被替换、Artifact 篡改、部署凭证过宽。
其次，CI/CD 是高权限自动化控制面，应比业务系统更严格。
流水线经常同时拥有源码、生产凭据、构建机和制品发布权限，因此攻击价值极高。
特别要区分 trusted branch 与 untrusted contribution，避免来自 fork/PR 的代码在带生产 secret 的 runner 上执行。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- Runner 权限过大、Secrets 暴露、不可信 PR 执行、依赖/Action 被替换、Artifact 篡改、部署凭证过宽。
- CI/CD 是高权限自动化控制面，应比业务系统更严格。
- 需要隔离 runner、最小权限、环境级 secret、branch protection、签名与审计。

### 02 · 面试答题主线

1. Runner 权限过大、Secrets 暴露、不可信 PR 执行、依赖/Action 被替换、Artifact 篡改、部署凭证过宽。
2. CI/CD 是高权限自动化控制面，应比业务系统更严格。
3. 需要隔离 runner、最小权限、环境级 secret、branch protection、签名与审计。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

流水线经常同时拥有源码、生产凭据、构建机和制品发布权限，因此攻击价值极高。

特别要区分 trusted branch 与 untrusted contribution，避免来自 fork/PR 的代码在带生产 secret 的 runner 上执行。

### 04 · 高频追问

- 为什么 ephemeral runner 更安全？
- 如何实现 build once, promote many？

### 05 · 易错点

- 把 CI/CD 当普通服务器。
- 允许一个人从提交直接推进生产。

### 06 · 工程实践

- 审计 pipeline token/runner 权限。
- 对生产发布增加保护环境和审批。

### 07 · 一句话记忆

> CI/CD 是软件供应链的“自动化超级管理员”，必须按控制面保护。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

CI/CD 往往拥有代码、制品和生产部署权限，因此属于高价值控制面。

对不可信 PR、第三方 Action/插件、runner 隔离、secret scope 和 artifact integrity 要单独建模。

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
- [ ] 审计 pipeline token/runner 权限。
- [ ] 对生产发布增加保护环境和审批。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- 代码仓与审计记录
- CI/CD 日志
- 依赖与制品元数据
- 扫描结果与代码 owner
- 构建 provenance/签名

### 5. 追问怎么接

#### 追问：为什么 ephemeral runner 更安全？

**回答要点：** 先解释导致该现象的协议/信任边界，再说明成立所需条件，最后补充防守侧如何通过配置、日志或测试验证。

#### 追问：如何实现 build once, promote many？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 CI/CD Security 的边界，而不是只相信配置名称？
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

- CI/CD 是“自动执行 + 高权限 + 软件发布”的组合控制面，因此 compromise 影响可跨源码、secret、artifact 到 production。
- 核心风险维度：trigger trust、runner isolation、token permissions、dependency/action trust、artifact integrity、deploy approval。
- Pipeline YAML 本身是安全策略的一部分，应 code review。

### B. 成立条件、边界与典型失效模式

- fork PR/untrusted code 与 internal trusted branch 的执行权限必须不同。
- self-hosted runner 可能保留状态/secret，需隔离与清理。
- 第三方 action/plugin 更新会引入供应链信任。

### C. 工程设计：从“修一个点”到“设计控制面”

- 最小默认 token 权限，按 job 提升。
- untrusted PR 不接触 production secrets/privileged runner。
- ephemeral runner/隔离执行环境。
- artifact signing/provenance + deploy admission/approval。

### D. Detection & Evidence：如何证明你的判断

- CI trigger/actor/job/runner/token scope logs。
- secret access、artifact hash/provenance。
- deployment audit 和 environment approval。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- 用测试 PR 验证拿不到高权 secret。
- runner lifecycle/cleanup 检查。
- 从 commit 到 deployment 做完整 lineage trace。

### F. 面试追问树：把一题答成一棵知识树

1. 为什么 self-hosted runner 风险更高？
2. GitHub/GitLab token 默认权限为什么重要？
3. 如何防止 build artifact 在 CI 后被替换？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

CI/CD threat model + trust zones + token matrix + runner isolation + artifact provenance/deploy gates。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 自动化高权限流水线若失信可污染软件发布链。 |
| 边界 | untrusted trigger、runner state、第三方 action。 |
| 主要控制 | least privilege + isolated runner + provenance/admission。 |
| 关键证据 | pipeline/runner/secret/artifact/deploy audit。 |
| 验证 | untrusted PR 与 lineage 测试。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：CI/CD Security
- **一句话**：CI/CD 是软件供应链的“自动化超级管理员”，必须按控制面保护。
- **最容易答错**：把 CI/CD 当普通服务器。
- **工程动作**：审计 pipeline token/runner 权限。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q57 Git 仓库泄露密钥为什么严重？](q57-secrets-incident.md)
- [Q59 为什么安全研究员喜欢分析补丁 diff？](q59-root-cause-analysis.md)
- [Q56 什么是 SBOM？SBOM 能解决所有供应链问题吗？](q56-sbom.md)
- [Q60 Buffer Overflow 的本质和现代防护是什么？](q60-memory-safety.md)

## 参考标准 / 延伸阅读

- [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) - Secure Software Development Framework。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q57](q57-secrets-incident.md) | [章节首页](../../chapters/06-appsec-supply-chain/README.md) | [Q59](q59-root-cause-analysis.md) →
