# 第 3 章：CPU 调度

> 从经典调度算法走向 locality、实时调度与现代 Linux EEVDF。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q23](q23.md) | Preemptive 与 Non-preemptive Scheduling 的差异？ | ★★★★★ | 基础 | `preemption/scheduling` |
| [Q24](q24.md) | 如何评价一个调度算法？ | ★★★★★ | 基础 | `throughput/latency/fairness` |
| [Q25](q25.md) | FCFS 为什么会产生 Convoy Effect？ | ★★★★☆ | 基础 | `FCFS/convoy` |
| [Q26](q26.md) | SJF 为什么理论优秀但现实难实现？ | ★★★★☆ | 中等 | `SJF/SRTF/prediction` |
| [Q27](q27.md) | Round Robin 时间片应该多大？ | ★★★★☆ | 中等 | `RR/quantum/context-switch` |
| [Q28](q28.md) | Priority Scheduling 为什么会 starvation？Aging 如何解决？ | ★★★★★ | 基础 | `priority/starvation/aging` |
| [Q29](q29.md) | MLFQ 为什么适合交互式任务？ | ★★★★☆ | 中等 | `MLFQ/feedback` |
| [Q30](q30.md) | Real-time Scheduling 与普通调度最大的区别？ | ★★★☆☆ | 中等 | `real-time/deadline/EDF` |
| [Q31](q31.md) | CPU Affinity 为什么可能提升性能？ | ★★★★☆ | 中等 | `affinity/cache/NUMA` |
| [Q32](q32.md) | 现代 Linux 还是 CFS 吗？EEVDF 是什么？ | ★★★★★ | 高级 | `CFS/EEVDF/vruntime` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
