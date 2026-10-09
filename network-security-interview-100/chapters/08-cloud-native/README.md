# 第 8 章：Cloud、Container、Kubernetes 与 DevSecOps

> 云安全的第一控制面是身份，其次才是网络

**关键词：** Cloud IAM / 对象存储 / 容器 / Kubernetes / IaC / Serverless

## 本章学习目标

- 考察云控制面、工作负载身份、配置和供应链的共同责任，而不是把“云安全”理解成安全组扫描。
- 面试时先回答“原理和边界”，再回答“检测、修复与验证”。
- 所有攻防相关内容均以授权测试、蓝队分析和工程防护为目的。

## 本章统一分析框架

- 这是云厂商还是客户责任？
- 控制面身份具有什么权限？
- 资源是否公开、跨账号或跨租户？
- 临时工作负载如何留证和响应？

## 题目索引

- [Q71 什么是 Cloud Shared Responsibility Model？](../../questions/08-cloud-native/q71-cloud-security.md) - 难度 3/5 - Cloud Security
- [Q72 Cloud IAM 为什么是云安全最重要的领域之一？](../../questions/08-cloud-native/q72-cloud-iam.md) - 难度 4/5 - Cloud IAM
- [Q73 对象存储桶公开访问问题应该怎样治理？](../../questions/08-cloud-native/q73-object-storage.md) - 难度 3/5 - Object Storage
- [Q74 云环境 SSRF 为什么尤其值得关注？](../../questions/08-cloud-native/q74-ssrf-cloud-identity.md) - 难度 4/5 - SSRF + Cloud Identity
- [Q75 Container 和 VM 的安全边界有什么不同？](../../questions/08-cloud-native/q75-container-security.md) - 难度 3/5 - Container Security
- [Q76 Kubernetes 最常见的安全风险有哪些？](../../questions/08-cloud-native/q76-kubernetes.md) - 难度 4/5 - Kubernetes
- [Q77 Container Image 安全怎么做？](../../questions/08-cloud-native/q77-image-supply-chain.md) - 难度 3/5 - Image Supply Chain
- [Q78 IaC 为什么有利于安全？](../../questions/08-cloud-native/q78-iac-policy-as-code.md) - 难度 3/5 - IaC / Policy as Code
- [Q79 Serverless 是否意味着“不需要做服务器安全”？](../../questions/08-cloud-native/q79-serverless-security.md) - 难度 3/5 - Serverless Security
- [Q80 Cloud Incident Response 与传统机房 IR 最大差异是什么？](../../questions/08-cloud-native/q80-cloud-ir.md) - 难度 4/5 - Cloud IR

<!-- BEGIN CHAPTER_V2_MATRIX -->
## 高级工程师复习矩阵（v2）

这一矩阵用于二刷：不要只背定义，要能把每题压缩为 **机制 → 控制 → 证据**。面试追问时再展开边界和验证。

| 题目 | 根因/机制 | 主要控制 | 关键证据 |
|---|---|---|---|
| [Q71](../../questions/08-cloud-native/q71-cloud-security.md) | 云安全责任按服务层分配而非全部转移。 | RACI + IAM/config/log/data controls。 | cloud audit + provider assurance。 |
| [Q72](../../questions/08-cloud-native/q72-cloud-iam.md) | 云 API 权限控制资源与控制平面。 | least privilege + short-lived role + org guardrails。 | cloud API/IAM change/credential logs。 |
| [Q73](../../questions/08-cloud-native/q73-object-storage.md) | 多层 policy 可能使数据暴露超出预期。 | default private + org guardrail + short-lived sharing。 | policy/ACL/data access audit。 |
| [Q74](../../questions/08-cloud-native/q74-ssrf-cloud-identity.md) | 服务器请求能力可继承云网络与身份权限。 | destination/egress + metadata + least-privilege workload identity。 | STS/API/egress/app。 |
| [Q75](../../questions/08-cloud-native/q75-container-security.md) | 容器共享内核，隔离依赖内核与运行时策略。 | non-root + capability/seccomp/LSM + admission。 | runtime config + node/audit。 |
| [Q76](../../questions/08-cloud-native/q76-kubernetes.md) | 编排控制面、身份和高能力 workload 配置共同决定集群风险。 | least RBAC + admission + network + provenance。 | K8s audit/admission/runtime/network。 |
| [Q77](../../questions/08-cloud-native/q77-image-supply-chain.md) | 镜像风险来自组件、构建与来源完整性。 | trusted build + SBOM/provenance/signing + admission。 | digest/SBOM/provenance/registry/admission。 |
| [Q78](../../questions/08-cloud-native/q78-iac-policy-as-code.md) | 手工基础设施缺乏可重复/可审查安全状态。 | PR policy gate + controlled apply + drift。 | diff/plan/apply/runtime。 |
| [Q79](../../questions/08-cloud-native/q79-serverless-security.md) | 底层运维托管不等于应用与身份责任消失。 | least IAM + event validation + observability。 | cloud invocation/audit/trace。 |
| [Q80](../../questions/08-cloud-native/q80-cloud-ir.md) | 云资源短命且控制面 API/身份决定大量行为。 | central audit + automated containment + cloud playbooks。 | API/identity/flow/object/config/snapshot。 |

<!-- END CHAPTER_V2_MATRIX -->

## 推荐复习方法

1. 第一遍只读每题的“30 秒回答”和“一句话记忆”。
2. 第二遍遮住答案，口述 2-3 分钟，并回答追问。
3. 第三遍把自己的项目或实验经历映射到“证据 - 根因 - 修复 - 验证”。
