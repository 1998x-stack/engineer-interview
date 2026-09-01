# 使用指南

本仓库不是“100 个标准答案”，而是一套 LLM 后训练面试的推理框架。

推荐四遍法：

1. **30 秒结论**：只练定义与 why。
2. **白板推导**：PPO、GAE、DPO、GRPO、GSPO 必须能写公式并解释符号的工程含义。
3. **项目映射**：把问题替换成自己的模型规模、数据、reward、GPU、框架、指标与失败案例。
4. **连续追问**：每题至少追三层，用 failure mode 推导下一步选择。

高分回答骨架：

```text
Problem -> Objective -> Data -> Reward -> Exploration -> Credit Assignment
        -> Compute/System -> Failure Mode -> Algorithm Choice -> Eval
```


<!-- GUIDE_V2 -->
## V2 · 专业版阅读协议

每道题至少经过四次：**定义复述 → 白板推导 → failure-driven 追问 → 项目数字复盘**。优先把“为什么成立、何时失效、如何证伪”说清，再追求术语覆盖。

推荐同时使用：[研究方法论](research-methodology.md) · [工程实现检查表](implementation-checklist.md) · [白板训练](../11-playbooks/whiteboard-drills.md)。
