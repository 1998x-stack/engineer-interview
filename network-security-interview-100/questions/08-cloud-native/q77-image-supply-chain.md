---
id: Q77
title: "Container Image 安全怎么做？"
chapter: 8
difficulty: 3
roles: "DevSecOps / 云安全"
framework: "Image Supply Chain"
pdf_page: 89
source_baseline: "网络安全面试宝典_100题_2026.pdf"
status: expanded-2026-v2
---

← [Q76](q76-kubernetes.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q78](q78-iac-policy-as-code.md) →

# Q77 · Container Image 安全怎么做？

> **定位**：本文件完整保留 PDF 对本题的题解结构，并在“扩展解析”部分加入更详细的工程化分析。新增内容用于学习与面试准备，不代表任何公司的内部题库。

## 题目信息

| 项目 | 内容 |
|---|---|
| 难度 | 3/5 |
| 适用岗位 | DevSecOps / 云安全 |
| Framework / 对标 | Image Supply Chain |
| PDF 页码 | 第 89 页 |
| 所属章节 | 第 8 章 · Cloud、Container、Kubernetes 与 DevSecOps |

## 面试官为什么问这题

考察云控制面、工作负载身份、配置和供应链的共同责任，而不是把“云安全”理解成安全组扫描。

通常不仅是在确认“是否知道名词”，还在观察以下能力：

- 这是云厂商还是客户责任？
- 控制面身份具有什么权限？
- 资源是否公开、跨账号或跨租户？
- 临时工作负载如何留证和响应？

## 30 秒回答

**一句话结论：** 镜像安全目标是“内容最小、来源可信、制品不可变、部署可验证”。

展开时优先抓住以下三点：

1. 可信 base、最小包、依赖/secret 扫描、build provenance、签名、registry policy、admission、runtime monitoring。
1. CVE 扫描只是其中一环。
1. 镜像应不可变并绑定 digest。

## 2-3 分钟标准回答

首先，可信 base、最小包、依赖/secret 扫描、build provenance、签名、registry policy、admission、runtime monitoring。
其次，CVE 扫描只是其中一环。
镜像供应链从 Dockerfile/Base image 到 build runner、registry、deployment 全程都可能被篡改。
成熟体系会使用 digest pinning、签名验证和 admission，确保“被部署的是经过构建与批准的那个镜像”。
最后要把回答落到工程闭环：说明根因控制是什么、还能有哪些纵深防御，以及如何通过日志、测试或安全回归证明控制真正生效。

---

## PDF 基线内容

> 以下部分对应成品 PDF 的本题内容，保持其术语、组织方式与观点。

### 01 · 考点拆解

- 可信 base、最小包、依赖/secret 扫描、build provenance、签名、registry policy、admission、runtime monitoring。
- CVE 扫描只是其中一环。
- 镜像应不可变并绑定 digest。

### 02 · 面试答题主线

1. 可信 base、最小包、依赖/secret 扫描、build provenance、签名、registry policy、admission、runtime monitoring。
2. CVE 扫描只是其中一环。
3. 镜像应不可变并绑定 digest。
4. 把答案收束到可验证的工程控制：说明“如何修复/设计”，并补一句“如何通过日志、测试或回归验证控制真的生效”。

### 03 · 深度解析

镜像供应链从 Dockerfile/Base image 到 build runner、registry、deployment 全程都可能被篡改。

成熟体系会使用 digest pinning、签名验证和 admission，确保“被部署的是经过构建与批准的那个镜像”。

### 04 · 高频追问

- 为什么 latest tag 风险高？
- 签名验证应该在哪一层执行？

### 05 · 易错点

- 只修高危 CVE。
- 在不同环境重新 build。

### 06 · 工程实践

- 使用 minimal/base image policy。
- 对生产部署按 digest + signature 验证。

### 07 · 一句话记忆

> 镜像安全目标是“内容最小、来源可信、制品不可变、部署可验证”。

---

## 扩展解析：从“会回答”到“会做工程”

### 1. 更深一层的原理

镜像安全是“可信来源 -> 最小内容 -> 扫描 -> 签名/provenance -> registry -> admission -> runtime”的链。

CVE 扫描只覆盖一部分风险，还要考虑 secret、恶意包、错误配置和运行时权限。

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
- [ ] 使用 minimal/base image policy。
- [ ] 对生产部署按 digest + signature 验证。

### 4. 可观测性与证据

面试中主动补一句“我会从哪些证据验证”，通常很加分：

- Cloud audit/control-plane logs
- IAM policy changes
- Kubernetes audit
- object storage access
- workload/runtime telemetry

### 5. 追问怎么接

#### 追问：为什么 latest tag 风险高？

**回答要点：** 先解释导致该现象的协议/信任边界，再说明成立所需条件，最后补充防守侧如何通过配置、日志或测试验证。

#### 追问：签名验证应该在哪一层执行？

**回答要点：** 先给一句话结论，再用本题的核心原理解释边界条件；最后补充检测/修复/验证三个工程点。

### 6. 面试官可能继续升级的场景题

- 如果这个问题发生在核心业务而不是测试环境，你会如何调整风险优先级、证据保全和修复节奏？
- 如果已有一层安全产品/框架默认保护，你如何验证它真的覆盖了 Image Supply Chain 的边界，而不是只相信配置名称？
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

- Image 安全是 source→build→package→SBOM→sign→registry→admission→runtime 的供应链问题。
- CVE scanning 只回答已知组件风险，不证明镜像来源、构建完整性或 secret cleanliness。
- digest 是内容地址，tag 是可变标签；安全部署更偏向不可变 digest/provenance。

### B. 成立条件、边界与典型失效模式

- 无 CVE 镜像仍可能包含恶意代码或 secret。
- 签名只在 signing identity 和 key 可信时有意义。
- base image 更新会改变大量 transitive packages。

### C. 工程设计：从“修一个点”到“设计控制面”

- 最小受信 base、multi-stage build、non-root。
- 构建生成 SBOM/provenance、secret scan。
- artifact signing 与 registry immutability。
- admission 验证 signature/provenance/policy。

### D. Detection & Evidence：如何证明你的判断

- image digest、SBOM、build provenance/signature。
- registry push/pull audit。
- admission decision 与 runtime image ID。

一个成熟回答要主动区分：**事实（日志/状态）**、**推断（关联分析）**、**假设（尚待验证）**。这能显著降低“看到一个异常就直接下结论”的面试失分。

### E. 修复后的验证与回归

- 从 running pod 反向追踪到 commit/build。
- 拒绝 unsigned/untrusted image 测试。
- base image update 自动 rebuild/regression。

### F. 面试追问树：把一题答成一棵知识树

1. 为什么用 digest 比 tag 更适合不可变部署？
2. 签名镜像仍可能有漏洞吗？
3. SBOM 和 provenance 分别回答什么？

回答这些追问时，建议始终使用：**结论 → 原理 → 条件 → 反例/边界 → 工程控制 → 验证**。如果题目涉及生产环境，再补充可用性、兼容性、灰度和回滚。

### G. 这道题在真实工作中的“交付物”

Container image trust pipeline + SBOM/signing/provenance + registry/admission policy。

### H. 一页纸复盘

| 维度 | 应该能说清楚什么 |
|---|---|
| 根因 | 镜像风险来自组件、构建与来源完整性。 |
| 边界 | 扫描/签名各自不能覆盖全部风险。 |
| 主要控制 | trusted build + SBOM/provenance/signing + admission。 |
| 关键证据 | digest/SBOM/provenance/registry/admission。 |
| 验证 | commit→runtime trace 和 unsigned deny test。 |

<!-- END PROFESSIONAL_V2 -->


## 复习卡片

- **核心关键词**：Image Supply Chain
- **一句话**：镜像安全目标是“内容最小、来源可信、制品不可变、部署可验证”。
- **最容易答错**：只修高危 CVE。
- **工程动作**：使用 minimal/base image policy。
- **答题顺序**：定义 -> 原理 -> 边界 -> 风险 -> 检测 -> 修复 -> 验证。

## 关联题

- [Q75 Container 和 VM 的安全边界有什么不同？](q75-container-security.md)
- [Q76 Kubernetes 最常见的安全风险有哪些？](q76-kubernetes.md)
- [Q78 IaC 为什么有利于安全？](q78-iac-policy-as-code.md)
- [Q79 Serverless 是否意味着“不需要做服务器安全”？](q79-serverless-security.md)

## 参考标准 / 延伸阅读

- 参见仓库 [官方标准与参考资料](../../references/official-standards.md)。

## 安全边界

> 本仓库面向合法授权的面试学习、安全工程、检测与防守。涉及攻击技术时聚焦原理、证据、修复和验证，不提供针对真实目标的利用步骤、隐蔽规避或武器化操作。

---

← [Q76](q76-kubernetes.md) | [章节首页](../../chapters/08-cloud-native/README.md) | [Q78](q78-iac-policy-as-code.md) →
