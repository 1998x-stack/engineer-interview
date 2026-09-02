# Manipulation 路线：从几何到实机策略

```text
SE(3) / Frame
  → FK / IK / Jacobian
  → Collision-free Planning
  → PID / Impedance / Force
  → Teleoperation & Dataset
  → BC / ACT / Diffusion
  → VLA Action Head
  → Receding Horizon + Low-level Controller
  → Real Robot Evaluation
```

## 必做练习

1. 手写 SE(3) 逆变换与 frame composition。
2. 实现 Damped Least Squares IK。
3. 解释一个“抓取失败”如何区分 perception / IK / control / policy。
4. 对同一 demonstration 比较 single-step BC、ACT、Diffusion 的动作分布与实时性。
