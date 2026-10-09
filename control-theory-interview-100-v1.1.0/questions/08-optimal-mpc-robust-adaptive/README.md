# 第 8 章：最优、MPC、鲁棒与自适应

理解 LQR/LQG/MPC/H∞ 等算法解决的不同问题。

题号：Q071–Q080

## 本章题目

- [Q071. 为什么 Pole Placement 之后还需要 LQR？](q071.md) — 进阶 · ★★★★★
- [Q072. LQR 中 Q、R 如何选？](q072.md) — 工程 · ★★★★★
- [Q073. CARE / Riccati 方程在 LQR 中为什么出现？](q073.md) — 高级 · ★★★★☆
- [Q074. LQG 是什么？为什么“最优”不等于“鲁棒”？](q074.md) — 高级 · ★★★★☆
- [Q075. MPC 和 LQR 最大区别是什么？](q075.md) — 进阶 · ★★★★★
- [Q076. MPC horizon N 怎么选？越长越好吗？](q076.md) — 工程 · ★★★★☆
- [Q077. 什么是鲁棒控制？Nominal stability 与 robust stability 有何区别？](q077.md) — 进阶 · ★★★★★
- [Q078. H-infinity 控制的核心目标是什么？](q078.md) — 高级 · ★★★★☆
- [Q079. 自适应控制和鲁棒控制有何本质不同？](q079.md) — 进阶 · ★★★★☆
- [Q080. 什么是 disturbance observer / ADRC 类思想？](q080.md) — 工程 · ★★★★☆

## 章节学习建议

现代控制算法不要用“高级程度”排序，而要按它们解决的问题排序：Pole placement 解决极点位置，LQR 解决二次代价下的反馈权衡，Kalman 解决随机估计，MPC 解决有限时域优化与显式约束，鲁棒控制解决模型族的最坏情况，自适应控制解决在线参数变化。

面试时最有价值的回答通常是“为什么需要它，而不是更简单的方法”。如果没有约束，MPC 未必优于精心设计的 LQR；如果模型不确定性很小，也未必需要 $H_\infty$。

## 专业学习框架

### 知识主线

- LQR/Riccati
- LQG 与 robustness
- MPC constraints/horizon
- H∞/small-gain/μ
- adaptive/DOB/ADRC

### 学完本章应达到

- [ ] 能解释“最优依赖什么假设/代价”
- [ ] 能把 hard constraints 与普通 state feedback 区分
- [ ] 能区分 robust 与 adaptive 的问题设定

### 面试表达原则

算法名不是答案。先定义 cost、constraints、uncertainty、noise 和 compute budget，再谈 LQR/MPC/H∞。

### 推荐复习顺序

1. 先做本章所有 ★★★★★ 题，只练 30 秒结论。
2. 第二遍只做公式/白板推导，不看标准答案。
3. 第三遍逐题回答“什么时候失效”和“如何用实验验证”。
4. 最后从本章任选两题串成连续追问链，练 5–10 分钟深挖。

## 推荐实验

- 运行 `examples/python/08_*.py` 对应实验。
- 每道题至少完成一次 30 秒口述和一次白板推导。
