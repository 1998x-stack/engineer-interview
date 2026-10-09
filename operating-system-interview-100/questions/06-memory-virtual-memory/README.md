# 第 6 章：内存与虚拟内存

> 打通 VA→TLB→Page Table→Page Fault→COW/Reclaim/Swap/OOM。

| 题号 | 题目 | 高频度 | 难度 | 标签 |
|---|---|---:|---|---|
| [Q56](q56.md) | 为什么需要 Virtual Memory？ | ★★★★★ | 基础 | `virtual-memory/isolation/demand-paging` |
| [Q57](q57.md) | Virtual Address 如何转换为 Physical Address？ | ★★★★★ | 基础 | `MMU/page-table/TLB` |
| [Q58](q58.md) | Paging 与 Segmentation 有什么区别？ | ★★★★★ | 基础 | `paging/segmentation/fragmentation` |
| [Q59](q59.md) | VA→PA 的页表项通常包含什么？ | ★★★★★ | 中等 | `PTE/present/permission` |
| [Q60](q60.md) | TLB 是什么？为什么必须有？ | ★★★★★ | 基础 | `TLB/translation-cache` |
| [Q61](q61.md) | 为什么 Page Table 要多级？ | ★★★★★ | 中等 | `multi-level-page-table/sparsity` |
| [Q62](q62.md) | Page Fault 发生后 OS 做什么？ | ★★★★★ | 中等 | `page-fault/fault-handler` |
| [Q63](q63.md) | Minor Page Fault 与 Major Page Fault 有何区别？ | ★★★★☆ | 中等 | `minor/major-fault` |
| [Q64](q64.md) | 什么是 Demand Paging？ | ★★★★★ | 基础 | `demand-paging/lazy-loading` |
| [Q65](q65.md) | Page Replacement 常见算法及真实系统差异？ | ★★★★★ | 中等 | `LRU/FIFO/Clock/MGLRU` |
| [Q66](q66.md) | 什么是 Belady’s Anomaly？ | ★★★★☆ | 中等 | `FIFO/Belady/stack-algorithm` |
| [Q67](q67.md) | 什么是 Thrashing？如何识别和缓解？ | ★★★★★ | 中等 | `thrashing/working-set/reclaim` |
| [Q68](q68.md) | COW 为什么一定通过 Page Fault 驱动？ | ★★★★★ | 中等 | `COW/protection-fault` |
| [Q69](q69.md) | mmap 是什么？为什么数据库/存储系统关心它？ | ★★★★★ | 中等 | `mmap/file-backed/page-cache` |
| [Q70](q70.md) | malloc 是 System Call 吗？底层如何向 OS 要内存？ | ★★★★★ | 中等 | `malloc/brk/mmap/allocator` |
| [Q71](q71.md) | Internal 与 External Fragmentation 的区别？ | ★★★★★ | 基础 | `fragmentation` |
| [Q72](q72.md) | Buddy Allocator 与 Slab/SLUB 分别解决什么？ | ★★★★☆ | 高级 | `buddy/slub/kernel-memory` |

## 本章建议学习法

1. 先按顺序完成题目，建立概念依赖。
2. 第二轮只看标题，做 60 秒口述。
3. 第三轮从任意题的“追问”继续向下展开，直到能跨题连接。
4. 最后一轮用 Linux 工具验证至少 2-3 个机制，而不是只读文字。

[← 返回总目录](../../README.md)
