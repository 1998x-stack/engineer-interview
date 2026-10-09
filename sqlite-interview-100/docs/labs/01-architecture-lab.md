# 架构与连接行为 Lab

目标：验证“嵌入式、单文件、连接、事务”这些词在文件和 API 层实际意味着什么。

```bash
sqlite3 --version
sqlite3 lab.db "PRAGMA database_list; PRAGMA journal_mode; PRAGMA compile_options;"
ls -lh lab.db*
```

建议实验：分别创建文件数据库和 `:memory:` 数据库；打开两个进程连接同一文件；观察 journal/WAL 辅助文件的生命周期。
