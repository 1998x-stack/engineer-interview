# CUDA Profiling Playbook

## 1. Correctness First

- 固定输入与参考实现。
- 定义容忍误差与数值精度。
- 检查 race、越界、未初始化数据。

## 2. Nsight Systems：先找端到端瓶颈

检查：CPU launch gap、Memcpy、同步、NCCL、stream overlap、短 kernel 密度。

## 3. Nsight Compute：只深挖真正的 hot kernel

按顺序看：

1. SpeedOfLight / Roofline；
2. SchedulerStats / eligible warps；
3. Memory workload / L1 L2 DRAM；
4. Occupancy / register / shared / spill；
5. Warp state / stall；
6. Source / SASS。

## 4. 建立可证伪假设

错误：`我觉得 shared memory 会快。`

正确：`当前 global load sectors/request 高且同一数据被重复读取；如果用 shared tile，DRAM bytes 应下降，kernel time 应同步下降。`

## 5. 一次只改一个主要因素

否则无法解释为什么变快，也无法知道未来换 shape/架构时应保留哪部分。
