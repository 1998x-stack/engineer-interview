# Contributing

本仓库接受新题、纠错、示例和参考资料改进。目标是保持“可验证、可维护、不过度声称来源”。

## 提交新题

1. 使用 `templates/QUESTION_TEMPLATE.md`；
2. 一个问题一个 Markdown；
3. 标题必须是面试可直接提出的问题；
4. 30 秒答案必须能独立成立；
5. 深入部分必须说明机制和边界；
6. 至少给一个工程场景、一个验证方法和一个常见错误；
7. 实验涉及 CAN 发送/重放/故障注入时，只提供 `vcan`、SIL/HIL 或隔离台架方案。

## 来源规则

- 协议事实优先引用官方/标准组织/工具官方文档；
- 公开面经只用于“频度/题型”标记；
- 不把原创扩展写成某家公司逐字真题；
- 项目学习笔记与外部规范冲突时，不擅自替项目选择真值，应明确权威源待确认。

## 风格

推荐术语同时保留常用英文，例如 `Sample Point`、`Bus-Off`、`Acceptance Filter`。不要为了显得专业而堆缩写；第一次出现时说明职责。

## 提交前检查

```bash
python scripts/validate_repo.py
python scripts/build_index.py
python scripts/build_book.py
```
