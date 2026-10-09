# 第 7 章：文件系统与存储

> 打通 FD→VFS→dentry/inode→page cache→writeback→journal→durability。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q73](q73.md) | inode 是什么？文件名存在哪里？ | ★★★★★ | 基础 | `inode/dentry/metadata` |
| [Q74](q74.md) | open("/a/b/c") 大致发生什么？ | ★★★★★ | 高级 | `VFS/path-lookup/dentry/inode` |
| [Q75](q75.md) | File Descriptor 到底是什么？ | ★★★★★ | 基础 | `fd/file-description/inode` |
| [Q76](q76.md) | Hard Link 与 Symbolic Link 的区别？ | ★★★★★ | 基础 | `hard-link/symlink` |
| [Q77](q77.md) | Page Cache 是什么？为什么第二次读文件更快？ | ★★★★★ | 中等 | `page-cache/read/writeback` |
| [Q78](q78.md) | Buffered I/O 与 Direct I/O 如何取舍？ | ★★★★☆ | 高级 | `buffered-io/direct-io` |
| [Q79](q79.md) | write 返回后，数据一定落盘了吗？ | ★★★★★ | 中等 | `write/fsync/writeback` |
| [Q80](q80.md) | Journaling File System 为什么需要 Journal？ | ★★★★★ | 中等 | `journal/crash-consistency` |
| [Q81](q81.md) | ext4 data=ordered / writeback / journal 有何差异？ | ★★★★☆ | 高级 | `ext4/jbd2/data-mode` |
| [Q82](q82.md) | 为什么 rename 常用于原子文件更新？ | ★★★★★ | 高级 | `rename/fsync/atomic-update` |
| [Q83](q83.md) | 打开的文件被 rm 后为什么还能继续读？ | ★★★★★ | 中等 | `unlink/open-reference/link-count` |
| [Q84](q84.md) | RAID 0/1/5/6/10 的 trade-off？ | ★★★☆☆ | 中等 | `RAID/parity/redundancy` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
