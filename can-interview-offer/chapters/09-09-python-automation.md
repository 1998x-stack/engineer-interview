# 第 09 章：Python、SocketCAN 与自动化

> **章节目标**：设计可维护的 CAN 自动化分层，而不是把所有逻辑写进一个 send/recv 脚本。

## 1. 章节心智模型

```text
pytest testcase → vehicle signal/service API → cantools codec → python-can transport → SocketCAN/adapter → DUT → observer → assertion → artifact collection。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- python-can 与 cantools 的职责分离
- vcan 能验证什么/不能验证什么
- SocketCAN error frame/BCM
- 周期发送的实际 jitter 验证
- fixture、日志、配置版本化与失败证据

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q081 python-can 的职责是什么？](../questions/09-python-automation/Q081.md) | A - 高频掌握 | 2/3 |
| [Q082 cantools 与 python-can 有什么区别？为什么常一起使用？](../questions/09-python-automation/Q082.md) | A - 高频掌握 | 2/3 |
| [Q083 什么是 Linux vcan？它能验证什么、不能验证什么？](../questions/09-python-automation/Q083.md) | A - 高频掌握 | 2/3 |
| [Q084 SocketCAN 如何把底层 CAN 错误暴露给用户空间？](../questions/09-python-automation/Q084.md) | B - 进阶理解 | 1/3 |
| [Q085 python-can 的 Filter 匹配逻辑是什么？](../questions/09-python-automation/Q085.md) | A - 高频掌握 | 2/3 |
| [Q086 Python 如何更稳定地周期发送 CAN？](../questions/09-python-automation/Q086.md) | A - 高频掌握 | 2/3 |
| [Q087 如何设计 pytest + CAN 自动化框架？](../questions/09-python-automation/Q087.md) | A - 高频掌握 | 2/3 |
| [Q088 CAN Trace Replay 有什么用途和陷阱？](../questions/09-python-automation/Q088.md) | B - 进阶理解 | 1/3 |
| [Q089 如何做 CAN 输入到车机 HMI 的全自动验证？](../questions/09-python-automation/Q089.md) | A - 高频掌握 | 2/3 |
| [Q090 为什么自动化测试系统必须统一时间戳？](../questions/09-python-automation/Q090.md) | A - 高频掌握 | 2/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

在 `vcan0` 完成 DBC 编码、周期发送、接收解码和 pytest 断言；把 Trace、DBC hash 和 verdict 自动保存。

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
