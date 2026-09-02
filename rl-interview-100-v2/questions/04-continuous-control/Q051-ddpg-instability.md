---
id: Q051
title: "DDPG 为什么容易不稳定？"
chapter: "第四章 DDPG / TD3 / SAC 连续控制"
source_type: "公开面经追问"
frequency: "★★★★☆"
difficulty: "★★★★☆"
roles: "机器人/控制"
tags: ["ddpg", "continuous-control"]
---

# Q051 DDPG 为什么容易不稳定？

> **题型**：公开面经追问 ｜ **频率**：★★★★☆ ｜ **难度**：★★★★☆ ｜ **岗位**：机器人/控制  
> **来源层级**：本页“PDF 原始要点”来自仓库内原版 PDF；“Repo 扩展解析”是在不改变原结论的前提下新增的理论、工程与面试组织内容。

[← Q050](Q050-ddpg-updates.md) · [章节首页](README.md) · [Q052 →](Q052-td3-three-tricks.md)

## 1. 面试官真正想确认什么

这不是单纯的名词解释题。面试官通常会顺着 **定义 → 数学对象 → 为什么有效 → 什么时候失效 → 如何实现/监控 → 如何迁移到项目** 连续追问。

连续控制里无法枚举所有动作求 max，因此通常显式学习 actor。随后新的核心风险变成：critic 的误差会通过 actor 的梯度被“主动利用”。DDPG→TD3→SAC 的演化可以围绕 **Q 过估计、探索方式、策略随机性、目标平滑与熵正则** 来解释。

## 2. 30 秒回答（PDF 原始要点）

> critic overestimation 与 function approximation error 会被 actor 主动利用；deterministic exploration 也脆弱，导致性能对超参和随机种子敏感。

面试开场建议只讲这一层；如果面试官点头继续，再进入后面的推导与 failure mode。

## 3. 深入解析（PDF 原始要点）

- bootstrapped Q error 会传播。
- actor 每次都朝当前 Q 峰值走，若 Q 峰值是噪声就会被放大。
- TD3 的 twin critic、delayed policy、target smoothing 正是针对这些问题。

## 4. Repo 扩展解析：把概念放回统一框架

连续控制里无法枚举所有动作求 max，因此通常显式学习 actor。随后新的核心风险变成：critic 的误差会通过 actor 的梯度被“主动利用”。DDPG→TD3→SAC 的演化可以围绕 **Q 过估计、探索方式、策略随机性、目标平滑与熵正则** 来解释。

### 4.1 推导/证明应该从哪里开始

建议在白板上先写“随机变量、条件、期望/采样分布、优化参数”四件事，再推公式；这样可以避免只记住最终等式却解释不了每一项。

### 4.2 关键公式

这道题更偏概念/系统设计。面试时仍建议先明确随机变量、目标函数和数据分布。





## 4.3 Repo v2 专业深化：从第一原则理解

DDPG 的脆弱性来自“actor 会主动利用 critic 的函数逼近误差”。critic 一旦对某区域虚高，actor 会快速把动作推过去，随后 bootstrap 进一步放大。

### 数学/推导抓手

这是 optimization over estimated Q 引入的 extrapolation/overestimation 问题。

> **面试要求**：这里的公式不是“背出来就结束”。需要能解释每个期望是对什么随机变量取、哪些量来自 rollout、哪些量是 learned estimate、哪些分支必须 stop-gradient。

### 工程化检查点

- 关注 Q scale、actor saturation、exploration noise 与 critic target 分布。
- TD3 的三项改进正对应这些病灶。
- 动作是否经过 squash/scale，log-prob/Jacobian 是否正确。
- critic target 与 actor update 的 stop-gradient 边界明确。
- 区分环境探索噪声、target smoothing noise 与 stochastic policy entropy。

### 面试中如何把回答从 70 分提升到 90 分

1. **先给结论**：一句话说明该方法解决的 failure mode。
2. **再写公式**：只写决定算法差异的那一项，不堆无关符号。
3. **解释估计误差**：指出 bias、variance、distribution shift 或 optimization instability 从哪里来。
4. **给反例**：说明算法在哪类数据/环境/系统条件下会失效。
5. **落到日志**：说清你会看哪些指标来验证判断，而不是“调参试试”。


## 5. 工程实现与训练观测

连续控制需特别检查 action scaling、tanh squashing、环境动作边界、target action noise、replay warm-up 与 reward scale。许多“算法不收敛”其实是动作单位或环境接口问题。

### 推荐观测项

- **数据层**：状态/动作/response mask 是否正确，terminal/truncation、policy version、reward component 是否可追踪。
- **统计层**：均值之外同时看方差、分位数和按难度/长度/任务类型切片的分布。
- **优化层**：loss、gradient norm、value/Q/advantage/ratio/KL/entropy 中与本题相关的量是否同步变化。
- **真实目标层**：训练 reward 上升是否真的带来 held-out return / accuracy / pass@k / success rate 提升。

## 6. 常见失败模式与排查

- 动作缩放或 tanh 边界实现错误
- critic 过估计被 actor 利用
- 探索噪声、entropy 或 reward scale 与环境不匹配

排查原则：**先证伪数据与实现 bug，再讨论算法超参；先看分布，再看平均值。**

## 7. 高频追问

- 为什么 target network 仍不足？
- OU noise 为什么曾经流行？

### 推荐追问回答结构

1. 先给一句结论；
2. 写出最关键公式/数据分布；
3. 解释为什么该公式能解决上一层 failure mode；
4. 给一个反例或失效场景；
5. 最后落到工程监控或项目经验。

## 7.1 高频追问参考答法

### 追问 1：为什么 target network 仍不足？

DDPG 的脆弱性来自“actor 会主动利用 critic 的函数逼近误差”。critic 一旦对某区域虚高，actor 会快速把动作推过去，随后 bootstrap 进一步放大。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。

### 追问 2：OU noise 为什么曾经流行？

关注 Q scale、actor saturation、exploration noise 与 critic target 分布。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。


## 8. 易错点

> 不要只说“DDPG deterministic 所以不稳定”，核心是 actor-critic error coupling。

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

- [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)

## 11.1 Primary Source 精读建议

- [Continuous control with deep reinforcement learning](https://arxiv.org/abs/1509.02971)

阅读时不要只看摘要。建议至少定位：**problem formulation → objective/algorithm box → ablation → failure/limitation**。面试里真正有区分度的是能把论文中的设计选择与本题的 failure mode 对上。

## 12. 90 秒专业回答

> **结论先行**：critic overestimation 与 function approximation error 会被 actor 主动利用；deterministic exploration 也脆弱，导致性能对超参和随机种子敏感。

继续展开时，先把它放回本章的统一问题框架：**bootstrapped Q error 会传播。；actor 每次都朝当前 Q 峰值走，若 Q 峰值是噪声就会被放大。**。随后写出本题最关键的数学对象：`见上文推导`。最后必须补一句工程判断：公式成立不代表实现健康，需要用本页列出的分布指标、边界条件和 failure mode 验证。

一个高质量的 90 秒回答应满足：

- **前 15 秒**：明确“这个方法解决什么问题”；
- **15–45 秒**：给核心公式，并解释符号来自哪个数据分布；
- **45–70 秒**：讲一个典型失败模式或 tradeoff；
- **70–90 秒**：落到实现/日志，并说明如何验证。

> **不要这样答**：只按论文顺序背名词。面试官通常更在意你能否从 failure mode 推回设计，再从设计推到可观测指标。

## 13. 最小可验证实验

**实验目标**：不是做 leaderboard，而是把本题的核心机制变成可以 falsify 的小实验。

1. **环境/数据**：在 Pendulum 或自定义一维连续控制环境建立小实验。
2. **记录与对照**：记录 action distribution、Q1/Q2、target Q、actor output、entropy/temperature（若适用）以及 replay age。
3. **验收标准**：重点验证连续动作优化、Q 偏差与探索机制，而不是追求 benchmark 最优分。

针对本题额外要求：把 **“DDPG 为什么容易不稳定？”** 对应的关键变量单独画分布或写断言；如果实验结果和理论预期相反，优先检查数据定义、mask/terminal、旧策略版本和归一化维度，再讨论超参数。

---

[← Q050](Q050-ddpg-updates.md) · [章节首页](README.md) · [Q052 →](Q052-td3-three-tricks.md)
