# 第 9 章：Linux、容器与性能排障

> 把 OS 原理落到 namespace/cgroup、OOM 与线上 P99 系统化排障。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q93](q93.md) | Container 为什么不是“小型 VM”？ | ★★★★★ | 中等 | `container/namespaces/cgroups` |
| [Q94](q94.md) | Namespace 与 Cgroup 有什么区别？ | ★★★★★ | 基础 | `namespace/cgroup/isolation` |
| [Q95](q95.md) | 为什么容器里的 root 不一定是 Host root？ | ★★★★☆ | 高级 | `user-namespace/rootless` |
| [Q96](q96.md) | malloc(100GB) 为什么在 32GB RAM 机器上可能成功？ | ★★★★★ | 高级 | `overcommit/virtual-memory/OOM` |
| [Q97](q97.md) | OOM Killer 为什么不能简单杀 RSS 最大的进程？ | ★★★★★ | 高级 | `OOM/oom_score_adj/cgroup` |
| [Q98](q98.md) | CPU 使用率不高但服务很慢，怎么排查？ | ★★★★★ | 高级 | `latency/iowait/lock/page-fault` |
| [Q99](q99.md) | File Descriptor 不断增长，如何判断 FD Leak？ | ★★★★★ | 高级 | `fd-leak/proc/EMFILE` |
| [Q100](q100.md) | 线上服务 P99 延迟突然暴涨，如何做完整 OS 排查？ | ★★★★★ | 综合 | `P99/perf/strace/IO/memory/network` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
