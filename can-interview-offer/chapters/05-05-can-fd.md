# 第 05 章：CAN FD

> **章节目标**：理解 FD 的价值、双 bit timing、DLC 映射、兼容性和迁移风险。

## 1. 章节心智模型

```text
仲裁阶段使用 nominal timing → FDF 表明 FD 格式 → BRS 可切到 data timing → payload 最多 64 Byte → 更强 CRC 机制 → 帧末切回 nominal timing。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- FDF/BRS/ESI
- DLC 9~15 的离散映射
- Nominal/Arbitration 与 Data Bit Rate
- Classic-only 节点兼容问题
- FD 高速数据相位的物理层 margin

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q041 Classic CAN 与 CAN FD 的核心区别是什么？](../questions/05-can-fd/Q041.md) | S - 必须掌握 | 3/3 |
| [Q042 为什么需要 CAN FD？](../questions/05-can-fd/Q042.md) | A - 高频掌握 | 2/3 |
| [Q043 BRS 是什么？为什么仲裁阶段和数据阶段可以使用不同速率？](../questions/05-can-fd/Q043.md) | S - 必须掌握 | 3/3 |
| [Q044 CAN FD 的 DLC 如何映射到 64 Byte？](../questions/05-can-fd/Q044.md) | A - 高频掌握 | 2/3 |
| [Q045 FDF、BRS、ESI 分别表示什么？](../questions/05-can-fd/Q045.md) | B - 进阶理解 | 1/3 |
| [Q046 CAN FD 一定比 Classic CAN 快吗？](../questions/05-can-fd/Q046.md) | B - 进阶理解 | 1/3 |
| [Q047 Classic CAN 节点能否直接混入 CAN FD 网络？](../questions/05-can-fd/Q047.md) | B - 进阶理解 | 1/3 |
| [Q048 Arbitration Bit Rate 与 Data Bit Rate 分别是什么？](../questions/05-can-fd/Q048.md) | A - 高频掌握 | 2/3 |
| [Q049 为什么 CAN FD 对物理层设计更严格？](../questions/05-can-fd/Q049.md) | B - 进阶理解 | 1/3 |
| [Q050 从 Classic CAN 迁移到 CAN FD，需要检查哪些层？](../questions/05-can-fd/Q050.md) | A - 高频掌握 | 2/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

用支持 CAN FD 的离线工具或日志练习解析 FDF/BRS/ESI 和 DLC 映射；没有 FD 硬件时不对真实网络做兼容性实验。

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
