# 官方资料与源码索引

> 版本基准：**Memcached 1.6.45（2026-07-09）**。仓库问题答案以稳定版语义为基准；源码定位链接固定到 `1.6.45` tag，避免 `master` 后续漂移。

## S1 · Memcached 官方首页 / Downloads

项目定位、下载与版本入口。

- https://www.memcached.org/

## S2 · Basic Text Protocol

基础文本协议与命令语义。

- https://docs.memcached.org/protocols/basic/

## S3 · Meta Text Protocol

Meta 命令、anti-dogpiling、stale、CAS 等高级语义。

- https://docs.memcached.org/protocols/meta/

## S4 · Protocols Overview

当前协议状态；Binary Protocol 已 deprecated。

- https://docs.memcached.org/protocols/

## S5 · memcached.h @ 1.6.45

struct item、conn、flags、配置结构。

- https://github.com/memcached/memcached/blob/1.6.45/memcached.h

## S6 · items.c @ 1.6.45

Item alloc/link/unlink、LRU 与生命周期。

- https://github.com/memcached/memcached/blob/1.6.45/items.c

## S7 · assoc.c @ 1.6.45

本地 HashTable、find/insert/delete、rehash。

- https://github.com/memcached/memcached/blob/1.6.45/assoc.c

## S8 · slabs.c @ 1.6.45

Slab class、page、chunk、freelist 与 reassign。

- https://github.com/memcached/memcached/blob/1.6.45/slabs.c

## S9 · thread.c @ 1.6.45

Worker、item locks、LRU locks 与线程调度。

- https://github.com/memcached/memcached/blob/1.6.45/thread.c

## S10 · Memcached 1.5.0 Release Notes

Segmented LRU、crawler、automove 的重要历史节点。

- https://docs.memcached.org/releasenotes/releasenotes150/

## S11 · Server Maintenance

hit rate、eviction、slab 监控与维护。

- https://docs.memcached.org/serverguide/maintenance/

## S12 · Server Configuring

内存、连接、线程、item size、运行配置。

- https://docs.memcached.org/serverguide/configuring/

## S13 · Flash Storage / Extstore

SSD/NVMe 扩展容量模型。

- https://docs.memcached.org/features/flashstorage/

## S14 · Built-in Proxy

1.6.23+ 内置代理、pool、route 与一致性路由。

- https://docs.memcached.org/features/proxy/

## S15 · FAQ

缓存语义、持久性、复制等常见问题。

- https://docs.memcached.org/userguide/faq/

## S16 · Memcached 1.6.45 Release Notes

2026-07-09 稳定版说明。

- https://github.com/memcached/memcached/wiki/ReleaseNotes1645

## S17 · Performance and Efficiency

内存占用、回收与性能行为。

- https://docs.memcached.org/serverguide/performance/

## 使用原则

- 优先引用官方协议、官方文档和官方源码。
- 面试回答优先掌握稳定的不变量与设计意图，再追具体函数名。
- `master` 与稳定版可能有少量实现差异；本仓库源码链接尽量固定到 `1.6.45`。
