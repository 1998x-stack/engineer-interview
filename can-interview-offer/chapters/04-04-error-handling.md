# 第 04 章：错误检测、错误隔离与 Bus-Off

> **章节目标**：建立“检测错误—通知全网—自动重传—错误计数—隔离故障节点—恢复”的完整模型。

## 1. 章节心智模型

```text
Bit/Stuff/CRC/Form/ACK 等错误检测 → Error Flag 使当前帧无效 → 发送方按规则重传 → TEC/REC 更新 → Error Active/Passive → 严重发送错误导致 Bus-Off → ECU 软件执行恢复策略。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- CRC 只是可靠性机制之一
- ACK 不等于目标功能成功
- Error Active/Passive/Bus-Off
- TEC/REC 阈值的设计目的
- Bus-Off 协议恢复与 OEM 软件策略的区别

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q031 CAN 为什么可靠？请不要只回答“因为有 CRC”。](../questions/04-error-handling/Q031.md) | S - 必须掌握 | 3/3 |
| [Q032 什么是 Bit Stuffing？它解决什么问题？](../questions/04-error-handling/Q032.md) | B - 进阶理解 | 1/3 |
| [Q033 CAN 硬件 CRC 与应用层 Checksum/CRC8 是一回事吗？](../questions/04-error-handling/Q033.md) | A - 高频掌握 | 2/3 |
| [Q034 ACK 到底证明了什么？为什么 ACK 不等于功能成功？](../questions/04-error-handling/Q034.md) | S - 必须掌握 | 3/3 |
| [Q035 如果总线上只有一个发送节点，为什么它可能不断重发？](../questions/04-error-handling/Q035.md) | A - 高频掌握 | 2/3 |
| [Q036 Error Active、Error Passive、Bus-Off 是什么？](../questions/04-error-handling/Q036.md) | S - 必须掌握 | 3/3 |
| [Q037 TEC/REC 的关键阈值和设计目的是什么？](../questions/04-error-handling/Q037.md) | A - 高频掌握 | 2/3 |
| [Q038 Bus-Off 后如何恢复？](../questions/04-error-handling/Q038.md) | A - 高频掌握 | 2/3 |
| [Q039 Error Frame 是什么？它为什么会“破坏”当前帧？](../questions/04-error-handling/Q039.md) | B - 进阶理解 | 1/3 |
| [Q040 总线出现大量 Error Frame，应该如何系统排查？](../questions/04-error-handling/Q040.md) | S - 必须掌握 | 3/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

错误注入默认仅用于仿真或受控 HIL。练习重点是读取/分析 error counters 和状态转换，不建议在未知真实网络上制造物理错误。

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
