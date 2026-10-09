---
id: q090
title: "如何利用 STL 做异常检测？"
chapter: 8
difficulty: "★★★☆☆"
frequency: "★★★★☆"
tags: ["STL", "残差", "MAD"]
source: "PDF 2026.09"
---

# Q090 如何利用 STL 做异常检测？

> **章节：** 异常检测、变化点与漂移  
> **难度：** ★★★☆☆ ｜ **频率：** ★★★★☆  
> **关键词：** STL / 残差 / MAD

> [!NOTE]
> **内容来源说明：** “PDF 基线”部分来自仓库附带的《时间序列面试100题_专业详细版_2026.pdf》；“专业扩展”及代码是为 GitHub 版新增的讲解与工程化补充。二者明确分开，便于回溯。

## 20 秒面试回答

先用 STL 提取趋势与季节，再对 remainder 做 robust threshold，可减少季节性导致的误报。

## PDF 基线：核心公式 / 结构

$$
r_t=y_t-T_t-S_t; z_robust=(r-med)/1.4826MAD
$$

> 若上面的内容是流程或文字而不是严格 LaTeX 公式，请按 PDF 原意理解；PDF 中的记号在此保持不变。

## PDF 基线：原理深挖

生产上要防 STL 使用未来信息：在线异常检测应使用 causal/rolling decomposition 或只在已发生历史上更新。

### PDF 易错点

> 用双向平滑分解做实时告警评估。

### PDF 高级加分点

> （PDF 未给独立高级加分点。）

---

## 专业扩展（GitHub 增强版）

### 1. 这道题真正考什么

线上时序系统必须区分偶发异常、永久机制变化和渐进漂移；三者对应的告警、重训和业务动作不同。

- 从本题继续追问时，优先沿着‘假设 -> 统计直觉 -> 回测 -> 工程约束’展开。
- 线上时序系统必须区分偶发异常、永久机制变化和渐进漂移；三者对应的告警、重训和业务动作不同。

### 2. 建议使用的“剑指 Offer 式”回答层次

1. **先定义**：用一句话说明对象、假设或目标。
2. **给核心数学结构**：能写公式就写公式；不能写时明确输入、状态和输出。
3. **解释统计直觉**：说明为什么成立，以及它改变了什么信息。
4. **指出失败模式**：样本太短、非平稳、结构突变、协变量不可用、泄漏等。
5. **落到验证与工程**：给出时间正确的 backtest、baseline、监控或 decision metric。

### 3. 面试官追问树

### 1. 为什么 MAD 比 std 稳健？

**回答方向：** 回答时不要停在现象层。先说明其改变的统计/信息条件，再指出对验证或部署的影响。可结合本题核心：先用 STL 提取趋势与季节，再对 remainder 做 robust threshold，可减少季节性导致的误报。

### 2. 异常会污染 trend 吗？

**回答方向：** 围绕本章主线回答：线上时序系统必须区分偶发异常、永久机制变化和渐进漂移；三者对应的告警、重训和业务动作不同，并落到假设、验证与工程边界。


### 4. 工程检查清单

- [ ] 区分数据质量故障、异常、change point 与 drift。
- [ ] 告警应带 severity、segment、horizon 和业务影响。
- [ ] 重训不是唯一动作：还可 fallback、缩短窗口、切换 regime model。


## 最小可运行示例

```python
import numpy as np
from statsmodels.tsa.seasonal import STL

resid = STL(y, period=7, robust=True).fit().resid
med = np.nanmedian(resid)
mad = np.nanmedian(np.abs(resid - med))
robust_z = (resid - med) / (1.4826 * mad + 1e-12)
anomaly = np.abs(robust_z) > 3.5
```

<!-- V2_DEEP_DIVE_START -->
## 深度专业版 v2：从“会答”到“能推导、能上线”

> 这一节是 GitHub 版第二轮扩展，不改写上面的 PDF 基线。目标是把题目扩展到高级算法岗 / Forecasting Scientist / Staff DS 面试所要求的深度。

### 1. 核心机制拆解

1. STL anomaly detection 先移除 trend/seasonality，再在 remainder 上检测离群。
2. robust STL 可避免异常点污染 decomposition；remainder 阈值可用 MAD/IQR/robust z-score。
3. 检测阈值需要随业务 false-positive cost 校准。

### 2. 一条可复用的推理链

回答 **“如何利用 STL 做异常检测？”** 时，推荐按下面顺序组织，而不是先抛模型名：

1. **定义对象与信息边界**：目标变量、时间粒度、forecast origin、horizon、当前可用信息分别是什么。
2. **写最小数学结构**：指出核心随机关系、损失函数或约束。
3. **说明成立条件**：平稳性、独立性、未来协变量可用性、样本长度、分布假设等。
4. **给反例或失败模式**：至少说明一种“理论上成立但工程上失败”的情况。
5. **落到 OOS 证据**：用 rolling / expanding backtest 和强 baseline 证明选择，而不是靠模型复杂度。

### 3. 典型反例、边界与故障模式

- **边界 1：** 先普通 STL 后异常点已经扭曲 trend，再对 remainder 设阈值。
- **边界 2：** 用全历史未来数据拟合 decomposition 做实时告警，形成 look-ahead。

> **面试习惯：** 只会描述模型“优点”通常是中级答案；主动说出失效条件、可观测症状和修复动作，才更接近高级答案。

### 4. 具体业务例子

网站流量有强日/周周期，直接 z-score 会把每天夜间低谷误报；STL remainder 更合适。

把例子继续追问到工程层时，至少要回答：**这个变量在预测 cutoff 当时真的可见吗？这个 horizon 的误差由谁承担？模型失败时 fallback 是什么？**

### 5. 高级加分点

实时场景需 causal/online decomposition 或只用过去窗口，经典双向 smoother 可能偷看未来。

这一点不是为了“炫术语”，而是为了说明你能把统计原理、验证协议和生产约束放在同一个框架里。

### 6. 在线鲁棒性 Checklist

- [ ] 定义 anomaly/drift 的业务后果
- [ ] 监控 detection delay 与 false positive
- [ ] 预先设计 retrain/rollback/fallback

建议把 checklist 真正落实到实验记录中：每个候选模型保存 `data_snapshot / cutoff / feature_version / model_version / horizon / metrics_by_segment`，才能复现实验和定位线上偏差。

### 8. 2～3 分钟完整口述参考

> **第一句先给结论。** 先用 STL 提取趋势与季节，再对 remainder 做 robust threshold，可减少季节性导致的误报。
>
> **第二层解释机制。** 生产上要防 STL 使用未来信息：在线异常检测应使用 causal/rolling decomposition 或只在已发生历史上更新。
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

> **结论：** 先用 STL 提取趋势与季节，再对 remainder 做 robust threshold，可减少季节性导致的误报。  
> **原理：** 生产上要防 STL 使用未来信息：在线异常检测应使用 causal/rolling decomposition 或只在已发生历史上更新。  
> **边界：** 说明何时假设会失效，以及如何通过 rolling/expanding backtest 验证。  
> **工程：** 把预测时点、特征可用性、horizon、指标和 fallback 说清楚。

## 关联题

- [Q089 Point、Contextual 和 Collective Anomaly 有何区别？](../08-anomaly-drift/q089-anomaly-types.md)
- [Q091 Change Point Detection 和 Anomaly Detection 有何不同？](../08-anomaly-drift/q091-change-point-vs-anomaly.md)

## 延伸阅读

- [FPP - Practical forecasting issues](https://otexts.com/fpppy/)

---

**上一层目标：** 不只会“背答案”，而是能解释 **why / when it fails / how to validate / how to ship**。
