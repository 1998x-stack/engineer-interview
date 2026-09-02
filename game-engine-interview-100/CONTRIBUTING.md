# Contributing

## 修改一道题

1. 保留 `PDF 核心内容（Source-derived）` 与 `专业扩展` 的边界。
2. 若修正 PDF 基线内容，请说明是“勘误”，不要静默覆盖来源。
3. 新增事实性主张优先引用官方文档、规范、论文或原始资料。
4. 性能结论必须说明平台/数据规模/测试方式，避免“永远更快”。
5. 运行 `python scripts/validate_repo.py`。

## PR 建议格式

- Problem：为什么改？
- Evidence：规范/官方文档/benchmark？
- Scope：影响哪几题？
- Validation：如何验证？
