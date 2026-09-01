# Lab 04 · Stats Cheat Sheet

```bash
printf "stats\r\n" | nc 127.0.0.1 11211
printf "stats settings\r\n" | nc 127.0.0.1 11211
printf "stats slabs\r\n" | nc 127.0.0.1 11211
printf "stats items\r\n" | nc 127.0.0.1 11211
```

优先关注：`get_hits/get_misses`、`evictions/reclaimed`、`bytes/limit_maxbytes`、`curr_connections/listen_disabled_num` 以及每个 slab class 的 page/chunk/eviction。

采样累计 counter 时应计算时间差分和 rate。
