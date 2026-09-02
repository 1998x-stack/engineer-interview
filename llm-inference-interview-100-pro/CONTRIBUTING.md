# Contributing

欢迎修正文档、补充实验、增加版本差异说明。

## 原则

1. 不把匿名面经包装成可验证的“某公司原题”。
2. 新增事实尽量链接论文或官方文档。
3. 框架特性必须注明版本/日期或 commit。
4. 性能结论必须说明模型、硬件、workload 与 SLO。
5. 一个 PR 尽量只做一类修改。

提交前运行：

```bash
python scripts/verify_repo.py
```
