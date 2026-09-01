# Memcached 1.6.45 源码符号地图

> 目标：把 100 道题从“概念记忆”映射到固定版本源码。所有链接/命令以 **Memcached 1.6.45** 为基线；升级版本时优先重新 `git grep`，不要依赖行号永久稳定。

## 推荐源码阅读顺序

1. `memcached.h`：先理解 `struct item`、flags、connection/thread 结构。
2. `assoc.c`：只解决 `key → item*`。
3. `items.c`：Item alloc/link/unlink、LRU、refcount 生命周期。
4. `slabs.c` / `slabs_mover.c`：chunk/page/freelist 与 reassign。
5. `proto_text.c` / `proto_parser.c`：命令如何进入核心对象层。
6. `thread.c` / `memcached.c`：item locks、worker、connection 状态机。
7. `crawler.c`：后台 expiration/LRU 扫描。
8. `storage.c` / `extstore.c`：Extstore。
9. `proto_proxy.c` / `proxy_config.c`：Built-in Proxy。

## 核心符号表

| 主题 | 关键符号 | 先回答的问题 |
|---|---|---|
| Item 布局 | `struct _stritem`, `ITEM_key`, `ITEM_data`, `ITEM_ntotal` | key/value/CAS 在 chunk 中怎样布局？ |
| Item 分配 | `item_alloc`, `do_item_alloc`, `item_make_header` | 总尺寸何时计算？ |
| Publication | `do_item_link`, `assoc_insert`, `item_link_q` | 什么时候对 GET 可见？ |
| Unlink/Free | `do_item_unlink`, `do_item_remove`, `item_free` | 逻辑删除和物理释放如何分离？ |
| 引用 | `refcount_incr`, `refcount_decr` | 并发 reader 如何避免 UAF？ |
| Hash | `assoc_find`, `assoc_insert`, `assoc_delete` | key 如何变为 item 指针？ |
| Hash 扩容 | `assoc_start_expand`, `assoc_maintenance_thread` | 如何避免大规模停顿？ |
| Slab class | `slabs_clsid`, `slabclass_t` | item 进入哪个尺寸池？ |
| Chunk 分配 | `slabs_alloc`, `do_slabs_alloc`, `slabs_free` | freelist 如何工作？ |
| Reassign | `slabs_reassign`, `slabs_pick_any_for_reassign` | page 如何跨 class 调整？ |
| LRU | `HOT_LRU`, `WARM_LRU`, `COLD_LRU`, `lru_pull_tail` | 为什么不是 strict LRU？ |
| TTL | `exptime`, `do_item_get` | 过期为何不等于立即 free？ |
| Crawler | `lru_crawler_thread` | 后台如何主动回收 expired item？ |
| SET | `process_update_command`, `complete_nread_ascii`, `store_item`, `do_store_item` | construct→publish 的边界在哪？ |
| GET | `item_get`, `do_item_get`, `assoc_find` | hit 路径有哪些共享状态？ |
| 锁 | `item_lock`, `lru_locks`, `slabs_lock` | 每种锁保护什么？ |
| Worker | `thread_init`, `dispatch_conn_new`, `LIBEVENT_THREAD` | socket 如何分配到 worker？ |
| Event loop | `event_handler`, `drive_machine` | connection 状态如何推进？ |
| Extstore | `storage.c`, `extstore.c`, `ITEM_HDR` | RAM/SSD 各保存什么？ |
| Proxy | `proto_proxy.c`, `proxy_config.c` | 路由逻辑如何集中？ |

## 建议的源码实验

```bash
git clone https://github.com/memcached/memcached.git
cd memcached
git checkout 1.6.45

git grep -n "do_item_link"
git grep -n "assoc_find"
git grep -n "do_slabs_alloc"
git grep -n "lru_pull_tail"
git grep -n "dispatch_conn_new"
```

每次跟函数不要只抄调用树，建议维护下面这张表：

| 函数 | item 是否 linked | refcount | 持有锁 | Hash 变化 | LRU 变化 | Slab 变化 |
|---|---:|---:|---|---|---|---|
| 进入前 | | | | | | |
| 成功返回 | | | | | | |
| 失败返回 | | | | | | |
