# Game Engine Interview 100

> 游戏引擎 / Graphics / Engine Programmer 系统面试题库。  
> **100 道题，1 题 = 1 Markdown**；附完整 PDF、学习路线、评分 Rubric、来源映射与仓库自动校验。

## Why this repo

很多面试题库停在“定义 + 八股”。本仓库强制每题回答到：

**Concept → Mechanism → Cost Model → Trade-off → Engine Context → Profiling / Evidence**

内容基线来自仓库附带的《游戏引擎面试指南：100 道高频真题与系统解法》PDF。Markdown 在保留 PDF 原始组织的基础上进一步扩展；扩展与原 PDF 明确分层，不会把新增内容伪装成 PDF 原文。

## 目录

| 章 | 主题 | 题号 | 核心目标 |
|---:|---|---|---|
| 01 | [C++ 对象模型与语言机制](docs/questions/01-cpp-object-model/README.md) | Q001-Q010 | 从“会写 C++”升级到理解 ABI、对象生命周期、资源所有权、容器语义与引擎级元编程。 |
| 02 | [内存、STL 与数据导向设计](docs/questions/02-memory-data-oriented/README.md) | Q011-Q020 | 围绕 cache、allocator、数据布局和稳定帧时理解“为什么数据结构就是性能结构”。 |
| 03 | [操作系统、多线程与并发](docs/questions/03-os-concurrency/README.md) | Q021-Q030 | 从线程基础走到 Job System、原子内存序、线程所有权和 CPU/GPU 异步流水。 |
| 04 | [数据结构与算法](docs/questions/04-algorithms/README.md) | Q031-Q040 | 不仅写出正确算法，还要解释复杂度、数据规模、内存访问和游戏场景中的工程化版本。 |
| 05 | [3D 数学与几何](docs/questions/05-3d-math/README.md) | Q041-Q050 | 建立统一的坐标、变换、旋转、求交和插值心智模型，避免只背公式。 |
| 06 | [实时渲染管线](docs/questions/06-real-time-rendering/README.md) | Q051-Q060 | 从 GPU raster pipeline 到 depth、Forward/Deferred、clustered lighting 与 draw submission。 |
| 07 | [PBR、阴影、GI 与 Ray Tracing](docs/questions/07-pbr-ray-tracing/README.md) | Q061-Q070 | 用 Rendering Equation 统一理解 BRDF、阴影、Monte Carlo、importance sampling 与 BVH。 |
| 08 | [引擎架构与资源系统](docs/questions/08-engine-architecture/README.md) | Q071-Q080 | 从模块边界、序列化和 Asset Pipeline，走到 Render Graph 与跨平台 RHI。 |
| 09 | [动画、物理、AI 与网络](docs/questions/09-simulation-networking/README.md) | Q081-Q090 | 掌握实时模拟中的姿态、约束、固定时间步、碰撞、寻路、预测和确定性。 |
| 10 | [GPU API、现代引擎与性能优化](docs/questions/10-gpu-api-performance/README.md) | Q091-Q100 | 面向 Vulkan/D3D12 显式同步、Bindless、GPU-driven，以及 UE5 现代系统和系统级 profiling。 |

**[→ 打开 100 道题总目录](docs/questions/README.md)**  
**[→ 学习路线](docs/STUDY_GUIDE.md)**  
**[→ 面试评分标准](docs/INTERVIEW_RUBRIC.md)**  
**[→ PDF Source Map](docs/PDF_SOURCE_MAP.md)**  
**[→ 资料来源](docs/SOURCES.md)**

## 每题 Markdown 的固定结构

```text
题目定位
├─ 30 秒回答（PDF）
├─ PDF 深入拆解 / 核心抓手 / Gotcha
├─ 专业扩展：成本模型与工程机制
├─ 最小实现 / 公式 / 结构图
├─ Engine Context
├─ Profiling / Validation
├─ 扩展 Gotchas
├─ 高频追问树
├─ 面试评分 Rubric
├─ 关联题目
└─ 权威资料
```

## 内容口径

- **Source-derived**：以 PDF 为基线，保留原有问题、30 秒答案、深入拆解、Gotcha、追问与面试官视角。
- **Repository enrichment**：新增机制推导、实现骨架、性能验证、跨题关联和当前官方资料。
- **公开面经**：只证明主题曾公开出现，不视为公司官方题库。

## PDF

[下载 / 查看完整 PDF](docs/assets/book/game-engine-interview-100.pdf)

## Repository QA

```bash
python scripts/validate_repo.py
```

校验：
- 恰好 100 个问题文件；
- Q001-Q100 无缺号/重复；
- frontmatter ID 与文件名一致；
- 所有内部 Markdown 链接存在；
- 每题必须包含 source / enrichment / profiling / references 等核心章节。

## 适合的岗位

- Game Engine Programmer
- Graphics / Rendering Engineer
- Engine / Core Systems Engineer
- Technical Artist（偏底层与渲染）
- Gameplay Engineer（需要引擎基础）

## 发布前许可说明

仓库没有替维护者预选开源许可证。公开发布前请根据你的用途选择合适许可，并再次检查第三方链接、候选人面经引用与公司商标的使用方式。详见 [PUBLISHING_CHECKLIST.md](PUBLISHING_CHECKLIST.md)。
