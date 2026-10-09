# 第 02 章：仲裁、优先级与实时性

> **章节目标**：从“ID 越小优先”升级到逐位仲裁、最坏响应时间和实时调度分析。

## 1. 章节心智模型

```text
多个节点同时开始发送 → 每发送一位同时采样 → recessive 发送者读到 dominant 即失去仲裁 → 获胜帧不被破坏 → 失败帧等待下一次总线空闲 → 周期与优先级共同决定 worst-case latency。
```

本章不以记忆名词为目标，而以“**能从一个问题继续追到下一层，并给出可验证证据**”作为掌握标准。

## 2. 必须掌握的核心结论

- dominant=0、recessive=1 的位级含义
- 仲裁失败不是 CAN Error
- 相同 ID/不同 Data 的风险
- 平均 bus load 与 worst-case latency 的区别
- 低优先级 starvation 与 deadline 分析

## 3. 本章 10 题

| 题目 | 优先级 | 难度 |
|---|---|---|
| [Q011 CAN 的仲裁机制是什么？](../questions/02-arbitration-realtime/Q011.md) | S - 必须掌握 | 3/3 |
| [Q012 为什么 CAN ID 越小通常优先级越高？](../questions/02-arbitration-realtime/Q012.md) | S - 必须掌握 | 3/3 |
| [Q013 为什么称 CAN 为“非破坏性仲裁”？](../questions/02-arbitration-realtime/Q013.md) | B - 进阶理解 | 1/3 |
| [Q014 仲裁失败算 CAN Error 吗？](../questions/02-arbitration-realtime/Q014.md) | S - 必须掌握 | 3/3 |
| [Q015 两个 ECU 同时发送相同 CAN ID、但 Data 不同会怎样？](../questions/02-arbitration-realtime/Q015.md) | A - 高频掌握 | 2/3 |
| [Q016 两个节点发送完全相同 ID 和完全相同 Data 会怎样？](../questions/02-arbitration-realtime/Q016.md) | B - 进阶理解 | 1/3 |
| [Q017 CAN 是实时总线吗？](../questions/02-arbitration-realtime/Q017.md) | A - 高频掌握 | 2/3 |
| [Q018 低优先级 CAN 报文会不会饿死？](../questions/02-arbitration-realtime/Q018.md) | A - 高频掌握 | 2/3 |
| [Q019 一条 CAN 报文的端到端延迟由哪些部分组成？](../questions/02-arbitration-realtime/Q019.md) | B - 进阶理解 | 1/3 |
| [Q020 高优先级突发流量会怎样影响低优先级报文？](../questions/02-arbitration-realtime/Q020.md) | B - 进阶理解 | 1/3 |

## 4. 推荐学习顺序

1. **第一遍：只读 30 秒标准回答。** 建立术语和结论；
2. **第二遍：看深入原理。** 尝试自己画 frame/bit/stack/timing 图；
3. **第三遍：做工程练习。** 用 Trace、脚本或静态位图验证；
4. **第四遍：压力追问。** 遮住正文，只看“面试官连续追问”口述；
5. **第五遍：跨章串联。** 把本章概念连接到 DBC、ECU 软件和测试证据。

## 5. 章节实验

> **安全边界**：所有报文注入、重放、错误注入默认仅用于 `vcan`、SIL、HIL 或隔离低风险台架；不面向行驶车辆或安全关键真实网络。

使用两个虚拟发送任务生成不同优先级和周期的帧，离线统计低优先级帧的周期/jitter。注意 vcan 不能复现真实硬件位级仲裁，只用于软件调度和分析框架练习。

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
