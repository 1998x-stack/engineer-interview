---
id: Q010
title: "SFT、DPO 与 Online RL 应该如何选？"
chapter: 1
chapter_title: "后训练全景与 SFT"
type: "系统设计"
level: L3
priority: high
tags: [sft, dpo, reward, verifier]
source_refs: [P14]
---

# Q010 · SFT、DPO 与 Online RL 应该如何选？

> **题型**：系统设计 · **难度**：L3 · **优先级**：🔥 高频 20 题
>
> **来源说明**：下方“PDF 原始提要”严格来自《剑指 LLM 后训练 Offer》；“扩展讲义”是在此基础上结合公开论文与工程实践做的补充分析。

[← Q009](../01-sft-data/q009-sft-cold-start-pure-rl.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q011 →](../02-reward-model/q011-reward-model-bradley-terry.md)

## 1. 题目定位

### 面试官为什么问

考察你是否能在信息不完备时做工程权衡：先定义约束和成功指标，再选择算法与系统。

### PDF 原始核心结论

SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward”。

### PDF 原始深入理解

决策顺序：有没有可靠 reward/verifier？是否需要探索新轨迹？数据是静态 pair 还是可以在线生成？系统是否 承担 rollout 成本？这比“哪个算法更新”更重要。

### PDF 原始常见失分点

用算法热度做选择，而不是由任务约束推出算法。

## 2. 面试回答阶梯

### 30 秒版

SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward”。

### 2 分钟版

1. 先给核心判断：SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward”。
2. 再解释机制：决策顺序：有没有可靠 reward/verifier？是否需要探索新轨迹？数据是静态 pair 还是可以在线生成？系统是否 承担 rollout 成本？这比“哪个算法更新”更重要。
3. 最后补一个边界条件或失败模式：算法选择先问 reward 是否可计算、是否需要在线探索、是否有偏好 pair、系统能否承受 rollout；不要从算法名出发。

### 5 分钟版

按 **定义目标 → 数据/目标函数差异 → 能解决什么 → 不能解决什么 → 如何用实验验证** 展开。不要一开始堆算法名；先明确问题的优化对象、数据分布和约束，再把公式、工程实现和评测接上。

## 3. Know-Why：为什么这个问题重要

算法选择先问 reward 是否可计算、是否需要在线探索、是否有偏好 pair、系统能否承受 rollout；不要从算法名出发。

**数据视角**：训练样本的“边际价值”比总 token 数更重要。要能说出质量、难度、多样性、覆盖和泄漏分别怎么测。

**优化视角**：SFT 是条件似然最大化，不会主动对“多个合理答案谁更好”建模，也不会探索没见过的策略。

## 4. Know-How：面试与工程上怎么做

回答时建议按照下面的顺序组织，而不是直接背结论：

1. **定义边界**：先明确本题讨论的 policy/data/reward/system 粒度与假设。
2. **写出机制**：能写公式就写公式；不能写公式就画数据流或因果链。
3. **给可观测量**：说明训练时具体看什么日志、分布和系统指标。
4. **给 failure mode**：至少讲一个“什么时候这套方法会失效”。
5. **给验证实验**：用受控 ablation 证明你的判断。

**实验视角**：用等 token / 等 step 的 data ablation，配合能力分桶与回归集，避免把更多 compute 误判成更好数据。

## 5. 公式 / 白板推导

本题重点不在死记单一公式，而在明确优化对象、数据分布和 failure mode。建议把相关目标函数与监控量写在同一张白板上。

> 白板要求：每写一个符号，都能回答“它由谁计算、在哪个阶段产生、数值异常时说明什么”。

## 6. 算法或系统流程

```text
Problem: SFT、DPO 与 Online RL 应该如何选？
  -> identify objective / data distribution
  -> choose observable training signal
  -> implement / optimize
  -> monitor failure indicators
  -> held-out evaluation
  -> ablation & iterate
```

## 7. 复杂度与工程成本

主要成本是高质量数据构建与训练 token；重点关注有效 token 比例、数据去重与筛选器成本。

在项目里至少把成本量化为 **GPU-hours / rollout tokens / peak memory / communication / labeling or verifier cost** 中适用的几项，而不是只说“更省”。

## 8. Failure Modes 与诊断

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| train loss 下降但能力回退 | 数据过窄/重复/错误 | 按领域和难度切片回归；检查 mixture 与 replay |
| 简单题涨、难题不涨 | 数据过易 | 提高 frontier/hard case 权重；做等 token ablation |
| 输出风格高度模板化 | synthetic/template bias | 聚类 n-gram/style；扩大 prompt/source diversity |

### 本题特有风险

- 用算法热度做选择，而不是由任务约束推出算法。
- 边界条件：算法选择先问 reward 是否可计算、是否需要在线探索、是否有偏好 pair、系统能否承受 rollout；不要从算法名出发。
- 若训练曲线与理论预期相反，优先检查数据/版本/归一化/掩码是否和公式假设一致，再调超参。

## 9. 推荐实验与 Ablation

| 项目 | 建议设计 |
|---|---|
| Baseline | 固定模型、总 token/step、seed 与评测协议 |
| 自变量 | 只改变本题对应的数据/reward/objective 设计 |
| 质量指标 | held-out task score / win-rate / calibration / regression |
| 行为指标 | 长度、格式、拒答、diversity、错误类型分布 |
| 判断 | 不只看最终点，还看学习曲线、方差与副作用 |

## 10. 面试官连续追问树

1. 如果用户偏好主观、但工具任务可验证，你会不会在同一模型上混用 DPO 与 RL？ 举一反三 / 章节检查 尝试不看答案，用“任务 → 数据 → reward → exploration → credit → compute → failure → eval”重新讲本章。若能把 3 个以上问题串成一条因果链，而不是逐题背诵，本章才算掌 握。 第二章 Preference、Reward Model 与 Reward Design 本章目标 完成面试题 11-20。要求不是记忆名词，而是把每个方法与其输入、目标函数、failure mode 和工程代价连接起来。
2. 如果把数据量减半，怎样保证信息量不减半？
3. 如何用一个离线实验证明改动来自数据，而不是更长训练？
4. 哪些指标能提前发现 catastrophic forgetting？

### 追问回答原则

不要把每个追问当新题。沿同一条因果链回答：**假设 → 机制 → 可观测量 → 反例 → 实验**。如果能把上一问的 failure mode 自然推成下一问的算法选择，通常比背更多术语更有说服力。

## 11. 项目映射模板

把下面字段替换成你自己的项目数字；面试时“具体数字 + 失败案例 + ablation”比泛泛而谈更可信。

- **模型/阶段**：Base/SFT checkpoint、参数规模、上下文长度。
- **数据**：来源、原始量、保留率、去重率、正确率、难度分布、领域 mixture。
- **实验**：等 token baseline；至少一个数据筛选/采样 ablation。
- **结果**：不仅报总分，还报能力分桶、遗忘项和训练成本。
- **失败案例**：说明一次“数据看起来更多但效果更差”的原因与修复。

## 12. 一句话记忆

> **Q010：SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward”。**

## 13. 参考资料

- **[P14] PDF/论文参考**：[Ouyang et al. — Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

## 14. 关联题目

- [Q001 · 什么是 Post-Training？为什么 Pretraining 后仍需要后训练？](q001-post-training-goal.md)
- [Q002 · SFT 到底在学什么？为什么说它是 behavior cloning？](q002-sft-behavior-cloning.md)
- [Q005 · 为什么 SFT 会造成 catastrophic forgetting 或 alignment tax？](q005-sft-forgetting-alignment-tax.md)
- [Q009 · 为什么 SFT 经常是 RL 的 cold start？DeepSeek-R1-Zero 又为什么可以跳 过？](q009-sft-cold-start-pure-rl.md)
- [Q011 · Reward Model 如何训练？Bradley-Terry 假设是什么？](../02-reward-model/q011-reward-model-bradley-terry.md)

<!-- V2_EXPERT_START -->
## 15. V2 专业进阶：从“会答”到“能做研究/工程”

> **内容属性**：本节是基于 PDF 原始提要的扩展讲义。它不是对 PDF 原文的复述，而是把本题展开到真实后训练项目所需要的假设、实现、诊断与实验层级。

### 15.1 把题目还原成一个可研究的问题

本题不能停在“SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward””。更专业的表述是先确定五个对象：

| 维度 | 本题应明确的内容 |
|---|---|
| Optimization objective | 把 base model 的通用能力塑造成目标行为分布 |
| Statistical unit | instruction / response token |
| 关键估计误差 | 数据选择偏差、模板偏差、遗忘 |
| 系统承载 | data pipeline + supervised trainer |
| Scale variable | 有效 token、质量过滤吞吐、训练 GPU-hours |

对 **Q010**，最关键的机制判断是：**算法选择先问 reward 是否可计算、是否需要在线探索、是否有偏好 pair、系统能否承受 rollout；不要从算法名出发。**

再进一步，工程上真正需要落地的是：先回答四个门槛：有没有可靠 reward、需不需要探索、偏好数据是否静态、rollout 系统能否承受；再从 SFT/DPO/online RL 中选择，而不是按“先进程度”排序。

### 15.2 机制链：输入 → 估计 → 更新 → 行为 → 评测

建议把本题按下面的因果链讲清楚：

1. **输入分布**：样本/trajectory 来自哪里？是否与当前 policy 一致？是否存在 selection bias？
2. **训练信号**：监督标签、preference、reward、advantage 或系统指标具体由谁产生？噪声和尺度如何控制？
3. **优化更新**：哪个参数被更新？梯度是按 token、sequence、group 还是 trajectory 聚合？
4. **行为变化**：模型概率分布应该发生什么方向的变化？若没有发生，优先怀疑哪一层？
5. **独立验证**：至少使用一个不参与训练信号构造的 held-out evaluator，避免“训练 proxy 自证成功”。

本题 PDF 的深入结论是：决策顺序：有没有可靠 reward/verifier？是否需要探索新轨迹？数据是静态 pair 还是可以在线生成？系统是否 承担 rollout 成本？这比“哪个算法更新”更重要。把它变成研究问题时，需要追问：**哪一个可观测量能够证伪这句话？** 如果无法设计证伪实验，说明理解仍停留在概念层。

### 15.3 数学与数值实现的专业要求

本题未必需要单一闭式公式，但仍应把关键量形式化：输入分布、优化对象、约束、成本与观测指标。能把工程问题写成可测量变量，本身就是算法能力的一部分。

工程上建议始终保存原始统计量，不要只保存均值。例如 ratio/reward/length/KL 至少保留分位数或 histogram；大量 RL failure 都发生在尾部，而不会先体现在 mean 上。

## 16. 工程实现：最小可验证闭环

```text
# Interview-to-engineering skeleton for Q010
def investigate(problem):
    assumptions = define_scope(problem)
    baseline = build_minimal_baseline(assumptions)
    metrics = instrument(baseline)
    failure = reproduce_and_slice(metrics)
    hypothesis = connect_failure_to_mechanism(failure)
    result = run_controlled_ablation(hypothesis)
    return validate_on_heldout_and_regression(result)
```

### 16.1 实现检查表

- **数据身份**：每条样本能追溯 `dataset_version / prompt_id / policy_version / reward_version` 中适用的字段。
- **mask 与长度**：明确 prompt token、response token、padding、EOS、truncation 是否进入 loss/reward/normalization。
- **数值稳定**：logprob 差优先在 log-space 计算；标准化必须显式加 epsilon；极端值要记录而不是静默丢弃。
- **可复现性**：模型 checkpoint、tokenizer/chat template、随机 seed、生成参数、verifier 版本全部进入实验元数据。
- **独立评测**：训练 reward/judge 与最终评测至少有一层独立实现或独立数据。
- **失败可回放**：保留能还原单条 trajectory 的最小日志，而不是只有 aggregate dashboard。

### 16.2 一个真实项目场景

假设你在做一个 32B 通用助手的 SFT，原始池 300 万条，最终只能训练 30 万条；你的设计必须回答“删谁、留谁、怎么证明删得对”。

如果面试官把本题放进这个场景，回答时不要先给算法名。先给**约束、基线和最小实验**，再说明为什么某个算法/数据策略是由 failure mode 推出来的。

## 17. 指标仪表盘与实验设计

### 17.1 本题优先监控的指标

| # | 指标 | 如何解释 |
|---:|---|---|
| 1 | `reward quantiles` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 2 | `reward calibration` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 3 | `queue depth` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 4 | `data age` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 5 | `chosen-rejected margin` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 6 | `effective tokens` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 7 | `dedup rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 8 | `filter keep-rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |

### 17.2 推荐的三层实验

**Layer A — correctness test**：在 toy data / 小模型上验证符号、mask、归一化、版本和边界条件。例如把 reward 固定成常量、构造全对/全错 group、手工设置正负 advantage，确认梯度方向。

**Layer B — mechanism ablation**：固定模型、数据、总 token、rollout budget、seed，只改本题对应机制。目标不是追最高点，而是验证预期中间量是否变化，例如 entropy、group std、clip fraction、length distribution。

**Layer C — scaling test**：在更长 context、更大模型、更大 batch、更异步的设置下验证结论是否保持。很多方法在单机 toy case 正确，但在 policy lag、MoE routing 或重尾长度下失效。

### 17.3 怎样避免“伪 ablation”

- 总训练 step 相同但 rollout token 不同，不是等 compute。
- 数据条数相同但平均长度不同，不是等 token。
- 一个方案使用更强 judge/verifier，不能把增益全部归因于 optimizer。
- 系统吞吐变快导致看到更多样本，也会改变学习曲线；算法质量与系统效率需要拆开报告。

## 18. 反事实、边界条件与方法比较

### 18.1 三个必须会回答的反事实

1. **如果去掉本题机制，最早会坏哪个指标？** 先说中间量，再说最终 benchmark。
2. **如果把模型/长度/batch 放大 10×，哪个假设最先失效？** 优先考虑 estimator variance、memory、communication、policy freshness 与 evaluator reliability。
3. **如果训练 reward 很好但独立评测不涨，怎样证明不是 reward hacking 或数据泄漏？** 给出 held-out evaluator、行为切片、top-reward audit 与污染检查。

### 18.2 与相邻题目的关系

本题不是孤立知识点。它应被放回本章主线：**把 base model 的通用能力塑造成目标行为分布**。面试中如果能主动说明“当前方法解决了什么 failure，同时引入了什么新成本/新偏差”，通常比继续罗列算法名更有区分度。

### 18.3 常见高级误区

- 把论文中的**目标函数**当成完整系统；真实结果还取决于 sampling、版本、mask、normalization、scheduler 与 evaluator。
- 把 correlation 当 causal evidence；例如长度与 reward 同涨，不等于“更长 reasoning 导致能力提升”。
- 只比较最终分数，不比较 compute、variance、稳定性和回归项。
- 只描述成功 recipe，不解释它在什么分布、模型规模和 verifier 假设下成立。

## 19. 面试评分 Rubric：怎样从 60 分答到 95 分

| 档位 | 面试表现 |
|---|---|
| 60–70 | 能复述核心结论：SFT 解决“学会目标行为模板”；DPO 解决“离线偏好排序”；Online RL 解决“通过新采样探索并最大化可计 算 reward” |
| 70–80 | 能解释机制，并写出适用的公式/数据流；知道一个主要 failure mode。 |
| 80–90 | 能给出工程实现、关键监控指标、最小 ablation，并讨论 bias/variance 或系统成本。 |
| 90–95+ | 能处理反事实和规模化约束；从真实 failure 反推算法选择；能说明为什么**不选**另一个常见方案。 |

**本题难度 L3 的最低合格线**：需要能推导/拆解目标函数，讨论 bias-variance 或系统 trade-off，并给出监控指标。

## 20. 复习与项目化清单

在认为自己“掌握 Q010”之前，至少能独立完成：

- [ ] 不看资料给出 30 秒结论，不混淆概念边界。
- [ ] 白板写出关键公式/变量关系，逐项解释数据从哪里来。
- [ ] 画出端到端数据流，并标出最可能的三个 failure point。
- [ ] 给出至少一个能证伪自己判断的 controlled ablation。
- [ ] 给出一组线上/离线监控指标，以及一个异常时的排查顺序。
- [ ] 用自己的项目数字重述本题：模型规模、数据量、G/长度、GPU、吞吐、收益或回归。
- [ ] 回答“为什么不用另一种方法”，并明确 trade-off 而不是说“效果更好”。

<!-- V2_EXPERT_END -->

---

[← Q009](../01-sft-data/q009-sft-cold-start-pure-rl.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q011 →](../02-reward-model/q011-reward-model-bradley-terry.md)
