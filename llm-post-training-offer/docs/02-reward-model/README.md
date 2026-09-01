# 第 2 章 · Preference、Reward Model 与 Reward Design

> 偏好数据、BT 模型、Reward Hacking、Verifier

## 本章目标

**统计建模视角**：Reward/Preference 通常只观察到相对标签或代理信号，要明确噪声模型、可识别性和 calibration 边界。

**Goodhart 视角**：一旦 reward 成为优化目标，policy 会主动搜索 proxy 的漏洞；因此 held-out evaluator 必须独立。

**产品视角**：帮助性、正确性、安全、风格常常冲突，硬约束与软 reward 要分层设计。

## 回答框架

**定义 reward/preference → 统计假设 → 数据生成 → proxy failure → 检测与修复**

## 题目列表

| 题目 | 类型 | 难度 | 高频 |
|---|---|---:|:---:|
| [Q011 · Reward Model 如何训练？Bradley-Terry 假设是什么？](q011-reward-model-bradley-terry.md) | 高频题 | L2 | 🔥 |
| [Q012 · 公开真题：PPO 中的 Reward Model 数据从哪里来？](q012-reward-model-data-source.md) | 公开真题 | L2 |  |
| [Q013 · Preference pair 的 margin、难度和 annotator agreement 为什么重要？](q013-preference-margin-agreement.md) | 原理推导 | L2 |  |
| [Q014 · 如何处理不同标注员之间的 preference disagreement？](q014-annotator-disagreement.md) | 系统设计 | L3 |  |
| [Q015 · Reward Model 为什么会被 policy exploit？](q015-reward-model-exploitation.md) | 原理推导 | L3 |  |
| [Q016 · 公开真题：什么是 Reward Hacking？常见类型有哪些？](q016-reward-hacking-types.md) | 公开真题 | L2 | 🔥 |
| [Q017 · 如何系统检测 Reward Hacking？](q017-detect-reward-hacking.md) | 系统设计 | L3 |  |
| [Q018 · Outcome Reward 与 Process Reward 有什么本质差异？](q018-outcome-vs-process-reward.md) | 高频题 | L3 |  |
| [Q019 · 多个 Reward / Judge 如何组合？](q019-multi-reward-composition.md) | 系统设计 | L3 |  |
| [Q020 · 为什么 rule-based verifier 是 RLVR 的关键基础设施？](q020-rule-verifier-rlvr.md) | 原理推导 | L2 |  |

## 本章诊断速查

| 现象 | 优先假设 | 第一检查项 |
|---|---|---|
| proxy reward 持续涨，独立评分不涨 | reward hacking / OOD | 审计 top reward 尾部；引入独立 verifier/judge |
| 标注一致率低 | 任务主观或 pair 太接近 | 分群/软标签/过滤低置信 pair |
| RM 对长度高度相关 | verbosity bias | 做 length-controlled evaluation 和去偏 |

## 本章学习方法

1. 先把 10 题都练到 60 秒结构化回答。
2. 再选择高优先级题手推公式或画系统图。
3. 最后用自己的项目替换抽象变量：模型规模、数据量、G、max tokens、GPU、reward、benchmark。
4. 每章至少准备一个真实失败案例，以及一个能推翻自己原始假设的 ablation。

<!-- CHAPTER_V2_START -->
## V2 · 本章工程与研究 Dashboard

### 本章的统一问题定义

- **Objective**：把人类/规则偏好映射成可优化的相对质量信号
- **Unit of optimization**：pair / response / reward component
- **主要统计偏差**：annotator noise、proxy gap、OOD exploitation
- **系统载体**：label/judge/verifier + RM service
- **规模化变量**：标注成本、judge latency、reward refresh 周期

### 本章必须会看的指标

- `pair accuracy`
- `AUC/calibration`
- `reward margin`
- `annotator agreement`
- `reward-vs-length correlation`
- `OOD/top-reward audit rate`

### 推荐学习顺序

1. **定义与机制**：先能解释本章每个变量和数据来源。
2. **目标函数/数据流**：能在白板上从输入画到 loss/reward，再画到更新。
3. **failure-driven**：每学一个机制，都回答“没有它会坏什么”。
4. **系统化**：把 wall-clock、memory、policy freshness 与 quality 放到同一张图。
5. **项目化**：用自己做过的模型规模和真实数字替换书中的抽象变量。

本章高优先题：Q011, Q016。

### 章节级案例

假设 preference 数据来自三种来源：人工标注、强模型 judge、规则 verifier；三者成本与噪声不同，你需要设计可校准的 reward pipeline。

把 10 道题放进同一个案例连续回答，比单题背诵更接近二面/三面的真实形式。
<!-- CHAPTER_V2_END -->

