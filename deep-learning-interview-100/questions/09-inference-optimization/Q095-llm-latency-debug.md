---
id: "Q095"
title: "线上 LLM 突然变慢，如何分层定位？"
chapter: 9
chapter_name: "模型压缩与推理优化"
difficulty: "★★★"
frequency: "极高频"
priority: "S"
pdf_page: 64
tags:
  - deep-learning
  - interview
  - inference
  - system-design
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q095 · 线上 LLM 突然变慢，如何分层定位？

> **章节：** 模型压缩与推理优化
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** S（Top 30）
> **PDF 对应：** 第 64 页附近

## 面试官在考什么

系统诊断能力。

**高质量回答标准：** 能区分 TTFT/TPOT、prefill/decode、权重/KV；能基于指标定位 serving 瓶颈。

## 一句话结论

把端到端 latency 拆成 Queue、Preprocess、Prefill、Decode、Network、Postprocess；同时监控 TTFT、TPOT、input/output tokens、batch size、GPU/显存、KV occupancy、queue depth、NCCL 与 kernel time。

## 60–90 秒面试回答

把端到端 latency 拆成 Queue、Preprocess、Prefill、Decode、Network、Postprocess；同时监控 TTFT、TPOT、input/output tokens、batch size、GPU/显存、KV occupancy、queue depth、NCCL 与 kernel time。先找发生变化的层，再关联流量/版本/配置变更。

## 深度解析

- 平均延迟正常而 P99 恶化，常见是排队、长请求、straggler 或资源争抢。
- 吞吐下降但 GPU 利用率高，可能是序列变长或 memory-bound。
- 需要与基线版本做 canary/A-B 对照。

### 分层定位框架

把端到端延迟拆成：

`client/network → gateway/queue → tokenize → scheduler → prefill → decode → detokenize/postprocess`。

服务侧至少分开监控：

- **TTFT**：对 queue、prompt length、prefill 最敏感；
- **TPOT / inter-token latency**：对 decode batch、memory bandwidth、KV 访问最敏感；
- **throughput**：与 continuous batching、并发和输出长度相关；
- **P95/P99**：容易被长尾 prompt、异构 request、GC/allocator、跨机通信拖坏。

正确做法是先找到哪一段 latency 发生结构性变化，再看最近的模型、kernel、driver、流量分布和配置变更。

## 数学、Shape 与复杂度

本题没有唯一必须背诵的闭式公式；面试时应把关键变量、tensor shape、复杂度或资源量写清楚，并说明它们如何随 batch、sequence、hidden size 或并行度变化。

## 工程实现 / PyTorch 验证

### 推荐验证协议

建立 dashboard：prompt/output token histogram、queue depth、batch tokens、KV occupancy、GPU BW/SM、NCCL、kernel time；做 canary diff。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- Serving 至少同时监控 TTFT、TPOT、吞吐、queue time、KV usage、GPU util、输入/输出 token 分布。
- 延迟优化要区分 prefill 和 decode；同一个优化不一定同时改善二者。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 如何区分排队慢和模型本身慢？
- KV cache 命中率下降会怎样？
- 为什么 token 长度分布变化会导致延迟突增？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 第一反应就是换 FlashAttention 或加 GPU。

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

线上变慢要先分 TTFT/TPOT/queue/throughput/P99，再按 gateway→scheduler→prefill→decode→network 分层；最后关联流量分布与版本变更。

### 工程与实验抓手

建立 dashboard：prompt/output token histogram、queue depth、batch tokens、KV occupancy、GPU BW/SM、NCCL、kernel time；做 canary diff。

### 失败边界 / 反例

平均 latency 不变但 P99 飙升通常指向长尾/排队/straggler；加 GPU 可能只是暂时掩盖调度或流量问题。

### 白板专项练习

给‘TTFT 翻倍但 TPOT 不变’与‘TPOT 变差但 queue 不变’两种现象，各列前三根因。

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
- **本题特定证据：** 建立 dashboard：prompt/output token histogram、queue depth、batch tokens、KV occupancy、GPU BW/SM、NCCL、kernel time；做 canary diff。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**平均 latency 不变但 P99 飙升通常指向长尾/排队/straggler；加 GPU 可能只是暂时掩盖调度或流量问题。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

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

- [Q091 · vLLM / PagedAttention 解决了什么问题？](../09-inference-optimization/Q091-vllm-pagedattention.md)
- [Q092 · Continuous Batching 为什么能提高 LLM Serving 吞吐？](../09-inference-optimization/Q092-continuous-batching.md)
- [Q093 · Prefill 与 Decode 的性能特征有什么区别？](../09-inference-optimization/Q093-prefill-decode.md)
- [Q094 · Speculative Decoding 的原理是什么？为什么能保持目标模型分布？](../09-inference-optimization/Q094-speculative-decoding.md)

## 参考资料

- [Kwon et al., Efficient Memory Management for LLM Serving with PagedAttention](https://arxiv.org/abs/2309.06180)
- [vLLM documentation](https://docs.vllm.ai/)
- [Leviathan et al., Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
