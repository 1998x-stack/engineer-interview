# 第 5 章 · GRPO

> group-relative baseline、token credit、off-policy 与 rollout

## 本章目标

**估计量视角**：GRPO 用 group Monte Carlo baseline 取代 learned critic，降低模型状态成本但依赖组内 reward 方差。

**吞吐视角**：G 条 rollout 使 decode token 成本显著，group size 与有效样本率必须一起看。

**off-policy 视角**：异步流水线里 policy version 是一等公民；所有 ratio/clip 解释都要建立在版本正确上。

## 回答框架

**PPO baseline → 去 critic 的动机 → group advantage → token/sequence credit → rollout/off-policy 工程**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q041 · 公开真题：PPO 与 GRPO 最大区别是什么？](q041-ppo-vs-grpo.md) | 公开真题 | L2 | 🔥 |
| [Q042 · 为什么 group-relative baseline 能替代 Critic？](q042-group-relative-baseline.md) | 原理推导 | L3 | 🔥 |
| [Q043 · GRPO 去掉 Critic 后，真正的成本转移到了哪里？](q043-grpo-cost-transfer.md) | 系统设计 | L3 |  |
| [Q044 · 公开真题：Sequence-level reward 如何传到 token？credit assignment 有什么问题？](q044-sequence-reward-token-credit.md) | 公开真题 | L3 | 🔥 |
| [Q045 · 为什么 group 内全对或全错时 GRPO 基本没有有效梯度？](q045-grpo-all-correct-all-wrong.md) | 原理推导 | L3 |  |
| [Q046 · Group size G 越大越好吗？](q046-grpo-group-size.md) | 系统设计 | L3 |  |
| [Q047 · 公开真题：πθ、πold、πrollout 分别是什么？为什么工程中可能不相等？](q047-policy-old-rollout.md) | 公开真题 | L3 |  |
| [Q048 · 公开真题：batch 很大时为什么 GRPO 会越来越 off-policy？](q048-grpo-large-batch-off-policy.md) | 公开真题 | L4 |  |
| [Q049 · 如何缓解 policy lag？同步 RL 与异步 RL 各自适合什么？](q049-policy-lag-sync-async.md) | 系统设计 | L4 |  |
| [Q050 · 为什么 GRPO 特别适合数学/代码等 verifiable tasks？](q050-grpo-verifiable-tasks.md) | 原理推导 | L2 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| 大量 group std≈0 | prompt 过易/过难 | 动态采样/难度调度 |
| importance ratio 重尾 | policy lag / update 过多 | version bound、减少 epoch、丢弃 stale samples |
| rollout tokens 暴涨 | G/length 太大 | 调 group size、token budget、bucketing |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：用同 prompt 的组内相对 reward 替代 learned critic
- **Unit of optimization**：group / sequence advantage / token logprob
- **主要统计偏差**：group degeneracy、粗粒度 credit、staleness
- **系统载体**：rollout pool + verifier + learner + versioning
- **规模化变量**：G×rollout tokens、verifier、有效 group 比

### 本章必须会看的指标

- `group reward mean/std`
- `effective-group ratio`
- `pass@k`
- `ratio quantiles`
- `entropy`
- `policy-version lag`
- `useful rollout tokens/s`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q041, Q042, Q044。

### 章节级案例

假设数学 reasoning 任务每个 prompt 采 8 条长 CoT，verifier 是 0/1；你需要在 rollout 成本、group 信号与稳定性之间取舍。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

