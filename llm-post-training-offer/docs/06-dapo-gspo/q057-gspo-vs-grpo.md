---
id: Q057
title: "公开真题：GSPO 与 GRPO 的核心区别是什么？"
chapter: 6
chapter_title: "DAPO / GSPO"
type: "公开真题"
level: L4
priority: high
tags: [grpo, gspo, reward]
source_refs: [I3, I11, P10, P9]
---

# Q057 · 公开真题：GSPO 与 GRPO 的核心区别是什么？

> **题型**：公开真题 · **难度**：L4 · **优先级**：🔥 高频 20 题
>
> **来源说明**：下方“PDF 原始提要”严格来自《剑指 LLM 后训练 Offer》；“扩展讲义”是在此基础上结合公开论文与工程实践做的补充分析。

[← Q056](../06-dapo-gspo/q056-overlong-reward-shaping.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q058 →](../06-dapo-gspo/q058-gspo-length-normalization.md)

## 1. 题目定位

### 面试官为什么问

考察你是否能把概念放进完整后训练链路，并从目标函数、数据分布与系统约束解释选择，而不是复述论文摘要。

### PDF 原始核心结论

GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10]

### PDF 原始深入理解

其 sequence ratio 本质是每 token likelihood ratio 的几何平均，降低长序列与局部数值误差带来的不稳定，并 与 sequence reward 更一致。

### PDF 原始常见失分点

只说“GSPO 更稳定”。

## 2. 面试回答阶梯

### 30 秒版

GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10]

### 2 分钟版

1. 先给核心判断：GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10]
2. 再解释机制：其 sequence ratio 本质是每 token likelihood ratio 的几何平均，降低长序列与局部数值误差带来的不稳定，并 与 sequence reward 更一致。
3. 最后补一个边界条件或失败模式：GSPO 把 importance ratio、clipping 与优化粒度提升到 sequence 级，直接针对 token-ratio 噪声和长期训练稳定性。

### 5 分钟版

按 **先说 GRPO failure → 对应 DAPO/GSPO 修改 → 粒度与公式 → 训练现象 → 何时值得使用** 展开。不要一开始堆算法名；先明确问题的优化对象、数据分布和约束，再把公式、工程实现和评测接上。

## 3. Know-Why：为什么这个问题重要

GSPO 把 importance ratio、clipping 与优化粒度提升到 sequence 级，直接针对 token-ratio 噪声和长期训练稳定性。

**failure-driven 视角**：DAPO/GSPO 不应背成名词列表；每个修改都要对应 entropy、无效 group、长度 weighting、ratio 噪声或 MoE mismatch。

**粒度视角**：token、sequence、group 是不同 normalization / importance / loss aggregation 粒度，改变粒度会改变估计量性质。

## 4. Know-How：面试与工程上怎么做

回答时建议按照下面的顺序组织，而不是直接背结论：

1. **定义边界**：先明确本题讨论的 policy/data/reward/system 粒度与假设。
2. **写出机制**：能写公式就写公式；不能写公式就画数据流或因果链。
3. **给可观测量**：说明训练时具体看什么日志、分布和系统指标。
4. **给 failure mode**：至少讲一个“什么时候这套方法会失效”。
5. **给验证实验**：用受控 ablation 证明你的判断。

**规模化视角**：前沿 RL 算法必须与 rollout 系统、MoE routing、policy freshness 一起理解。

## 5. 公式 / 白板推导

\[s_i(\theta)=\left(\frac{\pi_\theta(y_i|x)}{\pi_{old}(y_i|x)}\right)^{1/|y_i|}\]

> 白板要求：每写一个符号，都能回答“它由谁计算、在哪个阶段产生、数值异常时说明什么”。

## 6. 算法或系统流程

```text
sample sequence y with old policy
compute sequence log-ratio = mean_t(logp_new_t - logp_old_t)
ratio = exp(sequence log-ratio)
apply sequence-level clipping
optimize sequence advantage
```

## 7. 复杂度与工程成本

成本重点转向更长 rollout、有效 group 比率、sequence/token normalization 以及 MoE/分布式稳定性。

在项目里至少把成本量化为 **GPU-hours / rollout tokens / peak memory / communication / labeling or verifier cost** 中适用的几项，而不是只说“更省”。

## 8. Failure Modes 与诊断

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| entropy 快速塌缩 | 正向探索受限 | Clip-Higher/采样温度/难度调度 |
| 有效 group 比例低 | 全对/全错过多 | Dynamic Sampling |
| 长序列训练不稳定 | length weighting / ratio noise | 检查 token-vs-sequence normalization，考虑 GSPO |

### 本题特有风险

- 只说“GSPO 更稳定”。
- 边界条件：GSPO 把 importance ratio、clipping 与优化粒度提升到 sequence 级，直接针对 token-ratio 噪声和长期训练稳定性。
- 若训练曲线与理论预期相反，优先检查数据/版本/归一化/掩码是否和公式假设一致，再调超参。

## 9. 推荐实验与 Ablation

| 项目 | 建议设计 |
|---|---|
| Baseline | 同模型、同 rollout token budget、同 verifier |
| 优化变量 | 单独改变 clip/baseline/normalization/sampling 等一个机制 |
| 训练统计 | reward、KL、entropy、ratio quantiles、有效样本率 |
| 任务指标 | pass@1 / pass@k / held-out benchmark / length-controlled score |
| 系统指标 | rollout tokens/s、learner utilization、p95/p99 length、staleness |
| 判断 | 质量提升必须能覆盖 compute 增量与稳定性风险 |

## 10. 面试官连续追问树

1. 为什么优化单位和 reward 单位的一致性重要？ [I3][I11]
2. sequence-level ratio 为什么可能更稳定？
3. GSPO 下 sequence clipping 与 token clipping 的梯度差异是什么？
4. 这个改动解决的是估计量问题还是系统问题？
5. 长 CoT 与 MoE 下最容易出现哪类 train-inference mismatch？
6. 怎样设计 ablation 证明该 trick 必要？

### 追问回答原则

不要把每个追问当新题。沿同一条因果链回答：**假设 → 机制 → 可观测量 → 反例 → 实验**。如果能把上一问的 failure mode 自然推成下一问的算法选择，通常比背更多术语更有说服力。

## 11. 项目映射模板

把下面字段替换成你自己的项目数字；面试时“具体数字 + 失败案例 + ablation”比泛泛而谈更可信。

- **先给 failure**：entropy collapse / ineffective groups / long-CoT weighting / MoE mismatch。
- **再给改动**：只引入能对应 failure 的 DAPO/GSPO 机制。
- **Ablation**：单独开关 trick，控制 rollout token budget 与训练 steps。
- **证据**：同时给质量、entropy、有效样本率、吞吐和稳定性曲线。

## 12. 一句话记忆

> **Q057：GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10]**

## 13. 参考资料

- **[I3] 公开面经**：[牛客：字节 大模型算法岗（CoT / GRPO / DAPO / GSPO）](https://www.nowcoder.com/discuss/921960727672299520)
- **[I11] 公开面经**：[牛客：字节大模型算法一面（2026-08）](https://www.nowcoder.com/feed/main/detail/94b11dafd5e94b89a3170f3c179a3012)
- **[P10] PDF/论文参考**：[Qwen Team — Group Sequence Policy Optimization / GSPO](https://arxiv.org/abs/2507.18071)
- **[P9] PDF/论文参考**：[Yu et al. — DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)

## 14. 关联题目

- [Q051 · 公开真题：DAPO 相比 GRPO 做了哪些核心改进？](q051-dapo-vs-grpo.md)
- [Q052 · 为什么 DAPO 需要 Clip-Higher？](q052-dapo-clip-higher.md)
- [Q053 · 公开真题：Dynamic Sampling 为什么有效？](q053-dapo-dynamic-sampling.md)
- [Q054 · 长 CoT 下 sequence-level normalization 为什么可能产生长度偏差？](q054-long-cot-length-normalization.md)
- [Q055 · Token-level Policy Gradient Loss 解决什么？](q055-token-level-policy-gradient.md)
- [Q056 · Overlong Reward Shaping 为什么比硬截断惩罚更稳？](q056-overlong-reward-shaping.md)

<!-- V2_EXPERT_START -->
## 15. V2 专业进阶：从“会答”到“能做研究/工程”

> **内容属性**：本节是基于 PDF 原始提要的扩展讲义。它不是对 PDF 原文的复述，而是把本题展开到真实后训练项目所需要的假设、实现、诊断与实验层级。

### 15.1 把题目还原成一个可研究的问题

本题不能停在“GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10]”。更专业的表述是先确定五个对象：

| 维度 | 本题应明确的内容 |
|---|---|
| Optimization objective | 修复 long-CoT/大规模 RL 中的稳定性与粒度失配 |
| Statistical unit | token aggregation 或 sequence ratio |
| 关键估计误差 | length weighting、entropy collapse、MoE mismatch |
| 系统承载 | 高吞吐 rollout + sequence/token statistics |
| Scale variable | 长序列 KV cache、有效样本、路由/后端一致性 |

对 **Q057**，最关键的机制判断是：**GSPO 把 importance ratio、clipping 与优化粒度提升到 sequence 级，直接针对 token-ratio 噪声和长期训练稳定性。**

再进一步，工程上真正需要落地的是：GSPO 的关键不是“把 ratio 平均一下”，而是把 policy update 的信赖与 clip 粒度上升到 sequence；这更匹配 sequence reward，并降低 token ratio 极端值的影响。

### 15.2 机制链：输入 → 估计 → 更新 → 行为 → 评测

建议把本题按下面的因果链讲清楚：

1. **输入分布**：样本/trajectory 来自哪里？是否与当前 policy 一致？是否存在 selection bias？
2. **训练信号**：监督标签、preference、reward、advantage 或系统指标具体由谁产生？噪声和尺度如何控制？
3. **优化更新**：哪个参数被更新？梯度是按 token、sequence、group 还是 trajectory 聚合？
4. **行为变化**：模型概率分布应该发生什么方向的变化？若没有发生，优先怀疑哪一层？
5. **独立验证**：至少使用一个不参与训练信号构造的 held-out evaluator，避免“训练 proxy 自证成功”。

本题 PDF 的深入结论是：其 sequence ratio 本质是每 token likelihood ratio 的几何平均，降低长序列与局部数值误差带来的不稳定，并 与 sequence reward 更一致。把它变成研究问题时，需要追问：**哪一个可观测量能够证伪这句话？** 如果无法设计证伪实验，说明理解仍停留在概念层。

### 15.3 数学与数值实现的专业要求

本题已有白板公式。专业回答应继续说明：**优化变量是谁、期望/归一化是按 token 还是 sequence、数据由哪个 policy 采样、极端值如何被 clip/normalize、公式假设在异步系统中何时失效**。

工程上建议始终保存原始统计量，不要只保存均值。例如 ratio/reward/length/KL 至少保留分位数或 histogram；大量 RL failure 都发生在尾部，而不会先体现在 mean 上。

## 16. 工程实现：最小可验证闭环

```text
sample sequence y with old policy
compute sequence log-ratio = mean_t(logp_new_t - logp_old_t)
ratio = exp(sequence log-ratio)
apply sequence-level clipping
optimize sequence advantage
```

### 16.1 实现检查表

- **数据身份**：每条样本能追溯 `dataset_version / prompt_id / policy_version / reward_version` 中适用的字段。
- **mask 与长度**：明确 prompt token、response token、padding、EOS、truncation 是否进入 loss/reward/normalization。
- **数值稳定**：logprob 差优先在 log-space 计算；标准化必须显式加 epsilon；极端值要记录而不是静默丢弃。
- **可复现性**：模型 checkpoint、tokenizer/chat template、随机 seed、生成参数、verifier 版本全部进入实验元数据。
- **独立评测**：训练 reward/judge 与最终评测至少有一层独立实现或独立数据。
- **失败可回放**：保留能还原单条 trajectory 的最小日志，而不是只有 aggregate dashboard。

### 16.2 一个真实项目场景

假设模型平均 CoT 从 1k 增长到 8k tokens，并且是 MoE；原先 GRPO 训练开始出现 entropy 下降、ratio 尾部异常与吞吐恶化。

如果面试官把本题放进这个场景，回答时不要先给算法名。先给**约束、基线和最小实验**，再说明为什么某个算法/数据策略是由 failure mode 推出来的。

## 17. 指标仪表盘与实验设计

### 17.1 本题优先监控的指标

| # | 指标 | 如何解释 |
|---:|---|---|
| 1 | `reward quantiles` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 2 | `reward calibration` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 3 | `entropy` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 4 | `positive/negative clip fraction` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 5 | `effective sample rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 6 | `response length p50/p95` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 7 | `sequence ratio` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 8 | `routing mismatch` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |

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

本题不是孤立知识点。它应被放回本章主线：**修复 long-CoT/大规模 RL 中的稳定性与粒度失配**。面试中如果能主动说明“当前方法解决了什么 failure，同时引入了什么新成本/新偏差”，通常比继续罗列算法名更有区分度。

### 18.3 常见高级误区

- 把论文中的**目标函数**当成完整系统；真实结果还取决于 sampling、版本、mask、normalization、scheduler 与 evaluator。
- 把 correlation 当 causal evidence；例如长度与 reward 同涨，不等于“更长 reasoning 导致能力提升”。
- 只比较最终分数，不比较 compute、variance、稳定性和回归项。
- 只描述成功 recipe，不解释它在什么分布、模型规模和 verifier 假设下成立。

## 19. 面试评分 Rubric：怎样从 60 分答到 95 分

| 档位 | 面试表现 |
|---|---|
| 60–70 | 能复述核心结论：GSPO 将 importance ratio、clipping 与优化单位提升到 sequence level，而 GRPO 通常在 token level 处理 ratio。[P10] |
| 70–80 | 能解释机制，并写出适用的公式/数据流；知道一个主要 failure mode。 |
| 80–90 | 能给出工程实现、关键监控指标、最小 ablation，并讨论 bias/variance 或系统成本。 |
| 90–95+ | 能处理反事实和规模化约束；从真实 failure 反推算法选择；能说明为什么**不选**另一个常见方案。 |

**本题难度 L4 的最低合格线**：需要能处理反例、实现细节、分布式/规模化约束，并从 failure 反推方法选择。

## 20. 复习与项目化清单

在认为自己“掌握 Q057”之前，至少能独立完成：

- [ ] 不看资料给出 30 秒结论，不混淆概念边界。
- [ ] 白板写出关键公式/变量关系，逐项解释数据从哪里来。
- [ ] 画出端到端数据流，并标出最可能的三个 failure point。
- [ ] 给出至少一个能证伪自己判断的 controlled ablation。
- [ ] 给出一组线上/离线监控指标，以及一个异常时的排查顺序。
- [ ] 用自己的项目数字重述本题：模型规模、数据量、G/长度、GPU、吞吐、收益或回归。
- [ ] 回答“为什么不用另一种方法”，并明确 trade-off 而不是说“效果更好”。

<!-- V2_EXPERT_END -->

---

[← Q056](../06-dapo-gspo/q056-overlong-reward-shaping.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q058 →](../06-dapo-gspo/q058-gspo-length-normalization.md)
