---
id: "Q073"
title: "如何把 Text-only LLM 改造成多模态模型？"
chapter: 7
chapter_name: "对比学习、多模态与 Diffusion"
difficulty: "★★★"
frequency: "极高频"
priority: "A"
pdf_page: 51
tags:
  - deep-learning
  - interview
  - multimodal
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q073 · 如何把 Text-only LLM 改造成多模态模型？

> **章节：** 对比学习、多模态与 Diffusion
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** A
> **PDF 对应：** 第 51 页附近

## 面试官在考什么

考察 VLM 标准架构。

**高质量回答标准：** 能给出表征/生成的核心目标；能估算 token/compute；能说明跨模态对齐或采样成本。

## 一句话结论

常见路径是使用 vision encoder 把图片编码成视觉 token，经 projector/Q-Former/adapter 对齐到 LLMhidden space，再与文本 token 拼接或通过 cross-attention 输入语言模型；训练通常分对齐预训练、指令微调，再按需要做偏好/强化学习。

## 60–90 秒面试回答

常见路径是使用 vision encoder 把图片编码成视觉 token，经 projector/Q-Former/adapter 对齐到 LLMhidden space，再与文本 token 拼接或通过 cross-attention 输入语言模型；训练通常分对齐预训练、指令微调，再按需要做偏好/强化学习。

## 深度解析

- 投影层是模态接口，容量过小会成为信息瓶颈。
- vision encoder 可冻结、部分解冻或联合训练。
- 视觉 token 数量直接影响上下文和推理成本。



## 数学、Shape 与复杂度

本题没有唯一必须背诵的闭式公式；面试时应把关键变量、tensor shape、复杂度或资源量写清楚，并说明它们如何随 batch、sequence、hidden size 或并行度变化。

## 工程实现 / PyTorch 验证

### 推荐验证协议

统计不同分辨率/patch size 的 visual token 数和 LLM context 占比；比较 linear projector 与 token resampler。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 多模态问题先做 token budget：图片/视频 token 数决定 attention 成本和可支持的 batch/上下文。
- 生成模型要区分训练参数化、采样器、guidance 与 backbone，避免把不同层次概念混为一谈。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 为什么 projector 可能成为瓶颈？
- 图片分辨率提高后 token 数怎么控制？
- 早融合与 cross-attention 有何不同？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 只说“接一个视觉编码器”，不解释 token 对齐与训练阶段。

### 3 分钟展开框架

1. 先定义表示或生成目标；
2. 写关键 loss/forward process；
3. 估算 token/latent/采样成本；
4. 说明对齐、false negative、视频 token 或采样器的边界。

## 实战练习

- **对比学习**：手算一个 3×3 similarity matrix 的 InfoNCE。
- **多模态**：估算不同 frame sampling 下 visual token 总量。
- **Diffusion**：画出 $x_0 \rightarrow x_t \rightarrow x_0$ 的训练与采样信息流。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

多模态 LLM 的核心接口是把视觉 encoder 输出映射/压缩成 LLM 可消费的 token 表示；projector、cross-attention、Q-Former 等是不同 bridge。

### 工程与实验抓手

统计不同分辨率/patch size 的 visual token 数和 LLM context 占比；比较 linear projector 与 token resampler。

### 失败边界 / 反例

只做 embedding dimension 对齐不等于语义对齐；通常还需要图文预训练/指令调优与精细数据。

### 白板专项练习

画 vision encoder→projector/resampler→LLM 的 shape，并说明哪些参数可冻结。

> **本章 90 分标准：** 多模态/生成题要同时说明表示接口、token/compute 成本、训练目标和生成/评估失败模式。

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

- **核心观测：** retrieval/zero-shot/生成质量、token 数、分辨率/帧数、FLOPs、VRAM、采样步数。
- **证据原则：** 多模态与生成模型要把质量曲线与 token/step/分辨率成本放在同一张表里。
- **本题特定证据：** 统计不同分辨率/patch size 的 visual token 数和 LLM context 占比；比较 linear projector 与 token resampler。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**只做 embedding dimension 对齐不等于语义对齐；通常还需要图文预训练/指令调优与精细数据。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先画模态/latent 接口 → 算 token/step 成本 → 讲训练目标 → 讲质量失败模式 → 给压缩/采样 trade-off。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q072 · CLIP 为什么能做 Zero-shot 分类？](../07-multimodal-diffusion/Q072-clip-zero-shot.md)
- [Q074 · 多模态模型如何处理视频？视觉 token 爆炸怎么办？](../07-multimodal-diffusion/Q074-video-multimodal.md)
- [Q071 · 对比学习中的 False Negative 如何处理？](../07-multimodal-diffusion/Q071-false-negative.md)
- [Q075 · Diffusion 的 Forward Process 是什么？](../07-multimodal-diffusion/Q075-diffusion-forward.md)

## 参考资料

- [Radford et al., CLIP](https://arxiv.org/abs/2103.00020)
- [Ho et al., Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)
- [Rombach et al., High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [Peebles & Xie, Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
