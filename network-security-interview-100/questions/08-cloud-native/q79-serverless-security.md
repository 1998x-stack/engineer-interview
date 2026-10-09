---
id: Q79
title: "Serverless 是否意味着“不需要做服务器安全”？"
chapter: 8
difficulty: 3
roles: "云安全 / AppSec"
framework: "Serverless Security"
pdf_page: 91
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q78](q78-iac-policy-as-code.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q80](q80-cloud-ir.md) →

# Q79 · Serverless 是否意味着“不需要做服务器安全”？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 3/5 |
| 适用岗位 | 云安全 / AppSec |
| Framework / 对标 | Serverless Security |
| PDF 页码 | 第 91 页 |
| 所属章节 | 第 8 章 · Cloud、Container、Kubernetes 与 DevSecOps |

## 面试官为什么问这题

考察云控制面、工作负载身份、配置和供应链的共同责任，而不是把“云安全”理解成安全组扫描。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- 这是云厂商还是客户责任？
- 控制面身份具有什么权限？
- 资源是否公开、跨账号或跨租户？
- 临时工作负载如何留证和响应？

## 30 秒回答

**一句话结论：** Serverless 减少服务器管理，不减少身份、代码和数据安全责任。

展开时优先抓住以下三点：

1. 底层 OS 运维责任下降，但 IAM、Secrets、依赖、事件输入、数据、日志仍属于客户。
1. 关注过权函数、供应链、事件触发和冷启动/依赖。
1. 无服务器管理 != 无安全责任。

## 2-3 分钟标准回答

首先，底层 OS 运维责任下降，但 IAM、Secrets、依赖、事件输入、数据、日志仍属于客户。
其次，关注过权函数、供应链、事件触发和冷启动/依赖。
Serverless 把基础设施抽象掉，但应用仍可能产生注入、越权和数据泄露。更重要的是函数身份常直接拥有云 API 权限，一旦逻辑被滥用，影响面取决于 IAM。
事件驱动架构还要验证消息来源、重放与幂等。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- 底层 OS 运维责任下降，但 IAM、Secrets、依赖、事件输入、数据、日志仍属于客户。
- 关注过权函数、供应链、事件触发和冷启动/依赖。
- 无服务器管理 != 无安全责任。

### 02 · 面试答题主线

1. 底层 OS 运维责任下降，但 IAM、Secrets、依赖、事件输入、数据、日志仍属于客户。
2. 关注过权函数、供应链、事件触发和冷启动/依赖。
3. 无服务器管理 != 无安全责任。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

Serverless 把基础设施抽象掉，但应用仍可能产生注入、越权和数据泄露。更重要的是函数身份常直接拥有云 API 权限，一旦逻辑被滥用，影响面取决于 IAM。

事件驱动架构还要验证消息来源、重放与幂等。

### 04 · 高频追问

- 函数身份如何最小权限？
- 事件来源如何做真实性校验？

### 05 · 易错点

- 认为 provider 管了 OS 就没有补丁/依赖问题。
- 一个通用函数角色给所有函数复用。

### 06 · 工程实践

- 每个函数定义独立 IAM。
- 检查第三方依赖与事件 schema。

### 07 · 一句话记忆

> Serverless 减少服务器管理，不减少身份、代码和数据安全责任。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

Serverless 减少服务器运维，不减少身份、依赖、输入验证、数据和事件源安全责任。

函数往往权限过宽且事件来源多样，最小权限和事件 schema 验证尤其重要。

### 2. 边界条件与面试高分点

- **先定义边界**：明确主体、资产、数据/状态和信任边界，避免把问题描述成绝对结论。
- **区分根治与纵深**：根治方案应消除不安全的数据流、权限或协议状态；WAF、告警、限流等通常属于补充控制。
- **考虑失败模式**：不仅说明正常路径，还要考虑配置漂移、解析差异、权限过宽、依赖升级和异常条件。
- **给验证方式**：安全设计必须能被单元测试、集成测试、审计日志、检测规则或演练验证。

### 3. 工程化检查清单

- [ ] 优先短期工作负载身份而非长期静态密钥
- [ ] policy as code 和默认拒绝
- [ ] 镜像/制品供应链与 admission 控制
- [ ] 云 IR 重视 API、快照、不可变日志
- [ ] 每个函数定义独立 IAM。
- [ ] 检查第三方依赖与事件 schema。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- Cloud audit/control-plane logs
- IAM policy changes
- Kubernetes audit
- object storage access
- workload/runtime telemetry

### 5. 追问怎么接

#### 追问：函数身份如何最小权限？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

#### 追问：事件来源如何做真实性校验？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 Serverless Security 的边界，而不是只相信配置名称？
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

- Serverless 减少服务器 OS 运维责任，但应用、IAM、event validation、dependency、secret、data 和 logging 仍是客户安全责任。
- 函数的权限和事件源配置成为核心攻击/错误面。
- 短生命周期实例改变传统主机 EDR/取证模型，控制更依赖 cloud audit 和 application telemetry。

### B. 成立条件、边界与典型失效模式

- 冷启动/并发和自动扩缩可导致资源/成本型 abuse。
- managed runtime patch 由 provider 负责的程度随平台不同。
- 第三方 layer/dependency 仍需供应链治理。

### C. 工程设计：从“修一个点”到“设计控制面”

- 函数/服务独立最小 IAM。
- 严格验证 event schema/source。
- secret manager/workload identity。
- 并发/timeout/egress/observability controls。

### D. Detection & Evidence：如何证明你的判断

- cloud invocation/audit/role assumption。
- application structured logs/traces。
- event source/queue/API gateway logs。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- 无权限 role 的 deny tests。
- 异常 event/schema 与 retry/dead-letter 测试。
- 高并发/失败场景验证成本和告警。

### F. 面试追问树：把一题答成一棵知识树

1. Serverless 没有“服务器管理”为什么仍有主机级风险边界？
2. event source 为什么等同输入信任边界？
3. 如何做 Serverless IR？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

Serverless threat model + function IAM/event schema/egress/logging + cost/abuse controls。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 底层运维托管不等于应用与身份责任消失。 |
| 边界 | event source、IAM、ephemeral runtime、cost abuse。 |
| 主要控制 | least IAM + event validation + observability。 |
| 关键证据 | cloud invocation/audit/trace。 |
| 验证 | deny/schema/concurrency tests。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：Serverless Security
- **一句话**：Serverless 减少服务器管理，不减少身份、代码和数据安全责任。
- **最容易答错**：认为 provider 管了 OS 就没有补丁/依赖问题。
- **工程动作**：每个函数定义独立 IAM。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q78 IaC 为什么有利于安全？](q78-iac-policy-as-code.md)
- [Q80 Cloud Incident Response 与传统机房 IR 最大差异是什么？](q80-cloud-ir.md)
- [Q77 Container Image 安全怎么做？](q77-image-supply-chain.md)
- [Q76 Kubernetes 最常见的安全风险有哪些？](q76-kubernetes.md)

## 参考标准 / 延伸阅读

- 参见仓库 [官方标准与参考资料](../../references/official-standards.md)。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q78](q78-iac-policy-as-code.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q80](q80-cloud-ir.md) →
