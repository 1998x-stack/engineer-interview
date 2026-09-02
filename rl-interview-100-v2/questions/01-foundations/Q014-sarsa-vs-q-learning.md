---
id: Q014
title: "SARSA 与 Q-learning 有什么区别？"
chapter: "第一章 MDP / Bellman / DP / MC / TD"
source_type: "经典母题"
frequency: "★★★★☆"
difficulty: "★★★☆☆"
roles: "全方向"
tags: ["q-learning", "value-based"]
---

# Q014 SARSA 与 Q-learning 有什么区别？

> **题型**：经典母题 ｜ **频率**：★★★★☆ ｜ **难度**：★★★☆☆ ｜ **岗位**：全方向  
> **来源层级**：本页“PDF 原始要点”来自仓库内原版 PDF；“Repo 扩展解析”是在不改变原结论的前提下新增的理论、工程与面试组织内容。

[← Q013](Q013-importance-sampling.md) · [章节首页](README.md) · [Q015 →](Q015-exploration-exploitation.md)

## 1. 面试官真正想确认什么

这不是单纯的名词解释题。面试官通常会顺着 **定义 → 数学对象 → 为什么有效 → 什么时候失效 → 如何实现/监控 → 如何迁移到项目** 连续追问。

把这道题放回 RL 的三条主线理解：**Bellman/Bootstrap** 决定价值如何递归传播，**Bias-Variance/Credit Assignment** 决定估计器是否稳定，**Distribution Shift** 决定采样数据还能否支持当前目标。面试时不要只报定义；应主动说明成立条件、估计误差从哪里来，以及当状态不充分、回报方差很大或行为策略改变时，公式中的哪一项首先失效。

## 2. 30 秒回答（PDF 原始要点）

> SARSA 用真实下一动作 a′ 做 target，是 on-policy；Q-learning 用 max_a′Q 做 target，学习 greedy target policy，因此 off-policy。

面试开场建议只讲这一层；如果面试官点头继续，再进入后面的推导与 failure mode。

## 3. 深入解析（PDF 原始要点）

- SARSA target 反映探索策略本身的风险，所以 Cliff Walking 中常学到更安全路径。
- Q-learning 的 max operator 更激进，同时带来 maximization bias。
- Expected SARSA 用期望替代 sampled a′，在方差上介于两者之间。

## 4. Repo 扩展解析：把概念放回统一框架

把这道题放回 RL 的三条主线理解：**Bellman/Bootstrap** 决定价值如何递归传播，**Bias-Variance/Credit Assignment** 决定估计器是否稳定，**Distribution Shift** 决定采样数据还能否支持当前目标。面试时不要只报定义；应主动说明成立条件、估计误差从哪里来，以及当状态不充分、回报方差很大或行为策略改变时，公式中的哪一项首先失效。

### 4.1 推导/证明应该从哪里开始

建议在白板上先写“随机变量、条件、期望/采样分布、优化参数”四件事，再推公式；这样可以避免只记住最终等式却解释不了每一项。

### 4.2 关键公式

```text
SARSA: y=r+γQ(s′,a′); Q-learning: y=r+γ max_{a′}Q(s′,a′)
```





## 4.3 Repo v2 专业深化：从第一原则理解

SARSA 的 target 跟随实际行为策略，Q-learning 的 target 使用 greedy max。前者学习“带探索的真实行为后果”，后者学习 greedy optimality fixed point。

### 数学/推导抓手

SARSA: y=r+γQ(s′,a′), a′~π；Q-learning: y=r+γmaxₐ′Q(s′,a′)。

> **面试要求**：这里的公式不是“背出来就结束”。需要能解释每个期望是对什么随机变量取、哪些量来自 rollout、哪些量是 learned estimate、哪些分支必须 stop-gradient。

### 工程化检查点

- 安全控制里 exploration 本身有成本时，SARSA 的行为敏感性常是重要直觉。
- 明确随机变量与条件分布，不把采样值和期望混写。
- 明确 terminal、horizon、γ 以及状态是否真正 Markov。
- 能从 return 定义推回 Bellman/TD，而不是只背更新式。

### 面试中如何把回答从 70 分提升到 90 分

1. **先给结论**：一句话说明该方法解决的 failure mode。
2. **再写公式**：只写决定算法差异的那一项，不堆无关符号。
3. **解释估计误差**：指出 bias、variance、distribution shift 或 optimization instability 从哪里来。
4. **给反例**：说明算法在哪类数据/环境/系统条件下会失效。
5. **落到日志**：说清你会看哪些指标来验证判断，而不是“调参试试”。


## 5. 工程实现与训练观测

建议把每次实验的配置、checkpoint、数据版本、随机种子和指标快照固化成 manifest；系统问题与算法问题必须能通过日志切片分离。

### 推荐观测项

- **数据层**：状态/动作/response mask 是否正确，terminal/truncation、policy version、reward component 是否可追踪。
- **统计层**：均值之外同时看方差、分位数和按难度/长度/任务类型切片的分布。
- **优化层**：loss、gradient norm、value/Q/advantage/ratio/KL/entropy 中与本题相关的量是否同步变化。
- **真实目标层**：训练 reward 上升是否真的带来 held-out return / accuracy / pass@k / success rate 提升。

## 6. 常见失败模式与排查

- 状态不是 Markov 导致价值函数把不可观测历史误当噪声
- 折扣/终止处理错误使 bootstrap target 系统性偏移
- 把 bias-variance 的取舍说成某个算法“绝对更优”

排查原则：**先证伪数据与实现 bug，再讨论算法超参；先看分布，再看平均值。**

## 7. 高频追问

- Expected SARSA 是什么？
- 为什么 Q-learning 能 off-policy？

### 推荐追问回答结构

1. 先给一句结论；
2. 写出最关键公式/数据分布；
3. 解释为什么该公式能解决上一层 failure mode；
4. 给一个反例或失效场景；
5. 最后落到工程监控或项目经验。

## 7.1 高频追问参考答法

### 追问 1：Expected SARSA 是什么？

SARSA 的 target 跟随实际行为策略，Q-learning 的 target 使用 greedy max。前者学习“带探索的真实行为后果”，后者学习 greedy optimality fixed point。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。

### 追问 2：为什么 Q-learning 能 off-policy？

安全控制里 exploration 本身有成本时，SARSA 的行为敏感性常是重要直觉。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。


## 8. 易错点

> 不要把“off-policy”解释成“训练时不用 policy”。

## 9. 面试官评分标准

> 优秀回答应同时覆盖定义/公式、为什么成立、失败模式与项目迁移。

可以进一步按四档自评：

| 档位 | 表现 |
|---|---|
| 及格 | 能准确给定义和主公式 |
| 良好 | 能解释每一项、算法动机与典型优缺点 |
| 优秀 | 能说明 failure mode、边界条件和替代方案 |
| 强工程/研究 | 能从日志、数据分布、系统成本或项目迁移给出可验证判断 |

## 10. 白板自测

在不看答案的情况下，尝试完成：

- 用 **3 句话**重新回答本题；
- 从第一原则推导/解释核心公式，而不是默写；
- 给出一个“这个方法会失败”的具体环境或训练现象；
- 说明你会记录哪 3 个指标来验证自己的判断。

## 11. 延伸阅读

- [Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)

## 12. 90 秒专业回答

> **结论先行**：SARSA 用真实下一动作 a′ 做 target，是 on-policy；Q-learning 用 max_a′Q 做 target，学习 greedy target policy，因此 off-policy。

继续展开时，先把它放回本章的统一问题框架：**SARSA target 反映探索策略本身的风险，所以 Cliff Walking 中常学到更安全路径。；Q-learning 的 max operator 更激进，同时带来 maximization bias。**。随后写出本题最关键的数学对象：`SARSA: y=r+γQ(s′,a′); Q-learning: y=r+γ max_{a′}Q(s′,a′)`。最后必须补一句工程判断：公式成立不代表实现健康，需要用本页列出的分布指标、边界条件和 failure mode 验证。

一个高质量的 90 秒回答应满足：

- **前 15 秒**：明确“这个方法解决什么问题”；
- **15–45 秒**：给核心公式，并解释符号来自哪个数据分布；
- **45–70 秒**：讲一个典型失败模式或 tradeoff；
- **70–90 秒**：落到实现/日志，并说明如何验证。

> **不要这样答**：只按论文顺序背名词。面试官通常更在意你能否从 failure mode 推回设计，再从设计推到可观测指标。

## 13. 最小可验证实验

**实验目标**：不是做 leaderboard，而是把本题的核心机制变成可以 falsify 的小实验。

1. **环境/数据**：构造一个 3~5 状态的 tabular MDP，手工给定转移和奖励。
2. **记录与对照**：用枚举/矩阵解作为 ground truth，再比较 MC/TD/DP 或对应公式的数值结果。
3. **验收标准**：目标不是跑出高分，而是验证公式、terminal 处理和期望的维度是否正确。

针对本题额外要求：把 **“SARSA 与 Q-learning 有什么区别？”** 对应的关键变量单独画分布或写断言；如果实验结果和理论预期相反，优先检查数据定义、mask/terminal、旧策略版本和归一化维度，再讨论超参数。

---

[← Q013](Q013-importance-sampling.md) · [章节首页](README.md) · [Q015 →](Q015-exploration-exploitation.md)
