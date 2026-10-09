# Linux 线上排障速查

这是原 PDF “附录 C” 的扩展版。原则：**先做系统快照，再提出假设；每个假设必须对应可验证证据。**

| 现象 | 优先指标 | 常用入口 | 可能方向 |
|---|---|---|---|
| CPU 高 | user/system/irq/softirq、run queue | `top` / `pidstat` / `perf` | 热点函数、系统调用、软中断、锁竞争 |
| CPU 低但延迟高 | load、blocked、iowait、futex | `vmstat` / `pidstat` / `strace` | I/O、锁、外部依赖、调度延迟 |
| 内存持续增长 | RSS/PSS、anon/file、fault | `/proc/<pid>/smaps` / `pmap` | 泄漏、cache、allocator fragmentation |
| major fault 暴涨 | pgmajfault、disk latency | `vmstat` / `perf` / `iostat` | 工作集超内存、文件随机访问 |
| 磁盘慢 | await、queue depth、util | `iostat` / block tracing | 设备拥塞、`fsync`、随机 I/O |
| 网络慢 | retransmit/drop/socket queue | `ss` / `sar` / `ethtool` | 拥塞、丢包、应用读写不及时 |
| FD 增长 | `/proc/<pid>/fd` count | `lsof` / `strace` / eBPF | socket/file leak、CLOEXEC |
| 容器 OOM | memory.current/events/limit | cgroupfs / container metrics | cgroup limit、working set、cache |

## 推荐排障顺序

```text
1. 影响范围：单实例 / 单机 / 单 AZ / 全局？
2. 资源概况：CPU / run queue / memory / pressure / disk / network
3. 进程级：线程状态、context switch、fault、fd、socket
4. 系统调用：哪里在 block？futex / read / fsync / connect？
5. Profile：CPU on-CPU 与 off-CPU 分开看
6. 验证根因：构造可复现条件或对照实验
```

## 一分钟快照

```bash
uptime
vmstat 1 5
pidstat -durw 1 5
iostat -xz 1 5
ss -s
cat /proc/pressure/cpu 2>/dev/null
cat /proc/pressure/memory 2>/dev/null
cat /proc/pressure/io 2>/dev/null
```

> 工具输出必须结合具体内核、容器和业务环境解释；单个指标不能直接等同于根因。
