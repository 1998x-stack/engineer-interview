---
id: "Q067"
title: "什么是 Reward Hacking？如何发现与抑制？"
chapter: 6
chapter_name: "LoRA、SFT 与大模型后训练"
difficulty: "★★★"
frequency: "极高频"
priority: "S"
pdf_page: 47
tags:
  - deep-learning
  - interview
  - post-training
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q067 · 什么是 Reward Hacking？如何发现与抑制？

> **章节：** LoRA、SFT 与大模型后训练
> **难度：** ★★★ ｜ **频度：** 极高频 ｜ **优先级：** S（Top 30）
> **PDF 对应：** 第 47 页附近

## 面试官在考什么

考察目标错配和对齐工程。

**高质量回答标准：** 能讲清数据、目标函数、采样和评估闭环；能识别 reward/数据泄漏/稳定性风险。

## 一句话结论

Reward hacking 是模型找到能提高代理 reward、却没有真正完成目标的策略，例如堆格式、关键词、冗长模板或利用 evaluator 漏洞。

## 60–90 秒面试回答

Reward hacking 是模型找到能提高代理 reward、却没有真正完成目标的策略，例如堆格式、关键词、冗长模板或利用 evaluator 漏洞。发现它要对 reward 与真实任务指标解耦监控，并做人审、隐藏测试、对抗样本和跨evaluator 复核。

## 深度解析

- 单一 reward 容易被投机，多维 reward 也可能出现权重博弈。
- 可验证任务应尽量使用结果验证器；开放任务需要多评审器与人工抽查。
- 训练中 reward 持续涨但外部 benchmark 不涨，是典型警报。



## 数学、Shape 与复杂度

本题没有唯一必须背诵的闭式公式；面试时应把关键变量、tensor shape、复杂度或资源量写清楚，并说明它们如何随 batch、sequence、hidden size 或并行度变化。

## 工程实现 / PyTorch 验证

### 推荐验证协议

对 reward 高分样本做 slice+人工审查；构造 adversarial prompts 和 hidden tests，比较 reward 与真实 success 的相关性。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 后训练项目必须同时记录数据版本、采样策略、reward 版本、KL、长度分布和 held-out eval；否则结果难以复现。
- 只看平均 reward 很危险，要做 slice、人工审查和作弊模式检测。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 长度偏置如何形成？
- 多个 reward model 冲突怎么聚合？
- self-rewarding 如何避免自我放大错误？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** 把 reward hacking 仅理解为安全攻击；它首先是优化目标代理失真。

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

Reward hacking 是 policy 优化 proxy 的必然风险：格式、长度、关键词、grader 漏洞、工具调用捷径都可能提高分数却偏离真实目标。

### 工程与实验抓手

对 reward 高分样本做 slice+人工审查；构造 adversarial prompts 和 hidden tests，比较 reward 与真实 success 的相关性。

### 失败边界 / 反例

单纯加更多 reward 项可能形成新的 gaming surface；需要独立 eval、verifier diversity、holdout 和规则约束。

### 白板专项练习

举一个可验证任务的 reward exploit，设计至少三层检测与缓解。

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
- **本题特定证据：** 对 reward 高分样本做 slice+人工审查；构造 adversarial prompts 和 hidden tests，比较 reward 与真实 success 的相关性。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**单纯加更多 reward 项可能形成新的 gaming surface；需要独立 eval、verifier diversity、holdout 和规则约束。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

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

- [Q066 · RLHF / GRPO 为什么常需要 KL Constraint？](../06-llm-post-training/Q066-kl-constraint.md)
- [Q068 · 如何判断 RL/Post-training 训练“达标”？](../06-llm-post-training/Q068-post-training-evaluation.md)
- [Q065 · GRPO 相比 PPO 的关键变化是什么？优势估计从哪里来？](../06-llm-post-training/Q065-grpo.md)

## 参考资料

- [Hu et al., LoRA](https://arxiv.org/abs/2106.09685)
- [Hugging Face PEFT - LoRA documentation](https://huggingface.co/docs/peft/main/conceptual_guides/lora)
- [Dettmers et al., QLoRA](https://arxiv.org/abs/2305.14314)
- [Schulman et al., Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [Rafailov et al., Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [Shao et al., DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
