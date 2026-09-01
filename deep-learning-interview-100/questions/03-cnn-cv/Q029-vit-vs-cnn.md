---
id: "Q029"
title: "ViT 与 CNN 的本质差异是什么？"
chapter: 3
chapter_name: "CNN 与计算机视觉基础"
difficulty: "★★☆"
frequency: "高频"
priority: "A"
pdf_page: 23
tags:
  - deep-learning
  - interview
  - computer-vision
  - cv
  - vit
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q029 · ViT 与 CNN 的本质差异是什么？

> **章节：** CNN 与计算机视觉基础
> **难度：** ★★☆ ｜ **频度：** 高频 ｜ **优先级：** A
> **PDF 对应：** 第 23 页附近

## 面试官在考什么

考察视觉架构归纳偏置与数据规模。

**高质量回答标准：** 能从 shape、参数量、FLOPs 与任务指标四个层面回答；能写一个关键实现或边界条件。

## 一句话结论

CNN 把 locality 和 translation equivariance 直接编码进结构；ViT 把图像切成 patch token，通过 self-attention 建模全局关系，结构归纳偏置更弱，因此通常更依赖大规模数据/预训练，但扩展性与统一多模态接口更好。

## 60–90 秒面试回答

CNN 把 locality 和 translation equivariance 直接编码进结构；ViT 把图像切成 patch token，通过 self-attention 建模全局关系，结构归纳偏置更弱，因此通常更依赖大规模数据/预训练，但扩展性与统一多模态接口更好。

## 深度解析

- Patch embedding 本质可用 stride=P 的卷积实现。
- ViT 仍需要位置编码，否则 patch 顺序不可辨。
- 现代视觉系统常混合卷积局部偏置和 Transformer 全局建模。



## 数学、Shape 与复杂度

建议至少写出一个最小数学表达或 shape 关系，并明确 reduction/statistics 发生在哪些维度；若属于经验型问题，则给出可验证的实验假设。

## 工程实现 / PyTorch 验证

### 推荐验证协议

在小数据/大数据两个 regime 比较 CNN/ViT；控制参数量并记录训练速度、数据增强依赖与迁移性能。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- CV 题尽量同时说明 tensor layout、stride/padding、训练与推理差异以及 latency/显存成本。
- 检测/分割类问题要主动关注长尾、阈值、NMS、分辨率和 augmentation 对线上分布的影响。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 为什么 ViT 小数据上早期不如 CNN？
- CLS token 一定必要吗？
- Patch size 改变会如何影响 token 数和复杂度？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 把 ViT 描述为“没有任何局部性”。

### 3 分钟展开框架

1. 从 tensor shape 和参数量开始；
2. 再谈 receptive field / inductive bias / FLOPs；
3. 连接到检测、分类或 ViT 场景；
4. 最后讨论延迟、分辨率和数据增强 trade-off。

## 实战练习

- **手算**：给定输入尺寸，手算输出 shape、参数量和主要 FLOPs。
- **实现**：写最小 PyTorch 版本并与框架 reference 对齐。
- **实验**：对一个小数据集做 ablation，记录准确率与推理成本。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

CNN 强 locality/translation equivariance inductive bias；ViT 通过 patch token + global attention 用更弱先验换取数据规模与可扩展性。

### 工程与实验抓手

在小数据/大数据两个 regime 比较 CNN/ViT；控制参数量并记录训练速度、数据增强依赖与迁移性能。

### 失败边界 / 反例

‘ViT 一定比 CNN 强’不成立；输入分辨率使 token 数平方增长，patch size 也会影响细粒度信息。

### 白板专项练习

计算 224² 图片在 patch=16/14 下 token 数，并估算 attention score matrix 大小。

> **本章 90 分标准：** CV 题优先量化 shape、参数量、FLOPs、感受野和任务边界；能给 profiler/ablation 会明显加分。

## 面试官评分拆解

| 档位 | 典型表现 |
|---|---|
| 40–50 分 | 只会给定义或背结论，缺公式/机制，追问一层就断。 |
| 60–70 分 | 能解释主机制并写关键公式，但缺边界条件和工程证据。 |
| 80–90 分 | 能定量推导、比较替代方案，主动说明失败场景并给验证方法。 |
| 90+ 分 | 能把数学、实现、系统成本和项目决策串成完整证据链，并能反向设计实验验证假设。 |

### 面试表达建议

建议用 **结论 → 机制 → 定量 → trade-off → 边界 → 验证** 六步法回答。先在 60–90 秒内给主线；只有面试官继续追问时再展开公式、代码或系统细节。这样既显示深度，也避免一上来堆知识点失去重点。

## 项目化证据链：如何证明你真的做过

只讲原理只能证明“学过”，项目面试还要证明“做过、量过、复盘过”。针对本题，建议准备一张实验卡：**问题/假设 → baseline → 改动 → 指标 → 结果 → 失败 slice → 结论**。

### 建议报告的指标

- **核心观测：** mAP/IoU/Top-1、参数量、MACs/FLOPs、peak memory、latency、分辨率敏感性。
- **证据原则：** CV 方案要同时回答精度与计算预算，理论 FLOPs 必须用 profiler 验证。
- **本题特定证据：** 在小数据/大数据两个 regime 比较 CNN/ViT；控制参数量并记录训练速度、数据增强依赖与迁移性能。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**‘ViT 一定比 CNN 强’不成立；输入分辨率使 token 数平方增长，patch size 也会影响细粒度信息。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先做 shape/参数/FLOPs → 解释 inductive bias → 对比替代模块 → 给任务级指标 → 说硬件实测。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q028 · Focal Loss 为什么能处理前景/背景极度不平衡？](../03-cnn-cv/Q028-focal-loss.md)
- [Q030 · 数据增强为什么有效？Mixup 与 CutMix 有什么不同？](../03-cnn-cv/Q030-mixup-cutmix.md)
- [Q027 · IoU 与 NMS 分别是什么？请说明 NMS 实现细节。](../03-cnn-cv/Q027-iou-nms.md)

## 参考资料

- [Dosovitskiy et al., An Image is Worth 16x16 Words](https://arxiv.org/abs/2010.11929)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
