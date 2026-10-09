# 第 07 章：ECU 软件收发链路

> **章节目标**：把总线帧与 MCU Controller、Driver、AUTOSAR 通信栈和 Application 连接成完整调用链。

## 1. 章节心智模型

```text
CAN_H/L → Transceiver → Controller → Filter/FIFO → ISR/Driver → CanIf/PduR/Com → RTE/SWC；发送路径反向，并通过 TxConfirmation 回传完成状态。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- 初始化项：clock/bit timing/filter/FIFO/interrupt
- Rx 与 Tx 典型调用链
- Acceptance Filter 与软件 PDU mapping
- ISR 短路径与任务解耦
- FIFO overflow 的生产者-消费者模型

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q061 MCU 初始化 CAN 通常需要配置哪些内容？](../questions/07-ecu-stack/Q061.md) | A - 高频掌握 | 2/3 |
| [Q062 一帧 CAN 从总线进入 ECU 软件大概经过哪些层？](../questions/07-ecu-stack/Q062.md) | S - 必须掌握 | 3/3 |
| [Q063 CAN 发送方向的软件调用链是什么？](../questions/07-ecu-stack/Q063.md) | A - 高频掌握 | 2/3 |
| [Q064 CAN Acceptance Filter 是什么？Mask 怎么工作？](../questions/07-ecu-stack/Q064.md) | S - 必须掌握 | 3/3 |
| [Q065 为什么 Filter 配置正确，软件仍可能收不到报文？](../questions/07-ecu-stack/Q065.md) | B - 进阶理解 | 1/3 |
| [Q066 CAN 接收应该用 Polling 还是 Interrupt？](../questions/07-ecu-stack/Q066.md) | A - 高频掌握 | 2/3 |
| [Q067 为什么 ISR 里不要直接做复杂 CAN 业务逻辑？](../questions/07-ecu-stack/Q067.md) | B - 进阶理解 | 1/3 |
| [Q068 RX FIFO Overflow 会造成什么？如何定位？](../questions/07-ecu-stack/Q068.md) | A - 高频掌握 | 2/3 |
| [Q069 为什么 CAN Trace 的时间戳是测试的核心证据？](../questions/07-ecu-stack/Q069.md) | A - 高频掌握 | 2/3 |
| [Q070 如何避免多个 ECU 重复发送同一个 CAN ID？](../questions/07-ecu-stack/Q070.md) | B - 进阶理解 | 1/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

优先做软件模拟：为 Rx FIFO→queue→consumer 写一个最小生产者/消费者模型，观察消费不足造成的 overflow；不要连接真实安全关键执行器。

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
