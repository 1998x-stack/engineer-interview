# 运维与完整性 Lab

在数据库副本上执行：

```sql
PRAGMA quick_check;
PRAGMA integrity_check;
PRAGMA foreign_key_check;
PRAGMA freelist_count;
VACUUM INTO 'backup.db';
```

记录执行耗时、文件大小和 free pages。Migration Lab 应至少准备三个历史 schema fixture，并自动测试 v1→current、v2→current、vN-1→current。
