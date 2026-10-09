# 第 03 章：物理层、终端与位时序

> **章节目标**：把差分信号、传输线、bit timing 和逻辑 Trace 连接起来，知道什么时候必须看示波器。

## 1. 章节心智模型

```text
CAN Controller 产生逻辑位 → Transceiver 转为 CAN_H/CAN_L 差分 → 线缆/终端决定反射和传播 → 接收端在 Sample Point 采样 → SJW/重同步容忍时钟偏差。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- 差分传输与共模噪声
- 两端终端与约 60Ω 静态测量的边界
- TQ/TSEG/Sample Point/SJW
- bit rate 与传播延迟/总线长度
- stub/星型拓扑导致的反射风险

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q021 CAN 为什么使用差分信号？](../questions/03-physical-bit-timing/Q021.md) | S - 必须掌握 | 3/3 |
| [Q022 为什么 CAN 总线两端通常使用 120Ω 终端电阻？](../questions/03-physical-bit-timing/Q022.md) | S - 必须掌握 | 3/3 |
| [Q023 为什么断电测 CAN_H 与 CAN_L 通常约 60Ω？](../questions/03-physical-bit-timing/Q023.md) | A - 高频掌握 | 2/3 |
| [Q024 Dominant 与 Recessive 的典型电气含义是什么？](../questions/03-physical-bit-timing/Q024.md) | B - 进阶理解 | 1/3 |
| [Q025 CAN 常见波特率有哪些？为什么不能只背 500 kbit/s？](../questions/03-physical-bit-timing/Q025.md) | B - 进阶理解 | 1/3 |
| [Q026 为什么波特率越高，允许的总线长度通常越短？](../questions/03-physical-bit-timing/Q026.md) | A - 高频掌握 | 2/3 |
| [Q027 什么是 CAN Sample Point？为什么它重要？](../questions/03-physical-bit-timing/Q027.md) | S - 必须掌握 | 3/3 |
| [Q028 什么是 TQ？CAN 波特率如何从时钟参数计算？](../questions/03-physical-bit-timing/Q028.md) | A - 高频掌握 | 2/3 |
| [Q029 SJW 是什么？为什么多个 ECU 的时钟不同仍能通信？](../questions/03-physical-bit-timing/Q029.md) | B - 进阶理解 | 1/3 |
| [Q030 为什么高速 CAN 不推荐长支线和复杂星型拓扑？](../questions/03-physical-bit-timing/Q030.md) | A - 高频掌握 | 2/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

本章涉及电气层。若没有合规隔离台架，不做真实线束故障注入；用公开波形资料和计算练习 TQ/采样点即可。

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
