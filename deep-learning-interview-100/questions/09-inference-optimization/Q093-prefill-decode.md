---
id: "Q093"
title: "Prefill 与 Decode 的性能特征有什么区别？"
chapter: 9
chapter_name: "模型压缩与推理优化"
difficulty: "★★★"
frequency: "极高频"
priority: "S"
pdf_page: 63
tags:
  - deep-learning
  - interview
  - inference
  - serving
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q093 · Prefill 与 Decode 的性能特征有什么区别？

> **章节：** 模型压缩与推理优化
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** S
> **PDF 对应：** 第 63 页附近

## 面试官在考什么

考察 LLM Serving roofline 思维。

**高质量回答标准：** 能区分 TTFT/TPOT、prefill/decode、权重/KV；能基于指标定位 serving 瓶颈。

## 一句话结论

Prefill 一次并行处理整段 prompt，矩阵规模大、算术强度高，常偏 compute-bound；Decode 每步通常只有一个新 token，但要读取大量模型权重和 KV，矩阵瘦小，常偏 memory-bandwidth/latency-bound。

## 60–90 秒面试回答

Prefill 一次并行处理整段 prompt，矩阵规模大、算术强度高，常偏 compute-bound；Decode 每步通常只有一个新 token，但要读取大量模型权重和 KV，矩阵瘦小，常偏 memory-bandwidth/latency-bound。

## 深度解析

- TTFT 主要受 queue+prefill 影响；TPOT/ITL 主要受 decode 调度和带宽影响。
- batching 可以显著提高 decode 的矩阵规模和硬件利用。
- 长 context decode 还会增加读取 KV 的成本。



## 数学、Shape 与复杂度

Prefill 一次处理较长 prompt，矩阵乘规模大、并行度高，常更 compute-bound；decode 每步只多一个 token，却反复读取权重和历史 KV，算术强度低，常更 memory-bandwidth-bound。

## 工程实现 / PyTorch 验证

### 推荐验证协议

分别扫 prompt length/output length，画 TTFT/TPOT/GPU memory BW；不要只报总 latency。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- Serving 至少同时监控 TTFT、TPOT、吞吐、queue time、KV usage、GPU util、输入/输出 token 分布。
- 延迟优化要区分 prefill 和 decode；同一个优化不一定同时改善二者。

### 边界条件与反例

- 注意动态 batch、长尾 prompt、KV fragmentation、调度公平性、prefill/decode 干扰与 P99。

## 面试官连续追问

- 为什么 decode 的 FLOPs 少却可能很慢？
- Prefill/Decode 分离部署有什么好处？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 认为 GPU 算力峰值越高 decode 一定越快。

### 3 分钟展开框架

1. 先拆 TTFT / TPOT / throughput / P99；
2. 再拆 prefill 与 decode；
3. 估算 weight / KV / batching 的资源；
4. 最后定位 scheduler、kernel、network 或流量变化。

## 实战练习

- **容量规划**：给定模型层数、KV heads、context 和并发，估算 KV cache。
- **压测**：分别改变 prompt/output 长度，观察 TTFT 与 TPOT 的变化方向。
- **复盘**：解释 FlashAttention、PagedAttention、GQA、continuous batching 各解决哪一层问题。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

Prefill 处理整段 prompt，矩阵乘并行度高；decode 每步一个新 token、反复读权重与 KV，算术强度低。优化指标分别偏向 TTFT 与 TPOT。

### 工程与实验抓手

分别扫 prompt length/output length，画 TTFT/TPOT/GPU memory BW；不要只报总 latency。

### 失败边界 / 反例

‘prefill compute-bound、decode memory-bound’是常见近似而非永恒规律，超长 context、很大 batch、不同硬件会改变瓶颈。

### 白板专项练习

用 roofline 思路比较两阶段 arithmetic intensity，并说明 continuous batching 如何改变 decode batch。

> **本章 90 分标准：** 推理题至少区分 prefill/decode、TTFT/TPOT/throughput/P99、weight/KV，并能做容量与性能估算。

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

- **核心观测：** TTFT、TPOT、throughput、P50/P95/P99、queue time、KV occupancy、GPU BW、cost/request。
- **证据原则：** 推理方案用负载分布压测，不用单请求 demo；必须报告 warmup、并发和输入/输出 token 分布。
- **本题特定证据：** 分别扫 prompt length/output length，画 TTFT/TPOT/GPU memory BW；不要只报总 latency。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**‘prefill compute-bound、decode memory-bound’是常见近似而非永恒规律，超长 context、很大 batch、不同硬件会改变瓶颈。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先拆 TTFT/TPOT/queue → 区分 prefill/decode → 建权重/KV 账本 → 看 scheduler/kernel → 做容量规划。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q092 · Continuous Batching 为什么能提高 LLM Serving 吞吐？](../09-inference-optimization/Q092-continuous-batching.md)
- [Q094 · Speculative Decoding 的原理是什么？为什么能保持目标模型分布？](../09-inference-optimization/Q094-speculative-decoding.md)
- [Q091 · vLLM / PagedAttention 解决了什么问题？](../09-inference-optimization/Q091-vllm-pagedattention.md)
- [Q095 · 线上 LLM 突然变慢，如何分层定位？](../09-inference-optimization/Q095-llm-latency-debug.md)

## 参考资料

- [Kwon et al., Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [vLLM documentation](https://docs.vllm.ai/)
- [Leviathan et al., Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
