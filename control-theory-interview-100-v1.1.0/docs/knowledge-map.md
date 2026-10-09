# 知识图谱

```text
建模 ─→ 传递函数 ─→ 极点/零点 ─→ 时域指标
  │          │               └→ Root Locus ─→ Lead/Lag
  │          └→ Bode/Nyquist ─→ PM/GM ─→ S/T ─→ 鲁棒直觉
  │
  └→ 状态空间 ─→ eigenstructure ─→ controllability ─→ state feedback ─→ LQR
                 └→ observability ─→ observer ─→ Kalman ─→ LQG

LQR + constraints ─→ MPC
模型集合 + worst-case ─→ H∞ / robust control
参数在线变化 ─→ adaptive control

连续实现 ─→ sampling/ZOH/z-plane ─→ quantization/jitter/delay ─→ 实机验证

非线性系统 ─→ linearization ─→ Lyapunov ─→ feedback linearization / SMC / backstepping
```

## 建议学习顺序

先建立经典闭环直觉，再学状态空间结构；之后把 LQR/Kalman/MPC 看成结构化扩展；最后学习鲁棒、非线性和实时实现。
