# 控制系统工程调试 Checklist

## 1. 信号正确性
- [ ] feedback sign
- [ ] unit / scale
- [ ] coordinate frame
- [ ] sensor direction

## 2. 时序
- [ ] sample time
- [ ] timestamp alignment
- [ ] end-to-end delay
- [ ] jitter / dropped sample

## 3. 执行器
- [ ] amplitude saturation
- [ ] rate limit
- [ ] current/torque limit
- [ ] anti-windup status

## 4. 传感器与估计
- [ ] raw vs filtered signal
- [ ] bias / drift
- [ ] innovation/residual
- [ ] estimator covariance consistency

## 5. 结构动态
- [ ] crossover / PM / GM
- [ ] mechanical resonance
- [ ] unmodeled flexible mode
- [ ] aliasing / notch side effects

## 6. 验证闭环
- [ ] reproduce in simulation
- [ ] parameter sweep / Monte Carlo
- [ ] SIL/HIL
- [ ] A/B experiment
- [ ] regression test
