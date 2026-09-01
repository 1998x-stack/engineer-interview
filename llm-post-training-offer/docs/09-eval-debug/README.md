# 第 9 章 · 训练稳定性、评测与 Debug

> 曲线诊断、ablation、数据/算法/系统归因

## 本章目标

**诊断视角**：先验证数据流和指标正确，再做算法归因；很多“算法不收敛”其实是版本、mask、reward 或分布式 bug。

**因果视角**：ablation 需要控制 compute/data/seed，只改变一个因子，并观察训练动态而不只是最终点。

**评测视角**：proxy、held-out benchmark、human/judge、线上行为与成本是不同层次，不应互相替代。

## 回答框架

**描述症状 → 建假设树 → 设计最小隔离实验 → 修复 → regression 防复发**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q081 · 公开真题：怎么判断一次 RL 训练“质量达标”？](q081-rl-training-quality-gate.md) | 公开真题 | L3 |  |
| [Q082 · Reward 一直涨但 benchmark 不涨，怎么排查？](q082-reward-up-benchmark-flat.md) | 系统设计 | L4 |  |
| [Q083 · KL 突然暴涨通常意味着什么？](q083-kl-spike-debug.md) | 系统设计 | L3 |  |
| [Q084 · Entropy 一路下降怎么办？](q084-entropy-down-debug.md) | 系统设计 | L3 |  |
| [Q085 · Reward variance 很大怎么办？](q085-reward-variance-debug.md) | 系统设计 | L3 |  |
| [Q086 · 为什么离线 benchmark 不能完全代表线上？](q086-offline-vs-online-eval.md) | 高频题 | L2 |  |
| [Q087 · 怎么做后训练 ablation 才可信？](q087-post-training-ablation.md) | 系统设计 | L3 |  |
| [Q088 · 为什么 SFT 变好但 RL 可能变差？](q088-sft-better-rl-worse.md) | 原理推导 | L4 |  |
| [Q089 · 如何构建 hard-example data flywheel？](q089-hard-example-data-flywheel.md) | 系统设计 | L3 |  |
| [Q090 · 如何判断问题来自数据、算法还是系统实现？](q090-data-vs-algorithm-vs-system.md) | 系统设计 | L4 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| 训练指标好但线上差 | eval distribution gap | 建立真实流量切片和 failure set |
| 不同 seed 结论反转 | 方差大 | 多 seed/置信区间；延长训练观察趋势 |
| 单卡正常多卡异常 | distributed bug | 固定 batch 对齐 logits/loss/grad，逐层比对 |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：把异常训练曲线转化为可证伪的分层诊断
- **Unit of optimization**：metric slice / checkpoint / minimal repro
- **主要统计偏差**：指标混淆、相关≠因果、不可复现
- **系统载体**：instrumentation + regression + experiment registry
- **规模化变量**：诊断迭代速度、复现成本、回归覆盖

### 本章必须会看的指标

- `reward/benchmark delta`
- `KL/entropy/grad norm`
- `metric slices`
- `seed variance`
- `regression failures`
- `time-to-reproduce`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：以章节内 L3/L4 题为主。

### 章节级案例

假设某次 RL 实验 reward 稳定上涨，但 held-out benchmark 3 天不动；你不能“再跑一轮看看”，必须设计最小诊断矩阵。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

