# Publishing Checklist

在创建公开 GitHub Repository 之前建议完成：

- [ ] 替换仓库名、owner、description 与 topics。
- [ ] 根据实际用途选择代码/文档许可证；本包未替维护者做法律选择。
- [ ] 确认候选人面经只作为公开主题证据，不把内容表述成公司官方题库。
- [ ] 检查公司名称、商标、第三方书名与外部链接的使用方式。
- [ ] 运行 `python scripts/validate_repo.py`。
- [ ] 可选：`pip install -r requirements-docs.txt && mkdocs serve` 本地预览文档站。
- [ ] 在 GitHub Settings 中按需开启 Pages / Actions / Issues。
