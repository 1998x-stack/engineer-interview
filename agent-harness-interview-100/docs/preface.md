# 编写说明、使用方法与 Agent Harness 心智模型

> 本页把 PDF 的前言、使用说明与“为什么 2026 年要单独准备 Agent Harness”完整映射到 Repo，并在不改变原意的前提下改成更适合 GitHub 阅读的结构。

## “真题”口径

本资料借鉴题目驱动型技术面试书“以题带知识、逐层追问、从朴素答案走向工程最优解”的教学组织方式，但不复制第三方图书原文、题解或版式。

“100 道真题”采用严格工程口径：公开可验证的岗位职责、公开 Agent 系统实践、论文暴露的真实 failure mode 与生产问题，被重构为高拟真面试题。无法公开验证的公司内部原题，不做“某厂原题”式虚构标注。

本资料训练的不是框架 API 记忆，而是系统性回答能力：**Know-Why → Know-How → Failure Modes → Trade-offs → Evals / Observability**。

## 资料基线

PDF 使用的资料基线包括：

- *AI Agents in Action*：actions/tools、memory/knowledge、reasoning/evaluation、planning/feedback；
- 《AI Agent 开发与应用：基于大模型的智能体构建》：上下文、短/长期记忆、API、向量数据库、ReAct、多智能体；
- 《字节跳动 RAG 实践手册》：检索触发、查询理解、质量-效率-成本三维评估、全链路监控、故障复盘、RAG + Agent；
- Anthropic/OpenAI/SWE-agent 等公开一手工程实践与论文。

完整书目见 [参考资料](appendices/references.md)。

## 如何使用这套 Repo

不要先背答案。每题建议走完整训练闭环：

1. 不看答案，先用 **90 秒**给结论；
2. 阅读 Know-Why，确认你解释的是 failure mode，而不是名词定义；
3. 把 Know-How 落到**数据结构、状态机、API、策略或指标**；
4. 用 Production Deep Dive 明确 source of truth、故障窗口、SLO；
5. 回答面试追问；
6. 设计一个最小 Eval / fault injection / ablation 证明机制有效；
7. 最后用 5 分钟版本做一次白板式展开。

## 能力分层

| 层级 | 典型能力 | 面试信号 | 建议题目 |
|---|---|---|---|
| L1 应用开发 | Framework / API 调用 | 会搭 Demo | Q01-Q30 |
| L2 Agent Engineer | Loop / Tools / RAG / Memory | 会实现 Agent | Q01-Q40 |
| L3 Harness Engineer | Checkpoint / Permission / Eval / Trace | 会做可靠系统 | Q41-Q80 |
| L4 AI Systems | Distributed / Cost / Ablation / Runtime | 会从证据优化系统 | Q71-Q100 |
| L5 Staff / Research | Model × Harness co-design | 会定义 runtime primitive | 重点题 + 系统设计 |

## 统一答题框架：12 个问题

1. **Goal**：系统究竟要完成什么，什么叫成功？
2. **Environment**：Agent 操作的真实世界是什么？
3. **Observation**：模型能看见什么，哪些信息不可信？
4. **Action Space**：可以执行哪些工具和副作用？
5. **State**：状态存在哪里，哪些必须持久化？
6. **Control Loop**：下一步由谁决定，何时停止？
7. **Failure**：典型失败模式是什么？
8. **Recovery**：失败、超时、Crash 后如何恢复？
9. **Security**：权限、凭证、Sandbox、Blast Radius 如何控制？
10. **Evaluation**：如何证明完成，不依赖模型自述？
11. **Economics**：Latency / Token / Cost 如何约束？
12. **Observability**：如何从 Trace 还原一次失败？

核心心智模型：**LLM 是概率策略，Harness 是控制系统与运行环境。**

## 为什么 2026 年要单独准备 Agent Harness

PDF 的判断是：Agent Engineer 的边界已经从 `Prompt + RAG + Function Calling` 扩展到 execution loop、context/memory、sandboxing、permissions、orchestration、long-running workflow、observability、evals、latency/cost 与分布式可靠性。

因此面试问题不再只是“模型会不会调用工具”，而是：

- 长任务怎样持续与恢复；
- 模型与 Harness failure 怎样归因；
- tool side effect 怎样幂等、重试与对账；
- permission/sandbox/credential 怎样限制 blast radius；
- trace/eval 怎样把随机行为变成可度量工程对象；
- context、latency、token、cost 怎样成为系统预算。

## 三根主轴

### 1. Intelligence Amplification

用 `context / tools / planning / environment / feedback` 放大模型能力。

### 2. Reliability Engineering

用 `state / checkpoint / idempotency / eval` 把概率行为工程化。

### 3. Capability Containment

用 `permission / sandbox / identity / audit` 缩小 blast radius。

三者合起来，才是完整 Agent Harness。
