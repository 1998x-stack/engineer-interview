---
id: "Q080"
title: "Mixed Precision 为什么能提速？Loss Scaling 的作用是什么？"
chapter: 8
chapter_name: "训练工程与分布式训练"
difficulty: "★★☆"
frequency: "高频"
priority: "S"
pdf_page: 55
tags:
  - deep-learning
  - interview
  - training-systems
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q080 · Mixed Precision 为什么能提速？Loss Scaling 的作用是什么？

> **章节：** 训练工程与分布式训练
> **难度：** ★★☆ ｜ **频度：** 高频 ｜ **优先级：** S
> **PDF 对应：** 第 55 页附近

## 面试官在考什么

考察 Tensor Core 与数值稳定。

**高质量回答标准：** 能先定位 compute/memory/communication/input 哪类瓶颈，再选择工具；能解释优化手段的代价。

## 一句话结论

混合精度让大部分 GEMM/卷积使用 FP16/BF16，提高 Tensor Core 吞吐并降低显存/带宽；对需要高动态范围或累积精度的部分保持 FP32。

## 60–90 秒面试回答

混合精度让大部分 GEMM/卷积使用 FP16/BF16，提高 Tensor Core 吞吐并降低显存/带宽；对需要高动态范围或累积精度的部分保持 FP32。FP16 下小梯度可能 underflow，loss scaling 先放大 loss/grad，更新前再缩回。

## 深度解析

- 动态 loss scaling 会在检测到 overflow 时降低 scale。
- BF16 一般不依赖 loss scaling。
- 混合精度收益取决于算子是否进入高效 kernel。



## 数学、Shape 与复杂度

本题没有唯一必须背诵的闭式公式；面试时应把关键变量、tensor shape、复杂度或资源量写清楚，并说明它们如何随 batch、sequence、hidden size 或并行度变化。

## 工程实现 / PyTorch 验证

### 推荐验证协议

用 autocast+GradScaler 训练小模型，记录 scaler 动态变化；再用 BF16 说明为何通常不需要同样的 loss scaling。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 训练工程题先定位瓶颈属于 compute、memory、communication 还是 input pipeline，再选优化手段。
- 分布式系统的正确性优先于吞吐：先确认各 rank 数据、随机种子、梯度同步和 checkpoint 可恢复性。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 为什么 LayerNorm/softmax 有时用更高精度累计？
- master weights 是什么？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 认为所有 tensor 都变成 FP16。

### 3 分钟展开框架

1. 先定位 compute / memory / communication / input；
2. 再拆 steady-state 与 peak；
3. 解释并行/精度/重计算的 trade-off；
4. 最后说 profiler、指标和最小复现。

## 实战练习

- **显存账本**：估算 parameter / gradient / optimizer / activation 四大项。
- **故障定位**：对 OOM、NaN、低 GPU util 各写一棵 5 步排障树。
- **分布式**：说明 DDP/FSDP/TP/PP 各自发生哪些 collective 或数据交换。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

Mixed precision 的关键是把适合低精度的 matmul/conv 放到 Tensor Core，同时对敏感 reduction/optimizer 等保留更高精度。

### 工程与实验抓手

用 autocast+GradScaler 训练小模型，记录 scaler 动态变化；再用 BF16 说明为何通常不需要同样的 loss scaling。

### 失败边界 / 反例

并非所有 op 都应强制 cast；手工全模型 `.half()` 可能比 autocast 更不稳定。

### 白板专项练习

解释 FP16 loss scaling 为什么在 backward 前乘 scale、step 前再 unscale。

> **本章 90 分标准：** 训练系统题先建资源账本，再定位 compute/memory/communication/input；任何优化都要说明交换来的代价。

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

- **核心观测：** allocated/reserved/peak memory、step time、GPU util、SM/BW、NCCL time、dataloader wait。
- **证据原则：** 系统题用 timeline 和资源账本说话；所有优化都要注明换来的 compute/communication/复杂度。
- **本题特定证据：** 用 autocast+GradScaler 训练小模型，记录 scaler 动态变化；再用 BF16 说明为何通常不需要同样的 loss scaling。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**并非所有 op 都应强制 cast；手工全模型 `.half()` 可能比 autocast 更不稳定。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先建资源账本 → 定位阶段 → 看 profiler/timeline → 选择优化 → 量化收益和副作用 → 验证可恢复性。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q079 · FP16、BF16、FP32 的差异是什么？为什么大模型偏爱 BF16？](../08-training-distributed/Q079-fp16-bf16-fp32.md)
- [Q081 · Gradient Accumulation 如何得到更大的 Effective Batch？](../08-training-distributed/Q081-gradient-accumulation.md)
- [Q082 · Gradient Checkpointing 为什么能省显存？代价是什么？](../08-training-distributed/Q082-gradient-checkpointing.md)

## 参考资料

- [Micikevicius et al., Mixed Precision Training](https://arxiv.org/abs/1710.03740)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
