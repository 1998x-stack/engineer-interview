# 第 01 章：CAN 基础与数据帧

> **章节目标**：建立正确的 CAN 消息总线模型，能够从一条 raw frame 解释到字段语义，并明确协议层与业务层边界。

## 1. 章节心智模型

```text
节点共享同一总线 → SOF 建立帧边界 → 仲裁字段决定优先级/格式 → Data Field 承载 payload → CRC/ACK/EOF 完成帧级可靠传输 → Controller Filter 选择是否交给软件。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- CAN 是消息广播总线，不是传统目的地址网络
- 11-bit Standard 与 29-bit Extended 的差异
- Data Frame 字段与每个字段解决的问题
- CAN ID、DLC、ACK 的结论边界
- Classic CAN 与 CAN FD 的格式判断不能只看 payload 长度

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q001 什么是 CAN？为什么汽车大量使用 CAN？](../questions/01-fundamentals/Q001.md) | S - 必须掌握 | 3/3 |
| [Q002 CAN 与 UART、SPI、I²C 的本质区别是什么？](../questions/01-fundamentals/Q002.md) | A - 高频掌握 | 2/3 |
| [Q003 为什么说 CAN 是广播通信？硬件过滤器又起什么作用？](../questions/01-fundamentals/Q003.md) | A - 高频掌握 | 2/3 |
| [Q004 CAN 有哪些帧类型？现代汽车里哪些最重要？](../questions/01-fundamentals/Q004.md) | B - 进阶理解 | 1/3 |
| [Q005 请完整描述一帧 Classic CAN Data Frame。](../questions/01-fundamentals/Q005.md) | S - 必须掌握 | 3/3 |
| [Q006 标准帧和扩展帧有什么区别？](../questions/01-fundamentals/Q006.md) | S - 必须掌握 | 3/3 |
| [Q007 标准帧与扩展帧前 11 位 ID 相同时谁优先？为什么？](../questions/01-fundamentals/Q007.md) | A - 高频掌握 | 2/3 |
| [Q008 Data Frame 与 Remote Frame 有什么区别？](../questions/01-fundamentals/Q008.md) | B - 进阶理解 | 1/3 |
| [Q009 CAN ID 是 ECU 地址吗？](../questions/01-fundamentals/Q009.md) | B - 进阶理解 | 1/3 |
| [Q010 DLC 是什么？DLC=8 就一定是 Classic CAN 吗？](../questions/01-fundamentals/Q010.md) | A - 高频掌握 | 2/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

在 `vcan0` 上构造 Standard/Extended Data Frame，并用日志记录 ID、DLC、payload；然后写一段说明，指出仅凭这些信息哪些业务结论仍然不能得到。

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
