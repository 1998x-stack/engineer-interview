# Lab 01 · Basic Text Protocol

```bash
memcached -p 11211 -m 64 -vv
```

另开终端：

```bash
printf "set foo 0 5 3\r\nbar\r\nget foo\r\n" | nc 127.0.0.1 11211
```

继续测试 `add`、`replace`、`delete`、`incr/decr`、TTL。记录服务端 `-vv` 输出与客户端响应的对应关系。
