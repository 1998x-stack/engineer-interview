---
id: Q76
title: "Kubernetes 最常见的安全风险有哪些？"
chapter: 8
difficulty: 4
roles: "K8s / 云安全 / DevSecOps"
framework: "Kubernetes"
pdf_page: 88
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q75](q75-container-security.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q77](q77-image-supply-chain.md) →

# Q76 · Kubernetes 最常见的安全风险有哪些？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 4/5 |
| 适用岗位 | K8s / 云安全 / DevSecOps |
| Framework / 对标 | Kubernetes |
| PDF 页码 | 第 88 页 |
| 所属章节 | 第 8 章 · Cloud、Container、Kubernetes 与 DevSecOps |

## 面试官为什么问这题

考察云控制面、工作负载身份、配置和供应链的共同责任，而不是把“云安全”理解成安全组扫描。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- 这是云厂商还是客户责任？
- 控制面身份具有什么权限？
- 资源是否公开、跨账号或跨租户？
- 临时工作负载如何留证和响应？

## 30 秒回答

**一句话结论：** K8s 安全必须同时看控制面、身份、工作负载、网络和供应链。

展开时优先抓住以下三点：

1. API Server、RBAC、ServiceAccount、Secrets、Privileged、hostPath、Admission、Image、NetworkPolicy、Control Plane。
1. 围绕 Identity + Workload + Network + Supply Chain + Control Plane 分析。
1. 重点是 default-deny 与最小权限。

## 2-3 分钟标准回答

首先，API Server、RBAC、ServiceAccount、Secrets、Privileged、hostPath、Admission、Image、NetworkPolicy、Control Plane。
其次，围绕 Identity + Workload + Network + Supply Chain + Control Plane 分析。
K8s 安全最容易碎片化：有人只看镜像，有人只看网络。真正系统的模型是：谁能通过 API 创建什么 workload；workload 以什么权限运行；能访问哪些网络和 secret；镜像是否可信。
Admission policy 是把安全基线前置到部署时的重要控制，但仍需运行时监控。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- API Server、RBAC、ServiceAccount、Secrets、Privileged、hostPath、Admission、Image、NetworkPolicy、Control Plane。
- 围绕 Identity + Workload + Network + Supply Chain + Control Plane 分析。
- 重点是 default-deny 与最小权限。

### 02 · 面试答题主线

1. API Server、RBAC、ServiceAccount、Secrets、Privileged、hostPath、Admission、Image、NetworkPolicy、Control Plane。
2. 围绕 Identity + Workload + Network + Supply Chain + Control Plane 分析。
3. 重点是 default-deny 与最小权限。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

K8s 安全最容易碎片化：有人只看镜像，有人只看网络。真正系统的模型是：谁能通过 API 创建什么 workload；workload 以什么权限运行；能访问哪些网络和 secret；镜像是否可信。

Admission policy 是把安全基线前置到部署时的重要控制，但仍需运行时监控。

### 04 · 高频追问

- RBAC 最小权限怎么做？
- NetworkPolicy 为什么不能替代应用授权？

### 05 · 易错点

- 只开 NetworkPolicy 就认为安全。
- ServiceAccount 默认权限过大。

### 06 · 工程实践

- 对 cluster-admin 使用做清单。
- 建立 Pod Security/Admission policy。

### 07 · 一句话记忆

> K8s 安全必须同时看控制面、身份、工作负载、网络和供应链。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

K8s 风险可以按 Control Plane、Identity/RBAC、Workload、Network、Secrets、Supply Chain 分类。

最常见工程问题不是某个 Kubernetes CVE，而是过宽 RBAC、特权 workload、错误 Secret 和缺少 admission/network policy。

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
- [ ] 对 cluster-admin 使用做清单。
- [ ] 建立 Pod Security/Admission policy。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- Cloud audit/control-plane logs
- IAM policy changes
- Kubernetes audit
- object storage access
- workload/runtime telemetry

### 5. 追问怎么接

#### 追问：RBAC 最小权限怎么做？

**回答要点：** 按“资产/主体 -> 信任边界 -> 控制点 -> 可观测性 -> 回归验证”组织答案；优先给结构化、最小权限和默认拒绝的工程方案。

#### 追问：NetworkPolicy 为什么不能替代应用授权？

**回答要点：** 先解释导致该现象的协议/信任边界，再说明成立所需条件，最后补充防守侧如何通过配置、日志或测试验证。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 Kubernetes 的边界，而不是只相信配置名称？
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

- Kubernetes 安全应拆为 identity/RBAC、workload spec、network、secrets、supply chain、control plane、admission 和 observability。
- 最大误区是把 K8s 安全等同“扫描镜像 CVE”。
- service account/RBAC 和 admission policy 是连接 deployment intent 与 runtime privilege 的关键控制。

### B. 成立条件、边界与典型失效模式

- NetworkPolicy 只在 CNI 正确支持且规则覆盖时有效。
- Secrets 对象默认并非“绝对安全保险箱”，仍需 etcd/KMS/IAM/访问控制。
- namespace 是组织边界但通常不是强多租户安全边界。

### C. 工程设计：从“修一个点”到“设计控制面”

- RBAC 最小权限、禁默认 token 滥用、workload identity。
- Pod Security/自定义 admission 拒绝 privileged、hostPath、危险 capabilities。
- default-deny network + 必要 egress。
- 镜像签名/provenance 和受信 registry。

### D. Detection & Evidence：如何证明你的判断

- K8s audit：actor、verb、resource、namespace。
- admission deny/allow、RBAC changes。
- runtime/network/registry evidence。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- RBAC can-i/deny tests + service account review。
- policy tests 验证危险 workload manifest 被拒。
- namespace/egress/secret access regression。

### F. 面试追问树：把一题答成一棵知识树

1. namespace 为什么不是天然强租户边界？
2. Admission Controller 与 RBAC 各自解决什么？
3. NetworkPolicy 为什么可能配置了却没有效果？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

K8s security baseline + RBAC/admission/network policy pack + audit/detection + supply-chain gates。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 编排控制面、身份和高能力 workload 配置共同决定集群风险。 |
| 边界 | CNI、secret、namespace、多租户。 |
| 主要控制 | least RBAC + admission + network + provenance。 |
| 关键证据 | K8s audit/admission/runtime/network。 |
| 验证 | policy/RBAC/egress tests。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：Kubernetes
- **一句话**：K8s 安全必须同时看控制面、身份、工作负载、网络和供应链。
- **最容易答错**：只开 NetworkPolicy 就认为安全。
- **工程动作**：对 cluster-admin 使用做清单。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q75 Container 和 VM 的安全边界有什么不同？](q75-container-security.md)
- [Q77 Container Image 安全怎么做？](q77-image-supply-chain.md)
- [Q74 云环境 SSRF 为什么尤其值得关注？](q74-ssrf-cloud-identity.md)
- [Q78 IaC 为什么有利于安全？](q78-iac-policy-as-code.md)

## 参考标准 / 延伸阅读

- 参见仓库 [官方标准与参考资料](../../references/official-standards.md)。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q75](q75-container-security.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q77](q77-image-supply-chain.md) →
