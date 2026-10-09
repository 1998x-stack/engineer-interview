# 典型错误表达 → 更专业说法

| 不够准确 | 更专业 |
|---|---|
| “64 位 CPU 一次处理 64 位，所以更快。” | 64 位主要改变 ISA/寄存器/地址与 ABI 能力；性能仍由微架构、工作负载和内存系统共同决定。 |
| “Cache 在 MMU 后面。” | 架构语义依赖物理地址；L1 可通过 VIPT 与 TLB 并行隐藏 translation latency。 |
| “有 MESI 就不会乱序。” | MESI 解决 coherence；memory ordering 仍由 ISA 内存模型和 fence/atomic 约束。 |
| “DMA 不需要 CPU。” | CPU 配置 descriptor/buffer，DMA engine 负责数据搬运，控制路径仍需要 CPU/驱动。 |
| “流水线让一条指令快 5 倍。” | 流水线主要提高 steady-state throughput，单指令 latency 未必降低。 |
| “TLB miss 就是缺页。” | TLB miss 是 translation-cache miss；page fault 是页表/权限语义要求 OS 介入。 |
