# V2 Deep-Dive Enrichment Report

本报告记录第二轮“逐题专业化扩写”的结果。

## 覆盖范围

- 题目 Markdown：**100 / 100**
- 题号连续性：**Q01-Q100 完整**
- 平均单题体积：**7.4 KiB**
- 最小/最大单题：**6.8 / 8.9 KiB**
- 100 题 Markdown 总字符字节量：**761,516 bytes**
- 平均单题行数：**298 行**
- 总行数：**29,834 行**

## 每题新增的专业层

1. **机制级推演**：把定义改写成状态机/调用链。
2. **性能模型**：拆分 CPU、Cache/TLB、调度/等待、I/O/持久化成本。
3. **Linux 对象导航**：标出关键内核对象、接口和状态承载位置。
4. **边界条件与反例**：明确“机制保证什么、不保证什么”。
5. **高级追问树**：从定义继续追到慢路径、生产验证、不同硬件/容器环境。
6. **可复现实验**：提供 perf/strace/proc/cgroup/PSI/小程序实验入口。
7. **五级评分 Rubric**：从基础定义到系统级实现与证据。
8. **90 秒高级回答**：形成可直接口述的完整因果链。
9. **实验设计方法**：Hypothesis → Variable → Observation → Falsification。
10. **官方资料**：优先指向 Linux Kernel docs 与 man-pages。

## 重点增强示例

- Q17：`fork → COW PTE → protection fault → copy → update PTE → retry`。
- Q32：从 CFS 的传统 `vruntime` 直觉延伸到 EEVDF 的 eligibility / virtual deadline。
- Q41：区分 atomicity、visibility、ordering，明确 acquire/release 与 happens-before。
- Q47：futex 用户态 fast path 与内核 wait/wake slow path。
- Q57/Q60/Q62：打通 `VA → TLB → page-table walk → page fault`，并明确 TLB miss ≠ page fault。
- Q74/Q75：打通 `fdtable → struct file → dentry → inode`。
- Q79/Q82：区分可见性、原子 rename 与 crash durability，补 `fsync(file) + fsync(dir)`。
- Q87-Q90：从 readiness 模型的 epoll 到 completion-oriented io_uring。
- Q93-Q97：namespace / cgroup / user namespace / overcommit / OOM。
- Q98-Q100：形成 CPU、scheduler、lock、memory、storage、network、cgroup、PSI 的证据驱动排障树。

## 新增学习材料

- [`guides/kernel-source-reading-map.md`](guides/kernel-source-reading-map.md)：把 100 题映射到 Linux Kernel 源码子系统与阅读顺序。

## 自动质量检查

`scripts/validate_repo.py` 检查：

- 100 道题是否齐全；
- Q01-Q100 是否连续；
- YAML frontmatter 是否存在；
- Markdown 内部链接是否失效。

此外本轮额外检查每题：

- V2 deep-dive block 恰好 1 份；
- Markdown fenced code block 成对闭合；
- `edition: 2.0-deep-dive` 元数据存在；
- 9.2-9.11 深度章节全部存在。
