# 第 8 章 · 引擎架构与资源系统

从模块边界、序列化和 Asset Pipeline，走到 Render Graph 与跨平台 RHI。

## 本章能力目标

- module boundaries
- serialization
- asset pipeline
- streaming
- RDG / RHI

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q071](Q071.md) | 如果从零设计游戏引擎，最核心模块有哪些？ | Advanced | `engine-architecture, assets` |
| [Q072](Q072.md) | Scene Graph 和 ECS 有什么关系？ | Intermediate | `engine-architecture, assets, ecs` |
| [Q073](Q073.md) | 游戏引擎 Serialization 系统如何设计？ | Advanced | `engine-architecture, assets` |
| [Q074](Q074.md) | Asset Pipeline 为什么不能直接运行时读取 FBX/PSD？ | Intermediate | `engine-architecture, assets` |
| [Q075](Q075.md) | 如何设计 Asset GUID？ | Intermediate | `engine-architecture, assets` |
| [Q076](Q076.md) | 什么是 Resource Streaming？ | Advanced | `engine-architecture, assets` |
| [Q077](Q077.md) | Game Thread、Render Thread、RHI Thread 如何交互？ | Advanced | `engine-architecture, assets, rhi` |
| [Q078](Q078.md) | 什么是 Render Graph？ | Advanced | `engine-architecture, assets, render-graph` |
| [Q079](Q079.md) | 为什么 Shader Variant 会爆炸？如何控制？ | Advanced | `engine-architecture, assets` |
| [Q080](Q080.md) | 如何设计跨平台 RHI？ | Advanced | `engine-architecture, assets, rhi` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
