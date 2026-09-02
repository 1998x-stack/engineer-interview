# 第 10 章 · GPU API、现代引擎与性能优化

面向 Vulkan/D3D12 显式同步、Bindless、GPU-driven，以及 UE5 现代系统和系统级 profiling。

## 本章能力目标

- explicit sync
- bindless
- GPU-driven
- profiling
- Nanite / Lumen / open-world design

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q091](Q091.md) | Vulkan 中 Fence、Semaphore、Barrier 分别解决什么？ | Advanced | `gpu-api, performance, vulkan` |
| [Q092](Q092.md) | 为什么 Pipeline Barrier 写得太保守会掉性能？ | Advanced | `gpu-api, performance` |
| [Q093](Q093.md) | 什么是 Bindless Rendering？ | Advanced | `gpu-api, performance, bindless` |
| [Q094](Q094.md) | GPU-Driven Rendering 是什么？ | Advanced | `gpu-api, performance, gpu-driven` |
| [Q095](Q095.md) | Compute Shader 可以在游戏引擎里做什么？ | Intermediate | `gpu-api, performance` |
| [Q096](Q096.md) | 一帧只有 20 FPS，你如何定位问题？ | Advanced | `gpu-api, performance` |
| [Q097](Q097.md) | 为什么移动 GPU 和桌面 GPU 优化思路不同？ | Advanced | `gpu-api, performance` |
| [Q098](Q098.md) | Nanite 到底解决了什么问题？ | Advanced | `gpu-api, performance, nanite` |
| [Q099](Q099.md) | Lumen 的设计目标是什么？ | Advanced | `gpu-api, performance, lumen` |
| [Q100](Q100.md) | 系统设计：如何设计一个稳定 60 FPS 的开放世界引擎？ | Advanced | `gpu-api, performance, system-design` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
