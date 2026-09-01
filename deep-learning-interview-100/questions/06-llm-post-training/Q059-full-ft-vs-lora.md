---
id: "Q059"
title: "Full Fine-tuning 与 LoRA 应该如何选择？"
chapter: 6
chapter_name: "LoRA、SFT 与大模型后训练"
difficulty: "★★☆"
frequency: "高频"
priority: "S"
pdf_page: 42
tags:
  - deep-learning
  - interview
  - post-training
  - lora
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q059 · Full Fine-tuning 与 LoRA 应该如何选择？

> **章节：** LoRA、SFT 与大模型后训练
> **难度：** ★★☆ ｜ **频度：** 高频 ｜ **优先级：** S
> **PDF 对应：** 第 42 页附近

## 面试官在考什么

考察工程 trade-off。

**高质量回答标准：** 能讲清数据、目标函数、采样和评估闭环；能识别 reward/数据泄漏/稳定性风险。

## 一句话结论

选择取决于目标性能、domain shift、数据规模、显存/训练预算与部署方式。

## 60–90 秒面试回答

选择取决于目标性能、domain shift、数据规模、显存/训练预算与部署方式。LoRA 适合快速、多任务、多租户适配；Full FT 自由度最高，在数据足够且任务偏移大时可能有更高上限，但训练、存储和版本管理成本都更高。

## 深度解析

- 多 adapter 可共享一份 base，运营成本低。
- LoRA 不能自动修复 base 缺失的基础能力。
- 要用相同 token budget 和数据做公平对比。



## 数学、Shape 与复杂度

本题没有唯一必须背诵的闭式公式；面试时应把关键变量、tensor shape、复杂度或资源量写清楚，并说明它们如何随 batch、sequence、hidden size 或并行度变化。

## 工程实现 / PyTorch 验证

### 推荐验证协议

设计一个决策矩阵：质量上限、训练显存、checkpoint 大小、灾难性遗忘、推理部署、版本管理。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 后训练项目必须同时记录数据版本、采样策略、reward 版本、KL、长度分布和 held-out eval；否则结果难以复现。
- 只看平均 reward 很危险，要做 slice、人工审查和作弊模式检测。

### 边界条件与反例

- 注意 target_modules、rank/alpha、adapter dropout、merge/unmerge、量化基座和多 adapter 管理。

## 面试官连续追问

- 什么时候 LoRA 会明显输给 Full FT？
- 多 LoRA merge 会发生什么？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 只按 GPU 是否够用做决策，不看任务偏移和部署。

### 3 分钟展开框架

1. 先讲数据与目标函数；
2. 再讲参数更新/采样机制；
3. 再讲稳定性、KL、reward 或 mask；
4. 最后讲评估 gate 与线上风险。

## 实战练习

- **数据卡**：为一批 SFT/preference 数据写来源、去重、长度、domain 和质量统计。
- **训练卡**：记录 token count、LR、grad norm、KL/reward、长度分布和 checkpoint。
- **评估**：设计至少一个 held-out slice 专门发现 reward hacking 或 regression。



## 90 分深挖：从会背到能做设计

### 机制与定量抓手

Full FT 与 LoRA 是 capacity/成本/部署治理的决策题：看 domain shift、数据规模、是否需改变知识、硬件、adapter 多租户与最终合并策略。

### 工程与实验抓手

设计一个决策矩阵：质量上限、训练显存、checkpoint 大小、灾难性遗忘、推理部署、版本管理。

### 失败边界 / 反例

不能仅凭训练样本少就自动选 LoRA；某些小数据任务 full FT 配强正则仍可行，反之大数据也可用 LoRA 做高效适配。

### 白板专项练习

给出两个项目情境，现场说明选择并写出你会跑的最小 ablation。

> **本章 90 分标准：** Post-training 题必须把 data→sampling→objective→optimization→evaluation 闭环讲完整，并主动讨论 reward/data 风险。

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

- **核心观测：** tokens、loss、grad norm、reward、KL、entropy、length、pass@k/held-out、regression slices。
- **证据原则：** Post-training 的结果必须可追溯到 data/reward/policy/eval 版本，平均 reward 不能作为单一上线依据。
- **本题特定证据：** 设计一个决策矩阵：质量上限、训练显存、checkpoint 大小、灾难性遗忘、推理部署、版本管理。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**不能仅凭训练样本少就自动选 LoRA；某些小数据任务 full FT 配强正则仍可行，反之大数据也可用 LoRA 做高效适配。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

## 5 分钟深挖路线

先讲数据来源 → 写 objective → 讲 sampling/update → 讲 reward/KL/稳定性 → 讲 held-out 与 release gate。

如果面试官继续追问到第 3–4 层，建议把回答切换到白板：写公式、画 tensor/系统数据流，再给一个量化例子。不要继续只用口头名词解释名词。

## 自测清单

- [ ] 能在 60–90 秒内不看资料完整回答。
- [ ] 能写出本题最关键的公式 / shape / 复杂度关系。
- [ ] 能回答至少 3 个连续追问。
- [ ] 能说出至少 1 个失败场景或反例。
- [ ] 能给出一个可执行的 PyTorch 验证或工程排障方法。
- [ ] 能解释它与相邻技术的区别，而不是把概念混在一起。

## 关联题目

- [Q058 · QLoRA 与 LoRA 的区别是什么？4-bit 基座为什么还能训练？](../06-llm-post-training/Q058-qlora.md)
- [Q060 · SFT 的完整数据流程应该怎么设计？](../06-llm-post-training/Q060-sft-data-pipeline.md)
- [Q057 · LoRA Rank 怎么选？为什么经典初始化常让一侧为零？](../06-llm-post-training/Q057-lora-rank-init.md)
- [Q061 · SFT 时如何设计 Label Mask？为什么 user prompt 常不计算 Loss？](../06-llm-post-training/Q061-sft-label-mask.md)

## 参考资料

- [Hu et al., LoRA](https://arxiv.org/abs/2106.09685)
- [Dettmers et al., QLoRA](https://arxiv.org/abs/2305.14314)
- [Hugging Face PEFT - LoRA documentation](https://huggingface.co/docs/peft/main/conceptual_guides/lora)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
