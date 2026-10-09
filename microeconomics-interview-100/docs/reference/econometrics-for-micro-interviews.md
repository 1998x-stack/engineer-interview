---
title: Micro Interview Econometrics
---

# 微观面试中的因果识别与计量工具

这不是计量教材，而是为 Q073–Q100 等应用题准备的“识别语言”。

## 1. 先定义 estimand

例如需求弹性、pass-through、overcharge、lost profit、merger price effect。没有 estimand，回归式只是描述。

## 2. 常见内生性

- **simultaneity**：价格与数量共同由供需决定；
- **selection**：谁接受合同/进入平台并非随机；
- **omitted variables**：质量、成本、宏观需求同时影响解释变量与结果；
- **reverse causality**：企业因预期需求弱而降价；
- **measurement error**：价格、质量、市场份额构造误差。

## 3. 常见设计语言

- IV：相关性 + exclusion；
- DID：parallel trends + no differential anticipation；
- event study：动态路径和 pre-trend；
- RDD：阈值附近连续性；
- structural estimation：行为模型 + 参数识别 + counterfactual simulation。

## 4. 面试表达模板

> “我不是先选择回归，而是先明确需要识别 X。X 的内生性来自 Y，因此我需要一个只通过 Z 影响 X 的外生变化；如果这个 exclusion 不可信，我会换 benchmark 或结构。”
