# 存储结构 Lab

```sql
PRAGMA page_size;
PRAGMA page_count;
PRAGMA freelist_count;
```

插入大量小行和少量超大 TEXT/BLOB，比较 page_count；删除一半数据观察 freelist；执行 VACUUM 再观察文件大小。若构建启用 `dbstat`，进一步查看表/索引页分布。
