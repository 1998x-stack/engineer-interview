# E. 机器学习与 Financial ML

> **模块目标**：Financial ML  
> **统一方法**：把模型放在完整数据协议里评估：特征可用时间、OOS 切分、校准、漂移、线上一致性往往比模型复杂度更重要。

## 1. 为什么这一章重要

这一章不是孤立知识点集合，而是一组在 Quant Research / Algorithm 面试中反复出现的**推理模式**。真正的掌握标准不是“看过公式”，而是能在新题里识别同一结构，并说清楚假设、推导、边界与验证。

## 2. 学习目标

- 建立 strong baseline 与完整 ML pipeline
- 理解 metric/calibration/drift
- 掌握 offline-online parity 诊断

## 3. 面试能力分层

### Level 1：会做
能在 2–5 分钟内得到基础答案，符号和条件不出错。

### Level 2：会解释
能回答“为什么”，并给出至少一个反例/边界条件。

### Level 3：会迁移
能把数学结构映射到真实市场数据、研究协议或系统设计。

### Level 4：会审计
面对异常结果时，主动检查数据生成、时间信息、统计假设和实现差异，而不是默认结论正确。

## 4. 本章 10 题

| 题目 | 难度 | 标签 |
|---|---:|---|
| [041. 训练准确率 99%，测试 52%，你首先检查什么？](q041-训练准确率-99%-测试-52%-你首先检查什么.md) | ★★☆ | Debugging｜leakage｜overfit |
| [042. 为什么线性模型在金融预测中仍然重要？](q042-为什么线性模型在金融预测中仍然重要.md) | ★★☆ | Linear model｜inductive bias｜鲁棒性 |
| [043. Random Forest 与 Gradient Boosting 的根本区别？](q043-Random-Forest-与-Gradient-Boosting-的根本区别.md) | ★★☆ | Tree ensemble｜bagging｜boosting |
| [044. Feature scaling 为什么会造成未来信息泄漏？](q044-Feature-scaling-为什么会造成未来信息泄漏.md) | ★☆☆ | Preprocessing｜pipeline｜leakage |
| [045. 一个 feature 的 IC 很低，是否一定没有价值？](q045-一个-feature-的-IC-很低-是否一定没有价值.md) | ★★☆ | Signal evaluation｜interaction｜nonlinearity |
| [046. 如何判断分类概率是否 calibrated？](q046-如何判断分类概率是否-calibrated.md) | ★★☆ | Calibration｜Brier｜reliability |
| [047. Finance 中为什么 accuracy 往往不是好指标？](q047-Finance-中为什么-accuracy-往往不是好指标.md) | ★☆☆ | Imbalanced data｜metric｜utility |
| [048. 什么时候 Transformer 可能优于传统时间序列模型？](q048-什么时候-Transformer-可能优于传统时间序列模型.md) | ★★★ | Transformer｜长序列｜多变量 |
| [049. 什么是 Concept Drift？](q049-什么是-Concept-Drift.md) | ★★☆ | Distribution shift｜drift｜monitoring |
| [050. 模型 offline 很好，上线立即下降，如何系统排查？](q050-模型-offline-很好-上线立即下降-如何系统排查.md) | ★★★ | Research-to-production｜debug｜MLOps |

## 5. 推荐刷题顺序

1. **第一遍：** 只做题，不看答案，每题限制 10 分钟。
2. **第二遍：** 强制补“假设 + Why + 一个失效场景”。
3. **第三遍：** 回答每题追问树，并做 30 秒口述。
4. **第四遍：** 把本章知识迁移到一个真实 research/system 案例。

## 6. 本章检查清单

完成本章后，你应该能：

- [ ] 不看答案复述 10 题核心结论；
- [ ] 对每题写出 formal model / key equation；
- [ ] 至少指出一个常见误用；
- [ ] 给出一个量化金融中的对应场景；
- [ ] 解释如何用 OOS / simulation / replay 验证。

## 7. 推荐阅读

- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*；López de Prado, *Advances in Financial Machine Learning*
- [知识地图](../../docs/knowledge-map.md)
- [100 题总索引](../../docs/100-question-index.md)
- [面试回答框架](../../docs/interview-answer-framework.md)
