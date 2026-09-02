# Question Writing Standard · V2

本标准用于保证 100 道题不是“同一模板换标题”，而是每道题都包含题目特定的数学、金融或工程内容。

## 1. 固定 14 段

1. 面试官到底在考什么
2. 先给结论（30 秒版本）
3. Formalization：变量、假设与数学对象
4. 标准推导：从第一原则得到答案
5. Why：为什么这个方法有效
6. 量化金融 / 工程语境中的对应问题
7. 边界条件、失效场景与模型风险
8. 追问树：问题 + 回答方向
9. 高频错误：错误为什么会发生
10. 3 分钟专业回答模板
11. 自测与延伸练习
12. 关联题目
13. 延伸阅读
14. 来源与内容边界

## 2. 数学内容标准

- 公式必须定义变量；
- 明确条件，不把定理无条件化；
- 若有 closed form，至少说明一条推导主线；
- 若有经典反例，优先加入反例；
- 渐近结论要标明 asymptotic，不与有限样本混淆。

## 3. 统计 / ML 内容标准

必须至少讨论其中三项：

- data generating process；
- point-in-time availability；
- estimator uncertainty；
- time-aware validation；
- multiple testing；
- calibration / drift；
- OOS incremental utility。

“模型分数更高”不能作为完整结论。

## 4. 回测 / 市场内容标准

必须显式考虑：

- timestamp；
- universe/PIT；
- cost；
- fill；
- latency；
- capacity / market impact（相关时）；
- replay / counterfactual validation。

## 5. 系统题标准

至少覆盖：

- input/output contract；
- state / invariant；
- time complexity；
- memory / cache behavior；
- duplicate / gap / out-of-order；
- idempotency / recovery；
- test / replay strategy。

## 6. 来源标准

- 不把未公开题归因给具体公司；
- PDF 原内容与扩展分析要分开标注；
- 外部事实若加入，优先使用官方/教材/论文并可核验；
- 教学解释可以扩展，但不能伪装成公司官方标准答案。

## 7. Anti-template 检查

Technical review 时至少问：

> 如果把题目标题换成同章节另一题，这一节是否仍然“完全说得通”？

如果答案是“是”，说明内容仍然太泛，需要加入题目特定推导、反例、数据结构或实验设计。
