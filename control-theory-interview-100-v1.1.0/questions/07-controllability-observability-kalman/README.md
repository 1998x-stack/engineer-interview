# 第 7 章：可控可观、观测器与 Kalman

从结构性质走向状态估计和传感器融合。

题号：Q061–Q070

## 本章题目

- [Q061. 可控性是什么意思？Kalman rank test 在看什么？](q061.md) — 基础 · ★★★★★
- [Q062. 不可控系统一定不能稳定吗？Stabilizable 是什么？](q062.md) — 进阶 · ★★★★★
- [Q063. 可观性是什么意思？为什么“传感器少”不等于不可观？](q063.md) — 基础 · ★★★★★
- [Q064. Detectability 是什么？为什么观测器不一定要求完全可观？](q064.md) — 进阶 · ★★★★☆
- [Q065. Luenberger Observer 如何推导？](q065.md) — 基础 · ★★★★★
- [Q066. Observer poles 为什么不能无限快？](q066.md) — 工程 · ★★★★★
- [Q067. Separation Principle 为什么重要？](q067.md) — 进阶 · ★★★★★
- [Q068. Kalman Filter 和 Luenberger Observer 的本质关系？](q068.md) — 进阶 · ★★★★★
- [Q069. Kalman Filter 的 predict/update 两步各在做什么？](q069.md) — 基础 · ★★★★★
- [Q070. Kalman 中 Q、R 怎么调？为什么不能把它们当普通“滤波强度旋钮”？](q070.md) — 工程 · ★★★★★

## 章节学习建议

可控/可观问题不要只报 rank。rank test 是代数判据，真正的工程问题是：**某个模态能否被执行器影响？某个模态能否在传感器数据中留下可辨识痕迹？** 稳定但不可控/不可观的模态有时可接受，不稳定模态则必须分别满足 stabilizable/detectable。

观测器设计还必须考虑噪声与模型误差；把 observer pole 设得极快虽然名义收敛快，却会显著放大 measurement noise，并暴露离散采样和数值问题。

## 专业学习框架

### 知识主线

- controllability/PBH/Gramian
- stabilizable/detectable
- Luenberger observer
- Separation principle
- Kalman predict/update 与 consistency

### 学完本章应达到

- [ ] 不仅会 rank test，还会解释“难控/难观”
- [ ] 能从 error dynamics 推 observer
- [ ] 能用 innovation/NIS 而非肉眼调 Q/R

### 面试表达原则

结构可行只是第一层；真正工程问题是 energy、conditioning、noise 和 estimator bandwidth。

### 推荐复习顺序

1. 先做本章所有 ★★★★★ 题，只练 30 秒结论。
2. 第二遍只做公式/白板推导，不看标准答案。
3. 第三遍逐题回答“什么时候失效”和“如何用实验验证”。
4. 最后从本章任选两题串成连续追问链，练 5–10 分钟深挖。

## 推荐实验

- 运行 `examples/python/07_*.py` 对应实验。
- 每道题至少完成一次 30 秒口述和一次白板推导。
