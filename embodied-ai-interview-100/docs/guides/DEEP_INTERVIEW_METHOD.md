# 深度面试方法论：从“知道答案”到“系统级推理”

本指南用于配合 100 道题的 GitHub v2 深度增强版。

## 1. 每道题固定用五层理解

```text
Definition → Mechanism → Boundary → Evidence → System impact
```

- **Definition**：变量、空间、时间尺度；
- **Mechanism**：为什么有效，最好有公式；
- **Boundary**：什么条件下失效；
- **Evidence**：如何做 A/B、怎样量化；
- **System impact**：对数据、控制、延迟、安全的影响。

## 2. 具身题最重要的四个“坐标系”

除几何 frame 外，还要持续区分：

1. **空间坐标系**：camera/base/world/tool；
2. **时间坐标系**：sensor timestamp、policy rate、servo rate；
3. **数据坐标系**：train/val/deploy distribution；
4. **责任坐标系**：perception / policy / planner / controller / hardware。

大多数实机故障都可以沿这四个轴定位。

## 3. 面试白板最低标准

- 机器人学：画 frame + 写 mapping / Jacobian；
- 感知：画 timestamp + transform + estimator；
- 控制：画 closed loop；
- IL/RL：画 data distribution / rollout loop；
- VLA：画 multimodal backbone → action head → controller；
- World Model：画 action-conditioned future + planner；
- 系统题：画 SLO → modules → telemetry → fallback → data flywheel。

## 4. 项目题统一证据链

```text
Baseline → Failure taxonomy → Evidence → Hypothesis → Ablation → Result → Trade-off
```

没有 baseline 数字的“优化”难以验证；没有 failure taxonomy 的“效果不好”无法诊断；没有 ablation 的“提升”无法归因。
