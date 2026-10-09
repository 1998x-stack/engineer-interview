---
id: q025
title: "解释 ARIMA(p,d,q)。"
chapter: 3
difficulty: "★★★☆☆"
frequency: "★★★★★"
tags: ["ARIMA", "p d q", "Box-Jenkins"]
source: "PDF 2026.09"
---

# Q025 解释 ARIMA(p,d,q)。

> **章节：** ARIMA、ETS 与状态空间模型  
> **难度：** ★★★☆☆ ｜ **频率：** ★★★★★  
> **关键词：** ARIMA / p d q / Box-Jenkins

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

ARIMA 先通过 d 阶差分把非平稳 level 转为近似平稳序列，再用 AR(p)+MA(q) 建模其线性依赖。

## PDF 基线：核心公式 / 结构

$$
φ(B)(1-B)^d y_t=θ(B)ε_t
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

高分回答必须补一句：ARIMA 不只是“ACF/PACF 选阶”，还要做残差白噪声诊断和 out-of-sample rolling validation。

### PDF 易错点

> 把 I 解释成“interpolation”。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

掌握 Box-Jenkins 不是为了背 p/d/q，而是为了建立‘识别 -> 估计 -> 诊断 -> 回测’的闭环。

- $d$ 负责把非平稳部分转成可建模增量，$p/q$ 再解释差分后序列的自相关结构。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. ARIMA 与 ARMA 差别？

**回答方向：** 围绕本章主线回答：掌握 Box-Jenkins 不是为了背 p/d/q，而是为了建立‘识别 -> 估计 -> 诊断 -> 回测’的闭环，并落到假设、验证与工程边界。

### 2. drift 怎么加？

**回答方向：** 先给可执行流程：诊断数据与可用信息 -> 建 baseline -> 时间正确的回测 -> 误差分解 -> 再决定模型或修复动作。


### 4. 工程检查清单

- [ ] ARIMA/ETS 至少与 Naive/Seasonal Naive 比较。
- [ ] 残差诊断与 rolling backtest 缺一不可。
- [ ] 外生变量必须标注未来可用性和发布时间。


## 最小可运行示例

```python
from statsmodels.tsa.arima.model import ARIMA

model = ARIMA(y_train, order=(2, 1, 1)).fit()
forecast = model.forecast(steps=14)
```

<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. ARIMA(p,d,q) 先通过 $(1-B)^d$ 把 integrated series 转为近似平稳，再对差分序列建 ARMA(p,q)。
2. Box-Jenkins 不是“ACF/PACF 选阶”一个动作，而是 Identification → Estimation → Diagnostic Checking → Forecasting/Validation。
3. p/q 的统计结构应由差分后的序列识别；d 过大时会引入近不可逆 MA 结构。
4. 含 drift 的 ARIMA(0,1,0) 可写成随机游走加平均增量，长期预测是线性外推。

### 2. 一条可复用的推理链

回答 **“解释 ARIMA(p,d,q)。”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 把 I 解释成 interpolation。
- **边界 2：** 只用 in-sample AIC 选模型，不做残差白噪声和滚动回测。
- **边界 3：** 对明显多季节、多变量、强非线性问题仍执着于单一 ARIMA。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

日销量若含 weekly seasonality，普通 ARIMA 可能在残差 lag-7 留下显著结构，应考虑 SARIMA、Fourier regression 或其他季节模型。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

ARIMA 的价值之一是结构清晰、样本效率高、prediction interval 可解析构造；这也是它仍应作为强 baseline 的原因。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 经典模型闭环 Checklist

- [ ] 先与 Naive/Seasonal Naive 比较
- [ ] 识别→估计→诊断→回测
- [ ] 检查参数稳定、残差白噪声和区间质量

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** ARIMA 先通过 d 阶差分把非平稳 level 转为近似平稳序列，再用 AR(p)+MA(q) 建模其线性依赖。
>
> **第二层解释机制。** 高分回答必须补一句：ARIMA 不只是“ACF/PACF 选阶”，还要做残差白噪声诊断和 out-of-sample rolling validation。
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

> **结论：** ARIMA 先通过 d 阶差分把非平稳 level 转为近似平稳序列，再用 AR(p)+MA(q) 建模其线性依赖。  
> **原理：** 高分回答必须补一句：ARIMA 不只是“ACF/PACF 选阶”，还要做残差白噪声诊断和 out-of-sample rolling validation。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q024 AR 和 MA 最大的直觉差异是什么？](../03-classical-models/q024-ar-vs-ma.md)
- [Q026 如何选择 p,d,q？](../03-classical-models/q026-select-pdq.md)
- [Q027 SARIMA 是什么？](../03-classical-models/q027-sarima.md)
- [Q029 如何判断 ARIMA 拟合完成？](../03-classical-models/q029-arima-residual-diagnostics.md)

## 延伸阅读

- [FPP - ARIMA models](https://otexts.com/fpp3/arima.html)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
