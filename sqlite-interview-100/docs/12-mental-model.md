# SQLite 心智模型速查

```text
SQL
 ↓
Parser / Query Planner
 ↓
VDBE bytecode
 ↓
B-Tree (Table / Index)
 ↓
Pager + Page Cache
 ↓
Journal / WAL + File Locks
 ↓
VFS
 ↓
Operating System / Filesystem
```

## 并发模型

```text
Rollback Journal:
many readers -> writer 最终需要更强锁完成提交

WAL:
reader(snapshot) --\
reader(snapshot) ----+-- 可与 writer 重叠
writer ---------------/    但同时仍只有一个 writer
                     ↓
                    WAL
                     ↓ checkpoint
                  main database
```

## 索引设计公式

**Filter + Order + Cover**：等值过滤列 -> 范围/排序列 -> 必要输出列（covering candidate）。最后必须用真实 `EXPLAIN QUERY PLAN` 与数据分布验证。
