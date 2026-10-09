# 14 天 CUDA 面试冲刺计划

## Day 1-2：执行模型与同步（Q001-Q010）
目标：不看资料画出 Grid/Block/Thread 与 SM/Warp 的映射，能解释 barrier 与 async launch。

## Day 3-4：Memory / Coalescing（Q011-Q030）
目标：手算 10 组 warp 地址的 transactions；写 AoS→SoA 和 transpose 的数据布局推导。

## Day 5：Shared / Warp（Q031-Q040）
目标：手算 bank mapping；现场写 warp reduction。

## Day 6：Occupancy / Register（Q041-Q050）
目标：对一个假想 kernel 给出 registers/shared/block size 的 residency 推导。

## Day 7-8：Coding（Q051-Q060）
目标：不看答案写 Reduction、Transpose、Tiled GEMM；Scan/Histogram 能讲完整设计。

## Day 9：Streams / Async（Q061-Q070）
目标：画 H2D/Compute/D2H 三阶段 pipeline；解释 cp.async 与 TMA。

## Day 10-11：Profiling（Q071-Q080）
目标：给任何 kernel 先做 Systems→Compute→Roofline→Stall 的诊断流程。

## Day 12：GEMM / CUTLASS（Q081-Q090）
目标：画 CTA tile / warp tile / MMA tile；解释 Stream-K 与 persistent kernel。

## Day 13：Hopper / Blackwell（Q091-Q099）
目标：明确 DSM/TMA/TMEM 的区别，并能解释 Hopper/Blackwell warp specialization 不能机械照搬。

## Day 14：综合模拟（Q100 + 随机 20 题）
规则：每题先 30 秒回答；被追问后扩展到 2 分钟；所有性能结论必须说出 profiler 证据。
