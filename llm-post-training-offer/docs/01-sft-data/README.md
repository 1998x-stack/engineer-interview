# 第 1 章 · 后训练全景与 SFT

> 目标、数据质量、采样、CoT 冷启动与方法选择

## 本章目标

**数据视角**：训练样本的“边际价值”比总 token 数更重要。要能说出质量、难度、多样性、覆盖和泄漏分别怎么测。

**优化视角**：SFT 是条件似然最大化，不会主动对“多个合理答案谁更好”建模，也不会探索没见过的策略。

**实验视角**：用等 token / 等 step 的 data ablation，配合能力分桶与回归集，避免把更多 compute 误判成更好数据。

## 回答框架

**定义目标 → 数据/目标函数差异 → 能解决什么 → 不能解决什么 → 如何用实验验证**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q001 · 什么是 Post-Training？为什么 Pretraining 后仍需要后训练？](q001-post-training-goal.md) | 高频题 | L1 |  |
| [Q002 · SFT 到底在学什么？为什么说它是 behavior cloning？](q002-sft-behavior-cloning.md) | 高频题 | L1 | 🔥 |
| [Q003 · 公开真题：SFT 数据如何筛选和采样？](q003-sft-data-filter-sampling.md) | 公开真题 | L2 | 🔥 |
| [Q004 · SFT 数据是越多越好吗？如何理解 data quality × diversity × difficulty？](q004-sft-data-quality-diversity-difficulty.md) | 高频题 | L2 |  |
| [Q005 · 为什么 SFT 会造成 catastrophic forgetting 或 alignment tax？](q005-sft-forgetting-alignment-tax.md) | 原理推导 | L2 |  |
| [Q006 · 多领域 SFT 数据应该怎么配比？](q006-sft-domain-mixture.md) | 高频题 | L2 |  |
| [Q007 · 为什么 instruction data 需要 prompt diversity，而不只是 response diversity？](q007-prompt-diversity.md) | 原理推导 | L1 |  |
| [Q008 · 公开真题：CoT 数据怎么构建、筛选与验证？](q008-cot-data-build-filter-verify.md) | 公开真题 | L3 |  |
| [Q009 · 为什么 SFT 经常是 RL 的 cold start？DeepSeek-R1-Zero 又为什么可以跳 过？](q009-sft-cold-start-pure-rl.md) | 原理推导 | L3 |  |
| [Q010 · SFT、DPO 与 Online RL 应该如何选？](q010-sft-dpo-online-rl-choice.md) | 系统设计 | L3 | 🔥 |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| train loss 下降但能力回退 | 数据过窄/重复/错误 | 按领域和难度切片回归；检查 mixture 与 replay |
| 简单题涨、难题不涨 | 数据过易 | 提高 frontier/hard case 权重；做等 token ablation |
| 输出风格高度模板化 | synthetic/template bias | 聚类 n-gram/style；扩大 prompt/source diversity |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：把 base model 的通用能力塑造成目标行为分布
- **Unit of optimization**：instruction / response token
- **主要统计偏差**：数据选择偏差、模板偏差、遗忘
- **系统载体**：data pipeline + supervised trainer
- **规模化变量**：有效 token、质量过滤吞吐、训练 GPU-hours

### 本章必须会看的指标

- `effective tokens`
- `dedup rate`
- `filter keep-rate`
- `train/heldout loss`
- `capability regression`
- `domain/difficulty coverage`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q002, Q003, Q010。

### 章节级案例

假设你在做一个 32B 通用助手的 SFT，原始池 300 万条，最终只能训练 30 万条；你的设计必须回答“删谁、留谁、怎么证明删得对”。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

