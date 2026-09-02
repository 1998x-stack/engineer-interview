# 面试答题 Playbook

## 30 秒版本

1. 一句话定义。
2. 一句话核心机制。
3. 一句话指出主要 trade-off。

## 5 分钟版本

```text
Problem / Assumption
→ Core mechanism
→ Formula / System diagram
→ Failure modes
→ Engineering metric
→ Verification experiment
```

## 项目拷打

不要说“用了某模型，提升很多”。改成：

```text
Baseline: success=62%, P95 latency=80ms
Failure taxonomy: 45% calibration, 30% action jitter, 25% grasp semantics
Evidence: replay + frame overlay + ablation
Change: recalibration + action chunk smoothing
Result: success 62%→84%, P95 latency +6ms
Trade-off: faster motions still fail on reflective objects
```

## 失败归因的五层

- Data / supervision
- Perception / state
- Policy / planning
- Control / calibration
- Hardware / timing / communication
