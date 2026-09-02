---
id: Q073
title: "Reward Model 怎么训练？"
chapter: "第六章 RLHF / DPO / GRPO / DAPO / GSPO"
source_type: "LLM 高频"
frequency: "★★★★★"
difficulty: "★★★☆☆"
roles: "LLM Post-training"
tags: ["reward"]
---

# Q073 Reward Model 怎么训练？

> **题型**：LLM 高频 ｜ **频率**：★★★★★ ｜ **难度**：★★★☆☆ ｜ **岗位**：LLM Post-training  
> **来源层级**：本页“PDF 原始要点”来自仓库内原版 PDF；“Repo 扩展解析”是在不改变原结论的前提下新增的理论、工程与面试组织内容。

[← Q072](Q072-why-rl-after-sft.md) · [章节首页](README.md) · [Q074 →](Q074-rm-distribution-shift.md)

## 1. 面试官真正想确认什么

这不是单纯的名词解释题。面试官通常会顺着 **定义 → 数学对象 → 为什么有效 → 什么时候失效 → 如何实现/监控 → 如何迁移到项目** 连续追问。

LLM 后训练可以看成超大离散动作空间上的 policy optimization。一个 response 是长序列，reward 往往是 sequence-level，而训练更新发生在 token-level 参数上，因此 **credit assignment、importance ratio 粒度、KL、采样成本与 verifier 可靠性** 同时成为一等问题。回答 2026 面试题时，应把算法公式与 rollout 系统、显存占用、长尾序列和 reward pipeline 一起讲。

## 2. 30 秒回答（PDF 原始要点）

> 对同一 prompt 的 preferred/rejected response 学 Bradley-Terry 排序：让 chosen 的 scalar reward 高于 rejected。

面试开场建议只讲这一层；如果面试官点头继续，再进入后面的推导与 failure mode。

## 3. 深入解析（PDF 原始要点）

- RM 学相对偏好，不要求绝对分数有真实物理含义。
- pair 构造质量、长度 bias、annotator disagreement 会直接进入 reward。
- 训练后还必须做 calibration、OOD、adversarial 与 optimizer-facing 测试。

## 4. Repo 扩展解析：把概念放回统一框架

LLM 后训练可以看成超大离散动作空间上的 policy optimization。一个 response 是长序列，reward 往往是 sequence-level，而训练更新发生在 token-level 参数上，因此 **credit assignment、importance ratio 粒度、KL、采样成本与 verifier 可靠性** 同时成为一等问题。回答 2026 面试题时，应把算法公式与 rollout 系统、显存占用、长尾序列和 reward pipeline 一起讲。

### 4.1 推导/证明应该从哪里开始

建议在白板上先写“随机变量、条件、期望/采样分布、优化参数”四件事，再推公式；这样可以避免只记住最终等式却解释不了每一项。

### 4.2 关键公式

```text
L_RM = -log σ(r(x,y_w)-r(x,y_l))
```





## 4.3 Repo v2 专业深化：从第一原则理解

Reward Model 通常把 preference pair 转成相对排序学习。它学习的是“在数据分布上的偏好函数近似”，不是客观真值标量。

### 数学/推导抓手

P(y_w≻y_l|x)=σ(rφ(x,y_w)−rφ(x,y_l)); L=−logσ(r_w−r_l)。

> **面试要求**：这里的公式不是“背出来就结束”。需要能解释每个期望是对什么随机变量取、哪些量来自 rollout、哪些量是 learned estimate、哪些分支必须 stop-gradient。

### 工程化检查点

- 要做 position/order 随机化、长度偏差分析、annotator disagreement 切片。
- RM 评估要包含 policy-generated OOD responses，而不只静态 held-out pair accuracy。
- 明确 prompt、sequence、token 三种粒度。
- 明确 old policy、current policy、reference policy 三个角色。
- 记录 rollout policy version、response mask、reward components、KL/entropy/length。

### 面试中如何把回答从 70 分提升到 90 分

1. **先给结论**：一句话说明该方法解决的 failure mode。
2. **再写公式**：只写决定算法差异的那一项，不堆无关符号。
3. **解释估计误差**：指出 bias、variance、distribution shift 或 optimization instability 从哪里来。
4. **给反例**：说明算法在哪类数据/环境/系统条件下会失效。
5. **落到日志**：说清你会看哪些指标来验证判断，而不是“调参试试”。


## 5. 工程实现与训练观测

工程实现时建议把“数据形状、mask、旧策略版本、target/stop-gradient 边界、归一化维度”写在代码旁边。RL 中大量 bug 不会报错，而会以训练慢、KL 异常、value 爆炸或 reward 假提升的形式出现。

> 配套代码：[`code/reward_model_loss.py`](../../code/reward_model_loss.py)。先自己手写，再对照仓库版本。

### 推荐观测项

- **数据层**：状态/动作/response mask 是否正确，terminal/truncation、policy version、reward component 是否可追踪。
- **统计层**：均值之外同时看方差、分位数和按难度/长度/任务类型切片的分布。
- **优化层**：loss、gradient norm、value/Q/advantage/ratio/KL/entropy 中与本题相关的量是否同步变化。
- **真实目标层**：训练 reward 上升是否真的带来 held-out return / accuracy / pass@k / success rate 提升。

## 6. 常见失败模式与排查

- Reward Model 在训练分布上准确，但 policy 优化后进入 RM 未覆盖的分布
- 长序列造成 ratio/KL/长度权重的粒度错配
- rollout policy、reference、old logp 版本不一致

排查原则：**先证伪数据与实现 bug，再讨论算法超参；先看分布，再看平均值。**

## 7. 高频追问

- 为什么 RM accuracy 高仍会 reward hack？
- 如何做 listwise preference？

### 推荐追问回答结构

1. 先给一句结论；
2. 写出最关键公式/数据分布；
3. 解释为什么该公式能解决上一层 failure mode；
4. 给一个反例或失效场景；
5. 最后落到工程监控或项目经验。

## 7.1 高频追问参考答法

### 追问 1：为什么 RM accuracy 高仍会 reward hack？

Reward Model 通常把 preference pair 转成相对排序学习。它学习的是“在数据分布上的偏好函数近似”，不是客观真值标量。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。

### 追问 2：如何做 listwise preference？

要做 position/order 随机化、长度偏差分析、annotator disagreement 切片。

回答时继续补一层：先说明**为什么**，再指出一个**边界条件/失败现象**，最后给出一个可观测指标或实现检查点。


## 8. 易错点

> 不要只看 held-out pair accuracy；policy 会主动搜索 RM 的漏洞。

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

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

## 11.1 Primary Source 精读建议

- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155)

阅读时不要只看摘要。建议至少定位：**problem formulation → objective/algorithm box → ablation → failure/limitation**。面试里真正有区分度的是能把论文中的设计选择与本题的 failure mode 对上。

## 12. 90 秒专业回答

> **结论先行**：对同一 prompt 的 preferred/rejected response 学 Bradley-Terry 排序：让 chosen 的 scalar reward 高于 rejected。

继续展开时，先把它放回本章的统一问题框架：**RM 学相对偏好，不要求绝对分数有真实物理含义。；pair 构造质量、长度 bias、annotator disagreement 会直接进入 reward。**。随后写出本题最关键的数学对象：`L_RM = -log σ(r(x,y_w)-r(x,y_l))`。最后必须补一句工程判断：公式成立不代表实现健康，需要用本页列出的分布指标、边界条件和 failure mode 验证。

一个高质量的 90 秒回答应满足：

- **前 15 秒**：明确“这个方法解决什么问题”；
- **15–45 秒**：给核心公式，并解释符号来自哪个数据分布；
- **45–70 秒**：讲一个典型失败模式或 tradeoff；
- **70–90 秒**：落到实现/日志，并说明如何验证。

> **不要这样答**：只按论文顺序背名词。面试官通常更在意你能否从 failure mode 推回设计，再从设计推到可观测指标。

## 13. 最小可验证实验

**实验目标**：不是做 leaderboard，而是把本题的核心机制变成可以 falsify 的小实验。

1. **环境/数据**：用少量 prompt，每个 prompt 采 G 个短 completion，并使用可重复的 toy verifier/reward。
2. **记录与对照**：保存 prompt/response mask、old/ref/new logp、group reward、advantage、ratio、KL、entropy、length。
3. **验收标准**：先在极小 batch 上逐元素核对 loss，再扩到真实 rollout；这能捕获绝大多数 silent bug。

针对本题额外要求：把 **“Reward Model 怎么训练？”** 对应的关键变量单独画分布或写断言；如果实验结果和理论预期相反，优先检查数据定义、mask/terminal、旧策略版本和归一化维度，再讨论超参数。

---

[← Q072](Q072-why-rl-after-sft.md) · [章节首页](README.md) · [Q074 →](Q074-rm-distribution-shift.md)
