# 第 06 章：DBC 与信号编解码

> **章节目标**：能够手算简单信号、工具验证复杂信号，并识别数据库重叠/越界/版本错误。

## 1. 章节心智模型

```text
BO_ 定义 Message → SG_ 定义 Signal → bit layout 提取 Raw → factor/offset 转 Physical → VAL_ 提供枚举 → 需求定义 ECU 收到后如何处理。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- BO_/SG_/VAL_/属性的职责
- Physical <-> Raw 公式与量化
- Intel/Motorola 的真正区别
- Motorola sawtooth start bit
- Multiplex 合法重叠与普通重叠
- DBC 不能替代业务需求

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q051 DBC 是什么？它在工程链路中的位置是什么？](../questions/06-dbc-signals/Q051.md) | S - 必须掌握 | 3/3 |
| [Q052 DBC 中 BO_ 与 SG_ 分别表示什么？](../questions/06-dbc-signals/Q052.md) | A - 高频掌握 | 2/3 |
| [Q053 Factor 与 Offset 如何完成 Raw/Physical 转换？](../questions/06-dbc-signals/Q053.md) | S - 必须掌握 | 3/3 |
| [Q054 给定 22℃，如何从 DBC 生成最终 CAN 数据？](../questions/06-dbc-signals/Q054.md) | A - 高频掌握 | 2/3 |
| [Q055 Intel 与 Motorola 大小端在 DBC 中怎么理解？](../questions/06-dbc-signals/Q055.md) | S - 必须掌握 | 3/3 |
| [Q056 Motorola Start Bit 为什么最容易出错？](../questions/06-dbc-signals/Q056.md) | S - 必须掌握 | 3/3 |
| [Q057 Signed/Unsigned 与负 Offset 有什么关系？](../questions/06-dbc-signals/Q057.md) | A - 高频掌握 | 2/3 |
| [Q058 VAL_ 枚举的作用是什么？](../questions/06-dbc-signals/Q058.md) | B - 进阶理解 | 1/3 |
| [Q059 Multiplexing 是什么？为什么复用信号可以“合法重叠”？](../questions/06-dbc-signals/Q059.md) | B - 进阶理解 | 1/3 |
| [Q060 DBC 能不能告诉你 ECU 收到信号后应该做什么？](../questions/06-dbc-signals/Q060.md) | A - 高频掌握 | 2/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

使用仓库 `hvac_demo.dbc` 做 encode→bytes→decode round-trip，并运行 `validate_dbc_layout.py`。复杂 Motorola 位布局要画 occupancy 图。

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
