# 第 7 章 · PBR、阴影、GI 与 Ray Tracing

用 Rendering Equation 统一理解 BRDF、阴影、Monte Carlo、importance sampling 与 BVH。

## 本章能力目标

- rendering equation
- microfacet BRDF
- shadowing
- Monte Carlo
- ray tracing / BVH

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q061](Q061.md) | 写出 Rendering Equation，并解释每一项。 | Advanced | `pbr, ray-tracing` |
| [Q062](Q062.md) | Cook-Torrance BRDF 怎么理解？ | Advanced | `pbr, ray-tracing` |
| [Q063](Q063.md) | Metallic/Roughness PBR Workflow 是什么意思？ | Intermediate | `pbr, ray-tracing` |
| [Q064](Q064.md) | Normal Map 为什么通常存在 Tangent Space？ | Intermediate | `pbr, ray-tracing` |
| [Q065](Q065.md) | Shadow Mapping 原理是什么？ | Intermediate | `pbr, ray-tracing, shadows` |
| [Q066](Q066.md) | Shadow Acne 和 Peter Panning 为什么出现？ | Intermediate | `pbr, ray-tracing, shadows` |
| [Q067](Q067.md) | PCF 和 PCSS 有什么区别？ | Advanced | `pbr, ray-tracing` |
| [Q068](Q068.md) | Path Tracing 为什么会有噪声？收敛速度如何理解？ | Advanced | `pbr, ray-tracing` |
| [Q069](Q069.md) | 什么是 Importance Sampling？ | Advanced | `pbr, ray-tracing` |
| [Q070](Q070.md) | BVH 在 Ray Tracing 中解决什么问题？ | Advanced | `pbr, ray-tracing, bvh` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
