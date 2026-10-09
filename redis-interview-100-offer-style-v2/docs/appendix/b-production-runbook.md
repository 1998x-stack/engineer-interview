# 附录 B · 生产故障排查 Runbook

## 延迟突然上升

- 客户端连接池 / GC / 事件循环与网络 RTT
- `SLOWLOG` 与 `INFO commandstats`
- `LATENCY LATEST` / `HISTORY` / `DOCTOR`
- fork、AOF fsync/rewrite、active expire、eviction、defrag
- Big Key、Hot Key、大集合命令、Lua/Functions
- CPU steal、Swap、THP、磁盘与网络异常

## 内存异常

- `used_memory` 与 RSS 是否明显背离
- `mem_fragmentation_ratio` 与 allocator 视角
- Big Key / 无界集合 / 无界 Stream
- client output buffer 与 replication buffer
- BGSAVE/AOF rewrite 的 COW headroom
- maxmemory policy 是否符合业务语义

## 复制异常

- connected replicas / replication lag
- primary replication offset 与 replica offset
- backlog 是否足够覆盖断线窗口
- full resync 是否反复发生
- 网络带宽、fork、RDB 传输/加载压力
- failover 后是否有 acknowledged write 丢失风险

## Cluster 异常

- `cluster_state`、slot coverage、FAIL/PFAIL
- MOVED/ASK 激增是否来自 resharding 或拓扑过期
- slot skew / Hot Slot
- CROSSSLOT 是否来自数据建模
- reshard/migration 是否碰到 Big Key
- 客户端是否正确刷新 slot map

## 缓存异常

- hit ratio 是否突降
- 数据库 QPS 是否同步飙升
- 是否出现单 Hot Key 击穿
- TTL 是否集中导致雪崩
- negative cache / Bloom 是否有效
- 更新 DB 与缓存失效链路是否存在重试/CDC

> **排障原则：** 先区分“客户端 / 网络 / 服务端 / 操作系统”，再区分“持续高负载 / 周期性尖刺 / 单 Key 热点 / 后台任务”。没有证据时不要直接重启 Redis；重启可能清掉可观测证据，并诱发全量同步或缓存雪崩。
