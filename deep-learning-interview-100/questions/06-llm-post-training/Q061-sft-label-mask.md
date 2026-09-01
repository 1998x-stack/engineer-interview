---
id: "Q061"
title: "SFT 时如何设计 Label Mask？为什么 user prompt 常不计算 Loss？"
chapter: 6
chapter_name: "LoRA、SFT 与大模型后训练"
difficulty: "★★☆"
frequency: "高频"
priority: "S"
pdf_page: 44
tags:
  - deep-learning
  - interview
  - post-training
  - sft
last_reviewed: "2026-09-01"
content_level: "v2-deep"
---

# Q061 · SFT 时如何设计 Label Mask？为什么 user prompt 常不计算 Loss？

> **章节：** LoRA、SFT 与大模型后训练
> **难度：** ★★☆ ｜ **频度：** 高频 ｜ **优先级：** S
> **PDF 对应：** 第 44 页附近

## 面试官在考什么

考察 instruction tuning 训练目标。

**高质量回答标准：** 能讲清数据、目标函数、采样和评估闭环；能识别 reward/数据泄漏/稳定性风险。

## 一句话结论

Padding 必须 mask；对于单轮 instruction tuning，常只对 assistant response 计算 next-token loss，使梯度集中在“如何回答”而非复述 prompt。

## 60–90 秒面试回答

Padding 必须 mask；对于单轮 instruction tuning，常只对 assistant response 计算 next-token loss，使梯度集中在“如何回答”而非复述 prompt。多轮对话可按模板选择是否训练 assistant 历史轮次。

## 深度解析

- 如果全序列都计算 loss，模型也会学习预测 system/user 文本，这未必符合目标。
- mask 设计必须与 chat template、shifted labels 对齐。
- 工具调用/思维轨迹数据还可能对特定字段做选择性监督。



## 数学、Shape 与复杂度

Causal LM 常对 labels 做 shift。Instruction SFT 中通常把 system/user/padding 对应 label 设为 ignore index，只对 assistant response token 求交叉熵，防止训练预算浪费在复述 prompt。

## 工程实现 / PyTorch 验证

```python
labels = input_ids.clone()
# assistant_mask=True 表示需要监督的 assistant token
labels[~assistant_mask] = -100
labels[attention_mask == 0] = -100
# Hugging Face CausalLM 通常在模型内部完成 shift
out = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
loss = out.loss
```

### 推荐验证协议

可视化一条多轮样本的 token、role、label、loss mask；随机抽样 100 条人工 spot-check。

**最低验收标准：** shape 正确、输出 finite、forward 与 reference 对齐；涉及训练时再比较 backward/gradient，涉及系统性能时至少报告 warmup 后的中位数与 P95。

## 工程实践与诊断视角

- 后训练项目必须同时记录数据版本、采样策略、reward 版本、KL、长度分布和 held-out eval；否则结果难以复现。
- 只看平均 reward 很危险，要做 slice、人工审查和作弊模式检测。

### 边界条件与反例

- 回答时主动给出一个边界条件或反例，避免把经验规律说成无条件定理。

## 面试官连续追问

- 为什么有些预训练式 SFT 会全量算 loss？
- 多轮对话 mask 如何构造？

### 推荐的追问回答结构

1. **先给结论**：一句话直接回答，不绕定义。
2. **再给机制**：公式、shape、统计维度或系统路径。
3. **说明 trade-off**：速度、显存、泛化、稳定性或数据成本。
4. **给失败边界**：什么时候不成立、会退化或需要替代方案。
5. **落到工程**：如何验证、监控或排查。

## 高频失分点

- **易错：** off-by-one：把当前位置而不是下一 token label mask 错。

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

Label mask 决定模型‘在哪些 token 上被监督’，必须与 chat template、shift、packing 和多轮 assistant span 对齐。

### 工程与实验抓手

可视化一条多轮样本的 token、role、label、loss mask；随机抽样 100 条人工 spot-check。

### 失败边界 / 反例

只按字符串位置 mask 很脆弱；模板特殊 token、截断、packing 边界可能造成 user token 被误监督。

### 白板专项练习

给一条 system/user/assistant/user/assistant 序列，逐 token 标注监督区间。

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
- **本题特定证据：** 可视化一条多轮样本的 token、role、label、loss mask；随机抽样 100 条人工 spot-check。

### 方案选择与停止条件

当收益只存在于单一 benchmark、无法复现到多个 seed/slice、引入明显 latency/显存/维护成本，或触发本题的失败边界——**只按字符串位置 mask 很脆弱；模板特殊 token、截断、packing 边界可能造成 user token 被误监督。**——就不应继续用“模型更复杂”掩盖问题。面试中主动说出停止条件，通常比继续堆方案更像真实工程负责人。

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

- [Q060 · SFT 的完整数据流程应该怎么设计？](../06-llm-post-training/Q060-sft-data-pipeline.md)
- [Q062 · SFT Loss 剧烈震荡或突然 NaN，如何排查？](../06-llm-post-training/Q062-sft-loss-debug.md)
- [Q059 · Full Fine-tuning 与 LoRA 应该如何选择？](../06-llm-post-training/Q059-full-ft-vs-lora.md)
- [Q063 · 经典 PPO-based RLHF 由哪些模型组成？目标是什么？](../06-llm-post-training/Q063-ppo-rlhf.md)

## 参考资料

- [Hu et al., LoRA](https://arxiv.org/abs/2106.09685)
- [Hugging Face PEFT - LoRA documentation](https://huggingface.co/docs/peft/main/conceptual_guides/lora)
- [Dettmers et al., QLoRA](https://arxiv.org/abs/2305.14314)
- [Schulman et al., Proximal Policy Optimization Algorithms](https://arxiv.org/abs/1707.06347)
- [Rafailov et al., Direct Preference Optimization](https://arxiv.org/abs/2305.18290)
- [Shao et al., DeepSeekMath (GRPO)](https://arxiv.org/abs/2402.03300)

> 题目来自公开候选人面经的高频问法归一化，并结合论文/官方文档扩展；不代表任何公司的官方题库或内部材料。
