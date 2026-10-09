# 类型、Affinity 与 ROWID Lab

```sql
CREATE TABLE loose(x INTEGER, y VARCHAR(3));
INSERT INTO loose VALUES('123','abcdef'),('abc','xy');
SELECT x, typeof(x), y, typeof(y) FROM loose;

CREATE TABLE strict_t(x INTEGER, y ANY) STRICT;
INSERT INTO strict_t VALUES(123,'000123');
SELECT x, typeof(x), y, typeof(y) FROM strict_t;
```

再分别创建 `INTEGER PRIMARY KEY`、`INT PRIMARY KEY`、`WITHOUT ROWID` 表，用 `EXPLAIN QUERY PLAN` 比较主键查找路径。
