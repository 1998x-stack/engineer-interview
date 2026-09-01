# 实验设计 Playbook：如何证明一个 Post-Training 改动真的有效

## 1. 先写“预注册式”实验卡

在开跑前写清：

- Hypothesis：机制假设是什么？
- Prediction：哪个中间量先变化？
- Primary metric：最终判断指标是什么？
- Guardrails：哪些能力不能回退？
- Compute control：如何保证 token/GPU-hours/verifier 等价？
- Stop condition：什么情况提前判定失败？

## 2. 常用对照矩阵

| 问题 | A | B | 需要固定 |
|---|---|---|---|
| 数据筛选有效吗 | raw mixture | filtered mixture | 有效 token、steps、model |
| DPO beta 是否合适 | beta1 | beta2 | pairs、reference、steps |
| GRPO G 是否值得 | G1 | G2 | 总 rollout token budget |
| DAPO trick 是否有效 | off | on | 其它 trick、compute |
| 系统调度是否有效 | scheduler A | B | workload、hardware、quality |
| PRM 是否有效 | ORM | ORM+PRM | reward compute、rollout budget |

## 3. 结果报告模板

不要只报“+2.3”。至少报告：

- quality：pass@1/pass@k/win-rate/benchmark
- behavior：length、entropy、diversity、format/safety
- optimization：KL、ratio、clip fraction、grad norm、group std
- system：tokens/s、GPU active ratio、memory、p99、staleness
- cost：GPU-hours、rollout tokens、judge/verifier calls
- regression：下降的能力与失败样本类别

## 4. 结论写法

专业结论应该是：

> 在固定 X/Y/Z 的条件下，改动 A 使中间量 M 朝机制预期变化，同时主指标 P 提升、guardrail G 不回退；增益在 seed/长度/难度分桶中保持，代价是 C。因此证据支持“机制 H 在当前设置下成立”，而不是笼统声称“A 优于 B”。


<!-- PROFESSIONAL_FOOTER -->
## 使用建议

把本页内容与具体问题文件联动使用：先选一个 Qxxx，按本页模板做白板/实验/项目复盘；记录自己无法回答的变量、指标和反例，再回到对应章节补齐。目标是形成**可迁移的问题解决结构**，而不是增加背诵量。
