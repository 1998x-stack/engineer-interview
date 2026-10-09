# 附录 D · Redis 版本差异速览

| 版本 | 关键变化 | 面试影响 |
|---|---|---|
| Redis 5 / 6 | Streams 逐步成熟；Redis 6 引入 ACL、I/O threading 等。 | 传统高频题仍是底座，但不能把“Redis 单线程”绝对化。 |
| Redis 7.x | Functions、Multi-Part AOF 等成为重要生产知识点。 | 持久化与服务器端可编程的面试答案需要升级。 |
| Redis 8.0 | Search、JSON、Time Series、概率结构等整合进 Redis Open Source；Vector Set 进入新数据类型体系。 | “Redis 只有五大类型”的回答已经过时。 |
| Redis 8.8 | Array、INCREX、XNACK 等新能力。 | 数组、窗口计数、Stream pending 主动释放成为新版加分题。 |
| Redis 8.10 | Compact Hash、HIMPORT、BACKUP、LMOVEM/BLMOVEM、集合基数类命令等。 | 关注内存密度、批量导入与运维备份的新路径。 |

## 版本意识

面试回答应先说明“经典语义”再补“当前版本变化”。不要把新命令当作必须替代旧方案，也不要用 Redis 5/6 的知识断言 Redis 8.x 的能力边界。

当前仓库版本基线：**Redis Open Source 8.10.1（2026-08）**。
