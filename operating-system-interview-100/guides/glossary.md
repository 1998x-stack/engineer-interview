# 操作系统面试术语表

| 术语 | 面试语境中的一句话定义 | 关联题 |
|---|---|---|
| Process | 资源/隔离边界上的运行实例 | Q11-Q18 |
| Thread | 共享进程资源的执行单元 | Q14-Q15 |
| Context Switch | 从一个可执行上下文切换到另一个，涉及寄存器/调度状态并可能破坏 locality | Q23-Q31 |
| Syscall | 用户态通过受控入口请求内核服务 | Q02-Q03 |
| Race Condition | 结果依赖未受约束的并发交错 | Q33 |
| Mutex | 带 ownership 语义的互斥同步原语 | Q35-Q37 |
| Semaphore | 计数/通知型同步原语 | Q35-Q36, Q42 |
| Futex | Linux 面向用户态同步库的 wait/wake 原语，常用于“无竞争用户态快路径 + 竞争内核慢路径” | Q47 |
| Deadlock | 一组执行实体形成无法自行打破的循环等待 | Q48-Q52 |
| TLB | 缓存虚拟页到物理页框地址翻译的硬件结构 | Q57-Q60 |
| Page Fault | CPU 因页表状态/权限而进入内核处理的同步异常 | Q62-Q68 |
| COW | 写时复制：先共享，再在写入时通过 fault 延迟复制 | Q17, Q68 |
| VFS | Linux 统一文件系统接口与对象模型 | Q73-Q75 |
| inode | 文件系统对象的元数据/数据映射身份，不等同于文件名 | Q73-Q76 |
| Page Cache | Linux 对 file-backed pages 的统一缓存核心之一 | Q69, Q77-Q79 |
| `fsync` | 请求把文件相关脏数据/元数据推进到持久化边界；具体保证仍取决于文件系统/设备语义 | Q79-Q82 |
| epoll | Linux 高并发 fd readiness 通知接口 | Q87-Q89 |
| io_uring | 基于 submission/completion ring 的通用异步操作接口 | Q90 |
| Namespace | 隔离进程看到的系统资源视图 | Q93-Q95 |
| cgroup | 进程层级的资源统计、限制与控制机制 | Q93-Q97 |
| PSI | Pressure Stall Information，反映 CPU/memory/I/O 资源压力造成的 stall | Q98-Q100 |

> 术语表用于快速复习，不能替代单题中的边界与机制解释。
