# Content Quality Gate

> GitHub Expanded Edition 2.0 不把“内容更长”当成质量本身。质量门围绕 **来源一致性、题目专属性、工程可执行性、故障覆盖和可验证性**。

## 当前覆盖

- Q001–Q100：100 个独立 Markdown。
- 10 个能力轴 Chapter README。
- 每题包含 PDF-derived 原始核心字段。
- 每题包含 Expanded Professional 章节：
  - 题目定位 / Invariant。
  - 3 分钟专业展开。
  - 深挖机制。
  - Mermaid 控制流。
  - State / Interface Design。
  - Pseudocode / Implementation Skeleton。
  - Failure Modes。
  - Trade-off。
  - Observability & Metrics。
  - Follow-up Answer Direction。
  - Know-Why / Know-How。
  - Production Checklist。
  - Related Questions。
- 20 道必刷题额外包含“深水区 / 故障注入 / 面试评分点”。
- Q100 包含企业级完整参考架构、State Model、Tool Gateway Contract、Latency Budget、可靠性状态机、RAG Action Safety、SLO Scorecard 和故障推演。

## 自动化 Gate

运行：

```bash
make validate
```

检查内容：

1. 数据层必须恰好有 Q001–Q100。
2. PDF-derived `q/quick/points/followups/pitfall/why/how` 必须逐字段保留在 Markdown。
3. Q100 必须保留 20 个系统设计追问。
4. Expanded Edition 关键标题必须存在。
5. 每个问题 Markdown 必须达到专业扩展最低内容门槛。
6. Questions Index 与 JSON 必须同步。
7. 所有仓库内 Markdown/PDF 相对链接必须可解析。

## 人工 Review Gate

自动检查不能判断“是不是模板废话”，人工 Review 应额外问：

- 这题有没有一个独立、准确的 invariant？
- 深挖段落是否真的解释本题机制，而不是复制其他题？
- Failure Mode 是否和本题真实风险相关？
- Pseudocode/State 是否能指导实现？
- Metrics 是否能验证设计，而不是只列通用 latency/cost？
- Trade-off 是否说明何时不应该使用该方案？
- 新增 framework/spec 事实是否有官方来源？

## 防止内容退化

不接受以下“扩充”：

- 为了长度重复同一结论。
- 只增加框架 API 列表。
- 把 Prompt 规则描述成安全边界。
- 用 retry 代替 error taxonomy / recovery。
- 用“更大模型/更长 context”代替系统设计。
- 新增当前规范事实却没有来源或版本语境。

## 版本原则

- `data/questions.json`：PDF-derived 核心内容契约。
- `questions/**/qxxx.md`：可持续深化的专业面试章节。
- `docs/09-references.md`：外部官方工程资料索引。
- `CHANGELOG.md`：内容模型变化记录。

目标不是做“最长的 Agent 面试题库”，而是做一套 **Know-Why + Know-How + Failure-Driven** 的可维护工程知识库。
