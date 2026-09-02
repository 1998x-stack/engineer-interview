# 第七篇 ACT / Diffusion / Flow Matching

> 理解现代动作生成器为什么从单步回归走向 action chunk 与生成式建模。

ACT 解决时间一致性，Diffusion 解决多模态动作分布，Flow Matching进一步面向高频连续控制。三者是当前具身面试的核心算法链。

## 本章题目

- [Q061 · ACT 为什么要预测 Action Chunk？](Q061.md) · ★★★★
- [Q062 · ACT 为什么使用 CVAE？Latent z 在表示什么？](Q062.md) · ★★★★
- [Q063 · ACT 的 Temporal Aggregation 是什么？](Q063.md) · ★★★★
- [Q064 · Diffusion Policy 为什么适合机器人动作？](Q064.md) · ★★★★
- [Q065 · Diffusion Policy 的训练目标是什么？](Q065.md) · ★★★★
- [Q066 · Diffusion Policy 最大的部署瓶颈是什么？如何加速？](Q066.md) · ★★★★
- [Q067 · Flow Matching 与 Diffusion 有什么区别？](Q067.md) · ★★★★★
- [Q068 · Action Chunk 为什么不能无限长？](Q068.md) · ★★★★
- [Q069 · Receding Horizon Control 为什么和生成式动作策略很搭？](Q069.md) · ★★★★
- [Q070 · ACT、Diffusion、Flow Matching 三者应该怎么选？](Q070.md) · ★★★★★

## 建议学法

1. 先用 30 秒口述每题。
2. 再闭卷写核心公式或系统图。
3. 最后用自己的项目替换“项目迁移题”中的抽象场景。


## GitHub v2 深度阅读要求

本模块的每一道题都不再以“背定义”为完成标准。建议至少完成四步：

1. **30 秒**：说清本质与边界；
2. **5 分钟**：能写关键公式/结构图，并解释 why；
3. **工程层**：能列失败模式、指标和最小验证实验；
4. **项目层**：能把答案映射到自己的机器人/数据/控制系统，并给出 baseline 与 ablation。

> 判断是否真正掌握：面试官把题目中的机器人、传感器、控制频率或数据规模换掉，你仍能重新推导，而不是只能复述原答案。
