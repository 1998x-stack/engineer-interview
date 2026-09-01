# 源码阅读路线

不要从 `memcached.c` 第一行开始顺序读。按“对象 → 索引 → 内存 → 生命周期 → 并发 → 网络”走。

1. `memcached.h`：先掌握 `struct item`、flags、`ITEM_key/ITEM_data`。
2. `items.c`：追 `item_alloc/do_item_alloc`、`do_item_link/unlink`、LRU。
3. `slabs.c`：看 `slabs_clsid`、alloc/free、page/chunk/freelist。
4. `assoc.c`：看 `assoc_find/insert/delete` 与扩容。
5. `thread.c`：看 item lock、LRU lock、worker。
6. `proto_parser.c` + `proto_text.c`：把 `set foo` header/body 串起来。
7. `memcached.c`：最后再回看 connection state machine 与整体调度。
8. 高阶：`extstore.c`、`proto_proxy.c`、`proxy_*`。

## 推荐断点

```text
process_update_command
item_alloc / do_item_alloc
slabs_alloc
store_item / do_store_item
assoc_find / assoc_insert
do_item_link / do_item_unlink
item_link_q
```

每个断点记录 `item*`、`refcount`、`it_flags`、`slabs_clsid`、`h_next/next/prev`，你会看到一个 KV 的完整生命史。
