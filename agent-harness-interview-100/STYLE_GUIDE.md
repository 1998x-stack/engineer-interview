# Content Style Guide

- 主语言：中文；保留行业通用英文术语，首次出现时解释。
- 优先使用 `Agent Harness`、`Run/Turn/ToolCall`、`Checkpoint` 等稳定术语。
- 观点必须分清：**PDF 原稿**、**Repo 扩展**、**外部资料**。
- 不写“万能最佳实践”；必须说明适用边界与 trade-off。
- 系统设计优先给状态语义、失败恢复和 eval，不堆框架名。
- Mermaid 只画关键控制流，不把图做成组件清单。
- 代码/伪代码只展示面试需要的核心机制，不引入无关框架样板。

## v1.1 题目质量标准

每道题必须明确区分三层内容：PDF Source Layer、Teaching Layer、Engineering Research Layer。新增工程事实不得伪装成 PDF 原稿。

题目至少包含：核心结论、Know-Why、Know-How、Production Deep Dive、Failure Modes、Trade-offs、Eval、90 秒/5 分钟回答、来源、关联题，以及 v1.1 的 Design Review / Fault Injection / Ablation / Metrics / Debugging / Senior-Staff signal。

### 写作禁忌

- 不用“加重试、加缓存、加多 Agent”作为无条件最佳实践；必须说明 failure mode 与代价。
- 不把模型自述当环境事实。
- 不把 framework API 细节写成架构原理。
- 不把单次 benchmark 当稳定结论；涉及随机 Agent 应说明 trial/variance。
- 不把外部新增研究标成 PDF 原始证据。
