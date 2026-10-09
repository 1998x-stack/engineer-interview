---
title: Advanced Micro Interview Methods
---

# Advanced Micro Interview Methods

这份索引把 100 题背后的研究生级方法压缩成可复用的面试工具。目标不是增加术语，而是帮助你在陌生题里迅速选择正确模型。

## 1. 四类最优化问题

1. **消费者 primal**：maximize utility subject to budget；
2. **消费者 dual**：minimize expenditure subject to utility；
3. **企业成本最小化**：minimize input cost subject to output；
4. **企业利润最大化**：maximize revenue minus cost。

每次看到题目先问：目标函数是谁的？choice variable 是什么？约束是什么？

## 2. 五类均衡

- Walrasian market-clearing；
- Nash / subgame-perfect；
- matching / search；
- rational-expectations / dynamic state equilibrium；
- mechanism / contract 中的 IC-compatible allocation。

## 3. Comparative statics

用隐函数定理统一理解：若 $F(y,θ)=0$，则局部有 $dy/dθ=-F_θ/F_y$。面试中不必总写完整矩阵，但要能说清参数影响“哪一个边际条件”。

## 4. Counterfactual discipline

所有政策、并购、侵权、cartel、补贴、税收问题都应问：

> actual outcome 应与哪个 **but-for outcome** 比较？

“前后变化”只有在前期真的是合适反事实时才等于因果效应。

## 5. Identification before regression

先写 estimand，再判断解释变量为何内生，最后选证据。常见识别困难：simultaneity、selection、omitted variables、reverse causality、measurement error、anticipation。

## 6. Model risk

任何漂亮结论都要附带至少一个边界：角点、非凸、容量、动态、异质性、一般均衡、信息不对称、多产品或制度约束。
