# 第 5 章 · 3D 数学与几何

建立统一的坐标、变换、旋转、求交和插值心智模型，避免只背公式。

## 本章能力目标

- coordinate spaces
- homogeneous coordinates
- normal transform
- quaternion
- intersection / interpolation

## 题目索引

| 题号 | 题目 | 级别 | Tags |
|---|---|---|---|
| [Q041](Q041.md) | 游戏渲染中有哪些坐标空间？ | Intermediate | `3d-math, geometry` |
| [Q042](Q042.md) | 齐次坐标为什么需要第四维？ | Intermediate | `3d-math, geometry` |
| [Q043](Q043.md) | 为什么 Normal 不能直接乘 Model Matrix？ | Advanced | `3d-math, geometry` |
| [Q044](Q044.md) | Quaternion 为什么适合表示旋转？ | Advanced | `3d-math, geometry, quaternion` |
| [Q045](Q045.md) | SLERP 和 LERP 有什么区别？ | Advanced | `3d-math, geometry` |
| [Q046](Q046.md) | 如何判断一个点/包围体是否在视锥体中？ | Intermediate | `3d-math, geometry` |
| [Q047](Q047.md) | Ray 与 Triangle 如何求交？ | Advanced | `3d-math, geometry` |
| [Q048](Q048.md) | AABB 和 OBB 的区别？ | Intermediate | `3d-math, geometry` |
| [Q049](Q049.md) | 什么是重心坐标？ | Intermediate | `3d-math, geometry` |
| [Q050](Q050.md) | 为什么纹理属性必须做透视矫正插值？ | Advanced | `3d-math, geometry` |

## 复习建议

先完成本章所有题目的 **30 秒回答**，再挑 3 道 `Advanced` 题做实现/推导实验。最终目标是能把任意题回答到“机制 → Trade-off → Engine Context → Profiling”。

[返回 100 题总目录](../README.md)
