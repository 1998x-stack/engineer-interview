---
id: "Q065"
title: "GRPO 相比 PPO 的关键变化是什么？优势估计从哪里来？"
chapter: 6
chapter_name: "LoRA、SFT 与大模型后训练"
difficulty: "★★★"
frequency: "极高频"
priority: "S"
pdf_page: 46
tags:
  - deep-learning
  - interview
  - post-training
  - ppo
  - grpo
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q065 · GRPO 相比 PPO 的关键变化是什么？优势估计从哪里来？

> **章节：** LoRA、SFT 与大模型后训练
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** S（Top 30）
> **PDF 对应：** 第 46 页附近

## 面试官在考什么

2026 高频后训练真题。

**高质量回答标准：** 能讲清数据、目标函数、采样和评估闭环；能识别 reward/数据泄漏/稳定性风险。

## 一句话结论

GRPO 对同一个 prompt 采样一组 responses，用组内 reward 的相对统计构造 advantage，从而不再依赖独立value/critic 网络。

## 60–90 秒面试回答

GRPO 对同一个 prompt 采样一组 responses，用组内 reward 的相对统计构造 advantage，从而不再依赖独立value/critic 网络。这样减少模型常驻显存和 critic 训练成本，特别适合可验证 reward 的推理任务。
A_i≈(r_i-μ_group)/(σ_group+ε)

## 深度解析

- 典型 advantage 可用 (r_i-mean(r))/std(r) 标准化。
- 仍需处理 policy ratio、KL、采样分布和 reward 质量。
- 组内奖励都相同或方差很小时，学习信号会退化。

### GRPO 的工程难点

- rollout 成本可能主导训练吞吐；
- group 内 reward 全相同会导致 advantage 信号退化；
- reward model / verifier 的偏差会被策略放大；
- 长度、格式和采样温度会改变组内比较；
- old-policy logprob 与当前 policy logprob 的计算一致性非常关键。

面试时可以主动补充：GRPO “省掉 critic”并不代表整个系统简单了，reward、rollout、采样与稳定性仍然是核心工程问题。

## 数学、Shape 与复杂度

同一 prompt 采样 $G$ 个回答，典型组内标准化 advantage：

$$
A_i=\frac{r_i-\mu_G}{\sigma_G+\epsilon}.
$$

当组内 reward 方差接近 0 时，学习信号变弱；group size 增大可改善统计但会提高 rollout 成本。

## 工程实现 / PyTorch 验证

### 推荐验证协议

对 G=2/8/32 模拟 reward，统计 advantage 方差；构造全相同 reward 验证学习信号退化。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 后训练项目必须同时记录数据版本、采样策略、reward 版本、KL、长度分布和 held-out eval；否则结果难以复现。
- 只看平均 reward 很危险，要做 slice、人工审查和作弊模式检测。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- GRPO 为什么适合数学/代码？
- group size 怎么影响方差和成本？
- DAPO/GSPO 试图修正 GRPO 的哪些问题？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 说 GRPO “完全没有 value 概念”而忽略它用相对 reward 构造 advantage。

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

GRPO 用同 prompt 的 group responses 做相对 reward 标准化，移除独立 critic；但 rollout、old/current logprob、KL 与 verifier 仍构成复杂系统。

### 工程与实验抓手

对 G=2/8/32 模拟 reward，统计 advantage 方差；构造全相同 reward 验证学习信号退化。

### 失败边界 / 反例

group 内比较会受采样温度、答案长度和 reward scale 影响；若 reward 大量 ties，增加 G 不一定有用。

### 白板专项练习

推导 group-normalized advantage，并讨论 zero-variance、outlier reward 与 per-token credit assignment。

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
- **本题特定证据：** 对 G=2/8/32 模拟 reward，统计 advantage 方差；构造全相同 reward 验证学习信号退化。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**group 内比较会受采样温度、答案长度和 reward scale 影响；若 reward 大量 ties，增加 G 不一定有用。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

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

- [Q063 · 经典 PPO-based RLHF 由哪些模型组成？目标是什么？](../06-llm-post-training/Q063-ppo-rlhf.md)
- [Q064 · DPO 为什么不需要显式 Reward Model 与在线 RL？](../06-llm-post-training/Q064-dpo.md)
- [Q066 · RLHF / GRPO 为什么常需要 KL Constraint？](../06-llm-post-training/Q066-kl-constraint.md)
- [Q067 · 什么是 Reward Hacking？如何发现与抑制？](../06-llm-post-training/Q067-reward-hacking.md)

## 参考资料

- [Shao et al., DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
