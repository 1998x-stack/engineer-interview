# 第 2 章 · 内存、STL 与数据导向设计

围绕 cache、allocator、数据布局和稳定帧时理解“为什么数据结构就是性能结构”。

## 本章能力目标

- alignment
- allocator
- cache locality
- AoS / SoA
- ECS / pooling

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q011](Q011.md) | 游戏引擎为什么特别在意内存对齐？ | Intermediate | `memory, data-oriented` |
| [Q012](Q012.md) | Stack 和 Heap 的区别是什么？实时引擎如何选择？ | Intermediate | `memory, data-oriented` |
| [Q013](Q013.md) | 如何设计一个固定大小 Memory Pool？ | Intermediate | `memory, data-oriented` |
| [Q014](Q014.md) | Arena / Linear Allocator 为什么适合每帧临时对象？ | Intermediate | `memory, data-oriented` |
| [Q015](Q015.md) | AoS 和 SoA 有什么区别？为什么 SoA 常用于热点系统？ | Intermediate | `memory, data-oriented` |
| [Q016](Q016.md) | ECS 为什么越来越常见？它解决了什么，又带来什么成本？ | Advanced | `memory, data-oriented, ecs` |
| [Q017](Q017.md) | Hash Map 和红黑树怎么选？ | Intermediate | `memory, data-oriented` |
| [Q018](Q018.md) | Object Pool 适合什么场景？如何避免把它用成“内存垃圾场”？ | Intermediate | `memory, data-oriented` |
| [Q019](Q019.md) | 什么是 Cache Miss？为什么游戏引擎比普通业务代码更在意？ | Intermediate | `memory, data-oriented, cache` |
| [Q020](Q020.md) | 什么是 False Sharing？如何定位与修复？ | Advanced | `memory, data-oriented` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
