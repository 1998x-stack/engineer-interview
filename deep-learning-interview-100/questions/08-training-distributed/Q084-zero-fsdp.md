---
id: "Q084"
title: "ZeRO-1/2/3 与 FSDP 的核心区别和关系是什么？"
chapter: 8
chapter_name: "训练工程与分布式训练"
difficulty: "★★★"
frequency: "极高频"
priority: "S"
pdf_page: 57
tags:
  - deep-learning
  - interview
  - training-systems
  - distributed
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q084 · ZeRO-1/2/3 与 FSDP 的核心区别和关系是什么？

> **章节：** 训练工程与分布式训练
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** S
> **PDF 对应：** 第 57 页附近

## 面试官在考什么

2026 大模型训练核心工程题。

**高质量回答标准：** 能先定位 compute/memory/communication/input 哪类瓶颈，再选择工具；能解释优化手段的代价。

## 一句话结论

ZeRO 按训练状态逐级分片：Stage 1 分 optimizer states，Stage 2 再分 gradients，Stage 3 再分parameters。

## 60–90 秒面试回答

ZeRO 按训练状态逐级分片：Stage 1 分 optimizer states，Stage 2 再分 gradients，Stage 3 再分parameters。PyTorch FSDP 的 FULL_SHARD 与 ZeRO-3 思想相近：参数按需 all-gather，反向后 reduce-scatter，并让每个 rank 常驻自己的 shard。

## 深度解析

- 越高 stage 省显存越多，但通信与调度更复杂。
- FSDP 还涉及 wrap policy、state_dict、mixed precision、prefetch 等工程细节。
- ZeRO/FSDP 都是 data-parallel family 的内存分片，不等同于 Tensor Parallel。

### 选型思路

- 模型能单卡放下：优先 DDP，简单且吞吐高；
- optimizer/grad/param 占用过大：考虑 FSDP/ZeRO；
- 单层矩阵本身太大：需要 Tensor Parallel；
- 层数很多且可流水：Pipeline Parallel；
- 超大规模常组合 DP/TP/PP/sequence/context parallel。

回答时不要把“并行方式”当互斥选项，它们通常是多维组合。

## 数学、Shape 与复杂度

ZeRO 的思路是逐级切分 optimizer state、gradient、parameter；FSDP 在 PyTorch 中以参数 shard + 按需 all-gather/reduce-scatter 组织完整训练过程。两者思想高度相关，但实现与 API 生态不同。

## 工程实现 / PyTorch 验证

### 推荐验证协议

列 7B Adam 训练的 parameter/grad/moment 内存账本，估算不同 world size 下 shard 后量级。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 训练工程题先定位瓶颈属于 compute、memory、communication 还是 input pipeline，再选优化手段。
- 分布式系统的正确性优先于吞吐：先确认各 rank 数据、随机种子、梯度同步和 checkpoint 可恢复性。

### 边界条件与反例

- 注意通信拓扑、bucket、collective 同步、checkpoint 格式、故障恢复和各 rank 数据一致性。

## 面试官连续追问

- ZeRO-2 为什么参数仍复制？
- FSDP forward 前为什么 all-gather？
- checkpoint 怎么保存？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 把 ZeRO-3 和 Tensor Parallel 混为一谈。

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

ZeRO-1/2/3 逐级 shard optimizer/gradient/parameter；PyTorch FSDP/FSDP2 采用参数分片+按需 all-gather/reduce-scatter。2026 的 FSDP2 `fully_shard` 基于 DTensor per-parameter sharding。

### 工程与实验抓手

列 7B Adam 训练的 parameter/grad/moment 内存账本，估算不同 world size 下 shard 后量级。

### 失败边界 / 反例

节省显存不是免费的：更高 stage 增加通信、调度和 checkpoint 复杂度；小模型可能得不偿失。

### 白板专项练习

画一层 FSDP forward：sharded param→all-gather→compute→reshard；backward 再说明 reduce-scatter。

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
- **本题特定证据：** 列 7B Adam 训练的 parameter/grad/moment 内存账本，估算不同 world size 下 shard 后量级。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**节省显存不是免费的：更高 stage 增加通信、调度和 checkpoint 复杂度；小模型可能得不偿失。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

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

- [Q083 · DDP 的核心原理是什么？为什么每卡模型保持一致？](../08-training-distributed/Q083-ddp.md)
- [Q085 · Data Parallel、Tensor Parallel、Pipeline Parallel 怎么区分？](../08-training-distributed/Q085-parallelism.md)
- [Q086 · CUDA OOM 怎么系统排查，而不是只减 batch？](../08-training-distributed/Q086-cuda-oom.md)

## 参考资料

- [Rajbhandari et al., ZeRO](https://arxiv.org/abs/1910.02054)
- [PyTorch FSDP documentation](https://docs.pytorch.org/docs/stable/fsdp.html)
- [PyTorch FSDP2 `fully_shard` documentation](https://docs.pytorch.org/docs/main/distributed.fsdp.fully_shard.html)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
