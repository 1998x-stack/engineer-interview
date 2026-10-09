# Python 并发模型决策表

| 场景 | 首选候选 | 优势 | 主要成本 | 版本备注 |
|---|---|---|---|---|
| 大量网络 I/O | asyncio | 单线程高并发、结构化任务管理 | 要求全链路非阻塞 | TaskGroup 3.11+ |
| 阻塞 I/O SDK | ThreadPool / to_thread | 兼容旧库 | 线程数与共享状态 | 默认 CPython 的 CPU Python 代码仍受 GIL 影响 |
| CPU-heavy pure Python | ProcessPool | 成熟多核方案 | pickle / IPC / 内存 | start method 随平台和版本变化 |
| CPU-heavy, free-threaded ready | Threads | 共享内存 + 真并行潜力 | 线程安全 / 扩展兼容 | 3.13+ 可选，3.14 仍需显式选择 |
| 隔离解释器并行 | InterpreterPoolExecutor | 各解释器独立 GIL、多核 | 数据隔离 / 序列化 | Python 3.14 新增 |
| 重计算服务化 | 独立 worker / service | 容量隔离、可水平扩展 | 系统复杂度 | 高并发 API 常用 |

## 决策顺序

1. 先判断 CPU-bound / I/O-bound。
2. 再判断是否需要共享大对象。
3. 评估 pickle/IPC 与线程同步成本。
4. 确认 C 扩展、运行时和部署环境是否支持 free-threading。
5. 最后才决定线程、进程、多解释器或服务化。
