# 计算机组成原理面试 100 题

> 题目 → 核心结论 → 原理 → 微架构/系统边界 → 工程连接 → 追问 → 自测。

本 GitHub 版完整覆盖原 PDF 的 100 题与附录，并对每题加入更详细的专业扩展。为保证可追溯性，每个题目文件都标注原 PDF 页码；新增内容与 PDF 来源内容明确分区。

## 快速入口

- [30 道必须脱稿的核心题](appendices/core-30.md)
- [八条连续追问链](appendices/interview-chains.md)
- [核心公式速查](appendices/formulas.md)
- [典型错误表达修正](appendices/pitfalls.md)
- [参考资料](appendices/references.md)
- [7 天冲刺](study-plans/7-day.md) / [30 天系统学习](study-plans/30-day.md)

## 100 题总表

| 题号 | 题目 | 模块 | 难度 | 频率 |
|---|---|---|---|---|
| [Q001](./01-architecture-data/q001-question.md) | 冯·诺依曼体系结构是什么？它的瓶颈在哪里？ | 体系结构与数据表示 | ★★★★☆ | 高频 |
| [Q002](./01-architecture-data/q002-question.md) | 冯·诺依曼结构与哈佛结构有什么区别？ | 体系结构与数据表示 | ★★★★☆ | 高频 |
| [Q003](./01-architecture-data/q003-32-64.md) | 32 位与 64 位处理器的本质区别是什么？ | 体系结构与数据表示 | ★★★★☆ | 高频 |
| [Q004](./01-architecture-data/q004-question.md) | 为什么计算机主流使用二进制？ | 体系结构与数据表示 | ★★★☆☆ | 常见 |
| [Q005](./01-architecture-data/q005-question.md) | 什么是大端与小端？如何判断机器端序？ | 体系结构与数据表示 | ★★★★★ | 必考 |
| [Q006](./01-architecture-data/q006-question.md) | 原码、反码、补码是什么？为什么现代机器使用补码？ | 体系结构与数据表示 | ★★★★★ | 必考 |
| [Q007](./01-architecture-data/q007-int-min.md) | 为什么 INT_MIN 的绝对值无法用同宽有符号整数表示？ | 体系结构与数据表示 | ★★★★☆ | 高频 |
| [Q008](./01-architecture-data/q008-ieee-754.md) | IEEE 754 单精度和双精度浮点数如何编码？ | 体系结构与数据表示 | ★★★★★ | 必考 |
| [Q009](./01-architecture-data/q009-0-1-0-2-0.md) | 为什么 0.1 + 0.2 通常不精确等于 0.3？ | 体系结构与数据表示 | ★★★★★ | 必考 |
| [Q010](./01-architecture-data/q010-padding.md) | 什么是内存对齐？为什么结构体会出现 padding？ | 体系结构与数据表示 | ★★★★★ | 必考 |
| [Q011](./02-arithmetic-alu/q011-cpu.md) | CPU 如何只用加法器实现减法？ | 运算器与计算机算术 | ★★★★☆ | 高频 |
| [Q012](./02-arithmetic-alu/q012-carry-overflow.md) | Carry 与 Overflow 有什么区别？ | 运算器与计算机算术 | ★★★★★ | 必考 |
| [Q013](./02-arithmetic-alu/q013-alu.md) | ALU 通常包含哪些功能？ | 运算器与计算机算术 | ★★★☆☆ | 常见 |
| [Q014](./02-arithmetic-alu/q014-cpu.md) | CPU 如何完成有符号与无符号比较？ | 运算器与计算机算术 | ★★★★☆ | 高频 |
| [Q015](./02-arithmetic-alu/q015-2.md) | 左移为什么常被视为乘 2？有哪些边界？ | 运算器与计算机算术 | ★★★★☆ | 高频 |
| [Q016](./02-arithmetic-alu/q016-question.md) | 逻辑右移与算术右移有什么区别？ | 运算器与计算机算术 | ★★★★☆ | 高频 |
| [Q017](./02-arithmetic-alu/q017-question.md) | 硬件乘法器为何比加法器复杂？ | 运算器与计算机算术 | ★★★★☆ | 进阶 |
| [Q018](./02-arithmetic-alu/q018-question.md) | 为什么整数除法往往比乘法慢？ | 运算器与计算机算术 | ★★★★☆ | 进阶 |
| [Q019](./02-arithmetic-alu/q019-question.md) | 浮点加法器执行一次加法需要哪些步骤？ | 运算器与计算机算术 | ★★★★★ | 高频 |
| [Q020](./02-arithmetic-alu/q020-nan-infinity-subnormal.md) | NaN、Infinity 和 Subnormal 分别为什么存在？ | 运算器与计算机算术 | ★★★★☆ | 高频 |
| [Q021](./03-isa-abi/q021-isa-isa.md) | 什么是 ISA？ISA 与微架构有什么区别？ | ISA、指令与 ABI | ★★★★★ | 必考 |
| [Q022](./03-isa-abi/q022-risc-cisc.md) | RISC 与 CISC 的核心差别是什么？ | ISA、指令与 ABI | ★★★★★ | 必考 |
| [Q023](./03-isa-abi/q023-load-store-architecture.md) | 什么是 Load/Store Architecture？ | ISA、指令与 ABI | ★★★★☆ | 高频 |
| [Q024](./03-isa-abi/q024-base-offset.md) | 常见寻址方式有哪些？Base+Offset 为什么重要？ | ISA、指令与 ABI | ★★★★☆ | 高频 |
| [Q025](./03-isa-abi/q025-question.md) | 固定长度和可变长度指令编码如何权衡？ | ISA、指令与 ABI | ★★★★☆ | 进阶 |
| [Q026](./03-isa-abi/q026-pc.md) | PC/程序计数器在流水线中扮演什么角色？ | ISA、指令与 ABI | ★★★★☆ | 高频 |
| [Q027](./03-isa-abi/q027-question.md) | 函数调用在机器层面发生了什么？ | ISA、指令与 ABI | ★★★★★ | 必考 |
| [Q028](./03-isa-abi/q028-caller-saved-callee-saved.md) | Caller-saved 与 Callee-saved 寄存器怎么理解？ | ISA、指令与 ABI | ★★★★☆ | 高频 |
| [Q029](./03-isa-abi/q029-cpu.md) | 什么是 CPU 特权级？为何需要硬件隔离？ | ISA、指令与 ABI | ★★★★★ | 必考 |
| [Q030](./03-isa-abi/q030-isa-abi.md) | ISA 与 ABI 有什么区别？ | ISA、指令与 ABI | ★★★★★ | 高频 |
| [Q031](./04-datapath-control/q031-question.md) | 一条指令从取指到完成经历哪些阶段？ | CPU 数据通路与控制 | ★★★★★ | 必考 |
| [Q032](./04-datapath-control/q032-cpu.md) | CPU 中常见寄存器有哪些？ | CPU 数据通路与控制 | ★★★☆☆ | 常见 |
| [Q033](./04-datapath-control/q033-question.md) | 控制器如何驱动数据通路执行指令？ | CPU 数据通路与控制 | ★★★★☆ | 高频 |
| [Q034](./04-datapath-control/q034-question.md) | 硬布线控制与微程序控制有什么区别？ | CPU 数据通路与控制 | ★★★★☆ | 进阶 |
| [Q035](./04-datapath-control/q035-cpu.md) | 单周期 CPU 为什么主频难以提高？ | CPU 数据通路与控制 | ★★★★☆ | 高频 |
| [Q036](./04-datapath-control/q036-cpu.md) | 多周期 CPU 为何比单周期设计更灵活？ | CPU 数据通路与控制 | ★★★★☆ | 高频 |
| [Q037](./04-datapath-control/q037-latency-throughput.md) | 流水线究竟提高的是 Latency 还是 Throughput？ | CPU 数据通路与控制 | ★★★★★ | 必考 |
| [Q038](./04-datapath-control/q038-cpu.md) | CPU 主频越高一定越快吗？ | CPU 数据通路与控制 | ★★★★★ | 必考 |
| [Q039](./04-datapath-control/q039-cpi-ipc.md) | CPI 与 IPC 如何理解？ | CPU 数据通路与控制 | ★★★★★ | 高频 |
| [Q040](./04-datapath-control/q040-latency-throughput.md) | Latency 与 Throughput 在微架构性能分析中如何区分？ | CPU 数据通路与控制 | ★★★★★ | 高频 |
| [Q041](./05-pipeline-ooo/q041-question.md) | 流水线冒险有哪些类型？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q042](./05-pipeline-ooo/q042-raw-war-waw.md) | RAW、WAR、WAW 分别是什么？哪些是真依赖？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q043](./05-pipeline-ooo/q043-forwarding-bypassing.md) | Forwarding/Bypassing 如何减少流水线停顿？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q044](./05-pipeline-ooo/q044-load-use-hazard.md) | Load-Use Hazard 为何特别难处理？ | 流水线、预测与乱序执行 | ★★★★★ | 高频 |
| [Q045](./05-pipeline-ooo/q045-control-hazard.md) | 分支为什么会造成 Control Hazard？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q046](./05-pipeline-ooo/q046-question.md) | 分支预测器通常预测哪些东西？ | 流水线、预测与乱序执行 | ★★★★★ | 高频 |
| [Q047](./05-pipeline-ooo/q047-question.md) | 分支预测失败为何代价高？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q048](./05-pipeline-ooo/q048-out-of-order-execution.md) | 什么是乱序执行（Out-of-Order Execution）？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q049](./05-pipeline-ooo/q049-register-renaming-war-waw.md) | Register Renaming 为何能消除 WAR/WAW？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q050](./05-pipeline-ooo/q050-rob-reorder-buffer.md) | ROB（Reorder Buffer）的核心作用是什么？ | 流水线、预测与乱序执行 | ★★★★★ | 必考 |
| [Q051](./06-cache-memory/q051-cache.md) | 为什么需要 Cache？什么是局部性？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q052](./06-cache-memory/q052-l1-l2-l3.md) | L1/L2/L3 为何容量越大通常越慢？ | Cache 与存储层次 | ★★★★★ | 高频 |
| [Q053](./06-cache-memory/q053-cache-line-64b.md) | Cache Line 是什么？为什么常见为 64B？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q054](./06-cache-memory/q054-cache-tag-index-offset.md) | Cache 地址中的 Tag/Index/Offset 如何划分？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q055](./06-cache-memory/q055-question.md) | 直接映射、全相联和组相联如何权衡？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q056](./06-cache-memory/q056-cache-miss.md) | Cache Miss 有哪些经典类型？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q057](./06-cache-memory/q057-cache-lru.md) | 为什么真实 Cache 很少做精确 LRU？ | Cache 与存储层次 | ★★★★☆ | 进阶 |
| [Q058](./06-cache-memory/q058-write-through-write-back.md) | Write-Through 与 Write-Back 怎么选？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q059](./06-cache-memory/q059-write-allocate-no-write-allocate.md) | Write-Allocate 与 No-Write-Allocate 有什么区别？ | Cache 与存储层次 | ★★★★☆ | 高频 |
| [Q060](./06-cache-memory/q060-amat-miss-rate.md) | AMAT 如何计算？如何判断优化一个 miss rate 值不值得？ | Cache 与存储层次 | ★★★★★ | 必考 |
| [Q061](./07-mmu-tlb/q061-question.md) | 为什么现代系统需要虚拟地址？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q062](./07-mmu-tlb/q062-mmu.md) | MMU 的核心工作是什么？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q063](./07-mmu-tlb/q063-tlb.md) | TLB 是什么？为什么它对性能如此关键？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q064](./07-mmu-tlb/q064-tlb-miss-page-fault.md) | TLB Miss 与 Page Fault 有何本质区别？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q065](./07-mmu-tlb/q065-question.md) | 为什么页表通常设计成多级？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q066](./07-mmu-tlb/q066-cpu-load.md) | 一次 CPU Load 从虚拟地址到数据返回经历什么？ | MMU、页表与 TLB | ★★★★★ | 必考 |
| [Q067](./07-mmu-tlb/q067-cache-mmu.md) | Cache 和 MMU 到底谁先？ | MMU、页表与 TLB | ★★★★★ | 高频 |
| [Q068](./07-mmu-tlb/q068-vivt-vipt-pipt-cache.md) | VIVT、VIPT、PIPT Cache 如何比较？ | MMU、页表与 TLB | ★★★★★ | 进阶 |
| [Q069](./07-mmu-tlb/q069-huge-page.md) | Huge Page 为何能改善性能？有什么代价？ | MMU、页表与 TLB | ★★★★★ | 高频 |
| [Q070](./07-mmu-tlb/q070-tlb-invalidation-shootdown.md) | 为什么修改页表后要做 TLB invalidation/shootdown？ | MMU、页表与 TLB | ★★★★★ | 进阶 |
| [Q071](./08-coherence-memory-model/q071-cpu-cache-coherence.md) | 为什么多核 CPU 需要 Cache Coherence？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q072](./08-coherence-memory-model/q072-mesi.md) | MESI 四个状态分别表示什么？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q073](./08-coherence-memory-model/q073-cache-coherence-memory-consistency.md) | Cache Coherence 与 Memory Consistency 有什么区别？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q074](./08-coherence-memory-model/q074-mesi-memory-barrier-fence.md) | 为什么有 MESI 还需要 Memory Barrier/Fence？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q075](./08-coherence-memory-model/q075-x86-arm-risc-v.md) | x86、Arm、RISC-V 内存模型为何不同？ | 多核一致性、原子与内存模型 | ★★★★★ | 进阶 |
| [Q076](./08-coherence-memory-model/q076-arm-dmb-dsb-isb.md) | Arm 中的 DMB、DSB、ISB 怎么区分？ | 多核一致性、原子与内存模型 | ★★★★★ | 进阶 |
| [Q077](./08-coherence-memory-model/q077-false-sharing.md) | 什么是 False Sharing？为什么逻辑上不同变量也会互相拖慢？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q078](./08-coherence-memory-model/q078-false-sharing.md) | 如何系统解决 False Sharing？ | 多核一致性、原子与内存模型 | ★★★★☆ | 高频 |
| [Q079](./08-coherence-memory-model/q079-cpu.md) | CPU 原子操作如何实现？ | 多核一致性、原子与内存模型 | ★★★★★ | 必考 |
| [Q080](./08-coherence-memory-model/q080-cas-aba.md) | CAS 的 ABA 问题是什么？如何缓解？ | 多核一致性、原子与内存模型 | ★★★★★ | 进阶 |
| [Q081](./09-io-dma-interconnect/q081-polling.md) | 中断是什么？为什么比纯 Polling 高效？ | I/O、中断、DMA 与互连 | ★★★★★ | 必考 |
| [Q082](./09-io-dma-interconnect/q082-interrupt-exception-trap.md) | Interrupt、Exception、Trap 如何区分？ | I/O、中断、DMA 与互连 | ★★★★★ | 高频 |
| [Q083](./09-io-dma-interconnect/q083-question.md) | 中断向量表/异常向量的作用是什么？ | I/O、中断、DMA 与互连 | ★★★★☆ | 高频 |
| [Q084](./09-io-dma-interconnect/q084-polling-interrupt.md) | Polling 与 Interrupt 如何选择？ | I/O、中断、DMA 与互连 | ★★★★★ | 高频 |
| [Q085](./09-io-dma-interconnect/q085-dma.md) | DMA 是什么？完整工作流程是什么？ | I/O、中断、DMA 与互连 | ★★★★★ | 必考 |
| [Q086](./09-io-dma-interconnect/q086-dma-cpu-cache.md) | DMA 与 CPU Cache 为何会产生一致性问题？ | I/O、中断、DMA 与互连 | ★★★★★ | 必考 |
| [Q087](./09-io-dma-interconnect/q087-mmio.md) | MMIO 是什么？为什么设备寄存器不能当普通内存访问？ | I/O、中断、DMA 与互连 | ★★★★★ | 必考 |
| [Q088](./09-io-dma-interconnect/q088-soc.md) | 地址线、数据线、控制线的教材模型在现代 SoC 中如何演化？ | I/O、中断、DMA 与互连 | ★★★☆☆ | 常见 |
| [Q089](./09-io-dma-interconnect/q089-axi-ahb.md) | AXI 与 AHB 的主要区别是什么？ | I/O、中断、DMA 与互连 | ★★★★★ | 芯片岗 |
| [Q090](./09-io-dma-interconnect/q090-pcie-packet.md) | PCIe 为什么采用点对点串行和 packet 事务模型？ | I/O、中断、DMA 与互连 | ★★★★★ | 高频 |
| [Q091](./10-storage-boot-performance/q091-sram-dram-cache.md) | SRAM 与 DRAM 为什么一个做 Cache、一个做主存？ | 存储、启动与综合性能 | ★★★★★ | 必考 |
| [Q092](./10-storage-boot-performance/q092-dram-refresh.md) | DRAM 为什么需要 Refresh？ | 存储、启动与综合性能 | ★★★★☆ | 高频 |
| [Q093](./10-storage-boot-performance/q093-hdd-ssd.md) | HDD 与 SSD 的性能差异来自哪里？ | 存储、启动与综合性能 | ★★★★☆ | 高频 |
| [Q094](./10-storage-boot-performance/q094-ssd-write-amplification.md) | SSD 为什么会产生 Write Amplification？ | 存储、启动与综合性能 | ★★★★★ | 进阶 |
| [Q095](./10-storage-boot-performance/q095-cpu-gpu.md) | CPU 与 GPU 的架构目标有何根本不同？ | 存储、启动与综合性能 | ★★★★★ | 必考 |
| [Q096](./10-storage-boot-performance/q096-simd-simt.md) | SIMD 与 SIMT 有什么区别？ | 存储、启动与综合性能 | ★★★★★ | 高频 |
| [Q097](./10-storage-boot-performance/q097-reset-kernel.md) | 从上电 Reset 到操作系统 Kernel 开始执行发生了什么？ | 存储、启动与综合性能 | ★★★★★ | 芯片岗 |
| [Q098](./10-storage-boot-performance/q098-hardware-prefetch.md) | Hardware Prefetch 如何工作？为什么有时反而变慢？ | 存储、启动与综合性能 | ★★★★★ | 高频 |
| [Q099](./10-storage-boot-performance/q099-question.md) | 为什么顺序遍历数组比随机访问快很多？ | 存储、启动与综合性能 | ★★★★★ | 必考 |
| [Q100](./10-storage-boot-performance/q100-cpu.md) | 给你一个‘CPU 很慢’的程序，如何从组成原理角度系统定位？ | 存储、启动与综合性能 | ★★★★★ | 终局 |
