---
id: Q95
title: "你如何把安全加入 SDLC？"
chapter: 10
difficulty: 5
roles: "AppSec / 安全研发 / 管理"
framework: "NIST SSDF / Secure SDLC"
pdf_page: 109
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q94](q94-secure-upload-architecture.md) | [章节首页](../../chapters/10-system-design/README.md) | [Q96](q96-risk-based-vm.md) →

# Q95 · 你如何把安全加入 SDLC？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 5/5 |
| 适用岗位 | AppSec / 安全研发 / 管理 |
| Framework / 对标 | NIST SSDF / Secure SDLC |
| PDF 页码 | 第 109 页 |
| 所属章节 | 第 10 章 · 高级场景、工程能力与终面题 |

## 面试官为什么问这题

考察候选人能否把安全知识转成架构、路线图、指标和跨团队可执行方案。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- 保护的关键资产是什么？
- 最重要信任边界和 attack path 是什么？
- 什么控制能真正降低风险？
- 如何验证控制有效并向业务解释优先级？

## 30 秒回答

**一句话结论：** 把安全变成默认工程路径，而不是发布前的额外障碍。

展开时优先抓住以下三点：

1. Requirements -> Threat Modeling -> Secure Design -> Coding -> Review -> SAST/SCA/Secrets -> Build -> DAST/Test -> Deploy -> Runtime -> Feedback。
1. 安全要求应和工程流程绑定，而不是最后一道人工审批。
1. 用风险分级决定 gate 强度。

## 2-3 分钟标准回答

首先，Requirements -> Threat Modeling -> Secure Design -> Coding -> Review -> SAST/SCA/Secrets -> Build -> DAST/Test -> Deploy -> Runtime -> Feedback。
其次，安全要求应和工程流程绑定，而不是最后一道人工审批。
NIST SSDF 强调把安全实践集成进各类 SDLC，而不是建立一条完全独立的“安全流程”。
成熟 AppSec 关注 developer experience：安全模板、库、自动检查、清晰 owner 和快速反馈，比单纯增加审批更可持续。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- Requirements -> Threat Modeling -> Secure Design -> Coding -> Review -> SAST/SCA/Secrets -> Build -> DAST/Test -> Deploy -> Runtime -> Feedback。
- 安全要求应和工程流程绑定，而不是最后一道人工审批。
- 用风险分级决定 gate 强度。

### 02 · 面试答题主线

1. Requirements -> Threat Modeling -> Secure Design -> Coding -> Review -> SAST/SCA/Secrets -> Build -> DAST/Test -> Deploy -> Runtime -> Feedback。
2. 安全要求应和工程流程绑定，而不是最后一道人工审批。
3. 用风险分级决定 gate 强度。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

NIST SSDF 强调把安全实践集成进各类 SDLC，而不是建立一条完全独立的“安全流程”。

成熟 AppSec 关注 developer experience：安全模板、库、自动检查、清晰 owner 和快速反馈，比单纯增加审批更可持续。

### 04 · 高频追问

- 哪些安全检查适合阻断 CI？
- Threat Modeling 应该在什么时候做？

### 05 · 易错点

- 把安全等同于上线前渗透测试。
- 所有漏洞都用同一阻断阈值。

### 06 · 工程实践

- 建立 secure-by-default 组件库。
- 对高风险设计引入 threat modeling gate。

### 07 · 一句话记忆

> 把安全变成默认工程路径，而不是发布前的额外障碍。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

安全 SDLC 的目标不是塞更多扫描器，而是把威胁建模、代码/依赖控制、构建完整性和运行反馈嵌入开发流程。

NIST SSDF 适合作为组织级实践框架，具体门禁应按风险和团队成熟度分层。

### 2. 边界条件与面试高分点

- **先定义边界**：明确主体、资产、数据/状态和信任边界，避免把问题描述成绝对结论。
- **区分根治与纵深**：根治方案应消除不安全的数据流、权限或协议状态；WAF、告警、限流等通常属于补充控制。
- **考虑失败模式**：不仅说明正常路径，还要考虑配置漂移、解析差异、权限过宽、依赖升级和异常条件。
- **给验证方式**：安全设计必须能被单元测试、集成测试、审计日志、检测规则或演练验证。

### 3. 工程化检查清单

- [ ] 先事实基础再大规模改造
- [ ] 把安全设计成平台能力而非一次性项目
- [ ] 指标反映风险下降而非扫描数量
- [ ] 明确 owner、SLA、验证和 30/60/90 日路线图
- [ ] 建立 secure-by-default 组件库。
- [ ] 对高风险设计引入 threat modeling gate。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- 架构/资产清单
- 身份与暴露面
- 关键控制覆盖率
- 事件与漏洞趋势
- 业务可恢复性指标

### 5. 追问怎么接

#### 追问：哪些安全检查适合阻断 CI？

**回答要点：** 先给一句话结论，再用本题的核心原理解释边界条件；最后补充检测/修复/验证三个工程点。

#### 追问：Threat Modeling 应该在什么时候做？

**回答要点：** 先给一句话结论，再用本题的核心原理解释边界条件；最后补充检测/修复/验证三个工程点。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 NIST SSDF / Secure SDLC 的边界，而不是只相信配置名称？
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

- Secure SDLC 的目标是把安全要求和验证嵌入需求、设计、开发、构建、测试、发布和运营，而不是发布前一次渗透。
- NIST SSDF 强调组织准备、软件保护、安全生产、漏洞响应等实践。
- 高分回答要把工具与工程 ownership/feedback loop 连接。

### B. 成立条件、边界与典型失效模式

- “shift left”不代表所有安全工作都移到开发阶段，runtime feedback 仍重要。
- 过多 gate 会诱导绕过；应按风险与信号质量设计。
- 第三方/开源/CI/CD 同样属于软件生产范围。

### C. 工程设计：从“修一个点”到“设计控制面”

- security requirements + threat modeling。
- secure coding/review + SAST/SCA/secret scan。
- build provenance/signing + test/DAST。
- runtime findings/incident 回流 root cause 和 standards。

### D. Detection & Evidence：如何证明你的判断

- repo/build/test/deploy artifacts。
- finding→owner→fix→regression history。
- SDLC coverage/MTTR/escape rate。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- seeded defect 检查 gates。
- post-release defect 追踪为何未在早期发现。
- exception/waiver 定期 review。

### F. 面试追问树：把一题答成一棵知识树

1. Shift Left 为什么不等于“把责任甩给开发”？
2. 如何衡量 Secure SDLC 是否有效？
3. 哪些安全检查适合 blocking gate？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

Secure SDLC control map + risk-tier gates + metrics + exception/root-cause feedback loop。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 安全若不进入软件生命周期，会在发布末端高成本发现。 |
| 边界 | gate friction、runtime feedback、供应链。 |
| 主要控制 | requirements→build→runtime 全链安全。 |
| 关键证据 | pipeline/finding/fix/escape metrics。 |
| 验证 | seeded flaw 与 escaped-defect review。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：NIST SSDF / Secure SDLC
- **一句话**：把安全变成默认工程路径，而不是发布前的额外障碍。
- **最容易答错**：把安全等同于上线前渗透测试。
- **工程动作**：建立 secure-by-default 组件库。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q94 设计一个安全文件上传系统。](q94-secure-upload-architecture.md)
- [Q96 如果让你设计企业漏洞管理平台，你怎么设计？](q96-risk-based-vm.md)
- [Q93 设计一个 API Gateway 安全体系，你会考虑什么？](q93-api-security.md)
- [Q97 面试现场让你写一个日志分析脚本，重点考什么？](q97-python-data-processing.md)

## 参考标准 / 延伸阅读

- [NIST SP 800-218 SSDF v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) - Secure Software Development Framework。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q94](q94-secure-upload-architecture.md) | [章节首页](../../chapters/10-system-design/README.md) | [Q96](q96-risk-based-vm.md) →
