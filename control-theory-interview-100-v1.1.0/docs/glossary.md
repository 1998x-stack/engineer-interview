# 术语表

| 术语 | 简明定义 |
|---|---|
| Loop gain $L$ | 控制器与对象在环路中的开环乘积 |
| Sensitivity $S$ | $1/(1+L)$，反映误差/扰动/模型敏感度的重要闭环函数 |
| Complementary sensitivity $T$ | $L/(1+L)$，且 $S+T=1$ |
| Bandwidth | 闭环有效跟踪/响应的主要频率范围 |
| Phase margin | gain crossover 处距离 -180° 的相位余量 |
| Controllability | 输入能否驱动全部状态/模态 |
| Observability | 输出历史能否区分/恢复全部状态/模态 |
| Stabilizable | 所有不可控模态均稳定 |
| Detectable | 所有不可观模态均稳定 |
| Innovation | 测量与预测输出之差 $y-C\hat x$ |
| Anti-windup | 饱和时防止/解除积分器状态过度累积的机制 |
| Non-minimum phase | 存在 RHP zero 等导致稳定因果逆不可实现的特性 |
