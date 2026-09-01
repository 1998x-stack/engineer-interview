# GitHub Expanded Edition：内容设计规范

本仓库的目标不是“100 个答案”，而是把每道题变成一个可复用的 **Agent Engineering reasoning unit**。

## 单题统一结构

每个 Qxxx Markdown 至少包含：

1. 题目定位：失败类别、风险、核心 invariant。
2. 面试官在考什么：保留 PDF 原始意图并扩展能力层次。
3. 30 秒回答：用于首轮面试。
4. 3 分钟专业展开：语义、状态、控制、验证四层。
5. 参考架构 / 控制流：GitHub Mermaid 可直接渲染。
6. 状态与接口设计：强迫回答落到可执行系统。
7. 实现骨架 / 伪代码：避免只讲抽象概念。
8. Failure Modes：从错误传播反推设计。
9. Trade-off：说明什么时候不应该采用该方案。
10. Observability & Metrics：方案必须可验证。
11. 连续追问与回答方向。
12. Know-Why / Know-How。
13. Production Checklist 与面试自测。

## 核心思想：Invariant-First

高级 Agent 面试答案应该先识别不可违反的系统事实，再选择框架：

```text
Question
  -> define semantics
  -> identify invariant
  -> model state transitions
  -> identify failure windows
  -> place deterministic controls
  -> design recovery
  -> add observability/eval
  -> discuss trade-offs
```

框架名只作为实现示例。即便把 LangGraph、OpenAI Agents SDK、MCP 或 A2A 换掉，状态、一致性、权限、恢复和评估逻辑仍然成立。

## Reliability First

所有故障题默认使用：

`Detect -> Classify -> Contain -> Recover -> Preserve -> Verify`

它避免面试回答直接跳到 retry，从而忽略副作用、重复执行、状态不一致和 blast radius。

## 内容来源标签

- PDF 原始字段必须原样保留，CI 会逐字段验证。
- Expanded Edition 内容用于工程深化，不声称来自上传资料逐字内容。
- 当前规范/框架事实集中维护在 `docs/09-references.md`，便于未来版本更新。
