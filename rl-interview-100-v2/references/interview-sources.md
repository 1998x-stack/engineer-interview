# 公开面经口径说明 · Evidence Policy

本仓库把“面经”只用于判断 **题型与复习优先级**，不把匿名帖子当算法事实来源。

## 题源标签

### 公开面经真题 / 母题

公开面经中存在直接对应或高度一致的问题。仓库会做原创改写，**不声称逐字复现公司内部题目**。

### 高频追问 / 扩展题

沿母题常见二问、三问展开，或根据原论文补足推导、工程和边界条件。

### 核心理论 / 系统设计

未必来自某一条面经，但属于岗位能力模型不可缺失的题。

## 事实证据优先级

```text
原论文 / 官方文档 / 教材
    >
公开实现与作者仓库
    >
高质量技术文章
    >
公开面经（仅题型）
```

如果面经中的说法与论文冲突，以原论文/官方资料为准，并在题目页把“PDF 原始要点”和“Repo 扩展解析”分开。

## 2026 高权重方向

- 传统游戏/控制：MC/TD、on/off-policy、Q-learning、DQN tricks、PPO、reward design、自博弈；
- 机器人：连续动作、DDPG/TD3/SAC、Sim2Real、并行采样；
- LLM Post-training：PPO、KL、Reward Model、DPO、GRPO；
- 2025–2026 Reasoning RL：DAPO、GSPO、zero-signal group、entropy collapse、long-tail rollout、policy lag、RL infra。

## 使用建议

面试前不要背“某公司问过什么”作为答案。正确做法是：

1. 用面经决定优先级；
2. 用本仓库题目页建立 30 秒/90 秒回答；
3. 用 Primary Papers 校验公式；
4. 用最小代码/实验验证；
5. 最后把方法迁移到自己的项目。
