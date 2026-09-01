# 03. 目标函数、Optimizer 与 Training Recipe

从 CLM、AdamW、warmup、batch 到 MTP，理解训练 recipe 的优化逻辑。

## 本章训练目标

- 不只会定义：能够写公式、画数据/通信流；
- 不只会 Why：能够说明代价、失效边界和等成本实验；
- 不只会小规模：能够把问题映射到真实预训练系统。

## 题目

- [Q021. Causal LM Loss 是什么？为什么 Next-Token Prediction 能学出复杂能力？](./021.md) · B 类等价追问题 · ★★★★★ · 中
- [Q022. 为什么训练能并行预测所有 Token，而推理必须逐 Token 生成？](./022.md) · B 类等价追问题 · ★★★★☆ · 易
- [Q023. AdamW 为什么长期是 LLM 预训练默认优化器？](./023.md) · A 类高频真题型 · ★★★★★ · 中
- [Q024. 为什么大模型训练需要 Learning-Rate Warmup？](./024.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q025. Cosine Decay 为什么常见？Continued Pretraining 如何重设 LR？](./025.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q026. Batch Size 增大后，优化和系统分别发生什么？](./026.md) · B 类等价追问题 · ★★★★☆ · 中
- [Q027. Global Batch、Micro Batch、Gradient Accumulation 如何换算？](./027.md) · A 类高频真题型 · ★★★★★ · 易
- [Q028. Weight Decay 为什么通常不施加到所有参数？](./028.md) · B 类等价追问题 · ★★★☆☆ · 中
- [Q029. 为什么 Label Smoothing 不是 LLM 预训练的默认配置？](./029.md) · B 类等价追问题 · ★★★☆☆ · 中
- [Q030. Multi-Token Prediction（MTP）为什么重新受到重视？](./030.md) · B 类等价追问题 · ★★★★☆ · 难
