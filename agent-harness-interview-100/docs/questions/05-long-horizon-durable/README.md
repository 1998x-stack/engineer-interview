# 第五章 Long-Horizon / Durable Agent

> 让长任务可分解、可验证、可交接、可恢复。


## 本章工程目标（v1.1）

本章把长程 Agent 当 durable system：进程可死、任务语义不能丢。

**学习结果：** 完成后应能设计 checkpoint、handoff、operation reconciliation、human interrupt 与 12 小时长任务架构。

### 章节级设计审查

读完本章后，尝试在不看答案的情况下完成四件事：

1. 用一张图标出本章的 **source of truth、control point、failure boundary**；
2. 给出至少一个可序列化的数据结构，而不是只讲概念；
3. 写出一个 fault-injection case，说明系统如何检测与恢复；
4. 设计一个只改变单一 Harness 变量的 eval/ablation。

### 面试训练建议

- **第一遍**：90 秒回答每题，只讲结论、Why、核心机制；
- **第二遍**：5 分钟回答，加入数据结构、failure、trade-off、metrics；
- **第三遍**：把本章 10 题串成一套系统设计，解释各 primitive 如何互相约束；
- **第四遍**：反向练习——给一个生产 incident，判断它属于模型、Harness、环境、权限还是 eval 问题。

## PDF 原稿：本章定位

本章核心 长任务不是无限循环，而是可分解、可验证、可交接、可恢复的 durable workflow。
长任务的关键是“外部化进度”。当上下文、进程或 worker 可以随时消失时，系统仍必须知道目标、已完成内容和下一步。
本章面试目标
- 能把小时级任务拆成 durable sprint。
- 理解 checkpoint/recovery/HITL。
- 知道“环境验证”为什么比模型自述可靠。

```mermaid
flowchart LR
  SPEC[Goal/Spec] --> INIT[Initializer]
  INIT --> PLAN[Task Plan]
  PLAN --> RUN[Short Sprint]
  RUN --> VERIFY[Verify]
  VERIFY --> CP[Checkpoint + Progress Artifact]
  CP -->|new session| RUN
  CP --> DONE[Verified Completion]
```

## 本章必须掌握的工程不变量

1. 长任务必须允许 session/context 重启而不丢失任务真相。
2. 每个阶段都有可验证 Definition of Done。
3. 副作用与 checkpoint 之间必须有 reconciliation 语义。

## 题目索引

| 题号 | 题目 | 难度 | 高频 |
|---|---|---:|---:|
| [Q41](q41-long-running-agent-degradation.md) | 为什么 Long-Running Agent 会随着时间变差？ | ★★★★☆ | ★★★★★ |
| [Q42](q42-progress-artifact.md) | 为什么 progress file 很重要？ | ★★★★☆ | ★★★☆☆ |
| [Q43](q43-initializer-agent.md) | Initializer Agent 有什么作用？ | ★★★★☆ | ★★★★☆ |
| [Q44](q44-sprint-contract-definition-of-done.md) | 什么是 Sprint Contract / Definition of Done？ | ★★★★☆ | ★★★★☆ |
| [Q45](q45-checkpoint-schema.md) | Checkpoint 应该保存什么？ | ★★★★★ | ★★★★★ |
| [Q46](q46-crash-resume-recovery.md) | Agent Crash 后怎样 Resume，而不是重新开始？ | ★★★★★ | ★★★★★ |
| [Q47](q47-human-interrupt.md) | 如何支持 Human Interrupt？ | ★★★★☆ | ★★★★☆ |
| [Q48](q48-prevent-plan-drift.md) | Long-running Agent 如何避免 Plan Drift？ | ★★★★☆ | ★★★☆☆ |
| [Q49](q49-verify-coding-agent-completion.md) | 如何判断 Coding Agent 真的完成任务？ | ★★★★☆ | ★★★★★ |
| [Q50](q50-twelve-hour-agent-design.md) | 设计一个运行 12 小时的 Agent，要新增哪些机制？ | ★★★★★ | ★★★★☆ |

## 本章训练方法

1. 先不看答案，90 秒口述结论与 Why。
2. 选 2 道题画数据结构/状态机/调用链。
3. 每题至少写 3 个 failure modes，并说明 trace 证据。
4. 给本章设计一个 20-30 task 的最小 eval suite。
5. 最后比较一个“简单 baseline”和一个“复杂 Harness”方案，确认复杂度换来了可测量收益。

## 本章重点指标

- `resume success rate`
- `checkpoint recovery time`
- `rework after crash`
- `plan-drift rate`
- `verified completion rate`

## 资料

- [W4][W5] Anthropic long-running harness series
- LangGraph persistence / interrupts

## PDF 原稿：本章复盘

> 长任务依赖 initializer、sprint contract、incremental progress、environment verification、checkpoint 与 structured handoff，最终实现可恢复自治。
