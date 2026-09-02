---
id: Q064
title: "Model-based 与 Model-free RL 有何区别？"
chapter: "第五章 Offline RL / Model-based / MARL / Sim2Real"
source_type: "高级母题"
frequency: "★★★★☆"
difficulty: "★★★☆☆"
roles: "研究/机器人"
tags: ["model-based"]
---

# Q064 Model-based 与 Model-free RL 有何区别？

> **题型**：高级母题 ｜ **频率**：★★★★☆ ｜ **难度**：★★★☆☆ ｜ **岗位**：研究/机器人  
> **来源层级**：本页“PDF 原始要点”来自仓库内原版 PDF；“Repo 扩展解析”是在不改变原结论的前提下新增的理论、工程与面试组织内容。

[← Q063](Q063-iql.md) · [章节首页](README.md) · [Q065 →](Q065-reward-shaping.md)

## 1. 面试官真正想确认什么

这不是单纯的名词解释题。面试官通常会顺着 **定义 → 数学对象 → 为什么有效 → 什么时候失效 → 如何实现/监控 → 如何迁移到项目** 连续追问。

这一章的共同主题是“训练数据与真实决策分布不完全一致”。Offline RL 担心 dataset support，model-based RL 担心 model bias，MARL 担心其他智能体导致环境非平稳，Sim2Real 则担心仿真动力学与真实世界不一致。回答时应明确：你用什么约束保证 policy 不会过度利用模型/价值函数在分布外区域的错误。

## 2. 30 秒回答（PDF 原始要点）

> Model-based 显式学习/使用环境动力学再做规划或 imagined rollout；Model-free 直接学 value/policy。

面试开场建议只讲这一层；如果面试官点头继续，再进入后面的推导与 failure mode。

## 3. 深入解析（PDF 原始要点）

- model-based sample efficient，但 model bias 会随 rollout horizon 累积。
- 短 imagined rollout、uncertainty ensemble、MPC 是控制误差的常见手段。
- 真实系统中 learned model 还能用于安全预测与规划。

## 4. Repo 扩展解析：把概念放回统一框架

这一章的共同主题是“训练数据与真实决策分布不完全一致”。Offline RL 担心 dataset support，model-based RL 担心 model bias，MARL 担心其他智能体导致环境非平稳，Sim2Real 则担心仿真动力学与真实世界不一致。回答时应明确：你用什么约束保证 policy 不会过度利用模型/价值函数在分布外区域的错误。

### 4.1 推导/证明应该从哪里开始

建议在白板上先写“随机变量、条件、期望/采样分布、优化参数”四件事，再推公式；这样可以避免只记住最终等式却解释不了每一项。

### 4.2 关键公式

这道题更偏概念/系统设计。面试时仍建议先明确随机变量、目标函数和数据分布。





## 4.3 Repo v2 专业深化：从第一原则理解

Model-based RL 把环境 dynamics/reward 也作为可学习对象，获得额外 imagined data/规划能力；主要风险是 model bias 在长 rollout 中累积并被 policy exploitation。

### 数学/推导抓手

真实 P 被 P̂θ 代替；k-step imagined rollout 的误差通常随 horizon 累积。

> **面试要求**：这里的公式不是“背出来就结束”。需要能解释每个期望是对什么随机变量取、哪些量来自 rollout、哪些量是 learned estimate、哪些分支必须 stop-gradient。

### 工程化检查点

- 常限制 model rollout horizon、做 uncertainty penalty/ensemble。
- world model 评估不能只看 one-step prediction loss，还要看 rollout calibration。
- 先描述数据覆盖和行为策略，再谈算法。
- 明确 OOD action / model bias / non-stationarity 属于哪一类分布偏移。
- 给出保守性与策略改进之间的 tradeoff。

### 面试中如何把回答从 70 分提升到 90 分

1. **先给结论**：一句话说明该方法解决的 failure mode。
2. **再写公式**：只写决定算法差异的那一项，不堆无关符号。
3. **解释估计误差**：指出 bias、variance、distribution shift 或 optimization instability 从哪里来。
4. **给反例**：说明算法在哪类数据/环境/系统条件下会失效。
5. **落到日志**：说清你会看哪些指标来验证判断，而不是“调参试试”。


## 5. 工程实现与训练观测

工程上必须保存数据来源与行为策略版本，并对 dataset coverage 做切片；只看训练 loss 很容易误判。真实机器人还应增加 safety gate、动作限幅、reset 策略和仿真/真实差异监控。

### 推荐观测项

- **数据层**：状态/动作/response mask 是否正确，terminal/truncation、policy version、reward component 是否可追踪。
- **统计层**：均值之外同时看方差、分位数和按难度/长度/任务类型切片的分布。
- **优化层**：loss、gradient norm、value/Q/advantage/ratio/KL/entropy 中与本题相关的量是否同步变化。
- **真实目标层**：训练 reward 上升是否真的带来 held-out return / accuracy / pass@k / success rate 提升。

## 6. 常见失败模式与排查

- policy 选择数据支持集外动作
- 模型 rollout 过长积累 model bias
- 仿真参数覆盖不足或多智能体训练分布非平稳

排查原则：**先证伪数据与实现 bug，再讨论算法超参；先看分布，再看平均值。**

## 7. 高频追问

- world model 为什么重新流行？
- model error 如何估计？

### 推荐追问回答结构

1. 先给一句结论；
2. 写出最关键公式/数据分布；
3. 解释为什么该公式能解决上一层 failure mode；
4. 给一个反例或失效场景；
5. 最后落到工程监控或项目经验。

## 7.1 高频追问参考答法

### 追问 1：world model 为什么重新流行？

Model-based RL 把环境 dynamics/reward 也作为可学习对象，获得额外 imagined data/规划能力；主要风险是 model bias 在长 rollout 中累积并被 policy exploitation。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。

### 追问 2：model error 如何估计？

常限制 model rollout horizon、做 uncertainty penalty/ensemble。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。


## 8. 易错点

> “Model-based 一定更好”错误；模型误差可能比样本效率收益更致命。

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

> **结论先行**：Model-based 显式学习/使用环境动力学再做规划或 imagined rollout；Model-free 直接学 value/policy。

继续展开时，先把它放回本章的统一问题框架：**model-based sample efficient，但 model bias 会随 rollout horizon 累积。；短 imagined rollout、uncertainty ensemble、MPC 是控制误差的常见手段。**。随后写出本题最关键的数学对象：`见上文推导`。最后必须补一句工程判断：公式成立不代表实现健康，需要用本页列出的分布指标、边界条件和 failure mode 验证。

一个高质量的 90 秒回答应满足：

- **前 15 秒**：明确“这个方法解决什么问题”；
- **15–45 秒**：给核心公式，并解释符号来自哪个数据分布；
- **45–70 秒**：讲一个典型失败模式或 tradeoff；
- **70–90 秒**：落到实现/日志，并说明如何验证。

> **不要这样答**：只按论文顺序背名词。面试官通常更在意你能否从 failure mode 推回设计，再从设计推到可观测指标。

## 13. 最小可验证实验

**实验目标**：不是做 leaderboard，而是把本题的核心机制变成可以 falsify 的小实验。

1. **环境/数据**：构造可控的数据覆盖差异：例如只收集某一部分 action/state 的静态 dataset。
2. **记录与对照**：比较 BC、普通 off-policy 方法与本题算法在 in-distribution / OOD action 上的 Q、动作分布与 return。
3. **验收标准**：让 distribution shift、conservatism 或 model bias 变成可观测现象。

针对本题额外要求：把 **“Model-based 与 Model-free RL 有何区别？”** 对应的关键变量单独画分布或写断言；如果实验结果和理论预期相反，优先检查数据定义、mask/terminal、旧策略版本和归一化维度，再讨论超参数。

---

[← Q063](Q063-iql.md) · [章节首页](README.md) · [Q065 →](Q065-reward-shaping.md)
