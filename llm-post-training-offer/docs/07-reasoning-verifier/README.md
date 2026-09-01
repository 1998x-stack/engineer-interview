# 第 7 章 · Reasoning RL、Verifier 与 Credit Assignment

> 探索、可验证奖励、稀疏奖励、熵与 hacking

## 本章目标

**探索视角**：reasoning RL 的价值来自闭环搜索，但探索只有在 reward 足够可靠且正信号不太稀疏时才有效。

**credit 视角**：ORM/PRM、token/sequence reward、length shaping 都在回答“哪一步应该被强化”。

**抗作弊视角**：verifier 不是 ground truth 本身；parser/test/judge 都要做对抗验证。

## 回答框架

**任务可验证性 → reward 稠密度 → exploration → credit assignment → hacking → eval**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q061 · 为什么 Online RL 可能提升 reasoning，而 SFT 不一定？](q061-online-rl-reasoning.md) | 原理推导 | L3 |  |
| [Q062 · RL 是“创造能力”还是“激活已有能力”？](q062-rl-create-vs-elicit.md) | 系统设计 | L4 |  |
| [Q063 · 为什么数学/代码 RL 比 open-ended chat RL 更容易？](q063-verifiable-vs-open-ended-rl.md) | 原理推导 | L2 |  |
| [Q064 · Process Reward 一定比 Outcome Reward 好吗？](q064-process-vs-outcome-reward.md) | 系统设计 | L3 |  |
| [Q065 · Sparse Reward 如何改善？](q065-sparse-reward.md) | 系统设计 | L3 |  |
| [Q066 · 如何避免模型把“更长 CoT”误学成“更高能力”？](q066-cot-length-vs-capability.md) | 系统设计 | L3 |  |
| [Q067 · Entropy collapse 是什么？为什么 GRPO/DAPO 特别关注？](q067-entropy-collapse.md) | 原理推导 | L3 |  |
| [Q068 · 为什么只看训练 reward 非常危险？](q068-train-reward-is-not-enough.md) | 高频题 | L2 |  |
| [Q069 · Rule-based verifier 也会被 hacking 吗？](q069-verifier-hacking.md) | 系统设计 | L3 |  |
| [Q070 · 如何设计一个“好 Reward”？](q070-good-reward-design.md) | 系统设计 | L4 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| 准确率涨但长度暴涨 | length shortcut | length-controlled metric + efficiency reward |
| reward 很高但答案异常 | verifier exploit | 对抗测试 verifier/parser/test |
| 采样越来越同质 | entropy collapse | 提高探索与任务难度，监控 group diversity |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：让策略通过可验证反馈探索更好的 reasoning trajectory
- **Unit of optimization**：trajectory / step / token
- **主要统计偏差**：sparse credit、reward hacking、test-time compute confound
- **系统载体**：sampler + verifier/PRM + evaluation
- **规模化变量**：pass@k/group sampling、verifier cost、长 CoT

### 本章必须会看的指标

- `pass@1/pass@k`
- `verifier precision`
- `reward sparsity`
- `trajectory diversity`
- `accuracy/token`
- `entropy`
- `independent eval gap`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：以章节内 L3/L4 题为主。

### 章节级案例

假设数学/代码任务有可靠终局 verifier，但过程 reward 不完美；你要决定 credit 粒度、探索强度与 anti-hacking 方案。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

