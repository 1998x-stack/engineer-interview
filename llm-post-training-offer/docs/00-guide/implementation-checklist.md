# 后训练工程实现检查表

这份 checklist 用于 code review、实验启动前检查和面试项目复盘。

## Data / Tokenization

- [ ] tokenizer、special token、chat template 与 reference/rollout/learner 完全一致。
- [ ] 明确 loss mask：prompt、assistant、tool observation、padding、EOS、truncated token。
- [ ] 数据可追溯到 source/version；train/eval contamination 有独立检查。
- [ ] 长度、领域、难度、语言、来源分布进入 dashboard。

## Policy / LogProb

- [ ] old/current/rollout/reference policy 角色与版本能区分。
- [ ] logprob 在相同 tokenization、mask 与 precision 下计算。
- [ ] ratio 使用 log-space 差，保存 p1/p50/p99 和极端样本。
- [ ] 对 padding/EOS/工具 token 的 ratio/advantage 处理有单元测试。

## Reward / Verifier

- [ ] reward scale、normalization、clipping、missing/timeout 明确定义。
- [ ] verifier 有独立 adversarial/regression set。
- [ ] reward top tail 定期人工或独立 judge 审计。
- [ ] 训练 evaluator 与最终 evaluator 至少一层独立。

## Distributed / System

- [ ] peak memory 分解到 param/grad/optimizer/activation/KV/buffer。
- [ ] rollout tokens/s、learner tokens/s、GPU active ratio、queue depth、p99 latency 可观测。
- [ ] weight sync 有版本号、失败恢复与最大 staleness 策略。
- [ ] 单卡/多卡数值一致性有 smoke test。

## Evaluation / Release Gate

- [ ] benchmark 不只看总分，按任务/难度/长度/语言切片。
- [ ] 记录 KL、entropy、长度、拒答、格式、diversity 等行为指标。
- [ ] 关键能力 regression 设硬门槛。
- [ ] 发布前有 reward hacking/verifier hacking 专项测试。
