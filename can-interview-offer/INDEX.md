# 100 题总索引

本页用于 GitHub 快速检索。每道题均对应一个独立 Markdown；PDF/BOOK 内容由同一批题目源文件生成。

| ID | 题目 | 分类 | 优先级 | 来源类型 |
|---|---|---|---|---|
| Q001 | [什么是 CAN？为什么汽车大量使用 CAN？](questions/01-fundamentals/Q001.md) | CAN 基础与数据帧 | S - 必须掌握 | 公开面经高频原型 |
| Q002 | [CAN 与 UART、SPI、I²C 的本质区别是什么？](questions/01-fundamentals/Q002.md) | CAN 基础与数据帧 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q003 | [为什么说 CAN 是广播通信？硬件过滤器又起什么作用？](questions/01-fundamentals/Q003.md) | CAN 基础与数据帧 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q004 | [CAN 有哪些帧类型？现代汽车里哪些最重要？](questions/01-fundamentals/Q004.md) | CAN 基础与数据帧 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q005 | [请完整描述一帧 Classic CAN Data Frame。](questions/01-fundamentals/Q005.md) | CAN 基础与数据帧 | S - 必须掌握 | 公开面经高频原型 |
| Q006 | [标准帧和扩展帧有什么区别？](questions/01-fundamentals/Q006.md) | CAN 基础与数据帧 | S - 必须掌握 | 公开面经高频原型 |
| Q007 | [标准帧与扩展帧前 11 位 ID 相同时谁优先？为什么？](questions/01-fundamentals/Q007.md) | CAN 基础与数据帧 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q008 | [Data Frame 与 Remote Frame 有什么区别？](questions/01-fundamentals/Q008.md) | CAN 基础与数据帧 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q009 | [CAN ID 是 ECU 地址吗？](questions/01-fundamentals/Q009.md) | CAN 基础与数据帧 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q010 | [DLC 是什么？DLC=8 就一定是 Classic CAN 吗？](questions/01-fundamentals/Q010.md) | CAN 基础与数据帧 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q011 | [CAN 的仲裁机制是什么？](questions/02-arbitration-realtime/Q011.md) | 仲裁、优先级与实时性 | S - 必须掌握 | 公开面经高频原型 |
| Q012 | [为什么 CAN ID 越小通常优先级越高？](questions/02-arbitration-realtime/Q012.md) | 仲裁、优先级与实时性 | S - 必须掌握 | 公开面经高频原型 |
| Q013 | [为什么称 CAN 为“非破坏性仲裁”？](questions/02-arbitration-realtime/Q013.md) | 仲裁、优先级与实时性 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q014 | [仲裁失败算 CAN Error 吗？](questions/02-arbitration-realtime/Q014.md) | 仲裁、优先级与实时性 | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q015 | [两个 ECU 同时发送相同 CAN ID、但 Data 不同会怎样？](questions/02-arbitration-realtime/Q015.md) | 仲裁、优先级与实时性 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q016 | [两个节点发送完全相同 ID 和完全相同 Data 会怎样？](questions/02-arbitration-realtime/Q016.md) | 仲裁、优先级与实时性 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q017 | [CAN 是实时总线吗？](questions/02-arbitration-realtime/Q017.md) | 仲裁、优先级与实时性 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q018 | [低优先级 CAN 报文会不会饿死？](questions/02-arbitration-realtime/Q018.md) | 仲裁、优先级与实时性 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q019 | [一条 CAN 报文的端到端延迟由哪些部分组成？](questions/02-arbitration-realtime/Q019.md) | 仲裁、优先级与实时性 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q020 | [高优先级突发流量会怎样影响低优先级报文？](questions/02-arbitration-realtime/Q020.md) | 仲裁、优先级与实时性 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q021 | [CAN 为什么使用差分信号？](questions/03-physical-bit-timing/Q021.md) | 物理层、终端与位时序 | S - 必须掌握 | 公开面经高频原型 |
| Q022 | [为什么 CAN 总线两端通常使用 120Ω 终端电阻？](questions/03-physical-bit-timing/Q022.md) | 物理层、终端与位时序 | S - 必须掌握 | 公开面经高频原型 |
| Q023 | [为什么断电测 CAN_H 与 CAN_L 通常约 60Ω？](questions/03-physical-bit-timing/Q023.md) | 物理层、终端与位时序 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q024 | [Dominant 与 Recessive 的典型电气含义是什么？](questions/03-physical-bit-timing/Q024.md) | 物理层、终端与位时序 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q025 | [CAN 常见波特率有哪些？为什么不能只背 500 kbit/s？](questions/03-physical-bit-timing/Q025.md) | 物理层、终端与位时序 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q026 | [为什么波特率越高，允许的总线长度通常越短？](questions/03-physical-bit-timing/Q026.md) | 物理层、终端与位时序 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q027 | [什么是 CAN Sample Point？为什么它重要？](questions/03-physical-bit-timing/Q027.md) | 物理层、终端与位时序 | S - 必须掌握 | 公开面经高频原型 |
| Q028 | [什么是 TQ？CAN 波特率如何从时钟参数计算？](questions/03-physical-bit-timing/Q028.md) | 物理层、终端与位时序 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q029 | [SJW 是什么？为什么多个 ECU 的时钟不同仍能通信？](questions/03-physical-bit-timing/Q029.md) | 物理层、终端与位时序 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q030 | [为什么高速 CAN 不推荐长支线和复杂星型拓扑？](questions/03-physical-bit-timing/Q030.md) | 物理层、终端与位时序 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q031 | [CAN 为什么可靠？请不要只回答“因为有 CRC”。](questions/04-error-handling/Q031.md) | 错误检测、错误隔离与 Bus-Off | S - 必须掌握 | 公开面经高频原型 |
| Q032 | [什么是 Bit Stuffing？它解决什么问题？](questions/04-error-handling/Q032.md) | 错误检测、错误隔离与 Bus-Off | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q033 | [CAN 硬件 CRC 与应用层 Checksum/CRC8 是一回事吗？](questions/04-error-handling/Q033.md) | 错误检测、错误隔离与 Bus-Off | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q034 | [ACK 到底证明了什么？为什么 ACK 不等于功能成功？](questions/04-error-handling/Q034.md) | 错误检测、错误隔离与 Bus-Off | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q035 | [如果总线上只有一个发送节点，为什么它可能不断重发？](questions/04-error-handling/Q035.md) | 错误检测、错误隔离与 Bus-Off | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q036 | [Error Active、Error Passive、Bus-Off 是什么？](questions/04-error-handling/Q036.md) | 错误检测、错误隔离与 Bus-Off | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q037 | [TEC/REC 的关键阈值和设计目的是什么？](questions/04-error-handling/Q037.md) | 错误检测、错误隔离与 Bus-Off | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q038 | [Bus-Off 后如何恢复？](questions/04-error-handling/Q038.md) | 错误检测、错误隔离与 Bus-Off | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q039 | [Error Frame 是什么？它为什么会“破坏”当前帧？](questions/04-error-handling/Q039.md) | 错误检测、错误隔离与 Bus-Off | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q040 | [总线出现大量 Error Frame，应该如何系统排查？](questions/04-error-handling/Q040.md) | 错误检测、错误隔离与 Bus-Off | S - 必须掌握 | 公开面经高频原型 |
| Q041 | [Classic CAN 与 CAN FD 的核心区别是什么？](questions/05-can-fd/Q041.md) | CAN FD | S - 必须掌握 | 公开面经高频原型 |
| Q042 | [为什么需要 CAN FD？](questions/05-can-fd/Q042.md) | CAN FD | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q043 | [BRS 是什么？为什么仲裁阶段和数据阶段可以使用不同速率？](questions/05-can-fd/Q043.md) | CAN FD | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q044 | [CAN FD 的 DLC 如何映射到 64 Byte？](questions/05-can-fd/Q044.md) | CAN FD | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q045 | [FDF、BRS、ESI 分别表示什么？](questions/05-can-fd/Q045.md) | CAN FD | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q046 | [CAN FD 一定比 Classic CAN 快吗？](questions/05-can-fd/Q046.md) | CAN FD | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q047 | [Classic CAN 节点能否直接混入 CAN FD 网络？](questions/05-can-fd/Q047.md) | CAN FD | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q048 | [Arbitration Bit Rate 与 Data Bit Rate 分别是什么？](questions/05-can-fd/Q048.md) | CAN FD | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q049 | [为什么 CAN FD 对物理层设计更严格？](questions/05-can-fd/Q049.md) | CAN FD | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q050 | [从 Classic CAN 迁移到 CAN FD，需要检查哪些层？](questions/05-can-fd/Q050.md) | CAN FD | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q051 | [DBC 是什么？它在工程链路中的位置是什么？](questions/06-dbc-signals/Q051.md) | DBC 与信号编解码 | S - 必须掌握 | 公开面经高频原型 |
| Q052 | [DBC 中 BO_ 与 SG_ 分别表示什么？](questions/06-dbc-signals/Q052.md) | DBC 与信号编解码 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q053 | [Factor 与 Offset 如何完成 Raw/Physical 转换？](questions/06-dbc-signals/Q053.md) | DBC 与信号编解码 | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q054 | [给定 22℃，如何从 DBC 生成最终 CAN 数据？](questions/06-dbc-signals/Q054.md) | DBC 与信号编解码 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q055 | [Intel 与 Motorola 大小端在 DBC 中怎么理解？](questions/06-dbc-signals/Q055.md) | DBC 与信号编解码 | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q056 | [Motorola Start Bit 为什么最容易出错？](questions/06-dbc-signals/Q056.md) | DBC 与信号编解码 | S - 必须掌握 | 基于公开高频题的工程追问重构 |
| Q057 | [Signed/Unsigned 与负 Offset 有什么关系？](questions/06-dbc-signals/Q057.md) | DBC 与信号编解码 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q058 | [VAL_ 枚举的作用是什么？](questions/06-dbc-signals/Q058.md) | DBC 与信号编解码 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q059 | [Multiplexing 是什么？为什么复用信号可以“合法重叠”？](questions/06-dbc-signals/Q059.md) | DBC 与信号编解码 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q060 | [DBC 能不能告诉你 ECU 收到信号后应该做什么？](questions/06-dbc-signals/Q060.md) | DBC 与信号编解码 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q061 | [MCU 初始化 CAN 通常需要配置哪些内容？](questions/07-ecu-stack/Q061.md) | ECU 软件收发链路 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q062 | [一帧 CAN 从总线进入 ECU 软件大概经过哪些层？](questions/07-ecu-stack/Q062.md) | ECU 软件收发链路 | S - 必须掌握 | 公开面经高频原型 |
| Q063 | [CAN 发送方向的软件调用链是什么？](questions/07-ecu-stack/Q063.md) | ECU 软件收发链路 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q064 | [CAN Acceptance Filter 是什么？Mask 怎么工作？](questions/07-ecu-stack/Q064.md) | ECU 软件收发链路 | S - 必须掌握 | 公开面经高频原型 |
| Q065 | [为什么 Filter 配置正确，软件仍可能收不到报文？](questions/07-ecu-stack/Q065.md) | ECU 软件收发链路 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q066 | [CAN 接收应该用 Polling 还是 Interrupt？](questions/07-ecu-stack/Q066.md) | ECU 软件收发链路 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q067 | [为什么 ISR 里不要直接做复杂 CAN 业务逻辑？](questions/07-ecu-stack/Q067.md) | ECU 软件收发链路 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q068 | [RX FIFO Overflow 会造成什么？如何定位？](questions/07-ecu-stack/Q068.md) | ECU 软件收发链路 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q069 | [为什么 CAN Trace 的时间戳是测试的核心证据？](questions/07-ecu-stack/Q069.md) | ECU 软件收发链路 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q070 | [如何避免多个 ECU 重复发送同一个 CAN ID？](questions/07-ecu-stack/Q070.md) | ECU 软件收发链路 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q071 | [CANoe 与 CANalyzer 的定位有什么区别？](questions/08-canoe-testing/Q071.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 公开面经高频原型 |
| Q072 | [CAPL 是什么？事件驱动模型怎么理解？](questions/08-canoe-testing/Q072.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 公开面经高频原型 |
| Q073 | [什么是 Restbus Simulation？](questions/08-canoe-testing/Q073.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q074 | [为什么测试优先按 Signal 注入，而不是手写十六进制？](questions/08-canoe-testing/Q074.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q075 | [工具显示“发送成功”，为什么 ECU 完全没反应？](questions/08-canoe-testing/Q075.md) | CANoe、CAPL 与 ECU 测试 | S - 必须掌握 | 公开面经高频原型 |
| Q076 | [如何证明一个 CAN 功能测试真正通过？](questions/08-canoe-testing/Q076.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q077 | [报文 Timeout 应该怎么测试？](questions/08-canoe-testing/Q077.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q078 | [Alive Counter 应该如何设计测试？](questions/08-canoe-testing/Q078.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q079 | [应用 Checksum 错误应该怎么测试？](questions/08-canoe-testing/Q079.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q080 | [一条专业 CAN/ECU 测试用例应包含哪些字段？](questions/08-canoe-testing/Q080.md) | CANoe、CAPL 与 ECU 测试 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q081 | [python-can 的职责是什么？](questions/09-python-automation/Q081.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q082 | [cantools 与 python-can 有什么区别？为什么常一起使用？](questions/09-python-automation/Q082.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q083 | [什么是 Linux vcan？它能验证什么、不能验证什么？](questions/09-python-automation/Q083.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q084 | [SocketCAN 如何把底层 CAN 错误暴露给用户空间？](questions/09-python-automation/Q084.md) | Python、SocketCAN 与自动化 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q085 | [python-can 的 Filter 匹配逻辑是什么？](questions/09-python-automation/Q085.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q086 | [Python 如何更稳定地周期发送 CAN？](questions/09-python-automation/Q086.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q087 | [如何设计 pytest + CAN 自动化框架？](questions/09-python-automation/Q087.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q088 | [CAN Trace Replay 有什么用途和陷阱？](questions/09-python-automation/Q088.md) | Python、SocketCAN 与自动化 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q089 | [如何做 CAN 输入到车机 HMI 的全自动验证？](questions/09-python-automation/Q089.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q090 | [为什么自动化测试系统必须统一时间戳？](questions/09-python-automation/Q090.md) | Python、SocketCAN 与自动化 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q091 | [CAN 总线负载率怎么计算？](questions/10-system-debug-design/Q091.md) | 系统设计与故障定位 | S - 必须掌握 | 公开面经高频原型 |
| Q092 | [总线负载过高有哪些优化手段？](questions/10-system-debug-design/Q092.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q093 | [Gateway 在 CAN 网络中做什么？为什么它会影响故障定位？](questions/10-system-debug-design/Q093.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q094 | [周期报文、事件报文和混合报文怎么选？](questions/10-system-debug-design/Q094.md) | 系统设计与故障定位 | B - 进阶理解 | 基于公开高频题的工程追问重构 |
| Q095 | [Timeout 阈值应该如何设计？](questions/10-system-debug-design/Q095.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q096 | [CAN、ISO-TP 与 UDS 是什么关系？](questions/10-system-debug-design/Q096.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q097 | [ISO-TP 为什么存在？SF/FF/CF/FC 分别是什么？](questions/10-system-debug-design/Q097.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q098 | [“打开右前车窗”从 HMI 到执行器的完整链路如何讲？](questions/10-system-debug-design/Q098.md) | 系统设计与故障定位 | A - 高频掌握 | 基于公开高频题的工程追问重构 |
| Q099 | [发送 CAN Signal 后 ECU 没有返回，如何系统定位？](questions/10-system-debug-design/Q099.md) | 系统设计与故障定位 | S - 必须掌握 | 公开面经高频原型 |
| Q100 | [如何从零设计“CAN → 真实 ECU → 车机 UI”的自动测试系统？](questions/10-system-debug-design/Q100.md) | 系统设计与故障定位 | S - 必须掌握 | 基于公开高频题的工程追问重构 |
