# 第 6 章 · 实时渲染管线

从 GPU raster pipeline 到 depth、Forward/Deferred、clustered lighting 与 draw submission。

## 本章能力目标

- raster pipeline
- depth / Early-Z
- Hi-Z
- deferred / forward+
- instancing

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q051](Q051.md) | 请完整讲一遍现代 GPU Rasterization Pipeline。 | Advanced | `rendering, rasterization` |
| [Q052](Q052.md) | Rasterization 本质上在做什么？ | Intermediate | `rendering, rasterization` |
| [Q053](Q053.md) | Vertex Shader 与 Fragment Shader 谁调用次数更多？ | Intermediate | `rendering, rasterization` |
| [Q054](Q054.md) | 什么是 Early-Z？它为什么能加速？ | Advanced | `rendering, rasterization, depth` |
| [Q055](Q055.md) | Early-Z 什么时候可能失效或受限？ | Advanced | `rendering, rasterization, depth` |
| [Q056](Q056.md) | Hi-Z / Hierarchical Z 是什么？ | Advanced | `rendering, rasterization` |
| [Q057](Q057.md) | Forward 和 Deferred Rendering 如何比较？ | Intermediate | `rendering, rasterization, deferred-rendering` |
| [Q058](Q058.md) | Forward+ / Clustered Rendering 为什么出现？ | Advanced | `rendering, rasterization` |
| [Q059](Q059.md) | 为什么 Deferred GBuffer 可以不保存 World Position？ | Intermediate | `rendering, rasterization, deferred-rendering` |
| [Q060](Q060.md) | Instancing 为什么能减少 Draw Call？ | Intermediate | `rendering, rasterization` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
