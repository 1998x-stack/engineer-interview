---
id: Q093
title: "公开真题：Tool Calling / Function Calling 数据怎么构造？"
chapter: 10
chapter_title: "Agentic RL 与系统设计"
type: "公开真题"
level: L3
priority: normal
tags: [agentic-rl]
source_refs: [P8, R1]
---

# Q093 · 公开真题：Tool Calling / Function Calling 数据怎么构造？

> **题型**：公开真题 · **难度**：L3 · **优先级**：常规
>
> **来源说明**：下方“PDF 原始提要”严格来自《剑指 LLM 后训练 Offer》；“扩展讲义”是在此基础上结合公开论文与工程实践做的补充分析。

[← Q092](../10-agentic-rl/q092-agentic-credit-assignment.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q094 →](../10-agentic-rl/q094-agent-reward-design.md)

## 1. 题目定位

### 面试官为什么问

考察你是否能把概念放进完整后训练链路，并从目标函数、数据分布与系统约束解释选择，而不是复述论文摘要。

### PDF 原始核心结论

覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases。

### PDF 原始深入理解

只训练正确 tool call 会造成 over-calling；Agent 数据的难点是状态转移与异常恢复，不只是 JSON 格式。

### PDF 原始常见失分点

只做 schema 格式 SFT。

## 2. 面试回答阶梯

### 30 秒版

覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases。

### 2 分钟版

1. 先给核心判断：覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases。
2. 再解释机制：只训练正确 tool call 会造成 over-calling；Agent 数据的难点是状态转移与异常恢复，不只是 JSON 格式。
3. 最后补一个边界条件或失败模式：tool-calling 数据不能只教“怎么调用”，还要教“何时不调用、选哪个工具、参数怎么填、失败后怎么恢复、如何基于 observation 继续”。

### 5 分钟版

按 **定义 state/action/observation/reward → horizon/credit → tool/environment → 系统 → 评测与安全约束** 展开。不要一开始堆算法名；先明确问题的优化对象、数据分布和约束，再把公式、工程实现和评测接上。

## 3. Know-Why：为什么这个问题重要

tool-calling 数据不能只教“怎么调用”，还要教“何时不调用、选哪个工具、参数怎么填、失败后怎么恢复、如何基于 observation 继续”。

**MDP 视角**：Agent 的 state/action/observation/horizon 比单轮文本任务复杂，环境本身是训练系统的一部分。

**reward 视角**：终局成功、过程进展、工具成本、无效动作与安全约束要分层，而不是堆成一个随意加权的标量。

## 4. Know-How：面试与工程上怎么做

回答时建议按照下面的顺序组织，而不是直接背结论：

1. **定义边界**：先明确本题讨论的 policy/data/reward/system 粒度与假设。
2. **写出机制**：能写公式就写公式；不能写公式就画数据流或因果链。
3. **给可观测量**：说明训练时具体看什么日志、分布和系统指标。
4. **给 failure mode**：至少讲一个“什么时候这套方法会失效”。
5. **给验证实验**：用受控 ablation 证明你的判断。

**项目答辩视角**：高级回答必须能把算法、环境、系统和 ablation 串成一条研究决策链。

## 5. 公式 / 白板推导

本题重点不在死记单一公式，而在明确优化对象、数据分布和 failure mode。建议把相关目标函数与监控量写在同一张白板上。

> 白板要求：每写一个符号，都能回答“它由谁计算、在哪个阶段产生、数值异常时说明什么”。

## 6. 算法或系统流程

```text
intent
 -> should_call_tool?
 -> tool selection
 -> argument generation
 -> execution / error
 -> observation grounding
 -> retry / alternate tool / stop
 -> final answer
```

## 7. 复杂度与工程成本

环境执行和 tool latency 可能比模型本身更慢；还要计入失败重试、长 horizon 与外部服务成本。

在项目里至少把成本量化为 **GPU-hours / rollout tokens / peak memory / communication / labeling or verifier cost** 中适用的几项，而不是只说“更省”。

## 8. Failure Modes 与诊断

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| 成功率高但工具调用次数暴涨 | cost hacking | step cost + duplicate detection + budget |
| 长程任务失败集中在早期步骤 | credit/plan failure | trajectory slicing + intermediate progress verifier |
| tool error 后循环 | termination/recovery policy 缺失 | 明确 retry budget、fallback 与 stop condition |

### 本题特有风险

- 只做 schema 格式 SFT。
- 边界条件：tool-calling 数据不能只教“怎么调用”，还要教“何时不调用、选哪个工具、参数怎么填、失败后怎么恢复、如何基于 observation 继续”。
- 若训练曲线与理论预期相反，优先检查数据/版本/归一化/掩码是否和公式假设一致，再调超参。

## 9. 推荐实验与 Ablation

| 项目 | 建议设计 |
|---|---|
| Environment | 固定工具版本、超时、错误注入与预算 |
| Reward | success 与 process/cost 分开记录 |
| 轨迹指标 | steps、tool calls、invalid actions、retries、success |
| Ablation | 去掉 process reward / step cost / 某工具，观察策略变化 |
| 长程稳健性 | 按 horizon、环境噪声、工具失败率做分桶 |

## 10. 面试官连续追问树

1. 如何构造工具失败后的 recovery trajectories？
2. 如果工具返回错误/超时，策略应如何恢复？
3. 如何给长程任务做 credit 而不把路径写死？
4. Agent 成功率与工具成本冲突时，什么是 primary objective？

### 追问回答原则

不要把每个追问当新题。沿同一条因果链回答：**假设 → 机制 → 可观测量 → 反例 → 实验**。如果能把上一问的 failure mode 自然推成下一问的算法选择，通常比背更多术语更有说服力。

## 11. 项目映射模板

把下面字段替换成你自己的项目数字；面试时“具体数字 + 失败案例 + ablation”比泛泛而谈更可信。

- **环境**：state/action/observation、工具集合、max steps、失败返回。
- **Reward**：成功、进展、成本、非法动作分别怎么处理。
- **Credit**：终局 reward 如何分配到长 trajectory。
- **系统**：rollout 并发、环境 latency、staleness、重试策略。
- **评测**：task success、steps、tool error、cost、long-horizon robustness。

## 12. 一句话记忆

> **Q093：覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases。**

## 13. 参考资料

- **[P8] PDF/论文参考**：[Guo et al. — DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning](https://www.nature.com/articles/s41586-025-09422-z)
- **[R1] 工程资料**：[verl — Volcano Engine Reinforcement Learning for LLMs](https://github.com/verl-project/verl)

## 14. 关联题目

- [Q091 · 公开真题：什么是 Agentic RL？与单轮 reasoning RL 的状态空间有何不同？](q091-agentic-rl-state-space.md)
- [Q092 · 公开真题：Agentic RL 的 credit assignment 怎么做？](q092-agentic-credit-assignment.md)
- [Q094 · Agent reward 应如何设计？](q094-agent-reward-design.md)
- [Q095 · 如何防止 Agent 为了 reward 无限调用工具或重复搜索？](q095-agent-tool-loop-hacking.md)
- [Q096 · Multi-turn RL 与 single-turn RL 最大区别是什么？](q096-multi-turn-vs-single-turn-rl.md)
- [Q097 · 公开真题：长程任务为什么可能选 GRPO 而不是 PPO？](q097-long-horizon-grpo-vs-ppo.md)

<!-- V2_EXPERT_START -->
## 15. V2 专业进阶：从“会答”到“能做研究/工程”

> **内容属性**：本节是基于 PDF 原始提要的扩展讲义。它不是对 PDF 原文的复述，而是把本题展开到真实后训练项目所需要的假设、实现、诊断与实验层级。

### 15.1 把题目还原成一个可研究的问题

本题不能停在“覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases”。更专业的表述是先确定五个对象：

| 维度 | 本题应明确的内容 |
|---|---|
| Optimization objective | 在环境交互中优化长程任务成功、效率与安全 |
| Statistical unit | state-action-observation trajectory |
| 关键估计误差 | long-horizon credit、environment noise、tool hacking |
| 系统承载 | agent runtime + tools + environment + RL trainer |
| Scale variable | environment latency、steps/trajectory、tool budget |

对 **Q093**，最关键的机制判断是：**tool-calling 数据不能只教“怎么调用”，还要教“何时不调用、选哪个工具、参数怎么填、失败后怎么恢复、如何基于 observation 继续”。**

再进一步，工程上真正需要落地的是：工具数据一定包含 no-tool、wrong-tool、bad-args、tool-error、retry、stop 等负例；只教成功调用会让模型学成“遇事就 call”。

### 15.2 机制链：输入 → 估计 → 更新 → 行为 → 评测

建议把本题按下面的因果链讲清楚：

1. **输入分布**：样本/trajectory 来自哪里？是否与当前 policy 一致？是否存在 selection bias？
2. **训练信号**：监督标签、preference、reward、advantage 或系统指标具体由谁产生？噪声和尺度如何控制？
3. **优化更新**：哪个参数被更新？梯度是按 token、sequence、group 还是 trajectory 聚合？
4. **行为变化**：模型概率分布应该发生什么方向的变化？若没有发生，优先怀疑哪一层？
5. **独立验证**：至少使用一个不参与训练信号构造的 held-out evaluator，避免“训练 proxy 自证成功”。

本题 PDF 的深入结论是：只训练正确 tool call 会造成 over-calling；Agent 数据的难点是状态转移与异常恢复，不只是 JSON 格式。把它变成研究问题时，需要追问：**哪一个可观测量能够证伪这句话？** 如果无法设计证伪实验，说明理解仍停留在概念层。

### 15.3 数学与数值实现的专业要求

本题未必需要单一闭式公式，但仍应把关键量形式化：输入分布、优化对象、约束、成本与观测指标。能把工程问题写成可测量变量，本身就是算法能力的一部分。

工程上建议始终保存原始统计量，不要只保存均值。例如 ratio/reward/length/KL 至少保留分位数或 histogram；大量 RL failure 都发生在尾部，而不会先体现在 mean 上。

## 16. 工程实现：最小可验证闭环

```text
intent
 -> should_call_tool?
 -> tool selection
 -> argument generation
 -> execution / error
 -> observation grounding
 -> retry / alternate tool / stop
 -> final answer
```

### 16.1 实现检查表

- **数据身份**：每条样本能追溯 `dataset_version / prompt_id / policy_version / reward_version` 中适用的字段。
- **mask 与长度**：明确 prompt token、response token、padding、EOS、truncation 是否进入 loss/reward/normalization。
- **数值稳定**：logprob 差优先在 log-space 计算；标准化必须显式加 epsilon；极端值要记录而不是静默丢弃。
- **可复现性**：模型 checkpoint、tokenizer/chat template、随机 seed、生成参数、verifier 版本全部进入实验元数据。
- **独立评测**：训练 reward/judge 与最终评测至少有一层独立实现或独立数据。
- **失败可回放**：保留能还原单条 trajectory 的最小日志，而不是只有 aggregate dashboard。

### 16.2 一个真实项目场景

假设 agent 需要搜索、代码执行和结构化 API，多轮最长 30 steps；最终成功率稀疏且工具调用有真实成本。

如果面试官把本题放进这个场景，回答时不要先给算法名。先给**约束、基线和最小实验**，再说明为什么某个算法/数据策略是由 failure mode 推出来的。

## 17. 指标仪表盘与实验设计

### 17.1 本题优先监控的指标

| # | 指标 | 如何解释 |
|---:|---|---|
| 1 | `tool success/error rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 2 | `task success` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 3 | `steps/trajectory` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 4 | `tool calls` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 5 | `invalid-action rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 6 | `retry rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 7 | `latency/cost` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |
| 8 | `environment failure rate` | 用来验证本题对应机制是否按预期工作；必须与质量指标联合解释 |

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

本题不是孤立知识点。它应被放回本章主线：**在环境交互中优化长程任务成功、效率与安全**。面试中如果能主动说明“当前方法解决了什么 failure，同时引入了什么新成本/新偏差”，通常比继续罗列算法名更有区分度。

### 18.3 常见高级误区

- 把论文中的**目标函数**当成完整系统；真实结果还取决于 sampling、版本、mask、normalization、scheduler 与 evaluator。
- 把 correlation 当 causal evidence；例如长度与 reward 同涨，不等于“更长 reasoning 导致能力提升”。
- 只比较最终分数，不比较 compute、variance、稳定性和回归项。
- 只描述成功 recipe，不解释它在什么分布、模型规模和 verifier 假设下成立。

## 19. 面试评分 Rubric：怎样从 60 分答到 95 分

| 档位 | 面试表现 |
|---|---|
| 60–70 | 能复述核心结论：覆盖“是否需要工具 → 选哪个工具 → 参数 → 观察 → 继续推理 → final”，还必须有不该调用、参数错误、工 具失败、结果冲突等 negative cases |
| 70–80 | 能解释机制，并写出适用的公式/数据流；知道一个主要 failure mode。 |
| 80–90 | 能给出工程实现、关键监控指标、最小 ablation，并讨论 bias/variance 或系统成本。 |
| 90–95+ | 能处理反事实和规模化约束；从真实 failure 反推算法选择；能说明为什么**不选**另一个常见方案。 |

**本题难度 L3 的最低合格线**：需要能推导/拆解目标函数，讨论 bias-variance 或系统 trade-off，并给出监控指标。

## 20. 复习与项目化清单

在认为自己“掌握 Q093”之前，至少能独立完成：

- [ ] 不看资料给出 30 秒结论，不混淆概念边界。
- [ ] 白板写出关键公式/变量关系，逐项解释数据从哪里来。
- [ ] 画出端到端数据流，并标出最可能的三个 failure point。
- [ ] 给出至少一个能证伪自己判断的 controlled ablation。
- [ ] 给出一组线上/离线监控指标，以及一个异常时的排查顺序。
- [ ] 用自己的项目数字重述本题：模型规模、数据量、G/长度、GPU、吞吐、收益或回归。
- [ ] 回答“为什么不用另一种方法”，并明确 trade-off 而不是说“效果更好”。

<!-- V2_EXPERT_END -->

---

[← Q092](../10-agentic-rl/q092-agentic-credit-assignment.md) · [章节首页](README.md) · [总索引](../question-index.md) · [Q094 →](../10-agentic-rl/q094-agent-reward-design.md)
