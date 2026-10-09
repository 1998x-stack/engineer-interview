---
id: q042
title: "Recursive、Direct、MIMO 多步预测有什么区别？"
chapter: 4
difficulty: "★★★★☆"
frequency: "★★★★★"
tags: ["多步", "递归", "Direct", "MIMO"]
source: "PDF 2026.09"
---

# Q042 Recursive、Direct、MIMO 多步预测有什么区别？

> **章节：** 机器学习与大规模 Global Forecasting  
> **难度：** ★★★★☆ ｜ **频率：** ★★★★★  
> **关键词：** 多步 / 递归 / Direct / MIMO

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

Recursive 只训练一步模型但会误差累积；Direct 为每个 horizon 训练独立模型；MIMO 一次输出整个 horizon 并可学习各步关联。

## PDF 基线：核心公式 / 结构

$$
Recursive: one-step repeated; Direct: f_h; MIMO: vector output
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

还可以做 direct-recursive hybrid。实际选择取决于 horizon、数据量、推理成本以及未来 covariates 的形式。

### PDF 易错点

> 只按“模型数量少”选择 recursive。

### PDF 高级加分点

> 选择多步策略时同时考虑误差传播、模型数量、联合一致性和推理吞吐。

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

机器学习预测的核心不是换模型，而是构造 point-in-time 正确的监督学习样本，并决定 local/global、多步策略与业务 covariates。

- Recursive 有 exposure bias/error accumulation；Direct 忽略 horizon 共享；MIMO/seq2seq 则一次学习整个未来向量。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 为什么 recursive 训练/推理分布不一致？

**回答方向：** 回答时不要停在现象层。先说明其改变的统计/信息条件，再指出对验证或部署的影响。可结合本题核心：Recursive 只训练一步模型但会误差累积；Direct 为每个 horizon 训练独立模型；MIMO 一次输出整个 horizon 并可学习各步关联。

### 2. teacher forcing 相关吗？

**回答方向：** 围绕本章主线回答：机器学习预测的核心不是换模型，而是构造 point-in-time 正确的监督学习样本，并决定 local/global、多步策略与业务 covariates，并落到假设、验证与工程边界。


### 4. 工程检查清单

- [ ] 特征构造统一遵循 point-in-time contract。
- [ ] 对每个 horizon 说明 recursive/direct/MIMO 策略。
- [ ] Global model 要评估跨实体泛化、cold start 与 scale normalization。


<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. Recursive 只学 one-step，推理时把预测喂回模型；Direct 每个 horizon 独立建模；MIMO/seq2seq 一次输出整个 horizon。
2. Recursive 参数共享高、样本效率好，但 error accumulation 与 train-inference mismatch 明显。
3. Direct 避免递归误差，却忽略 horizon 间结构并增加模型数量；MIMO 可联合建模 horizon dependence。

### 2. 一条可复用的推理链

回答 **“Recursive、Direct、MIMO 多步预测有什么区别？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 只比较点误差，不比较推理成本和 forecast coherence。
- **边界 2：** Direct 模型没有加入 horizon identifier 或共享结构，维护成本巨大。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

28 天零售预测常用 direct multi-output 或按 horizon 分组模型，而不是把 1-day model 连滚 28 次。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

可以做 DirRec、multi-task direct 或 probabilistic trajectory sampling，形成中间折中。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 监督学习流水线 Checklist

- [ ] 构造 point-in-time correct features
- [ ] 明确 future covariate availability
- [ ] 按 horizon/segment 做滚动回测

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** Recursive 只训练一步模型但会误差累积；Direct 为每个 horizon 训练独立模型；MIMO 一次输出整个 horizon 并可学习各步关联。
>
> **第二层解释机制。** 还可以做 direct-recursive hybrid。实际选择取决于 horizon、数据量、推理成本以及未来 covariates 的形式。
>
> **第三层补边界。** 这个结论只有在数据生成机制、信息可用性和验证协议匹配时才有意义；我会主动检查本题上面列出的失败模式。
>
> **第四层落到工程。** 最后我会用与生产一致的 rolling backtest、强 baseline 和 horizon/segment 分解指标验证，并记录 point-in-time feature lineage，确保离线提升可以复现到线上。

### 9. 自测：面试前必须能脱口而出的 4 个问题

- **定义题：** 不看笔记，能否用 20 秒给出一句准确答案？
- **推导题：** 能否写出本题最关键公式，并解释每个符号的统计/业务含义？
- **反例题：** 能否给出一个模型表面合理、实际会失败的案例？
- **工程题：** 能否说明如何在不泄漏未来的前提下验证，并给出 fallback？
<!-- V2_DEEP_DIVE_END -->

## 面试表达模板

> **结论：** Recursive 只训练一步模型但会误差累积；Direct 为每个 horizon 训练独立模型；MIMO 一次输出整个 horizon 并可学习各步关联。  
> **原理：** 还可以做 direct-recursive hybrid。实际选择取决于 horizon、数据量、推理成本以及未来 covariates 的形式。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q041 什么是 Known Future Covariate？](../04-machine-learning/q041-known-future-covariates.md)
- [Q043 Random Forest 和 ARIMA 做趋势外推时有什么区别？](../04-machine-learning/q043-random-forest-vs-arima-extrapolation.md)
- [Q068 为什么必须按 Forecast Horizon 评估？](../06-evaluation-probabilistic/q068-evaluate-by-horizon.md)

## 延伸阅读

- [M5 Accuracy competition paper](https://www.sciencedirect.com/science/article/pii/S0169207021001874)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
