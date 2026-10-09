# 第 10 章：系统设计与故障定位

> **章节目标**：把 CAN 题提升到网关、诊断、端到端时延和自动测试平台设计。

## 1. 章节心智模型

```text
Source ECU/Service → CAN/PDU → Gateway/Route → Target ECU stack → Application state machine → Actuator/HMI → feedback；每个边界都有观测点和 failure mode。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- Bus Load 与 worst-case 的区别
- Gateway 不是透明导线
- 周期/事件/混合发送策略
- Timeout 阈值与恢复
- CAN→ISO-TP→UDS 分层
- 端到端故障树与统一时间戳

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q091 CAN 总线负载率怎么计算？](../questions/10-system-debug-design/Q091.md) | S - 必须掌握 | 3/3 |
| [Q092 总线负载过高有哪些优化手段？](../questions/10-system-debug-design/Q092.md) | A - 高频掌握 | 2/3 |
| [Q093 Gateway 在 CAN 网络中做什么？为什么它会影响故障定位？](../questions/10-system-debug-design/Q093.md) | A - 高频掌握 | 2/3 |
| [Q094 周期报文、事件报文和混合报文怎么选？](../questions/10-system-debug-design/Q094.md) | B - 进阶理解 | 1/3 |
| [Q095 Timeout 阈值应该如何设计？](../questions/10-system-debug-design/Q095.md) | A - 高频掌握 | 2/3 |
| [Q096 CAN、ISO-TP 与 UDS 是什么关系？](../questions/10-system-debug-design/Q096.md) | A - 高频掌握 | 2/3 |
| [Q097 ISO-TP 为什么存在？SF/FF/CF/FC 分别是什么？](../questions/10-system-debug-design/Q097.md) | A - 高频掌握 | 2/3 |
| [Q098 “打开右前车窗”从 HMI 到执行器的完整链路如何讲？](../questions/10-system-debug-design/Q098.md) | A - 高频掌握 | 2/3 |
| [Q099 发送 CAN Signal 后 ECU 没有返回，如何系统定位？](../questions/10-system-debug-design/Q099.md) | S - 必须掌握 | 3/3 |
| [Q100 如何从零设计“CAN → 真实 ECU → 车机 UI”的自动测试系统？](../questions/10-system-debug-design/Q100.md) | S - 必须掌握 | 3/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

用 `vcan`/模拟服务构造 source→gateway-like router→target 三段链路，练习双侧 Trace 与端到端 timestamp。

## 6. 面试自检

完成本章后，应能回答：

- 我能否在 **30 秒**内给出定义且不说错边界？
- 我能否在 **3 分钟**内讲清底层机制？
- 我能否给出一个真实工程场景和观测点？
- 我能否指出至少两个常见错误答案为什么错？
- 如果面试官给一段 Trace/DBC/日志，我能否用本章模型定位它属于哪一层？

## 7. 与其它章节的连接

```text
基础帧/仲裁/物理/错误
        ↓
CAN FD 与 DBC 数据模型
        ↓
ECU 软件栈
        ↓
CANoe / Python 测试
        ↓
Gateway / UDS / 端到端系统设计
```

单章知识只有连接到上下游，才能在项目题里发挥作用。
